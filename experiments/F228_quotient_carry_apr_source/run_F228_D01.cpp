#include <algorithm>
#include <chrono>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <limits>
#include <numeric>
#include <set>
#include <stdexcept>
#include <string>
#include <tuple>
#include <vector>

using u64 = std::uint64_t;
using u128 = __uint128_t;

static u64 mul_mod(u64 a, u64 b, u64 m) {
    return static_cast<u64>((static_cast<u128>(a) * b) % m);
}

static u64 pow_mod(u64 a, u64 e, u64 m) {
    u64 r = 1 % m;
    while (e) {
        if (e & 1) r = mul_mod(r, a, m);
        a = mul_mod(a, a, m);
        e >>= 1;
    }
    return r;
}

static bool is_prime(u64 n) {
    if (n < 2) return false;
    for (u64 p : {2ULL, 3ULL, 5ULL, 7ULL, 11ULL, 13ULL, 17ULL, 19ULL,
                  23ULL, 29ULL, 31ULL, 37ULL}) {
        if (n % p == 0) return n == p;
    }
    u64 d = n - 1, s = 0;
    while ((d & 1) == 0) {
        d >>= 1;
        ++s;
    }
    for (u64 a : {2ULL, 325ULL, 9375ULL, 28178ULL, 450775ULL,
                  9780504ULL, 1795265022ULL}) {
        if (a % n == 0) continue;
        u64 x = pow_mod(a % n, d, n);
        if (x == 1 || x == n - 1) continue;
        bool witness = true;
        for (u64 r = 1; r < s; ++r) {
            x = mul_mod(x, x, n);
            if (x == n - 1) {
                witness = false;
                break;
            }
        }
        if (witness) return false;
    }
    return true;
}

static u64 ceil_fourth_root(u64 n) {
    u64 lo = 0, hi = 1;
    auto fourth_lt = [n](u64 x) {
        u128 y = static_cast<u128>(x) * x;
        return y * y < n;
    };
    while (fourth_lt(hi)) hi <<= 1;
    while (lo + 1 < hi) {
        u64 mid = lo + (hi - lo) / 2;
        if (fourth_lt(mid)) lo = mid;
        else hi = mid;
    }
    return hi;
}

static std::vector<unsigned> sieve(unsigned limit) {
    std::vector<bool> mark(limit + 1, true);
    mark[0] = mark[1] = false;
    for (unsigned p = 2; p * p <= limit; ++p) {
        if (!mark[p]) continue;
        for (unsigned k = p * p; k <= limit; k += p) mark[k] = false;
    }
    std::vector<unsigned> primes;
    for (unsigned p = 2; p <= limit; ++p) if (mark[p]) primes.push_back(p);
    return primes;
}

static void factor_distinct(u64 x, const std::vector<unsigned>& primes,
                            std::set<u64>& out) {
    for (u64 p : primes) {
        if (p * p > x) break;
        if (x % p != 0) continue;
        out.insert(p);
        while (x % p == 0) x /= p;
    }
    if (x > 1) out.insert(x);
}

static std::string join(const std::vector<u64>& xs) {
    std::string s;
    for (std::size_t j = 0; j < xs.size(); ++j) {
        if (j) s += ',';
        s += std::to_string(xs[j]);
    }
    return s.empty() ? "-" : s;
}

static std::string exact_product(const std::vector<u64>& xs) {
    static constexpr u64 base = 1000000000ULL;
    std::vector<u64> limbs(1, 1);
    for (u64 x : xs) {
        u128 carry = 0;
        for (u64& limb : limbs) {
            u128 z = static_cast<u128>(limb) * x + carry;
            limb = static_cast<u64>(z % base);
            carry = z / base;
        }
        while (carry) {
            limbs.push_back(static_cast<u64>(carry % base));
            carry /= base;
        }
    }
    std::string s = std::to_string(limbs.back());
    for (auto it = limbs.rbegin() + 1; it != limbs.rend(); ++it) {
        std::string block = std::to_string(*it);
        s += std::string(9 - block.size(), '0') + block;
    }
    return s;
}

