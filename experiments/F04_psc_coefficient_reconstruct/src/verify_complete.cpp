#include <flint/flint.h>
#include <flint/nmod.h>

#include <atomic>
#include <chrono>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <stdexcept>
#include <string>
#include <thread>
#include <vector>

namespace {

constexpr std::uint64_t N = 20000000499999937ULL;
constexpr std::uint64_t PRIME_P = 100000007ULL;
constexpr std::uint64_t PRIME_Q = 199999991ULL;
constexpr std::uint32_t R = 2953;
constexpr std::uint32_t SHIFT_FIRST = 1;
constexpr std::uint32_t SHIFT_LAST = 2942;
constexpr char MAGIC[8] = {'F', '0', '4', 'G', 'L', 'O', 'B', '1'};

struct Options {
    std::string input;
    std::string summary;
    std::string per_shift;
    unsigned threads = 1;
};

struct Header {
    std::uint32_t version;
    std::uint32_t r;
    std::uint32_t first;
    std::uint32_t last;
    std::uint64_t n;
    std::uint64_t p;
    std::uint64_t q;
    std::uint64_t coefficient_count;
};

struct ChainResult {
    bool pass = false;
    int expected_degree = -2;
    int actual_degree = -2;
};

struct ShiftResult {
    std::uint64_t nonunits = 0;
    bool global_top_nonzero = false;
    bool p_top_nonzero = false;
    bool q_top_nonzero = false;
    ChainResult p_chain;
    ChainResult q_chain;
};

Options parse_options(int argc, char** argv) {
    Options options;
    options.threads = std::max(1u, std::thread::hardware_concurrency());
    for (int i = 1; i < argc; ++i) {
        const std::string arg = argv[i];
        if (arg == "--input" && i + 1 < argc) {
            options.input = argv[++i];
        } else if (arg == "--summary" && i + 1 < argc) {
            options.summary = argv[++i];
        } else if (arg == "--per-shift" && i + 1 < argc) {
            options.per_shift = argv[++i];
        } else if (arg == "--threads" && i + 1 < argc) {
            options.threads = std::stoul(argv[++i]);
        } else {
            throw std::runtime_error("unknown or incomplete argument: " + arg);
        }
    }
    if (options.input.empty() || options.summary.empty() || options.per_shift.empty() ||
        options.threads == 0) {
        throw std::runtime_error("invalid options");
    }
    return options;
}

std::uint32_t read_u32(std::istream& stream) {
    std::uint32_t value = 0;
    for (unsigned i = 0; i < 4; ++i) {
        const int byte = stream.get();
        if (byte == EOF) {
            throw std::runtime_error("unexpected EOF in uint32");
        }
        value |= static_cast<std::uint32_t>(byte) << (8 * i);
    }
    return value;
}

std::uint64_t read_u64(std::istream& stream) {
    std::uint64_t value = 0;
    for (unsigned i = 0; i < 8; ++i) {
        const int byte = stream.get();
        if (byte == EOF) {
            throw std::runtime_error("unexpected EOF in uint64");
        }
        value |= static_cast<std::uint64_t>(byte) << (8 * i);
    }
    return value;
}

ChainResult normal_chain(const std::uint64_t* global, std::uint64_t prime) {
    nmod_t mod;
    nmod_init(&mod, prime);
    std::vector<ulong> a(R + 1, 0);
    std::vector<ulong> b(R, 0);
    std::vector<ulong> remainder;
    a[0] = prime - 1;
    a[R] = 1;
    for (std::uint32_t i = 0; i < R; ++i) {
        b[i] = global[i] % prime;
    }
    if (b[R - 1] == 0) {
        return {false, static_cast<int>(R - 1), static_cast<int>(R - 2)};
    }

    // Given degrees k+1 and k, the ordinary quotient is q1*X+q0.
    // Computing that two-term division directly is exact and records a
    // failure as soon as the next degree is not k-1.
    for (int k = static_cast<int>(R) - 1; k >= 1; --k) {
        const ulong divisor_lead = b[k];
        if (divisor_lead == 0) {
            return {false, k, k - 1};
        }
        const ulong inverse = n_invmod(divisor_lead, prime);
        const ulong q1 = nmod_mul(a[k + 1], inverse, mod);
        const ulong degree_k_after_first =
            nmod_sub(a[k], nmod_mul(q1, b[k - 1], mod), mod);
        const ulong q0 = nmod_mul(degree_k_after_first, inverse, mod);
        remainder.assign(k, 0);
        for (int i = 0; i < k; ++i) {
            ulong value = a[i];
            if (i > 0) {
                value = nmod_sub(value, nmod_mul(q1, b[i - 1], mod), mod);
            }
            value = nmod_sub(value, nmod_mul(q0, b[i], mod), mod);
            remainder[i] = value;
        }
        if (remainder[k - 1] == 0) {
            int actual = k - 2;
            while (actual >= 0 && remainder[actual] == 0) {
                --actual;
            }
            return {false, k - 1, actual};
        }
        a.swap(b);
        b.swap(remainder);
    }
    return {true, -1, -1};
}

}  // namespace

