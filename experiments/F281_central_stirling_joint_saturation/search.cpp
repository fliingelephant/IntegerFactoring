#include <gmpxx.h>

extern "C" {
#include <flint/flint.h>
#include <flint/ulong_extras.h>
}

#include <algorithm>
#include <array>
#include <atomic>
#include <cerrno>
#include <chrono>
#include <cmath>
#include <cstdint>
#include <filesystem>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <limits>
#include <numeric>
#include <sstream>
#include <stdexcept>
#include <string>
#include <system_error>
#include <thread>
#include <tuple>
#include <utility>
#include <vector>

#include <sys/resource.h>
#include <sys/types.h>
#include <unistd.h>

namespace fs = std::filesystem;

namespace {

constexpr const char *VERSION = "F281-D01";
constexpr std::uint64_t MAX_EXACT_S = 16000;
constexpr std::uint64_t MAX_OFFSET_S = 300000;
constexpr std::uint64_t MAX_OFFSET_H = 64;
constexpr std::uint64_t MAX_WORKERS = 8;
constexpr std::uint64_t DELTA_TELEMETRY_CAP = 512;
constexpr std::uint64_t ADDRESS_SPACE_BYTES = UINT64_C(4294967296);
constexpr std::uint64_t FILE_SIZE_BYTES = UINT64_C(536870912);
constexpr std::uint64_t OUTPUT_RESERVATION_BYTES = UINT64_C(268435456);
constexpr std::uint64_t MIN_FREE_DISK_BYTES = UINT64_C(536870912);

[[noreturn]] void fail(const std::string &message) {
    throw std::runtime_error(message);
}

void require(bool condition, const std::string &message) {
    if (!condition) fail(message);
}

std::uint64_t parse_u64(const char *text, const char *name) {
    require(text != nullptr && *text != '\0', std::string("missing ") + name);
    std::size_t used = 0;
    const std::string value(text);
    unsigned long long parsed = 0;
    try {
        parsed = std::stoull(value, &used, 10);
    } catch (const std::exception &) {
        fail(std::string("invalid ") + name);
    }
    require(used == value.size(), std::string("invalid ") + name);
    return static_cast<std::uint64_t>(parsed);
}

std::vector<std::string> split_tsv(const std::string &line) {
    std::vector<std::string> fields;
    std::size_t begin = 0;
    while (true) {
        const std::size_t tab = line.find('\t', begin);
        if (tab == std::string::npos) {
            fields.push_back(line.substr(begin));
            return fields;
        }
        fields.push_back(line.substr(begin, tab - begin));
        begin = tab + 1;
    }
}

void prepare_output_dir(const fs::path &path) {
    require(!path.empty(), "empty output path");
    require(!fs::exists(path), "output path already exists: " + path.string());
    require(fs::create_directories(path), "cannot create output path");
    const fs::space_info space = fs::space(path);
    require(space.available >= MIN_FREE_DISK_BYTES, "insufficient free disk");
}

void write_done(const fs::path &path, const std::string &mode) {
    std::ofstream out(path / "DONE", std::ios::binary | std::ios::trunc);
    require(static_cast<bool>(out), "cannot open DONE");
    out << "version\tmode\tstatus\n" << VERSION << '\t' << mode << "\tCLOSED\n";
    out.flush();
    require(static_cast<bool>(out), "cannot close DONE");
}

std::uint64_t maxrss_kib() {
    struct rusage usage {};
    require(getrusage(RUSAGE_SELF, &usage) == 0, "getrusage failed");
    return static_cast<std::uint64_t>(usage.ru_maxrss);
}

void require_one_limit(int resource, rlim_t exact, const char *name) {
    struct rlimit limit {};
    require(getrlimit(resource, &limit) == 0, std::string("getrlimit failed: ") + name);
    require(limit.rlim_cur == exact && limit.rlim_max == exact,
            std::string("wrong soft/hard limit: ") + name);
}

void require_bounded_limit(int resource, rlim_t minimum, rlim_t maximum,
                           const char *name) {
    struct rlimit limit {};
    require(getrlimit(resource, &limit) == 0, std::string("getrlimit failed: ") + name);
    require(limit.rlim_cur >= minimum && limit.rlim_cur <= maximum,
            std::string("wrong soft limit: ") + name);
    require(limit.rlim_max >= minimum && limit.rlim_max <= maximum,
            std::string("wrong hard limit: ") + name);
}

void require_runtime_limits() {
    require(sizeof(unsigned long) == 8, "target must have 64-bit unsigned long");
    require_one_limit(RLIMIT_AS, static_cast<rlim_t>(ADDRESS_SPACE_BYTES), "RLIMIT_AS");
    require_one_limit(RLIMIT_CORE, 0, "RLIMIT_CORE");
    require_bounded_limit(RLIMIT_FSIZE, UINT64_C(67108864),
                          static_cast<rlim_t>(FILE_SIZE_BYTES), "RLIMIT_FSIZE");
    require_bounded_limit(RLIMIT_NOFILE, 32, 128, "RLIMIT_NOFILE");
#ifdef RLIMIT_NPROC
    require_bounded_limit(RLIMIT_NPROC, 8, 64, "RLIMIT_NPROC");
#endif
    errno = 0;
    int priority = getpriority(PRIO_PROCESS, 0);
    require(errno == 0, "getpriority failed");
    if (priority < 15) {
        require(setpriority(PRIO_PROCESS, 0, 15) == 0, "setpriority failed");
        errno = 0;
        priority = getpriority(PRIO_PROCESS, 0);
        require(errno == 0 && priority >= 15, "niceness readback failed");
    }
}

struct Fnv64 {
    std::uint64_t value = UINT64_C(1469598103934665603);

    void add_u64(std::uint64_t x) {
        for (unsigned i = 0; i < 8; ++i) {
            value ^= static_cast<unsigned char>(x & 0xffU);
            value *= UINT64_C(1099511628211);
            x >>= 8U;
        }
    }

