#include <algorithm>
#include <atomic>
#include <chrono>
#include <cctype>
#include <cstdint>
#include <fstream>
#include <functional>
#include <iomanip>
#include <iostream>
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
#include <utility>
#include <vector>

#include <boost/multiprecision/cpp_int.hpp>
#include <boost/multiprecision/integer.hpp>

#if defined(__unix__) || defined(__APPLE__)
#include <sys/resource.h>
#endif

using boost::multiprecision::cpp_int;

namespace {

constexpr uint64_t MASTER_SEED = 0xF265E11C0B1C5EEDULL;
constexpr int FAMILY_COUNT = 12;
constexpr int WORKERS_MAX = 8;
constexpr int ROW_BITS_MAX = 361;
constexpr int ROWS_MAX = 384;
constexpr int BLOCKS_MAX = 4096;
constexpr int SPLITS_MAX = 20000;
constexpr int TOTAL_ROW_BITS_MAX = 160000;

uint64_t mix64(uint64_t x) {
  x += 0x9e3779b97f4a7c15ULL;
  x = (x ^ (x >> 30)) * 0xbf58476d1ce4e5b9ULL;
  x = (x ^ (x >> 27)) * 0x94d049bb133111ebULL;
  return x ^ (x >> 31);
}

uint64_t seed_key(std::initializer_list<uint64_t> xs) {
  uint64_t h = MASTER_SEED;
  for (uint64_t x : xs) h = mix64(h ^ mix64(x));
  return h;
}

struct Rng {
  uint64_t s;
  explicit Rng(uint64_t seed) : s(seed) {}
  uint64_t next() { return s = mix64(s); }
};

cpp_int absz(cpp_int x) { return x < 0 ? -x : x; }

cpp_int modz(cpp_int x, const cpp_int& n) {
  x %= n;
  if (x < 0) x += n;
  return x;
}

cpp_int gcdz(cpp_int a, cpp_int b) {
  a = absz(a);
  b = absz(b);
  while (b != 0) {
    cpp_int r = a % b;
    a = b;
    b = r;
  }
  return a;
}

cpp_int powz(cpp_int a, unsigned e) {
  cpp_int r = 1;
  while (e) {
    if (e & 1U) r *= a;
    e >>= 1U;
    if (e) a *= a;
  }
  return r;
}

cpp_int powmod(cpp_int a, cpp_int e, const cpp_int& n) {
  a = modz(a, n);
  cpp_int r = 1 % n;
  while (e > 0) {
    if ((e & 1) != 0) r = (r * a) % n;
    e >>= 1;
    if (e != 0) a = (a * a) % n;
  }
  return r;
}

cpp_int invmod(const cpp_int& a0, const cpp_int& n) {
  cpp_int a = modz(a0, n), b = n;
  cpp_int x0 = 1, x1 = 0;
  while (b != 0) {
    cpp_int q = a / b;
    cpp_int r = a - q * b;
    a = b;
    b = r;
    cpp_int x2 = x0 - q * x1;
    x0 = x1;
    x1 = x2;
  }
  if (a != 1) throw std::runtime_error("inverse requested for nonunit");
  return modz(x0, n);
}

int bitlen(const cpp_int& x) {
  if (x == 0) return 0;
  return static_cast<int>(boost::multiprecision::msb(absz(x))) + 1;
}

cpp_int isqrtz(const cpp_int& x) {
  if (x < 0) throw std::runtime_error("negative integer square root");
  if (x < 2) return x;
  cpp_int r = cpp_int(1) << ((bitlen(x) + 1) / 2);
  for (;;) {
    cpp_int y = (r + x / r) >> 1;
    if (y >= r) {
      while ((r + 1) * (r + 1) <= x) ++r;
      while (r * r > x) --r;
      return r;
    }
    r = y;
  }
}

bool squarez(const cpp_int& x, cpp_int* root = nullptr) {
  if (x < 0) return false;
  cpp_int r = isqrtz(x);
  if (r * r != x) return false;
  if (root) *root = r;
  return true;
}

std::string dec(const cpp_int& x) { return x.convert_to<std::string>(); }

uint64_t mulmod64(uint64_t a, uint64_t b, uint64_t m) {
  return static_cast<uint64_t>((static_cast<unsigned __int128>(a) * b) % m);
}

uint64_t powmod64(uint64_t a, uint64_t e, uint64_t m) {
  uint64_t r = 1;
  while (e) {
    if (e & 1ULL) r = mulmod64(r, a, m);
    e >>= 1ULL;
    if (e) a = mulmod64(a, a, m);
  }
  return r;
}

bool prime64(uint64_t n) {
  if (n < 2) return false;
  for (uint64_t p : {2ULL, 3ULL, 5ULL, 7ULL, 11ULL, 13ULL, 17ULL, 19ULL,
                     23ULL, 29ULL, 31ULL, 37ULL}) {
    if (n % p == 0) return n == p;
  }
  uint64_t d = n - 1, s = 0;
  while ((d & 1ULL) == 0) {
    d >>= 1ULL;
    ++s;
  }
  for (uint64_t a : {2ULL, 325ULL, 9375ULL, 28178ULL, 450775ULL,
                     9780504ULL, 1795265022ULL}) {
    if (a % n == 0) continue;
    uint64_t x = powmod64(a % n, d, n);
    if (x == 1 || x == n - 1) continue;
    bool witness = true;
    for (uint64_t r = 1; r < s; ++r) {
      x = mulmod64(x, x, n);
      if (x == n - 1) {
        witness = false;
        break;
      }
    }
    if (witness) return false;
  }
  return true;
}

uint64_t random_prime(Rng& rng, int bits, bool safe) {
  const uint64_t lo = 1ULL << (bits - 1);
  const uint64_t hi_mask = (1ULL << bits) - 1;
  const uint64_t cap = safe ? 1000000ULL : 200000ULL;
  for (uint64_t t = 0; t < cap; ++t) {
    if (!safe) {
      uint64_t x = (rng.next() & hi_mask) | lo | 1ULL;
      if (prime64(x)) return x;
    } else {
      uint64_t qlo = 1ULL << (bits - 2);
      uint64_t qmask = (1ULL << (bits - 1)) - 1;
      uint64_t q = (rng.next() & qmask) | qlo | 1ULL;
      uint64_t p = 2 * q + 1;
      if (p >= lo && p <= hi_mask && prime64(q) && prime64(p)) return p;
    }
  }
  return 0;
}

uint64_t next_prime_same_bits(uint64_t x, int bits) {
  const uint64_t hi = (1ULL << bits) - 1;
  if ((x & 1ULL) == 0) ++x;
  for (uint64_t t = 0; t < 200000 && x <= hi; ++t, x += 2) {
    if (prime64(x)) return x;
  }
  return 0;
}

cpp_int random_below(Rng& rng, const cpp_int& n) {
  if (n <= 1) return 0;
  int bits = bitlen(n - 1);
  for (;;) {
    cpp_int x = cpp_int(rng.next());
    if (bits > 64) x |= cpp_int(rng.next()) << 64;
    if (bits < 128) x &= (cpp_int(1) << bits) - 1;
    if (x < n) return x;
  }
}

struct Case {
  int split = 0;
  int factor_bits = 0;
  int shape = 0;
  int index = 0;
  cpp_int N;
  uint64_t p = 0, q = 0;
};

const char* shape_name(int s) {
  return s == 0 ? "random" : (s == 1 ? "neighbor" : "safe");
}

bool make_case(int split, int bits, int shape, int index,
               std::set<std::string>& used, Case& out) {
  Rng rng(seed_key({0xC0A0ULL, static_cast<uint64_t>(split),
                    static_cast<uint64_t>(bits), static_cast<uint64_t>(shape),
                    static_cast<uint64_t>(index)}));
  for (int retry = 0; retry < 128; ++retry) {
    uint64_t p = 0, q = 0;
    if (shape == 0) {
      p = random_prime(rng, bits, false);
      q = random_prime(rng, bits, false);
    } else if (shape == 1) {
      p = random_prime(rng, bits, false);
      uint64_t offset = 2 * (2 + (rng.next() % 2048));
      q = p ? next_prime_same_bits(p + offset, bits) : 0;
    } else {
      p = random_prime(rng, bits, true);
      q = random_prime(rng, bits, true);
    }
    if (!p || !q || p == q) continue;
    if (p > q) std::swap(p, q);
    cpp_int N = cpp_int(p) * q;
    std::string key = dec(N);
    if (!used.insert(key).second) continue;
    out = {split, bits, shape, index, N, p, q};
    return true;
  }
  return false;
}

std::vector<Case> make_corpus(int wanted_split, int* shortfall) {
  const int bits_menu[] = {12, 16, 20, 24, 32, 40, 48, 60};
  std::set<std::string> used;
  std::vector<Case> selected;
  *shortfall = 0;
  for (int split = 0; split < 2; ++split) {
    for (int bits : bits_menu) {
      for (int shape = 0; shape < 3; ++shape) {
        for (int index = 0; index < 16; ++index) {
          Case c;
          if (!make_case(split, bits, shape, index, used, c)) {
            if (split == wanted_split) ++*shortfall;
            continue;
          }
          if (split == wanted_split) selected.push_back(c);
        }
      }
    }
  }
  return selected;
}

struct Point {
  cpp_int x, y;
  bool infinity = false;
};

struct AddResult {
  Point point;
  cpp_int factor = 1;
  std::string status = "OK";
};

AddResult add_points(const Point& p, const Point& q, const cpp_int& A,
                     const cpp_int& N) {
  if (p.infinity) return {q, 1, "OK"};
  if (q.infinity) return {p, 1, "OK"};
  cpp_int numerator, denominator;
  bool doubling = false;
  if (p.x == q.x) {
    if (modz(p.y + q.y, N) == 0) return {{0, 0, true}, 1, "OK_INFINITY"};
    if (p.y != q.y) {
      cpp_int g1 = gcdz(p.y - q.y, N);
      if (g1 > 1 && g1 < N) return {{}, g1, "FACTOR_X_SIGN"};
      cpp_int g2 = gcdz(p.y + q.y, N);
      if (g2 > 1 && g2 < N) return {{}, g2, "FACTOR_X_SIGN"};
      return {{}, N, "FULL_X_EXCEPTION"};
    }
    doubling = true;
    numerator = 3 * p.x * p.x + A;
    denominator = 2 * p.y;
  } else {
    numerator = q.y - p.y;
    denominator = q.x - p.x;
  }
  cpp_int den = modz(denominator, N);
  cpp_int g = gcdz(den, N);
  if (g > 1 && g < N) return {{}, g, "FACTOR_DENOMINATOR"};
  if (g == N) {
    if (doubling && modz(p.y, N) == 0)
      return {{0, 0, true}, 1, "OK_INFINITY"};
    return {{}, N, "FULL_DENOMINATOR"};
  }
  cpp_int lambda = modz(numerator, N) * invmod(den, N) % N;
  cpp_int x3 = modz(lambda * lambda - p.x - q.x, N);
  cpp_int y3 = modz(lambda * (p.x - x3) - p.y, N);
  return {{x3, y3, false}, 1, "OK"};
}

struct Family {
  int id;
  const char* mode;
  const char* schedule;
  int multiplier;
  int domain;
};

const Family FAMILIES[FAMILY_COUNT] = {
    {0, "U", "ALL", 1, 100},       {1, "U", "ALL", 2, 101},
    {2, "U", "ODD", 2, 102},      {3, "U", "PRIME", 3, 103},
    {4, "XS", "ALL", 2, 104},     {5, "YS", "ALL", 2, 105},
    {6, "AS", "ALL", 2, 106},     {7, "CENTER", "ALL", 2, 107},
    {8, "POWER", "ALL", 2, 108},  {9, "POWER", "ODD", 3, 109},
    {10, "U", "LOWHAM", 4, 110},  {11, "XS", "PRIME", 4, 111}};

bool emit_index(const Family& f, int k) {
  if (std::string(f.schedule) == "ALL") return true;
  if (std::string(f.schedule) == "ODD") return k == 1 || (k & 1);
  if (std::string(f.schedule) == "PRIME") return k == 1 || prime64(k);
  return k == 1 || __builtin_popcount(static_cast<unsigned>(k)) <= 2;
}

int scalar_limit(const Family& f, const cpp_int& N) {
  int n = bitlen(N);
  return std::min(f.multiplier * n, 192);
}

int planned_rows(const Family& f, int nbits) {
  int K = std::min(f.multiplier * nbits, 192), c = 0;
  for (int k = 1; k <= K; ++k) c += emit_index(f, k) ? 1 : 0;
  return 2 * c;
}

struct CurveInfo {
  int id = -1;
  cpp_int A, B, delta, x0, y0;
};

struct Row {
  int curve = -1;
  int index = 0;
  cpp_int u, v, a, carry;
};

struct Relation {
  std::vector<int> cols;
  std::string label;
  std::string root_class;
  cpp_int exact_root, supplied_root, normalized_root, gcd_minus, gcd_plus;
};

struct BankResult {
  int family = -1;
  bool eligible = false;
  bool resource_reject = false;
  bool direct = false;
  cpp_int first_factor = 1;
  std::string first_factor_kind;
  uint64_t rows = 0, pairs = 0, relations = 0, useful = 0;
  uint64_t strict_useful = 0, residual_relations = 0, chord_relations = 0;
  uint64_t singleton_squares = 0, equal_rows = 0, inverse_duplicates = 0;
  uint64_t square_multiple_pairs = 0, tangent_shared_pairs = 0;
  uint64_t chord_shared_pairs = 0, discriminant_shared_pairs = 0;
  bool residual_bank = false;
  std::vector<CurveInfo> curves;
  std::vector<Row> rows_data;
  std::vector<Relation> saved;
  std::string error;
};

void record_factor(BankResult& br, const cpp_int& g, const cpp_int& N,
                   const std::string& kind) {
  if (g > 1 && g < N) {
    br.direct = true;
    if (br.first_factor == 1) {
      br.first_factor = g;
      br.first_factor_kind = kind;
    }
  }
}

bool choose_curve(const Case& c, const Family& f, int curve_id,
                  CurveInfo& out, BankResult& br) {
  Rng rng(seed_key({0xEC265ULL, static_cast<uint64_t>(c.split),
                    static_cast<uint64_t>(c.factor_bits),
                    static_cast<uint64_t>(c.shape),
                    static_cast<uint64_t>(c.index),
                    static_cast<uint64_t>(f.domain),
                    static_cast<uint64_t>(curve_id)}));
  int nbits = bitlen(c.N);
  cpp_int small_bound = (cpp_int(1) << std::min(16, std::max(1, nbits - 1))) - 1;
  for (int attempt = 0; attempt < 32; ++attempt) {
    cpp_int A, x, y;
    std::string mode(f.mode);
    if (mode == "POWER") {
      cpp_int s = 1 + random_below(rng, c.N - 1);
      x = s * s % c.N;
      y = x * s % c.N;
      A = modz(s + 1, c.N);
      if (A == 0) A = 1;
    } else {
      A = 1 + random_below(rng, c.N - 1);
      x = random_below(rng, c.N);
      y = random_below(rng, c.N);
      if (mode == "XS") x = 1 + random_below(rng, small_bound);
      if (mode == "YS") y = 1 + random_below(rng, small_bound);
      if (mode == "AS") A = 1 + random_below(rng, small_bound);
      if (mode == "CENTER") {
        cpp_int quarter = c.N / 4;
        cpp_int width = c.N / 2;
        A = quarter + random_below(rng, width);
        x = quarter + random_below(rng, width);
        y = quarter + random_below(rng, width);
        if (A == 0) A = 1;
      }
    }
    cpp_int B = modz(y * y - x * x * x - A * x, c.N);
    if (B == 0) continue;
    cpp_int delta = 4 * A * A * A + 27 * B * B;
    cpp_int g = gcdz(delta, c.N);
    if (g > 1 && g < c.N) {
      record_factor(br, g, c.N, "CURVE_DISCRIMINANT");
      return false;
    }
    if (g == c.N) continue;
    out = {curve_id, A, B, delta, x, y};
    return true;
  }
  br.resource_reject = true;
  br.error = "CURVE_ATTEMPT_EXHAUSTED";
  return false;
}

bool append_curve_rows(const Case& c, const Family& f, const CurveInfo& curve,
                       BankResult& br) {
  Point base{curve.x0, curve.y0, false}, current = base;
  int K = scalar_limit(f, c.N);
  for (int k = 1; k <= K; ++k) {
    if (!current.infinity && emit_index(f, k)) {
      cpp_int a = current.x * current.x * current.x +
                  curve.A * current.x + curve.B;
      if (bitlen(a) > ROW_BITS_MAX) {
        br.resource_reject = true;
        br.error = "ROW_BIT_CAP";
        return false;
      }
      cpp_int g = gcdz(current.y, c.N);
      if (g > 1 && g < c.N) {
        record_factor(br, g, c.N, "ROW_ROOT");
        return false;
      }
      if (g == c.N) {
        br.error = "FULL_ROW_ROOT";
        return false;
      }
      cpp_int diff = a - current.y * current.y;
      if (diff % c.N != 0) throw std::runtime_error("row congruence failed");
      br.rows_data.push_back(
          {curve.id, k, current.x, current.y, a, diff / c.N});
      if (static_cast<int>(br.rows_data.size()) > ROWS_MAX) {
        br.resource_reject = true;
        br.error = "ROW_COUNT_CAP";
        return false;
      }
    }
    if (k != K) {
      AddResult ar = add_points(current, base, curve.A, c.N);
      if (ar.factor > 1 && ar.factor < c.N) {
        record_factor(br, ar.factor, c.N, ar.status);
        return false;
      }
      if (ar.factor == c.N) {
        br.error = ar.status;
        return false;
      }
      current = ar.point;
    }
  }
  return true;
}

struct Block {
  cpp_int value;
  std::vector<uint16_t> exponents;
};

struct Decoder {
  bool ok = false;
  bool resource_reject = false;
  std::vector<Block> blocks;
  std::vector<std::vector<uint64_t>> kernel;
  std::string error;
};

bool bit_get(const std::vector<uint64_t>& v, int i) {
  return ((v[i >> 6] >> (i & 63)) & 1ULL) != 0;
}

void bit_flip(std::vector<uint64_t>& v, int i) {
  v[i >> 6] ^= 1ULL << (i & 63);
}

void bit_xor(std::vector<uint64_t>& a, const std::vector<uint64_t>& b) {
  for (size_t i = 0; i < a.size(); ++i) a[i] ^= b[i];
}

Decoder decode_rows(const std::vector<Row>& rows) {
  Decoder d;
  const int m = static_cast<int>(rows.size());
  int total_bits = 0;
  for (const Row& r : rows) total_bits += bitlen(r.a);
  if (total_bits > TOTAL_ROW_BITS_MAX) {
    d.resource_reject = true;
    d.error = "TOTAL_ROW_BITS_CAP";
    return d;
  }
  for (int i = 0; i < m; ++i) {
    if (rows[i].a == 1) continue;
    Block b{rows[i].a, std::vector<uint16_t>(m, 0)};
    b.exponents[i] = 1;
    d.blocks.push_back(std::move(b));
  }
  int splits = 0;
  bool changed = true;
  while (changed) {
    changed = false;
    for (size_t i = 0; i < d.blocks.size() && !changed; ++i) {
      for (size_t j = i + 1; j < d.blocks.size(); ++j) {
        cpp_int g = gcdz(d.blocks[i].value, d.blocks[j].value);
        if (g == 1) continue;
        Block bi = d.blocks[i], bj = d.blocks[j];
        cpp_int ci = bi.value / g, cj = bj.value / g;
        std::vector<uint16_t> eg(m);
        for (int k = 0; k < m; ++k) {
          unsigned s = static_cast<unsigned>(bi.exponents[k]) + bj.exponents[k];
          if (s > std::numeric_limits<uint16_t>::max())
            throw std::runtime_error("exponent overflow");
          eg[k] = static_cast<uint16_t>(s);
        }
        d.blocks.erase(d.blocks.begin() + j);
        d.blocks.erase(d.blocks.begin() + i);
        if (ci > 1) d.blocks.push_back({ci, std::move(bi.exponents)});
        if (cj > 1) d.blocks.push_back({cj, std::move(bj.exponents)});
        d.blocks.push_back({g, std::move(eg)});
        ++splits;
        if (splits > SPLITS_MAX || static_cast<int>(d.blocks.size()) > BLOCKS_MAX) {
          d.resource_reject = true;
          d.error = "GCD_FREE_CAP";
          return d;
        }
        changed = true;
        break;
      }
    }
  }
  std::sort(d.blocks.begin(), d.blocks.end(),
            [](const Block& a, const Block& b) { return a.value < b.value; });
  for (size_t i = 0; i < d.blocks.size(); ++i)
    for (size_t j = i + 1; j < d.blocks.size(); ++j)
      if (gcdz(d.blocks[i].value, d.blocks[j].value) != 1) {
        d.error = "FINAL_BLOCKS_NOT_COPRIME";
        return d;
      }
  for (int col = 0; col < m; ++col) {
    cpp_int rebuilt = 1;
    for (const Block& b : d.blocks)
      if (b.exponents[col]) rebuilt *= powz(b.value, b.exponents[col]);
    if (rebuilt != rows[col].a) {
      d.error = "ROW_RECONSTRUCTION_FAILED";
      return d;
    }
  }
  const int words = (m + 63) / 64;
  std::vector<std::vector<uint64_t>> matrix;
  for (const Block& b : d.blocks) {
    if (squarez(b.value)) continue;
    std::vector<uint64_t> eq(words, 0);
    for (int col = 0; col < m; ++col)
      if (b.exponents[col] & 1U) bit_flip(eq, col);
    if (std::any_of(eq.begin(), eq.end(), [](uint64_t w) { return w != 0; }))
      matrix.push_back(std::move(eq));
  }
  std::vector<int> pivots;
  int rank = 0;
  for (int col = 0; col < m; ++col) {
    int sel = -1;
    for (int r = rank; r < static_cast<int>(matrix.size()); ++r)
      if (bit_get(matrix[r], col)) {
        sel = r;
        break;
      }
    if (sel < 0) continue;
    std::swap(matrix[rank], matrix[sel]);
    for (int r = 0; r < static_cast<int>(matrix.size()); ++r)
      if (r != rank && bit_get(matrix[r], col)) bit_xor(matrix[r], matrix[rank]);
    pivots.push_back(col);
    ++rank;
  }
  std::vector<char> is_pivot(m, 0);
  for (int c : pivots) is_pivot[c] = 1;
  for (int free_col = 0; free_col < m; ++free_col) {
    if (is_pivot[free_col]) continue;
    std::vector<uint64_t> v(words, 0);
    bit_flip(v, free_col);
    for (int r = 0; r < rank; ++r)
      if (bit_get(matrix[r], free_col)) bit_flip(v, pivots[r]);
    d.kernel.push_back(std::move(v));
  }
  for (const auto& v : d.kernel) {
    for (const auto& eq : matrix) {
      unsigned parity = 0;
      for (int w = 0; w < words; ++w)
        parity ^= static_cast<unsigned>(__builtin_parityll(v[w] & eq[w]));
      if (parity) {
        d.error = "KERNEL_VERIFICATION_FAILED";
        return d;
      }
    }
  }
  d.ok = true;
  return d;
}

const CurveInfo& curve_by_id(const BankResult& br, int id) {
  for (const auto& c : br.curves)
    if (c.id == id) return c;
  throw std::runtime_error("curve id absent");
}

std::string relation_label(const std::vector<int>& cols, const cpp_int& N,
                           const BankResult& br) {
  if (cols.size() == 1) return "SINGLETON";
  if (cols.size() == 2) {
    const Row& a = br.rows_data[cols[0]];
    const Row& b = br.rows_data[cols[1]];
    if (a.curve == b.curve && a.u == b.u && modz(a.v + b.v, N) == 0)
      return "INVERSE_DUPLICATE";
    if (a.a == b.a) return "EQUAL_ROW";
    const cpp_int& lo = a.a < b.a ? a.a : b.a;
    const cpp_int& hi = a.a < b.a ? b.a : a.a;
    if (hi % lo == 0 && squarez(hi / lo)) return "SQUARE_MULTIPLE_PAIR";
  }
  bool tangent = false, chord = false, disc = false, cross = false;
  for (size_t ii = 0; ii < cols.size(); ++ii) {
    for (size_t jj = ii + 1; jj < cols.size(); ++jj) {
      const Row& r = br.rows_data[cols[ii]];
      const Row& s = br.rows_data[cols[jj]];
      if (r.curve != s.curve) {
        cross = true;
        continue;
      }
      const CurveInfo& c = curve_by_id(br, r.curve);
      cpp_int shared = gcdz(r.a, s.a);
      if (gcdz(shared, r.u - s.u) > 1) tangent = true;
      cpp_int H = r.u * r.u + r.u * s.u + s.u * s.u + c.A;
      if (gcdz(shared, H) > 1) chord = true;
      if (gcdz(shared, c.delta) > 1) disc = true;
    }
  }
  if (tangent) return "TANGENT_SUPPORTED";
  if (chord) return "CHORD_SUPPORTED";
  if (disc) return "DISCRIMINANT_SUPPORTED";
  if (cross) return "CROSS_CURVE";
  return "OTHER_SAME_CURVE";
}

Relation verify_relation(const std::vector<uint64_t>& bits,
                         const cpp_int& N, const BankResult& br) {
  Relation rel;
  cpp_int product = 1, supplied = 1;
  for (int i = 0; i < static_cast<int>(br.rows_data.size()); ++i) {
    if (!bit_get(bits, i)) continue;
    rel.cols.push_back(i);
    product *= br.rows_data[i].a;
    supplied = supplied * br.rows_data[i].v % N;
  }
  if (rel.cols.empty()) throw std::runtime_error("empty kernel vector");
  cpp_int root;
  if (!squarez(product, &root)) throw std::runtime_error("reported relation is not square");
  cpp_int rm = root % N;
  cpp_int gm = gcdz(rm - supplied, N);
  cpp_int gp = gcdz(rm + supplied, N);
  cpp_int normalized = rm * invmod(supplied, N) % N;
  std::string root_class;
  if (rm == supplied)
    root_class = "GLOBAL_PLUS";
  else if (rm == modz(-supplied, N))
    root_class = "GLOBAL_MINUS";
  else if ((gm > 1 && gm < N) || (gp > 1 && gp < N))
    root_class = "USEFUL";
  else
    throw std::runtime_error("normalized root has invalid gcd classification");
  rel.label = relation_label(rel.cols, N, br);
  rel.root_class = root_class;
  rel.exact_root = root;
  rel.supplied_root = supplied;
  rel.normalized_root = normalized;
  rel.gcd_minus = gm;
  rel.gcd_plus = gp;
  return rel;
}

BankResult analyze_bank(const Case& c, const Family& f) {
  BankResult br;
  br.family = f.id;
  try {
    for (int curve_id = 0; curve_id < 2; ++curve_id) {
      CurveInfo curve;
      if (!choose_curve(c, f, curve_id, curve, br)) break;
      br.curves.push_back(curve);
      if (!append_curve_rows(c, f, curve, br)) break;
    }
    br.rows = br.rows_data.size();
    if (br.resource_reject || br.rows_data.empty()) return br;

    for (const Row& r : br.rows_data) {
      cpp_int s;
      if (!squarez(r.a, &s)) continue;
      ++br.singleton_squares;
      record_factor(br, gcdz(s - r.v, c.N), c.N, "SINGLETON_MINUS");
      record_factor(br, gcdz(s + r.v, c.N), c.N, "SINGLETON_PLUS");
    }
    for (size_t i = 0; i < br.rows_data.size(); ++i) {
      for (size_t j = i + 1; j < br.rows_data.size(); ++j) {
        ++br.pairs;
        const Row& r = br.rows_data[i];
        const Row& s = br.rows_data[j];
        record_factor(br, gcdz(r.u - s.u, c.N), c.N, "PAIR_X");
        record_factor(br, gcdz(r.v - s.v, c.N), c.N, "PAIR_Y_MINUS");
        record_factor(br, gcdz(r.v + s.v, c.N), c.N, "PAIR_Y_PLUS");
        if (r.a == s.a) {
          ++br.equal_rows;
          if (r.curve == s.curve && r.u == s.u && modz(r.v + s.v, c.N) == 0)
            ++br.inverse_duplicates;
        } else {
          const cpp_int& lo = r.a < s.a ? r.a : s.a;
          const cpp_int& hi = r.a < s.a ? s.a : r.a;
          if (hi % lo == 0) {
            cpp_int multiplier;
            if (squarez(hi / lo, &multiplier)) {
              ++br.square_multiple_pairs;
              cpp_int exact_root = lo * multiplier;
              cpp_int supplied = r.v * s.v % c.N;
              record_factor(br, gcdz(exact_root - supplied, c.N), c.N,
                            "SQUARE_MULTIPLE_MINUS");
              record_factor(br, gcdz(exact_root + supplied, c.N), c.N,
                            "SQUARE_MULTIPLE_PLUS");
            }
          }
        }
        if (r.curve == s.curve) {
          const CurveInfo& curve = curve_by_id(br, r.curve);
          cpp_int H = r.u * r.u + r.u * s.u + s.u * s.u + curve.A;
          record_factor(br, gcdz(H, c.N), c.N, "PAIR_CHORD");
          cpp_int shared = gcdz(r.a, s.a);
          if (gcdz(shared, r.u - s.u) > 1) ++br.tangent_shared_pairs;
          if (gcdz(shared, H) > 1) ++br.chord_shared_pairs;
          if (gcdz(shared, curve.delta) > 1) ++br.discriminant_shared_pairs;
        }
      }
    }

    Decoder decoder = decode_rows(br.rows_data);
    if (decoder.resource_reject) {
      br.resource_reject = true;
      br.error = decoder.error;
      return br;
    }
    if (!decoder.ok) throw std::runtime_error(decoder.error);
    br.eligible = true;
    for (const auto& bits : decoder.kernel) {
      Relation rel = verify_relation(bits, c.N, br);
      ++br.relations;
      bool useful = rel.root_class == "USEFUL";
      if (useful) ++br.useful;
      bool nonduplicate = rel.label != "SINGLETON" &&
                          rel.label != "INVERSE_DUPLICATE" &&
                          rel.label != "EQUAL_ROW";
      if (useful && !br.direct && nonduplicate) ++br.strict_useful;
      bool residual = nonduplicate && rel.label != "SQUARE_MULTIPLE_PAIR";
      if (residual) {
        ++br.residual_relations;
        br.residual_bank = true;
      }
      if (rel.label == "CHORD_SUPPORTED") ++br.chord_relations;
      if (br.saved.size() < 2 && (residual || useful)) br.saved.push_back(std::move(rel));
    }
  } catch (const std::exception& e) {
    br.eligible = false;
    br.error = e.what();
  }
  return br;
}

struct FamilyStats {
  uint64_t intended = 384, actual = 0, eligible = 0, resource_reject = 0;
  uint64_t direct_banks = 0, strict_banks = 0, strict_relations = 0;
  uint64_t residual_banks = 0, residual_relations = 0, chord_relations = 0;
  uint64_t rows = 0, pairs = 0, all_relations = 0, useful_relations = 0;
  uint64_t singleton_squares = 0, equal_rows = 0, inverse_duplicates = 0;
  uint64_t square_multiple_pairs = 0, tangent_shared_pairs = 0;
  uint64_t chord_shared_pairs = 0, discriminant_shared_pairs = 0;
};

std::string json_string(const std::string& s) {
  std::ostringstream o;
  o << '"';
  for (char c : s) {
    if (c == '"' || c == '\\') o << '\\' << c;
    else if (c == '\n') o << "\\n";
    else o << c;
  }
  o << '"';
  return o.str();
}

void write_certificate(std::ofstream& out, const Case& c, const Family& f,
                       const BankResult& br, const Relation& rel) {
  out << "{\"version\":\"F265_V1\",\"split\":" << c.split
      << ",\"factor_bits\":" << c.factor_bits
      << ",\"shape\":" << json_string(shape_name(c.shape))
      << ",\"case_index\":" << c.index << ",\"family\":" << f.id
      << ",\"N\":" << json_string(dec(c.N))
      << ",\"p_label\":" << json_string(std::to_string(c.p))
      << ",\"q_label\":" << json_string(std::to_string(c.q))
      << ",\"direct_before_relation\":" << (br.direct ? "true" : "false")
      << ",\"label\":" << json_string(rel.label)
      << ",\"root_class\":" << json_string(rel.root_class)
      << ",\"exact_root\":" << json_string(dec(rel.exact_root))
      << ",\"supplied_root\":" << json_string(dec(rel.supplied_root))
      << ",\"normalized_root\":" << json_string(dec(rel.normalized_root))
      << ",\"gcd_minus\":" << json_string(dec(rel.gcd_minus))
      << ",\"gcd_plus\":" << json_string(dec(rel.gcd_plus)) << ",\"rows\":[";
  for (size_t k = 0; k < rel.cols.size(); ++k) {
    if (k) out << ',';
    const Row& r = br.rows_data[rel.cols[k]];
    const CurveInfo& curve = curve_by_id(br, r.curve);
    out << "{\"curve\":" << r.curve << ",\"index\":" << r.index
        << ",\"A\":" << json_string(dec(curve.A))
        << ",\"B\":" << json_string(dec(curve.B))
        << ",\"u\":" << json_string(dec(r.u))
        << ",\"v\":" << json_string(dec(r.v))
        << ",\"a\":" << json_string(dec(r.a))
        << ",\"carry\":" << json_string(dec(r.carry)) << '}';
  }
  out << "]}\n";
}

struct RunOutput {
  std::vector<FamilyStats> stats;
  double seconds = 0;
  uint64_t peak_rss_kib = 0;
};

struct CellStats {
  uint64_t intended = 16, actual = 0, eligible = 0, strict_banks = 0;
};

uint64_t peak_rss_kib() {
#if defined(__unix__) || defined(__APPLE__)
  struct rusage ru {};
  if (getrusage(RUSAGE_SELF, &ru) == 0) return static_cast<uint64_t>(ru.ru_maxrss);
#endif
  return 0;
}

RunOutput run_cases(const std::vector<Case>& cases, const std::vector<int>& families,
                    int workers, const std::string& metrics_path,
                    const std::string& cert_path, const std::string& cells_path,
                    const std::string& banks_path) {
  struct Job { size_t case_id; int family; };
  std::vector<Job> jobs;
  for (size_t i = 0; i < cases.size(); ++i)
    for (int f : families) jobs.push_back({i, f});
  std::vector<BankResult> results(jobs.size());
  std::atomic<size_t> cursor{0};
  auto start = std::chrono::steady_clock::now();
  std::vector<std::thread> pool;
  workers = std::max(1, std::min(workers, WORKERS_MAX));
  for (int t = 0; t < workers; ++t) {
    pool.emplace_back([&] {
      for (;;) {
        size_t j = cursor.fetch_add(1);
        if (j >= jobs.size()) break;
        results[j] = analyze_bank(cases[jobs[j].case_id], FAMILIES[jobs[j].family]);
      }
    });
  }
  for (auto& t : pool) t.join();
  double seconds = std::chrono::duration<double>(std::chrono::steady_clock::now() - start).count();

  std::vector<FamilyStats> stats(FAMILY_COUNT);
  std::map<std::tuple<int, int, int>, CellStats> cells;
  for (int f = 0; f < FAMILY_COUNT; ++f) stats[f].intended = 384;
  std::ofstream cert(cert_path, std::ios::binary);
  if (!cert) throw std::runtime_error("cannot open certificate output");
  std::vector<int> saved_count(FAMILY_COUNT, 0);
  std::ofstream banks(banks_path, std::ios::binary);
  if (!banks) throw std::runtime_error("cannot open bank-status output");
  banks << "version\tsplit\tfactor_bits\tshape\tcase_index\tfamily\tN\teligible\tresource_reject"
           "\tdirect\tfirst_factor\tfactor_kind\tstrict_relations\trows\tpairs\trelations"
           "\tsingleton_squares\tequal_rows\tinverse_duplicates\tsquare_multiple_pairs"
           "\ttangent_shared_pairs\tchord_shared_pairs\tdiscriminant_shared_pairs\terror\n";
  for (size_t j = 0; j < jobs.size(); ++j) {
    const BankResult& br = results[j];
    const Case& current_case = cases[jobs[j].case_id];
    FamilyStats& s = stats[br.family];
    ++s.actual;
    s.eligible += br.eligible;
    s.resource_reject += br.resource_reject;
    s.direct_banks += br.direct;
    s.strict_banks += br.strict_useful > 0;
    s.strict_relations += br.strict_useful;
    s.residual_banks += br.residual_bank;
    s.residual_relations += br.residual_relations;
    s.chord_relations += br.chord_relations;
    s.rows += br.rows;
    s.pairs += br.pairs;
    s.all_relations += br.relations;
    s.useful_relations += br.useful;
    s.singleton_squares += br.singleton_squares;
    s.equal_rows += br.equal_rows;
    s.inverse_duplicates += br.inverse_duplicates;
    s.square_multiple_pairs += br.square_multiple_pairs;
    s.tangent_shared_pairs += br.tangent_shared_pairs;
    s.chord_shared_pairs += br.chord_shared_pairs;
    s.discriminant_shared_pairs += br.discriminant_shared_pairs;
    CellStats& cell = cells[{br.family, current_case.factor_bits, current_case.shape}];
    ++cell.actual;
    cell.eligible += br.eligible;
    cell.strict_banks += br.strict_useful > 0;
    banks << "F265_V1\t" << current_case.split << '\t' << current_case.factor_bits
          << '\t' << shape_name(current_case.shape) << '\t' << current_case.index
          << '\t' << br.family << '\t' << dec(current_case.N) << '\t' << br.eligible
          << '\t' << br.resource_reject << '\t' << br.direct << '\t'
          << dec(br.first_factor) << '\t' << br.first_factor_kind << '\t'
          << br.strict_useful << '\t' << br.rows << '\t' << br.pairs << '\t'
          << br.relations << '\t' << br.singleton_squares << '\t' << br.equal_rows
          << '\t' << br.inverse_duplicates << '\t' << br.square_multiple_pairs
          << '\t' << br.tangent_shared_pairs << '\t' << br.chord_shared_pairs
          << '\t' << br.discriminant_shared_pairs << '\t' << br.error << '\n';
    for (const Relation& rel : br.saved) {
      if (saved_count[br.family] >= 64) break;
      write_certificate(cert, cases[jobs[j].case_id], FAMILIES[br.family], br, rel);
      ++saved_count[br.family];
    }
  }
  banks.close();
  cert.close();
  std::ofstream metrics(metrics_path, std::ios::binary);
  if (!metrics) throw std::runtime_error("cannot open metrics output");
  metrics << "version\tfamily\tintended\tactual\teligible\tresource_reject\tdirect_banks"
             "\tstrict_banks\tstrict_relations\tresidual_banks\tresidual_relations"
             "\tchord_relations\trows\tpairs\tall_relations\tuseful_relations"
             "\tsingleton_squares\tequal_rows\tinverse_duplicates\tsquare_multiple_pairs"
             "\ttangent_shared_pairs\tchord_shared_pairs\tdiscriminant_shared_pairs\n";
  for (int f : families) {
    const auto& s = stats[f];
    metrics << "F265_V1\t" << f << '\t' << s.intended << '\t' << s.actual << '\t'
            << s.eligible << '\t' << s.resource_reject << '\t' << s.direct_banks
            << '\t' << s.strict_banks << '\t' << s.strict_relations << '\t'
            << s.residual_banks << '\t' << s.residual_relations << '\t'
            << s.chord_relations << '\t' << s.rows << '\t' << s.pairs << '\t'
            << s.all_relations << '\t' << s.useful_relations << '\t'
            << s.singleton_squares << '\t' << s.equal_rows << '\t'
            << s.inverse_duplicates << '\t' << s.square_multiple_pairs << '\t'
            << s.tangent_shared_pairs << '\t' << s.chord_shared_pairs << '\t'
            << s.discriminant_shared_pairs << '\n';
  }
  metrics.close();
  std::ofstream cell_out(cells_path, std::ios::binary);
  if (!cell_out) throw std::runtime_error("cannot open cell output");
  cell_out << "version\tfamily\tfactor_bits\tshape\tintended\tactual\teligible\tstrict_banks\n";
  for (const auto& kv : cells) {
    int f, bits, shape;
    std::tie(f, bits, shape) = kv.first;
    const CellStats& x = kv.second;
    cell_out << "F265_V1\t" << f << '\t' << bits << '\t' << shape_name(shape)
             << '\t' << x.intended << '\t' << x.actual << '\t' << x.eligible
             << '\t' << x.strict_banks << '\n';
  }
  cell_out.close();
  return {std::move(stats), seconds, peak_rss_kib()};
}

void write_cohort(const std::string& path, const std::vector<Case>& cases,
                  int shortfall) {
  std::ofstream out(path, std::ios::binary);
  if (!out) throw std::runtime_error("cannot open cohort output");
  out << "version\tshortfall\tsplit\tfactor_bits\tshape\tindex\tN\tp\tq\n";
  for (const Case& c : cases)
    out << "F265_V1\t" << shortfall << '\t' << c.split << '\t' << c.factor_bits
        << '\t' << shape_name(c.shape) << '\t' << c.index << '\t' << dec(c.N)
        << '\t' << c.p << '\t' << c.q << '\n';
}

std::vector<FamilyStats> read_metrics(const std::string& path) {
  std::ifstream in(path);
  if (!in) throw std::runtime_error("cannot read metrics");
  std::string line;
  std::getline(in, line);
  std::vector<FamilyStats> stats(FAMILY_COUNT);
  while (std::getline(in, line)) {
    if (line.empty()) continue;
    std::replace(line.begin(), line.end(), '\t', ' ');
    std::istringstream s(line);
    std::string version;
    int f;
    FamilyStats x;
    s >> version >> f >> x.intended >> x.actual >> x.eligible >> x.resource_reject
      >> x.direct_banks >> x.strict_banks >> x.strict_relations >> x.residual_banks
      >> x.residual_relations >> x.chord_relations >> x.rows >> x.pairs
      >> x.all_relations >> x.useful_relations >> x.singleton_squares
      >> x.equal_rows >> x.inverse_duplicates >> x.square_multiple_pairs
      >> x.tangent_shared_pairs >> x.chord_shared_pairs
      >> x.discriminant_shared_pairs;
    if (!s || version != "F265_V1" || f < 0 || f >= FAMILY_COUNT)
      throw std::runtime_error("invalid metrics row");
    stats[f] = x;
  }
  return stats;
}

bool better_family(int a, int b, const std::vector<FamilyStats>& s) {
  const auto& x = s[a];
  const auto& y = s[b];
  unsigned __int128 lhs = static_cast<unsigned __int128>(x.strict_banks) * y.eligible;
  unsigned __int128 rhs = static_cast<unsigned __int128>(y.strict_banks) * x.eligible;
  if (x.eligible == 0 && y.eligible != 0) return false;
  if (x.eligible != 0 && y.eligible == 0) return true;
  if (lhs != rhs) return lhs > rhs;
  if (x.strict_relations != y.strict_relations) return x.strict_relations > y.strict_relations;
  if (x.residual_banks != y.residual_banks) return x.residual_banks > y.residual_banks;
  if (x.residual_relations != y.residual_relations) return x.residual_relations > y.residual_relations;
  if (x.chord_relations != y.chord_relations) return x.chord_relations > y.chord_relations;
  if (x.eligible != y.eligible) return x.eligible > y.eligible;
  if (x.rows != y.rows) return x.rows < y.rows;
  return a < b;
}

std::vector<int> make_selection(const std::string& metrics_path,
                                const std::string& cohort_sha,
                                const std::string& selection_path) {
  if (cohort_sha.size() != 64 ||
      !std::all_of(cohort_sha.begin(), cohort_sha.end(),
                   [](unsigned char c) { return std::isxdigit(c) != 0; }))
    throw std::runtime_error("cohort SHA-256 must have 64 hex digits");
  auto stats = read_metrics(metrics_path);
  std::vector<int> ids(FAMILY_COUNT);
  std::iota(ids.begin(), ids.end(), 0);
  std::stable_sort(ids.begin(), ids.end(), [&](int a, int b) { return better_family(a, b, stats); });
  ids.resize(4);
  std::ofstream out(selection_path, std::ios::binary);
  if (!out) throw std::runtime_error("cannot write selection");
  out << "version F265_V1\n";
  out << "discovery_cohort_sha256 " << cohort_sha << "\n";
  out << "rank_fields strict_banks_per_eligible strict_relations residual_banks "
         "residual_relations chord_relations eligible rows_ascending family_id\n";
  out << "selected";
  for (int id : ids) out << ' ' << id;
  out << '\n';
  for (int id : ids) {
    const auto& x = stats[id];
    out << "family " << id << ' ' << x.strict_banks << ' ' << x.eligible << ' '
        << x.strict_relations << ' ' << x.residual_banks << ' '
        << x.residual_relations << ' ' << x.chord_relations << ' ' << x.rows << '\n';
  }
  return ids;
}

std::vector<int> read_selection(const std::string& path) {
  std::ifstream in(path, std::ios::binary);
  if (!in) throw std::runtime_error("cannot read selection");
  std::string token;
  std::vector<int> ids;
  while (in >> token) {
    if (token == "selected") {
      for (int i = 0; i < 4; ++i) {
        int id;
        in >> id;
        if (!in || id < 0 || id >= FAMILY_COUNT) throw std::runtime_error("bad selection id");
        ids.push_back(id);
      }
      break;
    }
    std::string rest;
    std::getline(in, rest);
  }
  if (ids.size() != 4 || std::set<int>(ids.begin(), ids.end()).size() != 4)
    throw std::runtime_error("selection must contain four distinct IDs");
  return ids;
}

std::map<std::tuple<int, int, int>, CellStats> read_cells(const std::string& path) {
  std::ifstream in(path);
  if (!in) throw std::runtime_error("cannot read cell metrics");
  std::string line;
  std::getline(in, line);
  std::map<std::tuple<int, int, int>, CellStats> cells;
  while (std::getline(in, line)) {
    if (line.empty()) continue;
    std::replace(line.begin(), line.end(), '\t', ' ');
    std::istringstream s(line);
    std::string version, shape;
    int f, bits, shape_id;
    CellStats x;
    s >> version >> f >> bits >> shape >> x.intended >> x.actual >> x.eligible
      >> x.strict_banks;
    if (!s || version != "F265_V1") throw std::runtime_error("invalid cell row");
    if (shape == "random") shape_id = 0;
    else if (shape == "neighbor") shape_id = 1;
    else if (shape == "safe") shape_id = 2;
    else throw std::runtime_error("invalid cell shape");
    cells[{f, bits, shape_id}] = x;
  }
  return cells;
}

void summarize_heldout(const std::string& metrics_path,
                       const std::string& cells_path,
                       const std::string& selection_path,
                       const std::string& output_path) {
  auto stats = read_metrics(metrics_path);
  auto cells = read_cells(cells_path);
  auto selected = read_selection(selection_path);
  uint64_t intended = 0, eligible = 0, strict_total = 0;
  std::map<int, uint64_t> strict_by_bits;
  bool cell_gate = true;
  for (int f : selected) {
    intended += stats[f].intended;
    eligible += stats[f].eligible;
    strict_total += stats[f].strict_banks;
  }
  for (int bits : {12, 16, 20, 24, 32, 40, 48, 60}) {
    for (int shape = 0; shape < 3; ++shape) {
      uint64_t max_eligible = 0;
      for (int f : selected) {
        auto it = cells.find({f, bits, shape});
        if (it != cells.end()) {
          max_eligible = std::max(max_eligible, it->second.eligible);
          strict_by_bits[bits] += it->second.strict_banks;
        }
      }
      if (max_eligible < 12) cell_gate = false;
    }
  }
  int positive_bit_cells = 0;
  for (const auto& kv : strict_by_bits)
    if (kv.second > 0) ++positive_bit_cells;
  std::string label;
  if (strict_total >= 2 && positive_bit_cells >= 2)
    label = "finite_positive_signal";
  else if (strict_total == 0 && eligible * 10 >= intended * 9 && cell_gate)
    label = "finite_null_signal";
  else
    label = "finite_mixed_or_inconclusive";
  std::ofstream out(output_path, std::ios::binary);
  if (!out) throw std::runtime_error("cannot write heldout summary");
  out << "{\"version\":\"F265_V1\",\"label\":" << json_string(label)
      << ",\"intended_selected_family_banks\":" << intended
      << ",\"eligible_selected_family_banks\":" << eligible
      << ",\"strict_hit_banks\":" << strict_total
      << ",\"positive_factor_size_cells\":" << positive_bit_cells
      << ",\"cell_eligibility_gate\":" << (cell_gate ? "true" : "false")
      << ",\"finite_only\":true}\n";
}

void self_test() {
  if (!prime64(2305843009213693951ULL) || prime64(221ULL))
    throw std::runtime_error("Miller-Rabin self-test failed");
  for (int i = 0; i < 1000; ++i) {
    cpp_int x = cpp_int(i) * i;
    cpp_int r;
    if (!squarez(x, &r) || r != i) throw std::runtime_error("isqrt self-test failed");
  }
  cpp_int N = 10403, A = 1, B = 5;
  Point base{5461, 5889, false}, cur = base;
  if (modz(base.y * base.y - base.x * base.x * base.x - A * base.x - B, N) != 0)
    throw std::runtime_error("P20 seed is not on curve");
  if (gcdz(4 * A * A * A + 27 * B * B, N) != 1)
    throw std::runtime_error("P20 discriminant control failed");
  std::vector<Point> pts(102);
  pts[1] = base;
  for (int k = 2; k <= 101; ++k) {
    AddResult ar = add_points(cur, base, A, N);
    if (ar.factor != 1 || ar.point.infinity)
      throw std::runtime_error("P20 affine reconstruction stopped early");
    cur = ar.point;
    pts[k] = cur;
  }
  if (gcdz(pts[11].x - pts[101].x, N) != 101 ||
      gcdz(pts[5].x - pts[101].x, N) != 103)
    throw std::runtime_error("P20 collision controls failed");
  cpp_int pooled = 1;
  for (int i = 1; i <= 101; ++i)
    for (int j = i + 1; j <= 101; ++j)
      pooled = pooled * modz(pts[i].x - pts[j].x, N) % N;
  if (pooled != 0) throw std::runtime_error("P20 pooled synchronization failed");

  std::vector<Row> synthetic = {{0, 1, 1, 57, 15, 0}, {1, 1, 2, 51, 60, 0}};
  Decoder d = decode_rows(synthetic);
  if (!d.ok || d.kernel.size() != 1) throw std::runtime_error("decoder self-test failed");
  BankResult br;
  br.curves = {{0, 1, 1, 31, 0, 0}, {1, 1, 1, 31, 0, 0}};
  br.rows_data = synthetic;
  Relation rel = verify_relation(d.kernel[0], cpp_int(77), br);
  if (rel.root_class != "USEFUL" || rel.gcd_minus != 7 || rel.gcd_plus != 11)
    throw std::runtime_error("normalized-root self-test failed");

  cpp_int u = 2, w = 3;
  cpp_int Fu = u * u * u + A * u + B;
  cpp_int Fw = w * w * w + A * w + B;
  cpp_int H = u * u + u * w + w * w + A;
  if (Fu - Fw != (u - w) * H) throw std::runtime_error("chord identity self-test failed");
  std::cout << "SELF_TEST_PASS p20_gcds=101,103 pooled=0 decoder_gcds=7,11\n";
}

std::vector<Case> make_preflight_cases() {
  std::set<std::string> used;
  std::vector<Case> out;
  int idx = 0;
  for (int bits : {12, 32, 60})
    for (int shape = 0; shape < 3; ++shape) {
      Case c;
      if (make_case(0, bits, shape, idx++, used, c)) out.push_back(c);
    }
  return out;
}

long double planned_full_work() {
  long double total = 0;
  for (int factor_bits : {12, 16, 20, 24, 32, 40, 48, 60}) {
    int nbits = 2 * factor_bits;
    std::vector<long double> family_work;
    for (const auto& f : FAMILIES) {
      long double r = planned_rows(f, nbits);
      family_work.push_back(std::max<long double>(1, r * r));
      total += 3.0L * 16.0L * std::max<long double>(1, r * r);
    }
    std::sort(family_work.begin(), family_work.end(), std::greater<long double>());
    for (int i = 0; i < 4; ++i)
      total += 3.0L * 16.0L * family_work[i];
  }
  return total;
}

long double planned_preflight_work(const std::vector<Case>& cases) {
  long double total = 0;
  for (const Case& c : cases)
    for (const auto& f : FAMILIES) {
      long double r = planned_rows(f, bitlen(c.N));
      total += std::max<long double>(1, r * r);
    }
  return total;
}

void preflight(const std::string& output, int workers) {
  auto cases = make_preflight_cases();
  std::vector<int> families(FAMILY_COUNT);
  std::iota(families.begin(), families.end(), 0);
  std::string metrics = output + ".metrics.tsv";
  std::string certs = output + ".certificates.jsonl";
  std::string cells = output + ".cells.tsv";
  std::string banks = output + ".banks.tsv";
  RunOutput r = run_cases(cases, families, workers, metrics, certs, cells, banks);
  long double ratio = planned_full_work() / planned_preflight_work(cases);
  long double projected = std::max<long double>(r.seconds, 0.001L) * ratio * 1.75L;
  bool pass = projected <= 12600.0L && r.peak_rss_kib <= 3670016ULL;
  std::ofstream out(output, std::ios::binary);
  out << "{\"version\":\"F265_V1\",\"cases\":" << cases.size()
      << ",\"families\":12,\"wall_seconds\":" << std::fixed << std::setprecision(6)
      << r.seconds << ",\"work_ratio\":" << static_cast<double>(ratio)
      << ",\"safety_multiplier\":1.75,\"projected_full_seconds\":"
      << static_cast<double>(projected) << ",\"peak_rss_kib\":" << r.peak_rss_kib
      << ",\"wall_gate_seconds\":12600,\"rss_gate_kib\":3670016,\"pass\":"
      << (pass ? "true" : "false") << "}\n";
  out.close();
  if (!pass) throw std::runtime_error("preflight projection rejected full packet");
}

int parse_workers(int argc, char** argv) {
  for (int i = 1; i + 1 < argc; ++i)
    if (std::string(argv[i]) == "--workers") return std::stoi(argv[i + 1]);
  return WORKERS_MAX;
}

std::string arg_value(int argc, char** argv, const std::string& key) {
  for (int i = 1; i + 1 < argc; ++i)
    if (std::string(argv[i]) == key) return argv[i + 1];
  throw std::runtime_error("missing argument " + key);
}

}  // namespace

