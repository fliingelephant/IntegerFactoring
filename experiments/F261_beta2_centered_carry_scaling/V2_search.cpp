#include <algorithm>
#include <array>
#include <atomic>
#include <chrono>
#include <cmath>
#include <cstdint>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <limits>
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
#include <utility>
#include <vector>

#include <boost/multiprecision/cpp_int.hpp>

using boost::multiprecision::cpp_int;
using u64 = std::uint64_t;
using u128 = __uint128_t;
using s128 = __int128_t;

static constexpr int FACTOR_BITS[] =
    {16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60};
static constexpr int COHORT_COUNT = 4;
static constexpr int PREFIX_COUNT = 4;
static constexpr int PREDICTOR_COUNT = 9;
static constexpr u64 U3_HARD_CAP = 1ULL << 20;
static constexpr bool EXECUTES_FACTOR_BANK = false;
static constexpr double PARALLEL_EFFICIENCY = 0.75;
static constexpr double MAX_PROJECTED_SECONDS = 14400.0;
static constexpr const char* EXPERIMENT_NAME = "F261-D02";
static constexpr const char* ORACLE_HIT_SEMANTICS =
    "hidden_label_true_carry_not_executed_factor_bank";
static constexpr const char* ORACLE_HIT_COLUMNS =
    "\toracle_hit_n\toracle_hit_n2\toracle_hit_n3\toracle_hit_cqp";
static constexpr u64 RANDOM_ATTEMPT_CAP = 20000000ULL;
static constexpr u64 CLOSE_ATTEMPT_CAP = 50000000ULL;
static constexpr u64 EDGE_ATTEMPT_CAP = 20000000ULL;
static constexpr u64 SAFE_ATTEMPT_CAP = 200000000ULL;

static const char* COHORT_NAMES[] = {"random", "close", "edge", "safe"};
static const int COHORT_SIZES[] = {64, 24, 24, 2};
static const u64 COHORT_TAGS[] = {
    0x52414e445f463236ULL, 0x434c4f5345463236ULL,
    0x454447455f463236ULL, 0x534146455f463236ULL};
static const u64 ATTEMPT_CAPS[] = {
    RANDOM_ATTEMPT_CAP, CLOSE_ATTEMPT_CAP, EDGE_ATTEMPT_CAP, SAFE_ATTEMPT_CAP};
static const char* PREFIX_NAMES[] = {"none", "eighth", "three8", "quarter"};
static const char* PREDICTOR_NAMES[] = {
    "first", "hash", "prefix_linf", "prefix_l1", "prefix_product",
    "sqrt_distance", "H_distance", "product_surrogate", "cf"};

[[noreturn]] static void fail(const std::string& message) {
  throw std::runtime_error(message);
}

static void require(bool condition, const std::string& message) {
  if (!condition) fail(message);
}

static u64 splitmix64(u64 x) {
  x += 0x9e3779b97f4a7c15ULL;
  x = (x ^ (x >> 30)) * 0xbf58476d1ce4e5b9ULL;
  x = (x ^ (x >> 27)) * 0x94d049bb133111ebULL;
  return x ^ (x >> 31);
}

static std::string string_u128(u128 x) {
  if (x == 0) return "0";
  std::string s;
  while (x) {
    s.push_back(static_cast<char>('0' + x % 10));
    x /= 10;
  }
  std::reverse(s.begin(), s.end());
  return s;
}

static std::string string_s128(s128 x) {
  if (x >= 0) return string_u128(static_cast<u128>(x));
  return "-" + string_u128(static_cast<u128>(-(x + 1)) + 1);
}

static u128 abs128(s128 x) {
  return x >= 0 ? static_cast<u128>(x) : static_cast<u128>(-(x + 1)) + 1;
}

static int bit_length(u128 x) {
  require(x > 0, "positive bit length");
  int bits = 0;
  while (x) {
    ++bits;
    x >>= 1;
  }
  return bits;
}

static u64 isqrt128(u128 x) {
  if (x == 0) return 0;
  const int rb = (bit_length(x) + 1) / 2;
  u64 r = 0;
  for (int j = rb - 1; j >= 0; --j) {
    const u64 candidate = r | (1ULL << j);
    if (static_cast<u128>(candidate) * candidate <= x) r = candidate;
  }
  return r;
}

static u64 mul_mod(u64 a, u64 b, u64 m) {
  return m == 1 ? 0 : static_cast<u64>((static_cast<u128>(a) * b) % m);
}

