#include <algorithm>
#include <array>
#include <chrono>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <map>
#include <numeric>
#include <stdexcept>
#include <string>
#include <utility>
#include <vector>

using u64 = std::uint64_t;
using u128 = __uint128_t;

constexpr int MENU_COUNT = 7;
constexpr std::array<int, MENU_COUNT> MENU_MASK{1, 2, 4, 3, 5, 6, 7};
constexpr std::array<const char*, MENU_COUNT> MENU_NAME{
    "K", "R", "C", "KR", "KC", "RC", "KRC"};
constexpr const char* PREREG_SHA =
    "0ae27d2388282828ca10150d13abe5213a81d718f1a7d28d9eb899579dd5f412";
constexpr const char* CORRIGENDUM_2_SHA =
    "4f89d5a9041a7d4137a8d9c1978d6421fcf2fd0144c931192262533ebadc78ce";

struct Factorization {
    std::array<u64, 16> prime{};
    std::array<int, 16> exponent{};
    std::array<u64, 16> power{};
    int size = 0;
};

struct Evaluation {
    std::array<u64, MENU_COUNT> rp{};
    std::array<u64, MENU_COUNT> rq{};
    Factorization fp;
    Factorization fq;
};

struct RankRow {
    u64 p, q, N, value;
    int n;
};

struct DomainStats {
    u64 total = 0;
    std::map<int, u64> count_by_n;
    std::array<u64, MENU_COUNT> maximum{};
    std::map<int, std::array<u64, MENU_COUNT>> maximum_by_n;
    std::array<std::array<u64, 4>, MENU_COUNT> threshold{};
    std::array<std::vector<RankRow>, MENU_COUNT> records;
    std::array<std::vector<RankRow>, MENU_COUNT> top;
    std::array<u64, 8> incidence_mask{};
    std::array<std::map<int, u64>, 3> first_hit;
};

static int bitlen(u64 x) {
    return 64 - __builtin_clzll(x);
}

static int valuation_two(u64 x) {
    return __builtin_ctzll(x);
}

static u64 powmod(u64 a, u64 e, u64 m) {
    if (m == 1) return 0;
    u64 r = 1;
    while (e) {
        if (e & 1) r = static_cast<u128>(r) * a % m;
        a = static_cast<u128>(a) * a % m;
        e >>= 1;
    }
    return r;
}

static u64 inverse_odd_power_two(u64 a, u64 m) {
    u64 x = a;
    for (int i = 0; i < 6; ++i) x *= 2 - a * x;
    return x & (m - 1);
}

static Factorization factor_value(u64 x, const std::vector<int>& spf) {
    Factorization f;
    while (x > 1) {
        const u64 ell = spf[x];
        int exponent = 0;
        u64 power = 1;
        do {
            x /= ell;
            power *= ell;
            ++exponent;
        } while (x % ell == 0);
        f.prime[f.size] = ell;
        f.exponent[f.size] = exponent;
        f.power[f.size] = power;
        ++f.size;
    }
    return f;
}

static void build_sequences(
    u64 N,
    int n,
    std::array<u64, 64>& quotient,
    std::array<u64, 64>& remainder,
    std::array<u64, 64>& centered_abs) {
    if ((N >> n) != 0) throw std::runtime_error("K_n is not zero");
    for (int j = 1; j <= n; ++j) {
        const u64 full = u64{1} << j;
        const u64 half = full >> 1;
        quotient[j] = N >> j;
        remainder[j] = N - (quotient[j] << j);
        centered_abs[j] = remainder[j] >= half
            ? full - remainder[j]
            : remainder[j];
        const u64 rounded = (N + half) >> j;
        const __int128 centered = static_cast<__int128>(N)
            - (static_cast<__int128>(rounded) << j);
        const u64 checked_abs = centered < 0
            ? static_cast<u64>(-centered)
            : static_cast<u64>(centered);
        if (checked_abs != centered_abs[j]
            || centered < -static_cast<__int128>(half)
            || centered >= static_cast<__int128>(half)) {
            throw std::runtime_error("centered remainder mismatch");
        }
        if (remainder[j] == 0 || centered_abs[j] == 0) {
            throw std::runtime_error("unexpected zero suffix on odd input");
        }
    }
    if (quotient[n] != 0 || quotient[n - 1] != 1
        || remainder[1] != 1 || remainder[n] != N
        || centered_abs[1] != 1) {
        throw std::runtime_error("endpoint mismatch");
    }
}