int main(int argc, char** argv) {
    if (argc != 2) throw std::runtime_error("usage: run_F228_D01 OUTPUT.tsv");
    const auto started = std::chrono::steady_clock::now();

    std::vector<u64> safe;
    for (u64 r = (1ULL << 18) | 1; safe.size() < 513; r += 2) {
        if (is_prime(r) && is_prime((r - 1) / 2)) safe.push_back(r);
    }
    for (std::size_t j = 0; j < 512; ++j) {
        if (safe[j + 1] >= 2 * safe[j]) throw std::runtime_error("cohort not balanced");
    }

    u64 max_n = safe[511] * safe[512];
    unsigned max_bits = 64 - __builtin_clzll(max_n);
    u64 max_a = 255ULL * (1ULL << ((max_bits + 1) / 2)) + 4;
    unsigned trial_limit = 1;
    while (static_cast<u64>(trial_limit) * trial_limit < max_a) ++trial_limit;
    auto primes = sieve(trial_limit);

    std::ofstream out(argv[1]);
    if (!out) throw std::runtime_error("cannot open output");
    out << "row\tp\tq\tN\tn\tB\tJ\tsuccess_num\ttrials\tcap_rejects"
           "\tbest_u\tbest_i\tbest_omega\tbest_product\tbest_primes\n";

    unsigned zero_rows = 0;
    u64 min_success = 129, max_success = 0, total_success = 0;
    for (std::size_t row = 0; row < 512; ++row) {
        u64 p = safe[row], q = safe[row + 1], N = p * q;
        unsigned n = 64 - __builtin_clzll(N);
        u64 B = 1ULL << (n / 2);
        u64 J = ceil_fourth_root(N);
        unsigned success = 0, cap_rejects = 0;
        u64 best_u = 0, best_i = 0;
        std::size_t best_omega = 0;
        u64 best_capped_product = 0;
        std::vector<u64> best_factors;

        for (u64 u = 1; u <= 255; u += 2) {
            u64 Q = static_cast<u64>((static_cast<u128>(u) * N) / B);
            std::set<u64> factor_set;
            for (int c = -4; c <= 4; ++c) {
                if (c < 0 && Q < static_cast<u64>(2 - c)) continue;
                u64 A = c < 0 ? Q - static_cast<u64>(-c) : Q + static_cast<u64>(c);
                if (A >= 2) factor_distinct(A, primes, factor_set);
            }
            factor_set.erase(2);
            for (auto it = factor_set.begin(); it != factor_set.end();) {
                if (N % *it == 0) it = factor_set.erase(it);
                else ++it;
            }
            if (factor_set.size() > 20) {
                ++cap_rejects;
                continue;
            }

            std::vector<u64> products(256, 1);
            std::vector<std::vector<u64>> factors_by_i(256);
            for (u64 ell : factor_set) {
                u64 x = 1 % ell;
                u64 Nm = N % ell;
                u64 pm = p % ell;
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
                    best_omega = factor_set.size();
                    best_factors = factors_by_i[i];
                }
            }
            if (terminal) ++success;
        }

        if (success == 0) ++zero_rows;
        min_success = std::min<u64>(min_success, success);
        max_success = std::max<u64>(max_success, success);
        total_success += success;
        out << row << '\t' << p << '\t' << q << '\t' << N << '\t' << n
            << '\t' << B << '\t' << J << '\t' << success << "\t128\t"
            << cap_rejects << '\t' << best_u << '\t' << best_i << '\t'
            << best_omega << '\t' << exact_product(best_factors) << '\t'
            << join(best_factors)
            << '\n';
    }
    out.close();
    const double seconds = std::chrono::duration<double>(
        std::chrono::steady_clock::now() - started).count();
    std::cout << "rows=512 zero_rows=" << zero_rows
              << " min_success=" << min_success
              << " max_success=" << max_success
              << " total_success=" << total_success
              << " elapsed_seconds=" << seconds << '\n';
    return 0;
}
