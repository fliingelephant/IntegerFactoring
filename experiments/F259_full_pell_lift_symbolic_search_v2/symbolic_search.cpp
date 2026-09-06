#include <algorithm>
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
#include <utility>
#include <vector>

#include <boost/multiprecision/cpp_int.hpp>

using boost::multiprecision::cpp_int;
using u64 = std::uint64_t;
using u128 = __uint128_t;

static constexpr int D_VALUES[] = {2, 3, 5, 6, 7, 10, 11, 13};
static constexpr int OFFSETS[] = {1, 2, 3, 5, 8, 13};
static constexpr int FACTOR_BITS[] = {16, 24, 32, 40, 48, 56, 60};
static constexpr int RANDOM_PER_BITS = 512;
static constexpr int NEIGHBOR_PER_BITS = 256;
static constexpr int SAFE_PER_BITS = 256;
static constexpr int SAFE_16_BITS = 128;
static constexpr int MAX_PELL_INDEX = 480;
static constexpr int PAIR_SCOPE_CAP_PER_D = 256;
static constexpr int TRIPLE_SCOPE_CAP_PER_D = 64;
static constexpr int FAMILY_COUNT = 22;
static constexpr int WORD_COUNT = 255;
static constexpr int PLANNED_INPUT_COUNT = 7040;
static constexpr int EXPECTED_TSV_COLUMNS = 634;
static constexpr u64 PREDICTED_OUTPUT_BYTES =
    u64(PLANNED_INPUT_COUNT) * 65536ULL + 33554432ULL;
static constexpr u64 COHORT_SEED = 0xf259d01c0ffee123ULL;

static const char* FAMILY_NAMES[FAMILY_COUNT] = {
    "row_ell", "row_k_control", "row_tangent_minus",
    "row_tangent_plus", "row_norm_defects", "original_q_minus",
    "original_q_plus", "multiplication_carry", "carry_norm_minus",
    "carry_norm_plus", "lift_determinants", "vector_determinants",
    "lift_resultant_minus", "lift_resultant_plus", "carry_resultants",
    "cross_lift_resultants", "collision_minus", "collision_plus",
    "triple_determinants", "first_carry_control", "second_carry_full",
    "second_carry_core"};

// Frozen typed template syntax. FAMILY_NAMES array order is the normalization
// order for commutative family products. Scope labels
// (row/edge/triple/composition) are not part of the expression template;
// distinct scopes remain distinct atoms.
static const char* FAMILY_SCHEMAS[FAMILY_COUNT] = {
    "row:scalar:ell", "row:scalar:k", "row:scalar:sub(mul(k,sub(x,1)),mul(y,ell))",
    "row:scalar:sub(mul(k,add(x,1)),mul(y,ell))",
    "row:scalar:{exact_div_N(sub(sub(pow2(x),mul(D,pow2(y))),1)),sub(pow2(ell),mul(D,pow2(k)))}",
    "edge:scalar:add(mul(D,pow2(det(pair(y_i,k_i),pair(y_j,k_j)))),pow2(sub(k_i,k_j)))",
    "edge:scalar:add(mul(D,pow2(det(pair(y_i,k_i),pair(y_j,k_j)))),pow2(add(k_i,k_j)))",
    "edge:scalar:{a_ij,b_ij}",
    "edge:scalar:sub(pow2(a_ij),mul(D,pow2(b_ij)))",
    "edge:scalar:add(pow2(a_ij),mul(D,pow2(b_ij)))",
    "edge:scalar:det(pair(ell_i,k_i),pair(ell_j,k_j))",
    "edge:scalar:det(each_pair({lift_i,lift_j,carry,tangent_i,tangent_j}))",
    "edge:scalar:add(mul(D,pow2(det(lift_i,lift_j))),pow2(sub(k_i,k_j)))",
    "edge:scalar:add(mul(D,pow2(det(lift_i,lift_j))),pow2(add(k_i,k_j)))",
    "edge:scalar:signed_norm(carry,each({lift_i,lift_j,tangent_i,tangent_j}))",
    "cross_edge:scalar:quadratic_resultant(each({lift,tangent}))",
    "edge:scalar:sub(each({ell,k,gminus,gplus,norm_digit})_i,same_j)",
    "edge:scalar:add(each({ell,k,gminus,gplus,norm_digit})_i,same_j)",
    "triple:scalar:{det3(each3of4(ell,k,gminus,gplus)),affine_det,carries_affine_det}",
    "composition:scalar:mul(mul(D,c),add(mul(2,z),mul(c,N)))",
    "composition:scalar:exact_div_N2(second_finite_difference(F_outer,z,cN))",
    "composition:scalar:{core3(3*z+c*N),core5(B5(z,c,N,D)),route_sum,route_difference}"};

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

struct Rng {
  u64 state;
  explicit Rng(u64 seed) : state(seed) {}
  u64 next() { return state = splitmix64(state); }
};

static u64 mul_mod(u64 a, u64 b, u64 modulus) {
  if (modulus == 1) return 0;
  return static_cast<u64>((static_cast<u128>(a) * b) % modulus);
}

static u64 add_mod(u64 a, u64 b, u64 modulus) {
  if (modulus == 1) return 0;
  return static_cast<u64>((static_cast<u128>(a) + b) % modulus);
}

static u64 sub_mod(u64 a, u64 b, u64 modulus) {
  if (modulus == 1) return 0;
  return a >= b ? a - b
                : static_cast<u64>(static_cast<u128>(a) + modulus - b);
}

static u64 pow_mod(u64 base, u64 exponent, u64 modulus) {
  if (modulus == 1) return 0;
  u64 result = 1 % modulus;
  while (exponent) {
    if (exponent & 1) result = mul_mod(result, base, modulus);
    base = mul_mod(base, base, modulus);
    exponent >>= 1;
  }
  return result;
}