static std::array<u64, MENU_COUNT> evaluate_side(
    u64 s,
    u64 N,
    u64 other_prime,
    int n,
    const Factorization& factors,
    const std::array<u64, 64>& quotient,
    const std::array<u64, 64>& remainder,
    const std::array<u64, 64>& centered_abs,
    DomainStats* stats) {
    std::array<u64, MENU_COUNT> by_incidence;
    by_incidence.fill(1);

    for (int f = 0; f < factors.size; ++f) {
        const u64 ell = factors.prime[f];
        std::array<bool, 3> hit{};
        std::array<int, 3> first{};
        for (int j = 1; j <= n; ++j) {
            const u64 full = u64{1} << j;
            if (j < n) {
                const bool direct = quotient[j] % ell == 0;
                const bool interval = static_cast<u128>(N)
                    % (static_cast<u128>(ell) * full) < full;
                const bool local = other_prime % ell == remainder[j] % ell;
                if (direct != interval || (ell != 2 && direct != local)) {
                    throw std::runtime_error("quotient incidence mismatch");
                }
                if (direct && !hit[0]) {
                    hit[0] = true;
                    first[0] = j;
                }
            }
            const bool remainder_hit = remainder[j] % ell == 0;
            if (remainder_hit && !hit[1]) {
                hit[1] = true;
                first[1] = j;
            }
            const bool centered_hit = centered_abs[j] % ell == 0;
            const u64 piecewise = remainder[j] >= (full >> 1)
                ? full - remainder[j]
                : remainder[j];
            if (centered_hit != (piecewise % ell == 0)) {
                throw std::runtime_error("centered incidence mismatch");
            }
            if (centered_hit && !hit[2]) {
                hit[2] = true;
                first[2] = j;
            }
        }
        const int mask = static_cast<int>(hit[0])
            | (static_cast<int>(hit[1]) << 1)
            | (static_cast<int>(hit[2]) << 2);
        if (stats) {
            ++stats->incidence_mask[mask];
            for (int kind = 0; kind < 3; ++kind) {
                ++stats->first_hit[kind][first[kind]];
            }
        }
        for (int menu = 0; menu < MENU_COUNT; ++menu) {
            if ((mask & MENU_MASK[menu]) == 0) {
                by_incidence[menu] *= factors.power[f];
            }
        }
    }

    if (s == 1) return by_incidence;
    std::array<u64, 3> product{1 % s, 1 % s, 1 % s};
    for (int j = 1; j <= n; ++j) {
        if (j < n) {
            product[0] = static_cast<u128>(product[0])
                * (quotient[j] % s) % s;
        }
        product[1] = static_cast<u128>(product[1])
            * (remainder[j] % s) % s;
        product[2] = static_cast<u128>(product[2])
            * (centered_abs[j] % s) % s;
    }
    for (u64& value : product) value = powmod(value, n, s);
    for (int menu = 0; menu < MENU_COUNT; ++menu) {
        u64 word = 1 % s;
        for (int kind = 0; kind < 3; ++kind) {
            if (MENU_MASK[menu] & (1 << kind)) {
                word = static_cast<u128>(word) * product[kind] % s;
            }
        }
        const u64 by_word = s / std::gcd(s, word);
        if (by_word != by_incidence[menu]) {
            throw std::runtime_error("word residual mismatch");
        }
    }
    return by_incidence;
}

static Evaluation evaluate(
    u64 p,
    u64 q,
    const std::vector<int>& spf,
    DomainStats* stats) {
    const u64 N = p * q;
    const int n = bitlen(N);
    const u64 d = std::gcd(p - 1, q - 1);
    const u64 sp = (p - 1) / d;
    const u64 sq = (q - 1) / d;
    Evaluation result;
    result.fp = factor_value(sp, spf);
    result.fq = factor_value(sq, spf);
    std::array<u64, 64> quotient{}, remainder{}, centered_abs{};
    build_sequences(N, n, quotient, remainder, centered_abs);
    result.rp = evaluate_side(
        sp, N, q, n, result.fp, quotient, remainder, centered_abs, stats);
    result.rq = evaluate_side(
        sq, N, p, n, result.fq, quotient, remainder, centered_abs, stats);
    return result;
}

static bool better(const RankRow& a, const RankRow& b) {
    return a.value > b.value || (a.value == b.value && a.N < b.N);
}

static void update_top(std::vector<RankRow>& top, const RankRow& row) {
    if (top.size() < 20) {
        top.push_back(row);
        return;
    }
    auto worst = std::max_element(top.begin(), top.end(), better);
    if (better(row, *worst)) *worst = row;
}

