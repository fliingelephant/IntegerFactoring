#include <algorithm>
#include <array>
#include <cmath>
#include <cstdint>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <stdexcept>
#include <string>
#include <tuple>
#include <unordered_set>
#include <utility>
#include <vector>

using u64 = std::uint64_t;
using u128 = __uint128_t;

static u64 splitmix_state = 0xF232D01C0FFEE123ULL;

static u64 splitmix64() {
    u64 z = (splitmix_state += 0x9E3779B97F4A7C15ULL);
    z = (z ^ (z >> 30)) * 0xBF58476D1CE4E5B9ULL;
    z = (z ^ (z >> 27)) * 0x94D049BB133111EBULL;
    return z ^ (z >> 31);
}

static int bit_length(u64 x) {
    return x == 0 ? 0 : 64 - __builtin_clzll(x);
}

static u64 mul_mod(u64 a, u64 b, u64 m) {
    return static_cast<u64>((static_cast<u128>(a) * b) % m);
}

static u64 pow_mod(u64 a, u64 e, u64 m) {
    u64 r = 1;
    while (e != 0) {
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
    u64 d = n - 1;
    int s = 0;
    while ((d & 1) == 0) {
        d >>= 1;
        ++s;
    }
    for (u64 a : {2ULL, 325ULL, 9375ULL, 28178ULL, 450775ULL,
                  9780504ULL, 1795265022ULL}) {
        if (a % n == 0) continue;
        u64 x = pow_mod(a % n, d, n);
        if (x == 1 || x == n - 1) continue;
        bool composite = true;
        for (int r = 1; r < s; ++r) {
            x = mul_mod(x, x, n);
            if (x == n - 1) {
                composite = false;
                break;
            }
        }
        if (composite) return false;
    }
    return true;
}

static u64 pollard_brent(u64 n) {
    if ((n & 1) == 0) return 2;
    if (n % 3 == 0) return 3;
    while (true) {
        const u64 y0 = 1 + splitmix64() % (n - 1);
        const u64 c = 1 + splitmix64() % (n - 1);
        const u64 block = 128;
        u64 y = y0;
        u64 r = 1;
        u64 q = 1;
        u64 g = 1;
        u64 x = 0;
        u64 ys = 0;
        while (g == 1) {
            x = y;
            for (u64 i = 0; i < r; ++i) y = (mul_mod(y, y, n) + c) % n;
            for (u64 k = 0; k < r && g == 1; k += block) {
                ys = y;
                const u64 lim = std::min(block, r - k);
                for (u64 i = 0; i < lim; ++i) {
                    y = (mul_mod(y, y, n) + c) % n;
                    const u64 diff = x > y ? x - y : y - x;
                    q = mul_mod(q, diff, n);
                }
                g = std::gcd(q, n);
            }
            if (r > (1ULL << 61)) break;
            r <<= 1;
        }
        if (g == n) {
            do {
                ys = (mul_mod(ys, ys, n) + c) % n;
                const u64 diff = x > ys ? x - ys : ys - x;
                g = std::gcd(diff, n);
            } while (g == 1);
        }
        if (g > 1 && g < n) return g;
    }
}

static void factor_rec(u64 n, std::map<u64, int>& out) {
    if (n == 1) return;
    if (is_prime(n)) {
        ++out[n];
        return;
    }
    const u64 d = pollard_brent(n);
    factor_rec(d, out);
    factor_rec(n / d, out);
}

static std::map<u64, int> factor(u64 n) {
    std::map<u64, int> out;
    factor_rec(n, out);
    return out;
}

static std::string factor_string(const std::map<u64, int>& f) {
    if (f.empty()) return "1";
    std::ostringstream s;
    bool first = true;
    for (const auto& [p, e] : f) {
        if (!first) s << '*';
        first = false;
        s << p;
        if (e != 1) s << '^' << e;
    }
    return s.str();
}

static u64 odd_part(u64 x) {
    while ((x & 1) == 0) x >>= 1;
    return x;
}

static u64 inverse_mod_power_two(u64 a, u64 modulus) {
    u64 x = 1;
    for (int i = 0; i < 6; ++i) x *= 2 - a * x;
    return x & (modulus - 1);
}

struct CorpusRow {
    std::string split;
    int target_n;
    int index;
    u64 p;
    u64 q;
    u64 N;
};

static std::vector<CorpusRow> make_corpus(const std::string& split,
                                          const std::vector<int>& targets,
                                          int rows_per_target) {
    std::vector<CorpusRow> rows;
    for (int n : targets) {
        const int m = n / 2;
        const u64 B = 1ULL << m;
        const u64 lo = B / 2 + 1;
        const u64 hi = B + B / 2 - 1;
        std::set<u64> seen;
        int attempts = 0;
        while (static_cast<int>(seen.size()) < rows_per_target) {
            if (++attempts > 5000000) throw std::runtime_error("corpus generation exhausted");
            u64 p = lo + splitmix64() % (hi - lo + 1);
            p |= 1;
            if (p > hi || !is_prime(p)) continue;
            const u64 v = inverse_mod_power_two(p, B);
            for (u64 k = 0; k <= 4 && static_cast<int>(seen.size()) < rows_per_target; ++k) {
                const u64 q = v + k * B;
                if (!(p < q && q < 2 * p)) continue;
                if (!is_prime(q)) continue;
                const u64 N = p * q;
                if (bit_length(N) != n) continue;
                if ((N - 1) % B != 0) throw std::runtime_error("zero-defect invariant failed");
                if (!seen.insert(N).second) continue;
                rows.push_back({split, n, static_cast<int>(seen.size()) - 1, p, q, N});
            }
        }
    }
    return rows;
}

static std::vector<u64> primes_through(u64 y) {
    std::vector<bool> sieve(y + 1, true);
    if (y >= 0) sieve[0] = false;
    if (y >= 1) sieve[1] = false;
    for (u64 p = 2; p * p <= y; ++p) {
        if (!sieve[p]) continue;
        for (u64 k = p * p; k <= y; k += p) sieve[k] = false;
    }
    std::vector<u64> ps;
    for (u64 p = 2; p <= y; ++p) if (sieve[p]) ps.push_back(p);
    return ps;
}

struct Witness {
    int u;
    int c;
    u64 A;
};

struct DirectEvent {
    std::string kind;
    int u;
    int c;
    u64 value;
    u64 factor;
};

struct PublicWord {
    int n;
    u64 B;
    u64 H;
    int Y;
    int U;
    int C;
    std::map<u64, int> H_factor;
    std::set<u64> base_support;
    std::set<u64> menu_support;
    std::map<u64, Witness> first_witness;
    std::vector<DirectEvent> direct_events;
    int shifted_children = 0;
};

// This function deliberately accepts N only. Hidden p and q cannot affect
// the public menu, its factorizations, or its first-witness map.
static PublicWord build_public_word(u64 N) {
    PublicWord w{};
    w.n = bit_length(N);
    w.B = 1ULL << (w.n / 2);
    if ((N - 1) % w.B != 0) throw std::runtime_error("row is not zero-defect");
    w.H = (N - 1) / w.B;
    w.Y = w.n * w.n;
    w.U = w.n;
    w.C = bit_length(static_cast<u64>(w.n));
    w.H_factor = factor(w.H);
    for (u64 ell : primes_through(w.Y)) w.base_support.insert(ell);
    for (const auto& [ell, e] : w.H_factor) {
        (void)e;
        w.base_support.insert(ell);
    }
    w.menu_support = w.base_support;

    for (int u = 1; u <= w.U; u += 2) {
        // c=0 is included analytically. Its support is contained in u and H,
        // and u<=Y, so it adds no prime to the baseline.
        for (int c = -w.C; c <= w.C; ++c) {
            if (c == 0) continue;
            ++w.shifted_children;
            const std::int64_t signed_A = static_cast<std::int64_t>(u * w.H) + c;
            if (signed_A <= 0) continue;
            const u64 A = static_cast<u64>(signed_A);
            const u64 g = std::gcd(A, N);
            if (g > 1 && g < N) w.direct_events.push_back({"A", u, c, A, g});
            const auto Af = factor(A);
            for (const auto& [ell, e] : Af) {
                (void)e;
                if (!w.menu_support.count(ell)) {
                    w.first_witness.emplace(ell, Witness{u, c, A});
                    w.menu_support.insert(ell);
                }
            }
            const u64 abs_c = static_cast<u64>(c < 0 ? -c : c);
            const u64 defect_gcd = std::gcd(abs_c * w.B, N);
            if (defect_gcd > 1 && defect_gcd < N)
                w.direct_events.push_back({"E", u, c, abs_c * w.B, defect_gcd});
            const auto cf = factor(abs_c);
            for (const auto& [ell, e] : cf) {
                (void)e;
                if (!w.base_support.count(ell)) {
                    throw std::runtime_error("defect supplied a nonbaseline prime");
                }
            }
        }
    }
    return w;
}

static u64 residual_from_support(const std::map<u64, int>& sf,
                                 const std::set<u64>& support) {
    u64 r = 1;
    for (const auto& [ell, e] : sf) {
        if (support.count(ell)) continue;
        for (int k = 0; k < e; ++k) r *= ell;
    }
    return r;
}

static u64 sum_phi_square_divisors(u64 D) {
    const auto f = factor(D);
    u128 total = 1;
    for (const auto& [ell, e] : f) {
        u128 local = 1;
        u128 phi = ell - 1;
        for (int k = 1; k <= e; ++k) {
            local += phi * phi;
            phi *= ell;
        }
        total *= local;
    }
    if (total > static_cast<u128>(UINT64_MAX)) throw std::runtime_error("phi-square overflow");
    return static_cast<u64>(total);
}

static std::string capture_string(const std::map<u64, int>& sf,
                                  const PublicWord& w) {
    std::ostringstream s;
    bool first = true;
    for (const auto& [ell, e] : sf) {
        if (w.base_support.count(ell) || !w.menu_support.count(ell)) continue;
        const auto it = w.first_witness.find(ell);
        if (it == w.first_witness.end()) throw std::runtime_error("missing witness");
        if (!first) s << ';';
        first = false;
        s << ell << '^' << e << '@' << it->second.u << ',' << it->second.c
          << ',' << it->second.A;
    }
    return first ? "-" : s.str();
}

static std::string direct_event_string(const PublicWord& w) {
    if (w.direct_events.empty()) return "-";
    std::ostringstream s;
    for (std::size_t i = 0; i < w.direct_events.size(); ++i) {
        if (i != 0) s << ';';
        const auto& e = w.direct_events[i];
        s << e.kind << '@' << e.u << ',' << e.c << ',' << e.value << ',' << e.factor;
    }
    return s.str();
}

struct Result {
    CorpusRow corpus;
    PublicWord word;
    u64 gap;
    u64 P;
    u64 Q;
    u64 D;
    u64 sp;
    u64 sq;
    std::map<u64, int> sp_factor;
    std::map<u64, int> sq_factor;
    u64 base_rp;
    u64 base_rq;
    u64 menu_rp;
    u64 menu_rq;
    long double base_min_bits;
    long double menu_min_bits;
    long double shrink_p_bits;
    long double shrink_q_bits;
    long double base_progress_M1;
    long double menu_progress_M1;
    long double base_progress_MD;
    long double menu_progress_MD;
    bool base_one;
    bool menu_one;
    bool base_qp;
    bool menu_qp;
    std::string captured_p;
    std::string captured_q;
};

static long double progress_probability(u64 rp, u64 rq, u64 P, u64 Q,
                                        u64 stale_numerator) {
    const long double union_return = 1.0L / rp + 1.0L / rq - 1.0L / (rp * (long double)rq);
    const long double stale = stale_numerator / (static_cast<long double>(P) * Q);
    return std::max(0.0L, union_return - stale);
}

static Result evaluate(const CorpusRow& c) {
    Result r{};
    r.corpus = c;
    r.word = build_public_word(c.N);
    r.gap = c.q - c.p;
    r.P = odd_part(c.p - 1);
    r.Q = odd_part(c.q - 1);
    r.D = std::gcd(r.P, r.Q);
    r.sp = r.P / r.D;
    r.sq = r.Q / r.D;
    r.sp_factor = factor(r.sp);
    r.sq_factor = factor(r.sq);
    r.base_rp = residual_from_support(r.sp_factor, r.word.base_support);
    r.base_rq = residual_from_support(r.sq_factor, r.word.base_support);
    r.menu_rp = residual_from_support(r.sp_factor, r.word.menu_support);
    r.menu_rq = residual_from_support(r.sq_factor, r.word.menu_support);
    r.base_min_bits = std::log2(static_cast<long double>(std::min(r.base_rp, r.base_rq)));
    r.menu_min_bits = std::log2(static_cast<long double>(std::min(r.menu_rp, r.menu_rq)));
    r.shrink_p_bits = std::log2(static_cast<long double>(r.base_rp) / r.menu_rp);
    r.shrink_q_bits = std::log2(static_cast<long double>(r.base_rq) / r.menu_rq);
    const u64 stale_D = sum_phi_square_divisors(r.D);
    r.base_progress_M1 = progress_probability(r.base_rp, r.base_rq, r.P, r.Q, 1);
    r.menu_progress_M1 = progress_probability(r.menu_rp, r.menu_rq, r.P, r.Q, 1);
    r.base_progress_MD = progress_probability(r.base_rp, r.base_rq, r.P, r.Q, stale_D);
    r.menu_progress_MD = progress_probability(r.menu_rp, r.menu_rq, r.P, r.Q, stale_D);
    r.base_one = std::min(r.base_rp, r.base_rq) == 1;
    r.menu_one = std::min(r.menu_rp, r.menu_rq) == 1;
    const u64 qcut = static_cast<u64>(r.word.n) * r.word.n * r.word.n * r.word.n;
    r.base_qp = std::min(r.base_rp, r.base_rq) <= qcut;
    r.menu_qp = std::min(r.menu_rp, r.menu_rq) <= qcut;
    r.captured_p = capture_string(r.sp_factor, r.word);
    r.captured_q = capture_string(r.sq_factor, r.word);
    if (!r.word.direct_events.empty()) {
        r.menu_progress_M1 = 1;
        r.menu_progress_MD = 1;
    }
    return r;
}

static std::string header() {
    return "split\ttarget_n\trow\tp\tq\tN\tgap\tB\tH\tY\tU\tC\tdirect_event_count\tdirect_events"
           "\tP\tQ\tD\tsp\tsq\tsp_factor\tsq_factor\tbase_rp\tbase_rq\tmenu_rp\tmenu_rq"
           "\tbase_min_bits\tmenu_min_bits\tshrink_p_bits\tshrink_q_bits"
           "\tbase_progress_M1\tmenu_progress_M1\tbase_progress_MD\tmenu_progress_MD"
           "\tbase_one\tmenu_one\tbase_n4\tmenu_n4\tbase_support_count\tmenu_support_count"
           "\tshifted_children\tcaptured_p\tcaptured_q";
}

static void write_row(std::ostream& out, const Result& r) {
    out << r.corpus.split << '\t' << r.corpus.target_n << '\t' << r.corpus.index
        << '\t' << r.corpus.p << '\t' << r.corpus.q << '\t' << r.corpus.N
        << '\t' << r.gap << '\t' << r.word.B << '\t' << r.word.H
        << '\t' << r.word.Y << '\t' << r.word.U << '\t' << r.word.C
        << '\t' << r.word.direct_events.size() << '\t' << direct_event_string(r.word)
        << '\t' << r.P << '\t' << r.Q << '\t' << r.D << '\t' << r.sp << '\t' << r.sq
        << '\t' << factor_string(r.sp_factor) << '\t' << factor_string(r.sq_factor)
        << '\t' << r.base_rp << '\t' << r.base_rq << '\t' << r.menu_rp << '\t' << r.menu_rq
        << '\t' << std::setprecision(18) << r.base_min_bits << '\t' << r.menu_min_bits
        << '\t' << r.shrink_p_bits << '\t' << r.shrink_q_bits
        << '\t' << std::scientific << r.base_progress_M1 << '\t' << r.menu_progress_M1
        << '\t' << r.base_progress_MD << '\t' << r.menu_progress_MD << std::defaultfloat
        << '\t' << r.base_one << '\t' << r.menu_one << '\t' << r.base_qp << '\t' << r.menu_qp
        << '\t' << r.word.base_support.size() << '\t' << r.word.menu_support.size()
        << '\t' << r.word.shifted_children << '\t' << r.captured_p << '\t' << r.captured_q
        << '\n';
}

static void write_summary(std::ostream& out, const std::vector<Result>& results) {
    out << "F232-D01 finite discovery summary\n";
    out << "rows=" << results.size() << "\n";
    for (const std::string split : {"train", "holdout"}) {
        std::vector<const Result*> rows;
        for (const auto& r : results) if (r.corpus.split == split) rows.push_back(&r);
        int direct = 0, base_one = 0, menu_one = 0, base_qp = 0, menu_qp = 0, no_gain = 0;
        long double shrink_sum = 0;
        long double min_progress = 1;
        const Result* worst = nullptr;
        for (const Result* r : rows) {
            direct += !r->word.direct_events.empty();
            base_one += r->base_one;
            menu_one += r->menu_one;
            base_qp += r->base_qp;
            menu_qp += r->menu_qp;
            no_gain += (r->base_rp == r->menu_rp && r->base_rq == r->menu_rq);
            shrink_sum += r->shrink_p_bits + r->shrink_q_bits;
            if (r->menu_progress_MD < min_progress) {
                min_progress = r->menu_progress_MD;
                worst = r;
            }
        }
        out << split << ": rows=" << rows.size() << " direct=" << direct
            << " base_one=" << base_one << " menu_one=" << menu_one
            << " base_n4=" << base_qp << " menu_n4=" << menu_qp
            << " no_gain=" << no_gain
            << " mean_total_shrink_bits=" << std::setprecision(12)
            << (rows.empty() ? 0 : shrink_sum / rows.size())
            << " min_menu_progress_MD=" << std::scientific << min_progress << std::defaultfloat;
        if (worst) out << " worst_N=" << worst->corpus.N;
        out << '\n';
        for (int target : (split == "train" ? std::vector<int>{30,34,38,42}
                                             : std::vector<int>{49,53,57,61})) {
            int count = 0, one = 0, qp = 0, zero = 0;
            long double shrink = 0;
            for (const Result* r : rows) if (r->corpus.target_n == target) {
                ++count;
                one += r->menu_one;
                qp += r->menu_qp;
                zero += (r->base_rp == r->menu_rp && r->base_rq == r->menu_rq);
                shrink += r->shrink_p_bits + r->shrink_q_bits;
            }
            out << "  n=" << target << " rows=" << count << " menu_one=" << one
                << " menu_n4=" << qp << " no_gain=" << zero
                << " mean_total_shrink_bits=" << (count ? shrink / count : 0) << '\n';
        }
    }
    out << "Interpretation: finite discovery evidence only; no asymptotic probability or runtime claim.\n";
}

int main(int argc, char** argv) {
    if (argc != 4) {
        std::cerr << "usage: F232_D01 OUTPUT.tsv SUMMARY.txt HOSTILE.tsv\n";
        return 2;
    }
    std::vector<CorpusRow> corpus;
    auto train = make_corpus("train", {30, 34, 38, 42}, 24);
    auto holdout = make_corpus("holdout", {49, 53, 57, 61}, 24);
    corpus.insert(corpus.end(), train.begin(), train.end());
    corpus.insert(corpus.end(), holdout.begin(), holdout.end());

    std::vector<Result> results;
    results.reserve(corpus.size());
    for (std::size_t i = 0; i < corpus.size(); ++i) {
        results.push_back(evaluate(corpus[i]));
        std::cerr << "completed " << (i + 1) << '/' << corpus.size() << '\n';
    }

    std::ofstream output(argv[1], std::ios::out | std::ios::trunc);
    if (!output) throw std::runtime_error("cannot open output");
    output << header() << '\n';
    for (const auto& r : results) write_row(output, r);

    std::ofstream summary(argv[2], std::ios::out | std::ios::trunc);
    if (!summary) throw std::runtime_error("cannot open summary");
    write_summary(summary, results);

    std::ofstream hostile(argv[3], std::ios::out | std::ios::trunc);
    if (!hostile) throw std::runtime_error("cannot open hostile output");
    hostile << "hostile_type\trank\t" << header() << '\n';
    for (const std::string split : {"train", "holdout"}) {
        std::vector<const Result*> v;
        for (const auto& r : results)
            if (r.corpus.split == split && r.word.direct_events.empty()) v.push_back(&r);
        std::sort(v.begin(), v.end(), [](const Result* a, const Result* b) {
            if (a->menu_progress_MD != b->menu_progress_MD)
                return a->menu_progress_MD < b->menu_progress_MD;
            return a->corpus.N < b->corpus.N;
        });
        for (int i = 0; i < std::min<int>(12, v.size()); ++i) {
            hostile << split << "_lowest_progress\t" << i + 1 << '\t';
            write_row(hostile, *v[i]);
        }
        std::sort(v.begin(), v.end(), [](const Result* a, const Result* b) {
            const long double ga = a->shrink_p_bits + a->shrink_q_bits;
            const long double gb = b->shrink_p_bits + b->shrink_q_bits;
            if (ga != gb) return ga < gb;
            return a->corpus.N < b->corpus.N;
        });
        for (int i = 0; i < std::min<int>(12, v.size()); ++i) {
            hostile << split << "_least_shrink\t" << i + 1 << '\t';
            write_row(hostile, *v[i]);
        }
    }
    return 0;
}