static u64 pow_mod(u64 a, u64 e, u64 m) {
  if (m == 1) return 0;
  u64 result = 1 % m;
  while (e) {
    if (e & 1) result = mul_mod(result, a, m);
    a = mul_mod(a, a, m);
    e >>= 1;
  }
  return result;
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
    bool composite = true;
    for (u64 r = 1; r < s; ++r) {
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

static bool is_safe_prime(u64 p) {
  return is_prime(p) && is_prime((p - 1) / 2);
}

static u64 inverse_power_two(u64 a, u64 B) {
  require((a & 1) && B && (B & (B - 1)) == 0, "inverse power-two input");
  u64 x = a;
  for (int i = 0; i < 6; ++i) x *= 2 - a * x;
  return x & (B - 1);
}

struct PrefixData {
  u64 a;
  u64 b;
};

static PrefixData prefix_data(u128 N, u64 p, u64 R,
                              bool* inverse_branch = nullptr) {
  if (inverse_branch) *inverse_branch = false;
  if (R == 1) return {0, 0};
  if (inverse_branch) *inverse_branch = true;
  const u64 a = p & (R - 1);
  return {a, mul_mod(static_cast<u64>(N % R), inverse_power_two(a, R), R)};
}

static s128 floor_div(s128 a, s128 b) {
  require(b > 0, "positive divisor");
  s128 q = a / b, r = a % b;
  if (r < 0) --q;
  return q;
}

static s128 ceil_div(s128 a, s128 b) {
  return -floor_div(-a, b);
}

static s128 centered_mod(u128 value, u64 modulus) {
  if (modulus == 1) return 0;
  const u64 r = static_cast<u64>(value % modulus);
  return r >= modulus / 2 ? static_cast<s128>(r) - modulus : r;
}

static u64 rounded_center(u128 value, u64 B) {
  return static_cast<u64>((value + B / 2) / B);
}

struct CarryPoint {
  u64 kp;
  u64 kq;
  s128 x;
  s128 y;
  s128 c;
  u128 T;
  bool tie_p;
  bool tie_q;
};

static CarryPoint carry_point(u64 p, u64 q, u128 N, u64 B, u64 H, u64 u) {
  const u128 up = static_cast<u128>(u) * p;
  const u128 uq = static_cast<u128>(u) * q;
  const u64 kp = rounded_center(up, B);
  const u64 kq = rounded_center(uq, B);
  const s128 x = static_cast<s128>(up) - static_cast<s128>(kp) * B;
  const s128 y = static_cast<s128>(uq) - static_cast<s128>(kq) * B;
  require(-static_cast<s128>(B / 2) <= x && x < static_cast<s128>(B / 2),
          "p centered range");
  require(-static_cast<s128>(B / 2) <= y && y < static_cast<s128>(B / 2),
          "q centered range");
  const s128 numerator = x * y - static_cast<s128>(u) * u;
  require(numerator % static_cast<s128>(B) == 0, "carry integrality");
  const s128 c = numerator / static_cast<s128>(B);
  const u128 A = static_cast<u128>(u) * u * H
                 + static_cast<u128>(kp) * kq * B;
  require(static_cast<s128>(A) - c >= 0, "positive trace numerator");
  require((static_cast<s128>(A) - c) % u == 0, "trace division");
  const u128 T = static_cast<u128>((static_cast<s128>(A) - c) / u);
  require(T == static_cast<u128>(kp) * q + static_cast<u128>(kq) * p,
          "weighted trace identity");
  require(N == static_cast<u128>(p) * q, "N label identity");
  return {kp, kq, x, y, c, T,
          static_cast<u64>(up % B) == B / 2,
          static_cast<u64>(uq % B) == B / 2};
}

struct Task {
  int factor_bits;
  int cohort;
  int index;
  u64 attempts;
  u64 p;
  u64 q;
};

static u64 candidate_p(int factor_bits, int cohort, u64 serial, u64 tag) {
  const u64 low = 1ULL << (factor_bits - 1);
  const u64 high = (1ULL << factor_bits) - 1;
  u64 lo = low, hi = high;
  if (cohort == 2) hi = static_cast<u64>((static_cast<u128>(high) * 32) / 63);
  require(lo <= hi, "candidate p interval");
  if ((lo & 1) == 0) ++lo;
  if ((hi & 1) == 0) --hi;
  const u64 count = (hi - lo) / 2 + 1;
  const u64 h = splitmix64(tag ^ (static_cast<u64>(factor_bits) << 48)
                            ^ (serial * 0x9e3779b97f4a7c15ULL));
  return lo + 2 * (h % count);
}

static bool cohort_accepts(int cohort, u64 p, u64 q) {
  if (cohort == 1 && static_cast<u128>(32) * q > static_cast<u128>(33) * p)
    return false;
  if (cohort == 2 && static_cast<u128>(32) * q < static_cast<u128>(63) * p)
    return false;
  (void)p;
  (void)q;
  return true;
}

static bool pair_from_serial(int factor_bits, int cohort, u64 serial, u64 tag,
                             u64& p_out, u64& q_out) {
  const u64 low = 1ULL << (factor_bits - 1);
  const u64 high = (1ULL << factor_bits) - 1;
  const u64 p = candidate_p(factor_bits, cohort, serial, tag);
  if (cohort == 3 ? !is_safe_prime(p) : !is_prime(p)) return false;
  for (int n : {2 * factor_bits - 1, 2 * factor_bits}) {
    const int m = n / 2;
    const u64 B = 1ULL << m;
    const u64 r = inverse_power_two(p, B);
    u128 q = r;
    if (q < low) q += ((static_cast<u128>(low) - q + B - 1) / B) * B;
    for (; q <= high; q += B) {
      const u64 qq = static_cast<u64>(q);
      if (!(p < qq && qq < 2 * p)) continue;
      const u128 N = static_cast<u128>(p) * qq;
      if (bit_length(N) != n || (N - 1) % B != 0) continue;
      if (cohort == 3 ? !is_safe_prime(qq) : !is_prime(qq)) continue;
      if (!cohort_accepts(cohort, p, qq)) continue;
      p_out = p;
      q_out = qq;
      return true;
    }
  }
  return false;
}

static std::vector<Task> make_tasks(std::vector<std::array<u64, COHORT_COUNT>>& attempts) {
  std::vector<Task> tasks;
  std::set<std::pair<u64, u64>> global_seen;
  attempts.assign(std::size(FACTOR_BITS), {});
  for (std::size_t fi = 0; fi < std::size(FACTOR_BITS); ++fi) {
    const int f = FACTOR_BITS[fi];
    for (int cohort = 0; cohort < COHORT_COUNT; ++cohort) {
      int accepted = 0;
      for (u64 serial = 0; serial < ATTEMPT_CAPS[cohort]; ++serial) {
        attempts[fi][cohort] = serial + 1;
        u64 p = 0, q = 0;
        if (!pair_from_serial(f, cohort, serial, COHORT_TAGS[cohort], p, q))
          continue;
        if (!global_seen.insert({p, q}).second) continue;
        tasks.push_back({f, cohort, accepted, serial + 1, p, q});
        if (++accepted == COHORT_SIZES[cohort]) break;
      }
      require(accepted == COHORT_SIZES[cohort],
              std::string("cohort attempt cap exhausted: ")
              + COHORT_NAMES[cohort] + " f=" + std::to_string(f));
    }
  }
  require(tasks.size() == 1368, "frozen task count");
  return tasks;
}

struct PredictorResult {
  u64 min_abs;
  u64 first_u;
};

struct InputResult {
  Task task;
  u128 N;
  int n;
  int m;
  u64 B;
  u64 H;
  std::array<u64, 3> min_abs;
  std::array<u64, 3> min_u;
  u64 odd_min_abs;
  u64 odd_min_u;
  std::array<u64, 4> oracle_hit_count;
  std::array<u64, 4> first_oracle_hit;
  u64 half_ties;
  u64 longest_diff_run;
  u64 max_c_fibre;
  u64 zero_count;
  int max_v2;
  u64 max_gcd_c_u;
  bool oracle_cf_p;
  bool oracle_cf_q;
  int oracle_rank2[2];
  int oracle_rank3[2];
  int surrogate_match[3];
  int surrogate_rank2[3][2];
  int surrogate_rank3[3][2];
  std::array<int, PREFIX_COUNT> prefix_t;
  std::array<bool, PREFIX_COUNT> prefix_terminal;
  std::array<std::string, PREFIX_COUNT> bank_c2;
  std::array<std::string, PREFIX_COUNT> bank_cqp;
  PredictorResult predictors[PREFIX_COUNT][PREDICTOR_COUNT];
};

static int ceil_log2_u64(u64 n) {
  int k = 0;
  u64 x = 1;
  while (x < n) {
    x <<= 1;
    ++k;
  }
  return k;
}

static int v2_abs(s128 x) {
  u128 a = abs128(x);
  if (a == 0) return 128;
  int v = 0;
  while ((a & 1) == 0) {
    ++v;
    a >>= 1;
  }
  return v;
}

static std::vector<u64> cf_denominators(u64 numerator, u64 denominator,
                                        u64 cap, std::size_t limit) {
  std::set<u64> values;
  if (denominator == 0) return {};
  u64 a = numerator, b = denominator;
  u128 qm2 = 1, qm1 = 0;
  while (b && values.size() < limit) {
    const u64 coefficient = a / b;
    for (u64 t = 1; t <= coefficient && values.size() < limit; ++t) {
      const u128 q = static_cast<u128>(t) * qm1 + qm2;
      if (q > cap) break;
      if (q > 0) values.insert(static_cast<u64>(q));
    }
    const u128 q = static_cast<u128>(coefficient) * qm1 + qm2;
    if (q > cap || q > std::numeric_limits<u64>::max()) break;
    qm2 = qm1;
    qm1 = q;
    const u64 r = a % b;
    a = b;
    b = r;
  }
  return {values.begin(), values.end()};
}

static std::vector<u64> first_n_by_score(std::vector<std::pair<u128, u64>> scores,
                                         int n) {
  std::sort(scores.begin(), scores.end(), [](const auto& a, const auto& b) {
    return a.first != b.first ? a.first < b.first : a.second < b.second;
  });
  std::vector<u64> values;
  std::set<u64> seen;
  for (const auto& [score, u] : scores) {
    (void)score;
    if (seen.insert(u).second) values.push_back(u);
    if (static_cast<int>(values.size()) == n) break;
  }
  return values;
}

static u64 lower_median_key(std::vector<u64> values) {
  require(!values.empty(), "lower median nonempty");
  std::sort(values.begin(), values.end());
  return values[(values.size() - 1) / 2];
}

static u64 public_sqrt_center(u128 N, u64 B, u64 u) {
  return rounded_center(static_cast<u128>(u) * isqrt128(N), B);
}

static double conservative_parallel_seconds(double single_worker_seconds,
                                            int workers) {
  require(1 <= workers && workers <= 8, "projection worker count 1..8");
  return single_worker_seconds / (PARALLEL_EFFICIENCY * workers);
}

static std::vector<std::array<int, 4>> monomial_exponents(int degree) {
  std::vector<std::array<int, 4>> out;
  for (int a = 0; a <= degree; ++a)
    for (int b = 0; b <= degree - a; ++b)
      for (int c = 0; c <= degree - a - b; ++c)
        for (int d = 0; d <= degree - a - b - c; ++d)
          out.push_back({a, b, c, d});
  return out;
}

static u64 mod_signed(s128 x, u64 prime) {
  s128 r = x % static_cast<s128>(prime);
  if (r < 0) r += prime;
  return static_cast<u64>(r);
}

static int polynomial_rank(const std::vector<std::array<s128, 4>>& points,
                           int degree, u64 prime) {
  const auto exponents = monomial_exponents(degree);
  std::vector<std::vector<u64>> matrix(points.size(),
                                       std::vector<u64>(exponents.size()));
  for (std::size_t i = 0; i < points.size(); ++i) {
    for (std::size_t j = 0; j < exponents.size(); ++j) {
      u64 value = 1;
      for (int v = 0; v < 4; ++v) {
        const u64 base = mod_signed(points[i][v], prime);
        for (int e = 0; e < exponents[j][v]; ++e)
          value = mul_mod(value, base, prime);
      }
      matrix[i][j] = value;
    }
  }
  int rank = 0;
  for (std::size_t col = 0; col < exponents.size() && rank < static_cast<int>(matrix.size());
       ++col) {
    int pivot = rank;
    while (pivot < static_cast<int>(matrix.size()) && matrix[pivot][col] == 0)
      ++pivot;
    if (pivot == static_cast<int>(matrix.size())) continue;
    std::swap(matrix[rank], matrix[pivot]);
    const u64 inv = pow_mod(matrix[rank][col], prime - 2, prime);
    for (std::size_t j = col; j < exponents.size(); ++j)
      matrix[rank][j] = mul_mod(matrix[rank][j], inv, prime);
    for (std::size_t i = 0; i < matrix.size(); ++i) {
      if (static_cast<int>(i) == rank || matrix[i][col] == 0) continue;
      const u64 factor = matrix[i][col];
      for (std::size_t j = col; j < exponents.size(); ++j) {
        const u64 sub = mul_mod(factor, matrix[rank][j], prime);
        matrix[i][j] = matrix[i][j] >= sub
                           ? matrix[i][j] - sub
                           : matrix[i][j] + prime - sub;
      }
    }
    ++rank;
  }
  return rank;
}

static std::pair<u64, u64> center_intervals(u128 N, u64 B, u64 u, bool p_side) {
  const u64 sqrtN = isqrt128(N);
  const u64 p_lo = isqrt128(N / 2) + 1;
  const u64 p_hi = sqrtN;
  const u64 q_lo = sqrtN + 1;
  const u64 q_hi = isqrt128(2 * N - 1);
  const u64 lo = p_side ? p_lo : q_lo;
  const u64 hi = p_side ? p_hi : q_hi;
  return {rounded_center(static_cast<u128>(u) * lo, B),
          rounded_center(static_cast<u128>(u) * hi, B)};
}

static cpp_int bank_bound(u128 N, u64 B, u64 U, const cpp_int& C, u64 R) {
  const u64 sqrtN = isqrt128(N);
  const u64 p_lo = isqrt128(N / 2) + 1;
  const u64 p_hi = sqrtN;
  const u64 q_lo = sqrtN + 1;
  const u64 q_hi = isqrt128(2 * N - 1);
  cpp_int total = 0;
  for (u64 u = 1; u <= U; ++u) {
    const u64 p_first = rounded_center(static_cast<u128>(u) * p_lo, B);
    const u64 p_last = rounded_center(static_cast<u128>(u) * p_hi, B);
    const u64 q_first = rounded_center(static_cast<u128>(u) * q_lo, B);
    const u64 q_last = rounded_center(static_cast<u128>(u) * q_hi, B);
    const u64 pc = p_last - p_first + 1;
    const u64 qc = q_last - q_first + 1;
    total += cpp_int(pc) * qc * (1 + (2 * C) / (cpp_int(u) * R));
  }
  return total;
}

static bool terminal_prefix(u128 N, u64 R, int n) {
  cpp_int left = cpp_int(R) * R * R * R;
  cpp_int ns = n;
  for (int i = 0; i < 8; ++i) left *= ns;
  cpp_int target(string_u128(N));
  return left >= target;
}

static std::pair<u64, u64> best_product_centers(u128 N, u64 B, u64 H, u64 u) {
  const auto pi = center_intervals(N, B, u, true);
  const auto qi = center_intervals(N, B, u, false);
  const u128 target = static_cast<u128>(u) * u * H;
  u128 best = ~static_cast<u128>(0);
  std::pair<u64, u64> answer{pi.first, qi.first};
  for (u64 kp = pi.first; kp <= pi.second; ++kp) {
    const u128 denominator = static_cast<u128>(kp) * B;
    u64 guess = denominator ? static_cast<u64>((target + denominator / 2) / denominator)
                            : qi.first;
    for (u64 kq : {qi.first, qi.second, guess, guess > 0 ? guess - 1 : 0, guess + 1}) {
      if (kq < qi.first || kq > qi.second) continue;
      const u128 value = static_cast<u128>(kp) * kq * B;
      const u128 error = value >= target ? value - target : target - value;
      if (error < best || (error == best && std::pair<u64, u64>{kp, kq} < answer)) {
        best = error;
        answer = {kp, kq};
      }
    }
    if (kp == pi.second) break;
  }
  return answer;
}

static InputResult process_input(const Task& task) {
  const u64 p = task.p, q = task.q;
  const u128 N = static_cast<u128>(p) * q;
  const int n = bit_length(N), m = n / 2;
  const u64 B = 1ULL << m;
  require((N - 1) % B == 0, "zero defect input");
  const u64 H = static_cast<u64>((N - 1) / B);
  const u64 U1 = n, U2 = static_cast<u64>(n) * n;
  const u64 U3 = std::min<u64>(static_cast<u64>(n) * n * n, U3_HARD_CAP);
  const std::array<u64, 4> C = {
      static_cast<u64>(n), static_cast<u64>(n) * n,
      static_cast<u64>(n) * n * n,
      1ULL << (ceil_log2_u64(n) * ceil_log2_u64(n))};

  InputResult result{};
  result.task = task;
  result.N = N;
  result.n = n;
  result.m = m;
  result.B = B;
  result.H = H;
  result.min_abs.fill(std::numeric_limits<u64>::max());
  result.min_u.fill(0);
  result.odd_min_abs = std::numeric_limits<u64>::max();
  result.first_oracle_hit.fill(0);
  std::vector<s128> carries(U2 + 1);
  std::vector<CarryPoint> first64;
  first64.reserve(64);
  std::unordered_map<std::int64_t, u64> fibres;
  fibres.reserve(2 * U2);
  s128 prior_diff = 0;
  u64 current_diff_run = 0;

  for (u64 u = 1; u <= U3; ++u) {
    const CarryPoint point = carry_point(p, q, N, B, H, u);
    const u64 ac = static_cast<u64>(abs128(point.c));
    if (u <= U1 && ac < result.min_abs[0]) result.min_abs[0] = ac, result.min_u[0] = u;
    if (u <= U2 && ac < result.min_abs[1]) result.min_abs[1] = ac, result.min_u[1] = u;
    if (ac < result.min_abs[2]) result.min_abs[2] = ac, result.min_u[2] = u;
    if ((u & 1) && ac < result.odd_min_abs)
      result.odd_min_abs = ac, result.odd_min_u = u;
    for (int j = 0; j < 4; ++j) {
      if (ac <= C[j]) {
        ++result.oracle_hit_count[j];
        if (result.first_oracle_hit[j] == 0) result.first_oracle_hit[j] = u;
      }
    }
    result.half_ties += point.tie_p + point.tie_q;
    if (u <= U2) {
      carries[u] = point.c;
      const auto key = static_cast<std::int64_t>(point.c);
      result.max_c_fibre = std::max(result.max_c_fibre, ++fibres[key]);
      if (point.c == 0) ++result.zero_count;
      result.max_v2 = std::max(result.max_v2, v2_abs(point.c));
      result.max_gcd_c_u = std::max<u64>(
          result.max_gcd_c_u, std::gcd(static_cast<u64>(abs128(point.c)), u));
      if (u >= 2) {
        const s128 diff = carries[u] - carries[u - 1];
        if (u == 2 || diff != prior_diff) current_diff_run = 1;
        else ++current_diff_run;
        prior_diff = diff;
        result.longest_diff_run = std::max(result.longest_diff_run, current_diff_run);
      }
      if (u <= 64) first64.push_back(point);
    }
  }

  const int prefix_t[PREFIX_COUNT] = {0, m / 4, (3 * m) / 8, m / 2};
  const u64 sqrtN = isqrt128(N);
  for (int pi = 0; pi < PREFIX_COUNT; ++pi) {
    const int t = prefix_t[pi];
    const u64 R = 1ULL << t;
    result.prefix_t[pi] = t;
    result.prefix_terminal[pi] = terminal_prefix(N, R, n);
    const PrefixData prefix = prefix_data(N, p, R);
    const u64 a = prefix.a, b = prefix.b;
    require(R == 1 || b == (q & (R - 1)), "public prefix companion");

    const cpp_int C2 = static_cast<u64>(n) * n;
    const cpp_int Cqp = cpp_int(1) << (ceil_log2_u64(n) * ceil_log2_u64(n));
    result.bank_c2[pi] = bank_bound(N, B, U2, C2, R).convert_to<std::string>();
    result.bank_cqp[pi] = bank_bound(N, B, U2, Cqp, R).convert_to<std::string>();

    std::vector<u64> candidates[PREDICTOR_COUNT];
    for (u64 u = 1; u <= U1; ++u) candidates[0].push_back(u);
    std::set<u64> hashed;
    for (u64 serial = 0; static_cast<int>(hashed.size()) < n; ++serial) {
      const u64 lo = static_cast<u64>(N);
      const u64 hi = static_cast<u64>(N >> 64);
      const u64 h = splitmix64(lo ^ (hi * 0xd6e8feb86659fd93ULL)
                               ^ (static_cast<u64>(pi) << 56) ^ serial);
      hashed.insert(1 + h % U2);
    }
    candidates[1] = {hashed.begin(), hashed.end()};

    std::vector<std::pair<u128, u64>> scores[6];
    for (u64 u = 1; u <= U2; ++u) {
      const s128 ra = centered_mod(static_cast<u128>(u) * a, R);
      const s128 rb = centered_mod(static_cast<u128>(u) * b, R);
      const u128 aa = abs128(ra), ab = abs128(rb);
      scores[0].push_back({std::max(aa, ab), u});
      scores[1].push_back({aa + ab, u});
      scores[2].push_back({abs128(ra * rb - static_cast<s128>(u) * u), u});
      scores[3].push_back({abs128(centered_mod(static_cast<u128>(u) * sqrtN, B)), u});
      scores[4].push_back({abs128(centered_mod(static_cast<u128>(u) * H, B)), u});
      const u64 k0 = public_sqrt_center(N, B, u);
      const s128 residual = static_cast<s128>(static_cast<u128>(k0) * k0 * B)
                            - static_cast<s128>(static_cast<u128>(u) * u * H);
      scores[5].push_back({abs128(residual), u});
    }
    for (int j = 0; j < 6; ++j) candidates[2 + j] = first_n_by_score(std::move(scores[j]), n);

    std::set<u64> cf;
    auto append_cf = [&](u64 numerator, u64 denominator) {
      for (u64 u : cf_denominators(numerator, denominator, U2, 4 * n)) cf.insert(u);
    };
    if (pi == 0) {
      append_cf(H, B);
      append_cf(sqrtN, B);
    } else {
      append_cf(a, R);
      append_cf(b, R);
      append_cf((a + b) & (R - 1), R);
      append_cf(a >= b ? a - b : b - a, R);
    }
    for (u64 u : cf) {
      candidates[8].push_back(u);
      if (static_cast<int>(candidates[8].size()) == n) break;
    }
    if (candidates[8].empty()) candidates[8] = candidates[0];

    for (int pred = 0; pred < PREDICTOR_COUNT; ++pred) {
      PredictorResult pr{std::numeric_limits<u64>::max(), 0};
      for (u64 u : candidates[pred]) {
        require(1 <= u && u <= U2, "predictor multiplier range");
        const u64 ac = static_cast<u64>(abs128(carries[u]));
        if (ac < pr.min_abs || (ac == pr.min_abs && u < pr.first_u))
          pr = {ac, u};
      }
      result.predictors[pi][pred] = pr;
    }
  }

  std::set<u64> cfp, cfq;
  for (u64 u : cf_denominators(p, B, U2, 4 * n)) cfp.insert(u);
  for (u64 u : cf_denominators(q, B, U2, 4 * n)) cfq.insert(u);
  result.oracle_cf_p = cfp.count(result.min_u[2]);
  result.oracle_cf_q = cfq.count(result.min_u[2]);

  const u64 primes[2] = {1000000007ULL, 1000000009ULL};
  std::vector<std::array<s128, 4>> oracle_points;
  for (u64 u = 1; u <= 64; ++u) {
    const auto& point = first64[u - 1];
    oracle_points.push_back({static_cast<s128>(u), static_cast<s128>(point.kp),
                             static_cast<s128>(point.kq), point.c});
  }
  for (int j = 0; j < 2; ++j) {
    result.oracle_rank2[j] = polynomial_rank(oracle_points, 2, primes[j]);
    result.oracle_rank3[j] = polynomial_rank(oracle_points, 3, primes[j]);
  }

  std::vector<std::array<s128, 4>> surrogate_points[3];
  for (u64 u = 1; u <= 64; ++u) {
    const auto& point = first64[u - 1];
    const u64 common = public_sqrt_center(N, B, u);
    const auto pi = center_intervals(N, B, u, true);
    const auto qi = center_intervals(N, B, u, false);
    const auto product = best_product_centers(N, B, H, u);
    const std::pair<u64, u64> pairs[3] = {
        {common, common}, {pi.first, qi.second}, product};
    for (int s = 0; s < 3; ++s) {
      if (pairs[s].first == point.kp && pairs[s].second == point.kq)
        ++result.surrogate_match[s];
      surrogate_points[s].push_back({static_cast<s128>(u),
                                      static_cast<s128>(pairs[s].first),
                                      static_cast<s128>(pairs[s].second), point.c});
    }
  }
  for (int s = 0; s < 3; ++s)
    for (int j = 0; j < 2; ++j) {
      result.surrogate_rank2[s][j] = polynomial_rank(surrogate_points[s], 2, primes[j]);
      result.surrogate_rank3[s][j] = polynomial_rank(surrogate_points[s], 3, primes[j]);
    }
  return result;
}

static s128 inverse_map_c(u64 x_mod, u64 B, u64 u) {
  require((x_mod & 1) && B >= 4, "inverse-map unit");
  const u64 inverse = inverse_power_two(x_mod, B);
  const u64 y_mod = mul_mod((u * u) & (B - 1), inverse, B);
  const s128 x = x_mod >= B / 2 ? static_cast<s128>(x_mod) - B : x_mod;
  const s128 y = y_mod >= B / 2 ? static_cast<s128>(y_mod) - B : y_mod;
  const s128 numerator = x * y - static_cast<s128>(u) * u;
  require(numerator % static_cast<s128>(B) == 0, "inverse-map carry");
  return numerator / static_cast<s128>(B);
}

static void write_inverse_studies(const std::vector<InputResult>& results,
                                  const std::string& path) {
  std::map<std::pair<int, int>, const InputResult*> worst;
  for (const auto& r : results) {
    const auto key = std::make_pair(r.task.factor_bits, r.task.cohort);
    auto it = worst.find(key);
    if (it == worst.end() || r.min_abs[2] > it->second->min_abs[2]
        || (r.min_abs[2] == it->second->min_abs[2] && r.N < it->second->N))
      worst[key] = &r;
  }
  std::ofstream out(path);
  require(static_cast<bool>(out), "open inverse TSV");
  out << "factor_bits\tcohort\tp\tq\tprefix\tt\tu\tmap_size\tmode"
         "\tpublic_samples\toracle_window\ttrue_abs_c\ttrue_rank"
         "\tmax_c_fibre\tmax_abs_fibre\tlongest_affine_run"
         "\tmax_v2" << ORACLE_HIT_COLUMNS << '\n';
  for (const auto& [key, rp] : worst) {
    (void)key;
    const auto& r = *rp;
    const u64 u = r.odd_min_u;
    const CarryPoint truth = carry_point(r.task.p, r.task.q, r.N, r.B, r.H, u);
    for (int pi = 1; pi < PREFIX_COUNT; ++pi) {
      const int t = r.prefix_t[pi];
      const u64 R = 1ULL << t;
      const u64 a = r.task.p & (R - 1);
      const s128 ua = static_cast<s128>(u) * a;
      const s128 zlo = ceil_div(-static_cast<s128>(r.B / 2) - ua, R);
      const s128 zhi = floor_div(static_cast<s128>(r.B / 2) - 1 - ua, R);
      require(zhi >= zlo, "inverse-map z interval");
      const u64 map_size = static_cast<u64>(zhi - zlo + 1);
      require(map_size == r.B / R, "inverse-map size");
      require((truth.x - ua) % R == 0, "true z congruence");
      const s128 true_z = (truth.x - ua) / R;
      require(zlo <= true_z && true_z <= zhi, "true z interval");
      const u64 true_index = static_cast<u64>(true_z - zlo);

      const u64 public_count = std::min<u64>(4096, map_size);
      const u64 start = splitmix64(static_cast<u64>(r.N) ^ (static_cast<u64>(pi) << 55))
                        & (map_size - 1);
      u64 step = splitmix64(static_cast<u64>(r.N >> 64) ^ (static_cast<u64>(pi) << 49)) | 1;
      step &= map_size - 1;
      if (step == 0) step = 1;
      std::unordered_map<std::int64_t, u64> c_fibres, abs_fibres;
      std::array<u64, 4> oracle_hits{};
      const std::array<u64, 4> thresholds = {
          static_cast<u64>(r.n), static_cast<u64>(r.n) * r.n,
          static_cast<u64>(r.n) * r.n * r.n,
          1ULL << (ceil_log2_u64(r.n) * ceil_log2_u64(r.n))};
      u64 less = 0, max_c = 0, max_abs = 0;
      const u64 true_abs = static_cast<u64>(abs128(truth.c));
      for (u64 j = 0; j < public_count; ++j) {
        const u64 index = (start + static_cast<u128>(j) * step) & (map_size - 1);
        const s128 z = zlo + index;
        s128 x = ua + static_cast<s128>(R) * z;
        s128 xm = x % static_cast<s128>(r.B);
        if (xm < 0) xm += r.B;
        const s128 c = inverse_map_c(static_cast<u64>(xm), r.B, u);
        const u64 ac = static_cast<u64>(abs128(c));
        if (ac < true_abs) ++less;
        max_c = std::max(max_c, ++c_fibres[static_cast<std::int64_t>(c)]);
        max_abs = std::max(max_abs, ++abs_fibres[static_cast<std::int64_t>(ac)]);
        for (int k = 0; k < 4; ++k)
          if (ac <= thresholds[k]) ++oracle_hits[k];
      }

      const u64 wlo = true_index > 1024 ? true_index - 1024 : 0;
      const u64 whi = std::min<u64>(map_size, wlo + 2048);
      u64 affine = 0, run = 0;
      s128 previous = 0, previous_diff = 0;
      int max_v = 0;
      for (u64 index = wlo; index < whi; ++index) {
        const s128 z = zlo + index;
        s128 x = ua + static_cast<s128>(R) * z;
        s128 xm = x % static_cast<s128>(r.B);
        if (xm < 0) xm += r.B;
        const s128 c = inverse_map_c(static_cast<u64>(xm), r.B, u);
        max_v = std::max(max_v, v2_abs(c));
        if (index > wlo) {
          const s128 diff = c - previous;
          if (index == wlo + 1 || diff != previous_diff) run = 1;
          else ++run;
          affine = std::max(affine, run);
          previous_diff = diff;
        }
        previous = c;
      }
      out << r.task.factor_bits << '\t' << COHORT_NAMES[r.task.cohort] << '\t'
          << r.task.p << '\t' << r.task.q << '\t' << PREFIX_NAMES[pi] << '\t'
          << t << '\t' << u << '\t' << map_size << '\t'
          << (map_size <= 4096 ? "complete" : "sample") << '\t'
          << public_count << '\t' << (whi - wlo) << '\t' << true_abs << '\t'
          << (less + 1) << '\t' << max_c << '\t' << max_abs << '\t' << affine
          << '\t' << max_v;
      for (u64 hit : oracle_hits) out << '\t' << hit;
      out << '\n';
    }
  }
}

static void write_consecutive(const std::string& path) {
  const int limit = 1 << 22;
  std::vector<bool> prime(limit, true);
  prime[0] = prime[1] = false;
  for (int p = 2; static_cast<long long>(p) * p < limit; ++p)
    if (prime[p]) for (int j = p * p; j < limit; j += p) prime[j] = false;
  std::vector<int> primes;
  for (int p = 2; p < limit; ++p) if (prime[p]) primes.push_back(p);
  std::ofstream out(path);
  require(static_cast<bool>(out), "open consecutive TSV");
  out << "factor_bits\tp\tq\tN\tn\tB\tmin_n\tu_n\tmin_n2\tu_n2\tmin_n3\tu_n3\n";
  for (std::size_t i = 0; i + 1 < primes.size(); ++i) {
    const u64 p = primes[i], q = primes[i + 1];
    const int f = 64 - __builtin_clzll(p);
    if (f < 8 || f > 22 || (64 - __builtin_clzll(q)) != f || q >= 2 * p) continue;
    const u128 N = static_cast<u128>(p) * q;
    const int n = bit_length(N), m = n / 2;
    const u64 B = 1ULL << m;
    if ((N - 1) % B) continue;
    const u64 H = static_cast<u64>((N - 1) / B);
    const u64 caps[3] = {static_cast<u64>(n), static_cast<u64>(n) * n,
                         std::min<u64>(static_cast<u64>(n) * n * n, U3_HARD_CAP)};
    u64 minima[3] = {~0ULL, ~0ULL, ~0ULL}, where[3]{};
    for (u64 u = 1; u <= caps[2]; ++u) {
      const u64 ac = static_cast<u64>(abs128(carry_point(p, q, N, B, H, u).c));
      for (int j = 0; j < 3; ++j)
        if (u <= caps[j] && ac < minima[j]) minima[j] = ac, where[j] = u;
    }
    out << f << '\t' << p << '\t' << q << '\t' << string_u128(N) << '\t'
        << n << '\t' << B;
    for (int j = 0; j < 3; ++j) out << '\t' << minima[j] << '\t' << where[j];
    out << '\n';
  }
}

struct SelectionScore {
  u64 min_hits;
  u64 min_count;
  u64 total_hits;
  u64 lower_median;
  std::string name;
  int predictor;
};

static bool better_score(const SelectionScore& a, const SelectionScore& b) {
  const u128 left = static_cast<u128>(a.min_hits) * b.min_count;
  const u128 right = static_cast<u128>(b.min_hits) * a.min_count;
  if (left != right) return left > right;
  if (a.total_hits != b.total_hits) return a.total_hits > b.total_hits;
  if (a.lower_median != b.lower_median)
    return a.lower_median < b.lower_median;
  return a.name < b.name;
}

static std::vector<std::array<int, 3>> select_predictors(
    const std::vector<InputResult>& results) {
  std::vector<std::array<int, 3>> selected(PREFIX_COUNT);
  for (int pi = 0; pi < PREFIX_COUNT; ++pi) {
    std::vector<SelectionScore> scores;
    for (int pred = 0; pred < PREDICTOR_COUNT; ++pred) {
      u64 min_hits = ~0ULL, min_count = 1, total = 0;
      std::vector<u64> values;
      for (int f : FACTOR_BITS) if (f <= 40) {
        for (int cohort = 0; cohort < COHORT_COUNT; ++cohort) {
          u64 hits = 0, count = 0;
          for (const auto& r : results)
            if (r.task.factor_bits == f && r.task.cohort == cohort) {
              ++count;
              const u64 v = r.predictors[pi][pred].min_abs;
              values.push_back(v);
              if (v <= static_cast<u64>(r.n) * r.n) ++hits;
            }
          require(count > 0, "train cell nonempty");
          if (min_hits == ~0ULL || static_cast<u128>(hits) * min_count
                                  < static_cast<u128>(min_hits) * count)
            min_hits = hits, min_count = count;
          total += hits;
        }
      }
      const u64 lower_median = lower_median_key(std::move(values));
      scores.push_back({min_hits, min_count, total, lower_median,
                        PREDICTOR_NAMES[pred], pred});
    }
    std::sort(scores.begin(), scores.end(), better_score);
    for (int j = 0; j < 3; ++j) selected[pi][j] = scores[j].predictor;
  }
  return selected;
}

static void write_rows(const std::vector<InputResult>& results,
                       const std::string& path) {
  std::ofstream out(path);
  require(static_cast<bool>(out), "open rows TSV");
  out << "factor_bits\tsplit\tcohort\tindex\tattempts\tp\tq\tN\tn\tB\tH"
         "\tmin_n\tu_n\tmin_n2\tu_n2\tmin_n3\tu_n3\todd_min\todd_u"
      << ORACLE_HIT_COLUMNS
      << "\tfirst_oracle_n\tfirst_oracle_n2\tfirst_oracle_n3"
         "\tfirst_oracle_cqp\thalf_ties\tlongest_diff_run\tmax_c_fibre\tzero_count"
         "\tmax_v2\tmax_gcd_c_u\toracle_cf_p\toracle_cf_q"
         "\torank2_p1\trank2_p2\trank3_p1\trank3_p2";
  for (int s = 0; s < 3; ++s)
    out << "\tsurr" << s << "_match\tsurr" << s << "_r2p1\tsurr" << s
        << "_r2p2\tsurr" << s << "_r3p1\tsurr" << s << "_r3p2";
  for (int pi = 0; pi < PREFIX_COUNT; ++pi) {
    out << '\t' << PREFIX_NAMES[pi] << "_t\t" << PREFIX_NAMES[pi]
        << "_terminal\t" << PREFIX_NAMES[pi] << "_bank_c2\t"
        << PREFIX_NAMES[pi] << "_bank_cqp";
    for (int pred = 0; pred < PREDICTOR_COUNT; ++pred)
      out << '\t' << PREFIX_NAMES[pi] << '_' << PREDICTOR_NAMES[pred] << "_min"
          << '\t' << PREFIX_NAMES[pi] << '_' << PREDICTOR_NAMES[pred] << "_u";
  }
  out << '\n';
  for (const auto& r : results) {
    out << r.task.factor_bits << '\t' << (r.task.factor_bits <= 40 ? "train" : "heldout")
        << '\t' << COHORT_NAMES[r.task.cohort] << '\t' << r.task.index << '\t'
        << r.task.attempts << '\t' << r.task.p << '\t' << r.task.q << '\t'
        << string_u128(r.N) << '\t' << r.n << '\t' << r.B << '\t' << r.H;
    for (int j = 0; j < 3; ++j) out << '\t' << r.min_abs[j] << '\t' << r.min_u[j];
    out << '\t' << r.odd_min_abs << '\t' << r.odd_min_u;
    for (u64 v : r.oracle_hit_count) out << '\t' << v;
    for (u64 v : r.first_oracle_hit) out << '\t' << v;
    out << '\t' << r.half_ties << '\t' << r.longest_diff_run << '\t'
        << r.max_c_fibre << '\t' << r.zero_count << '\t' << r.max_v2 << '\t'
        << r.max_gcd_c_u << '\t' << r.oracle_cf_p << '\t' << r.oracle_cf_q
        << '\t' << r.oracle_rank2[0] << '\t' << r.oracle_rank2[1]
        << '\t' << r.oracle_rank3[0] << '\t' << r.oracle_rank3[1];
    for (int s = 0; s < 3; ++s)
      out << '\t' << r.surrogate_match[s] << '\t' << r.surrogate_rank2[s][0]
          << '\t' << r.surrogate_rank2[s][1] << '\t' << r.surrogate_rank3[s][0]
          << '\t' << r.surrogate_rank3[s][1];
    for (int pi = 0; pi < PREFIX_COUNT; ++pi) {
      out << '\t' << r.prefix_t[pi] << '\t' << r.prefix_terminal[pi]
          << '\t' << r.bank_c2[pi] << '\t' << r.bank_cqp[pi];
      for (int pred = 0; pred < PREDICTOR_COUNT; ++pred)
        out << '\t' << r.predictors[pi][pred].min_abs
            << '\t' << r.predictors[pi][pred].first_u;
    }
    out << '\n';
  }
}

static void write_summary(const std::vector<InputResult>& results,
                          const std::vector<std::array<u64, COHORT_COUNT>>& attempts,
                          const std::vector<std::array<int, 3>>& selected,
                          double generation_seconds, double scan_seconds,
                          int threads, const std::string& path) {
  std::ofstream out(path);
  require(static_cast<bool>(out), "open summary JSON");
  out << "{\n  \"experiment\": \"" << EXPERIMENT_NAME
      << "\",\n  \"executes_factor_bank\": "
      << (EXECUTES_FACTOR_BANK ? "true" : "false")
      << ",\n  \"oracle_hit_semantics\": \"" << ORACLE_HIT_SEMANTICS
      << "\",\n  \"inputs\": " << results.size()
      << ",\n  \"threads\": " << threads
      << ",\n  \"generation_seconds\": " << std::setprecision(12) << generation_seconds
      << ",\n  \"scan_seconds\": " << scan_seconds << ",\n  \"attempts\": [\n";
  bool comma = false;
  for (std::size_t fi = 0; fi < std::size(FACTOR_BITS); ++fi)
    for (int cohort = 0; cohort < COHORT_COUNT; ++cohort) {
      if (comma) out << ",\n";
      comma = true;
      out << "    {\"factor_bits\": " << FACTOR_BITS[fi]
          << ", \"cohort\": \"" << COHORT_NAMES[cohort]
          << "\", \"attempts\": " << attempts[fi][cohort] << "}";
    }
  out << "\n  ],\n  \"selected_predictors\": [\n";
  for (int pi = 0; pi < PREFIX_COUNT; ++pi) {
    if (pi) out << ",\n";
    out << "    {\"prefix\": \"" << PREFIX_NAMES[pi] << "\", \"names\": [";
    for (int j = 0; j < 3; ++j) {
      if (j) out << ", ";
      out << "\"" << PREDICTOR_NAMES[selected[pi][j]] << "\"";
    }
    out << "]}";
  }
  out << "\n  ],\n  \"cells\": [\n";
  comma = false;
  for (int f : FACTOR_BITS) for (int cohort = 0; cohort < COHORT_COUNT; ++cohort) {
    std::vector<const InputResult*> cell;
    for (const auto& r : results)
      if (r.task.factor_bits == f && r.task.cohort == cohort) cell.push_back(&r);
    require(!cell.empty(), "summary cell");
    for (int pi = 0; pi < PREFIX_COUNT; ++pi) for (int pred = 0; pred < PREDICTOR_COUNT; ++pred) {
      u64 hits = 0, maximum = 0;
      const InputResult* worst = nullptr;
      for (const InputResult* r : cell) {
        const u64 value = r->predictors[pi][pred].min_abs;
        if (value <= static_cast<u64>(r->n) * r->n) ++hits;
        if (!worst || value > maximum) maximum = value, worst = r;
      }
      if (comma) out << ",\n";
      comma = true;
      out << "    {\"factor_bits\": " << f << ", \"split\": \""
          << (f <= 40 ? "train" : "heldout") << "\", \"cohort\": \""
          << COHORT_NAMES[cohort] << "\", \"prefix\": \"" << PREFIX_NAMES[pi]
          << "\", \"predictor\": \"" << PREDICTOR_NAMES[pred]
          << "\", \"count\": " << cell.size()
          << ", \"oracle_hits_n2\": " << hits
          << ", \"max_min_abs_c\": " << maximum << ", \"worst_p\": "
          << worst->task.p << ", \"worst_q\": " << worst->task.q << "}";
    }
  }
  out << "\n  ]\n}\n";
}

static void v2_self_test() {
  const u64 p = 101, q = 109;
  const u128 N = static_cast<u128>(p) * q;
  const int n = bit_length(N);
  const u64 B = 1ULL << (n / 2);
  require((N - 1) % B == 0, "self-test zero defect");
  const u64 H = static_cast<u64>((N - 1) / B);

  bool inverse_branch = false;
  const PrefixData none = prefix_data(N, p, 1, &inverse_branch);
  require(none.a == 0 && none.b == 0 && !inverse_branch,
          "R=1 explicit no-inverse convention");
  const PrefixData nontrivial = prefix_data(N, p, 8, &inverse_branch);
  require(inverse_branch && nontrivial.a == (p & 7)
          && nontrivial.b == (q & 7), "R>=2 inverse branch");

  const std::vector<u64> extreme_middle = {0, 0, 1000, 1000};
  const std::vector<u64> balanced_middle = {400, 400, 400, 400};
  require(lower_median_key(extreme_middle) == 0
          && lower_median_key(balanced_middle) == 400,
          "lower median exact convention");
  require(extreme_middle[1] + extreme_middle[2]
              > balanced_middle[1] + balanced_middle[2],
          "lower median differs from V1 raw mean witness");
  require(lower_median_key({9, 1, 5}) == 5, "odd lower median");

  require(public_sqrt_center(N, B, 19) == 15,
          "product surrogate floor-sqrt regression");
  require(static_cast<u128>(19) * 19 * N
              > static_cast<u128>(1984) * 1984,
          "real-sqrt alternative regression differs");

  require(conservative_parallel_seconds(12.0, 1) == 16.0
          && conservative_parallel_seconds(12.0, 2) == 8.0
          && conservative_parallel_seconds(12.0, 8) == 2.0,
          "worker-aware 75-percent projection");
  require(!EXECUTES_FACTOR_BANK
          && std::string(ORACLE_HIT_COLUMNS).find("oracle_hit_n")
                 != std::string::npos
          && std::string(ORACLE_HIT_SEMANTICS)
                 == "hidden_label_true_carry_not_executed_factor_bank",
          "oracle-hit and no-bank-execution contract");

  bool saw_tie = false, saw_negative = false;
  for (u64 u = 1; u <= 3 * B; ++u) {
    const auto point = carry_point(p, q, N, B, H, u);
    saw_tie |= point.tie_p || point.tie_q;
    saw_negative |= point.c < 0;
    for (int t = 0; t <= n / 2; ++t) {
      const u64 R = 1ULL << t;
      const PrefixData prefix = prefix_data(N, p, R);
      const u64 a = prefix.a, b = prefix.b;
      const s128 rhs = static_cast<s128>(u128(u) * u * H
                                        + u128(point.kp) * point.kq * B)
                       - static_cast<s128>(u) * (static_cast<s128>(point.kp) * b
                                                 + static_cast<s128>(point.kq) * a);
      require((point.c - rhs) % static_cast<s128>(u * R) == 0,
              "prefix carry congruence");
    }
  }
  require(saw_tie && saw_negative, "tie and negative-carry self-test");

  for (s128 lo = -25; lo <= 25; ++lo) for (s128 hi = lo; hi <= 25; ++hi)
    for (s128 R = 1; R <= 11; ++R) for (s128 residue = -13; residue <= 13; ++residue) {
      u64 brute = 0;
      for (s128 x = lo; x <= hi; ++x) if ((x - residue) % R == 0) ++brute;
      const s128 first = residue + ceil_div(lo - residue, R) * R;
      const u64 direct = first > hi ? 0 : static_cast<u64>(floor_div(hi - first, R) + 1);
      require(brute == direct, "signed residue enumeration");
    }

  const auto point = carry_point(p, q, N, B, H, 7);
  cpp_int T(string_u128(point.T));
  cpp_int Nbig(string_u128(N));
  cpp_int discriminant = T * T - cpp_int(4) * point.kp * point.kq * Nbig;
  cpp_int delta = cpp_int(point.kp) * q - cpp_int(point.kq) * p;
  require(discriminant == delta * delta, "decoder discriminant");
  require(point.kq != 0, "quadratic self-test");
  const cpp_int adelta = delta < 0 ? -delta : delta;
  require((T + adelta) % (2 * point.kq) == 0
          || (T - adelta) % (2 * point.kq) == 0,
          "quadratic integral root");

  const s128 linear_T = 7;
  const s128 linear_Kp = 1;
  require((linear_Kp * 21) % linear_T == 0
          && (linear_Kp * 21) / linear_T == 3, "linear endpoint");
  require(monomial_exponents(2).size() == 15 && monomial_exponents(3).size() == 35,
          "monomial counts");
  std::cout << "F261_V2_SELF_TEST_PASS N=" << string_u128(N)
            << " tie=1 negative=1 r1=1 median=1 product=1 workers=1 oracle=1\n";
}

static void preflight(int workers) {
  const u64 inner_iterations = 20000000ULL;
  u64 p = (1ULL << 59) + 1;
  const u64 B = 1ULL << 60;
  while (true) {
    const u64 q = inverse_power_two(p, B);
    if (q >= (1ULL << 59) && q > p && q < 2 * p) {
      const u128 N = static_cast<u128>(p) * q;
      const u64 H = static_cast<u64>((N - 1) / B);
      volatile u64 sink = 0;
      const auto start = std::chrono::steady_clock::now();
      for (u64 i = 0; i < inner_iterations; ++i) {
        const u64 u = 1 + i % U3_HARD_CAP;
        sink ^= static_cast<u64>(abs128(carry_point(p, q, N, B, H, u).c));
      }
      const double seconds = std::chrono::duration<double>(
          std::chrono::steady_clock::now() - start).count();
      const u64 frozen_evaluations = 712000000ULL;
      const double single_worker_projection =
          3.0 * seconds * frozen_evaluations / inner_iterations;
      const double inner_projection =
          conservative_parallel_seconds(single_worker_projection, workers);
      std::cout << "PREFLIGHT_INNER iterations=" << inner_iterations
                << " seconds=" << seconds << " sink=" << sink
                << " requested_workers=" << workers
                << " parallel_efficiency=" << PARALLEL_EFFICIENCY
                << " projected_scan_seconds=" << inner_projection << "\n";

      const u64 bench_attempts[COHORT_COUNT] = {2000000, 5000000, 2000000, 20000000};
      double generation_projection = 0;
      for (int cohort = 0; cohort < COHORT_COUNT; ++cohort) {
        u64 hits = 0;
        const auto gs = std::chrono::steady_clock::now();
        for (u64 serial = 0; serial < bench_attempts[cohort]; ++serial) {
          u64 bp = 0, bq = 0;
          if (pair_from_serial(60, cohort, serial,
                               COHORT_TAGS[cohort] ^ 0x42454e43484d4152ULL, bp, bq))
            ++hits;
        }
        const double elapsed = std::chrono::duration<double>(
            std::chrono::steady_clock::now() - gs).count();
        require(hits > 0, std::string("preflight zero generation hits: ")
                          + COHORT_NAMES[cohort]);
        const double rate = static_cast<double>(hits) / bench_attempts[cohort];
        generation_projection += 4.0 * elapsed / bench_attempts[cohort]
                                 * (12.0 * COHORT_SIZES[cohort] / rate);
        std::cout << "PREFLIGHT_GENERATION cohort=" << COHORT_NAMES[cohort]
                  << " attempts=" << bench_attempts[cohort] << " hits=" << hits
                  << " seconds=" << elapsed << "\n";
      }
      const double total = inner_projection + generation_projection;
      std::cout << "PREFLIGHT_PROJECTED_SECONDS conservative=" << total
                << " limit=" << MAX_PROJECTED_SECONDS << "\n";
      require(total <= MAX_PROJECTED_SECONDS,
              "preflight projection exceeds four hours");
      return;
    }
    p += 2;
  }
}

int main(int argc, char** argv) try {
  if (argc == 2 && std::string(argv[1]) == "--self-test") {
    v2_self_test();
    return 0;
  }
  if (argc == 3 && std::string(argv[1]) == "--preflight") {
    const int workers = std::stoi(argv[2]);
    require(1 <= workers && workers <= 8, "preflight worker count 1..8");
    preflight(workers);
    return 0;
  }
  require(argc == 6,
          "usage: V2_search THREADS SUMMARY_JSON ROWS_TSV INVERSE_TSV CONSECUTIVE_TSV");
  const int threads = std::stoi(argv[1]);
  require(1 <= threads && threads <= 8, "thread count 1..8");
  const auto generation_start = std::chrono::steady_clock::now();
  std::vector<std::array<u64, COHORT_COUNT>> attempts;
  const std::vector<Task> tasks = make_tasks(attempts);
  const double generation_seconds = std::chrono::duration<double>(
      std::chrono::steady_clock::now() - generation_start).count();

  std::vector<InputResult> results(tasks.size());
  std::atomic<std::size_t> next{0}, done{0};
  std::mutex output_mutex;
  const auto scan_start = std::chrono::steady_clock::now();
  auto worker = [&]() {
    for (;;) {
      const std::size_t index = next.fetch_add(1);
      if (index >= tasks.size()) return;
      results[index] = process_input(tasks[index]);
      const std::size_t completed = done.fetch_add(1) + 1;
      if (completed % 32 == 0 || completed == tasks.size()) {
        std::lock_guard<std::mutex> lock(output_mutex);
        const double elapsed = std::chrono::duration<double>(
            std::chrono::steady_clock::now() - scan_start).count();
        std::cerr << "progress=" << completed << "/" << tasks.size()
                  << " elapsed=" << std::fixed << std::setprecision(1) << elapsed
                  << "s rate=" << completed / elapsed << "/s\n";
      }
    }
  };
  std::vector<std::thread> workers;
  for (int j = 0; j < threads; ++j) workers.emplace_back(worker);
  for (auto& worker_thread : workers) worker_thread.join();
  const double scan_seconds = std::chrono::duration<double>(
      std::chrono::steady_clock::now() - scan_start).count();
  const auto selected = select_predictors(results);
  write_rows(results, argv[3]);
  write_inverse_studies(results, argv[4]);
  write_consecutive(argv[5]);
  write_summary(results, attempts, selected, generation_seconds, scan_seconds,
                threads, argv[2]);
  std::cout << "F261_D02_PASS inputs=" << results.size()
            << " generation_seconds=" << generation_seconds
            << " scan_seconds=" << scan_seconds << "\n";
  return 0;
} catch (const std::exception& e) {
  std::cerr << "F261_D02_FAIL " << e.what() << "\n";
  return 1;
}
