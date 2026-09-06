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
#include <string>
#include <thread>
#include <tuple>
#include <utility>
#include <vector>

#include <boost/multiprecision/cpp_int.hpp>

using boost::multiprecision::cpp_int;
using u64 = std::uint64_t;
using u128 = __uint128_t;

static constexpr int FAMILY_COUNT = 30;
static constexpr int WORD_DEPTH = 7;
static constexpr int PROFILE_COUNT = 2;
static constexpr int PAIR_CAP = 1024;
static constexpr int TRIPLE_CAP = 256;
static constexpr int COMMUTATOR_CAP = 1024;
static constexpr int ORDER_MAIN_PER_PROFILE = 8;
static constexpr int FACTOR_BITS[] = {16, 24, 32, 40, 48, 56, 60};
static constexpr int RANDOM_PER_BITS = 384;
static constexpr int CONSECUTIVE_PER_BITS = 192;
static constexpr int SAFE_PER_BITS = 192;
static constexpr int SAFE_16_BITS = 96;
static constexpr u64 SOURCE_SEED = 0xf264d02a71ce5eedULL;
static constexpr u64 COHORT_SEED = 0x264d02c0f0a57eedULL;
static constexpr u64 SYNTH_SEED = 0x2645a17e9d02beefULL;
static constexpr u64 FP1 = 1000000007ULL;
static constexpr u64 FP2 = 1000000009ULL;
static constexpr u64 PRIME_SEARCH_CAP = 1ULL << 20;
static constexpr u64 SAFE_SEARCH_CAP = 1ULL << 20;
static constexpr u64 COHORT_ATTEMPT_CAP = 1ULL << 22;
static constexpr u64 SCOPE_STEP_CAP = 4096;
static constexpr int DECOY_COUNT = 10;
static constexpr int ROOT_PROPOSAL_COUNT = 14;

static const char* DECOY_NAMES[DECOY_COUNT] = {
    "matrix_associativity", "associator_quotient", "trace_cyclicity",
    "inverse_trace", "fricke_mod_N2", "cayley_hamilton_mod_N2",
    "determinant_multiplicativity", "determinant_unit",
    "conjugacy_trace", "conjugacy_determinant"};
static const char* BASIS_FEATURE_NAMES[5] = {"low", "lift", "K", "k", "H"};

static const char* FAMILY_NAMES[FAMILY_COUNT] = {
    "low_entry_control", "lift_entry", "lift_trace", "lift_antitrace",
    "determinant_N2_quotient", "cayley_hamilton_N2_quotient",
    "step_carry_K", "step_carry_digit", "step_second_carry_H",
    "step_cross_minors", "commutator_low", "commutator_lift",
    "commutator_trace_lift", "fricke_N2_quotient",
    "fricke_pair_difference", "trace_collision",
    "commutator_trace_collision", "lift_collision", "low_entry_minors",
    "lift_minors", "mixed_low_lift_minors", "digit_associator_quotient",
    "associator_second_carry", "word_finite_difference",
    "word_second_difference", "trace_hankel_minor", "lift_hankel_minor",
    "character_discriminant", "split_root_residual",
    "conjugacy_coordinate_control"};

static const char* FAMILY_SCHEMAS[FAMILY_COUNT] = {
    "word:entry(r)", "word:entry(C)", "word:tr(C)",
    "word:antitrace(C)", "word:exact_div_N2(det(R)-1)",
    "word:exact_div_N2(CH_unit(R))", "step:entry(K)",
    "step:entry(K mod N)", "step:exact_div_N(K-k)",
    "step:three_minors(K,C_parent,C_word)", "word:entry(comm-I low)",
    "word:entry(comm lift)", "word:tr(comm lift)",
    "word:exact_div_N2(Fricke)", "pair:diff(Fricke_Q)",
    "pair:diff(trace)", "pair:diff(comm_trace)",
    "pair:diff(lift_entry)", "pair:minors(low,low)",
    "pair:minors(lift,lift)", "pair:minors(low,lift)",
    "triple:exact_div_N(digit_associator)",
    "triple:second_carry_associator_side", "triple:first_difference",
    "triple:second_difference", "triple:trace_hankel",
    "triple:lift_hankel", "word:character_discriminant",
    "word:square_root_residual",
    "step:conjugacy_difference(low,lift,K,k,H)"};

[[noreturn]] static void fail(const std::string& s) {
  throw std::runtime_error(s);
}
static void require(bool condition, const std::string& s) {
  if (!condition) fail(s);
}

static u64 splitmix64(u64 x) {
  x += 0x9e3779b97f4a7c15ULL;
  x = (x ^ (x >> 30)) * 0xbf58476d1ce4e5b9ULL;
  x = (x ^ (x >> 27)) * 0x94d049bb133111ebULL;
  return x ^ (x >> 31);
}
struct Rng {
  u64 state;
  explicit Rng(u64 seed) : state(seed) {}
  u64 next() { return state = splitmix64(state); }
};

static cpp_int abs_big(cpp_int x) { return x < 0 ? -x : x; }
static cpp_int mod_big(cpp_int x, const cpp_int& m) {
  x %= m;
  if (x < 0) x += m;
  return x;
}
static cpp_int gcd_big(cpp_int a, cpp_int b) {
  a = abs_big(a);
  b = abs_big(b);
  while (b != 0) {
    cpp_int r = a % b;
    a = b;
    b = r;
  }
  return a;
}
static cpp_int lcm_big(const cpp_int& a, const cpp_int& b) {
  return a == 0 || b == 0 ? cpp_int(0) : abs_big((a / gcd_big(a, b)) * b);
}
static u64 low64(const cpp_int& x) {
  static const cpp_int mask = (cpp_int(1) << 64) - 1;
  return (x & mask).convert_to<u64>();
}
static u64 hash_big(const cpp_int& x, u64 tag) {
  return splitmix64(SOURCE_SEED ^ tag ^ low64(x) ^
                    splitmix64(low64(x >> 64)) ^ splitmix64(low64(x >> 128)));
}
static std::string str_big(const cpp_int& x) {
  return x.convert_to<std::string>();
}
static int bit_length(cpp_int x) {
  x = abs_big(x);
  int n = 0;
  while (x != 0) {
    x >>= 1;
    ++n;
  }
  return n;
}
static cpp_int public_residue(const cpp_int& N, u64 tag) {
  cpp_int x = cpp_int(hash_big(N, tag)) << 64;
  x += splitmix64(hash_big(N, tag ^ 0x9e3779b97f4a7c15ULL));
  return mod_big(x, N - 1) + 1;
}
static cpp_int primitive_n(cpp_int x, const cpp_int& N) {
  bool negative = x < 0;
  x = abs_big(x);
  if (x == 0) return 0;
  while (x % N == 0) x /= N;
  return negative ? -x : x;
}

