#define main f228_d01_unused_main
#include "run_F228_D01.cpp"
#undef main

static void factor_fast_d03(u64 x, const std::vector<unsigned>& primes,
                            std::set<u64>& out) {
    if (is_prime(x)) {
        out.insert(x);
        return;
    }
    for (u64 p : primes) {
        if (p * p > x) break;
        if (x % p != 0) continue;
        out.insert(p);
        while (x % p == 0) x /= p;
        if (x == 1) return;
        if (is_prime(x)) {
            out.insert(x);
            return;
        }
    }
    if (x > 1) out.insert(x);
}

int main(int argc, char** argv) {
    if (argc != 2) throw std::runtime_error("usage: run_F228_D03 OUTPUT.tsv");
    const auto started = std::chrono::steady_clock::now();
    const std::vector<unsigned> scales{22, 26, 30};
    u64 max_a = 255ULL * (1ULL << 31) + 4;
    unsigned trial_limit = 1;
    while (static_cast<u64>(trial_limit) * trial_limit < max_a) ++trial_limit;
    auto primes = sieve(trial_limit);

    std::ofstream out(argv[1]);
    if (!out) throw std::runtime_error("cannot open output");
    out << "k\trow\tp\tq\tN\tn\tJ\toracle_num\tcap20_num\tcap40_num"
           "\tcap64_num\tmin_omega\tmax_omega\tsum_omega\tbest_u\tbest_i"
           "\tbest_product\tbest_primes\n";

    for (unsigned k : scales) {
        std::vector<u64> safe;
        for (u64 r = (1ULL << k) | 1; safe.size() < 33; r += 2) {
            if (is_prime(r) && is_prime((r - 1) / 2)) safe.push_back(r);
        }
        u64 zero_oracle = 0, oracle_total = 0, cap20_total = 0;
        u64 cap40_total = 0, cap64_total = 0;
        for (std::size_t row = 0; row < 32; ++row) {
            u64 p = safe[row], q = safe[row + 1];
            if (q >= 2 * p) throw std::runtime_error("cohort not balanced");
            u64 N = p * q;
            unsigned n = 64 - __builtin_clzll(N);
            u64 B = 1ULL << (n / 2), J = ceil_fourth_root(N);
            unsigned oracle = 0, cap20 = 0, cap40 = 0, cap64 = 0;
            std::size_t min_omega = std::numeric_limits<std::size_t>::max();
            std::size_t max_omega = 0, sum_omega = 0;
            u64 best_u = 0, best_i = 0, best_capped_product = 0;
            std::vector<u64> best_factors;

            for (u64 u = 1; u <= 255; u += 2) {
                u64 Q = static_cast<u64>((static_cast<u128>(u) * N) / B);
                std::set<u64> factor_set;
                for (int c = -4; c <= 4; ++c) {
                    if (c < 0 && Q < static_cast<u64>(2 - c)) continue;
                    u64 A = c < 0 ? Q - static_cast<u64>(-c)
                                  : Q + static_cast<u64>(c);
                    if (A >= 2) factor_fast_d03(A, primes, factor_set);
                }
                factor_set.erase(2);
                for (auto it = factor_set.begin(); it != factor_set.end();) {
                    if (N % *it == 0) it = factor_set.erase(it);
                    else ++it;
                }
                std::size_t omega = factor_set.size();
                min_omega = std::min(min_omega, omega);
                max_omega = std::max(max_omega, omega);
                sum_omega += omega;

                std::vector<u64> products(256, 1);
                std::vector<std::vector<u64>> factors_by_i(256);
                for (u64 ell : factor_set) {
                    u64 x = 1 % ell, Nm = N % ell, pm = p % ell;
                    for (u64 i = 0; i < 256; ++i) {
                        if (x == pm) {
                            if (products[i] < J) {
                                u128 z = static_cast<u128>(products[i]) * ell;
                                products[i] = z >= J ? J : static_cast<u64>(z);
                            }
                            factors_by_i[i].push_back(ell);
                        }
                        x = mul_mod(x, Nm, ell);
                    }
                }
                bool terminal = false;
                for (u64 i = 0; i < 256; ++i) {
                    if (products[i] >= J) terminal = true;
                    if (products[i] > best_capped_product) {
                        best_capped_product = products[i];
                        best_u = u;
                        best_i = i;
                        best_factors = factors_by_i[i];
                    }
                }
                if (terminal) {
                    ++oracle;
                    if (omega <= 20) ++cap20;
                    if (omega <= 40) ++cap40;
                    if (omega <= 64) ++cap64;
                }
            }
            if (oracle == 0) ++zero_oracle;
            oracle_total += oracle;
            cap20_total += cap20;
            cap40_total += cap40;
            cap64_total += cap64;
            out << k << '\t' << row << '\t' << p << '\t' << q << '\t' << N
                << '\t' << n << '\t' << J << '\t' << oracle << '\t' << cap20
                << '\t' << cap40 << '\t' << cap64 << '\t' << min_omega << '\t'
                << max_omega << '\t' << sum_omega << '\t' << best_u << '\t'
                << best_i << '\t' << exact_product(best_factors) << '\t'
                << join(best_factors) << '\n';
        }
        std::cout << "k=" << k << " zero_oracle=" << zero_oracle
                  << " oracle_total=" << oracle_total
                  << " cap20_total=" << cap20_total
                  << " cap40_total=" << cap40_total
                  << " cap64_total=" << cap64_total << '\n';
    }
    const double seconds = std::chrono::duration<double>(
        std::chrono::steady_clock::now() - started).count();
    std::cout << "elapsed_seconds=" << seconds << '\n';
    return 0;
}
