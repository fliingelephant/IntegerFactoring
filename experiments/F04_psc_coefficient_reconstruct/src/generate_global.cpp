#include <flint/flint.h>
#include <flint/nmod.h>
#include <flint/nmod_poly.h>

#include <atomic>
#include <chrono>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <mutex>
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
constexpr std::uint32_t SHIFT_COUNT = SHIFT_LAST - SHIFT_FIRST + 1;
constexpr char MAGIC[8] = {'F', '0', '4', 'G', 'L', 'O', 'B', '1'};

struct Options {
    std::string output;
    std::string summary;
    unsigned threads = 1;
    std::uint32_t first = SHIFT_FIRST;
    std::uint32_t last = SHIFT_LAST;
};

Options parse_options(int argc, char** argv) {
    Options options;
    options.threads = std::max(1u, std::thread::hardware_concurrency());
    for (int i = 1; i < argc; ++i) {
        const std::string arg = argv[i];
        if (arg == "--output" && i + 1 < argc) {
            options.output = argv[++i];
        } else if (arg == "--summary" && i + 1 < argc) {
            options.summary = argv[++i];
        } else if (arg == "--threads" && i + 1 < argc) {
            options.threads = std::stoul(argv[++i]);
        } else if (arg == "--first" && i + 1 < argc) {
            options.first = std::stoul(argv[++i]);
        } else if (arg == "--last" && i + 1 < argc) {
            options.last = std::stoul(argv[++i]);
        } else {
            throw std::runtime_error("unknown or incomplete argument: " + arg);
        }
    }
    if (options.output.empty() || options.summary.empty() || options.threads == 0 ||
        options.first < SHIFT_FIRST || options.last > SHIFT_LAST || options.first > options.last) {
        throw std::runtime_error("invalid options");
    }
    return options;
}

void write_u32(std::ostream& stream, std::uint32_t value) {
    for (unsigned i = 0; i < 4; ++i) {
        stream.put(static_cast<char>((value >> (8 * i)) & 0xff));
    }
}

void write_u64(std::ostream& stream, std::uint64_t value) {
    for (unsigned i = 0; i < 8; ++i) {
        stream.put(static_cast<char>((value >> (8 * i)) & 0xff));
    }
}

void component(std::uint32_t shift, std::uint64_t characteristic,
               std::uint64_t other_factor, std::vector<std::uint64_t>& coefficients) {
    nmod_poly_t modulus;
    nmod_poly_t base;
    nmod_poly_t power;
    nmod_poly_init(modulus, characteristic);
    nmod_poly_init(base, characteristic);
    nmod_poly_init(power, characteristic);

    nmod_poly_set_coeff_ui(modulus, 0, characteristic - 1);
    nmod_poly_set_coeff_ui(modulus, R, 1);
    nmod_poly_set_coeff_ui(base, 0, shift % characteristic);
    nmod_poly_set_coeff_ui(base, characteristic % R, 1);

    // In characteristic l, (X+a)^N = (X^l+a)^(N/l).
    nmod_poly_powmod_ui_binexp(power, base, other_factor, modulus);
    coefficients.resize(R);
    for (std::uint32_t k = 0; k < R; ++k) {
        coefficients[k] = nmod_poly_get_coeff_ui(power, k);
    }
    nmod_t mod;
    nmod_init(&mod, characteristic);
    coefficients[N % R] = nmod_sub(coefficients[N % R], 1, mod);
    coefficients[0] = nmod_sub(coefficients[0], shift % characteristic, mod);

    nmod_poly_clear(power);
    nmod_poly_clear(base);
    nmod_poly_clear(modulus);
}

}  // namespace

