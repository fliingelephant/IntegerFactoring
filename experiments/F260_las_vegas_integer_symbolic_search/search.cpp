#include <algorithm>
#include <array>
#include <atomic>
#include <chrono>
#include <cmath>
#include <cstdint>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <map>
#include <mutex>
#include <numeric>
#include <set>
#include <sstream>
#include <stdexcept>
#include <string>
#include <thread>
#include <tuple>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>

#include <sys/resource.h>

#include <boost/multiprecision/cpp_int.hpp>

using boost::multiprecision::cpp_int;
using u64 = std::uint64_t;
using u128 = __uint128_t;

static constexpr int DISCOVERY_BITS[] = {16, 24, 32};
static constexpr int HELDOUT_BITS[] = {40, 48, 56, 60};
static constexpr int D_VALUES[] = {2, 3, 5, 6, 7, 10, 11, 13};
static constexpr int MAX_SEQUENCE = 24;
static constexpr int MAX_PROGRAMS_PER_TYPE = 4096;
static constexpr u64 MASTER_SEED = 0xF260D01A6C3E91B7ULL;
static constexpr int COHORTS = 3;
static const char* COHORT_NAMES[] = {"random", "safe_safe", "consecutive"};

static long double timeval_seconds(const timeval& t) {
  return static_cast<long double>(t.tv_sec) +
         static_cast<long double>(t.tv_usec) / 1000000.0L;
}

static void print_process_resources(const char* tag,
                                    std::chrono::steady_clock::time_point start) {
  rusage usage{};
  if (getrusage(RUSAGE_SELF, &usage) != 0)
    throw std::runtime_error("getrusage");
  const double wall = std::chrono::duration<double>(
      std::chrono::steady_clock::now() - start).count();
  std::cout << std::fixed << std::setprecision(6)
            << tag << "_wall_seconds=" << wall << ' '
            << tag << "_user_seconds=" << timeval_seconds(usage.ru_utime) << ' '
            << tag << "_system_seconds=" << timeval_seconds(usage.ru_stime) << ' '
            << tag << "_maxrss_kib=" << usage.ru_maxrss << '\n';
}

[[noreturn]] static void fail(const std::string& message) {
  throw std::runtime_error(message);
}

static void require(bool condition, const std::string& message) {
  if (!condition) fail(message);
}

static u64 mix64(u64 x) {
  x += 0x9e3779b97f4a7c15ULL;
  x = (x ^ (x >> 30)) * 0xbf58476d1ce4e5b9ULL;
  x = (x ^ (x >> 27)) * 0x94d049bb133111ebULL;
  return x ^ (x >> 31);
}

struct Rng {
  u64 state;
  explicit Rng(u64 seed) : state(seed) {}
  u64 next() { return state = mix64(state); }
};

static u64 mul_mod(u64 a, u64 b, u64 m) {
  if (m == 1) return 0;
  return static_cast<u64>((static_cast<u128>(a) * b) % m);
}