    void add_mpz_shape(const mpz_class &x) {
        add_u64(static_cast<std::uint64_t>(mpz_sizeinbase(x.get_mpz_t(), 2)));
        add_u64(static_cast<std::uint64_t>(mpz_fdiv_ui(x.get_mpz_t(), 1000000007UL)));
        add_u64(static_cast<std::uint64_t>(mpz_fdiv_ui(x.get_mpz_t(), 1000000009UL)));
    }
};

std::string hex_u64(std::uint64_t value) {
    std::ostringstream out;
    out << std::hex << std::setw(16) << std::setfill('0') << value;
    return out.str();
}

std::uint64_t used_limb_bytes(const std::vector<mpz_class> &row) {
    unsigned __int128 total = 0;
    for (const mpz_class &value : row) {
        total += static_cast<unsigned long>(mpz_size(value.get_mpz_t())) * sizeof(mp_limb_t);
    }
    require(total <= std::numeric_limits<std::uint64_t>::max(), "limb byte overflow");
    return static_cast<std::uint64_t>(total);
}

std::vector<std::uint32_t> primes_through(std::uint64_t bound) {
    require(bound <= std::numeric_limits<std::uint32_t>::max(), "sieve bound too large");
    std::vector<bool> composite(static_cast<std::size_t>(bound + 1), false);
    std::vector<std::uint32_t> primes;
    for (std::uint64_t n = 2; n <= bound; ++n) {
        if (!composite[static_cast<std::size_t>(n)]) {
            primes.push_back(static_cast<std::uint32_t>(n));
            if (n <= bound / n) {
                for (std::uint64_t multiple = n * n; multiple <= bound; multiple += n)
                    composite[static_cast<std::size_t>(multiple)] = true;
            }
        }
    }
    return primes;
}

struct StripResult {
    mpz_class residual;
    std::uint64_t primes_tested = 0;
    std::uint64_t valuations_removed = 0;
};

StripResult strip_small_primes(const mpz_class &input, std::uint64_t bound,
                               const std::vector<std::uint32_t> &primes) {
    StripResult result;
    result.residual = input;
    mpz_class factor;
    for (std::uint32_t prime : primes) {
        if (prime > bound) break;
        ++result.primes_tested;
        mpz_set_ui(factor.get_mpz_t(), prime);
        const mp_bitcnt_t removed =
            mpz_remove(result.residual.get_mpz_t(), result.residual.get_mpz_t(),
                       factor.get_mpz_t());
        result.valuations_removed += static_cast<std::uint64_t>(removed);
    }
    return result;
}

std::vector<mpz_class> second_row_exact(std::uint64_t n) {
    std::vector<mpz_class> row(static_cast<std::size_t>(n + 1));
    row[0] = 1;
    for (std::uint64_t level = 1; level <= n; ++level) {
        for (std::uint64_t k = level; k >= 1; --k) {
            mpz_mul_ui(row[static_cast<std::size_t>(k)].get_mpz_t(),
                       row[static_cast<std::size_t>(k)].get_mpz_t(),
                       static_cast<unsigned long>(k));
            mpz_add(row[static_cast<std::size_t>(k)].get_mpz_t(),
                    row[static_cast<std::size_t>(k)].get_mpz_t(),
                    row[static_cast<std::size_t>(k - 1)].get_mpz_t());
        }
        row[0] = 0;
    }
    return row;
}

std::vector<mpz_class> first_row_exact(std::uint64_t n) {
    std::vector<mpz_class> row(static_cast<std::size_t>(n + 1));
    row[0] = 1;
    for (std::uint64_t level = 1; level <= n; ++level) {
        for (std::uint64_t k = level; k >= 1; --k) {
            mpz_mul_ui(row[static_cast<std::size_t>(k)].get_mpz_t(),
                       row[static_cast<std::size_t>(k)].get_mpz_t(),
                       static_cast<unsigned long>(level - 1));
            mpz_add(row[static_cast<std::size_t>(k)].get_mpz_t(),
                    row[static_cast<std::size_t>(k)].get_mpz_t(),
                    row[static_cast<std::size_t>(k - 1)].get_mpz_t());
        }
        mpz_mul_ui(row[0].get_mpz_t(), row[0].get_mpz_t(),
                   static_cast<unsigned long>(level - 1));
    }
    return row;
}

mpz_class complete_h_exact(std::uint64_t variables, std::uint64_t degree) {
    std::vector<mpz_class> h(static_cast<std::size_t>(degree + 1));
    h[0] = 1;
    for (std::uint64_t x = 1; x <= variables; ++x) {
        for (std::uint64_t d = 1; d <= degree; ++d)
            h[static_cast<std::size_t>(d)] +=
                x * h[static_cast<std::size_t>(d - 1)];
    }
    return h[static_cast<std::size_t>(degree)];
}

std::uint64_t mul_mod(std::uint64_t a, std::uint64_t b, std::uint64_t modulus) {
    return static_cast<std::uint64_t>((static_cast<unsigned __int128>(a) * b) % modulus);
}

std::uint64_t pow_mod(std::uint64_t base, std::uint64_t exponent,
                      std::uint64_t modulus) {
    std::uint64_t result = 1 % modulus;
    base %= modulus;
    while (exponent != 0) {
        if (exponent & 1U) result = mul_mod(result, base, modulus);
        exponent >>= 1U;
        if (exponent != 0) base = mul_mod(base, base, modulus);
    }
    return result;
}

std::uint64_t add_mod(std::uint64_t a, std::uint64_t b, std::uint64_t modulus) {
    const unsigned __int128 sum = static_cast<unsigned __int128>(a) + b;
    return static_cast<std::uint64_t>(sum % modulus);
}

std::uint64_t sub_mod(std::uint64_t a, std::uint64_t b, std::uint64_t modulus) {
    return a >= b ? a - b : modulus - (b - a);
}

std::uint64_t second_mod_prime(std::uint64_t n, std::uint64_t k,
                               std::uint64_t prime) {
    require(k < prime, "second_mod_prime needs k<p");
    std::vector<std::uint64_t> inverse(static_cast<std::size_t>(k + 1));
    if (k >= 1) inverse[1] = 1;
    for (std::uint64_t j = 2; j <= k; ++j) {
        const std::uint64_t product =
            mul_mod(prime / j, inverse[static_cast<std::size_t>(prime % j)], prime);
        inverse[static_cast<std::size_t>(j)] = product == 0 ? 0 : prime - product;
    }
    std::uint64_t combination = 1;
    std::uint64_t numerator = 0;
    std::uint64_t factorial = 1;
    for (std::uint64_t j = 0; j <= k; ++j) {
        const std::uint64_t term = mul_mod(combination, pow_mod(j, n, prime), prime);
        if ((k - j) & 1U)
            numerator = sub_mod(numerator, term, prime);
        else
            numerator = add_mod(numerator, term, prime);
        if (j < k) {
            combination = mul_mod(combination, k - j, prime);
            combination = mul_mod(combination, inverse[static_cast<std::size_t>(j + 1)], prime);
            factorial = mul_mod(factorial, j + 1, prime);
        }
    }
    return mul_mod(numerator, pow_mod(factorial, prime - 2, prime), prime);
}

mpz_class second_mod_composite(std::uint64_t n, std::uint64_t k,
                               const mpz_class &modulus) {
    require(modulus > 1, "bad composite modulus");
    mpz_class sum = 0;
    mpz_class combination = 1;
    mpz_class base;
    mpz_class power;
    mpz_class term;
    for (std::uint64_t j = 0; j <= k; ++j) {
        mpz_set_ui(base.get_mpz_t(), static_cast<unsigned long>(j));
        mpz_powm_ui(power.get_mpz_t(), base.get_mpz_t(),
                    static_cast<unsigned long>(n), modulus.get_mpz_t());
        mpz_mul(term.get_mpz_t(), power.get_mpz_t(), combination.get_mpz_t());
        mpz_mod(term.get_mpz_t(), term.get_mpz_t(), modulus.get_mpz_t());
        if ((k - j) & 1U)
            sum -= term;
        else
            sum += term;
        mpz_mod(sum.get_mpz_t(), sum.get_mpz_t(), modulus.get_mpz_t());
        if (j < k) {
            combination *= (k - j);
            mpz_divexact_ui(combination.get_mpz_t(), combination.get_mpz_t(),
                            static_cast<unsigned long>(j + 1));
        }
    }
    mpz_class factorial;
    mpz_fac_ui(factorial.get_mpz_t(), static_cast<unsigned long>(k));
    mpz_mod(factorial.get_mpz_t(), factorial.get_mpz_t(), modulus.get_mpz_t());
    mpz_class inverse;
    require(mpz_invert(inverse.get_mpz_t(), factorial.get_mpz_t(),
                       modulus.get_mpz_t()) != 0,
            "factorial is not invertible in replay");
    mpz_mul(sum.get_mpz_t(), sum.get_mpz_t(), inverse.get_mpz_t());
    mpz_mod(sum.get_mpz_t(), sum.get_mpz_t(), modulus.get_mpz_t());
    return sum;
}

std::vector<std::uint64_t> first_row_mod(std::uint64_t n, std::uint64_t max_k,
                                         std::uint64_t modulus) {
    std::vector<std::uint64_t> row(static_cast<std::size_t>(max_k + 1));
    row[0] = 1;
    for (std::uint64_t level = 1; level <= n; ++level) {
        const std::uint64_t top = std::min(level, max_k);
        for (std::uint64_t k = top; k >= 1; --k) {
            row[static_cast<std::size_t>(k)] = add_mod(
                row[static_cast<std::size_t>(k - 1)],
                mul_mod((level - 1) % modulus, row[static_cast<std::size_t>(k)], modulus),
                modulus);
        }
        row[0] = mul_mod(row[0], (level - 1) % modulus, modulus);
    }
    return row;
}

std::uint64_t second_exact_mod(std::uint64_t n, std::uint64_t k,
                               std::uint64_t modulus) {
    const std::vector<mpz_class> row = second_row_exact(n);
    return static_cast<std::uint64_t>(
        mpz_fdiv_ui(row[static_cast<std::size_t>(k)].get_mpz_t(),
                    static_cast<unsigned long>(modulus)));
}

mpz_class finite_difference_polynomial(std::uint64_t m, long x) {
    const std::uint64_t exponent = 2 * m + 3;
    mpz_class sum = 0;
    mpz_class binomial;
    mpz_class base;
    mpz_class power;
    for (std::uint64_t j = 0; j <= m; ++j) {
        mpz_bin_uiui(binomial.get_mpz_t(), static_cast<unsigned long>(m),
                     static_cast<unsigned long>(j));
        mpz_set_si(base.get_mpz_t(), x + static_cast<long>(j));
        mpz_pow_ui(power.get_mpz_t(), base.get_mpz_t(),
                   static_cast<unsigned long>(exponent));
        power *= binomial;
        if ((m - j) & 1U)
            sum -= power;
        else
            sum += power;
    }
    return sum;
}

struct DeltaTelemetry {
    mpz_class scaled_gcd;
    mpz_class delta;
    mpz_class ratio;
    mpz_class support_residual;
    bool ratio_divides_2s = false;
};

DeltaTelemetry delta_telemetry(const std::vector<mpz_class> &row,
                               std::uint64_t s,
                               const std::vector<std::uint32_t> &primes) {
    const std::uint64_t n = 2 * s + 1;
    const std::uint64_t m = s - 1;
    require(n < row.size(), "incomplete row for Delta telemetry");
    mpz_class factorial_m;
    mpz_fac_ui(factorial_m.get_mpz_t(), static_cast<unsigned long>(m));
    mpz_class left = factorial_m * row[static_cast<std::size_t>(m)];
    mpz_class factorial_s = factorial_m * s;
    mpz_class right = factorial_s * row[static_cast<std::size_t>(s)];
    DeltaTelemetry result;
    mpz_gcd(result.scaled_gcd.get_mpz_t(), left.get_mpz_t(), right.get_mpz_t());

    mpz_class factorial = 1;
    mpz_class term;
    result.delta = 0;
    for (std::uint64_t k = 1; k <= n; ++k) {
        factorial *= k;
        if (k < m) continue;
        term = factorial * row[static_cast<std::size_t>(k)];
        mpz_gcd(result.delta.get_mpz_t(), result.delta.get_mpz_t(), term.get_mpz_t());
    }
    require(result.delta > 0, "zero fixed divisor");
    require(mpz_divisible_p(result.scaled_gcd.get_mpz_t(), result.delta.get_mpz_t()) != 0,
            "Delta does not divide scaled gcd");
    mpz_divexact(result.ratio.get_mpz_t(), result.scaled_gcd.get_mpz_t(),
                 result.delta.get_mpz_t());
    mpz_class two_s = 2 * s;
    result.ratio_divides_2s =
        mpz_divisible_p(two_s.get_mpz_t(), result.ratio.get_mpz_t()) != 0;
    result.support_residual = strip_small_primes(result.ratio, n, primes).residual;
    return result;
}

bool power_of_two(std::uint64_t value) {
    return value != 0 && (value & (value - 1)) == 0;
}

void reserve_decimal_output(const fs::path &dir,
                            const std::vector<const mpz_class *> &values) {
    unsigned __int128 digits = 4096;
    for (const mpz_class *value : values)
        digits += mpz_sizeinbase(value->get_mpz_t(), 10) + 1;
    require(digits <= OUTPUT_RESERVATION_BYTES, "witness output reservation exceeded");
    const fs::space_info space = fs::space(dir);
    require(space.available >= static_cast<std::uint64_t>(digits) + MIN_FREE_DISK_BYTES,
            "witness disk reservation failed");
}

struct LaneResult {
    std::string status;
    std::uint64_t tested = 0;
    std::uint64_t witnesses = 0;
    std::uint64_t used_limbs = 0;
    std::uint64_t elapsed_ns = 0;
};

LaneResult run_exact_lane(std::uint64_t max_s, const fs::path &out_dir) {
    require(max_s >= 1 && max_s <= MAX_EXACT_S, "exact max_s out of range");
    prepare_output_dir(out_dir);
    const auto started = std::chrono::steady_clock::now();
    const std::vector<std::uint32_t> primes = primes_through(2 * max_s + 1);
    std::vector<mpz_class> row(static_cast<std::size_t>(max_s + 1));
    row[0] = 1;
    mpz_class support_lcm = 1;
    mpz_class gcd;
    Fnv64 trace;
    std::uint64_t updates = 0;
    std::uint64_t strip_prime_tests = 0;
    std::uint64_t stripped_valuations = 0;
    std::uint64_t individual_a_zero = 0;
    std::uint64_t individual_b_zero = 0;
    std::uint64_t telemetry_rows = 0;
    std::uint64_t ratio_divides_false = 0;
    std::uint64_t ratio_support_nonunit = 0;
    LaneResult result;
    result.status = "PASS";

    std::ofstream checkpoints(out_dir / "checkpoints.tsv", std::ios::binary);
    std::ofstream telemetry(out_dir / "telemetry.tsv", std::ios::binary);
    std::ofstream witness(out_dir / "witness.tsv", std::ios::binary);
    require(checkpoints && telemetry && witness, "cannot open exact outputs");
    checkpoints << "version\tlane\ts\tn\tA_bits\tB_bits\tgcd_bits\ttrace_hash\n";
    telemetry << "version\ts\tn\tA_bits\tB_bits\tG_bits\tDelta_bits\tratio"
                 "\tratio_divides_2s\tratio_support_residual\n";
    witness << "version\tlane\ts\tn\tbound\tA\tB\tgcd\tresidual\tsupport_lcm"
               "\tgcd_residual_support\tdivides_A\tdivides_B\tstripped_valuations\n";

    const std::uint64_t max_n = 2 * max_s + 1;
    for (std::uint64_t n = 1; n <= max_n; ++n) {
        const std::uint64_t top = std::min(n, max_s);
        for (std::uint64_t k = top; k >= 1; --k) {
            mpz_mul_ui(row[static_cast<std::size_t>(k)].get_mpz_t(),
                       row[static_cast<std::size_t>(k)].get_mpz_t(),
                       static_cast<unsigned long>(k));
            mpz_add(row[static_cast<std::size_t>(k)].get_mpz_t(),
                    row[static_cast<std::size_t>(k)].get_mpz_t(),
                    row[static_cast<std::size_t>(k - 1)].get_mpz_t());
            ++updates;
        }
        row[0] = 0;
        mpz_lcm_ui(support_lcm.get_mpz_t(), support_lcm.get_mpz_t(),
                   static_cast<unsigned long>(n));
        if ((n & 1U) == 0 || n < 3) continue;
        const std::uint64_t s = (n - 1) / 2;
        if (s > max_s) continue;
        const mpz_class &a = row[static_cast<std::size_t>(s)];
        const mpz_class &b = row[static_cast<std::size_t>(s - 1)];
        mpz_gcd(gcd.get_mpz_t(), a.get_mpz_t(), b.get_mpz_t());
        const StripResult stripped = strip_small_primes(gcd, n, primes);
        strip_prime_tests += stripped.primes_tested;
        stripped_valuations += stripped.valuations_removed;
        ++result.tested;
        trace.add_u64(s);
        trace.add_mpz_shape(a);
        trace.add_mpz_shape(b);
        trace.add_mpz_shape(gcd);
        if (a == 0) ++individual_a_zero;
        if (b == 0) ++individual_b_zero;

        if (n <= max_s && s <= DELTA_TELEMETRY_CAP) {
            const DeltaTelemetry item = delta_telemetry(row, s, primes);
            ++telemetry_rows;
            if (!item.ratio_divides_2s) ++ratio_divides_false;
            if (item.support_residual != 1) ++ratio_support_nonunit;
            telemetry << VERSION << '\t' << s << '\t' << n << '\t'
                      << mpz_sizeinbase(a.get_mpz_t(), 2) << '\t'
                      << mpz_sizeinbase(b.get_mpz_t(), 2) << '\t'
                      << mpz_sizeinbase(item.scaled_gcd.get_mpz_t(), 2) << '\t'
                      << mpz_sizeinbase(item.delta.get_mpz_t(), 2) << '\t'
                      << item.ratio.get_str() << '\t'
                      << (item.ratio_divides_2s ? 1 : 0) << '\t'
                      << item.support_residual.get_str() << '\n';
        }

        if (power_of_two(s) || s == max_s) {
            checkpoints << VERSION << "\texact\t" << s << '\t' << n << '\t'
                        << mpz_sizeinbase(a.get_mpz_t(), 2) << '\t'
                        << mpz_sizeinbase(b.get_mpz_t(), 2) << '\t'
                        << mpz_sizeinbase(gcd.get_mpz_t(), 2) << '\t'
                        << hex_u64(trace.value) << '\n';
        }

        if (stripped.residual != 1) {
            mpz_class support_gcd;
            mpz_gcd(support_gcd.get_mpz_t(), stripped.residual.get_mpz_t(),
                    support_lcm.get_mpz_t());
            const bool divides_a =
                mpz_divisible_p(a.get_mpz_t(), stripped.residual.get_mpz_t()) != 0;
            const bool divides_b =
                mpz_divisible_p(b.get_mpz_t(), stripped.residual.get_mpz_t()) != 0;
            require(support_gcd == 1 && divides_a && divides_b,
                    "invalid exact residual certificate");
            reserve_decimal_output(out_dir,
                                   {&a, &b, &gcd, &stripped.residual, &support_lcm});
            witness << VERSION << "\texact\t" << s << '\t' << n << '\t' << n << '\t'
                    << a.get_str() << '\t' << b.get_str() << '\t' << gcd.get_str() << '\t'
                    << stripped.residual.get_str() << '\t' << support_lcm.get_str() << '\t'
                    << support_gcd.get_str() << '\t' << (divides_a ? 1 : 0) << '\t'
                    << (divides_b ? 1 : 0) << '\t' << stripped.valuations_removed << '\n';
            result.status = "COUNTEREXAMPLE";
            result.witnesses = 1;
            break;
        }
    }

    checkpoints.flush();
    telemetry.flush();
    witness.flush();
    require(checkpoints && telemetry && witness, "cannot close exact outputs");
    result.used_limbs = used_limb_bytes(row);
    result.elapsed_ns = static_cast<std::uint64_t>(
        std::chrono::duration_cast<std::chrono::nanoseconds>(
            std::chrono::steady_clock::now() - started).count());

    std::ofstream summary(out_dir / "summary.tsv", std::ios::binary);
    require(summary, "cannot open exact summary");
    summary << "version\tlane\tmax_s\tmax_h\ttested\tstatus\twitnesses\tupdates"
               "\tprime_strip_tests\tstripped_valuations\tindividual_a_zero"
               "\tindividual_b_zero\ttelemetry_rows\tratio_divides_2s_false"
               "\tratio_support_residual_nonunit\ttrace_hash\tlimb_bytes"
               "\tmaxrss_kib\telapsed_ns\n";
    summary << VERSION << "\texact\t" << max_s << "\t0\t" << result.tested << '\t'
            << result.status << '\t' << result.witnesses << '\t' << updates << '\t'
            << strip_prime_tests << '\t' << stripped_valuations << '\t'
            << individual_a_zero << '\t' << individual_b_zero << '\t'
            << telemetry_rows << '\t' << ratio_divides_false << '\t'
            << ratio_support_nonunit << '\t' << hex_u64(trace.value) << '\t'
            << result.used_limbs << '\t' << maxrss_kib() << '\t' << result.elapsed_ns << '\n';
    summary.flush();
    require(summary, "cannot close exact summary");
    write_done(out_dir, "exact");
    return result;
}

LaneResult run_offset_lane(std::uint64_t max_s, std::uint64_t max_h,
                           const fs::path &out_dir) {
    require(max_s >= 1 && max_s <= MAX_OFFSET_S, "offset max_s out of range");
    require(max_h >= 1 && max_h <= MAX_OFFSET_H, "offset max_h out of range");
    prepare_output_dir(out_dir);
    const auto started = std::chrono::steady_clock::now();
    const std::uint64_t max_n = max_s + 2 * max_h + 1;
    const std::uint64_t max_t = max_s + max_h;
    require(2 * max_t + 1 <= std::numeric_limits<unsigned long>::max(),
            "offset prime exceeds FLINT word");
    std::vector<unsigned char> prime_cache(static_cast<std::size_t>(max_t + 1));
    for (std::uint64_t t = 1; t <= max_t; ++t) {
        const unsigned long candidate = static_cast<unsigned long>(2 * t + 1);
        prime_cache[static_cast<std::size_t>(t)] =
            static_cast<unsigned char>(n_is_prime(candidate) != 0);
    }

    std::vector<mpz_class> row(static_cast<std::size_t>(2 * max_h + 1));
    row[0] = 1;
    std::vector<std::uint64_t> candidates(static_cast<std::size_t>(max_h + 1));
    std::vector<std::uint64_t> even_zero(static_cast<std::size_t>(max_h + 1));
    std::vector<std::uint64_t> odd_zero(static_cast<std::size_t>(max_h + 1));
    std::uint64_t updates = 0;
    std::uint64_t prime_pairs = 0;
    std::uint64_t individual_even_zero = 0;
    std::uint64_t individual_odd_zero = 0;
    Fnv64 trace;
    LaneResult result;
    result.status = "PASS";

    std::ofstream checkpoints(out_dir / "checkpoints.tsv", std::ios::binary);
    std::ofstream telemetry(out_dir / "telemetry.tsv", std::ios::binary);
    std::ofstream witness(out_dir / "witness.tsv", std::ios::binary);
    require(checkpoints && telemetry && witness, "cannot open offset outputs");
    checkpoints << "version\tlane\tn\tlast_s\tprime_pairs\teven_zero\todd_zero"
                   "\ttrace_hash\n";
    telemetry << "version\th\tprime_pairs\tc_n_2h_zero\tc_n_2h_minus_1_zero\n";
    witness << "version\tlane\ts\th\tp\tn\tc_n_2h\tc_n_2h_minus_1"
               "\trem_2h\trem_2h_minus_1\tflint_prime\treplay_A\treplay_B\n";

    bool stop = false;
    for (std::uint64_t n = 1; n <= max_n && !stop; ++n) {
        const std::uint64_t top = std::min(n, 2 * max_h);
        for (std::uint64_t k = top; k >= 1; --k) {
            mpz_mul_ui(row[static_cast<std::size_t>(k)].get_mpz_t(),
                       row[static_cast<std::size_t>(k)].get_mpz_t(),
                       static_cast<unsigned long>(n - 1));
            mpz_add(row[static_cast<std::size_t>(k)].get_mpz_t(),
                    row[static_cast<std::size_t>(k)].get_mpz_t(),
                    row[static_cast<std::size_t>(k - 1)].get_mpz_t());
            ++updates;
        }
        mpz_mul_ui(row[0].get_mpz_t(), row[0].get_mpz_t(),
                   static_cast<unsigned long>(n - 1));

        for (std::uint64_t h = 1; h <= max_h; ++h) {
            if (n <= 2 * h + 1) continue;
            const std::uint64_t s = n - 2 * h - 1;
            if (s > max_s) continue;
            const std::uint64_t t = s + h;
            if (!prime_cache[static_cast<std::size_t>(t)]) continue;
            const std::uint64_t p = 2 * t + 1;
            ++prime_pairs;
            ++candidates[static_cast<std::size_t>(h)];
            const std::uint64_t rem_even = static_cast<std::uint64_t>(
                mpz_fdiv_ui(row[static_cast<std::size_t>(2 * h)].get_mpz_t(),
                            static_cast<unsigned long>(p)));
            const std::uint64_t rem_odd = static_cast<std::uint64_t>(
                mpz_fdiv_ui(row[static_cast<std::size_t>(2 * h - 1)].get_mpz_t(),
                            static_cast<unsigned long>(p)));
            if (rem_even == 0) {
                ++individual_even_zero;
                ++even_zero[static_cast<std::size_t>(h)];
            }
            if (rem_odd == 0) {
                ++individual_odd_zero;
                ++odd_zero[static_cast<std::size_t>(h)];
            }
            trace.add_u64(s);
            trace.add_u64(h);
            trace.add_u64(p);
            trace.add_u64(rem_even);
            trace.add_u64(rem_odd);
            ++result.tested;
            if (rem_even == 0 && rem_odd == 0) {
                require(n_is_prime(static_cast<unsigned long>(p)) != 0,
                        "FLINT prime replay failed");
                require(p > 2 * s + 1, "offset witness is not above boundary");
                const std::uint64_t replay_a = second_mod_prime(2 * s + 1, s, p);
                const std::uint64_t replay_b = second_mod_prime(2 * s + 1, s - 1, p);
                require(replay_a == 0 && replay_b == 0,
                        "offset complement failed independent replay");
                const mpz_class &c_even = row[static_cast<std::size_t>(2 * h)];
                const mpz_class &c_odd = row[static_cast<std::size_t>(2 * h - 1)];
                reserve_decimal_output(out_dir, {&c_even, &c_odd});
                witness << VERSION << "\toffset\t" << s << '\t' << h << '\t' << p
                        << '\t' << n << '\t' << c_even.get_str() << '\t'
                        << c_odd.get_str() << '\t' << rem_even << '\t' << rem_odd
                        << "\t1\t" << replay_a << '\t' << replay_b << '\n';
                result.status = "COUNTEREXAMPLE";
                result.witnesses = 1;
                stop = true;
                break;
            }
        }
        if (power_of_two(n) || n == max_n || stop) {
            const std::uint64_t last_s = n > 3 ? std::min(max_s, n - 3) : 0;
            checkpoints << VERSION << "\toffset\t" << n << '\t' << last_s << '\t'
                        << prime_pairs << '\t' << individual_even_zero << '\t'
                        << individual_odd_zero << '\t' << hex_u64(trace.value) << '\n';
        }
    }

    for (std::uint64_t h = 1; h <= max_h; ++h) {
        telemetry << VERSION << '\t' << h << '\t'
                  << candidates[static_cast<std::size_t>(h)] << '\t'
                  << even_zero[static_cast<std::size_t>(h)] << '\t'
                  << odd_zero[static_cast<std::size_t>(h)] << '\n';
    }
    checkpoints.flush();
    telemetry.flush();
    witness.flush();
    require(checkpoints && telemetry && witness, "cannot close offset outputs");
    result.used_limbs = used_limb_bytes(row);
    result.elapsed_ns = static_cast<std::uint64_t>(
        std::chrono::duration_cast<std::chrono::nanoseconds>(
            std::chrono::steady_clock::now() - started).count());

    std::ofstream summary(out_dir / "summary.tsv", std::ios::binary);
    require(summary, "cannot open offset summary");
    summary << "version\tlane\tmax_s\tmax_h\ttested\tstatus\twitnesses\tupdates"
               "\tprime_pairs\tindividual_2h_zero\tindividual_2h_minus_1_zero"
               "\ttrace_hash\tlimb_bytes\tmaxrss_kib\telapsed_ns\n";
    summary << VERSION << "\toffset\t" << max_s << '\t' << max_h << '\t'
            << result.tested << '\t' << result.status << '\t' << result.witnesses
            << '\t' << updates << '\t' << prime_pairs << '\t'
            << individual_even_zero << '\t' << individual_odd_zero << '\t'
            << hex_u64(trace.value) << '\t' << result.used_limbs << '\t'
            << maxrss_kib() << '\t' << result.elapsed_ns << '\n';
    summary.flush();
    require(summary, "cannot close offset summary");
    write_done(out_dir, "offset");
    return result;
}

void run_self_test(const fs::path &out_dir) {
    prepare_output_dir(out_dir);
    std::vector<std::string> tests;

    {
        const std::vector<mpz_class> row = second_row_exact(5);
        const std::array<unsigned long, 6> expected{{0, 1, 15, 25, 10, 1}};
        for (std::size_t k = 0; k < expected.size(); ++k)
            require(row[k] == expected[k], "small second-kind row failed");
        tests.push_back("small_second_kind_row");
    }
    {
        const std::vector<mpz_class> row = first_row_exact(5);
        const std::array<unsigned long, 6> expected{{0, 24, 50, 35, 10, 1}};
        for (std::size_t k = 0; k < expected.size(); ++k)
            require(row[k] == expected[k], "small first-kind row failed");
        tests.push_back("small_first_kind_row");
    }
    for (std::uint64_t k = 1; k <= 6; ++k) {
        for (std::uint64_t d = 0; d <= 6; ++d) {
            const std::vector<mpz_class> row = second_row_exact(k + d);
            require(row[static_cast<std::size_t>(k)] == complete_h_exact(k, d),
                    "complete homogeneous identity failed");
        }
    }
    tests.push_back("complete_homogeneous_identity");

    for (std::uint64_t s = 1; s <= 8; ++s) {
        const std::vector<mpz_class> target_row = second_row_exact(2 * s + 1);
        const std::vector<mpz_class> next_row = second_row_exact(2 * s + 2);
        const mpz_class a = target_row[static_cast<std::size_t>(s)];
        const mpz_class b = target_row[static_cast<std::size_t>(s - 1)];
        const mpz_class h_next = next_row[static_cast<std::size_t>(s)];
        require(h_next == b + s * a, "last-variable recurrence failed");
    }
    tests.push_back("last_variable_recurrence");

    for (const auto &[p, s] : std::vector<std::pair<std::uint64_t, std::uint64_t>>{
             {11, 2}, {13, 3}, {17, 4}, {43, 3}}) {
        require(p > 2 * s + 1 && ((p - 2 * s - 1) % 2 == 0),
                "bad complement self-test case");
        const std::uint64_t h = (p - 2 * s - 1) / 2;
        const std::uint64_t first_n = s + 2 * h + 1;
        const std::vector<std::uint64_t> first = first_row_mod(first_n, 2 * h, p);
        const std::uint64_t a = second_exact_mod(2 * s + 1, s, p);
        const std::uint64_t h_next = second_exact_mod(2 * s + 2, s, p);
        require(first[static_cast<std::size_t>(2 * h)] == a,
                "first-kind complement A failed");
        require(first[static_cast<std::size_t>(2 * h - 1)] == h_next,
                "first-kind complement next-h failed");
    }
    tests.push_back("first_kind_complement_equivalence");

    {
        const std::uint64_t p = 13, s = 4, half = 6, h_count = half - s;
        const std::uint64_t degree_cap = p - 2;
        std::vector<std::uint64_t> h(static_cast<std::size_t>(degree_cap + 1));
        h[0] = 1;
        for (std::uint64_t x = 1; x <= s; ++x) {
            for (std::uint64_t d = 1; d <= degree_cap; ++d)
                h[static_cast<std::size_t>(d)] = add_mod(
                    h[static_cast<std::size_t>(d)],
                    mul_mod(x, h[static_cast<std::size_t>(d - 1)], p), p);
        }
        std::vector<std::uint64_t> lhs(static_cast<std::size_t>(degree_cap + 1));
        for (std::uint64_t d = 0; d <= degree_cap; ++d) {
            for (std::uint64_t j = 0; j <= d; ++j) {
                std::uint64_t term = mul_mod(h[static_cast<std::size_t>(j)],
                                             h[static_cast<std::size_t>(d - j)], p);
                if ((d - j) & 1U)
                    lhs[static_cast<std::size_t>(d)] =
                        sub_mod(lhs[static_cast<std::size_t>(d)], term, p);
                else
                    lhs[static_cast<std::size_t>(d)] =
                        add_mod(lhs[static_cast<std::size_t>(d)], term, p);
            }
        }
        std::vector<std::uint64_t> rhs(static_cast<std::size_t>(degree_cap + 1));
        rhs[0] = 1;
        const std::uint64_t inverse_two = (p + 1) / 2;
        for (std::uint64_t i = 1; i <= h_count; ++i) {
            const std::uint64_t a = sub_mod(i % p, inverse_two, p);
            const std::uint64_t coefficient = sub_mod(0, mul_mod(a, a, p), p);
            for (std::uint64_t d = degree_cap; d >= 2; --d)
                rhs[static_cast<std::size_t>(d)] = add_mod(
                    rhs[static_cast<std::size_t>(d)],
                    mul_mod(coefficient, rhs[static_cast<std::size_t>(d - 2)], p), p);
        }
        require(lhs == rhs, "norm identity failed");
        tests.push_back("norm_identity_without_false_reindexing");
    }

    for (std::uint64_t m = 0; m <= 6; ++m) {
        const std::uint64_t n = 2 * m + 3;
        const std::vector<mpz_class> row = second_row_exact(n);
        mpz_class factorial_m;
        mpz_fac_ui(factorial_m.get_mpz_t(), static_cast<unsigned long>(m));
        require(finite_difference_polynomial(m, 0) ==
                    factorial_m * row[static_cast<std::size_t>(m)],
                "finite-difference endpoint zero failed");
        mpz_class factorial_next = factorial_m * (m + 1);
        require(finite_difference_polynomial(m, 1) - finite_difference_polynomial(m, 0) ==
                    factorial_next * row[static_cast<std::size_t>(m + 1)],
                "finite-difference endpoint one failed");
        for (long x = -3; x <= 3; ++x) {
            mpz_class rhs = finite_difference_polynomial(m, x);
            if ((m + 1) & 1U) rhs = -rhs;
            require(finite_difference_polynomial(m, -static_cast<long>(m) - x) == rhs,
                    "finite-difference reflection failed");
        }
    }
    tests.push_back("finite_difference_endpoints_and_reflection");

    {
        const std::uint64_t p = 43, s = 3, h_count = 18;
        require(second_exact_mod(7, 3, p) == 0, "negative control A failed");
        require(second_exact_mod(7, 2, p) == 20, "negative control B failed");
        require(second_exact_mod(37, 3, p) == 13, "false h34 residue changed");
        require(second_exact_mod(38, 3, p) == 36, "false h35 residue changed");
        require(h_count == (p - 2 * s - 1) / 2, "negative control h failed");
        tests.push_back("discarded_false_h_reparameterization");
    }
    require(second_exact_mod(9, 4, 37) == 0, "F277 p=37 saturation failed");
    require(second_exact_mod(9, 3, 37) != 0, "F277 p=37 became joint");
    require(second_exact_mod(10, 4, 19) == 0, "F277 p=19 saturation failed");
    require(second_exact_mod(9, 4, 19) != 0, "F277 p=19 became joint");
    tests.push_back("F277_individual_saturations");

    require(second_exact_mod(12, 3, 23) == 0 && second_exact_mod(12, 2, 23) == 0,
            "general adjacent positive control failed");
    tests.push_back("noncentral_adjacent_positive_control");

    {
        const std::uint64_t s = 73;
        const std::vector<mpz_class> row = second_row_exact(2 * s + 1);
        const std::vector<std::uint32_t> primes = primes_through(2 * s + 1);
        const DeltaTelemetry item = delta_telemetry(row, s, primes);
        require(item.ratio == 1679, "s=73 fixed-divisor ratio changed");
        require(!item.ratio_divides_2s, "refuted ratio diagnostic became a gate");
        require(item.support_residual == 1, "s=73 ratio support residual changed");
        tests.push_back("fixed_divisor_refuted_stronger_diagnostic");
    }

    {
        const std::vector<std::uint32_t> primes = primes_through(11);
        mpz_class synthetic = 1;
        synthetic *= 8;
        synthetic *= 9;
        synthetic *= 5;
        synthetic *= 169;
        const StripResult stripped = strip_small_primes(synthetic, 11, primes);
        require(stripped.residual == 169, "synthetic residual detector failed");
        mpz_class support = 1;
        for (unsigned long n = 1; n <= 11; ++n)
            mpz_lcm_ui(support.get_mpz_t(), support.get_mpz_t(), n);
        mpz_class common;
        mpz_gcd(common.get_mpz_t(), stripped.residual.get_mpz_t(), support.get_mpz_t());
        require(common == 1, "synthetic support gcd failed");
        tests.push_back("synthetic_residual_detector");
    }

    std::ofstream out(out_dir / "selftest.tsv", std::ios::binary);
    require(out, "cannot open selftest output");
    out << "version\ttest\tstatus\n";
    for (const std::string &test : tests) out << VERSION << '\t' << test << "\tPASS\n";
    out.flush();
    require(out, "cannot close selftest output");
    write_done(out_dir, "self-test");
}

std::array<std::uint64_t, 3> exact_pilots() { return {{512, 1024, 2048}}; }

std::array<std::pair<std::uint64_t, std::uint64_t>, 3> offset_pilots() {
    return {{{2048, 64}, {4096, 64}, {8192, 64}}};
}

struct Rung {
    std::uint64_t exact_s;
    std::uint64_t offset_s;
    std::uint64_t offset_h;
};

std::array<Rung, 6> production_rungs() {
    return {{{4000, 25000, 32}, {6000, 50000, 48}, {8000, 100000, 64},
             {10000, 150000, 64}, {12000, 200000, 64}, {16000, 300000, 64}}};
}

void require_exact_pilot(std::uint64_t s) {
    const auto pilots = exact_pilots();
    require(std::find(pilots.begin(), pilots.end(), s) != pilots.end(),
            "unregistered exact pilot");
}

void require_offset_pilot(std::uint64_t s, std::uint64_t h) {
    const auto pilots = offset_pilots();
    require(std::find(pilots.begin(), pilots.end(), std::make_pair(s, h)) != pilots.end(),
            "unregistered offset pilot");
}

void require_rung(std::uint64_t exact_s, std::uint64_t offset_s,
                  std::uint64_t offset_h) {
    bool found = false;
    for (const Rung &rung : production_rungs())
        found = found || (rung.exact_s == exact_s && rung.offset_s == offset_s &&
                          rung.offset_h == offset_h);
    require(found, "unregistered production rung");
}

void require_production_output_reservation(std::uint64_t exact_s,
                                           std::uint64_t offset_s,
                                           std::uint64_t offset_h,
                                           const fs::path &parent) {
    const long double exact_bound =
        16.0L * exact_s * std::log2(static_cast<long double>(exact_s + 1)) + 1048576.0L;
    const long double offset_n = offset_s + 2 * offset_h + 1;
    const long double offset_bound =
        8.0L * offset_n * std::log2(offset_n + 1.0L) + 1048576.0L;
    require(exact_bound + offset_bound <= OUTPUT_RESERVATION_BYTES,
            "production output reservation exceeds internal cap");
    const fs::space_info space = fs::space(parent);
    require(space.available >= static_cast<std::uint64_t>(exact_bound + offset_bound) +
                                   MIN_FREE_DISK_BYTES,
            "production disk reservation failed");
}

void run_production(std::uint64_t exact_s, std::uint64_t offset_s,
                    std::uint64_t offset_h, std::uint64_t workers,
                    const fs::path &out_dir) {
    require_rung(exact_s, offset_s, offset_h);
    require(workers >= 1 && workers <= MAX_WORKERS, "worker count outside hard cap");
    require(workers == 1 || workers == 2, "this packet selects only one or two workers");
    require_production_output_reservation(exact_s, offset_s, offset_h,
                                          out_dir.parent_path());
    prepare_output_dir(out_dir);
    LaneResult exact_result;
    LaneResult offset_result;
    std::exception_ptr exact_error;
    std::exception_ptr offset_error;

    if (workers == 1) {
        exact_result = run_exact_lane(exact_s, out_dir / "exact");
        offset_result = run_offset_lane(offset_s, offset_h, out_dir / "offset");
    } else {
        std::thread exact_thread([&] {
            try {
                exact_result = run_exact_lane(exact_s, out_dir / "exact");
            } catch (...) {
                exact_error = std::current_exception();
            }
        });
        std::thread offset_thread([&] {
            try {
                offset_result = run_offset_lane(offset_s, offset_h, out_dir / "offset");
            } catch (...) {
                offset_error = std::current_exception();
            }
        });
        exact_thread.join();
        offset_thread.join();
        if (exact_error) std::rethrow_exception(exact_error);
        if (offset_error) std::rethrow_exception(offset_error);
    }

    std::ofstream summary(out_dir / "production.tsv", std::ios::binary);
    require(summary, "cannot open production summary");
    summary << "version\texact_s\toffset_s\toffset_h\tworkers\texact_status"
               "\toffset_status\texact_tested\toffset_tested\texact_witnesses"
               "\toffset_witnesses\n";
    summary << VERSION << '\t' << exact_s << '\t' << offset_s << '\t' << offset_h
            << '\t' << workers << '\t' << exact_result.status << '\t'
            << offset_result.status << '\t' << exact_result.tested << '\t'
            << offset_result.tested << '\t' << exact_result.witnesses << '\t'
            << offset_result.witnesses << '\n';
    summary.flush();
    require(summary, "cannot close production summary");
    write_done(out_dir, "production");
}

void run_replay_exact(const fs::path &witness_path, const fs::path &out_dir) {
    prepare_output_dir(out_dir);
    std::ifstream in(witness_path, std::ios::binary);
    require(in, "cannot open exact witness");
    std::string header;
    std::string row;
    std::string extra;
    require(static_cast<bool>(std::getline(in, header)), "missing exact witness header");
    require(static_cast<bool>(std::getline(in, row)), "missing exact witness row");
    require(!std::getline(in, extra), "multiple exact witnesses");
    require(header ==
                "version\tlane\ts\tn\tbound\tA\tB\tgcd\tresidual\tsupport_lcm"
                "\tgcd_residual_support\tdivides_A\tdivides_B\tstripped_valuations",
            "wrong exact witness header");
    const std::vector<std::string> fields = split_tsv(row);
    require(fields.size() == 14 && fields[0] == VERSION && fields[1] == "exact",
            "wrong exact witness fields");
    const std::uint64_t s = parse_u64(fields[2].c_str(), "witness s");
    const std::uint64_t n = parse_u64(fields[3].c_str(), "witness n");
    const std::uint64_t bound = parse_u64(fields[4].c_str(), "witness bound");
    require(n == 2 * s + 1 && bound == n, "wrong exact witness indices");
    mpz_class a(fields[5]);
    mpz_class b(fields[6]);
    mpz_class serialized_gcd(fields[7]);
    mpz_class residual(fields[8]);
    mpz_class serialized_support(fields[9]);
    require(residual > 1, "unit exact witness residual");
    mpz_class actual_gcd;
    mpz_gcd(actual_gcd.get_mpz_t(), a.get_mpz_t(), b.get_mpz_t());
    require(actual_gcd == serialized_gcd, "exact witness gcd mismatch");
    require(mpz_divisible_p(a.get_mpz_t(), residual.get_mpz_t()) != 0 &&
                mpz_divisible_p(b.get_mpz_t(), residual.get_mpz_t()) != 0,
            "exact witness divisibility mismatch");
    mpz_class support = 1;
    for (std::uint64_t j = 1; j <= n; ++j)
        mpz_lcm_ui(support.get_mpz_t(), support.get_mpz_t(),
                   static_cast<unsigned long>(j));
    require(support == serialized_support, "exact witness support mismatch");
    mpz_class support_gcd;
    mpz_gcd(support_gcd.get_mpz_t(), residual.get_mpz_t(), support.get_mpz_t());
    require(support_gcd == 1 && fields[10] == "1" && fields[11] == "1" &&
                fields[12] == "1",
            "exact witness support certificate mismatch");
    const mpz_class replay_a = second_mod_composite(n, s, residual);
    const mpz_class replay_b = second_mod_composite(n, s - 1, residual);
    require(replay_a == 0 && replay_b == 0, "exact inclusion-exclusion replay failed");

    std::ofstream out(out_dir / "summary.tsv", std::ios::binary);
    require(out, "cannot open exact replay summary");
    out << "version\tlane\ts\tn\tresidual\tsupport_gcd\treplay_A\treplay_B\tstatus\n"
        << VERSION << "\texact\t" << s << '\t' << n << '\t' << residual.get_str()
        << '\t' << support_gcd.get_str() << '\t' << replay_a.get_str() << '\t'
        << replay_b.get_str() << "\tPASS\n";
    out.flush();
    require(out, "cannot close exact replay summary");
    write_done(out_dir, "replay-exact");
}

void run_replay_offset(const fs::path &witness_path, const fs::path &out_dir) {
    prepare_output_dir(out_dir);
    std::ifstream in(witness_path, std::ios::binary);
    require(in, "cannot open offset witness");
    std::string header;
    std::string row;
    std::string extra;
    require(static_cast<bool>(std::getline(in, header)), "missing offset witness header");
    require(static_cast<bool>(std::getline(in, row)), "missing offset witness row");
    require(!std::getline(in, extra), "multiple offset witnesses");
    require(header ==
                "version\tlane\ts\th\tp\tn\tc_n_2h\tc_n_2h_minus_1"
                "\trem_2h\trem_2h_minus_1\tflint_prime\treplay_A\treplay_B",
            "wrong offset witness header");
    const std::vector<std::string> fields = split_tsv(row);
    require(fields.size() == 13 && fields[0] == VERSION && fields[1] == "offset",
            "wrong offset witness fields");
    const std::uint64_t s = parse_u64(fields[2].c_str(), "witness s");
    const std::uint64_t h = parse_u64(fields[3].c_str(), "witness h");
    const std::uint64_t p = parse_u64(fields[4].c_str(), "witness p");
    const std::uint64_t n = parse_u64(fields[5].c_str(), "witness n");
    require(p == 2 * s + 2 * h + 1 && n == s + 2 * h + 1 && p > 2 * s + 1,
            "wrong offset witness indices");
    require(n_is_prime(static_cast<unsigned long>(p)) != 0, "offset replay prime failed");
    mpz_class c_even(fields[6]);
    mpz_class c_odd(fields[7]);
    require(mpz_fdiv_ui(c_even.get_mpz_t(), static_cast<unsigned long>(p)) == 0 &&
                mpz_fdiv_ui(c_odd.get_mpz_t(), static_cast<unsigned long>(p)) == 0,
            "serialized first-kind divisibility failed");
    const std::vector<std::uint64_t> first = first_row_mod(n, 2 * h, p);
    require(first[static_cast<std::size_t>(2 * h)] == 0 &&
                first[static_cast<std::size_t>(2 * h - 1)] == 0,
            "first-kind modular replay failed");
    const std::uint64_t replay_a = second_mod_prime(2 * s + 1, s, p);
    const std::uint64_t replay_b = second_mod_prime(2 * s + 1, s - 1, p);
    require(replay_a == 0 && replay_b == 0, "offset second-kind replay failed");

    std::ofstream out(out_dir / "summary.tsv", std::ios::binary);
    require(out, "cannot open offset replay summary");
    out << "version\tlane\ts\th\tp\tn\tfirst_2h\tfirst_2h_minus_1"
           "\treplay_A\treplay_B\tstatus\n"
        << VERSION << "\toffset\t" << s << '\t' << h << '\t' << p << '\t' << n
        << "\t0\t0\t" << replay_a << '\t' << replay_b << "\tPASS\n";
    out.flush();
    require(out, "cannot close offset replay summary");
    write_done(out_dir, "replay-offset");
}

}  // namespace