int main(int argc, char** argv) {
    try {
        const Options options = parse_options(argc, argv);
        const auto started = std::chrono::steady_clock::now();
        const std::uint32_t count = options.last - options.first + 1;
        std::vector<std::uint64_t> global(static_cast<std::size_t>(count) * R);
        const std::uint64_t p_inverse_mod_q = n_invmod(PRIME_P % PRIME_Q, PRIME_Q);
        std::atomic<std::uint32_t> next{0};
        std::atomic<bool> failed{false};
        std::mutex failure_mutex;
        std::string failure_message;

        const unsigned worker_count = std::min<unsigned>(options.threads, count);
        std::vector<std::thread> workers;
        workers.reserve(worker_count);
        for (unsigned worker = 0; worker < worker_count; ++worker) {
            workers.emplace_back([&]() {
                try {
                    std::vector<std::uint64_t> mod_p;
                    std::vector<std::uint64_t> mod_q;
                    while (!failed.load(std::memory_order_relaxed)) {
                        const std::uint32_t index = next.fetch_add(1);
                        if (index >= count) {
                            break;
                        }
                        const std::uint32_t shift = options.first + index;
                        component(shift, PRIME_P, PRIME_Q, mod_p);
                        component(shift, PRIME_Q, PRIME_P, mod_q);
                        const std::size_t offset = static_cast<std::size_t>(index) * R;
                        for (std::uint32_t k = 0; k < R; ++k) {
                            const std::uint64_t cp = mod_p[k];
                            const std::uint64_t cq = mod_q[k];
                            const std::uint64_t delta = (cq + PRIME_Q - cp) % PRIME_Q;
                            const std::uint64_t multiplier = static_cast<std::uint64_t>(
                                static_cast<unsigned __int128>(delta) * p_inverse_mod_q % PRIME_Q);
                            const std::uint64_t value = cp + PRIME_P * multiplier;
                            if (value >= N || value % PRIME_P != cp || value % PRIME_Q != cq) {
                                throw std::runtime_error("CRT reconstruction mismatch at shift " +
                                                         std::to_string(shift) + ", coefficient " +
                                                         std::to_string(k));
                            }
                            global[offset + k] = value;
                        }
                    }
                } catch (const std::exception& error) {
                    failed.store(true);
                    std::lock_guard<std::mutex> lock(failure_mutex);
                    failure_message = error.what();
                }
            });
        }
        for (auto& worker : workers) {
            worker.join();
        }
        if (failed.load()) {
            throw std::runtime_error(failure_message);
        }

        std::ofstream output(options.output, std::ios::binary | std::ios::trunc);
        if (!output) {
            throw std::runtime_error("cannot open global-vector output");
        }
        output.write(MAGIC, sizeof(MAGIC));
        write_u32(output, 1);
        write_u32(output, R);
        write_u32(output, options.first);
        write_u32(output, options.last);
        write_u64(output, N);
        write_u64(output, PRIME_P);
        write_u64(output, PRIME_Q);
        write_u64(output, static_cast<std::uint64_t>(count) * R);
        for (std::uint32_t index = 0; index < count; ++index) {
            write_u32(output, options.first + index);
            const std::size_t offset = static_cast<std::size_t>(index) * R;
            for (std::uint32_t k = 0; k < R; ++k) {
                write_u64(output, global[offset + k]);
            }
        }
        output.close();
        if (!output) {
            throw std::runtime_error("failed while writing global-vector output");
        }

        std::uint64_t nonunits = 0;
        std::uint64_t bad_top = 0;
        for (std::uint32_t index = 0; index < count; ++index) {
            const std::size_t offset = static_cast<std::size_t>(index) * R;
            bad_top += global[offset + R - 1] == 0;
            for (std::uint32_t k = 0; k < R; ++k) {
                nonunits += global[offset + k] % PRIME_P == 0 ||
                            global[offset + k] % PRIME_Q == 0;
            }
        }
        const double seconds = std::chrono::duration<double>(std::chrono::steady_clock::now() - started).count();
        std::ofstream summary(options.summary, std::ios::trunc);
        summary << "{\n"
                << "  \"status\": \"pass\",\n"
                << "  \"method\": \"field Frobenius powers, coefficientwise CRT, then materialize global vectors\",\n"
                << "  \"shift_first\": " << options.first << ",\n"
                << "  \"shift_last\": " << options.last << ",\n"
                << "  \"shift_count\": " << count << ",\n"
                << "  \"coefficient_count\": " << static_cast<std::uint64_t>(count) * R << ",\n"
                << "  \"nonunit_coefficients\": " << nonunits << ",\n"
                << "  \"global_vectors_with_zero_top_coefficient\": " << bad_top << ",\n"
                << "  \"threads\": " << worker_count << ",\n"
                << "  \"elapsed_seconds\": " << seconds << "\n"
                << "}\n";
        if (!summary) {
            throw std::runtime_error("failed while writing generator summary");
        }
        std::cout << "materialized " << count << " global vectors ("
                  << static_cast<std::uint64_t>(count) * R << " coefficients)\n";
        return nonunits == 0 && bad_top == 0 ? 0 : 2;
    } catch (const std::exception& error) {
        std::cerr << "generate_global: " << error.what() << '\n';
        return 1;
    }
}