int main(int argc, char** argv) {
    try {
        const Options options = parse_options(argc, argv);
        const auto started = std::chrono::steady_clock::now();
        std::ifstream input(options.input, std::ios::binary);
        if (!input) {
            throw std::runtime_error("cannot open global-vector input");
        }
        char magic[8];
        input.read(magic, sizeof(magic));
        if (!input || !std::equal(std::begin(magic), std::end(magic), std::begin(MAGIC))) {
            throw std::runtime_error("bad global-vector magic");
        }
        const Header header{read_u32(input), read_u32(input), read_u32(input), read_u32(input),
                            read_u64(input), read_u64(input), read_u64(input), read_u64(input)};
        if (header.version != 1 || header.r != R || header.n != N || header.p != PRIME_P ||
            header.q != PRIME_Q || header.first < SHIFT_FIRST || header.last > SHIFT_LAST ||
            header.first > header.last) {
            throw std::runtime_error("global-vector header does not match fixed statement");
        }
        const std::uint32_t count = header.last - header.first + 1;
        if (header.coefficient_count != static_cast<std::uint64_t>(count) * R) {
            throw std::runtime_error("bad coefficient count in header");
        }
        std::vector<std::uint64_t> global(static_cast<std::size_t>(count) * R);
        for (std::uint32_t index = 0; index < count; ++index) {
            const std::uint32_t shift = read_u32(input);
            if (shift != header.first + index) {
                throw std::runtime_error("shift sequence mismatch");
            }
            const std::size_t offset = static_cast<std::size_t>(index) * R;
            for (std::uint32_t k = 0; k < R; ++k) {
                global[offset + k] = read_u64(input);
                if (global[offset + k] >= N) {
                    throw std::runtime_error("noncanonical global coefficient");
                }
            }
        }
        if (input.peek() != EOF) {
            throw std::runtime_error("trailing bytes after final global vector");
        }

        std::vector<ShiftResult> results(count);
        std::atomic<std::uint32_t> next{0};
        const unsigned worker_count = std::min<unsigned>(options.threads, count);
        std::vector<std::thread> workers;
        workers.reserve(worker_count);
        for (unsigned worker = 0; worker < worker_count; ++worker) {
            workers.emplace_back([&]() {
                while (true) {
                    const std::uint32_t index = next.fetch_add(1);
                    if (index >= count) {
                        break;
                    }
                    const std::size_t offset = static_cast<std::size_t>(index) * R;
                    const std::uint64_t* vector = global.data() + offset;
                    ShiftResult result;
                    result.global_top_nonzero = vector[R - 1] != 0;
                    result.p_top_nonzero = vector[R - 1] % PRIME_P != 0;
                    result.q_top_nonzero = vector[R - 1] % PRIME_Q != 0;
                    for (std::uint32_t k = 0; k < R; ++k) {
                        result.nonunits += vector[k] % PRIME_P == 0 || vector[k] % PRIME_Q == 0;
                    }
                    result.p_chain = normal_chain(vector, PRIME_P);
                    result.q_chain = normal_chain(vector, PRIME_Q);
                    results[index] = result;
                }
            });
        }
        for (auto& worker : workers) {
            worker.join();
        }

        std::ofstream per_shift(options.per_shift, std::ios::trunc);
        per_shift << "shift,nonunits,global_top_nonzero,p_top_nonzero,q_top_nonzero,"
                     "p_chain,p_expected,p_actual,q_chain,q_expected,q_actual\n";
        std::uint64_t nonunits = 0;
        std::uint64_t global_degree_failures = 0;
        std::uint64_t p_degree_failures = 0;
        std::uint64_t q_degree_failures = 0;
        std::uint64_t p_chain_failures = 0;
        std::uint64_t q_chain_failures = 0;
        for (std::uint32_t index = 0; index < count; ++index) {
            const ShiftResult& result = results[index];
            nonunits += result.nonunits;
            global_degree_failures += !result.global_top_nonzero;
            p_degree_failures += !result.p_top_nonzero;
            q_degree_failures += !result.q_top_nonzero;
            p_chain_failures += !result.p_chain.pass;
            q_chain_failures += !result.q_chain.pass;
            per_shift << header.first + index << ',' << result.nonunits << ','
                      << result.global_top_nonzero << ',' << result.p_top_nonzero << ','
                      << result.q_top_nonzero << ',' << (result.p_chain.pass ? "pass" : "fail")
                      << ',' << result.p_chain.expected_degree << ',' << result.p_chain.actual_degree
                      << ',' << (result.q_chain.pass ? "pass" : "fail") << ','
                      << result.q_chain.expected_degree << ',' << result.q_chain.actual_degree << '\n';
        }
        if (!per_shift) {
            throw std::runtime_error("failed while writing per-shift output");
        }

        const bool full_range = header.first == SHIFT_FIRST && header.last == SHIFT_LAST;
        const std::uint64_t statuses_per_field =
            (full_range && p_chain_failures == 0) ? static_cast<std::uint64_t>(count) * R : 0;
        const std::uint64_t statuses_q =
            (full_range && q_chain_failures == 0) ? static_cast<std::uint64_t>(count) * R : 0;
        const double seconds = std::chrono::duration<double>(std::chrono::steady_clock::now() - started).count();
        const bool pass = full_range && nonunits == 0 && global_degree_failures == 0 &&
                          p_degree_failures == 0 && q_degree_failures == 0 &&
                          p_chain_failures == 0 && q_chain_failures == 0;
        std::ofstream summary(options.summary, std::ios::trunc);
        summary << "{\n"
                << "  \"status\": \"" << (pass ? "pass" : "fail") << "\",\n"
                << "  \"method\": \"read materialized global vectors, reduce entries, exact two-term ordinary Euclidean division\",\n"
                << "  \"full_claimed_shift_range\": " << (full_range ? "true" : "false") << ",\n"
                << "  \"shift_count\": " << count << ",\n"
                << "  \"coefficient_count\": " << static_cast<std::uint64_t>(count) * R << ",\n"
                << "  \"nonunit_coefficients\": " << nonunits << ",\n"
                << "  \"global_degree_failures\": " << global_degree_failures << ",\n"
                << "  \"p_degree_failures\": " << p_degree_failures << ",\n"
                << "  \"q_degree_failures\": " << q_degree_failures << ",\n"
                << "  \"p_chain_failures\": " << p_chain_failures << ",\n"
                << "  \"q_chain_failures\": " << q_chain_failures << ",\n"
                << "  \"p_nonzero_D_statuses\": " << statuses_per_field << ",\n"
                << "  \"q_nonzero_D_statuses\": " << statuses_q << ",\n"
                << "  \"total_nonzero_D_statuses\": " << statuses_per_field + statuses_q << ",\n"
                << "  \"threads\": " << worker_count << ",\n"
                << "  \"elapsed_seconds\": " << seconds << "\n"
                << "}\n";
        if (!summary) {
            throw std::runtime_error("failed while writing verifier summary");
        }
        std::cout << "verified " << count << " already-materialized global vectors; status="
                  << (pass ? "pass" : "fail") << '\n';
        return pass ? 0 : 2;
    } catch (const std::exception& error) {
        std::cerr << "verify_complete: " << error.what() << '\n';
        return 1;
    }
}