static u64 mul_u64(u64 a, u64 b, u64 m) {
  return static_cast<u64>((static_cast<u128>(a) * b) % m);
}
static u64 pow_u64(u64 a, u64 e, u64 m) {
  u64 r = 1 % m;
  while (e) {
    if (e & 1) r = mul_u64(r, a, m);
    a = mul_u64(a, a, m);
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
  while (!(d & 1)) {
    d >>= 1;
    ++s;
  }
  for (u64 a : {2ULL, 325ULL, 9375ULL, 28178ULL, 450775ULL, 9780504ULL,
                1795265022ULL}) {
    if (a % n == 0) continue;
    u64 x = pow_u64(a % n, d, n);
    if (x == 1 || x == n - 1) continue;
    bool composite = true;
    for (u64 i = 1; i < s; ++i) {
      x = mul_u64(x, x, n);
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
  const u64 lo = 1ULL << (bits - 1);
  const u64 mask = (1ULL << bits) - 1;
  for (u64 attempt = 0; attempt < PRIME_SEARCH_CAP; ++attempt) {
    u64 x = (rng.next() & mask) | lo | 1;
    for (int i = 0; i < 16384 && x <= mask; ++i, x += 2)
      if (is_prime(x)) return x;
  }
  fail("prime-search retry cap");
}
static u64 random_safe_prime(int bits, Rng& rng) {
  for (u64 attempt = 0; attempt < SAFE_SEARCH_CAP; ++attempt) {
    u64 h = random_prime(bits - 1, rng);
    u64 p = 2 * h + 1;
    if ((p >> (bits - 1)) == 1 && is_prime(p)) return p;
  }
  fail("safe-prime retry cap");
}
static u64 next_prime_same_bits(u64 x, int bits) {
  const u64 limit = 1ULL << bits;
  for (u64 attempt = 0, candidate = x + 2;
       attempt < PRIME_SEARCH_CAP && candidate < limit;
       ++attempt, candidate += 2)
    if (is_prime(candidate)) return candidate;
  return 0;
}

struct Task {
  int bits;
  int cohort;
  int index;
  u64 p;
  u64 q;
};
struct CohortBuild {
  int bits = 0;
  int cohort = 0;
  u64 attempts = 0;
  int accepted = 0;
};
static const char* cohort_name(int c) {
  return c == 0 ? "random" : c == 1 ? "consecutive" : "safe_safe";
}
static std::vector<Task> make_tasks(const std::string& split,
                                    std::vector<CohortBuild>& builds) {
  require(split == "discovery" || split == "heldout", "split name");
  std::vector<Task> tasks;
  std::set<std::pair<u64, u64>> seen;
  for (int bits : FACTOR_BITS) {
    if ((split == "discovery") != (bits <= 32)) continue;
    for (int cohort = 0; cohort < 3; ++cohort) {
      int count = cohort == 0 ? RANDOM_PER_BITS
                  : cohort == 1 ? CONSECUTIVE_PER_BITS
                  : bits == 16 ? SAFE_16_BITS : SAFE_PER_BITS;
      Rng rng(COHORT_SEED ^ (u64(bits) << 32) ^ (u64(cohort) << 48));
      u64 attempts = 0;
      for (int index = 0; index < count;) {
        require(attempts < COHORT_ATTEMPT_CAP, "cohort retry cap");
        ++attempts;
        u64 p = 0, q = 0;
        if (cohort == 0) {
          p = random_prime(bits, rng);
          q = random_prime(bits, rng);
        } else if (cohort == 1) {
          p = random_prime(bits, rng);
          q = next_prime_same_bits(p, bits);
          if (!q) continue;
        } else {
          p = random_safe_prime(bits, rng);
          q = random_safe_prime(bits, rng);
        }
        if (p > q) std::swap(p, q);
        if (p == q || q >= 2 * p || !seen.insert({p, q}).second) continue;
        tasks.push_back({bits, cohort, index++, p, q});
      }
      builds.push_back({bits, cohort, attempts, count});
    }
  }
  require(tasks.size() == (split == "discovery" ? 2208U : 3072U),
          "frozen split cohort size");
  return tasks;
}

struct M2 {
  std::array<cpp_int, 4> a{};
  cpp_int& operator[](int i) { return a[i]; }
  const cpp_int& operator[](int i) const { return a[i]; }
};
static M2 ident() {
  M2 r;
  r[0] = r[3] = 1;
  return r;
}
static M2 add_m(const M2& x, const M2& y) {
  M2 r;
  for (int i = 0; i < 4; ++i) r[i] = x[i] + y[i];
  return r;
}
static M2 sub_m(const M2& x, const M2& y) {
  M2 r;
  for (int i = 0; i < 4; ++i) r[i] = x[i] - y[i];
  return r;
}
static M2 mul_m(const M2& x, const M2& y) {
  M2 r;
  r[0] = x[0] * y[0] + x[1] * y[2];
  r[1] = x[0] * y[1] + x[1] * y[3];
  r[2] = x[2] * y[0] + x[3] * y[2];
  r[3] = x[2] * y[1] + x[3] * y[3];
  return r;
}
static M2 canon_m(M2 x, const cpp_int& m) {
  for (auto& v : x.a) v = mod_big(v, m);
  return x;
}
static M2 mul_mod_m(const M2& x, const M2& y, const cpp_int& m) {
  return canon_m(mul_m(x, y), m);
}
static M2 scalar_m(const M2& x, const cpp_int& s) {
  M2 r;
  for (int i = 0; i < 4; ++i) r[i] = x[i] * s;
  return r;
}
static cpp_int trace_m(const M2& x) { return x[0] + x[3]; }
static cpp_int det_m(const M2& x) { return x[0] * x[3] - x[1] * x[2]; }
static M2 adj_m(const M2& x) {
  M2 r;
  r[0] = x[3];
  r[1] = -x[1];
  r[2] = -x[2];
  r[3] = x[0];
  return r;
}
static bool equal_m(const M2& x, const M2& y) { return x.a == y.a; }
static M2 pow_mod_m(M2 a, cpp_int e, const cpp_int& m) {
  M2 r = ident();
  while (e != 0) {
    if ((e & 1) != 0) r = mul_mod_m(r, a, m);
    a = mul_mod_m(a, a, m);
    e >>= 1;
  }
  return r;
}
static M2 exact_div_m(const M2& x, const cpp_int& d,
                      const std::string& label) {
  M2 r;
  for (int i = 0; i < 4; ++i) {
    require(x[i] % d == 0, label + " exact division");
    r[i] = x[i] / d;
  }
  return r;
}
static cpp_int exact_div(const cpp_int& x, const cpp_int& d,
                         const std::string& label) {
  require(x % d == 0, label + " exact division");
  return x / d;
}
static cpp_int gcd_entries_minus_identity(const M2& x, const cpp_int& N) {
  cpp_int g = N;
  for (int i = 0; i < 4; ++i)
    g = gcd_big(g, x[i] - (i == 0 || i == 3 ? 1 : 0));
  return g;
}
static M2 commutator_mod(const M2& x, const M2& y, const cpp_int& m) {
  M2 r = mul_mod_m(x, y, m);
  r = mul_mod_m(r, canon_m(adj_m(x), m), m);
  return mul_mod_m(r, canon_m(adj_m(y), m), m);
}
static M2 inverse_unimodular_mod(const M2& x, const cpp_int& m) {
  return canon_m(adj_m(x), m);
}
static M2 section_carry(const M2& x, const M2& y, const cpp_int& N) {
  M2 product = mul_m(x, y);
  M2 z = canon_m(product, N);
  return exact_div_m(sub_m(product, z), N, "section carry");
}
static M2 carry_digit(const M2& K, const cpp_int& N) {
  return canon_m(K, N);
}
static M2 second_carry(const M2& K, const cpp_int& N) {
  return exact_div_m(sub_m(K, canon_m(K, N)), N, "second carry");
}
static M2 lift_low(const M2& full, const cpp_int& N) {
  return canon_m(full, N);
}
static M2 lift_digit(const M2& full, const cpp_int& N) {
  return exact_div_m(sub_m(full, canon_m(full, N)), N, "word lift");
}

static cpp_int egcd_inv(cpp_int a, const cpp_int& m) {
  a = mod_big(a, m);
  cpp_int old_r = a, r = m, old_s = 1, s = 0;
  while (r != 0) {
    cpp_int q = old_r / r;
    cpp_int nr = old_r - q * r;
    old_r = r;
    r = nr;
    cpp_int ns = old_s - q * s;
    old_s = s;
    s = ns;
  }
  require(old_r == 1, "modular inverse unit");
  return mod_big(old_s, m);
}

enum class CandidateOp {
  SUM,
  PRODUCT,
  SUM_PLUS_PRODUCT,
  SUM_MINUS_PRODUCT,
  SUM_TIMES_PRODUCT,
  DISCRIMINANT,
  SUM_PAIR_PLUS,
  SUM_PAIR_MINUS,
  PRODUCT_PAIR_PLUS,
  PRODUCT_PAIR_MINUS,
  SUM_PAIR_PRODUCT,
  PAIR_DETERMINANT,
  PAIR_SUM_SQUARES,
  PAIR_RESULTANT,
  SECOND_DIFFERENCE,
  AFFINE_DETERMINANT
};
struct Candidate {
  CandidateOp op;
  int i = 0, j = 0, k = 0;
  std::string syntax;
  u64 aliases = 1;
};

static u64 add_mod_u64(u64 a, u64 b, u64 p) {
  u64 c = a + b;
  if (c >= p || c < a) c -= p;
  return c;
}
static u64 sub_mod_u64(u64 a, u64 b, u64 p) {
  return a >= b ? a - b : p - (b - a);
}
static u64 eval_candidate_u64(const Candidate& c, const std::array<u64, FAMILY_COUNT>& S,
                              const std::array<u64, FAMILY_COUNT>& P, u64 m) {
  auto add = [&](u64 a, u64 b) { return add_mod_u64(a, b, m); };
  auto sub = [&](u64 a, u64 b) { return sub_mod_u64(a, b, m); };
  auto mul = [&](u64 a, u64 b) { return mul_u64(a, b, m); };
  const int i = c.i, j = c.j, k = c.k;
  switch (c.op) {
    case CandidateOp::SUM: return S[i];
    case CandidateOp::PRODUCT: return P[i];
    case CandidateOp::SUM_PLUS_PRODUCT: return add(S[i], P[i]);
    case CandidateOp::SUM_MINUS_PRODUCT: return sub(S[i], P[i]);
    case CandidateOp::SUM_TIMES_PRODUCT: return mul(S[i], P[i]);
    case CandidateOp::DISCRIMINANT:
      return sub(mul(S[i], S[i]), mul(4 % m, P[i]));
    case CandidateOp::SUM_PAIR_PLUS: return add(S[i], S[j]);
    case CandidateOp::SUM_PAIR_MINUS: return sub(S[i], S[j]);
    case CandidateOp::PRODUCT_PAIR_PLUS: return add(P[i], P[j]);
    case CandidateOp::PRODUCT_PAIR_MINUS: return sub(P[i], P[j]);
    case CandidateOp::SUM_PAIR_PRODUCT: return mul(S[i], S[j]);
    case CandidateOp::PAIR_DETERMINANT:
      return sub(mul(S[i], P[j]), mul(P[i], S[j]));
    case CandidateOp::PAIR_SUM_SQUARES:
      return add(mul(S[i], S[i]), mul(S[j], S[j]));
    case CandidateOp::PAIR_RESULTANT: {
      u64 pq = sub(P[i], P[j]);
      u64 sq = sub(mul(S[i], P[j]), mul(S[j], P[i]));
      return add(mul(pq, pq), mul(sub(S[i], S[j]), sq));
    }
    case CandidateOp::SECOND_DIFFERENCE:
      return add(sub(S[i], mul(2, S[j])), S[k]);
    case CandidateOp::AFFINE_DETERMINANT: {
      u64 a = sub(S[j], S[i]), b = sub(P[k], P[i]);
      u64 d = sub(S[k], S[i]), e = sub(P[j], P[i]);
      return sub(mul(a, b), mul(d, e));
    }
  }
  return 0;
}

static cpp_int eval_candidate_big(const Candidate& c,
                                  const std::array<cpp_int, FAMILY_COUNT>& S,
                                  const std::array<cpp_int, FAMILY_COUNT>& P,
                                  const cpp_int& m) {
  auto add = [&](const cpp_int& a, const cpp_int& b) { return mod_big(a + b, m); };
  auto sub = [&](const cpp_int& a, const cpp_int& b) { return mod_big(a - b, m); };
  auto mul = [&](const cpp_int& a, const cpp_int& b) { return mod_big(a * b, m); };
  const int i = c.i, j = c.j, k = c.k;
  switch (c.op) {
    case CandidateOp::SUM: return mod_big(S[i], m);
    case CandidateOp::PRODUCT: return mod_big(P[i], m);
    case CandidateOp::SUM_PLUS_PRODUCT: return add(S[i], P[i]);
    case CandidateOp::SUM_MINUS_PRODUCT: return sub(S[i], P[i]);
    case CandidateOp::SUM_TIMES_PRODUCT: return mul(S[i], P[i]);
    case CandidateOp::DISCRIMINANT: return sub(mul(S[i], S[i]), 4 * P[i]);
    case CandidateOp::SUM_PAIR_PLUS: return add(S[i], S[j]);
    case CandidateOp::SUM_PAIR_MINUS: return sub(S[i], S[j]);
    case CandidateOp::PRODUCT_PAIR_PLUS: return add(P[i], P[j]);
    case CandidateOp::PRODUCT_PAIR_MINUS: return sub(P[i], P[j]);
    case CandidateOp::SUM_PAIR_PRODUCT: return mul(S[i], S[j]);
    case CandidateOp::PAIR_DETERMINANT: return sub(mul(S[i], P[j]), mul(P[i], S[j]));
    case CandidateOp::PAIR_SUM_SQUARES: return add(mul(S[i], S[i]), mul(S[j], S[j]));
    case CandidateOp::PAIR_RESULTANT: {
      cpp_int pq = sub(P[i], P[j]);
      cpp_int sq = sub(mul(S[i], P[j]), mul(S[j], P[i]));
      return add(mul(pq, pq), mul(sub(S[i], S[j]), sq));
    }
    case CandidateOp::SECOND_DIFFERENCE:
      return add(sub(S[i], 2 * S[j]), S[k]);
    case CandidateOp::AFFINE_DETERMINANT:
      return sub(mul(sub(S[j], S[i]), sub(P[k], P[i])),
                 mul(sub(S[k], S[i]), sub(P[j], P[i])));
  }
  return 0;
}

static std::vector<Candidate> build_candidates() {
  std::vector<Candidate> raw;
  auto add = [&](CandidateOp op, int i, int j, int k, std::string syntax) {
    raw.push_back({op, i, j, k, std::move(syntax), 1});
  };
  for (int i = 0; i < FAMILY_COUNT; ++i) {
    std::string f = std::to_string(i);
    add(CandidateOp::SUM, i, 0, 0, "S(" + f + ")");
    add(CandidateOp::PRODUCT, i, 0, 0, "P(" + f + ")");
    add(CandidateOp::SUM_PLUS_PRODUCT, i, 0, 0, "+(P(" + f + "),S(" + f + "))");
    add(CandidateOp::SUM_MINUS_PRODUCT, i, 0, 0, "-(S(" + f + "),P(" + f + "))");
    add(CandidateOp::SUM_TIMES_PRODUCT, i, 0, 0, "*(P(" + f + "),S(" + f + "))");
    add(CandidateOp::DISCRIMINANT, i, 0, 0, "disc(S(" + f + "),P(" + f + "))");
  }
  for (int i = 0; i < FAMILY_COUNT; ++i) for (int j = i + 1; j < FAMILY_COUNT; ++j) {
    std::string a = std::to_string(i), b = std::to_string(j);
    add(CandidateOp::SUM_PAIR_PLUS, i, j, 0, "+(S(" + a + "),S(" + b + "))");
    add(CandidateOp::SUM_PAIR_MINUS, i, j, 0, "-(S(" + a + "),S(" + b + "))");
    add(CandidateOp::PRODUCT_PAIR_PLUS, i, j, 0, "+(P(" + a + "),P(" + b + "))");
    add(CandidateOp::PRODUCT_PAIR_MINUS, i, j, 0, "-(P(" + a + "),P(" + b + "))");
    add(CandidateOp::SUM_PAIR_PRODUCT, i, j, 0, "*(S(" + a + "),S(" + b + "))");
    add(CandidateOp::PAIR_DETERMINANT, i, j, 0, "det(SP(" + a + "),SP(" + b + "))");
    add(CandidateOp::PAIR_SUM_SQUARES, i, j, 0, "norm+(S(" + a + "),S(" + b + "))");
    add(CandidateOp::PAIR_RESULTANT, i, j, 0, "res2(SP(" + a + "),SP(" + b + "))");
  }
  for (int i = 0; i < FAMILY_COUNT; ++i)
    for (int j = i + 1; j < FAMILY_COUNT; ++j)
      for (int k = j + 1; k < FAMILY_COUNT; ++k) {
        std::string a = std::to_string(i), b = std::to_string(j), d = std::to_string(k);
        add(CandidateOp::SECOND_DIFFERENCE, i, j, k,
            "fd2(S(" + a + "),S(" + b + "),S(" + d + "))");
        add(CandidateOp::AFFINE_DETERMINANT, i, j, k,
            "adet(SP(" + a + "),SP(" + b + "),SP(" + d + "))");
      }

  std::array<u64, FAMILY_COUNT> s1{}, p1{}, s2{}, p2{};
  for (int i = 0; i < FAMILY_COUNT; ++i) {
    s1[i] = splitmix64(SYNTH_SEED + 11 * i) % FP1;
    p1[i] = splitmix64(SYNTH_SEED + 13 * i + 1) % FP1;
    s2[i] = splitmix64(SYNTH_SEED + 17 * i + 2) % FP2;
    p2[i] = splitmix64(SYNTH_SEED + 19 * i + 3) % FP2;
  }
  std::map<std::pair<u64, u64>, Candidate> canonical;
  for (auto& c : raw) {
    auto key = std::make_pair(eval_candidate_u64(c, s1, p1, FP1),
                              eval_candidate_u64(c, s2, p2, FP2));
    auto it = canonical.find(key);
    if (it == canonical.end()) canonical.emplace(key, c);
    else {
      ++it->second.aliases;
      if (c.syntax.size() < it->second.syntax.size() ||
          (c.syntax.size() == it->second.syntax.size() && c.syntax < it->second.syntax)) {
        u64 aliases = it->second.aliases;
        it->second = c;
        it->second.aliases = aliases;
      }
    }
  }
  std::vector<Candidate> out;
  out.reserve(canonical.size());
  for (auto& kv : canonical) out.push_back(std::move(kv.second));
  std::sort(out.begin(), out.end(), [](const Candidate& a, const Candidate& b) {
    return std::tie(a.syntax, a.i, a.j, a.k) < std::tie(b.syntax, b.i, b.j, b.k);
  });
  return out;
}

struct FamilyState {
  cpp_int N;
  std::array<u64, FAMILY_COUNT> atoms{}, zeros{}, units{}, n_powers{}, hits{};
  std::array<cpp_int, FAMILY_COUNT> sum{}, product{};
  std::array<std::vector<cpp_int>, FAMILY_COUNT> exact_atoms;
  std::array<u64, DECOY_COUNT> decoy_counts{};
  u64 cleanup_hits = 0;
  u64 source_gcd_hits = 0;
  u64 noncommutative_profiles = 0;
  u64 decoy_zeros = 0;
  u64 atom_hash = 0;
  std::array<u64, 5> basis_original_count{}, basis_conjugate_count{};
  std::array<u64, 5> basis_original_hash{}, basis_conjugate_hash{};
  std::string first_factor;
  explicit FamilyState(cpp_int modulus) : N(std::move(modulus)) {
    for (auto& x : product) x = 1;
  }
  void atom(int family, cpp_int value, const std::string& scope) {
    require(family >= 0 && family < FAMILY_COUNT, "family range");
    ++atoms[family];
    if (value == 0) {
      ++zeros[family];
      return;
    }
    while (value % N == 0) {
      value /= N;
      ++n_powers[family];
    }
    if (abs_big(value) == 1) ++units[family];
    cpp_int g = gcd_big(value, N);
    if (g > 1 && g < N) {
      ++hits[family];
      ++cleanup_hits;
      if (first_factor.empty()) first_factor = scope + ":" + str_big(g);
    }
    sum[family] = mod_big(sum[family] + value, N);
    product[family] = mod_big(product[family] * mod_big(value, N), N);
    exact_atoms[family].push_back(std::move(value));
    atom_hash = splitmix64(atom_hash ^ u64(family + 1) ^ low64(exact_atoms[family].back()));
  }
  void source_screen(const cpp_int& value, const std::string& scope) {
    cpp_int g = gcd_big(value, N);
    if (g > 1 && g < N) {
      ++cleanup_hits;
      ++source_gcd_hits;
      if (first_factor.empty()) first_factor = scope + ":" + str_big(g);
    }
  }
  void basis(int feature, bool conjugate, const cpp_int& value, u64 tag) {
    require(feature >= 0 && feature < 5, "basis feature range");
    if (conjugate) {
      ++basis_conjugate_count[feature];
      basis_conjugate_hash[feature] = splitmix64(
          basis_conjugate_hash[feature] ^ hash_big(value, tag));
    } else {
      ++basis_original_count[feature];
      basis_original_hash[feature] = splitmix64(
          basis_original_hash[feature] ^ hash_big(value, tag));
    }
  }
  void decoy(int kind, bool condition, const std::string& label) {
    require(kind >= 0 && kind < DECOY_COUNT, "decoy range");
    require(condition, label);
    ++decoy_counts[kind];
    ++decoy_zeros;
  }
};

struct WordNode {
  M2 full;
  M2 low;
  M2 lift;
  int parent = 0;
  int last = -1;
  int length = 0;
  u64 code = 0;
};
struct Profile {
  cpp_int a, b, c, u;
  std::array<M2, 4> generator;
  M2 conjugator;
  M2 conjugator_inverse;
  std::vector<WordNode> words;
  M2 cyclic_control;
  bool has_cyclic_control = false;
};

static M2 upper(const cpp_int& x, const cpp_int& m) {
  M2 r = ident();
  r[1] = mod_big(x, m);
  return r;
}
static M2 lower(const cpp_int& x, const cpp_int& m) {
  M2 r = ident();
  r[2] = mod_big(x, m);
  return r;
}
static cpp_int public_unit(const cpp_int& N, u64 tag, FamilyState& state,
                           const std::string& scope) {
  for (u64 attempt = 0; attempt < 128; ++attempt) {
    cpp_int value = public_residue(N, tag ^ splitmix64(attempt));
    cpp_int g = gcd_big(value, N);
    if (g == 1) return value;
    state.source_screen(value, scope);
  }
  fail("public-unit retry cap");
}
static Profile make_profile(const cpp_int& N, int profile, FamilyState& state) {
  const cpp_int N2 = N * N;
  const u64 base = SOURCE_SEED ^ (u64(profile) << 56);
  Profile out;
  out.a = public_unit(N, base ^ 0xa1, state,
                      "profile" + std::to_string(profile) + "_a_gcd");
  out.b = public_unit(N, base ^ 0xb2, state,
                      "profile" + std::to_string(profile) + "_b_gcd");
  out.c = public_residue(N, base ^ 0xc3);
  state.source_screen(out.c, "profile" + std::to_string(profile) + "_c_gcd");
  out.u = public_unit(N, base ^ 0xd4, state,
                      "profile" + std::to_string(profile) + "_u_gcd");
  out.generator = {upper(out.a, N2), upper(-out.a, N2),
                   lower(out.b, N2), lower(-out.b, N2)};
  out.conjugator = upper(out.c, N2);
  out.conjugator_inverse = upper(-out.c, N2);
  out.words.reserve(4373);
  WordNode identity;
  identity.full = identity.low = ident();
  out.words.push_back(identity);
  std::size_t layer_begin = 0, layer_end = 1;
  for (int length = 1; length <= WORD_DEPTH; ++length) {
    std::size_t next_begin = out.words.size();
    for (std::size_t parent = layer_begin; parent < layer_end; ++parent) {
      for (int letter = 0; letter < 4; ++letter) {
        if (out.words[parent].last >= 0 && letter == (out.words[parent].last ^ 1)) continue;
        WordNode node;
        node.parent = static_cast<int>(parent);
        node.last = letter;
        node.length = length;
        node.code = (out.words[parent].code << 2) | u64(letter);
        node.full = mul_mod_m(out.words[parent].full, out.generator[letter], N2);
        node.low = lift_low(node.full, N);
        node.lift = lift_digit(node.full, N);
        out.words.push_back(std::move(node));
      }
    }
    layer_begin = next_begin;
    layer_end = out.words.size();
  }
  require(out.words.size() == 4373, "reduced word count");

  require(!equal_m(mul_mod_m(out.generator[0], out.generator[2], N),
                   mul_mod_m(out.generator[2], out.generator[0], N)),
          "noncommuting public generators");
  ++state.noncommutative_profiles;

  cpp_int gu = gcd_big(out.u, N);
  if (gu > 1 && gu < N) {
    ++state.cleanup_hits;
    if (state.first_factor.empty()) state.first_factor = "profile_unit:" + str_big(gu);
  } else if (gu == 1) {
    cpp_int ui = egcd_inv(out.u, N2);
    M2 diagonal;
    diagonal[0] = out.u;
    diagonal[3] = ui;
    out.cyclic_control = mul_mod_m(mul_mod_m(out.conjugator, diagonal, N2),
                                   out.conjugator_inverse, N2);
    out.has_cyclic_control = true;
  }
  return out;
}

static u64 word_scope_hash(const cpp_int& N, int profile, u64 tag,
                           const WordNode& word) {
  u64 h = hash_big(N, SOURCE_SEED ^ tag ^ (u64(profile) << 48));
  h = splitmix64(h ^ (u64(word.length) << 56));
  return splitmix64(h ^ word.code);
}
static std::vector<int> priority_words(const Profile& words, int cap,
                                       const cpp_int& N, int profile, u64 tag) {
  std::vector<std::pair<u64, int>> scored;
  scored.reserve(words.words.size() - 1);
  for (int i = 1; i < static_cast<int>(words.words.size()); ++i)
    scored.push_back({word_scope_hash(N, profile, tag, words.words[i]), i});
  int keep = std::min(cap, static_cast<int>(scored.size()));
  std::sort(scored.begin(), scored.end());
  scored.resize(keep);
  std::vector<int> out;
  out.reserve(keep);
  for (auto& x : scored) out.push_back(x.second);
  return out;
}

static u64 choose2(u64 n) { return n < 2 ? 0 : n * (n - 1) / 2; }
static u64 choose3(u64 n) { return n < 3 ? 0 : n * (n - 1) * (n - 2) / 6; }
static std::vector<u64> permuted_scope_ranks(u64 total, int cap,
                                             const cpp_int& N, int profile,
                                             u64 tag) {
  require(total >= static_cast<u64>(cap) && cap > 0, "scope rank capacity");
  u64 seed = hash_big(N, SOURCE_SEED ^ tag ^ (u64(profile) << 48));
  u64 start = splitmix64(seed) % total;
  u64 step = 0;
  for (u64 attempt = 0; attempt < SCOPE_STEP_CAP; ++attempt) {
    u64 candidate = 1 + (splitmix64(seed ^ 0x9e3779b97f4a7c15ULL) + attempt) % (total - 1);
    if (std::gcd(candidate, total) == 1) {
      step = candidate;
      break;
    }
  }
  require(step != 0, "scope-step retry cap");
  std::vector<u64> ranks;
  ranks.reserve(cap);
  u64 rank = start;
  for (int i = 0; i < cap; ++i) {
    ranks.push_back(rank);
    rank = static_cast<u64>((static_cast<u128>(rank) + step) % total);
  }
  return ranks;
}

static std::pair<int, int> unrank_pair(int count, u64 rank) {
  const u64 total = choose2(static_cast<u64>(count));
  require(rank < total, "pair rank");
  int low = 0, high = count - 1;
  while (low + 1 < high) {
    int mid = low + (high - low) / 2;
    u64 before = total - choose2(static_cast<u64>(count - mid));
    if (before <= rank) low = mid;
    else high = mid;
  }
  int i = low;
  u64 before = total - choose2(static_cast<u64>(count - i));
  int j = i + 1 + static_cast<int>(rank - before);
  require(i >= 0 && i < j && j < count, "unrank pair result");
  return {i + 1, j + 1};
}

static std::array<int, 3> unrank_triple(int count, u64 rank) {
  const u64 total = choose3(static_cast<u64>(count));
  require(rank < total, "triple rank");
  int low = 0, high = count - 2;
  while (low + 1 < high) {
    int mid = low + (high - low) / 2;
    u64 before = total - choose3(static_cast<u64>(count - mid));
    if (before <= rank) low = mid;
    else high = mid;
  }
  int i = low;
  u64 before_i = total - choose3(static_cast<u64>(count - i));
  u64 pair_rank = rank - before_i;
  int remaining = count - i - 1;
  u64 pair_total = choose2(static_cast<u64>(remaining));
  int pair_low = 0, pair_high = remaining - 1;
  while (pair_low + 1 < pair_high) {
    int mid = pair_low + (pair_high - pair_low) / 2;
    u64 before = pair_total - choose2(static_cast<u64>(remaining - mid));
    if (before <= pair_rank) pair_low = mid;
    else pair_high = mid;
  }
  int j_rel = pair_low;
  u64 before_j = pair_total - choose2(static_cast<u64>(remaining - j_rel));
  int k_rel = j_rel + 1 + static_cast<int>(pair_rank - before_j);
  int j = i + 1 + j_rel, k = i + 1 + k_rel;
  require(i >= 0 && i < j && j < k && k < count, "unrank triple result");
  return {i + 1, j + 1, k + 1};
}

static void add_minor(FamilyState& state, int family, const M2& x, const M2& y,
                      int i, int j, const std::string& scope) {
  state.atom(family, x[i] * y[j] - x[j] * y[i], scope);
}

static cpp_int fricke_quotient(const M2& A, const M2& B, const cpp_int& N) {
  cpp_int N2 = N * N;
  M2 AB = mul_mod_m(A, B, N2);
  M2 C = commutator_mod(A, B, N2);
  cpp_int x = trace_m(A), y = trace_m(B), z = trace_m(AB);
  cpp_int numerator = trace_m(C) - x * x - y * y - z * z + x * y * z + 2;
  return exact_div(numerator, N2, "Fricke /N2");
}
static M2 cayley_quotient(const M2& R, const cpp_int& N) {
  M2 numerator = sub_m(mul_m(R, R), scalar_m(R, trace_m(R)));
  numerator = add_m(numerator, ident());
  return exact_div_m(numerator, N * N, "Cayley /N2");
}
static cpp_int character_discriminant(const M2& low) {
  cpp_int t = trace_m(low);
  return t * t - 4 * det_m(low);
}
static std::vector<cpp_int> split_root_proposals(const M2& low, const M2& lift,
                                                 const M2& conjugate_low,
                                                 const M2& conjugate_lift) {
  return {low[0] - low[3], low[1] + low[2], low[1] - low[2],
          lift[0] - lift[3], lift[1] + lift[2], lift[1] - lift[2],
          trace_m(lift),
          conjugate_low[0] - conjugate_low[3],
          conjugate_low[1] + conjugate_low[2],
          conjugate_low[1] - conjugate_low[2],
          conjugate_lift[0] - conjugate_lift[3],
          conjugate_lift[1] + conjugate_lift[2],
          conjugate_lift[1] - conjugate_lift[2], trace_m(conjugate_lift)};
}
struct SplitCheck {
  bool certified = false;
  cpp_int factor = 1;
  std::array<u64, ROOT_PROPOSAL_COUNT> index_checks{};
  u64 proposals_checked = 0;
  u64 square_matches = 0;
  u64 unit_matches = 0;
  u64 proper_matches = 0;
  u64 transcript_hash = 0;
};
static SplitCheck check_split_certificate(const M2& full, const cpp_int& N,
                                           const M2& conjugator,
                                           const M2& conjugator_inverse) {
  M2 low = lift_low(full, N), lift = lift_digit(full, N);
  M2 conjugate = mul_mod_m(mul_mod_m(conjugator, full, N * N),
                           conjugator_inverse, N * N);
  M2 conjugate_low = lift_low(conjugate, N);
  M2 conjugate_lift = lift_digit(conjugate, N);
  cpp_int disc = mod_big(character_discriminant(low), N);
  std::vector<cpp_int> proposals = split_root_proposals(
      low, lift, conjugate_low, conjugate_lift);
  require(proposals.size() == ROOT_PROPOSAL_COUNT, "root proposal count");
  SplitCheck out;
  for (int index = 0; index < ROOT_PROPOSAL_COUNT; ++index) {
    const cpp_int& s = proposals[index];
    ++out.proposals_checked;
    ++out.index_checks[index];
    cpp_int residue = mod_big(s * s - disc, N);
    cpp_int g = 1;
    u64 outcome = 0;
    if (residue == 0) {
      ++out.square_matches;
      g = gcd_big(s, N);
      if (g > 1 && g < N) {
        ++out.proper_matches;
        if (out.factor == 1) out.factor = g;
        outcome = 2;
      } else if (g == 1) {
        ++out.unit_matches;
        out.certified = true;
        outcome = 1;
      } else {
        outcome = 3;
      }
    }
    u64 item = splitmix64(
        u64(index + 1) ^ (outcome << 8) ^
        hash_big(mod_big(s, N), 0x264d030001ULL + u64(index)) ^
        hash_big(residue, 0x264d030101ULL + u64(index)) ^
        hash_big(g, 0x264d030201ULL + u64(index)));
    out.transcript_hash = splitmix64(out.transcript_hash ^ item);
  }
  return out;
}

static std::vector<std::pair<int, int>> public_pairs(int count, int cap,
                                                     const cpp_int& N,
                                                     int profile, u64 tag) {
  std::vector<std::pair<int, int>> out;
  out.reserve(cap);
  for (u64 rank : permuted_scope_ranks(choose2(count), cap, N, profile, tag))
    out.push_back(unrank_pair(count, rank));
  return out;
}
static std::vector<std::array<int, 3>> public_triples(int count, int cap,
                                                      const cpp_int& N,
                                                      int profile, u64 tag) {
  std::vector<std::array<int, 3>> out;
  out.reserve(cap);
  for (u64 rank : permuted_scope_ranks(choose3(count), cap, N, profile, tag))
    out.push_back(unrank_triple(count, rank));
  return out;
}

static void process_profile_atoms(Profile& profile, int profile_id,
                                  const cpp_int& N, FamilyState& state) {
  const cpp_int N2 = N * N;
  for (std::size_t index = 1; index < profile.words.size(); ++index) {
    const WordNode& w = profile.words[index];
    const WordNode& parent = profile.words[w.parent];
    M2 generator_low = lift_low(profile.generator[w.last], N);
    M2 K = section_carry(parent.low, generator_low, N);
    M2 k = carry_digit(K, N), H = second_carry(K, N);
    u64 word_hash = word_scope_hash(N, profile_id, 0x5ca1a2c0ULL, w);
    int q = int(word_hash & 3ULL);
    int q2 = (q + 1) & 3;
    std::string scope = "p" + std::to_string(profile_id) + ":w" +
                        std::to_string(w.length) + ":" + std::to_string(w.code);
    state.atom(0, w.low[q], scope + ":low");
    state.atom(1, w.lift[q], scope + ":lift");
    state.atom(2, trace_m(w.lift), scope + ":lift_trace");
    state.atom(3, q & 1 ? w.lift[0] - w.lift[3] : w.lift[1] - w.lift[2],
               scope + ":lift_antitrace");
    state.atom(4, exact_div(det_m(w.full) - 1, N2, "det /N2"), scope + ":detQ");
    M2 ch = cayley_quotient(w.full, N);
    state.decoy(5, true, "Cayley-Hamilton modulo N2");
    state.decoy(6,
                mod_big(det_m(w.full) -
                            det_m(parent.full) * det_m(profile.generator[w.last]),
                        N2) == 0,
                "determinant multiplicativity modulo N2");
    state.decoy(7, mod_big(det_m(w.full) - 1, N2) == 0,
                "determinant-one word modulo N2");
    state.atom(5, ch[q], scope + ":chQ");
    state.atom(6, K[q], scope + ":K");
    state.atom(7, k[q], scope + ":k");
    state.atom(8, H[q], scope + ":H");
    add_minor(state, 9, K, parent.lift, q, q2, scope + ":minor_K_parent");
    add_minor(state, 9, K, w.lift, q, q2, scope + ":minor_K_word");
    add_minor(state, 9, parent.lift, w.lift, q, q2,
              scope + ":minor_parent_word");

    M2 conjugate_parent = mul_mod_m(
        mul_mod_m(profile.conjugator, parent.full, N2),
        profile.conjugator_inverse, N2);
    M2 conjugate_generator = mul_mod_m(
        mul_mod_m(profile.conjugator, profile.generator[w.last], N2),
        profile.conjugator_inverse, N2);
    M2 conjugate_word = mul_mod_m(
        mul_mod_m(profile.conjugator, w.full, N2),
        profile.conjugator_inverse, N2);
    M2 conjugate_parent_low = lift_low(conjugate_parent, N);
    M2 conjugate_generator_low = lift_low(conjugate_generator, N);
    M2 conjugate_low = lift_low(conjugate_word, N);
    M2 conjugate_lift = lift_digit(conjugate_word, N);
    M2 conjugate_K = section_carry(conjugate_parent_low,
                                    conjugate_generator_low, N);
    M2 conjugate_k = carry_digit(conjugate_K, N);
    M2 conjugate_H = second_carry(conjugate_K, N);
    std::array<M2, 5> original_features{w.low, w.lift, K, k, H};
    std::array<M2, 5> conjugate_features{conjugate_low, conjugate_lift,
                                         conjugate_K, conjugate_k, conjugate_H};
    for (int feature = 0; feature < 5; ++feature)
      for (int coordinate = 0; coordinate < 4; ++coordinate) {
        u64 tag = word_hash ^ (u64(feature + 1) << 32) ^ u64(coordinate + 1);
        state.basis(feature, false, original_features[feature][coordinate], tag);
        state.basis(feature, true, conjugate_features[feature][coordinate], tag);
      }
    state.atom(29, conjugate_low[q] - w.low[q], scope + ":conj_low");
    state.atom(29, conjugate_lift[q] - w.lift[q], scope + ":conj_lift");
    state.atom(29, conjugate_K[q] - K[q], scope + ":conj_K");
    state.atom(29, conjugate_k[q] - k[q], scope + ":conj_k");
    state.atom(29, conjugate_H[q] - H[q], scope + ":conj_H");
    state.decoy(8, mod_big(trace_m(conjugate_word) - trace_m(w.full), N2) == 0,
                "conjugacy trace decoy");
    state.decoy(9, mod_big(det_m(conjugate_word) - det_m(w.full), N2) == 0,
                "conjugacy determinant decoy");
    cpp_int disc = character_discriminant(w.low);
    state.atom(27, disc, scope + ":disc");
    require(mod_big(character_discriminant(conjugate_low) - disc, N) == 0,
            "conjugacy character discriminant");
    auto roots = split_root_proposals(w.low, w.lift, conjugate_low, conjugate_lift);
    int root0 = int((word_hash >> 8) % 7), root1 = 7 + int((word_hash >> 16) % 7);
    state.atom(28, roots[root0] * roots[root0] - disc, scope + ":root_original");
    state.atom(28, roots[root1] * roots[root1] - disc, scope + ":root_conjugate");
  }

  std::vector<int> comm_scope = priority_words(profile, COMMUTATOR_CAP, N,
                                                profile_id, 0xc011a7eULL);
  for (int index : comm_scope) {
    const WordNode& w = profile.words[index];
    int letter = int(word_scope_hash(N, profile_id, 0xf11cc0deULL, w) & 3ULL);
    const M2& g = profile.generator[letter];
    M2 comm = commutator_mod(w.full, g, N2);
    M2 low = lift_low(comm, N), lift = lift_digit(comm, N);
    std::string scope = "p" + std::to_string(profile_id) + ":comm:" + std::to_string(index);
    for (int q = 0; q < 4; ++q) {
      state.atom(10, low[q] - (q == 0 || q == 3 ? 1 : 0), scope + ":low");
      state.atom(11, lift[q], scope + ":lift");
    }
    state.atom(12, trace_m(lift), scope + ":trace_lift");
    cpp_int fq = fricke_quotient(w.full, g, N);
    state.atom(13, fq, scope + ":frickeQ");
    state.decoy(4, true, "Fricke modulo N2");
    M2 wg = mul_mod_m(w.full, g, N2), gw = mul_mod_m(g, w.full, N2);
    state.decoy(2, mod_big(trace_m(wg) - trace_m(gw), N2) == 0,
                "trace cyclicity decoy");

    M2 inverse = inverse_unimodular_mod(w.full, N2);
    state.decoy(3, mod_big(trace_m(inverse) - trace_m(w.full), N2) == 0,
                "inverse trace decoy");
  }

  auto pairs = public_pairs(static_cast<int>(profile.words.size()) - 1, PAIR_CAP,
                            N, profile_id, 0x2a17c011ULL);
  for (const auto& ij : pairs) {
    const WordNode& u = profile.words[ij.first];
    const WordNode& v = profile.words[ij.second];
    std::string scope = "p" + std::to_string(profile_id) + ":pair:" +
                        std::to_string(ij.first) + ":" + std::to_string(ij.second);
    cpp_int fu = fricke_quotient(u.full, profile.generator[0], N);
    cpp_int fv = fricke_quotient(v.full, profile.generator[0], N);
    state.atom(14, fu - fv, scope + ":fricke_diff");
    state.atom(15, trace_m(u.low) - trace_m(v.low), scope + ":trace_diff");
    M2 cu = commutator_mod(u.full, profile.generator[0], N2);
    M2 cv = commutator_mod(v.full, profile.generator[0], N2);
    state.atom(16, trace_m(lift_low(cu, N)) - trace_m(lift_low(cv, N)),
               scope + ":comm_trace_diff");
    u64 pair_hash = word_scope_hash(N, profile_id, 0x2a17c011ULL, u);
    pair_hash = splitmix64(pair_hash ^ (u64(v.length) << 56) ^ v.code);
    int q = int(pair_hash & 3ULL), q2 = (q + 1) & 3;
    state.atom(17, u.lift[q] - v.lift[q], scope + ":lift_diff");
    add_minor(state, 18, u.low, v.low, q, q2, scope + ":low_minor");
    add_minor(state, 19, u.lift, v.lift, q, q2, scope + ":lift_minor");
    add_minor(state, 20, u.low, v.lift, q, q2, scope + ":mixed_minor");
  }

  auto triples = public_triples(static_cast<int>(profile.words.size()) - 1, TRIPLE_CAP,
                                N, profile_id, 0x7a1a550cULL);
  for (const auto& abc : triples) {
    const WordNode& u = profile.words[abc[0]];
    const WordNode& v = profile.words[abc[1]];
    const WordNode& w = profile.words[abc[2]];
    M2 uv = canon_m(mul_m(u.low, v.low), N), vw = canon_m(mul_m(v.low, w.low), N);
    M2 Kuv = section_carry(u.low, v.low, N), Kvw = section_carry(v.low, w.low, N);
    M2 Kleft = section_carry(uv, w.low, N), Kright = section_carry(u.low, vw, N);
    M2 full_assoc = sub_m(add_m(Kleft, mul_m(Kuv, w.low)),
                          add_m(Kright, mul_m(u.low, Kvw)));
    state.decoy(0, equal_m(full_assoc, M2{}), "exact noncommutative associator");
    M2 kuv = carry_digit(Kuv, N), kvw = carry_digit(Kvw, N);
    M2 kleft = carry_digit(Kleft, N), kright = carry_digit(Kright, N);
    M2 digit_assoc = sub_m(add_m(kleft, mul_m(kuv, w.low)),
                           add_m(kright, mul_m(u.low, kvw)));
    M2 quotient = exact_div_m(digit_assoc, N, "digit associator /N");
    M2 Huv = second_carry(Kuv, N), Hvw = second_carry(Kvw, N);
    M2 Hleft = second_carry(Kleft, N), Hright = second_carry(Kright, N);
    M2 rhs = sub_m(add_m(Hright, mul_m(u.low, Hvw)),
                   add_m(Hleft, mul_m(Huv, w.low)));
    state.decoy(1, equal_m(quotient, rhs), "associator quotient identity");
    u64 triple_hash = word_scope_hash(N, profile_id, 0x7a1a550cULL, u);
    triple_hash = splitmix64(triple_hash ^ (u64(v.length) << 56) ^ v.code);
    triple_hash = splitmix64(triple_hash ^ (u64(w.length) << 56) ^ w.code);
    int q = int(triple_hash & 3ULL);
    state.atom(21, quotient[q], "assoc:Q");
    state.atom(22, rhs[q], "assoc:Hside");
    cpp_int t0 = trace_m(u.low), t1 = trace_m(v.low), t2 = trace_m(w.low);
    state.atom(23, t1 - t0, "triple:fd1");
    state.atom(24, t0 - 2 * t1 + t2, "triple:fd2");
    state.atom(25, t0 * t2 - t1 * t1, "triple:trace_hankel");
    state.atom(26, u.lift[q] * w.lift[q] - v.lift[q] * v.lift[q],
               "triple:lift_hankel");
  }
}

struct SmoothSchedule {
  cpp_int value = 1;
  std::vector<std::pair<int, int>> factors;
};
static SmoothSchedule lcm_schedule(int limit) {
  SmoothSchedule out;
  for (int p = 2; p <= limit; ++p) {
    bool prime = true;
    for (int d = 2; d * d <= p; ++d) if (p % d == 0) { prime = false; break; }
    if (!prime) continue;
    int power = p, exponent = 1;
    while (power <= limit / p) {
      power *= p;
      ++exponent;
    }
    out.factors.push_back({p, exponent});
    for (int i = 0; i < exponent; ++i) out.value *= p;
  }
  return out;
}

struct OrderStats {
  u64 trials = 0, initial_returns = 0, gcd_hits = 0, split_returns = 0;
  u64 certified_blocks = 0, noncyclic_blocks = 0;
  std::array<u64, ROOT_PROPOSAL_COUNT> root_index_checks{};
  u64 root_proposals_checked = 0, root_square_matches = 0;
  u64 root_unit_matches = 0, root_proper_matches = 0;
  u64 root_transcript_hash = 0;
  cpp_int lcm = 1, cyclic_lcm = 1;
  std::string first_factor;
};
static void order_trial(const M2& G, const cpp_int& N, const SmoothSchedule& schedule,
                        const M2& conjugator, const M2& conjugator_inverse,
                        bool cyclic_control, OrderStats& stats) {
  u64 trial_index = stats.trials++;
  SplitCheck split = check_split_certificate(G, N, conjugator,
                                              conjugator_inverse);
  stats.root_proposals_checked += split.proposals_checked;
  stats.root_square_matches += split.square_matches;
  stats.root_unit_matches += split.unit_matches;
  stats.root_proper_matches += split.proper_matches;
  for (int index = 0; index < ROOT_PROPOSAL_COUNT; ++index)
    stats.root_index_checks[index] += split.index_checks[index];
  stats.root_transcript_hash = splitmix64(
      stats.root_transcript_hash ^ splitmix64(trial_index + 1) ^
      split.transcript_hash);
  if (split.factor > 1 && split.factor < N) {
    ++stats.gcd_hits;
    if (stats.first_factor.empty())
      stats.first_factor = "split_root:" + str_big(split.factor);
    return;
  }
  M2 power = pow_mod_m(lift_low(G, N), schedule.value, N);
  cpp_int g = gcd_entries_minus_identity(power, N);
  if (g > 1 && g < N) {
    ++stats.gcd_hits;
    if (stats.first_factor.empty()) stats.first_factor = "order_initial:" + str_big(g);
    return;
  }
  if (g != N) return;
  ++stats.initial_returns;
  cpp_int current = schedule.value;
  for (const auto& pe : schedule.factors) {
    int p = pe.first;
    for (int e = 0; e < pe.second; ++e) {
      cpp_int candidate = current / p;
      M2 test = pow_mod_m(lift_low(G, N), candidate, N);
      cpp_int h = gcd_entries_minus_identity(test, N);
      if (h == N) current = candidate;
      else if (h == 1) break;
      else {
        ++stats.gcd_hits;
        if (stats.first_factor.empty()) stats.first_factor = "order_strip:" + str_big(h);
        return;
      }
    }
  }
  if (!split.certified) return;
  ++stats.split_returns;
  ++stats.certified_blocks;
  if (cyclic_control) stats.cyclic_lcm = lcm_big(stats.cyclic_lcm, current);
  else {
    ++stats.noncyclic_blocks;
    stats.lcm = lcm_big(stats.lcm, current);
  }
}

static OrderStats run_order_programs(const cpp_int& N,
                                     const std::array<Profile, PROFILE_COUNT>& profiles) {
  OrderStats stats;
  std::array<SmoothSchedule, 2> schedules{lcm_schedule(64), lcm_schedule(128)};
  for (int profile = 0; profile < PROFILE_COUNT; ++profile) {
    auto indices = priority_words(profiles[profile], ORDER_MAIN_PER_PROFILE, N,
                                  profile, 0x0dde2a11ULL);
    for (int index : indices)
      for (const auto& schedule : schedules)
        order_trial(profiles[profile].words[index].full, N, schedule,
                    profiles[profile].conjugator,
                    profiles[profile].conjugator_inverse, false, stats);
    if (profiles[profile].has_cyclic_control)
      for (const auto& schedule : schedules)
        order_trial(profiles[profile].cyclic_control, N, schedule,
                    profiles[profile].conjugator,
                    profiles[profile].conjugator_inverse, true, stats);
  }
  return stats;
}

struct PublicResult {
  FamilyState state;
  OrderStats order;
  std::vector<std::pair<int, cpp_int>> candidate_hits;
  u64 candidate_hash = 0;
  explicit PublicResult(cpp_int N) : state(std::move(N)) {}
};
static PublicResult process_public(const cpp_int& N,
                                   const std::vector<Candidate>& candidates) {
  PublicResult out(N);
  std::array<Profile, PROFILE_COUNT> profiles;
  for (int p = 0; p < PROFILE_COUNT; ++p) {
    profiles[p] = make_profile(N, p, out.state);
    process_profile_atoms(profiles[p], p, N, out.state);
  }
  out.order = run_order_programs(N, profiles);
  if (!out.order.first_factor.empty() && out.state.first_factor.empty())
    out.state.first_factor = out.order.first_factor;
  for (int i = 0; i < static_cast<int>(candidates.size()); ++i) {
    cpp_int residue = eval_candidate_big(candidates[i], out.state.sum, out.state.product, N);
    cpp_int g = gcd_big(residue, N);
    if (g > 1 && g < N) {
      out.candidate_hits.push_back({i, g});
      out.candidate_hash = splitmix64(out.candidate_hash ^ u64(i + 1) ^ low64(g));
      if (out.state.first_factor.empty())
        out.state.first_factor = "candidate:" + std::to_string(i) + ":" + str_big(g);
    }
  }
  return out;
}

static u64 mod_big_u64(const cpp_int& x, u64 m) {
  cpp_int r = x % m;
  if (r < 0) r += m;
  return r.convert_to<u64>();
}
static u64 gcd_u64(u64 a, u64 b) { return std::gcd(a, b); }
static int ceil_log2_u64(u64 x) {
  require(x >= 1, "positive ceil-log2 input");
  if (x == 1) return 0;
  int bits = 0;
  for (u64 y = x - 1; y != 0; y >>= 1) ++bits;
  return bits;
}
struct ResidualPair {
  u64 gp = 1, gq = 1;
  int loss_bits = 0;
  u64 improvement_p = 1, improvement_q = 1;
};
static std::vector<ResidualPair> score_p205(const FamilyState& state, u64 p, u64 q) {
  u64 d = gcd_u64(p - 1, q - 1), sp = (p - 1) / d, sq = (q - 1) / d;
  std::array<u64, FAMILY_COUNT> pp{}, pq{};
  pp.fill(1 % sp);
  pq.fill(1 % sq);
  for (int f = 0; f < FAMILY_COUNT; ++f)
    for (const cpp_int& atom : state.exact_atoms[f]) {
      pp[f] = mul_u64(pp[f], mod_big_u64(atom, sp), sp);
      pq[f] = mul_u64(pq[f], mod_big_u64(atom, sq), sq);
    }
  int n = bit_length(state.N);
  u64 basep = mod_big_u64(state.N - 1, sp), baseq = mod_big_u64(state.N - 1, sq);
  std::vector<ResidualPair> out;
  out.reserve(467);
  auto insert = [&](u64 vp, u64 vq) {
    vp = pow_u64(vp, n, sp);
    vq = pow_u64(vq, n, sq);
    out.push_back({gcd_u64(vp, sp), gcd_u64(vq, sq)});
  };
  insert(basep, baseq);
  for (int f = 0; f < FAMILY_COUNT; ++f)
    insert(mul_u64(basep, pp[f], sp), mul_u64(baseq, pq[f], sq));
  for (int f = 0; f < FAMILY_COUNT; ++f)
    for (int g = f + 1; g < FAMILY_COUNT; ++g)
      insert(mul_u64(mul_u64(basep, pp[f], sp), pp[g], sp),
             mul_u64(mul_u64(baseq, pq[f], sq), pq[g], sq));
  u64 allp = basep, allq = baseq;
  for (int f = 0; f < FAMILY_COUNT; ++f) {
    allp = mul_u64(allp, pp[f], sp);
    allq = mul_u64(allq, pq[f], sq);
  }
  insert(allp, allq);
  require(out.size() == 467, "P205 word count");
  const u64 baseline_p = out[0].gp, baseline_q = out[0].gq;
  for (auto& score : out) {
    require(score.gp % baseline_p == 0 && score.gq % baseline_q == 0,
            "P205 baseline divisibility");
    score.improvement_p = score.gp / baseline_p;
    score.improvement_q = score.gq / baseline_q;
    score.loss_bits = std::min(ceil_log2_u64(sp / score.gp),
                               ceil_log2_u64(sq / score.gq));
  }
  return out;
}

static u64 inv_mod_u64(u64 a, u64 p) { return pow_u64(a, p - 2, p); }
static int rref_rank(std::vector<std::vector<u64>> a, u64 p) {
  if (a.empty()) return 0;
  int rows = static_cast<int>(a.size()), cols = static_cast<int>(a[0].size()), rank = 0;
  for (int col = 0; col < cols && rank < rows; ++col) {
    int pivot = rank;
    while (pivot < rows && a[pivot][col] == 0) ++pivot;
    if (pivot == rows) continue;
    std::swap(a[pivot], a[rank]);
    u64 inv = inv_mod_u64(a[rank][col], p);
    for (int j = col; j < cols; ++j) a[rank][j] = mul_u64(a[rank][j], inv, p);
    for (int i = 0; i < rows; ++i) if (i != rank && a[i][col] != 0) {
      u64 factor = a[i][col];
      for (int j = col; j < cols; ++j)
        a[i][j] = sub_mod_u64(a[i][j], mul_u64(factor, a[rank][j], p), p);
    }
    ++rank;
  }
  return rank;
}
static std::vector<std::vector<int>> ternary_nulls(const std::vector<std::vector<u64>>& a,
                                                   u64 p) {
  require(!a.empty() && a[0].size() <= 12, "ternary nullspace dimension cap");
  int cols = static_cast<int>(a[0].size());
  u64 total = 1;
  for (int i = 0; i < cols; ++i) total *= 3;
  std::vector<std::vector<int>> out;
  for (u64 code = 1; code < total; ++code) {
    u64 t = code;
    std::vector<int> v(cols);
    int first = 0;
    for (int j = 0; j < cols; ++j) {
      v[j] = int(t % 3) - 1;
      t /= 3;
      if (!first && v[j]) first = v[j];
    }
    if (first == 0) continue;
    if (first < 0) continue;
    bool zero = true;
    for (const auto& row : a) {
      u64 x = 0;
      for (int j = 0; j < cols; ++j) {
        if (v[j] == 1) x = add_mod_u64(x, row[j], p);
        else if (v[j] == -1) x = sub_mod_u64(x, row[j], p);
      }
      if (x != 0) { zero = false; break; }
    }
    if (zero) out.push_back(std::move(v));
  }
  return out;
}
static std::string mine_identities() {
  std::vector<std::vector<u64>> fricke, trace_cycle;
  std::vector<std::vector<u64>> assoc, cayley, determinant_product;
  for (int sample = 0; sample < 96; ++sample) {
    cpp_int N = cpp_int(1000003 + 2 * sample), N2 = N * N;
    cpp_int a = 1 + splitmix64(SYNTH_SEED + 17 * sample) % (N - 1).convert_to<u64>();
    cpp_int b = 1 + splitmix64(SYNTH_SEED + 19 * sample + 1) % (N - 1).convert_to<u64>();
    cpp_int c = 1 + splitmix64(SYNTH_SEED + 23 * sample + 2) % (N - 1).convert_to<u64>();
    cpp_int d = 1 + splitmix64(SYNTH_SEED + 29 * sample + 3) % (N - 1).convert_to<u64>();
    cpp_int e = 1 + splitmix64(SYNTH_SEED + 31 * sample + 4) % (N - 1).convert_to<u64>();
    M2 A = mul_m(upper(a, N2), lower(c, N2));
    M2 B = mul_m(lower(b, N2), upper(d, N2));
    M2 C = mul_m(upper(c, N2), lower(e, N2));
    M2 AB = mul_m(A, B), BA = mul_m(B, A);
    M2 comm = mul_m(mul_m(mul_m(A, B), adj_m(A)), adj_m(B));
    cpp_int x = trace_m(A), y = trace_m(B), z = trace_m(AB);
    std::array<cpp_int, 6> f{trace_m(comm), x*x, y*y, z*z, x*y*z, cpp_int(2)};
    std::vector<u64> fr;
    for (const auto& v : f) fr.push_back(mod_big_u64(v, FP1));
    fricke.push_back(std::move(fr));
    trace_cycle.push_back({mod_big_u64(trace_m(AB), FP1), mod_big_u64(trace_m(BA), FP1)});
    determinant_product.push_back(
        {mod_big_u64(det_m(AB), FP1), mod_big_u64(det_m(A) * det_m(B), FP1)});

    M2 u = canon_m(A, N), v = canon_m(B, N), w = canon_m(C, N);
    M2 zuv = canon_m(mul_m(u, v), N), zvw = canon_m(mul_m(v, w), N);
    M2 Kuv = section_carry(u, v, N), Kvw = section_carry(v, w, N);
    M2 Kleft = section_carry(zuv, w, N), Kright = section_carry(u, zvw, N);
    for (int q = 0; q < 4; ++q) {
      int row = q / 2, column = q % 2;
      assoc.push_back({
          mod_big_u64(Kleft[q], FP1),
          mod_big_u64(Kuv[2 * row] * w[column], FP1),
          mod_big_u64(Kuv[2 * row + 1] * w[2 + column], FP1),
          mod_big_u64(Kright[q], FP1),
          mod_big_u64(u[2 * row] * Kvw[column], FP1),
          mod_big_u64(u[2 * row + 1] * Kvw[2 + column], FP1)});
    }
    M2 aa = mul_m(AB, AB), tx = scalar_m(AB, trace_m(AB));
    for (int q = 0; q < 4; ++q)
      cayley.push_back({mod_big_u64(aa[q], FP1), mod_big_u64(tx[q], FP1),
                         mod_big_u64((q == 0 || q == 3) ? det_m(AB) : cpp_int(0), FP1)});
  }
  auto nf = ternary_nulls(fricke, FP1), nt = ternary_nulls(trace_cycle, FP1);
  auto na = ternary_nulls(assoc, FP1), nc = ternary_nulls(cayley, FP1);
  auto nd = ternary_nulls(determinant_product, FP1);
  require(nf.size() == 1, "unique ternary Fricke relation");
  require(nf[0] == std::vector<int>({1,-1,-1,-1,1,1}), "Fricke coefficients");
  require(nt.size() == 1 && nt[0] == std::vector<int>({1,-1}), "trace-cycle coefficients");
  require(na.size() == 1 &&
              na[0] == std::vector<int>({1,1,1,-1,-1,-1}),
          "six-summand associator coefficients");
  require(nc.size() == 1 && nc[0] == std::vector<int>({1,-1,1}), "Cayley coefficients");
  require(nd.size() == 1 && nd[0] == std::vector<int>({1,-1}),
          "determinant-product coefficients");
  int rank_f = rref_rank(fricke, FP1), rank_a = rref_rank(assoc, FP1);
  int rank_t = rref_rank(trace_cycle, FP1), rank_c = rref_rank(cayley, FP1);
  int rank_d = rref_rank(determinant_product, FP1);
  require(rank_f == 5 && rank_a == 5 && rank_t == 1 && rank_c == 2 &&
              rank_d == 1,
          "frozen modular ranks");

  for (int sample = 0; sample < 64; ++sample) {
    cpp_int N = cpp_int(2000003 + 2 * sample), N2 = N * N;
    cpp_int a = 1 + splitmix64(SYNTH_SEED ^ (31 * sample + 3)) % (N - 1).convert_to<u64>();
    cpp_int b = 1 + splitmix64(SYNTH_SEED ^ (37 * sample + 5)) % (N - 1).convert_to<u64>();
    cpp_int c = 1 + splitmix64(SYNTH_SEED ^ (41 * sample + 7)) % (N - 1).convert_to<u64>();
    M2 A = upper(a, N2), B = lower(b, N2), C = upper(c, N2);
    cpp_int fq = fricke_quotient(A, B, N);
    (void)fq;
    M2 u = canon_m(A, N), v = canon_m(B, N), w = canon_m(C, N);
    M2 zuv = canon_m(mul_m(u, v), N), zvw = canon_m(mul_m(v, w), N);
    M2 full = sub_m(add_m(section_carry(zuv, w, N), mul_m(section_carry(u,v,N), w)),
                    add_m(section_carry(u, zvw, N), mul_m(u, section_carry(v,w,N))));
    require(equal_m(full, M2{}), "heldback exact associator");
    M2 AB = mul_mod_m(A, B, N2);
    (void)cayley_quotient(AB, N);
    require((trace_m(AB) - trace_m(mul_mod_m(B, A, N2))) % N2 == 0,
            "heldback trace cycle");
    require((det_m(AB) - det_m(A) * det_m(B)) % N2 == 0,
            "heldback determinant product");
  }
  std::ostringstream out;
  out << "discovery=96 heldback=64 fricke_rank=" << rank_f
      << "/6 assoc_rank=" << rank_a << "/6 trace_rank="
      << rank_t << "/2 cayley_rank="
      << rank_c << "/3 determinant_rank="
      << rank_d
      << "/2 ternary_nulls=1,1,1,1,1";
  return out.str();
}

struct InputResult {
  Task task{};
  cpp_int N;
  std::array<u64, FAMILY_COUNT> atoms{}, zeros{}, units{}, n_powers{}, hits{};
  std::array<u64, DECOY_COUNT> decoy_counts{};
  u64 cleanup = 0, source_gcd_hits = 0, decoys = 0;
  u64 noncommutative_profiles = 0;
  u64 atom_hash = 0, candidate_hash = 0;
  std::array<u64, 5> basis_original_count{}, basis_conjugate_count{};
  std::array<u64, 5> basis_original_hash{}, basis_conjugate_hash{};
  std::size_t candidate_hits = 0;
  std::vector<int> candidate_hit_ids;
  OrderStats order;
  std::vector<ResidualPair> residuals;
  std::string first;
};
static InputResult process_input(const Task& task, const std::vector<Candidate>& candidates,
                                 bool score_labels) {
  cpp_int N = cpp_int(task.p) * task.q;
  PublicResult public_result = process_public(N, candidates);
  InputResult out;
  out.task = task;
  out.N = N;
  out.atoms = public_result.state.atoms;
  out.zeros = public_result.state.zeros;
  out.units = public_result.state.units;
  out.n_powers = public_result.state.n_powers;
  out.hits = public_result.state.hits;
  out.decoy_counts = public_result.state.decoy_counts;
  out.cleanup = public_result.state.cleanup_hits;
  out.source_gcd_hits = public_result.state.source_gcd_hits;
  out.decoys = public_result.state.decoy_zeros;
  out.noncommutative_profiles = public_result.state.noncommutative_profiles;
  out.atom_hash = public_result.state.atom_hash;
  out.candidate_hash = public_result.candidate_hash;
  out.basis_original_count = public_result.state.basis_original_count;
  out.basis_conjugate_count = public_result.state.basis_conjugate_count;
  out.basis_original_hash = public_result.state.basis_original_hash;
  out.basis_conjugate_hash = public_result.state.basis_conjugate_hash;
  out.candidate_hits = public_result.candidate_hits.size();
  out.candidate_hit_ids.reserve(public_result.candidate_hits.size());
  for (const auto& hit : public_result.candidate_hits) out.candidate_hit_ids.push_back(hit.first);
  out.order = public_result.order;
  out.first = public_result.state.first_factor;
  if (score_labels) out.residuals = score_p205(public_result.state, task.p, task.q);
  return out;
}

static void self_test(const std::vector<Candidate>& candidates) {
  require(is_prime(61) && is_prime(71) && !is_prime(4331), "primality self-test");
  require(candidates.size() > 11000, "large symbolic candidate count");
  require(primitive_n(45, 15) == 3 && gcd_big(45, 15) == 15 &&
              gcd_big(primitive_n(45, 15), 15) == 3,
          "N-primitive gcd-change witness");
  FamilyState unit_state(15);
  unit_state.atom(0, -1, "unit-test");
  require(unit_state.units[0] == 1 && unit_state.sum[0] == 14 &&
              unit_state.product[0] == 14 &&
              unit_state.exact_atoms[0] == std::vector<cpp_int>({-1}),
          "units remain in synthesized sums and products");
  auto pair_scope = public_pairs(32, 64, cpp_int(4331), 0, 0x2a17c011ULL);
  auto triple_scope = public_triples(32, 64, cpp_int(4331), 0, 0x7a1a550cULL);
  require(std::set<std::pair<int, int>>(pair_scope.begin(), pair_scope.end()).size() ==
              pair_scope.size(),
          "collision-free pair scope");
  require(std::set<std::array<int, 3>>(triple_scope.begin(), triple_scope.end()).size() ==
              triple_scope.size(),
          "collision-free triple scope");
  std::set<std::string> names, schemas;
  for (int f = 0; f < FAMILY_COUNT; ++f) {
    require(names.insert(FAMILY_NAMES[f]).second, "unique family name");
    require(schemas.insert(FAMILY_SCHEMAS[f]).second, "unique family schema");
  }
  std::string identities = mine_identities();
  Task task{7, 0, 0, 61, 71};
  InputResult result = process_input(task, candidates, true);
  u64 atoms = std::accumulate(result.atoms.begin(), result.atoms.end(), u64(0));
  require(atoms > 80000, "large static atom count");
  require(result.residuals.size() == 467, "P205 self-test words");
  for (const auto& residual : result.residuals)
    require(residual.improvement_p >= 1 && residual.improvement_q >= 1,
            "exact P205 improvement multipliers");
  require(result.order.trials == 36, "order trial count");
  require(result.order.root_proposals_checked ==
              u64(result.order.trials) * ROOT_PROPOSAL_COUNT,
          "all root proposals checked in every order trial");
  for (u64 count : result.order.root_index_checks)
    require(count == result.order.trials,
            "each root index checked in every order trial");
  require(result.atoms[9] == 2ULL * 4372 * 3,
          "three frozen step-minor pairs");
  require(result.atoms[29] == 2ULL * 4372 * 5,
          "five conjugation-difference types");
  for (int feature = 0; feature < 5; ++feature)
    require(result.basis_original_count[feature] == 2ULL * 4372 * 4 &&
                result.basis_conjugate_count[feature] ==
                    result.basis_original_count[feature],
            "both conjugate bases reported by type");
  require(result.noncommutative_profiles == 2,
          "genuinely noncommutative profiles");
  for (int kind = 0; kind < DECOY_COUNT; ++kind)
    require(result.decoy_counts[kind] > 0,
            std::string("named decoy count: ") + DECOY_NAMES[kind]);
  std::cout << "SELF_TEST_PASS N=4331 families=" << FAMILY_COUNT
            << " candidates=" << candidates.size() << " atoms=" << atoms
            << " decoys=" << result.decoys << " order_trials=" << result.order.trials
            << " root_checks=" << result.order.root_proposals_checked
            << " root_index_checks=36x14"
            << " identities={" << identities << "}\n";
}

struct CandidateAggregate {
  u64 discovery_tested = 0, heldout_tested = 0;
  u64 discovery_hits = 0, heldout_hits = 0;
  u64 discovery_safe_hits = 0, heldout_safe_hits = 0;
  u64 discovery_size_mask = 0, heldout_size_mask = 0;
};
struct P205Cell {
  int bits = 0, cohort = 0, word = 0;
  u64 count = 0, improved = 0, saturated = 0;
  int median_loss = 0, baseline_median_loss = 0;
};
static int lower_median(std::vector<int> values) {
  require(!values.empty(), "nonempty median");
  std::sort(values.begin(), values.end());
  return values[(values.size() - 1) / 2];
}

int main(int argc, char** argv) try {
  std::vector<Candidate> candidates = build_candidates();
  if (argc == 2 && std::string(argv[1]) == "--describe") {
    u64 aliases = 0;
    for (const auto& c : candidates) aliases += c.aliases - 1;
    std::cout << "F264_D03_DESCRIPTION families=" << FAMILY_COUNT
              << " candidates=" << candidates.size() << " aliases=" << aliases
              << " words_per_input=8744 p205_words=467 planned_inputs=5280"
              << " discovery_inputs=2208 heldout_inputs=3072 tsv_columns=2560"
              << " max_threads=8\n";
    return 0;
  }
  if (argc == 2 && std::string(argv[1]) == "--self-test") {
    self_test(candidates);
    return 0;
  }
  if (argc == 2 && std::string(argv[1]) == "--benchmark") {
    std::string identities = mine_identities();
    Rng rng(SYNTH_SEED ^ 0xbec4f264ULL);
    double total = 0;
    u64 atoms = 0, order_trials = 0;
    for (int rep = 0; rep < 1; ++rep) {
      u64 p = random_prime(60, rng), q = random_prime(60, rng);
      if (p > q) std::swap(p, q);
      if (p == q || q >= 2 * p) { --rep; continue; }
      auto start = std::chrono::steady_clock::now();
      InputResult r = process_input({60, 0, rep, p, q}, candidates, true);
      total += std::chrono::duration<double>(std::chrono::steady_clock::now() - start).count();
      atoms += std::accumulate(r.atoms.begin(), r.atoms.end(), u64(0));
      order_trials += r.order.trials;
    }
    double mean = total;
    double projection = mean * 5280.0 / 8.0 * 1.75;
    u64 predicted_output_bytes = 5280ULL * 65536ULL +
                                 u64(candidates.size()) * 4096ULL +
                                 64ULL * 1024 * 1024;
    std::cout << std::fixed << std::setprecision(6)
              << "BENCHMARK_PASS repetitions=1 mean_full_60bit_input_seconds=" << mean
              << " static_atoms=" << atoms << " candidates=" << candidates.size()
              << " order_trials=" << order_trials
              << " projected_8thread_seconds_1.75x=" << projection
              << " projected_peak_mib=1024 predicted_output_bytes="
              << predicted_output_bytes << " identities={"
              << identities << "}\n";
    return 0;
  }
  require(argc == 6,
          "usage: V3_symbolic_search THREADS SPLIT OUT_JSON OUT_TSV OUT_ANOMALIES");
  int thread_count = std::stoi(argv[1]);
  require(thread_count >= 1 && thread_count <= 8, "threads 1..8");
  std::string split = argv[2];
  require(split == "discovery" || split == "heldout", "production split");
  std::string identities = mine_identities();
  std::vector<CohortBuild> cohort_builds;
  std::vector<Task> tasks = make_tasks(split, cohort_builds);
  std::vector<InputResult> results(tasks.size());
  std::atomic<std::size_t> next{0}, done{0};
  std::mutex io;
  auto start = std::chrono::steady_clock::now();
  auto worker = [&]() {
    for (;;) {
      std::size_t index = next.fetch_add(1);
      if (index >= tasks.size()) return;
      results[index] = process_input(tasks[index], candidates, true);
      std::size_t finished = done.fetch_add(1) + 1;
      if (finished % 32 == 0 || finished == tasks.size()) {
        std::lock_guard<std::mutex> lock(io);
        double seconds = std::chrono::duration<double>(std::chrono::steady_clock::now() - start).count();
        std::cerr << "progress=" << finished << "/" << tasks.size()
                  << " elapsed=" << std::fixed << std::setprecision(1) << seconds
                  << "s rate=" << finished / seconds << "/s\n";
      }
    }
  };
  std::vector<std::thread> pool;
  for (int i = 0; i < thread_count; ++i) pool.emplace_back(worker);
  for (auto& t : pool) t.join();
  double elapsed = std::chrono::duration<double>(std::chrono::steady_clock::now() - start).count();

  std::ofstream tsv(argv[4]);
  require(bool(tsv), "open rows TSV");
  tsv << "factor_bits\tsplit\tcohort\tindex\tp\tq\tN\tcleanup\tsource_gcd_hits"
         "\tnoncommutative_profiles\tdecoys\tatom_hash\tcandidate_hits"
         "\tcandidate_hash\torder_trials\torder_gcd_hits\torder_initial_returns"
         "\torder_split_returns\tcertified_blocks\tnoncyclic_blocks\tcertified_lcm"
         "\tcertified_lcm_bits\tcertified_new_bits\tcyclic_lcm\tcyclic_lcm_bits"
         "\troot_proposals_checked\troot_square_matches\troot_unit_matches"
         "\troot_proper_matches\troot_transcript_hash\tfirst_certificate";
  for (int root = 0; root < ROOT_PROPOSAL_COUNT; ++root)
    tsv << "\troot_proposal_" << root << "_checks";
  for (int feature = 0; feature < 5; ++feature)
    tsv << "\tbasis_original_" << BASIS_FEATURE_NAMES[feature]
        << "_count\tbasis_original_" << BASIS_FEATURE_NAMES[feature]
        << "_hash\tbasis_conjugate_" << BASIS_FEATURE_NAMES[feature]
        << "_count\tbasis_conjugate_" << BASIS_FEATURE_NAMES[feature] << "_hash";
  for (int d = 0; d < DECOY_COUNT; ++d)
    tsv << '\t' << DECOY_NAMES[d] << "_zeros";
  for (int f = 0; f < FAMILY_COUNT; ++f)
    tsv << '\t' << FAMILY_NAMES[f] << "_atoms\t" << FAMILY_NAMES[f]
        << "_zeros\t" << FAMILY_NAMES[f] << "_units\t" << FAMILY_NAMES[f]
        << "_N_powers\t" << FAMILY_NAMES[f] << "_hits";
  for (int w = 0; w < 467; ++w)
    tsv << "\tW" << w << "_gp\tW" << w << "_gq\tW" << w
        << "_loss_bits\tW" << w << "_improvement_p\tW" << w
        << "_improvement_q";
  tsv << '\n';
  for (const auto& r : results) {
    tsv << r.task.bits << '\t' << (r.task.bits <= 32 ? "discovery" : "heldout")
        << '\t' << cohort_name(r.task.cohort) << '\t' << r.task.index << '\t'
        << r.task.p << '\t' << r.task.q << '\t' << r.N << '\t' << r.cleanup
        << '\t' << r.source_gcd_hits << '\t' << r.noncommutative_profiles
        << '\t' << r.decoys << '\t' << r.atom_hash << '\t' << r.candidate_hits
        << '\t' << r.candidate_hash << '\t' << r.order.trials << '\t'
        << r.order.gcd_hits << '\t' << r.order.initial_returns << '\t'
        << r.order.split_returns << '\t' << r.order.certified_blocks << '\t'
        << r.order.noncyclic_blocks << '\t' << r.order.lcm << '\t'
        << bit_length(r.order.lcm) << '\t'
        << std::max(0, bit_length(r.order.lcm) - 1) << '\t'
        << r.order.cyclic_lcm << '\t' << bit_length(r.order.cyclic_lcm) << '\t'
        << r.order.root_proposals_checked << '\t'
        << r.order.root_square_matches << '\t' << r.order.root_unit_matches << '\t'
        << r.order.root_proper_matches << '\t' << r.order.root_transcript_hash << '\t'
        << r.first;
    for (u64 count : r.order.root_index_checks) tsv << '\t' << count;
    for (int feature = 0; feature < 5; ++feature)
      tsv << '\t' << r.basis_original_count[feature] << '\t'
          << r.basis_original_hash[feature] << '\t'
          << r.basis_conjugate_count[feature] << '\t'
          << r.basis_conjugate_hash[feature];
    for (int d = 0; d < DECOY_COUNT; ++d) tsv << '\t' << r.decoy_counts[d];
    for (int f = 0; f < FAMILY_COUNT; ++f)
      tsv << '\t' << r.atoms[f] << '\t' << r.zeros[f] << '\t' << r.units[f]
          << '\t' << r.n_powers[f] << '\t' << r.hits[f];
    for (const auto& residual : r.residuals)
      tsv << '\t' << residual.gp << '\t' << residual.gq << '\t'
          << residual.loss_bits << '\t' << residual.improvement_p << '\t'
          << residual.improvement_q;
    tsv << '\n';
  }
  tsv.close();

  std::ofstream anomaly(argv[5]);
  require(bool(anomaly), "open anomaly TSV");
  anomaly << "factor_bits\tsplit\tcohort\tindex\ttype\tdetail\n";
  for (const auto& r : results) {
    if (!r.first.empty()) anomaly << r.task.bits << '\t'
      << (r.task.bits <= 32 ? "discovery" : "heldout") << '\t'
      << cohort_name(r.task.cohort) << '\t' << r.task.index
      << "\tfactor\t" << r.first << '\n';
    if (r.order.noncyclic_blocks)
      anomaly << r.task.bits << '\t' << (r.task.bits <= 32 ? "discovery" : "heldout")
              << '\t' << cohort_name(r.task.cohort) << '\t' << r.task.index
              << "\tcommon_order\tlcm=" << r.order.lcm
              << ";new_bits=" << std::max(0, bit_length(r.order.lcm) - 1) << '\n';
    std::size_t cap = std::min<std::size_t>(256, r.candidate_hit_ids.size());
    for (std::size_t j = 0; j < cap; ++j) {
      int id = r.candidate_hit_ids[j];
      anomaly << r.task.bits << '\t' << (r.task.bits <= 32 ? "discovery" : "heldout")
              << '\t' << cohort_name(r.task.cohort) << '\t' << r.task.index
              << "\tcandidate_gcd\tid=" << id << ";syntax=" << candidates[id].syntax << '\n';
    }
  }
  anomaly.close();

  std::vector<CandidateAggregate> candidate_agg(candidates.size());
  std::array<u64, FAMILY_COUNT> family_heldout_hits{}, family_heldout_safe_hits{},
      family_heldout_size_mask{};
  u64 order_rows = 0, order_safe_rows = 0, order_size_mask = 0;
  u64 root_proposals_checked = 0, root_square_matches = 0;
  u64 root_unit_matches = 0, root_proper_matches = 0;
  u64 root_transcript_hash = 0;
  std::array<u64, ROOT_PROPOSAL_COUNT> root_index_checks{};
  cpp_int order_global_lcm = 1;
  for (const auto& r : results) {
    root_proposals_checked += r.order.root_proposals_checked;
    root_square_matches += r.order.root_square_matches;
    root_unit_matches += r.order.root_unit_matches;
    root_proper_matches += r.order.root_proper_matches;
    root_transcript_hash = splitmix64(root_transcript_hash ^
                                      r.order.root_transcript_hash);
    for (int root = 0; root < ROOT_PROPOSAL_COUNT; ++root)
      root_index_checks[root] += r.order.root_index_checks[root];
    bool discovery = r.task.bits <= 32, safe = r.task.cohort == 2;
    if (!discovery) {
      for (int f = 0; f < FAMILY_COUNT; ++f)
        if (r.hits[f] != 0) {
          ++family_heldout_hits[f];
          family_heldout_size_mask[f] |= 1ULL << r.task.bits;
          if (safe) ++family_heldout_safe_hits[f];
        }
      if (r.order.noncyclic_blocks != 0 && r.order.lcm > 1) {
        ++order_rows;
        order_size_mask |= 1ULL << r.task.bits;
        if (safe) ++order_safe_rows;
        order_global_lcm = lcm_big(order_global_lcm, r.order.lcm);
      }
    }
    for (auto& a : candidate_agg) {
      if (discovery) ++a.discovery_tested;
      else ++a.heldout_tested;
    }
    for (int id : r.candidate_hit_ids) {
      auto& a = candidate_agg[id];
      if (discovery) {
        ++a.discovery_hits;
        if (safe) ++a.discovery_safe_hits;
        a.discovery_size_mask |= 1ULL << r.task.bits;
      } else {
        ++a.heldout_hits;
        if (safe) ++a.heldout_safe_hits;
        a.heldout_size_mask |= 1ULL << r.task.bits;
      }
    }
  }

  std::map<std::tuple<int, int, int>, P205Cell> p205_cells;
  for (int bits : FACTOR_BITS) {
    if ((split == "discovery") != (bits <= 32)) continue;
    for (int cohort = 0; cohort < 3; ++cohort)
      for (int word = 0; word < 467; ++word) {
        std::vector<int> losses;
        u64 improved = 0, saturated = 0;
        for (const auto& r : results) {
          if (r.task.bits != bits || r.task.cohort != cohort) continue;
          const auto& score = r.residuals[word];
          losses.push_back(score.loss_bits);
          improved += score.improvement_p > 1 || score.improvement_q > 1;
          u64 d = gcd_u64(r.task.p - 1, r.task.q - 1);
          u64 sp = (r.task.p - 1) / d, sq = (r.task.q - 1) / d;
          saturated += score.gp == sp || score.gq == sq;
        }
        P205Cell cell{bits, cohort, word, static_cast<u64>(losses.size()),
                      improved, saturated, lower_median(std::move(losses)), 0};
        p205_cells.emplace(std::make_tuple(bits, cohort, word), cell);
      }
  }
  for (auto& entry : p205_cells) {
    auto& cell = entry.second;
    cell.baseline_median_loss =
        p205_cells.at(std::make_tuple(cell.bits, cell.cohort, 0)).median_loss;
  }
  std::array<bool, 467> p205_finite_lead{};
  if (split == "heldout") {
    for (int word = 0; word < 467; ++word) {
      bool margin = true;
      for (int bits : {40, 48, 56, 60})
        for (int cohort : {0, 2}) {
          const auto& cell = p205_cells.at(std::make_tuple(bits, cohort, word));
          if (cell.median_loss + 2 > cell.baseline_median_loss) margin = false;
        }
      int safe_growth =
          p205_cells.at(std::make_tuple(60, 2, word)).median_loss -
          p205_cells.at(std::make_tuple(40, 2, word)).median_loss;
      int random_growth =
          p205_cells.at(std::make_tuple(60, 0, word)).median_loss -
          p205_cells.at(std::make_tuple(40, 0, word)).median_loss;
      p205_finite_lead[word] = margin && safe_growth <= 16 && random_growth <= 16;
    }
  }

  std::ofstream json(argv[3]);
  require(bool(json), "open summary JSON");
  u64 aliases = 0;
  for (const auto& c : candidates) aliases += c.aliases - 1;
  json << "{\n  \"experiment\": \"F264-D03\",\n  \"split\": \"" << split
       << "\",\n  \"inputs\": " << results.size()
       << ",\n  \"threads\": " << thread_count << ",\n  \"elapsed_seconds\": "
       << std::setprecision(12) << elapsed << ",\n  \"families\": " << FAMILY_COUNT
       << ",\n  \"candidates\": " << candidates.size() << ",\n  \"candidate_aliases\": "
       << aliases << ",\n  \"identity_mining\": \"" << identities << "\",\n"
          "  \"selection_uses_hidden_labels\": false,\n"
          "  \"executes_factor_bank\": false,\n"
          "  \"cohort_builds\": [\n";
  for (std::size_t i = 0; i < cohort_builds.size(); ++i) {
    if (i) json << ",\n";
    const auto& build = cohort_builds[i];
    json << "    {\"factor_bits\": " << build.bits << ", \"cohort\": \""
         << cohort_name(build.cohort) << "\", \"attempts\": " << build.attempts
         << ", \"accepted\": " << build.accepted << "}";
  }
  json << "\n  ],\n  \"decoy_summaries\": [\n";
  for (int d = 0; d < DECOY_COUNT; ++d) {
    if (d) json << ",\n";
    u64 count = 0;
    for (const auto& r : results) count += r.decoy_counts[d];
    json << "    {\"decoy\": \"" << DECOY_NAMES[d]
         << "\", \"exact_zero_count\": " << count << "}";
  }
  json << "\n  ],\n  \"family_summaries\": [\n";
  bool first_family = true;
  for (int bits : FACTOR_BITS) {
    if ((split == "discovery") != (bits <= 32)) continue;
    for (int cohort = 0; cohort < 3; ++cohort)
      for (int family = 0; family < FAMILY_COUNT; ++family) {
        u64 count = 0, atoms = 0, zeros = 0, units = 0, n_powers = 0,
            hit_events = 0, hit_inputs = 0;
        for (const auto& r : results) {
          if (r.task.bits != bits || r.task.cohort != cohort) continue;
          ++count;
          atoms += r.atoms[family];
          zeros += r.zeros[family];
          units += r.units[family];
          n_powers += r.n_powers[family];
          hit_events += r.hits[family];
          hit_inputs += r.hits[family] != 0;
        }
        if (!first_family) json << ",\n";
        first_family = false;
        json << "    {\"factor_bits\": " << bits << ", \"cohort\": \""
             << cohort_name(cohort) << "\", \"family\": \""
             << FAMILY_NAMES[family] << "\", \"count\": " << count
             << ", \"atoms\": " << atoms << ", \"zeros\": " << zeros
             << ", \"units\": " << units << ", \"N_powers\": " << n_powers
             << ", \"proper_gcd_events\": " << hit_events
             << ", \"proper_gcd_inputs\": " << hit_inputs << "}";
      }
  }
  json << "\n  ],\n  \"direct_family_leads\": [\n";
  for (int family = 0; family < FAMILY_COUNT; ++family) {
    if (family) json << ",\n";
    bool lead = split == "heldout" && family_heldout_hits[family] >= 16 &&
                __builtin_popcountll(family_heldout_size_mask[family]) >= 3 &&
                family_heldout_safe_hits[family] > 0;
    json << "    {\"family\": \"" << FAMILY_NAMES[family]
         << "\", \"heldout_hit_inputs\": " << family_heldout_hits[family]
         << ", \"heldout_safe_hit_inputs\": " << family_heldout_safe_hits[family]
         << ", \"heldout_size_mask\": " << family_heldout_size_mask[family]
         << ", \"finite_lead\": " << (lead ? "true" : "false") << "}";
  }
  bool order_lead = split == "heldout" && order_rows >= 16 &&
                    __builtin_popcountll(order_size_mask) >= 3 &&
                    order_safe_rows > 0;
  json << "\n  ],\n  \"order_summary\": {\"heldout_noncyclic_rows\": "
       << order_rows << ", \"heldout_safe_rows\": " << order_safe_rows
       << ", \"heldout_size_mask\": " << order_size_mask
       << ", \"accumulated_exact_lcm\": \"" << order_global_lcm
       << "\", \"new_bits\": " << std::max(0, bit_length(order_global_lcm) - 1)
       << ", \"root_proposals_checked\": " << root_proposals_checked
       << ", \"root_square_matches\": " << root_square_matches
       << ", \"root_unit_matches\": " << root_unit_matches
       << ", \"root_proper_matches\": " << root_proper_matches
       << ", \"root_transcript_hash\": " << root_transcript_hash
       << ", \"root_index_checks\": [";
  for (int root = 0; root < ROOT_PROPOSAL_COUNT; ++root) {
    if (root) json << ", ";
    json << root_index_checks[root];
  }
  json << "]"
       << ", \"finite_lead\": " << (order_lead ? "true" : "false")
       << "},\n  \"p205_score\": \"min(ceil_log2(sp/gp),ceil_log2(sq/gq))\",\n"
          "  \"p205_summaries\": [\n";
  bool first_p205 = true;
  for (const auto& entry : p205_cells) {
    const auto& cell = entry.second;
    if (!first_p205) json << ",\n";
    first_p205 = false;
    json << "    {\"factor_bits\": " << cell.bits << ", \"cohort\": \""
         << cohort_name(cell.cohort) << "\", \"word\": " << cell.word
         << ", \"count\": " << cell.count << ", \"median_loss_bits\": "
         << cell.median_loss << ", \"baseline_median_loss_bits\": "
         << cell.baseline_median_loss << ", \"improved_inputs\": "
         << cell.improved << ", \"saturated_inputs\": " << cell.saturated << "}";
  }
  json << "\n  ],\n  \"p205_finite_leads\": [";
  bool first_lead = true;
  for (int word = 0; word < 467; ++word)
    if (p205_finite_lead[word]) {
      if (!first_lead) json << ", ";
      first_lead = false;
      json << word;
    }
  json << "],\n  \"candidate_summary\": [\n";
  for (std::size_t i = 0; i < candidates.size(); ++i) {
    if (i) json << ",\n";
    const auto& a = candidate_agg[i];
    u64 tested = split == "discovery" ? a.discovery_tested : a.heldout_tested;
    u64 hits = split == "discovery" ? a.discovery_hits : a.heldout_hits;
    u64 safe_hits = split == "discovery" ? a.discovery_safe_hits : a.heldout_safe_hits;
    u64 size_mask = split == "discovery" ? a.discovery_size_mask : a.heldout_size_mask;
    bool lead = split == "heldout" && hits >= 16 &&
                __builtin_popcountll(size_mask) >= 3 && safe_hits > 0;
    json << "    {\"id\": " << i << ", \"syntax\": \"" << candidates[i].syntax
         << "\", \"aliases\": " << candidates[i].aliases
         << ", \"tested\": " << tested << ", \"proper_gcd_hits\": " << hits
         << ", \"safe_hits\": " << safe_hits << ", \"size_mask\": "
         << size_mask << ", \"finite_lead\": " << (lead ? "true" : "false")
         << "}";
  }
  json << "\n  ]\n}\n";
  json.close();
  require(bool(json), "write summary JSON");
  std::cout << "F264_D03_PASS split=" << split << " inputs=" << results.size()
            << " candidates="
            << candidates.size() << " elapsed_seconds=" << std::fixed
            << std::setprecision(3) << elapsed << " identities={" << identities << "}\n";
  return 0;
} catch (const std::exception& e) {
  std::cerr << "F264_D03_FAIL " << e.what() << "\n";
  return 1;
}
