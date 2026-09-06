#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <map>
#include <numeric>
#include <string>
#include <tuple>
#include <utility>
#include <vector>

using u64 = std::uint64_t;
using u128 = __uint128_t;

struct Row {
    u64 p, q, N, B, H, sp, sq;
    int n, e;
    u64 D, ordNp, ordNq, ordHp, ordHq;
    std::array<u64, 5> residual;
};

static u64 powmod(u64 a, u64 e, u64 m) {
    if (m == 1) return 0;
    u64 r = 1 % m;
    while (e) {
        if (e & 1) r = (u128)r * a % m;
        a = (u128)a * a % m;
        e >>= 1;
    }
    return r;
}

static int bitlen(u64 x) {
    return 64 - __builtin_clzll(x);
}

static int v2(u64 x) {
    return __builtin_ctzll(x);
}

static u64 inverse_odd_power_two(u64 a, u64 m) {
    // Newton inversion modulo 2^64, followed by masking to the requested modulus.
    u64 x = a;
    for (int i = 0; i < 6; ++i) x *= 2 - a * x;
    return x & (m - 1);
}

static std::vector<std::pair<u64, int>> factor(u64 x, const std::vector<int>& spf) {
    std::vector<std::pair<u64, int>> f;
    while (x > 1) {
        u64 p = spf[x];
        int e = 0;
        do { x /= p; ++e; } while (x % p == 0);
        f.push_back({p, e});
    }
    return f;
}

static u64 euler_phi(u64 x, const std::vector<int>& spf) {
    u64 r = x;
    for (auto [p, e] : factor(x, spf)) r = r / p * (p - 1);
    return r;
}

static u64 multiplicative_order(u64 a, u64 m, const std::vector<int>& spf) {
    if (m == 1) return 1;
    u64 ord = euler_phi(m, spf);
    for (auto [r, ignored] : factor(ord, spf)) {
        while (ord % r == 0 && powmod(a, ord / r, m) == 1) ord /= r;
    }
    return ord;
}

static u64 remove_supported_primes(u64 s, u64 a) {
    while (true) {
        u64 d = std::gcd(s, a);
        if (d == 1) return s;
        s /= d;
    }
}

static u64 word_residual(u64 s, u64 N, u64 H, int n, int kind) {
    if (s == 1) return 1;
    u64 w = 1 % s;
    if (kind == 0 || kind == 3) {
        for (int k = 1; k <= n; ++k) {
            u64 z = powmod(N, k, s);
            w = (u128)w * ((z + s - 1) % s) % s;
        }
    }
    if (kind == 1 || kind == 3) {
        for (int k = 1; k <= n; ++k) {
            u64 hk = 1;
            bool zero_integer = (H == 1);
            if (!zero_integer) {
                hk = powmod(H, k, s);
                w = (u128)w * ((hk + s - 1) % s) % s;
            }
        }
    }
    if (kind == 2 || kind == 3) {
        for (int u = 1; u <= n; ++u) {
            for (int c = -n; c <= n; ++c) {
                std::int64_t A = (std::int64_t)u * (std::int64_t)H + c;
                if (A <= 0) continue;
                w = (u128)w * powmod((u64)A, n, s) % s;
            }
        }
    }
    if (kind == 4) {
        for (int k = 2; k <= n; ++k) w = (u128)w * k % s;
    }
    return s / std::gcd(s, w);
}

static void print_factors(u64 x, const std::vector<int>& spf) {
    auto fs = factor(x, spf);
    if (fs.empty()) { std::cout << "1"; return; }
    for (std::size_t i = 0; i < fs.size(); ++i) {
        if (i) std::cout << "*";
        std::cout << fs[i].first;
        if (fs[i].second > 1) std::cout << "^" << fs[i].second;
    }
}

static void print_row(const Row& r, const std::vector<int>& spf) {
    std::cout << "p=" << r.p << " q=" << r.q << " N=" << r.N
              << " n=" << r.n << " B=" << r.B << " H=" << r.H
              << " gap=" << (r.q-r.p) << " e=" << r.e << " D=" << r.D
              << " sp=" << r.sp << "(";
    print_factors(r.sp, spf);
    std::cout << ") sq=" << r.sq << "(";
    print_factors(r.sq, spf);
    std::cout << ") ordN=(" << r.ordNp << "," << r.ordNq << ")"
              << " ordH=(" << r.ordHp << "," << r.ordHq << ")"
              << " residuals=[";
    for (int i = 0; i < 5; ++i) {
        if (i) std::cout << ",";
        std::cout << r.residual[i];
    }
    std::cout << "] centered_H={";
    bool first = true;
    for (u64 s : {r.sp, r.sq}) {
        for (auto [ell, ignored] : factor(s, spf)) {
            u64 z = r.H % ell;
            std::int64_t centered = z <= ell/2 ? (std::int64_t)z : (std::int64_t)z-(std::int64_t)ell;
            if (!first) std::cout << ",";
            first = false;
            std::cout << ell << ":" << centered;
        }
    }
    std::cout << "}\n";
}