static void update_stats(
    DomainStats& stats,
    u64 p,
    u64 q,
    const Evaluation& evaluation) {
    const u64 N = p * q;
    const int n = bitlen(N);
    ++stats.total;
    ++stats.count_by_n[n];
    auto& by_n = stats.maximum_by_n[n];
    for (int menu = 0; menu < MENU_COUNT; ++menu) {
        const u64 value = std::min(evaluation.rp[menu], evaluation.rq[menu]);
        const RankRow row{p, q, N, value, n};
        if (value > stats.maximum[menu]) {
            stats.maximum[menu] = value;
            stats.records[menu].push_back(row);
        }
        by_n[menu] = std::max(by_n[menu], value);
        if (value == 1) ++stats.threshold[menu][0];
        if (value <= static_cast<u64>(n)) ++stats.threshold[menu][1];
        if (value <= static_cast<u64>(n) * n) ++stats.threshold[menu][2];
        if (value <= static_cast<u64>(n) * n * n) {
            ++stats.threshold[menu][3];
        }
        update_top(stats.top[menu], row);
    }
}

static void print_factorization(
    std::ostream& out,
    const Factorization& factors) {
    if (factors.size == 0) {
        out << "1";
        return;
    }
    for (int i = 0; i < factors.size; ++i) {
        if (i) out << '*';
        out << factors.prime[i];
        if (factors.exponent[i] > 1) out << '^' << factors.exponent[i];
    }
}

static void print_detail(
    std::ostream& out,
    u64 p,
    u64 q,
    const std::vector<int>& spf) {
    const u64 N = p * q;
    const int n = bitlen(N);
    const u64 d = std::gcd(p - 1, q - 1);
    const u64 sp = (p - 1) / d;
    const u64 sq = (q - 1) / d;
    const Evaluation evaluation = evaluate(p, q, spf, nullptr);
    std::array<u64, 64> quotient{}, remainder{}, centered_abs{};
    build_sequences(N, n, quotient, remainder, centered_abs);
    out << "p=" << p << " q=" << q << " N=" << N << " n=" << n
        << " d=" << d << " sp=" << sp << '(';
    print_factorization(out, evaluation.fp);
    out << ") sq=" << sq << '(';
    print_factorization(out, evaluation.fq);
    out << ") residuals=";
    for (int menu = 0; menu < MENU_COUNT; ++menu) {
        if (menu) out << ',';
        out << MENU_NAME[menu] << ":(" << evaluation.rp[menu] << ','
            << evaluation.rq[menu] << ')';
    }
    out << " hits=";
    for (int side = 0; side < 2; ++side) {
        const Factorization& factors = side == 0 ? evaluation.fp : evaluation.fq;
        if (side) out << ';';
        out << (side == 0 ? 'p' : 'q') << '{';
        for (int f = 0; f < factors.size; ++f) {
            if (f) out << ',';
            const u64 ell = factors.prime[f];
            out << ell << ":K[";
            bool comma = false;
            for (int j = 1; j < n; ++j) if (quotient[j] % ell == 0) {
                if (comma) out << ',';
                out << j;
                comma = true;
            }
            out << "]R[";
            comma = false;
            for (int j = 1; j <= n; ++j) if (remainder[j] % ell == 0) {
                if (comma) out << ',';
                out << j;
                comma = true;
            }
            out << "]C[";
            comma = false;
            for (int j = 1; j <= n; ++j) if (centered_abs[j] % ell == 0) {
                if (comma) out << ',';
                out << j;
                comma = true;
            }
            out << ']';
        }
        out << '}';
    }
    out << '\n';
}

static void print_stats(
    std::ostream& out,
    const std::string& domain,
    DomainStats& stats,
    const std::vector<int>& spf) {
    out << "DOMAIN " << domain << "\nTOTAL " << stats.total << "\nBY_N";
    for (const auto& [n, count] : stats.count_by_n) {
        out << ' ' << n << ':' << count;
    }
    out << "\nINCIDENCE_MASK";
    for (int mask = 0; mask < 8; ++mask) {
        out << ' ' << mask << ':' << stats.incidence_mask[mask];
    }
    out << '\n';
    for (int kind = 0; kind < 3; ++kind) {
        out << "FIRST_" << "KRC"[kind];
        for (const auto& [index, count] : stats.first_hit[kind]) {
            out << ' ' << index << ':' << count;
        }
        out << '\n';
    }
    for (int menu = 0; menu < MENU_COUNT; ++menu) {
        out << "MENU " << MENU_NAME[menu] << " MAX " << stats.maximum[menu]
            << " COUNTS one=" << stats.threshold[menu][0]
            << " le_n=" << stats.threshold[menu][1]
            << " le_n2=" << stats.threshold[menu][2]
            << " le_n3=" << stats.threshold[menu][3] << "\nMAX_BY_N";
        for (const auto& [n, values] : stats.maximum_by_n) {
            out << ' ' << n << ':' << values[menu];
        }
        out << "\nRECORDS " << stats.records[menu].size() << '\n';
        for (const RankRow& row : stats.records[menu]) {
            out << "record p=" << row.p << " q=" << row.q
                << " N=" << row.N << " n=" << row.n
                << " value=" << row.value << '\n';
        }
        std::sort(stats.top[menu].begin(), stats.top[menu].end(), better);
        out << "TOP20\n";
        for (const RankRow& row : stats.top[menu]) {
            print_detail(out, row.p, row.q, spf);
        }
    }
}