static u64 pow_mod(u64 a, u64 e, u64 m) {
  if (m == 1) return 0;
  u64 out = 1 % m;
  while (e) {
    if (e & 1) out = mul_mod(out, a, m);
    a = mul_mod(a, a, m);
    e >>= 1;
  }
  return out;
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

static u64 random_prime(int bits, Rng& rng) {
  require(bits >= 3 && bits <= 60, "prime bit range");
  const u64 low = 1ULL << (bits - 1);
  const u64 high = (1ULL << bits) - 1;
  for (;;) {
    u64 x = (rng.next() & high) | low | 1ULL;
    for (int k = 0; k < 8192 && x <= high; ++k, x += 2) {
      if (is_prime(x)) return x;
    }
  }
}

static u64 random_safe_prime(int bits, Rng& rng) {
  for (;;) {
    u64 r = random_prime(bits - 1, rng);
    u64 p = 2 * r + 1;
    if ((p >> (bits - 1)) == 1 && is_prime(p)) return p;
  }
}

static u64 next_prime(u64 p) {
  u64 q = p + 2;
  while (!is_prime(q)) q += 2;
  return q;
}

static u64 pollard_brent(u64 n, Rng& rng) {
  if ((n & 1) == 0) return 2;
  if (n % 3 == 0) return 3;
  for (;;) {
    u64 y = 1 + rng.next() % (n - 1);
    u64 c = 1 + rng.next() % (n - 1);
    const u64 block = 128;
    u64 r = 1, qprod = 1, g = 1, x = 0, ys = 0;
    while (g == 1) {
      x = y;
      for (u64 i = 0; i < r; ++i) y = (mul_mod(y, y, n) + c) % n;
      for (u64 k = 0; k < r && g == 1; k += block) {
        ys = y;
        const u64 lim = std::min(block, r - k);
        for (u64 i = 0; i < lim; ++i) {
          y = (mul_mod(y, y, n) + c) % n;
          u64 diff = x > y ? x - y : y - x;
          qprod = mul_mod(qprod, diff, n);
        }
        g = std::gcd(qprod, n);
      }
      if (r > (1ULL << 61)) break;
      r <<= 1;
    }
    if (g == n) {
      do {
        ys = (mul_mod(ys, ys, n) + c) % n;
        u64 diff = x > ys ? x - ys : ys - x;
        g = std::gcd(diff, n);
      } while (g == 1);
    }
    if (g > 1 && g < n) return g;
  }
}

static void factor_rec(u64 n, std::map<u64, int>& out, Rng& rng) {
  if (n == 1) return;
  if (is_prime(n)) {
    ++out[n];
    return;
  }
  u64 d = pollard_brent(n, rng);
  factor_rec(d, out, rng);
  factor_rec(n / d, out, rng);
}

static std::map<u64, int> factor_u64(u64 n, u64 seed) {
  std::map<u64, int> out;
  Rng rng(seed ^ n);
  factor_rec(n, out, rng);
  return out;
}

static int bit_length(u64 x) {
  return x ? 64 - __builtin_clzll(x) : 0;
}

static int bit_length(const cpp_int& x) {
  if (x == 0) return 0;
  return boost::multiprecision::msb(x < 0 ? -x : x) + 1;
}

static cpp_int abs_cpp(cpp_int x) { return x < 0 ? -x : x; }

static u64 mod_cpp(const cpp_int& x, u64 m) {
  if (m == 1) return 0;
  cpp_int r = x % m;
  if (r < 0) r += m;
  return r.convert_to<u64>();
}

static int v2_cpp(cpp_int x) {
  x = abs_cpp(x);
  if (x == 0) return 128;
  int v = 0;
  while ((x & 1) == 0 && v < 128) {
    x >>= 1;
    ++v;
  }
  return v;
}

static cpp_int isqrt_cpp(const cpp_int& n) {
  require(n >= 0, "sqrt nonnegative");
  if (n < 2) return n;
  cpp_int x = cpp_int(1) << ((bit_length(n) + 1) / 2);
  for (;;) {
    cpp_int y = (x + n / x) >> 1;
    if (y >= x) return x;
    x = y;
  }
}

static std::vector<cpp_int> sample_evenly(const std::vector<cpp_int>& in) {
  if (static_cast<int>(in.size()) <= MAX_SEQUENCE) return in;
  std::vector<cpp_int> out;
  out.reserve(MAX_SEQUENCE);
  for (int i = 0; i < MAX_SEQUENCE; ++i) {
    std::size_t at = static_cast<std::size_t>(i) * (in.size() - 1) /
                     (MAX_SEQUENCE - 1);
    out.push_back(in[at]);
  }
  return out;
}

struct Ratio {
  cpp_int p = 1;
  cpp_int q = 1;
};

static cpp_int gcd_cpp(cpp_int a, cpp_int b) {
  a = abs_cpp(a);
  b = abs_cpp(b);
  while (b != 0) {
    cpp_int r = a % b;
    a = b;
    b = r;
  }
  return a;
}

static void reduce_ratio(Ratio& z) {
  cpp_int g = gcd_cpp(z.p, z.q);
  z.p /= g;
  z.q /= g;
  if (z.q < 0) {
    z.p = -z.p;
    z.q = -z.q;
  }
}

static Ratio binomial_ratio(u64 B, u64 H, int r, int c) {
  const long long top = static_cast<long long>(B) + c;
  const long long bot = static_cast<long long>(H) + r;
  if (top < 0 || bot < 0 || bot > top) return {0, 1};
  Ratio z;
  auto factorial_ratio = [&](long long a, long long b) {
    if (a > b) {
      for (long long v = b + 1; v <= a; ++v) z.p *= v;
    } else {
      for (long long v = a + 1; v <= b; ++v) z.q *= v;
    }
    reduce_ratio(z);
  };
  factorial_ratio(top, static_cast<long long>(B));
  factorial_ratio(static_cast<long long>(H), bot);
  factorial_ratio(static_cast<long long>(B - H), top - bot);
  reduce_ratio(z);
  return z;
}

struct BaseSequence {
  std::string name;
  std::vector<cpp_int> values;
};

static std::pair<int, int> fundamental_pell(int D) {
  int a0 = static_cast<int>(std::sqrt(D));
  int m = 0, den = 1, a = a0;
  long long pm = 1, p = a, qm = 0, q = 1;
  while (p * p - static_cast<long long>(D) * q * q != 1) {
    m = den * a - m;
    den = (D - m * m) / den;
    a = (a0 + m) / den;
    long long pn = a * p + pm;
    long long qn = a * q + qm;
    pm = p; qm = q; p = pn; q = qn;
  }
  return {static_cast<int>(p), static_cast<int>(q)};
}

struct PublicData {
  cpp_int N;
  int n;
  u64 B2;
  u64 B;
  std::vector<BaseSequence> base;
};

static PublicData build_public_data(const cpp_int& N) {
  PublicData d;
  d.N = N;
  d.n = bit_length(N);
  d.B2 = 1ULL << (d.n / 2);
  d.B = isqrt_cpp(N).convert_to<u64>();

  std::vector<cpp_int> dyq, dyr, dyc;
  std::set<int> js;
  for (int j = 1; j <= std::min(16, d.n - 1); ++j) js.insert(j);
  for (int num : {1, 2, 3}) {
    js.insert(std::max(1, d.n * num / 4));
    js.insert(std::max(1, d.n * num / 3));
  }
  js.insert(std::max(1, d.n - 2));
  for (int j : js) {
    if (j >= d.n || j >= 63) continue;
    u64 mod = 1ULL << j;
    cpp_int q = N / mod;
    cpp_int r = N % mod;
    cpp_int c = r;
    if (r * 2 >= mod) c -= mod;
    dyq.push_back(q); dyr.push_back(r); dyc.push_back(c);
  }
  d.base.push_back({"dyadic_q", sample_evenly(dyq)});
  d.base.push_back({"dyadic_r", sample_evenly(dyr)});
  d.base.push_back({"dyadic_c", sample_evenly(dyc)});

  std::vector<cpp_int> hq, hr, hc, hd;
  cpp_int prior = 0;
  for (int u = 1; u <= 31; u += 2) {
    cpp_int v = cpp_int(u) * N;
    cpp_int q = v / d.B2;
    cpp_int r = v % d.B2;
    cpp_int c = r;
    if (r * 2 >= d.B2) c -= d.B2;
    hq.push_back(q); hr.push_back(r); hc.push_back(c);
    if (u > 1) hd.push_back(r - prior);
    prior = r;
  }
  d.base.push_back({"half_q", sample_evenly(hq)});
  d.base.push_back({"half_r", sample_evenly(hr)});
  d.base.push_back({"half_c", sample_evenly(hc)});
  d.base.push_back({"half_adj_r", sample_evenly(hd)});

  std::vector<cpp_int> sq, sr, sc;
  for (int u = 1; u <= 16; ++u) {
    for (int c = -8; c <= 8; ++c) {
      long long den_ll = static_cast<long long>(d.B) + c;
      if (den_ll <= 0) continue;
      u64 den = static_cast<u64>(den_ll);
      cpp_int v = cpp_int(u) * N;
      cpp_int q = v / den;
      cpp_int r = v % den;
      cpp_int center = r;
      if (r * 2 >= den) center -= den;
      sq.push_back(q); sr.push_back(r); sc.push_back(center);
    }
  }
  d.base.push_back({"sqrt_q", sample_evenly(sq)});
  d.base.push_back({"sqrt_r", sample_evenly(sr)});
  d.base.push_back({"sqrt_c", sample_evenly(sc)});

  std::array<std::vector<cpp_int>, 7> pell;
  for (int D : D_VALUES) {
    auto [s0i, t0i] = fundamental_pell(D);
    cpp_int s = 1, t = 0, s0 = s0i, t0 = t0i;
    for (int j = 1; j <= std::min(32, 2 * d.n); ++j) {
      cpp_int sn = s0 * s + D * t0 * t;
      cpp_int tn = s0 * t + t0 * s;
      s = sn; t = tn;
      cpp_int x = s % N, y = t % N;
      cpp_int ell = (s - x) / N, k = (t - y) / N;
      cpp_int gm = k * (x - 1) - y * ell;
      cpp_int gp = k * (x + 1) - y * ell;
      cpp_int norm = (x * x - D * y * y - 1) / N;
      pell[0].push_back(x); pell[1].push_back(y);
      pell[2].push_back(k); pell[3].push_back(ell);
      pell[4].push_back(gm); pell[5].push_back(gp);
      pell[6].push_back(norm);
    }
  }
  const char* pn[] = {"pell_x", "pell_y", "pell_k", "pell_ell",
                      "pell_gminus", "pell_gplus", "pell_norm"};
  for (int i = 0; i < 7; ++i)
    d.base.push_back({pn[i], sample_evenly(pell[i])});

  std::vector<cpp_int> hp, hqv, hdet, vdet;
  std::map<std::pair<int, int>, Ratio> ratios;
  for (int c = -8; c <= 8; ++c) {
    for (int r = -8; r <= 8; ++r) {
      Ratio z = binomial_ratio(d.B, d.B / 2, r, c);
      ratios[{c, r}] = z;
      hp.push_back(z.p); hqv.push_back(z.q);
    }
  }
  for (int c = -8; c <= 8; ++c) {
    for (int r = -8; r < 8; ++r) {
      const auto& a = ratios[{c, r}];
      const auto& b = ratios[{c, r + 1}];
      hdet.push_back(a.p * b.q - b.p * a.q);
    }
  }
  for (int c = -8; c < 8; ++c) {
    for (int r = -8; r <= 8; ++r) {
      const auto& a = ratios[{c, r}];
      const auto& b = ratios[{c + 1, r}];
      vdet.push_back(a.p * b.q - b.p * a.q);
    }
  }
  d.base.push_back({"hyper_p", sample_evenly(hp)});
  d.base.push_back({"hyper_q", sample_evenly(hqv)});
  d.base.push_back({"hyper_det_h", sample_evenly(hdet)});
  d.base.push_back({"hyper_det_v", sample_evenly(vdet)});
  require(d.base.size() == 21, "base source count");
  return d;
}

enum class Transform { ID, ADIFF, PDIFF, ASUM, AQUOT, AREM };
static const char* TRANSFORM_NAMES[] = {"id", "adj_diff", "pair_diff",
                                        "adj_sum", "adj_quot", "adj_rem"};

struct SeqProgram {
  int base;
  Transform transform;
  std::string name;
  std::array<u64, 3> fingerprint{};
};

static std::vector<cpp_int> transform_sequence(const std::vector<cpp_int>& x,
                                                Transform t) {
  if (t == Transform::ID) return sample_evenly(x);
  std::vector<cpp_int> out;
  if (t == Transform::PDIFF) {
    for (std::size_t i = 0; i < x.size() && out.size() < MAX_SEQUENCE; ++i)
      for (std::size_t j = i + 1; j < x.size() && out.size() < MAX_SEQUENCE; ++j)
        out.push_back(abs_cpp(x[j] - x[i]));
    return out;
  }
  for (std::size_t i = 1; i < x.size() && out.size() < MAX_SEQUENCE; ++i) {
    cpp_int a = x[i - 1], b = x[i];
    if (t == Transform::ADIFF) out.push_back(abs_cpp(b - a));
    if (t == Transform::ASUM) out.push_back(abs_cpp(a + b));
    if (t == Transform::AQUOT) {
      a = abs_cpp(a); b = abs_cpp(b);
      out.push_back(b == 0 ? cpp_int(0) : cpp_int(a / b));
    }
    if (t == Transform::AREM) {
      a = abs_cpp(a); b = abs_cpp(b);
      out.push_back(b == 0 ? cpp_int(0) : cpp_int(a % b));
    }
  }
  return out;
}

struct WordProgram {
  int a;
  int b;
  std::string name;
  std::array<u64, 3> fingerprint{};
};

enum class FactMode { SMOOTH, ORACLE };
struct FactProgram {
  FactMode mode;
  int parameter;
  std::string name;
  bool oracle;
  std::array<u64, 3> fingerprint{};
};

enum class Kind { SEQUENCE, WORD, FACTORED };
struct ProgramRef {
  Kind kind;
  int index;
  std::string name;
  bool operational;
  bool oracle;
  std::array<u64, 3> fingerprint{};
};

struct Grammar {
  std::vector<SeqProgram> seq;
  std::vector<WordProgram> word;
  std::vector<FactProgram> fact;
  std::vector<ProgramRef> all;
};

static std::array<u64, 3> fingerprint_seq(
    const SeqProgram& p, const std::vector<PublicData>& synthetic) {
  const u64 mods[] = {2305843009213693951ULL, 2305843009213693921ULL,
                      2305843009213693907ULL};
  std::array<u64, 3> h = {mix64(1), mix64(2), mix64(3)};
  for (int t = 0; t < 24; ++t) {
    const PublicData& d = synthetic[t];
    auto v = transform_sequence(d.base[p.base].values, p.transform);
    for (int k = 0; k < 3; ++k) {
      h[k] = mix64(h[k] ^ static_cast<u64>(v.size()) ^ (u64(t) << 32));
      for (const auto& z : v) h[k] = mix64(h[k] ^ mod_cpp(z, mods[k]));
    }
  }
  return h;
}

static std::array<u64, 3> fingerprint_word(
    const WordProgram& p, const std::vector<SeqProgram>& seq,
    const std::vector<PublicData>& synthetic,
    const std::vector<std::array<std::array<u64, 3>, 24>>& residues) {
  const u64 mods[] = {2305843009213693951ULL, 2305843009213693921ULL,
                      2305843009213693907ULL};
  std::array<u64, 3> h = {mix64(11), mix64(12), mix64(13)};
  for (int t = 0; t < 24; ++t) {
    const PublicData& d = synthetic[t];
    for (int k = 0; k < 3; ++k) {
      u64 prod = pow_mod(mod_cpp(d.N - 1, mods[k]), d.n, mods[k]);
      if (p.a >= 0) prod = mul_mod(prod, residues[p.a][t][k], mods[k]);
      if (p.b >= 0) prod = mul_mod(prod, residues[p.b][t][k], mods[k]);
      h[k] = mix64(h[k] ^ prod ^ (u64(t) << 40));
    }
  }
  return h;
}

static std::string fp_string(const std::array<u64, 3>& fp) {
  std::ostringstream s;
  s << std::hex << std::setfill('0');
  for (u64 x : fp) s << std::setw(16) << x;
  return s.str();
}

static Grammar build_grammar() {
  std::vector<PublicData> synthetic;
  synthetic.reserve(24);
  for (int t = 0; t < 24; ++t)
    synthetic.push_back(build_public_data(cpp_int(1001 + 2 * t) * (2001 + 4 * t)));
  const PublicData& names = synthetic.front();
  std::vector<SeqProgram> raw;
  for (int b = 0; b < static_cast<int>(names.base.size()); ++b) {
    for (int tr = 0; tr < 6; ++tr) {
      SeqProgram p{b, static_cast<Transform>(tr),
                   "seq:" + names.base[b].name + ":" + TRANSFORM_NAMES[tr], {}};
      p.fingerprint = fingerprint_seq(p, synthetic);
      raw.push_back(std::move(p));
    }
  }
  std::sort(raw.begin(), raw.end(), [](const auto& a, const auto& b) {
    return a.name < b.name;
  });
  Grammar g;
  std::set<std::array<u64, 3>> seen_seq;
  for (auto& p : raw) {
    if (seen_seq.insert(p.fingerprint).second) g.seq.push_back(std::move(p));
  }
  require(!g.seq.empty() && g.seq.size() <= MAX_PROGRAMS_PER_TYPE,
          "sequence grammar cap");

  const u64 mods[] = {2305843009213693951ULL, 2305843009213693921ULL,
                      2305843009213693907ULL};
  std::vector<std::array<std::array<u64, 3>, 24>> residues(g.seq.size());
  for (std::size_t i = 0; i < g.seq.size(); ++i) for (int t = 0; t < 24; ++t) {
    auto values = transform_sequence(
        synthetic[t].base[g.seq[i].base].values, g.seq[i].transform);
    for (int k = 0; k < 3; ++k) {
      u64 prod = 1;
      for (const auto& z : values) if (z != 0)
        prod = mul_mod(prod,
            pow_mod(mod_cpp(abs_cpp(z), mods[k]), synthetic[t].n, mods[k]),
            mods[k]);
      residues[i][t][k] = prod;
    }
  }

  std::vector<WordProgram> wr;
  wr.push_back({-1, -1, "word:baseline", {}});
  for (int i = 0; i < static_cast<int>(g.seq.size()); ++i)
    wr.push_back({i, -1, "word:" + g.seq[i].name, {}});
  for (int i = 0; i < static_cast<int>(g.seq.size()); ++i) {
    for (int j = i + 1; j < static_cast<int>(g.seq.size()); ++j) {
      bool same_base = g.seq[i].base == g.seq[j].base;
      bool both_id = g.seq[i].transform == Transform::ID &&
                     g.seq[j].transform == Transform::ID;
      bool sparse = (mix64(static_cast<u64>(i) * 1315423911ULL + j) % 5) == 0;
      if (same_base || both_id || sparse)
        wr.push_back({i, j, "word:" + g.seq[i].name + "*" + g.seq[j].name, {}});
      if (static_cast<int>(wr.size()) >= MAX_PROGRAMS_PER_TYPE * 2) break;
    }
    if (static_cast<int>(wr.size()) >= MAX_PROGRAMS_PER_TYPE * 2) break;
  }
  std::sort(wr.begin(), wr.end(), [](const auto& a, const auto& b) {
    return a.name < b.name;
  });
  std::set<std::array<u64, 3>> seen_word;
  for (auto& p : wr) {
    p.fingerprint = fingerprint_word(p, g.seq, synthetic, residues);
    if (seen_word.insert(p.fingerprint).second) g.word.push_back(std::move(p));
    if (static_cast<int>(g.word.size()) == MAX_PROGRAMS_PER_TYPE) break;
  }
  require(g.word.size() >= 1000 && g.word.size() <= MAX_PROGRAMS_PER_TYPE,
          "word grammar size");

  g.fact.push_back({FactMode::SMOOTH, 1, "factored:lcm_1_n", false, {1, 1, 1}});
  g.fact.push_back({FactMode::SMOOTH, 2, "factored:lcm_1_n2", false, {2, 2, 2}});
  g.fact.push_back({FactMode::SMOOTH, 3, "factored:lcm_1_n3", false, {3, 3, 3}});
  for (int b : {1, 3, 4, 8, 11, 17}) {
    g.fact.push_back({FactMode::ORACLE, b,
                      "factored:recursive_first:" + names.base[b].name,
                      true, {u64(100 + b), u64(200 + b), u64(300 + b)}});
  }

  for (int i = 0; i < static_cast<int>(g.seq.size()); ++i)
    g.all.push_back({Kind::SEQUENCE, i, g.seq[i].name, true, false,
                     g.seq[i].fingerprint});
  for (int i = 0; i < static_cast<int>(g.word.size()); ++i)
    g.all.push_back({Kind::WORD, i, g.word[i].name, true, false,
                     g.word[i].fingerprint});
  for (int i = 0; i < static_cast<int>(g.fact.size()); ++i)
    g.all.push_back({Kind::FACTORED, i, g.fact[i].name, !g.fact[i].oracle,
                     g.fact[i].oracle, g.fact[i].fingerprint});
  return g;
}

struct CorpusRow {
  int bits;
  int cohort;
  int index;
  u64 p;
  u64 q;
  cpp_int N;
};

static std::vector<CorpusRow> make_corpus(bool discovery, bool tiny = false) {
  std::vector<CorpusRow> rows;
  std::set<std::string> seen;
  const int* bits = discovery ? DISCOVERY_BITS : HELDOUT_BITS;
  int nbits = discovery ? 3 : 4;
  for (int bi = 0; bi < nbits; ++bi) {
    int b = bits[bi];
    int counts[3] = {discovery ? 2048 : 4096,
                     discovery ? (b == 16 ? 256 : 512) : 1024,
                     discovery ? 512 : 1024};
    if (tiny) counts[0] = counts[1] = counts[2] = 2;
    for (int cohort = 0; cohort < 3; ++cohort) {
      Rng rng(MASTER_SEED ^ (u64(discovery) << 63) ^ (u64(b) << 24) ^
              (u64(cohort) << 48));
      int accepted = 0;
      int attempts = 0;
      while (accepted < counts[cohort]) {
        if (++attempts > 50000000) fail("corpus generation attempt cap");
        u64 p, q;
        if (cohort == 1) {
          p = random_safe_prime(b, rng);
          q = random_safe_prime(b, rng);
          if (p == q) continue;
          if (p > q) std::swap(p, q);
        } else if (cohort == 2) {
          p = random_prime(b, rng);
          q = next_prime(p);
          if (bit_length(q) != b) continue;
        } else {
          p = random_prime(b, rng);
          q = random_prime(b, rng);
          if (p == q) continue;
          if (p > q) std::swap(p, q);
        }
        if (!(p < q && q < 2 * p)) continue;
        cpp_int N = cpp_int(p) * q;
        std::string key = N.convert_to<std::string>();
        if (!seen.insert(key).second) continue;
        rows.push_back({b, cohort, accepted++, p, q, N});
      }
    }
  }
  return rows;
}

struct LocalLabels {
  u64 p, q, sp, sq, d;
  int vp2, vq2;
  std::map<u64, int> fp1, fq1, fsp, fsq;
};

static std::map<u64, int> divide_factor_maps(const std::map<u64, int>& a,
                                              const std::map<u64, int>& b) {
  auto out = a;
  for (auto [p, e] : b) {
    auto it = out.find(p);
    require(it != out.end() && it->second >= e, "factor map division");
    it->second -= e;
    if (it->second == 0) out.erase(it);
  }
  return out;
}

static LocalLabels make_labels(const CorpusRow& row) {
  LocalLabels z{};
  z.p = row.p; z.q = row.q;
  z.fp1 = factor_u64(row.p - 1, MASTER_SEED ^ row.p);
  z.fq1 = factor_u64(row.q - 1, MASTER_SEED ^ row.q);
  z.d = std::gcd(row.p - 1, row.q - 1);
  z.sp = (row.p - 1) / z.d;
  z.sq = (row.q - 1) / z.d;
  auto fd = factor_u64(z.d, MASTER_SEED ^ z.d);
  z.fsp = divide_factor_maps(z.fp1, fd);
  z.fsq = divide_factor_maps(z.fq1, fd);
  z.vp2 = z.fp1.count(2) ? z.fp1.at(2) : 0;
  z.vq2 = z.fq1.count(2) ? z.fq1.at(2) : 0;
  return z;
}

static long double miller_probability(u64 wp, u64 wq, int v2_exponent,
                                       const LocalLabels& z, int n) {
  u64 gp = std::gcd(z.sp, wp);
  u64 gq = std::gcd(z.sq, wq);
  u64 rp = z.sp / gp, rq = z.sq / gq;
  long double ap = 1.0L / static_cast<long double>(rp);
  long double aq = 1.0L / static_cast<long double>(rq);
  int vE = v2_exponent;
  int hp = std::min(z.vp2, vE), hq = std::min(z.vq2, vE);
  int a = std::min(hp, hq), b = std::max(hp, hq);
  long double mu = 1.0L -
      (std::pow(4.0L, a) + 2.0L) /
      (3.0L * std::pow(2.0L, a + b));
  require(mu >= 0.49L && mu <= 1.0L, "Miller probability range");
  (void)n;
  return ap + aq - (2.0L - mu) * ap * aq;
}

struct SeqEval {
  std::vector<cpp_int> values;
  u64 prod_p = 1, prod_q = 1;
  int v2sum = 0;
  long double collision_fraction = 0;
  long double pair_miller = 0;
  bool direct = false;
  u64 direct_factor = 0;
};

static long double captured_fraction(const std::vector<cpp_int>& v,
                                      const std::map<u64, int>& residual) {
  if (v.empty() || residual.empty()) return residual.empty() ? 1.0L : 0.0L;
  long double got = 0, total = 0;
  const long double denom = static_cast<long double>(v.size()) * v.size();
  for (auto [ell, e] : residual) {
    std::unordered_map<u64, u64> buckets;
    std::map<cpp_int, u64> exact;
    for (const auto& x : v) {
      ++buckets[mod_cpp(x, ell)];
      ++exact[x];
    }
    u64 num = 0;
    for (auto [r, c] : buckets) { (void)r; num += c * (c - 1); }
    for (auto& kv : exact) num -= kv.second * (kv.second - 1);
    long double kappa = static_cast<long double>(num) / denom;
    long double mass = e * std::log2(static_cast<long double>(ell));
    got += kappa * mass;
    total += mass;
  }
  return total == 0 ? 1.0L : got / total;
}

static SeqEval eval_sequence(const std::vector<cpp_int>& values,
                             const CorpusRow& row, const LocalLabels& z) {
  SeqEval e;
  e.values = sample_evenly(values);
  if (e.values.empty()) return e;
  for (const auto& raw : e.values) {
    cpp_int x = abs_cpp(raw);
    if (x == 0) continue;
    u64 mp = mod_cpp(x, z.p), mq = mod_cpp(x, z.q);
    if ((mp == 0) != (mq == 0)) {
      e.direct = true;
      e.direct_factor = mp == 0 ? z.p : z.q;
    }
    e.prod_p = mul_mod(e.prod_p, mod_cpp(x, z.sp), z.sp);
    e.prod_q = mul_mod(e.prod_q, mod_cpp(x, z.sq), z.sq);
    e.v2sum = std::min(127, e.v2sum + v2_cpp(x));
  }
  long double cp = captured_fraction(e.values, z.fsp);
  long double cq = captured_fraction(e.values, z.fsq);
  e.collision_fraction = std::min(cp, cq);

  const u64 basep = pow_mod(mod_cpp(row.N - 1, z.sp), bit_length(row.N), z.sp);
  const u64 baseq = pow_mod(mod_cpp(row.N - 1, z.sq), bit_length(row.N), z.sq);
  int basev2 = std::min(127, (bit_length(row.N) + 1) * v2_cpp(row.N - 1));
  long double sum = 0;
  const long double den = static_cast<long double>(e.values.size()) * e.values.size();
  for (std::size_t i = 0; i < e.values.size(); ++i) {
    for (std::size_t j = 0; j < e.values.size(); ++j) {
      cpp_int delta = e.values[i] == e.values[j] ? cpp_int(1) :
                      abs_cpp(e.values[i] - e.values[j]);
      u64 dp = pow_mod(mod_cpp(delta, z.sp), bit_length(row.N), z.sp);
      u64 dq = pow_mod(mod_cpp(delta, z.sq), bit_length(row.N), z.sq);
      int vd = std::min(127, bit_length(row.N) * v2_cpp(delta));
      sum += miller_probability(mul_mod(basep, dp, z.sp),
                                mul_mod(baseq, dq, z.sq),
                                std::min(127, basev2 + vd), z,
                                bit_length(row.N));
    }
  }
  e.pair_miller = sum / den;
  return e;
}

static std::map<u64, int> smooth_factor_map(int cap) {
  std::vector<bool> sieve(cap + 1, true);
  if (cap >= 0) sieve[0] = false;
  if (cap >= 1) sieve[1] = false;
  for (int p = 2; p * p <= cap; ++p) if (sieve[p])
    for (int k = p * p; k <= cap; k += p) sieve[k] = false;
  std::map<u64, int> out;
  for (int p = 2; p <= cap; ++p) if (sieve[p]) {
    u64 x = p;
    int e = 1;
    while (x <= static_cast<u64>(cap) / p) { x *= p; ++e; }
    out[p] = e;
  }
  return out;
}

static std::map<u64, int> cached_smooth_factor_map(int cap) {
  static std::mutex mutex;
  static std::map<int, std::map<u64, int>> cache;
  std::lock_guard<std::mutex> lock(mutex);
  auto it = cache.find(cap);
  if (it != cache.end()) return it->second;
  auto result = smooth_factor_map(cap);
  cache.emplace(cap, result);
  return result;
}

static long double prob_t(int ell, int f, int t) {
  if (t == 0) return std::pow(static_cast<long double>(ell), -f);
  return (ell - 1) * std::pow(static_cast<long double>(ell), t - 1 - f);
}

struct FactScore {
  long double progress = 0;
  long double expected_log_gain = 0;
  long double dyadic = 0;
};

static int exponent_in(const std::map<u64, int>& f, u64 p) {
  auto it = f.find(p);
  return it == f.end() ? 0 : it->second;
}

static FactScore score_factored(const std::map<u64, int>& A,
                                const LocalLabels& z, int n) {
  long double dp = 1, dq = 1;
  for (auto [ell, e] : A) {
    int ep = std::min(e, exponent_in(z.fp1, ell));
    int eq = std::min(e, exponent_in(z.fq1, ell));
    dp *= std::pow(static_cast<long double>(ell), ep);
    dq *= std::pow(static_cast<long double>(ell), eq);
  }
  long double ap = dp / static_cast<long double>(z.p - 1);
  long double aq = dq / static_cast<long double>(z.q - 1);
  long double direct = ap + aq - 2 * ap * aq;
  long double equal_product = 1, stale_product = 1;
  std::vector<std::tuple<long double, long double, long double>> primary;
  for (auto [ell64, e] : A) {
    int ell = static_cast<int>(ell64);
    int fp = std::min(e, exponent_in(z.fp1, ell64));
    int fq = std::min(e, exponent_in(z.fq1, ell64));
    long double equal = 0, stale = 0, gain = 0;
    int maxf = std::max(fp, fq);
    for (int t = 0; t <= maxf; ++t) {
      long double pp = t <= fp ? prob_t(ell, fp, t) : 0;
      long double pq = t <= fq ? prob_t(ell, fq, t) : 0;
      equal += pp * pq;
      if (t == 0) stale += pp * pq;
      if (t > 0) gain += pp * pq * t * std::log2(static_cast<long double>(ell));
    }
    equal_product *= equal;
    stale_product *= stale;
    primary.push_back({equal, stale, gain});
  }
  FactScore out;
  out.progress = direct + ap * aq * (1 - stale_product);
  for (std::size_t i = 0; i < primary.size(); ++i) {
    long double other = 1;
    for (std::size_t j = 0; j < primary.size(); ++j)
      if (i != j) other *= std::get<0>(primary[j]);
    out.expected_log_gain += ap * aq * std::get<2>(primary[i]) * other;
  }
  long double dyadic_sum = 0;
  for (int tbits : {n / 8, n / 6, n / 5}) {
    long double staleL = 1;
    for (auto [ell64, e] : A) {
      int ell = static_cast<int>(ell64);
      int fp = std::min(e, exponent_in(z.fp1, ell64));
      int fq = std::min(e, exponent_in(z.fq1, ell64));
      int oldv = ell == 2 ? tbits : 0;
      long double s = 0;
      for (int t = 0; t <= std::max(fp, fq); ++t) {
        long double pp = t <= fp ? prob_t(ell, fp, t) : 0;
        long double pq = t <= fq ? prob_t(ell, fq, t) : 0;
        if (t <= oldv) s += pp * pq;
      }
      staleL *= s;
    }
    dyadic_sum += direct + ap * aq * (1 - staleL);
  }
  out.dyadic = dyadic_sum / 3;
  require(out.progress >= -1e-12L && out.progress <= 1 + 1e-9L,
          "factored score range");
  return out;
}

struct Metrics {
  long double score = 0, miller = 0, collision = 0, growth = 0, dyadic = 0;
  bool direct = false;
  u64 factor = 0;
};

static std::vector<Metrics> evaluate_row(const CorpusRow& row, const Grammar& g) {
  PublicData d = build_public_data(row.N);
  LocalLabels z = make_labels(row);
  std::vector<SeqEval> seqeval(g.seq.size());
  for (std::size_t i = 0; i < g.seq.size(); ++i) {
    const auto& p = g.seq[i];
    seqeval[i] = eval_sequence(
        transform_sequence(d.base[p.base].values, p.transform), row, z);
  }
  std::vector<Metrics> out;
  out.reserve(g.all.size());
  for (const auto& ref : g.all) {
    Metrics m;
    if (ref.kind == Kind::SEQUENCE) {
      const auto& e = seqeval[ref.index];
      m.direct = e.direct; m.factor = e.direct_factor;
      m.miller = e.direct ? 1 : e.pair_miller;
      m.collision = e.collision_fraction;
      m.score = m.miller;
    } else if (ref.kind == Kind::WORD) {
      const auto& p = g.word[ref.index];
      u64 wp = pow_mod(mod_cpp(row.N - 1, z.sp), d.n, z.sp);
      u64 wq = pow_mod(mod_cpp(row.N - 1, z.sq), d.n, z.sq);
      int v2w = std::min(127, (d.n + 1) * v2_cpp(row.N - 1));
      for (int idx : {p.a, p.b}) if (idx >= 0) {
        const auto& e = seqeval[idx];
        if (e.direct) { m.direct = true; m.factor = e.direct_factor; }
        wp = mul_mod(wp, pow_mod(e.prod_p, d.n, z.sp), z.sp);
        wq = mul_mod(wq, pow_mod(e.prod_q, d.n, z.sq), z.sq);
        v2w = std::min(127, v2w + d.n * e.v2sum);
      }
      m.miller = m.direct ? 1 : miller_probability(wp, wq, v2w, z, d.n);
      m.score = m.miller;
    } else {
      const auto& p = g.fact[ref.index];
      std::map<u64, int> A;
      if (p.mode == FactMode::SMOOTH) {
        int cap = d.n;
        if (p.parameter == 2) cap = d.n * d.n;
        if (p.parameter == 3) cap = d.n * d.n * d.n;
        A = cached_smooth_factor_map(cap);
      } else {
        const auto& v = d.base[p.parameter].values;
        if (!v.empty()) {
          cpp_int x = abs_cpp(v.front());
          cpp_int bound = cpp_int(1) << ((d.n + 1) / 2 + 2);
          if (x > 1 && x < bound && bit_length(x) <= 63)
            A = factor_u64(x.convert_to<u64>(), MASTER_SEED ^ row.p ^ row.q);
        }
      }
      FactScore f = score_factored(A, z, d.n);
      m.growth = f.progress;
      m.dyadic = f.dyadic;
      m.score = f.progress;
    }
    out.push_back(m);
  }
  require(out.size() == g.all.size(), "metric count");
  return out;
}

struct Cell {
  long double score = 0, miller = 0, collision = 0, growth = 0, dyadic = 0;
  u64 count = 0, direct = 0;
  std::vector<double> collision_values;
};

struct Aggregate {
  std::array<Cell, COHORTS> c;
};

static std::vector<Aggregate> evaluate_corpus(const std::vector<CorpusRow>& rows,
                                               const Grammar& g, int workers,
                                               bool keep_collision) {
  workers = std::max(1, std::min(workers, 8));
  std::vector<std::vector<Aggregate>> local(
      workers, std::vector<Aggregate>(g.all.size()));
  std::atomic<std::size_t> next{0};
  std::vector<std::thread> threads;
  for (int w = 0; w < workers; ++w) {
    threads.emplace_back([&, w]() {
      for (;;) {
        std::size_t at = next.fetch_add(1);
        if (at >= rows.size()) break;
        auto metrics = evaluate_row(rows[at], g);
        int co = rows[at].cohort;
        for (std::size_t i = 0; i < metrics.size(); ++i) {
          auto& cell = local[w][i].c[co];
          const auto& m = metrics[i];
          cell.score += m.score; cell.miller += m.miller;
          cell.collision += m.collision; cell.growth += m.growth;
          cell.dyadic += m.dyadic; ++cell.count;
          if (m.direct) ++cell.direct;
          if (keep_collision && g.all[i].kind == Kind::SEQUENCE)
            cell.collision_values.push_back(static_cast<double>(m.collision));
        }
      }
    });
  }
  for (auto& t : threads) t.join();
  std::vector<Aggregate> out(g.all.size());
  for (int w = 0; w < workers; ++w) {
    for (std::size_t i = 0; i < out.size(); ++i) for (int c = 0; c < 3; ++c) {
      auto& a = out[i].c[c]; auto& b = local[w][i].c[c];
      a.score += b.score; a.miller += b.miller; a.collision += b.collision;
      a.growth += b.growth; a.dyadic += b.dyadic;
      a.count += b.count; a.direct += b.direct;
      a.collision_values.insert(a.collision_values.end(),
                                b.collision_values.begin(), b.collision_values.end());
    }
  }
  return out;
}

static long double min_mean(const Aggregate& a, int field) {
  long double out = 1e100L;
  for (const auto& c : a.c) {
    if (c.count == 0) return 0;
    long double s = field == 0 ? c.score : field == 1 ? c.miller :
                    field == 2 ? c.collision : field == 3 ? c.growth : c.dyadic;
    out = std::min(out, s / c.count);
  }
  return out;
}

static long double min_collision_median(const Aggregate& a) {
  long double out = 1;
  for (const auto& c : a.c) {
    if (c.collision_values.empty()) return 0;
    auto v = c.collision_values;
    std::sort(v.begin(), v.end());
    out = std::min(out, static_cast<long double>(v[v.size() / 2]));
  }
  return out;
}

static std::vector<int> select_programs(const Grammar& g,
                                        const std::vector<Aggregate>& a) {
  std::vector<int> selected;
  std::set<int> used;
  auto add_top = [&](int field, bool median_collision, int limit) {
    std::vector<int> ids;
    for (int i = 0; i < static_cast<int>(g.all.size()); ++i)
      if (g.all[i].operational) ids.push_back(i);
    std::sort(ids.begin(), ids.end(), [&](int x, int y) {
      long double sx = median_collision ? min_collision_median(a[x]) : min_mean(a[x], field);
      long double sy = median_collision ? min_collision_median(a[y]) : min_mean(a[y], field);
      if (sx != sy) return sx > sy;
      return g.all[x].name < g.all[y].name;
    });
    int added = 0;
    for (int id : ids) if (used.insert(id).second) {
      selected.push_back(id);
      if (++added == limit || selected.size() == 32) break;
    }
  };
  add_top(0, false, 8);
  add_top(0, true, 8);
  add_top(1, false, 8);
  add_top(4, false, 8);
  if (selected.size() < 32) add_top(0, false, 32);
  require(selected.size() == 32, "selection size");
  return selected;
}

static void write_grammar(const std::string& path, const Grammar& g) {
  std::ofstream f(path);
  require(bool(f), "open grammar output");
  f << "id\tkind\toperational\toracle\tfingerprint\tsyntax\n";
  for (std::size_t i = 0; i < g.all.size(); ++i) {
    const auto& p = g.all[i];
    const char* kind = p.kind == Kind::SEQUENCE ? "sequence" :
                       p.kind == Kind::WORD ? "word" : "factored";
    f << i << '\t' << kind << '\t' << p.operational << '\t' << p.oracle
      << '\t' << fp_string(p.fingerprint) << '\t' << p.name << '\n';
  }
}

static void write_aggregates(const std::string& path, const Grammar& g,
                             const std::vector<Aggregate>& a,
                             const std::vector<int>* only = nullptr) {
  std::ofstream f(path);
  require(bool(f), "open aggregate output");
  f << std::setprecision(18);
  f << "id\tsyntax\tcohort\tcount\tmean_score\tmean_miller\tmean_collision"
       "\tmean_growth\tmean_dyadic\tdirect\n";
  std::vector<int> ids;
  if (only) ids = *only;
  else { ids.resize(g.all.size()); std::iota(ids.begin(), ids.end(), 0); }
  for (int id : ids) for (int c = 0; c < 3; ++c) {
    const auto& z = a[id].c[c];
    long double den = z.count ? z.count : 1;
    f << id << '\t' << g.all[id].name << '\t' << COHORT_NAMES[c] << '\t'
      << z.count << '\t' << z.score / den << '\t' << z.miller / den << '\t'
      << z.collision / den << '\t' << z.growth / den << '\t'
      << z.dyadic / den << '\t' << z.direct << '\n';
  }
}

static void write_selection(const std::string& path, const Grammar& g,
                            const std::vector<Aggregate>& a,
                            const std::vector<int>& ids) {
  std::ofstream f(path);
  require(bool(f), "open selection output");
  f << std::setprecision(18);
  f << "id\tkind\toperational\toracle\tfingerprint\tmin_score\tmin_miller"
       "\tmin_collision_mean\tmin_collision_median\tmin_dyadic\tsyntax\n";
  for (int id : ids) {
    const auto& p = g.all[id];
    const char* kind = p.kind == Kind::SEQUENCE ? "sequence" :
                       p.kind == Kind::WORD ? "word" : "factored";
    f << id << '\t' << kind << '\t' << p.operational << '\t' << p.oracle
      << '\t' << fp_string(p.fingerprint) << '\t' << min_mean(a[id], 0)
      << '\t' << min_mean(a[id], 1) << '\t' << min_mean(a[id], 2)
      << '\t' << min_collision_median(a[id]) << '\t' << min_mean(a[id], 4)
      << '\t' << p.name << '\n';
  }
}

static std::vector<int> read_selection(const std::string& path,
                                       const Grammar& g) {
  std::ifstream f(path);
  require(bool(f), "open selection input");
  std::string line;
  std::getline(f, line);
  std::vector<int> ids;
  while (std::getline(f, line)) {
    std::istringstream s(line);
    std::string field;
    std::getline(s, field, '\t');
    int id = std::stoi(field);
    require(id >= 0 && id < static_cast<int>(g.all.size()), "selection id");
    ids.push_back(id);
  }
  require(ids.size() == 32, "read 32 selection rows");
  return ids;
}

static Grammar restricted_grammar(const Grammar& full,
                                  const std::vector<int>& selected,
                                  std::vector<int>& local_to_global) {
  // Keep all sequence descriptors because selected words refer to them, but
  // evaluate only selected public programs in the final projection.
  Grammar g = full;
  g.all.clear();
  for (int id : selected) {
    g.all.push_back(full.all[id]);
    local_to_global.push_back(id);
  }
  return g;
}

static void run_discovery(const std::string& outdir, int workers, bool tiny) {
  const auto start = std::chrono::steady_clock::now();
  Grammar g = build_grammar();
  write_grammar(outdir + "/F260-D01.grammar.tsv", g);
  auto rows = make_corpus(true, tiny);
  auto a = evaluate_corpus(rows, g, workers, true);
  auto ids = select_programs(g, a);
  write_aggregates(outdir + "/F260-D01.discovery.tsv", g, a);
  write_selection(outdir + "/F260-D01.selection.tsv", g, a, ids);
  std::cout << "discovery_rows=" << rows.size() << " programs=" << g.all.size()
            << " selected=" << ids.size() << '\n';
  print_process_resources("discovery", start);
}

static void run_heldout(const std::string& outdir, const std::string& selection,
                        int workers, bool tiny) {
  const auto start = std::chrono::steady_clock::now();
  Grammar full = build_grammar();
  auto ids = read_selection(selection, full);
  std::vector<int> local_to_global;
  Grammar g = restricted_grammar(full, ids, local_to_global);
  auto rows = make_corpus(false, tiny);
  auto a = evaluate_corpus(rows, g, workers, true);
  write_aggregates(outdir + "/F260-D01.heldout.tsv", g, a);
  std::ofstream map(outdir + "/F260-D01.heldout_ids.tsv");
  map << "local_id\tglobal_id\tsyntax\n";
  for (std::size_t i = 0; i < local_to_global.size(); ++i)
    map << i << '\t' << local_to_global[i] << '\t' << g.all[i].name << '\n';
  std::cout << "heldout_rows=" << rows.size() << " selected=" << ids.size() << '\n';
  print_process_resources("heldout", start);
}

static void self_test() {
  const auto start = std::chrono::steady_clock::now();
  require(is_prime(2) && is_prime(18446744073709551557ULL), "primality");
  require(!is_prime(341) && mul_mod(~u64(0), ~u64(0), 1000003) ==
          static_cast<u64>((static_cast<u128>(~u64(0)) * (~u64(0))) % 1000003),
          "mod arithmetic");
  auto f = factor_u64(2ULL * 3 * 3 * 1000003, MASTER_SEED);
  require(f[2] == 1 && f[3] == 2 && f[1000003] == 1, "factorization");
  require(isqrt_cpp(cpp_int(143) * 143 + 142) == 143, "integer sqrt");
  Ratio r = binomial_ratio(20, 10, 1, 1);
  require(r.p * 184756 == r.q * 352716, "binomial ratio");
  PublicData d = build_public_data(cpp_int(101) * 103);
  require(d.base.size() == 21, "public source");
  Grammar g = build_grammar();
  require(g.seq.size() >= 80 && g.word.size() >= 1000 && g.fact.size() == 9,
          "grammar sizes");
  CorpusRow row{8, 0, 0, 131, 137, cpp_int(131) * 137};
  auto metrics = evaluate_row(row, g);
  require(metrics.size() == g.all.size(), "row evaluation");
  for (const auto& x : metrics)
    require(x.score >= -1e-12L && x.score <= 1 + 1e-8L, "score range");
  std::cout << "SELF_TEST_OK seq=" << g.seq.size() << " word=" << g.word.size()
            << " fact=" << g.fact.size() << " all=" << g.all.size() << '\n';
  print_process_resources("selftest", start);
}

static void benchmark(int workers) {
  require(workers == 1, "public benchmark uses one worker");
  const auto start = std::chrono::steady_clock::now();
  Grammar g = build_grammar();
  // The grammar builder evaluates all public candidate fingerprints on 24
  // synthetic odd composites.  Repeat the widest public source construction
  // at a 120-bit modulus, without hidden factors or a semiprime score.
  cpp_int N = (cpp_int(1) << 119) + 0x260D01;
  PublicData d = build_public_data(N);
  u64 checksum = 0;
  for (const auto& p : g.seq) {
    auto values = transform_sequence(d.base[p.base].values, p.transform);
    for (const auto& x : values) checksum = mix64(checksum ^ mod_cpp(x, 1000000007));
  }
  std::cout << "BENCHMARK_OK public_synthetic=24 public_width_bits=120"
            << " seq=" << g.seq.size() << " word=" << g.word.size()
            << " fact=" << g.fact.size() << " checksum=" << checksum << '\n';
  print_process_resources("benchmark", start);
}

int main(int argc, char** argv) {
  try {
    if (argc == 2 && std::string(argv[1]) == "--self-test") {
      self_test();
      return 0;
    }
    if (argc == 3 && std::string(argv[1]) == "--benchmark") {
      benchmark(std::stoi(argv[2]));
      return 0;
    }
    if (argc >= 5 && std::string(argv[1]) == "--discovery") {
      run_discovery(argv[2], std::stoi(argv[3]), std::string(argv[4]) == "tiny");
      return 0;
    }
    if (argc >= 6 && std::string(argv[1]) == "--heldout") {
      run_heldout(argv[2], argv[3], std::stoi(argv[4]),
                  std::string(argv[5]) == "tiny");
      return 0;
    }
    std::cerr << "usage: search --self-test | --benchmark workers | "
                 "--discovery outdir workers full|tiny | "
                 "--heldout outdir selection workers full|tiny\n";
    return 2;
  } catch (const std::exception& e) {
    std::cerr << "F260 ERROR: " << e.what() << '\n';
    return 1;
  }
}