int main() {
    constexpr int P_LIMIT = 1 << 22;
    constexpr int Q_LIMIT = 1 << 23;
    std::vector<int> spf(Q_LIMIT, 0), primes;
    primes.reserve(600000);
    for (int i = 2; i < Q_LIMIT; ++i) {
        if (!spf[i]) { spf[i] = i; primes.push_back(i); }
        for (int p : primes) {
            if (p > spf[i] || (u64)i * p >= Q_LIMIT) break;
            spf[i*p] = p;
        }
    }

    std::map<int, u64> counts;
    std::vector<Row> records;
    std::array<u64, 7> maxima{}; // min ord N, min ord H, then five menu residuals
    std::vector<Row> worst;
    u64 total = 0;

    for (int pi : primes) {
        if (pi >= P_LIMIT) break;
        if (pi == 2) continue;
        u64 p = pi;
        int nlo = bitlen(p*p);
        int nhi = bitlen(2*p*p-1);
        for (int n = nlo; n <= nhi; ++n) {
            u64 B = u64(1) << (n/2);
            u64 r = inverse_odd_power_two(p, B);
            std::int64_t k0 = ((std::int64_t)p - (std::int64_t)r) / (std::int64_t)B - 1;
            for (std::int64_t k = std::max<std::int64_t>(0,k0); k <= k0+5; ++k) {
                u64 q = r + (u64)k*B;
                if (!(p < q && q < 2*p) || q >= Q_LIMIT || spf[q] != (int)q) continue;
                u64 N = p*q;
                if (bitlen(N) != n || (N-1)%B != 0) continue;
                int ep = v2(p-1), eq = v2(q-1);
                if (ep != eq) {
                    std::cerr << "valuation mismatch p=" << p << " q=" << q << "\n";
                    return 2;
                }
                u64 P=(p-1)>>ep, Q=(q-1)>>eq, D=std::gcd(P,Q), sp=P/D, sq=Q/D;
                Row row{p,q,N,B,(N-1)/B,sp,sq,n,ep,D};
                row.ordNp=multiplicative_order(N%sp,sp,spf);
                row.ordNq=multiplicative_order(N%sq,sq,spf);
                {
                    u64 hp=remove_supported_primes(sp,row.H), hq=remove_supported_primes(sq,row.H);
                    row.ordHp=multiplicative_order(row.H%hp,hp,spf);
                    row.ordHq=multiplicative_order(row.H%hq,hq,spf);
                }
                for (int j=0;j<5;++j) {
                    u64 rp=word_residual(sp,N,row.H,n,j);
                    u64 rq=word_residual(sq,N,row.H,n,j);
                    row.residual[j]=std::min(rp,rq);
                }
                ++total; ++counts[n];
                std::array<u64,7> vals{std::min(row.ordNp,row.ordNq),
                                       std::min(row.ordHp,row.ordHq),
                                       row.residual[0],row.residual[1],row.residual[2],
                                       row.residual[3],row.residual[4]};
                bool rec=false;
                for (int j=0;j<7;++j) if (vals[j]>maxima[j]) { maxima[j]=vals[j]; rec=true; }
                if (rec) records.push_back(row);
                worst.push_back(row);
            }
        }
    }

    std::cout << "TOTAL " << total << "\nCOUNTS";
    for (auto [n,c] : counts) std::cout << " " << n << ":" << c;
    std::cout << "\nMAX min_ordN=" << maxima[0] << " min_ordH=" << maxima[1]
              << " residual_WN=" << maxima[2] << " residual_WH=" << maxima[3]
              << " residual_shift=" << maxima[4] << " residual_combined=" << maxima[5]
              << " residual_factorial=" << maxima[6] << "\n";
    std::cout << "RECORDS " << records.size() << "\n";
    for (const auto& row : records) print_row(row,spf);
    std::sort(worst.begin(),worst.end(),[](const Row&a,const Row&b){
        if (a.residual[3]!=b.residual[3]) return a.residual[3]>b.residual[3];
        return a.N>b.N;
    });
    std::cout << "WORST_COMBINED\n";
    for (std::size_t i=0;i<std::min<std::size_t>(10,worst.size());++i) print_row(worst[i],spf);
}