int main(int argc, char** argv) {
    if (argc != 3) {
        std::cerr << "usage: scan zero|broad OUTPUT\n";
        return 2;
    }
    const std::string mode = argv[1];
    if (mode != "zero" && mode != "broad") {
        std::cerr << "unknown mode\n";
        return 2;
    }
    std::ofstream out(argv[2]);
    if (!out) {
        std::cerr << "cannot open output\n";
        return 2;
    }
    constexpr int P_LIMIT = 1 << 22;
    constexpr int Q_LIMIT = 1 << 23;
    std::vector<int> spf(Q_LIMIT, 0), primes;
    primes.reserve(600000);
    for (int i = 2; i < Q_LIMIT; ++i) {
        if (!spf[i]) {
            spf[i] = i;
            primes.push_back(i);
        }
        for (int p : primes) {
            if (p > spf[i] || static_cast<u64>(i) * p >= Q_LIMIT) break;
            spf[i * p] = p;
        }
    }

    DomainStats stats;
    const auto start = std::chrono::steady_clock::now();
    if (mode == "zero") {
        for (int pi : primes) {
            if (pi >= P_LIMIT) break;
            if (pi == 2) continue;
            const u64 p = pi;
            const int nlo = bitlen(p * p);
            const int nhi = bitlen(2 * p * p - 1);
            for (int n = nlo; n <= nhi; ++n) {
                const u64 B = u64{1} << (n / 2);
                const u64 inverse = inverse_odd_power_two(p, B);
                const std::int64_t k0 =
                    (static_cast<std::int64_t>(p)
                    - static_cast<std::int64_t>(inverse))
                    / static_cast<std::int64_t>(B) - 1;
                for (std::int64_t k = std::max<std::int64_t>(0, k0);
                     k <= k0 + 5; ++k) {
                    const u64 q = inverse + static_cast<u64>(k) * B;
                    if (!(p < q && q < 2 * p) || q >= Q_LIMIT
                        || spf[q] != static_cast<int>(q)) continue;
                    const u64 N = p * q;
                    if (bitlen(N) != n || (N - 1) % B != 0) continue;
                    if (valuation_two(p - 1) != valuation_two(q - 1)) {
                        std::cerr << "F236 valuation mismatch\n";
                        return 3;
                    }
                    const Evaluation evaluation = evaluate(p, q, spf, &stats);
                    update_stats(stats, p, q, evaluation);
                }
            }
        }
        if (stats.total != 34463) {
            std::cerr << "F236 count mismatch: " << stats.total << '\n';
            return 3;
        }
    } else {
        constexpr int BROAD_P_LIMIT = 1 << 16;
        for (auto p_it = primes.begin(); p_it != primes.end() && *p_it < BROAD_P_LIMIT;
             ++p_it) {
            const int p = *p_it;
            if (p == 2) continue;
            auto q_it = std::upper_bound(primes.begin(), primes.end(), p);
            const auto q_end = std::lower_bound(primes.begin(), primes.end(), 2 * p);
            for (; q_it != q_end; ++q_it) {
                const u64 q = *q_it;
                const Evaluation evaluation = evaluate(p, q, spf, &stats);
                update_stats(stats, p, q, evaluation);
            }
            if ((p & 4095) < 16) {
                const double seconds = std::chrono::duration<double>(
                    std::chrono::steady_clock::now() - start).count();
                std::cerr << "p=" << p << " rows=" << stats.total
                    << " seconds=" << seconds << '\n';
            }
        }
    }
    out << "PREREG_SHA256 " << PREREG_SHA << '\n';
    out << "PREREG_CORRIGENDUM_2_SHA256 " << CORRIGENDUM_2_SHA << '\n';
    print_stats(out, mode, stats, spf);
    const double seconds = std::chrono::duration<double>(
        std::chrono::steady_clock::now() - start).count();
    out << "ELAPSED_SECONDS " << seconds << '\n';
    std::cerr << "done rows=" << stats.total << " seconds=" << seconds << '\n';
}