int main(int argc, char** argv) {
  try {
    if (argc < 2) throw std::runtime_error("mode required");
    const std::string mode = argv[1];
    const int workers = parse_workers(argc, argv);
    if (mode == "--self-test") {
      self_test();
      return 0;
    }
    if (mode == "--preflight") {
      preflight(arg_value(argc, argv, "--output"), workers);
      return 0;
    }
    if (mode == "--select") {
      auto ids = make_selection(arg_value(argc, argv, "--metrics"),
                                arg_value(argc, argv, "--cohort-sha256"),
                                arg_value(argc, argv, "--output"));
      std::cout << "SELECTION";
      for (int id : ids) std::cout << ' ' << id;
      std::cout << '\n';
      return 0;
    }
    if (mode == "--summarize") {
      summarize_heldout(arg_value(argc, argv, "--metrics"),
                        arg_value(argc, argv, "--cells"),
                        arg_value(argc, argv, "--selection"),
                        arg_value(argc, argv, "--output"));
      return 0;
    }
    if (mode == "--discovery" || mode == "--heldout") {
      int split = mode == "--discovery" ? 0 : 1;
      int shortfall = 0;
      auto cases = make_corpus(split, &shortfall);
      write_cohort(arg_value(argc, argv, "--cohort"), cases, shortfall);
      std::vector<int> families;
      if (split == 0) {
        families.resize(FAMILY_COUNT);
        std::iota(families.begin(), families.end(), 0);
      } else {
        families = read_selection(arg_value(argc, argv, "--selection"));
      }
      RunOutput result = run_cases(cases, families, workers,
                                   arg_value(argc, argv, "--metrics"),
                                   arg_value(argc, argv, "--certificates"),
                                   arg_value(argc, argv, "--cells"),
                                   arg_value(argc, argv, "--banks"));
      std::cout << (split == 0 ? "DISCOVERY" : "HELDOUT")
                << " cases=" << cases.size() << " shortfall=" << shortfall
                << " wall_seconds=" << std::fixed << std::setprecision(6)
                << result.seconds << " peak_rss_kib=" << result.peak_rss_kib << '\n';
      return 0;
    }
    throw std::runtime_error("unknown mode " + mode);
  } catch (const std::exception& e) {
    std::cerr << "F265_ERROR " << e.what() << '\n';
    return 2;
  }
}