static bool is_prime(u64 value) {
  if (value < 2) return false;
  for (u64 prime : {2ULL, 3ULL, 5ULL, 7ULL, 11ULL, 13ULL, 17ULL, 19ULL,
                    23ULL, 29ULL, 31ULL, 37ULL}) {
    if (value % prime == 0) return value == prime;
  }
  u64 odd = value - 1, shift = 0;
  while ((odd & 1) == 0) {
    odd >>= 1;
    ++shift;
  }
  for (u64 base : {2ULL, 325ULL, 9375ULL, 28178ULL, 450775ULL,
                   9780504ULL, 1795265022ULL}) {
    if (base % value == 0) continue;
    u64 residue = pow_mod(base % value, odd, value);
    if (residue == 1 || residue == value - 1) continue;
    bool composite = true;
    for (u64 round = 1; round < shift; ++round) {
      residue = mul_mod(residue, residue, value);
      if (residue == value - 1) {
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
  const u64 mask = (1ULL << bits) - 1;
  for (int restart = 0; restart < 1000000; ++restart) {
    u64 value = (rng.next() & mask) | low | 1ULL;
    for (int step = 0; step < 8192 && value <= mask; ++step, value += 2)
      if (is_prime(value)) return value;
  }
  fail("prime generation exhausted");
}

static u64 random_safe_prime(int bits, Rng& rng) {
  for (int attempt = 0; attempt < 1000000; ++attempt) {
    u64 half = random_prime(bits - 1, rng);
    u64 value = 2 * half + 1;
    if ((value >> (bits - 1)) == 1 && is_prime(value)) return value;
  }
  fail("safe-prime generation exhausted");
}

static u64 next_prime_same_bits(u64 value, int bits) {
  const u64 limit = 1ULL << bits;
  for (int attempt = 0; attempt < 1000000; ++attempt) {
    value += 2;
    if (value >= limit) return 0;
    if (is_prime(value)) return value;
  }
  return 0;
}

static int bit_length(const cpp_int& value) {
  require(value > 0, "positive bit length");
  return boost::multiprecision::msb(value) + 1;
}

static u64 mod_cpp(const cpp_int& value, u64 modulus) {
  if (modulus == 1) return 0;
  cpp_int residue = value % modulus;
  if (residue < 0) residue += modulus;
  return residue.convert_to<u64>();
}

static std::string cpp_string(const cpp_int& value) {
  return value.convert_to<std::string>();
}

static std::string json_escape(const std::string& value) {
  std::ostringstream escaped;
  for (unsigned char byte : value) {
    switch (byte) {
      case '\\': escaped << "\\\\"; break;
      case '"': escaped << "\\\""; break;
      case '\b': escaped << "\\b"; break;
      case '\f': escaped << "\\f"; break;
      case '\n': escaped << "\\n"; break;
      case '\r': escaped << "\\r"; break;
      case '\t': escaped << "\\t"; break;
      default:
        if (byte < 0x20)
          escaped << "\\u00" << std::hex << std::setw(2)
                  << std::setfill('0') << static_cast<int>(byte) << std::dec;
        else
          escaped << byte;
    }
  }
  return escaped.str();
}

static cpp_int abs_cpp(const cpp_int& value) { return value < 0 ? -value : value; }

static cpp_int gcd_cpp(cpp_int left, cpp_int right) {
  left = abs_cpp(left);
  right = abs_cpp(right);
  while (right != 0) {
    cpp_int remainder = left % right;
    left = right;
    right = remainder;
  }
  return left;
}

static cpp_int primitive_n(cpp_int value, const cpp_int& modulus,
                           u64& removed_powers) {
  value = abs_cpp(value);
  removed_powers = 0;
  if (value == 0) return 0;
  while (value % modulus == 0) {
    value /= modulus;
    ++removed_powers;
  }
  return value;
}

static u64 low64(const cpp_int& value) {
  static const cpp_int mask = (cpp_int(1) << 64) - 1;
  return (value & mask).convert_to<u64>();
}

struct PellFundamental {
  int D;
  cpp_int S;
  cpp_int T;
  std::vector<cpp_int> S_values;
  std::vector<cpp_int> T_values;
};

static PellFundamental fundamental_pell(int D) {
  int root = static_cast<int>(std::sqrt(D));
  require(root * root != D, "nonsquare D");
  int m = 0, den = 1, a = root;
  cpp_int p0 = 1, p1 = a, q0 = 0, q1 = 1;
  while (p1 * p1 - D * q1 * q1 != 1) {
    m = den * a - m;
    den = (D - m * m) / den;
    a = (root + m) / den;
    cpp_int np = a * p1 + p0;
    cpp_int nq = a * q1 + q0;
    p0 = p1;
    p1 = np;
    q0 = q1;
    q1 = nq;
  }
  return {D, p1, q1, {}, {}};
}

static void populate(PellFundamental& fund) {
  fund.S_values.assign(MAX_PELL_INDEX + 1, 0);
  fund.T_values.assign(MAX_PELL_INDEX + 1, 0);
  fund.S_values[0] = 1;
  cpp_int S = 1, T = 0;
  for (int index = 1; index <= MAX_PELL_INDEX; ++index) {
    cpp_int nextS = fund.S * S + fund.D * fund.T * T;
    cpp_int nextT = fund.S * T + fund.T * S;
    S = nextS;
    T = nextT;
    require(S * S - fund.D * T * T == 1, "Pell recurrence");
    fund.S_values[index] = S;
    fund.T_values[index] = T;
  }
}

struct Row {
  int j;
  cpp_int S, T, x, y, ell, k, gminus, gplus, norm_digit, lift_norm;
};

static Row make_row(int index, const cpp_int& S, const cpp_int& T,
                    const cpp_int& N, int D) {
  Row row;
  row.j = index;
  row.S = S;
  row.T = T;
  row.ell = S / N;
  row.x = S % N;
  row.k = T / N;
  row.y = T % N;
  cpp_int numerator = row.x * row.x - D * row.y * row.y - 1;
  require(numerator % N == 0, "norm digit integral");
  row.norm_digit = numerator / N;
  row.lift_norm = row.ell * row.ell - D * row.k * row.k;
  require(row.norm_digit ==
              -2 * (row.x * row.ell - D * row.y * row.k) - N * row.lift_norm,
          "lifted norm identity");
  row.gminus = row.k * (row.x - 1) - row.y * row.ell;
  row.gplus = row.k * (row.x + 1) - row.y * row.ell;
  require(row.gplus - row.gminus == 2 * row.k, "tangent difference");
  require(row.gplus + row.gminus == 2 * (row.k * row.x - row.y * row.ell),
          "tangent sum");
  return row;
}

struct Pair {
  cpp_int a, b;
};

static cpp_int determinant(const Pair& left, const Pair& right) {
  return left.a * right.b - left.b * right.a;
}

static cpp_int determinant3(const cpp_int& a0, const cpp_int& a1,
                            const cpp_int& a2, const cpp_int& b0,
                            const cpp_int& b1, const cpp_int& b2,
                            const cpp_int& c0, const cpp_int& c1,
                            const cpp_int& c2) {
  return a0 * (b1 * c2 - b2 * c1) - a1 * (b0 * c2 - b2 * c0) +
         a2 * (b0 * c1 - b1 * c0);
}

static std::pair<cpp_int, cpp_int> signed_norms(int D, const Pair& left,
                                                const Pair& right) {
  cpp_int delta = determinant(left, right);
  cpp_int base = D * delta * delta;
  return {base + (left.b - right.b) * (left.b - right.b),
          base + (left.b + right.b) * (left.b + right.b)};
}

static cpp_int resultant(int D, const Pair& left, int E, const Pair& right) {
  cpp_int delta = determinant(left, right);
  cpp_int center = D * E * delta * delta + E * left.b * left.b +
                   D * right.b * right.b;
  return center * center - 4 * D * E * left.b * left.b * right.b * right.b;
}

static Pair multiplication_carry(const Row& left, const Row& right,
                                 const Row& target, const cpp_int& N, int D) {
  cpp_int anum = left.x * right.x + D * left.y * right.y - target.x;
  cpp_int bnum = left.x * right.y + left.y * right.x - target.y;
  require(anum % N == 0 && bnum % N == 0, "multiplication carry integral");
  Pair carry{anum / N, bnum / N};
  require(target.ell ==
              carry.a + left.x * right.ell + right.x * left.ell +
                  D * (left.y * right.k + right.y * left.k) +
                  N * (left.ell * right.ell + D * left.k * right.k),
          "S lift multiplication");
  require(target.k ==
              carry.b + left.x * right.k + right.x * left.k +
                  left.y * right.ell + right.y * left.ell +
                  N * (left.ell * right.k + left.k * right.ell),
          "T lift multiplication");
  return carry;
}

static cpp_int odd_f(int D, int multiplier, const cpp_int& y) {
  if (multiplier == 3) return 3 * y + 4 * D * y * y * y;
  require(multiplier == 5, "frozen odd multiplier");
  cpp_int y2 = y * y;
  return 5 * y + 20 * D * y2 * y + 16 * D * D * y2 * y2 * y;
}

static cpp_int odd_f_derivative(int D, int multiplier, const cpp_int& y) {
  if (multiplier == 3) return 3 + 12 * D * y * y;
  require(multiplier == 5, "frozen odd derivative");
  cpp_int y2 = y * y;
  return 5 + 60 * D * y2 + 80 * D * D * y2 * y2;
}

static cpp_int second_carry_core(int D, int outer, const cpp_int& z,
                                 const cpp_int& carry, const cpp_int& N) {
  if (outer == 3) return 3 * z + carry * N;
  require(outer == 5, "frozen second-carry core");
  cpp_int z2 = z * z;
  cpp_int carry2 = carry * carry;
  cpp_int N2 = N * N;
  return 5 * (3 * z + carry * N) +
         4 * D * (10 * z2 * z + 10 * z2 * carry * N +
                  5 * z * carry2 * N2 + carry2 * carry * N2 * N);
}

struct Task {
  int factor_bits;
  int cohort;
  int index;
  u64 p, q;
};

struct InputResult {
  Task task;
  cpp_int N;
  int n;
  u64 residual[2];
  u64 captured[WORD_COUNT][2];
  u64 atom_count[FAMILY_COUNT]{};
  u64 zero_count[FAMILY_COUNT]{};
  u64 unit_count[FAMILY_COUNT]{};
  u64 n_power_count[FAMILY_COUNT]{};
  u64 direct_count[FAMILY_COUNT]{};
  u64 cleanup_events = 0;
  bool cleanup_free = false;
  bool strict = false;
  std::string first_certificate;
};

static void record_cleanup(InputResult& output, const cpp_int& divisor,
                           const std::string& tag) {
  if (divisor <= 1 || divisor >= output.N) return;
  ++output.cleanup_events;
  if (output.cleanup_events == 1)
    output.first_certificate =
        "cleanup:" + tag + ":factor=" + cpp_string(divisor);
}

static const char* cohort_name(int cohort) {
  return cohort == 0 ? "random" : cohort == 1 ? "consecutive" : "safe-safe";
}

static std::pair<u64, u64> generate_pair(const Task& task, u64 attempt) {
  u64 seed = splitmix64(COHORT_SEED ^ (static_cast<u64>(task.factor_bits) << 48) ^
                        (static_cast<u64>(task.cohort) << 40) ^
                        (static_cast<u64>(task.index) << 8) ^ attempt);
  Rng rng(seed);
  u64 p, q;
  if (task.cohort == 2) {
    p = random_safe_prime(task.factor_bits, rng);
    q = random_safe_prime(task.factor_bits, rng);
  } else if (task.cohort == 1) {
    p = random_prime(task.factor_bits, rng);
    q = next_prime_same_bits(p, task.factor_bits);
    if (q == 0) return {0, 0};
  } else {
    p = random_prime(task.factor_bits, rng);
    q = random_prime(task.factor_bits, rng);
  }
  if (p > q) std::swap(p, q);
  if (p == q || q >= 2 * p) return {0, 0};
  return {p, q};
}

static std::vector<Task> make_tasks() {
  std::vector<Task> tasks;
  for (int bits : FACTOR_BITS) {
    std::set<std::pair<u64, u64>> seen;
    for (int cohort = 0; cohort < 3; ++cohort) {
      int count = cohort == 0 ? RANDOM_PER_BITS
                 : cohort == 1 ? NEIGHBOR_PER_BITS
                 : bits == 16  ? SAFE_16_BITS
                               : SAFE_PER_BITS;
      for (int index = 0; index < count; ++index) {
        Task task{bits, cohort, index, 0, 0};
        for (u64 attempt = 0;; ++attempt) {
          require(attempt < 1000000, "cohort generation exhausted");
          auto pair = generate_pair(task, attempt);
          if (pair.first == 0 || !seen.insert(pair).second) continue;
          task.p = pair.first;
          task.q = pair.second;
          tasks.push_back(task);
          break;
        }
      }
    }
  }
  require(tasks.size() == PLANNED_INPUT_COUNT, "frozen task count");
  return tasks;
}

struct AtomAccumulator {
  InputResult& result;
  const cpp_int& N;
  u64 residual[2];
  u64 product[FAMILY_COUNT][2];

  AtomAccumulator(InputResult& output, const cpp_int& modulus, u64 sp, u64 sq)
      : result(output), N(modulus), residual{sp, sq} {
    for (int family = 0; family < FAMILY_COUNT; ++family)
      for (int side = 0; side < 2; ++side)
        product[family][side] = residual[side] == 1 ? 0 : 1;
  }

  void add(int family, cpp_int value, const std::string& tag) {
    u64 removed_powers = 0;
    cpp_int primitive = primitive_n(value, N, removed_powers);
    result.n_power_count[family] += removed_powers;
    if (primitive == 0) {
      ++result.zero_count[family];
      return;
    }
    if (primitive == 1) {
      ++result.unit_count[family];
      return;
    }
    ++result.atom_count[family];
    cpp_int divisor = gcd_cpp(primitive, N);
    if (divisor > 1 && divisor < N) {
      ++result.direct_count[family];
      if (result.first_certificate.empty()) {
        std::ostringstream certificate;
        certificate << FAMILY_NAMES[family] << ":" << tag << ":factor="
                    << cpp_string(divisor) << ":atom_mod_N="
                    << cpp_string(primitive % N) << ":atom_bits="
                    << bit_length(primitive);
        result.first_certificate = certificate.str();
      }
    }
    for (int side = 0; side < 2; ++side)
      if (residual[side] > 1)
        product[family][side] =
            mul_mod(product[family][side], mod_cpp(primitive, residual[side]),
                    residual[side]);
  }
};

struct SyntheticRow {
  int D, i, j, k;
  Row ri, rj, rk, rij, rjk, rijk;
};

static std::pair<cpp_int, cpp_int> cocycle_residual(const SyntheticRow& sample,
                                                    const cpp_int& N) {
  Pair cij = multiplication_carry(sample.ri, sample.rj, sample.rij, N, sample.D);
  Pair cijk = multiplication_carry(sample.rij, sample.rk, sample.rijk, N, sample.D);
  Pair cjk = multiplication_carry(sample.rj, sample.rk, sample.rjk, N, sample.D);
  Pair c_ijk = multiplication_carry(sample.ri, sample.rjk, sample.rijk, N, sample.D);
  Pair left{cijk.a + cij.a * sample.rk.x + sample.D * cij.b * sample.rk.y,
            cijk.b + cij.a * sample.rk.y + cij.b * sample.rk.x};
  Pair right{c_ijk.a + sample.ri.x * cjk.a + sample.D * sample.ri.y * cjk.b,
             c_ijk.b + sample.ri.x * cjk.b + sample.ri.y * cjk.a};
  return {left.a - right.a, left.b - right.b};
}

static int modular_rank(std::vector<std::vector<u64>> matrix, u64 prime) {
  require(!matrix.empty(), "rank matrix nonempty");
  int rank = 0;
  int columns = static_cast<int>(matrix.front().size());
  for (int column = 0;
       column < columns && rank < static_cast<int>(matrix.size()); ++column) {
    int pivot = rank;
    while (pivot < static_cast<int>(matrix.size()) &&
           matrix[pivot][column] == 0)
      ++pivot;
    if (pivot == static_cast<int>(matrix.size())) continue;
    std::swap(matrix[rank], matrix[pivot]);
    u64 inverse = pow_mod(matrix[rank][column], prime - 2, prime);
    for (int c = column; c < columns; ++c)
      matrix[rank][c] = mul_mod(matrix[rank][c], inverse, prime);
    for (int row = 0; row < static_cast<int>(matrix.size()); ++row) {
      if (row == rank || matrix[row][column] == 0) continue;
      u64 multiple = matrix[row][column];
      for (int c = column; c < columns; ++c)
        matrix[row][c] =
            sub_mod(matrix[row][c],
                    mul_mod(multiple, matrix[rank][c], prime), prime);
    }
    ++rank;
  }
  return rank;
}

static std::vector<std::vector<int>> ternary_nulls(
    const std::vector<std::vector<u64>>& matrix, u64 prime) {
  require(!matrix.empty() && matrix.front().size() == 12,
          "frozen ternary basis");
  constexpr u64 total = 531441;  // 3^12
  std::vector<std::vector<int>> nulls;
  for (u64 code = 0; code < total; ++code) {
    u64 digits = code;
    std::vector<int> coefficients(12);
    int first_nonzero = 0;
    for (int column = 0; column < 12; ++column) {
      coefficients[column] = static_cast<int>(digits % 3) - 1;
      digits /= 3;
      if (first_nonzero == 0 && coefficients[column] != 0)
        first_nonzero = coefficients[column];
    }
    if (first_nonzero <= 0) continue;
    bool null = true;
    for (const auto& row : matrix) {
      u64 value = 0;
      for (int column = 0; column < 12; ++column) {
        if (coefficients[column] == 1)
          value = add_mod(value, row[column], prime);
        else if (coefficients[column] == -1)
          value = sub_mod(value, row[column], prime);
      }
      if (value != 0) {
        null = false;
        break;
      }
    }
    if (null) nulls.push_back(std::move(coefficients));
  }
  std::sort(nulls.begin(), nulls.end());
  return nulls;
}

// Public synthetic identity mining. The frozen basis is exactly the twelve
// additive scalar terms in the two displayed cocycle coordinates. All
// normalized {-1,0,1} null vectors are enumerated, and disjoint exact samples
// authenticate them before the two disjoint-support controls are retained as
// the primitive basis.
static std::string mine_identities(const std::vector<PellFundamental>& funds) {
  constexpr u64 prime = 1000000007ULL;
  constexpr int columns = 12;
  std::vector<std::vector<u64>> matrix;
  auto monomials = [](const SyntheticRow& sample, const cpp_int& N) {
    Pair cij = multiplication_carry(sample.ri, sample.rj, sample.rij, N, sample.D);
    Pair cijk = multiplication_carry(sample.rij, sample.rk, sample.rijk, N, sample.D);
    Pair cjk = multiplication_carry(sample.rj, sample.rk, sample.rjk, N, sample.D);
    Pair c_ijk = multiplication_carry(sample.ri, sample.rjk, sample.rijk, N, sample.D);
    return std::vector<cpp_int>{
        cijk.a, cij.a * sample.rk.x, sample.D * cij.b * sample.rk.y,
        -c_ijk.a, -sample.ri.x * cjk.a, -sample.D * sample.ri.y * cjk.b,
        cijk.b, cij.a * sample.rk.y, cij.b * sample.rk.x,
        -c_ijk.b, -sample.ri.x * cjk.b, -sample.ri.y * cjk.a};
  };
  for (int sample_index = 0; sample_index < 96; ++sample_index) {
    cpp_int N = 1000003 + 2 * sample_index;
    int di = sample_index % 8;
    int i = 1 + sample_index % 7;
    int j = 2 + (sample_index * 3) % 9;
    int k = 1 + (sample_index * 5) % 8;
    const auto& fund = funds[di];
    SyntheticRow sample{fund.D, i, j, k,
                        make_row(i, fund.S_values[i], fund.T_values[i], N, fund.D),
                        make_row(j, fund.S_values[j], fund.T_values[j], N, fund.D),
                        make_row(k, fund.S_values[k], fund.T_values[k], N, fund.D),
                        make_row(i + j, fund.S_values[i + j], fund.T_values[i + j], N, fund.D),
                        make_row(j + k, fund.S_values[j + k], fund.T_values[j + k], N, fund.D),
                        make_row(i + j + k, fund.S_values[i + j + k], fund.T_values[i + j + k], N, fund.D)};
    auto values = monomials(sample, N);
    std::vector<u64> row;
    for (const auto& value : values) row.push_back(mod_cpp(value, prime));
    matrix.push_back(std::move(row));
  }
  int rank = modular_rank(matrix, prime);
  require(rank == 10, "unexpected cocycle rank");
  std::vector<std::vector<int>> nulls = ternary_nulls(matrix, prime);
  std::vector<int> real(columns, 0), imag(columns, 0);
  for (int column = 0; column < 6; ++column) real[column] = 1;
  for (int column = 6; column < 12; ++column) imag[column] = 1;
  std::vector<int> sum(columns), difference(columns);
  for (int column = 0; column < columns; ++column) {
    sum[column] = real[column] + imag[column];
    difference[column] = real[column] - imag[column];
  }
  std::vector<std::vector<int>> expected{real, imag, sum, difference};
  std::sort(expected.begin(), expected.end());
  require(nulls == expected, "unexpected ternary cocycle relation");

  for (const auto& coefficients : nulls)
    for (int holdout = 0; holdout < 64; ++holdout) {
      int sample_index = 96 + holdout;
      cpp_int N = 2000003 + 2 * holdout;
      int di = sample_index % 8;
      int i = 2 + sample_index % 8;
      int j = 1 + (sample_index * 3) % 7;
      int k = 2 + (sample_index * 5) % 9;
      const auto& fund = funds[di];
      SyntheticRow sample{
          fund.D, i, j, k,
          make_row(i, fund.S_values[i], fund.T_values[i], N, fund.D),
          make_row(j, fund.S_values[j], fund.T_values[j], N, fund.D),
          make_row(k, fund.S_values[k], fund.T_values[k], N, fund.D),
          make_row(i + j, fund.S_values[i + j], fund.T_values[i + j], N,
                   fund.D),
          make_row(j + k, fund.S_values[j + k], fund.T_values[j + k], N,
                   fund.D),
          make_row(i + j + k, fund.S_values[i + j + k],
                   fund.T_values[i + j + k], N, fund.D)};
      auto values = monomials(sample, N);
      cpp_int total = 0;
      for (int column = 0; column < columns; ++column)
        total += coefficients[column] * values[column];
      require(total == 0, "held-out cocycle authentication");
    }
  std::ostringstream output;
  output << "prime=" << prime << ",samples=96,holdout=64,columns=" << columns
         << ",rank=" << rank << ",nullity=" << columns - rank
         << ",ternary_nulls=" << nulls.size()
         << ",primitive_controls=2,cocycle_real=1,cocycle_imag=1";
  return output.str();
}

static InputResult process_input(const Task& task,
                                 const std::vector<PellFundamental>& funds) {
  InputResult output;
  output.task = task;
  output.N = cpp_int(task.p) * task.q;
  output.n = bit_length(output.N);
  u64 common = std::gcd(task.p - 1, task.q - 1);
  output.residual[0] = (task.p - 1) / common;
  output.residual[1] = (task.q - 1) / common;
  AtomAccumulator atoms(output, output.N, output.residual[0], output.residual[1]);
  int limit = 4 * output.n;
  require(limit <= MAX_PELL_INDEX, "Pell window");
  std::vector<std::vector<Row>> raw(8, std::vector<Row>(limit + 1));
  std::vector<std::map<int, Row>> kept(8);

  for (int di = 0; di < 8; ++di) {
    const int D = D_VALUES[di];
    cpp_int Dgcd = gcd_cpp(D, output.N);
    if (Dgcd > 1 && Dgcd < output.N) {
      record_cleanup(output, Dgcd, "D=" + std::to_string(D));
      continue;
    }
    std::map<cpp_int, Row> first_y;
    for (int index = 1; index <= limit; ++index) {
      Row row = make_row(index, funds[di].S_values[index],
                         funds[di].T_values[index], output.N, D);
      raw[di][index] = row;
      cpp_int root_gcd = gcd_cpp(row.x, output.N);
      if (root_gcd != 1) {
        record_cleanup(output, root_gcd,
                       "supplied_root:D=" + std::to_string(D) +
                           ":j=" + std::to_string(index));
        continue;
      }
      cpp_int value = 1 + D * row.y * row.y;
      require(row.x * row.x % output.N == value % output.N, "supplied root");
      cpp_int root = sqrt(value);
      if (root * root == value) {
        cpp_int minus = gcd_cpp(root - row.x, output.N);
        cpp_int plus = gcd_cpp(root + row.x, output.N);
        record_cleanup(output, minus,
                       "exact_square_minus:D=" + std::to_string(D) +
                           ":j=" + std::to_string(index));
        record_cleanup(output, plus,
                       "exact_square_plus:D=" + std::to_string(D) +
                           ":j=" + std::to_string(index));
        continue;
      }
      auto found = first_y.find(row.y);
      if (found != first_y.end()) {
        cpp_int minus = gcd_cpp(row.x - found->second.x, output.N);
        cpp_int plus = gcd_cpp(row.x + found->second.x, output.N);
        std::string indices = ":j=" + std::to_string(found->second.j) + "," +
                              std::to_string(index);
        record_cleanup(output, minus,
                       "repeated_y_minus:D=" + std::to_string(D) + indices);
        record_cleanup(output, plus,
                       "repeated_y_plus:D=" + std::to_string(D) + indices);
        continue;
      }
      first_y.emplace(row.y, row);
      if (row.k == 0) continue;
      kept[di].emplace(index, row);
      atoms.add(0, row.ell, "row_ell");
      atoms.add(1, row.k, "row_k");
      atoms.add(2, row.gminus, "row_gminus");
      atoms.add(3, row.gplus, "row_gplus");
      atoms.add(4, row.norm_digit, "row_norm_digit");
      atoms.add(4, row.lift_norm, "row_lift_norm");
    }
  }

  auto add_pair = [&](int di, const Row& left, const Row& right) {
    int D = D_VALUES[di];
    const Row& target = raw[di][left.j + right.j];
    Pair carry = multiplication_carry(left, right, target, output.N, D);
    auto original = signed_norms(D, {left.y, left.k}, {right.y, right.k});
    auto lift = signed_norms(D, {left.ell, left.k}, {right.ell, right.k});
    atoms.add(5, original.first, "original_minus");
    atoms.add(6, original.second, "original_plus");
    atoms.add(7, carry.a, "carry_a");
    atoms.add(7, carry.b, "carry_b");
    atoms.add(8, carry.a * carry.a - D * carry.b * carry.b, "carry_norm_minus");
    atoms.add(9, carry.a * carry.a + D * carry.b * carry.b, "carry_norm_plus");
    Pair Li{left.ell, left.k}, Lj{right.ell, right.k};
    Pair Gi{left.gminus, left.gplus}, Gj{right.gminus, right.gplus};
    atoms.add(10, determinant(Li, Lj), "lift_det");
    atoms.add(12, lift.first, "lift_res_minus");
    atoms.add(13, lift.second, "lift_res_plus");
    std::vector<Pair> vectors{Li, Lj, carry, Gi, Gj};
    for (int i = 0; i < 5; ++i)
      for (int j = i + 1; j < 5; ++j)
        atoms.add(11, determinant(vectors[i], vectors[j]), "vector_det");
    for (Pair vector : {Li, Lj, Gi, Gj}) {
      auto factors = signed_norms(D, carry, vector);
      atoms.add(14, factors.first, "carry_resultant_minus");
      atoms.add(14, factors.second, "carry_resultant_plus");
    }
    std::vector<cpp_int> lf{left.ell, left.k, left.gminus, left.gplus,
                            left.norm_digit};
    std::vector<cpp_int> rf{right.ell, right.k, right.gminus, right.gplus,
                            right.norm_digit};
    for (int index = 0; index < 5; ++index) {
      atoms.add(16, lf[index] - rf[index], "collision_minus");
      atoms.add(17, lf[index] + rf[index], "collision_plus");
    }
  };

  for (int di = 0; di < 8; ++di) {
    std::set<std::pair<int, int>> edges;
    for (const auto& item : kept[di]) {
      int index = item.first;
      for (int offset : OFFSETS)
        if (kept[di].count(index + offset) && 2 * index + offset <= limit)
          edges.insert({index, index + offset});
      for (int multiplier : {3, 5})
        if (kept[di].count(multiplier * index) &&
            (multiplier + 1) * index <= limit)
          edges.insert({index, multiplier * index});
    }
    std::vector<std::pair<int, int>> selected_edges(edges.begin(), edges.end());
    const u64 public_key = low64(output.N) ^
                           (static_cast<u64>(D_VALUES[di]) << 56) ^
                           0x259ed9e5a11ce123ULL;
    std::sort(selected_edges.begin(), selected_edges.end(), [&](auto left, auto right) {
      auto priority = [&](auto edge) {
        return splitmix64(public_key ^ (static_cast<u64>(edge.first) << 32) ^
                          static_cast<u64>(edge.second));
      };
      u64 lp = priority(left), rp = priority(right);
      return lp != rp ? lp < rp : left < right;
    });
    if (selected_edges.size() > PAIR_SCOPE_CAP_PER_D)
      selected_edges.resize(PAIR_SCOPE_CAP_PER_D);
    for (auto edge : selected_edges)
      add_pair(di, kept[di].at(edge.first), kept[di].at(edge.second));

    std::set<std::tuple<int, int, int>> triples;
    for (const auto& item : kept[di]) {
      int j = item.first;
      for (auto triple : {std::make_tuple(j, j + 1, j + 2),
                          std::make_tuple(j, j + 2, j + 5),
                          std::make_tuple(j, 2 * j, 3 * j)}) {
        int a, b, c;
        std::tie(a, b, c) = triple;
        if (a != b && b != c && a != c && a + b + c <= limit && kept[di].count(a) &&
            kept[di].count(b) && kept[di].count(c))
          triples.insert(triple);
      }
    }
    std::vector<std::tuple<int, int, int>> selected_triples(triples.begin(), triples.end());
    std::sort(selected_triples.begin(), selected_triples.end(), [&](auto left, auto right) {
      auto priority = [&](auto triple) {
        int a, b, c;
        std::tie(a, b, c) = triple;
        return splitmix64(public_key ^ 0x7a1f1e5c0c0a2026ULL ^
                          (static_cast<u64>(a) << 40) ^
                          (static_cast<u64>(b) << 20) ^ static_cast<u64>(c));
      };
      u64 lp = priority(left), rp = priority(right);
      return lp != rp ? lp < rp : left < right;
    });
    if (selected_triples.size() > TRIPLE_SCOPE_CAP_PER_D)
      selected_triples.resize(TRIPLE_SCOPE_CAP_PER_D);
    for (auto triple : selected_triples) {
      int i, j, k;
      std::tie(i, j, k) = triple;
      const Row &a = kept[di].at(i), &b = kept[di].at(j), &c = kept[di].at(k);
      std::vector<std::vector<cpp_int>> columns{{a.ell, b.ell, c.ell},
                                                {a.k, b.k, c.k},
                                                {a.gminus, b.gminus, c.gminus},
                                                {a.gplus, b.gplus, c.gplus}};
      for (int omit = 0; omit < 4; ++omit) {
        std::vector<int> chosen;
        for (int col = 0; col < 4; ++col)
          if (col != omit) chosen.push_back(col);
        atoms.add(18,
                  determinant3(columns[chosen[0]][0], columns[chosen[1]][0],
                               columns[chosen[2]][0], columns[chosen[0]][1],
                               columns[chosen[1]][1], columns[chosen[2]][1],
                               columns[chosen[0]][2], columns[chosen[1]][2],
                               columns[chosen[2]][2]),
                  "triple_linear");
      }
      for (auto pair : {std::make_pair(0, 1), std::make_pair(0, 2),
                        std::make_pair(1, 3), std::make_pair(2, 3)})
        atoms.add(18,
                  determinant3(columns[pair.first][0], columns[pair.second][0], 1,
                               columns[pair.first][1], columns[pair.second][1], 1,
                               columns[pair.first][2], columns[pair.second][2], 1),
                  "triple_affine");
      Pair cab = multiplication_carry(a, b, raw[di][i + j], output.N, D_VALUES[di]);
      Pair cbc = multiplication_carry(b, c, raw[di][j + k], output.N, D_VALUES[di]);
      Pair cac = multiplication_carry(a, c, raw[di][i + k], output.N, D_VALUES[di]);
      atoms.add(18,
                determinant3(cab.a, cab.b, 1, cbc.a, cbc.b, 1, cac.a, cac.b, 1),
                "triple_carry_affine");
      auto cocycle = cocycle_residual(
          {D_VALUES[di], i, j, k, a, b, c, raw[di][i + j], raw[di][j + k],
           raw[di][i + j + k]},
          output.N);
      require(cocycle.first == 0 && cocycle.second == 0, "cocycle identity");
    }

    for (const auto& item : kept[di]) {
      const Row& row = item.second;
      std::map<std::pair<int, int>, cpp_int> cores;
      for (int inner : {3, 5}) {
        if (inner * row.j > limit) continue;
        cpp_int z = raw[di][inner * row.j].y;
        cpp_int f = odd_f(D_VALUES[di], inner, row.y);
        require((f - z) % output.N == 0 && f >= z, "first carry");
        cpp_int carry = (f - z) / output.N;
        cpp_int first =
            D_VALUES[di] * carry * (2 * z + carry * output.N);
        atoms.add(19, first, "first_carry");
        for (int outer : {3, 5}) {
          if (outer * inner * row.j > limit) continue;
          cpp_int numerator = odd_f(D_VALUES[di], outer, z + carry * output.N) -
                              odd_f(D_VALUES[di], outer, z) -
                              carry * output.N *
                                  odd_f_derivative(D_VALUES[di], outer, z);
          require(numerator % (output.N * output.N) == 0,
                  "second carry quotient");
          cpp_int curvature = numerator / (output.N * output.N);
          atoms.add(20, curvature, "second_carry_full");
          cpp_int core = second_carry_core(D_VALUES[di], outer, z, carry,
                                           output.N);
          require(curvature ==
                      4 * D_VALUES[di] * carry * carry * core,
                  "second carry core identity");
          cores[{outer, inner}] = core;
          atoms.add(21, core, "second_carry_core");
        }
      }
      if (cores.count({5, 3}) && cores.count({3, 5})) {
        atoms.add(21, cores[{5, 3}] - cores[{3, 5}], "second_carry_route_diff");
        atoms.add(21, cores[{5, 3}] + cores[{3, 5}], "second_carry_route_sum");
      }
    }
  }

  for (int index = 1; index <= limit; ++index)
    for (int di = 0; di < 8; ++di) {
      if (!kept[di].count(index)) continue;
      for (int dj = di + 1; dj < 8; ++dj) {
        if (!kept[dj].count(index)) continue;
        const Row &left = kept[di].at(index), &right = kept[dj].at(index);
        atoms.add(15,
                  resultant(D_VALUES[di], {left.ell, left.k}, D_VALUES[dj],
                            {right.ell, right.k}),
                  "cross_lift_resultant");
        atoms.add(15,
                  resultant(D_VALUES[di], {left.gminus, left.gplus},
                            D_VALUES[dj], {right.gminus, right.gplus}),
                  "cross_tangent_resultant");
      }
    }

  u64 bases[WORD_COUNT][2]{};
  int word = 0;
  for (int side = 0; side < 2; ++side)
    bases[word][side] = output.residual[side] == 1
                            ? 0
                            : mod_cpp(output.N - 1, output.residual[side]);
  ++word;
  for (int family = 0; family < FAMILY_COUNT; ++family, ++word)
    for (int side = 0; side < 2; ++side)
      bases[word][side] = output.residual[side] == 1
                              ? 0
                              : mul_mod(bases[0][side], atoms.product[family][side],
                                        output.residual[side]);
  for (int first = 0; first < FAMILY_COUNT; ++first)
    for (int second = first + 1; second < FAMILY_COUNT; ++second, ++word)
      for (int side = 0; side < 2; ++side)
        bases[word][side] = output.residual[side] == 1
                                ? 0
                                : mul_mod(mul_mod(bases[0][side],
                                                  atoms.product[first][side],
                                                  output.residual[side]),
                                          atoms.product[second][side],
                                          output.residual[side]);
  for (int side = 0; side < 2; ++side) {
    bases[word][side] = bases[0][side];
    for (int family = 0; family < FAMILY_COUNT; ++family)
      if (output.residual[side] > 1)
        bases[word][side] = mul_mod(bases[word][side], atoms.product[family][side],
                                    output.residual[side]);
  }
  ++word;
  require(word == WORD_COUNT, "word count");
  for (int candidate = 0; candidate < WORD_COUNT; ++candidate)
    for (int side = 0; side < 2; ++side) {
      u64 residual = output.residual[side];
      output.captured[candidate][side] =
          residual == 1
              ? 1
              : std::gcd(pow_mod(bases[candidate][side], output.n, residual),
                         residual);
    }
  u64 grammar_events = 0;
  for (u64 count : output.direct_count) grammar_events += count;
  output.cleanup_free = output.cleanup_events == 0;
  output.strict = output.cleanup_free && grammar_events == 0;
  require(output.cleanup_events == 0 || !output.first_certificate.empty(),
          "cleanup certificate preserved");
  require(output.cleanup_events == 0 ||
              output.first_certificate.rfind("cleanup:", 0) == 0,
          "cleanup certificate has priority");
  return output;
}

static std::vector<std::string> word_names() {
  std::vector<std::string> names{"baseline"};
  for (const char* name : FAMILY_NAMES) names.emplace_back(name);
  for (int first = 0; first < FAMILY_COUNT; ++first)
    for (int second = first + 1; second < FAMILY_COUNT; ++second)
      names.push_back(std::string(FAMILY_NAMES[first]) + "*" +
                      FAMILY_NAMES[second]);
  names.emplace_back("all_families");
  require(names.size() == WORD_COUNT, "word names");
  return names;
}

static std::vector<std::vector<int>> word_families() {
  std::vector<std::vector<int>> result(1);
  for (int family = 0; family < FAMILY_COUNT; ++family)
    result.push_back({family});
  for (int first = 0; first < FAMILY_COUNT; ++first)
    for (int second = first + 1; second < FAMILY_COUNT; ++second)
      result.push_back({first, second});
  std::vector<int> all(FAMILY_COUNT);
  std::iota(all.begin(), all.end(), 0);
  result.push_back(std::move(all));
  require(result.size() == WORD_COUNT, "word family map");
  return result;
}

static std::vector<std::string> word_syntaxes() {
  const std::string baseline = "pow(sub(N,1),n)";
  std::vector<std::string> syntaxes{baseline};
  for (int family = 0; family < FAMILY_COUNT; ++family)
    syntaxes.push_back("pow(mul(sub(N,1)," +
                       std::string(FAMILY_SCHEMAS[family]) + "),n)");
  for (int first = 0; first < FAMILY_COUNT; ++first)
    for (int second = first + 1; second < FAMILY_COUNT; ++second)
      syntaxes.push_back("pow(mul(sub(N,1)," +
                         std::string(FAMILY_SCHEMAS[first]) + "," +
                         FAMILY_SCHEMAS[second] + "),n)");
  std::string all = "pow(mul(sub(N,1)";
  for (const char* schema : FAMILY_SCHEMAS) all += "," + std::string(schema);
  all += "),n)";
  syntaxes.push_back(std::move(all));
  require(syntaxes.size() == WORD_COUNT, "word syntaxes");
  return syntaxes;
}

static void self_test(const std::vector<PellFundamental>& funds) {
  require(is_prime(61) && is_prime(71) && !is_prime(4331), "primality");
  std::set<std::string> family_names, family_schemas;
  for (int family = 0; family < FAMILY_COUNT; ++family) {
    require(family_names.insert(FAMILY_NAMES[family]).second,
            "duplicate family name");
    require(family_schemas.insert(FAMILY_SCHEMAS[family]).second,
            "duplicate normalized family schema");
  }
  std::vector<std::string> names = word_names();
  std::vector<std::string> syntaxes = word_syntaxes();
  require(names.size() == WORD_COUNT && word_families().size() == WORD_COUNT &&
              syntaxes.size() == WORD_COUNT,
          "word grammar dimensions");
  require(std::set<std::string>(names.begin(), names.end()).size() == WORD_COUNT,
          "unique word names");
  require(std::set<std::string>(syntaxes.begin(), syntaxes.end()).size() ==
              WORD_COUNT,
          "unique word syntaxes");
  std::string identities = mine_identities(funds);
  cpp_int zero_carry = 0, test_z = 7, test_N = 15;
  require(2 * zero_carry * (2 * test_z + zero_carry * test_N) == 0,
          "zero first-carry semantics");
  require(second_carry_core(2, 3, test_z, zero_carry, test_N) == 21,
          "zero cubic core semantics");
  require(second_carry_core(2, 5, test_z, zero_carry, test_N) ==
              15 * test_z + 80 * test_z * test_z * test_z,
          "zero quintic core semantics");
  u64 stripped_powers = 0;
  require(primitive_n(cpp_int(77) * 77 * 5, cpp_int(77), stripped_powers) ==
                  5 &&
              stripped_powers == 2,
          "exact common-N stripping");
  InputResult certificate_test;
  certificate_test.N = 77;
  AtomAccumulator certificate_atoms(certificate_test, certificate_test.N, 3,
                                    5);
  certificate_atoms.add(0, 7, "test_direct_scope");
  require(certificate_test.first_certificate.rfind("row_ell:", 0) == 0,
          "direct certificate");
  record_cleanup(certificate_test, 11, "test_cleanup_scope");
  require(certificate_test.cleanup_events == 1 &&
              certificate_test.first_certificate ==
                  "cleanup:test_cleanup_scope:factor=11",
          "cleanup certificate priority");
  Task task{7, 0, 0, 61, 71};
  InputResult result = process_input(task, funds);
  require(result.N == 4331 && result.residual[0] == 6 && result.residual[1] == 7,
          "input self-test");
  u64 atom_total = 0;
  for (int family = 0; family < FAMILY_COUNT; ++family) {
    atom_total += result.atom_count[family];
    require(result.atom_count[family] + result.zero_count[family] +
                    result.unit_count[family] >
                0,
            "every family generated");
  }
  require(atom_total > 0, "nonempty grammar");
  std::cout << "SELF_TEST_PASS N=4331 families=" << FAMILY_COUNT
            << " words=" << WORD_COUNT << " atoms=" << atom_total
            << " identity_mining={" << identities << "}\n";
}

static long double quantile(std::vector<long double> values, long double q) {
  require(!values.empty(), "quantile nonempty");
  std::sort(values.begin(), values.end());
  long double position = q * (values.size() - 1);
  std::size_t low = static_cast<std::size_t>(std::floor(position));
  std::size_t high = static_cast<std::size_t>(std::ceil(position));
  if (low == high) return values[low];
  return values[low] * (high - position) + values[high] * (position - low);
}

int main(int argc, char** argv) try {
  std::vector<PellFundamental> funds;
  for (int D : D_VALUES) {
    funds.push_back(fundamental_pell(D));
    populate(funds.back());
  }
  if (argc == 2 && std::string(argv[1]) == "--describe") {
    std::cout << "F259_D02_DESCRIPTION families=" << FAMILY_COUNT
              << " words=" << WORD_COUNT
              << " planned_inputs=" << PLANNED_INPUT_COUNT
              << " tsv_columns=" << EXPECTED_TSV_COLUMNS
              << " predicted_output_bytes=" << PREDICTED_OUTPUT_BYTES
              << " max_threads=8\n";
    return 0;
  }
  if (argc == 2 && std::string(argv[1]) == "--self-test") {
    self_test(funds);
    return 0;
  }
  if (argc == 2 && std::string(argv[1]) == "--benchmark") {
    double total_seconds = 0, maximum_seconds = 0;
    u64 atoms = 0;
    int modulus_bits = 0;
    for (int repetition = 0; repetition < 3; ++repetition) {
      Task task{60, -1, repetition, (1ULL << 60) - 93,
                (1ULL << 60) - 33};
      auto started = std::chrono::steady_clock::now();
      InputResult result = process_input(task, funds);
      double seconds = std::chrono::duration<double>(
                           std::chrono::steady_clock::now() - started)
                           .count();
      total_seconds += seconds;
      maximum_seconds = std::max(maximum_seconds, seconds);
      modulus_bits = result.n;
      if (repetition == 0)
        for (u64 count : result.atom_count) atoms += count;
    }
    double projection =
        maximum_seconds * PLANNED_INPUT_COUNT / 8.0 * 1.75;
    std::cout << "BENCHMARK_PASS repetitions=3 public_synthetic_N_bits="
              << modulus_bits << " atoms_per_input=" << atoms
              << " mean_seconds=" << std::fixed << std::setprecision(6)
              << total_seconds / 3.0
              << " max_seconds=" << maximum_seconds
              << " projected_8thread_seconds_1.75x=" << projection
              << " predicted_peak_mib=512 predicted_output_bytes="
              << PREDICTED_OUTPUT_BYTES << "\n";
    return 0;
  }
  require(argc == 4, "usage: symbolic_search THREADS OUT_JSON OUT_TSV");
  int thread_count = std::stoi(argv[1]);
  require(thread_count >= 1 && thread_count <= 8, "thread count 1..8");
  std::vector<Task> tasks = make_tasks();
  std::string identity_mining = mine_identities(funds);
  std::vector<InputResult> results(tasks.size());
  std::atomic<std::size_t> next{0}, done{0};
  std::mutex io_mutex;
  auto started = std::chrono::steady_clock::now();
  auto worker = [&]() {
    for (;;) {
      std::size_t index = next.fetch_add(1);
      if (index >= tasks.size()) return;
      results[index] = process_input(tasks[index], funds);
      std::size_t completed = done.fetch_add(1) + 1;
      if (completed % 32 == 0 || completed == tasks.size()) {
        std::lock_guard<std::mutex> lock(io_mutex);
        double elapsed = std::chrono::duration<double>(
                             std::chrono::steady_clock::now() - started)
                             .count();
        std::cerr << "progress=" << completed << "/" << tasks.size()
                  << " elapsed=" << std::fixed << std::setprecision(1)
                  << elapsed << "s rate=" << completed / elapsed << "/s\n";
      }
    }
  };
  std::vector<std::thread> threads;
  for (int index = 0; index < thread_count; ++index) threads.emplace_back(worker);
  for (auto& thread : threads) thread.join();
  double elapsed = std::chrono::duration<double>(
                       std::chrono::steady_clock::now() - started)
                       .count();

  std::ofstream tsv(argv[3]);
  require(static_cast<bool>(tsv), "open TSV");
  tsv << "factor_bits\tsplit\tcohort\tindex\tp\tq\tN\tn\tsp\tsq\tcleanup_events\tcleanup_free\tstrict\tfirst_certificate";
  for (int family = 0; family < FAMILY_COUNT; ++family)
    tsv << '\t' << FAMILY_NAMES[family] << "_atoms\t" << FAMILY_NAMES[family]
        << "_zeros\t" << FAMILY_NAMES[family] << "_units\t"
        << FAMILY_NAMES[family] << "_N_powers\t" << FAMILY_NAMES[family]
        << "_direct";
  for (const std::string& name : word_names())
    tsv << '\t' << name << "_gp\t" << name << "_gq";
  tsv << '\n';
  for (const auto& result : results) {
    tsv << result.task.factor_bits << '\t'
        << (result.task.factor_bits <= 32 ? "discovery" : "heldout") << '\t'
        << cohort_name(result.task.cohort) << '\t' << result.task.index << '\t'
        << result.task.p << '\t' << result.task.q << '\t'
        << cpp_string(result.N) << '\t' << result.n << '\t'
        << result.residual[0] << '\t' << result.residual[1] << '\t'
        << result.cleanup_events << '\t' << result.cleanup_free << '\t'
        << result.strict << '\t' << result.first_certificate;
    for (int family = 0; family < FAMILY_COUNT; ++family)
      tsv << '\t' << result.atom_count[family] << '\t'
          << result.zero_count[family] << '\t' << result.unit_count[family]
          << '\t' << result.n_power_count[family] << '\t'
          << result.direct_count[family];
    for (int candidate = 0; candidate < WORD_COUNT; ++candidate)
      tsv << '\t' << result.captured[candidate][0] << '\t'
          << result.captured[candidate][1];
    tsv << '\n';
  }
  tsv.close();
  require(static_cast<bool>(tsv), "write TSV");

  std::ofstream json(argv[2]);
  require(static_cast<bool>(json), "open JSON");
  std::vector<std::string> names = word_names();
  std::vector<std::string> syntaxes = word_syntaxes();
  json << std::setprecision(18);
  json << "{\n  \"experiment\": \"F259-D02\",\n"
       << "  \"threads\": " << thread_count << ",\n"
       << "  \"elapsed_seconds\": " << elapsed << ",\n"
       << "  \"input_count\": " << results.size() << ",\n"
       << "  \"identity_mining\": \"" << identity_mining << "\",\n";
  struct RankItem {
    int candidate;
    u64 direct_events = 0;
    long double safe_quality_sum = 0, quality_sum = 0;
    u64 safe_count = 0, count = 0, saturated = 0;
  };
  std::vector<RankItem> ranking(WORD_COUNT);
  auto family_map = word_families();
  for (int candidate = 0; candidate < WORD_COUNT; ++candidate) {
    ranking[candidate].candidate = candidate;
    for (const auto& result : results) {
      if (result.task.factor_bits > 32) continue;
      long double quality = std::max(
          static_cast<long double>(result.captured[candidate][0]) /
              result.residual[0],
          static_cast<long double>(result.captured[candidate][1]) /
              result.residual[1]);
      ranking[candidate].quality_sum += quality;
      ++ranking[candidate].count;
      if (result.task.cohort == 2) {
        ranking[candidate].safe_quality_sum += quality;
        ++ranking[candidate].safe_count;
      }
      ranking[candidate].saturated +=
          result.captured[candidate][0] == result.residual[0] ||
          result.captured[candidate][1] == result.residual[1];
      for (int family : family_map[candidate])
        ranking[candidate].direct_events += result.direct_count[family];
    }
  }
  std::sort(ranking.begin(), ranking.end(), [&](const RankItem& left,
                                                 const RankItem& right) {
    if (left.direct_events != right.direct_events)
      return left.direct_events > right.direct_events;
    long double left_safe = left.safe_quality_sum / left.safe_count;
    long double right_safe = right.safe_quality_sum / right.safe_count;
    if (left_safe != right_safe) return left_safe > right_safe;
    long double left_all = left.quality_sum / left.count;
    long double right_all = right.quality_sum / right.count;
    if (left_all != right_all) return left_all > right_all;
    if (syntaxes[left.candidate].size() != syntaxes[right.candidate].size())
      return syntaxes[left.candidate].size() < syntaxes[right.candidate].size();
    return names[left.candidate] < names[right.candidate];
  });
  json << "  \"discovery_ranking\": [\n";
  for (std::size_t index = 0; index < ranking.size(); ++index) {
    const auto& item = ranking[index];
    if (index) json << ",\n";
    json << "    {\"rank\": " << index + 1 << ", \"word\": \""
         << names[item.candidate] << "\", \"syntax\": \""
         << json_escape(syntaxes[item.candidate])
         << "\", \"direct_events\": "
         << item.direct_events << ", \"safe_mean_H\": "
         << static_cast<double>(item.safe_quality_sum / item.safe_count)
         << ", \"all_mean_H\": "
         << static_cast<double>(item.quality_sum / item.count)
         << ", \"saturated\": " << item.saturated
         << ", \"description_length\": "
         << syntaxes[item.candidate].size()
         << "}";
  }
  json << "\n  ],\n"
       << "  \"family_summaries\": [\n";
  bool first_family_summary = true;
  for (int bits : FACTOR_BITS)
    for (int cohort = 0; cohort < 3; ++cohort)
      for (int family = 0; family < FAMILY_COUNT; ++family) {
        u64 count = 0, cleanup_free_count = 0, atoms = 0, zeros = 0,
            units = 0, n_powers = 0, direct_events = 0, inputs_with_direct = 0,
            cleanup_free_inputs_with_direct = 0;
        for (const auto& result : results) {
          if (result.task.factor_bits != bits || result.task.cohort != cohort)
            continue;
          ++count;
          cleanup_free_count += result.cleanup_free;
          atoms += result.atom_count[family];
          zeros += result.zero_count[family];
          units += result.unit_count[family];
          n_powers += result.n_power_count[family];
          direct_events += result.direct_count[family];
          bool hit = result.direct_count[family] != 0;
          inputs_with_direct += hit;
          cleanup_free_inputs_with_direct += hit && result.cleanup_free;
        }
        require(count > 0, "family summary cohort");
        if (!first_family_summary) json << ",\n";
        first_family_summary = false;
        json << "    {\"factor_bits\": " << bits << ", \"split\": \""
             << (bits <= 32 ? "discovery" : "heldout")
             << "\", \"cohort\": \"" << cohort_name(cohort)
             << "\", \"family\": \"" << FAMILY_NAMES[family]
             << "\", \"count\": " << count
             << ", \"cleanup_free_count\": " << cleanup_free_count
             << ", \"atoms\": " << atoms << ", \"zeros\": " << zeros
             << ", \"units\": " << units << ", \"N_powers\": "
             << n_powers
             << ", \"direct_events\": " << direct_events
             << ", \"inputs_with_direct\": " << inputs_with_direct
             << ", \"cleanup_free_inputs_with_direct\": "
             << cleanup_free_inputs_with_direct << "}";
      }
  json << "\n  ],\n"
       << "  \"summaries\": [\n";
  bool first_summary = true;
  for (int bits : FACTOR_BITS)
    for (int cohort = 0; cohort < 3; ++cohort)
      for (int candidate = 0; candidate < WORD_COUNT; ++candidate) {
        std::vector<long double> logs, strict_logs;
        long double mean = 0, strict_mean = 0;
        std::size_t count = 0, strict_count = 0, improved = 0,
                    strict_improved = 0, saturated = 0, strict_saturated = 0;
        for (const auto& result : results) {
          if (result.task.factor_bits != bits || result.task.cohort != cohort)
            continue;
          long double quality = std::max(
              static_cast<long double>(result.captured[candidate][0]) /
                  result.residual[0],
              static_cast<long double>(result.captured[candidate][1]) /
                  result.residual[1]);
          long double baseline = std::max(
              static_cast<long double>(result.captured[0][0]) / result.residual[0],
              static_cast<long double>(result.captured[0][1]) / result.residual[1]);
          mean += quality;
          ++count;
          logs.push_back(-std::log2(quality));
          improved += quality > baseline;
          bool full = result.captured[candidate][0] == result.residual[0] ||
                      result.captured[candidate][1] == result.residual[1];
          saturated += full;
          if (result.strict) {
            strict_mean += quality;
            ++strict_count;
            strict_logs.push_back(-std::log2(quality));
            strict_improved += quality > baseline;
            strict_saturated += full;
          }
        }
        require(count > 0, "summary cohort");
        if (!first_summary) json << ",\n";
        first_summary = false;
        json << "    {\"factor_bits\": " << bits << ", \"split\": \""
             << (bits <= 32 ? "discovery" : "heldout")
             << "\", \"cohort\": \"" << cohort_name(cohort)
             << "\", \"word\": \"" << names[candidate]
             << "\", \"count\": " << count
             << ", \"strict_count\": " << strict_count
             << ", \"mean_H\": " << static_cast<double>(mean / count)
             << ", \"median_neglog2H\": "
             << static_cast<double>(quantile(logs, 0.5L))
             << ", \"p90_neglog2H\": "
             << static_cast<double>(quantile(logs, 0.9L))
             << ", \"p99_neglog2H\": "
             << static_cast<double>(quantile(logs, 0.99L))
             << ", \"improved\": " << improved
             << ", \"saturated\": " << saturated;
        if (strict_count)
          json << ", \"strict_mean_H\": "
               << static_cast<double>(strict_mean / strict_count)
               << ", \"strict_median_neglog2H\": "
               << static_cast<double>(quantile(strict_logs, 0.5L))
               << ", \"strict_p90_neglog2H\": "
               << static_cast<double>(quantile(strict_logs, 0.9L))
               << ", \"strict_p99_neglog2H\": "
               << static_cast<double>(quantile(strict_logs, 0.99L));
        else
          json << ", \"strict_mean_H\": null, \"strict_median_neglog2H\": null, \"strict_p90_neglog2H\": null, \"strict_p99_neglog2H\": null";
        json << ", \"strict_improved\": " << strict_improved
             << ", \"strict_saturated\": " << strict_saturated << "}";
      }
  json << "\n  ]\n}\n";
  json.close();
  require(static_cast<bool>(json), "write JSON");
  std::cout << "F259_D02_PASS inputs=" << results.size()
            << " elapsed_seconds=" << std::fixed << std::setprecision(3)
            << elapsed << " identity_mining={" << identity_mining << "}\n";
  return 0;
} catch (const std::exception& exception) {
  std::cerr << "F259_D02_FAIL " << exception.what() << "\n";
  return 1;
}