int main(int argc, char **argv) {
    try {
        require_runtime_limits();
        require(argc >= 2, "missing mode");
        const std::string mode(argv[1]);
        if (mode == "--self-test") {
            require(argc == 3, "usage: --self-test OUT_DIR");
            run_self_test(argv[2]);
        } else if (mode == "--pilot-exact") {
            require(argc == 4, "usage: --pilot-exact S OUT_DIR");
            const std::uint64_t s = parse_u64(argv[2], "pilot exact S");
            require_exact_pilot(s);
            run_exact_lane(s, argv[3]);
        } else if (mode == "--pilot-offset") {
            require(argc == 5, "usage: --pilot-offset S H OUT_DIR");
            const std::uint64_t s = parse_u64(argv[2], "pilot offset S");
            const std::uint64_t h = parse_u64(argv[3], "pilot offset H");
            require_offset_pilot(s, h);
            run_offset_lane(s, h, argv[4]);
        } else if (mode == "--production") {
            require(argc == 7, "usage: --production EXACT_S OFFSET_S H WORKERS OUT_DIR");
            const std::uint64_t exact_s = parse_u64(argv[2], "production exact S");
            const std::uint64_t offset_s = parse_u64(argv[3], "production offset S");
            const std::uint64_t offset_h = parse_u64(argv[4], "production H");
            const std::uint64_t workers = parse_u64(argv[5], "production workers");
            run_production(exact_s, offset_s, offset_h, workers, argv[6]);
        } else if (mode == "--replay-exact") {
            require(argc == 4, "usage: --replay-exact WITNESS OUT_DIR");
            run_replay_exact(argv[2], argv[3]);
        } else if (mode == "--replay-offset") {
            require(argc == 4, "usage: --replay-offset WITNESS OUT_DIR");
            run_replay_offset(argv[2], argv[3]);
        } else {
            fail("unknown mode");
        }
        return 0;
    } catch (const std::exception &error) {
        std::cerr << VERSION << " FATAL " << error.what() << '\n';
        return 70;
    }
}
