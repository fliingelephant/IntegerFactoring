#include <inttypes.h>
#include <math.h>
#include <stdint.h>
#include <stdio.h>

static uint64_t mul_mod(uint64_t a, uint64_t b, uint64_t m) {
    return (uint64_t)((__uint128_t)a * b % m);
}

static uint64_t pow_mod(uint64_t a, uint64_t e, uint64_t m) {
    uint64_t y = 1;
    while (e) {
        if (e & 1) y = mul_mod(y, a, m);
        a = mul_mod(a, a, m);
        e >>= 1;
    }
    return y;
}

static int is_prime(uint64_t n) {
    if (n < 2) return 0;
    if (!(n & 1)) return n == 2;
    if (n % 3 == 0) return n == 3;
    for (uint64_t k = 5; (__uint128_t)k * k <= n; k += 6) {
        if (n % k == 0 || n % (k + 2) == 0) return 0;
    }
    return 1;
}

static uint64_t next_prime(uint64_t n) {
    if (n <= 2) return 2;
    if (!(n & 1)) ++n;
    while (!is_prime(n)) n += 2;
    return n;
}

static uint64_t floor_sqrt(uint64_t n) {
    uint64_t x = (uint64_t)sqrtl((long double)n);
    while ((__uint128_t)(x + 1) * (x + 1) <= n) ++x;
    while ((__uint128_t)x * x > n) --x;
    return x;
}

static uint64_t ceil_sqrt_half(uint64_t n) {
    uint64_t x = floor_sqrt(n / 2);
    while ((__uint128_t)2 * x * x < n) ++x;
    while (x && (__uint128_t)2 * (x - 1) * (x - 1) >= n) --x;
    return x;
}

static uint64_t cross_value(uint64_t a, uint64_t e, uint64_t m) {
    uint64_t u = pow_mod((a + 1) % m, e, m);
    uint64_t v = pow_mod(a, e, m);
    return (u + m - v + m - 1) % m;
}

int main(void) {
    static const unsigned bits[] = {12, 14, 16, 18, 20};
    static const long double alphas[] = {0.60L, 0.70L, 0.80L, 0.90L};

    puts("b\tj\talpha100\tp\tq\td\tN\tt\tL\tlo\thi\tH\texact\tp_only\tq_only\tboth\tneither");
    for (size_t ib = 0; ib < sizeof(bits) / sizeof(bits[0]); ++ib) {
        unsigned b = bits[ib];
        uint64_t base = UINT64_C(1) << b;
        for (unsigned j = 0; j < 4; ++j) {
            uint64_t p = next_prime(base + j * (base / 7));
            for (size_t ia = 0; ia < sizeof(alphas) / sizeof(alphas[0]); ++ia) {
                uint64_t offset = (uint64_t)floorl(powl((long double)p, alphas[ia]));
                uint64_t q = next_prime(p + offset);
                if (q >= 2 * p) continue;
                uint64_t d = q - p;
                uint64_t N = p * q;
                uint64_t lo = ceil_sqrt_half(N);
                uint64_t hi = floor_sqrt(N);

                unsigned ts[6];
                size_t nt = 0;
                for (unsigned z = 0; z <= 5; ++z) {
                    unsigned t = z * b / 10;
                    if (!nt || ts[nt - 1] != t) ts[nt++] = t;
                }

                uint64_t H[6] = {0}, exact[6] = {0}, p_only[6] = {0};
                uint64_t q_only[6] = {0}, both[6] = {0}, neither[6] = {0};
                for (uint64_t x = lo; x <= hi; ++x) {
                    uint64_t ap = x % p;
                    uint64_t aq = x % q;
                    int zp = cross_value(ap, d + 1, p) == 0;
                    int zq = cross_value(aq, p, q) == 0;
                    uint64_t diff = x >= p ? x - p : p - x;
                    unsigned valuation = diff ? (unsigned)__builtin_ctzll(diff) : 63;

                    for (size_t it = 0; it < nt; ++it) {
                        unsigned t = ts[it];
                        if (valuation < t) continue;
                        ++H[it];
                        if (x == p) {
                            ++exact[it];
                        } else if (zp && zq) {
                            ++both[it];
                        } else if (zp) {
                            ++p_only[it];
                        } else if (zq) {
                            ++q_only[it];
                        } else {
                            ++neither[it];
                        }
                    }
                }

                for (size_t it = 0; it < nt; ++it) {
                    unsigned t = ts[it];
                    printf("%u\t%u\t%u\t%" PRIu64 "\t%" PRIu64 "\t%" PRIu64
                           "\t%" PRIu64 "\t%u\t%" PRIu64 "\t%" PRIu64 "\t%" PRIu64
                           "\t%" PRIu64 "\t%" PRIu64 "\t%" PRIu64 "\t%" PRIu64
                           "\t%" PRIu64 "\t%" PRIu64 "\n",
                           b, j, (unsigned)llroundl(100 * alphas[ia]), p, q, d, N,
                           t, UINT64_C(1) << t, lo, hi, H[it], exact[it], p_only[it],
                           q_only[it], both[it], neither[it]);
                }
            }
        }
    }
    return 0;
}
