#include <algorithm>
#include <array>
#include <atomic>
#include <chrono>
#include <cstdlib>
#include <cstdint>
#include <cstring>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <limits>
#include <map>
#include <mutex>
#include <set>
#include <sstream>
#include <stdexcept>
#include <string>
#include <thread>
#include <tuple>
#include <utility>
#include <vector>

#include <sys/resource.h>
#include <sys/stat.h>

#include <boost/multiprecision/cpp_int.hpp>

using boost::multiprecision::cpp_int;
using u64 = std::uint64_t;
using u128 = __uint128_t;

namespace {

constexpr u64 MASTER_SEED = 0xF26651D17A11C0DEULL;
constexpr int MAX_WORKERS = 8;
constexpr int MAX_ROWS = 96;
constexpr int MAX_GCD_FREE_STEPS = 25000;
constexpr int MAX_BLOCKS = 4096;
constexpr int MAX_TOTAL_ROW_BITS = 65536;
constexpr int MAX_CERTIFICATES = 64;
constexpr u64 OUTPUT_CAP = 1073741824ULL;
constexpr int DISCOVERY_BITS[] = {12, 16, 20, 24, 32};
constexpr int HELDOUT_BITS[] = {40, 48, 56, 60};
constexpr const char* SHAPES[] = {"random", "neighbor", "safe-safe"};

[[noreturn]] void fail(const std::string& message) {
  throw std::runtime_error(message);
}

void require(bool condition, const std::string& message) {
  if (!condition) fail(message);
}

u64 mix64(u64 x) {
  x += 0x9e3779b97f4a7c15ULL;
  x = (x ^ (x >> 30)) * 0xbf58476d1ce4e5b9ULL;
  x = (x ^ (x >> 27)) * 0x94d049bb133111ebULL;
  return x ^ (x >> 31);
}

struct Rng {
  u64 state;
  explicit Rng(u64 seed) : state(seed) {}
  u64 next() {
    state += 0x9e3779b97f4a7c15ULL;
    u64 z = state;
    z = (z ^ (z >> 30)) * 0xbf58476d1ce4e5b9ULL;
    z = (z ^ (z >> 27)) * 0x94d049bb133111ebULL;
    return z ^ (z >> 31);
  }
};

class Sha256 {
 public:
  Sha256() { reset(); }
  void update(const unsigned char* data, std::size_t length) {
    total_ += length;
    while (length) {
      std::size_t take = std::min<std::size_t>(length, 64 - used_);
      std::memcpy(block_.data() + used_, data, take);
      used_ += take;
      data += take;
      length -= take;
      if (used_ == 64) {
        compress(block_.data());
        used_ = 0;
      }
    }
  }
  void update(const std::string& value) {
    update(reinterpret_cast<const unsigned char*>(value.data()), value.size());
  }
  std::string final_hex() {
    u64 bit_count = total_ * 8;
    block_[used_++] = 0x80;
    if (used_ > 56) {
      while (used_ < 64) block_[used_++] = 0;
      compress(block_.data());
      used_ = 0;
    }
    while (used_ < 56) block_[used_++] = 0;
    for (int i = 7; i >= 0; --i)
      block_[used_++] = static_cast<unsigned char>(bit_count >> (8 * i));
    compress(block_.data());
    std::ostringstream out;
    out << std::hex << std::setfill('0');
    for (std::uint32_t x : state_) out << std::setw(8) << x;
    return out.str();
  }

 private:
  std::array<std::uint32_t, 8> state_{};
  std::array<unsigned char, 64> block_{};
  std::size_t used_ = 0;
  u64 total_ = 0;
  static std::uint32_t rotr(std::uint32_t x, int n) {
    return (x >> n) | (x << (32 - n));
  }
  void reset() {
    state_ = {0x6a09e667U, 0xbb67ae85U, 0x3c6ef372U, 0xa54ff53aU,
              0x510e527fU, 0x9b05688cU, 0x1f83d9abU, 0x5be0cd19U};
    used_ = 0;
    total_ = 0;
  }
  void compress(const unsigned char* b) {
    static constexpr std::uint32_t K[64] = {
      0x428a2f98U,0x71374491U,0xb5c0fbcfU,0xe9b5dba5U,0x3956c25bU,0x59f111f1U,0x923f82a4U,0xab1c5ed5U,
      0xd807aa98U,0x12835b01U,0x243185beU,0x550c7dc3U,0x72be5d74U,0x80deb1feU,0x9bdc06a7U,0xc19bf174U,
      0xe49b69c1U,0xefbe4786U,0x0fc19dc6U,0x240ca1ccU,0x2de92c6fU,0x4a7484aaU,0x5cb0a9dcU,0x76f988daU,
      0x983e5152U,0xa831c66dU,0xb00327c8U,0xbf597fc7U,0xc6e00bf3U,0xd5a79147U,0x06ca6351U,0x14292967U,
      0x27b70a85U,0x2e1b2138U,0x4d2c6dfcU,0x53380d13U,0x650a7354U,0x766a0abbU,0x81c2c92eU,0x92722c85U,
      0xa2bfe8a1U,0xa81a664bU,0xc24b8b70U,0xc76c51a3U,0xd192e819U,0xd6990624U,0xf40e3585U,0x106aa070U,
      0x19a4c116U,0x1e376c08U,0x2748774U,0x34b0bcb5U,0x391c0cb3U,0x4ed8aa4aU,0x5b9cca4fU,0x682e6ff3U,
      0x748f82eeU,0x78a5636fU,0x84c87814U,0x8cc70208U,0x90befffaU,0xa4506cebU,0xbef9a3f7U,0xc67178f2U
    };
    std::uint32_t w[64];
    for (int i = 0; i < 16; ++i)
      w[i] = (std::uint32_t(b[4*i]) << 24) |
             (std::uint32_t(b[4*i+1]) << 16) |
             (std::uint32_t(b[4*i+2]) << 8) | b[4*i+3];
    for (int i = 16; i < 64; ++i) {
      auto s0 = rotr(w[i-15],7) ^ rotr(w[i-15],18) ^ (w[i-15] >> 3);
      auto s1 = rotr(w[i-2],17) ^ rotr(w[i-2],19) ^ (w[i-2] >> 10);
      w[i] = w[i-16] + s0 + w[i-7] + s1;
    }
    auto a=state_[0], b0=state_[1], c=state_[2], d=state_[3];
    auto e=state_[4], f=state_[5], g=state_[6], h=state_[7];
    for (int i = 0; i < 64; ++i) {
      auto s1=rotr(e,6)^rotr(e,11)^rotr(e,25);
      auto ch=(e&f)^((~e)&g);
      auto t1=h+s1+ch+K[i]+w[i];
      auto s0=rotr(a,2)^rotr(a,13)^rotr(a,22);
      auto maj=(a&b0)^(a&c)^(b0&c);
      auto t2=s0+maj;
      h=g; g=f; f=e; e=d+t1; d=c; c=b0; b0=a; a=t1+t2;
    }
    state_[0]+=a; state_[1]+=b0; state_[2]+=c; state_[3]+=d;
    state_[4]+=e; state_[5]+=f; state_[6]+=g; state_[7]+=h;
  }
};

std::string sha256_bytes(const std::string& bytes) {
  Sha256 h;
  h.update(bytes);
  return h.final_hex();
}

std::string read_file(const std::string& path) {
  std::ifstream input(path, std::ios::binary);
  require(bool(input), "open input: " + path);
  std::ostringstream out;
  out << input.rdbuf();
  require(input.good() || input.eof(), "read input: " + path);
  return out.str();
}

std::string sha256_file(const std::string& path) {
  std::ifstream input(path, std::ios::binary);
  require(bool(input), "open hash input: " + path);
  Sha256 hash;
  std::array<unsigned char,65536> buffer{};
  for (;;) {
    input.read(reinterpret_cast<char*>(buffer.data()), buffer.size());
    std::streamsize got=input.gcount();
    if (got>0) hash.update(buffer.data(),static_cast<std::size_t>(got));
    if (input.eof()) break;
    require(bool(input), "read hash input: " + path);
  }
  return hash.final_hex();
}

cpp_int absz(cpp_int value) {
  if (value<0) value=-value;
  return value;
}

cpp_int modz(cpp_int value, const cpp_int& modulus) {
  value %= modulus;
  if (value < 0) value += modulus;
  return value;
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

cpp_int invmod(cpp_int a, const cpp_int& modulus) {
  a = modz(a, modulus);
  cpp_int old_r = a, r = modulus, old_s = 1, s = 0;
  while (r != 0) {
    cpp_int q = old_r / r;
    cpp_int next_r = old_r - q * r;
    old_r = r;
    r = next_r;
    cpp_int next_s = old_s - q * s;
    old_s = s;
    s = next_s;
  }
  require(old_r == 1, "inverse of nonunit");
  return modz(old_s, modulus);
}

int bitlen(const cpp_int& value) {
  cpp_int x = absz(value);
  if (x == 0) return 0;
  return boost::multiprecision::msb(x) + 1;
}

cpp_int powz(cpp_int base, unsigned exponent) {
  cpp_int out = 1;
  while (exponent) {
    if (exponent & 1U) out *= base;
    base *= base;
    exponent >>= 1U;
  }
  return out;
}

bool squarez(const cpp_int& value, cpp_int* root = nullptr) {
  if (value < 0) return false;
  if (value == 0) {
    if (root) *root = 0;
    return true;
  }
  cpp_int x = cpp_int(1) << ((bitlen(value) + 1) / 2);
  for (;;) {
    cpp_int y = (x + value / x) >> 1;
    if (y >= x) break;
    x = y;
  }
  while ((x + 1) * (x + 1) <= value) ++x;
  while (x * x > value) --x;
  if (x * x != value) return false;
  if (root) *root = x;
  return true;
}

u64 hash_cpp(const cpp_int& value, u64 seed = MASTER_SEED) {
  cpp_int x = absz(value);
  u64 h = mix64(seed ^ static_cast<u64>(value < 0));
  while (x != 0) {
    u64 limb = static_cast<u64>(x & std::numeric_limits<u64>::max());
    h = mix64(h ^ limb);
    x >>= 64;
  }
  return mix64(h ^ static_cast<u64>(bitlen(value)));
}

cpp_int random_below(Rng& rng, const cpp_int& bound) {
  require(bound > 0, "random_below bound");
  int bits = bitlen(bound - 1);
  for (int attempt = 0; attempt < 256; ++attempt) {
    cpp_int x = 0;
    int produced = 0;
    while (produced < bits) {
      x |= cpp_int(rng.next()) << produced;
      produced += 64;
    }
    if (bits % 64) x &= (cpp_int(1) << bits) - 1;
    if (x < bound) return x;
  }
  fail("bounded random rejection exhausted");
}

u64 mul_mod(u64 a, u64 b, u64 modulus) {
  return static_cast<u64>((static_cast<u128>(a) * b) % modulus);
}

u64 pow_mod(u64 a, u64 exponent, u64 modulus) {
  u64 out = 1 % modulus;
  while (exponent) {
    if (exponent & 1) out = mul_mod(out, a, modulus);
    a = mul_mod(a, a, modulus);
    exponent >>= 1;
  }
  return out;
}

bool is_prime(u64 n) {
  if (n < 2) return false;
  for (u64 p : {2ULL,3ULL,5ULL,7ULL,11ULL,13ULL,17ULL,19ULL,23ULL,29ULL,31ULL,37ULL}) {
    if (n % p == 0) return n == p;
  }
  u64 d = n - 1, s = 0;
  while ((d & 1) == 0) { d >>= 1; ++s; }
  for (u64 a : {2ULL,325ULL,9375ULL,28178ULL,450775ULL,9780504ULL,1795265022ULL}) {
    if (a % n == 0) continue;
    u64 x = pow_mod(a % n, d, n);
    if (x == 1 || x == n - 1) continue;
    bool witness = true;
    for (u64 r = 1; r < s; ++r) {
      x = mul_mod(x, x, n);
      if (x == n - 1) { witness = false; break; }
    }
    if (witness) return false;
  }
  return true;
}

u64 random_exact_bit_prime(Rng& rng, int bits, int cap = 200000) {
  require(bits >= 3 && bits <= 63, "prime bit range");
  u64 mask = bits == 64 ? ~u64(0) : ((u64(1) << bits) - 1);
  for (int i = 0; i < cap; ++i) {
    u64 x = rng.next() & mask;
    x |= u64(1) << (bits - 1);
    x |= 1;
    if (is_prime(x)) return x;
  }
  fail("ordinary prime cap");
}

u64 random_safe_prime(Rng& rng, int bits, int cap = 1000000) {
  require(bits >= 4, "safe prime bit range");
  u64 mask=(u64(1)<<(bits-1))-1;
  for (int i = 0; i < cap; ++i) {
    u64 r=rng.next()&mask;
    r|=u64(1)<<(bits-2);
    r|=1;
    if (!is_prime(r)) continue;
    u64 p = 2 * r + 1;
    if (bitlen(cpp_int(p)) == bits && is_prime(p)) return p;
  }
  fail("safe prime cap");
}

u64 next_prime_bounded(u64 start, int bits, int cap = 200000) {
  u64 x = start | 1ULL;
  u64 lower = u64(1) << (bits - 1);
  u64 upper = u64(1) << bits;
  if (x < lower) x = lower | 1ULL;
  for (int i = 0; i < cap && x < upper; ++i, x += 2)
    if (is_prime(x)) return x;
  fail("neighbor prime cap");
}

struct Case {
  std::string split;
  std::string shape;
  int factor_bits = 0;
  int index = 0;
  cpp_int N;
  u64 p = 0;
  u64 q = 0;
};

std::vector<Case> make_cases(const std::string& split, bool preflight = false,
                             const std::set<std::string>& forbidden = {}) {
  const int* sizes = split == "discovery" ? DISCOVERY_BITS : HELDOUT_BITS;
  int size_count = split == "discovery" ? 5 : 4;
  int target = preflight ? (split == "discovery" ? 1 : 2) :
                           (split == "discovery" ? 16 : 32);
  std::set<std::string> used=forbidden;
  std::vector<Case> out;
  for (int bi = 0; bi < size_count; ++bi) {
    int bits = sizes[bi];
    for (int si = 0; si < 3; ++si) {
      std::string shape = SHAPES[si];
      for (int index = 0; index < target; ++index) {
        bool accepted = false;
        for (int retry = 0; retry < 128 && !accepted; ++retry) {
          u64 seed = mix64(MASTER_SEED ^ hash_cpp(cpp_int(bits), 0x434f52505553ULL) ^
                           mix64(static_cast<u64>(si * 100000 + index * 257 + retry)) ^
                           (split == "heldout" ? 0x48454c444f5554ULL : 0x444953434f5645ULL));
          Rng rng(seed);
          u64 p = 0, q = 0;
          if (shape == "safe-safe") {
            p = random_safe_prime(rng, bits);
            q = random_safe_prime(rng, bits);
          } else if (shape == "neighbor") {
            p = random_exact_bit_prime(rng, bits);
            u64 offset = 2 * (1 + (rng.next() % 127));
            if (p > std::numeric_limits<u64>::max() - offset - 2) continue;
            q = next_prime_bounded(p + offset, bits);
          } else {
            p = random_exact_bit_prime(rng, bits);
            q = random_exact_bit_prime(rng, bits);
          }
          if (p == q) continue;
          if (p > q) std::swap(p, q);
          if (static_cast<u128>(q) >= static_cast<u128>(2) * p) continue;
          cpp_int N = cpp_int(p) * q;
          std::string key = N.convert_to<std::string>();
          if (!used.insert(key).second) continue;
          out.push_back({split, shape, bits, index, N, p, q});
          accepted = true;
        }
        require(accepted, "corpus pair retry cap");
      }
    }
  }
  return out;
}

struct Mat2 {
  long long a = 1, b = 0, c = 0, d = 1;
};

Mat2 multiply(const Mat2& x, const Mat2& y) {
  return {x.a*y.a+x.b*y.c, x.a*y.b+x.b*y.d,
          x.c*y.a+x.d*y.c, x.c*y.b+x.d*y.d};
}

long long determinant(const Mat2& x) { return x.a*x.d-x.b*x.c; }

std::array<long long,4> matrix_tuple(const Mat2& x) {
  return {x.a,x.b,x.c,x.d};
}

Mat2 canonical_sign(Mat2 x) {
  Mat2 y{-x.a,-x.b,-x.c,-x.d};
  if (matrix_tuple(y) < matrix_tuple(x)) return y;
  return x;
}

struct WordMatrix {
  Mat2 matrix;
  int length = 0;
  int last = -1;
  std::string syntax;
};

const std::vector<WordMatrix>& word_pool() {
  static const std::vector<WordMatrix> pool = [] {
    const std::array<Mat2,5> generator = {
      Mat2{1,1,0,1}, Mat2{1,-1,0,1}, Mat2{1,0,1,1},
      Mat2{1,0,-1,1}, Mat2{0,-1,1,0}
    };
    const std::array<const char*,5> name = {"U+","U-","L+","L-","S"};
    const std::array<int,5> inverse = {1,0,3,2,4};
    std::vector<WordMatrix> all{{Mat2{},0,-1,"I"}};
    std::vector<WordMatrix> frontier = all;
    std::map<std::array<long long,4>,WordMatrix> unique;
    unique[matrix_tuple(Mat2{})] = all[0];
    for (int length = 1; length <= 7; ++length) {
      std::vector<WordMatrix> next;
      for (const WordMatrix& parent : frontier) {
        for (int g = 0; g < 5; ++g) {
          if (parent.last >= 0 && inverse[parent.last] == g) continue;
          Mat2 raw = multiply(parent.matrix, generator[g]);
          require(determinant(raw) == 1, "SL2 word determinant");
          Mat2 canon = canonical_sign(raw);
          for (long long entry : matrix_tuple(canon))
            require(std::llabs(entry) <= 128, "matrix entry bound");
          std::string syntax = parent.syntax == "I" ? name[g] : parent.syntax + "." + name[g];
          WordMatrix row{canon,length,g,syntax};
          next.push_back(row);
          auto key = matrix_tuple(canon);
          auto it = unique.find(key);
          if (it == unique.end() ||
              std::tie(row.length,row.syntax) < std::tie(it->second.length,it->second.syntax))
            unique[key] = row;
        }
      }
      frontier.swap(next);
    }
    std::vector<WordMatrix> result;
    for (const auto& item : unique) result.push_back(item.second);
    std::sort(result.begin(), result.end(), [](const WordMatrix& x, const WordMatrix& y) {
      return std::tie(x.length,x.syntax) < std::tie(y.length,y.syntax);
    });
    return result;
  }();
  return pool;
}

struct Family {
  int id;
  const char* mode;
  int max_length;
  int matrix_cap;
};

const std::array<Family,8> FAMILIES = {{
  {0,"uniform",3,16}, {1,"small",5,20}, {2,"adjacent",7,24},
  {3,"symmetric",6,24}, {4,"inverse",7,24}, {5,"affine",6,24},
  {6,"central",5,20}, {7,"power",7,24}
}};

std::vector<WordMatrix> select_matrices(const cpp_int& N, const Family& family,
                                        int base_id) {
  std::vector<std::pair<u64,WordMatrix>> ranked;
  WordMatrix identity;
  bool have_identity = false;
  u64 nh = hash_cpp(N, MASTER_SEED ^ static_cast<u64>(family.id * 17 + base_id));
  for (const WordMatrix& word : word_pool()) {
    if (word.length > family.max_length) continue;
    if (word.length == 0) { identity = word; have_identity = true; continue; }
    u64 h = nh;
    for (unsigned char c : word.syntax) h = mix64(h ^ c);
    ranked.push_back({h,word});
  }
  require(have_identity, "identity word absent");
  std::sort(ranked.begin(), ranked.end(), [](const auto& x, const auto& y) {
    return std::tie(x.first,x.second.syntax) < std::tie(y.first,y.second.syntax);
  });
  std::vector<WordMatrix> out{identity};
  for (int i = 0; i + 1 < family.matrix_cap && i < static_cast<int>(ranked.size()); ++i)
    out.push_back(ranked[i].second);
  return out;
}

struct ProjectiveRoot { cpp_int numerator, denominator; };

struct BaseSource {
  int base_id = 0;
  cpp_int a, r, s;
  cpp_int lifted_a, lifted_r, lifted_s;
};

struct Row {
  int base_id = 0;
  int level = 1;
  bool identity = false;
  std::string syntax;
  Mat2 matrix;
  cpp_int modulus;
  cpp_int A0,B0,C0,delta0;
  cpp_int A,B,C,discriminant,value,root,carry;
  ProjectiveRoot pr, ps;
};

struct Relation {
  std::vector<int> columns;
  std::string label;
  std::string root_class;
  cpp_int exact_root, supplied_root, normalized_root, gcd_minus, gcd_plus;
};

struct OpaqueBlock {
  cpp_int value;
  std::vector<std::pair<int,std::uint32_t>> exponents;
  bool square = false;
  std::string status;
};

struct EvidenceCertificate {
  bool present = false;
  std::string kind;
  std::string label;
  std::string root_class;
  cpp_int numerator = 0;
  cpp_int divisor = 1;
  cpp_int candidate = 0;
  cpp_int factor = 1;
  cpp_int exact_root = 0;
  cpp_int supplied_root = 0;
  cpp_int normalized_root = 0;
  cpp_int gcd_minus = 1;
  cpp_int gcd_plus = 1;
  std::vector<Row> witnesses;
};

enum DirectStage {
  // Stage 1: source candidates a, r, s, r-s, and inverse-family seed u.
  DIRECT_SOURCE = 0,
  // Stage 2: A0, B0, C0, delta0, and the supplied discriminant root.
  DIRECT_BASE = 1,
  // Stage 3: transformed A, B, C, and discriminant.
  DIRECT_TRANSFORMED = 2,
  // Stage 4: projective coordinates and own/cross determinants.
  DIRECT_PROJECTIVE = 3,
  // Stage 5: exact pairwise Sylvester resultants.
  DIRECT_RESULTANT = 4,
  // Stage 6: invariant carries and same/cross-level quotients.
  DIRECT_CARRY = 5,
  // Stage 7: both signed singleton normalized-root gcds.
  DIRECT_SINGLETON = 6,
  // Stage 8: both signed equal-row/square-template normalized-root gcds.
  DIRECT_EQUAL_OR_TEMPLATE = 7
};

const std::array<const char*,8> DIRECT_STAGE_NAMES = {{
  "source", "base", "transformed", "projective", "resultant", "carry",
  "singleton", "equal_or_template"
}};

struct DirectCounter {
  u64 tests = 0;
  u64 unit = 0;
  u64 full = 0;
  u64 proper = 0;
};

struct BankResult {
  int family = 0;
  bool eligible = false;
  bool resource_reject = false;
  bool early_factor = false;
  bool carry_factor = false;
  bool strict_carry = false;
  bool strict_base_singleton = false;
  bool strict_orbit_singleton = false;
  bool strict_square_multiple = false;
  bool strict_equal_row = false;
  bool any_factor = false;
  cpp_int first_factor = 1;
  cpp_int first_candidate = 0;
  std::string first_channel;
  std::string error;
  std::vector<Row> rows;
  std::vector<OpaqueBlock> opaque_blocks;
  EvidenceCertificate first_certificate;
  bool strict_certificate_emitted = false;
  u64 generated_rows=0, coefficient_aliases=0, matrix_aliases=0;
  u64 tested_rows=0;
  u64 pairs=0, resultants=0, root_determinants=0, carry_tests=0;
  u64 base_singletons=0, orbit_singletons=0, useful_base_singletons=0;
  u64 useful_orbit_singletons=0, equal_rows=0, square_multiples=0;
  u64 useful_square_multiples=0, residual_rows=0, blocks=0;
  u64 baseline_rows=0;
  u64 gcd_free_steps=0, rank=0, nullity=0, private_columns=0;
  u64 relations=0, useful_relations=0, strict_multirow=0;
  u64 global_plus=0, global_minus=0;
  std::array<DirectCounter,8> direct{};
};

bool record_factor(BankResult& result, const cpp_int& candidate, const cpp_int& N,
                   const std::string& channel, bool carry = false,
                   int direct_stage = -1) {
  cpp_int g = gcdz(candidate,N);
  if (direct_stage >= 0) {
    require(direct_stage < static_cast<int>(result.direct.size()),"direct stage range");
    DirectCounter& counter=result.direct[direct_stage];
    ++counter.tests;
    if (g==1) ++counter.unit;
    else if (g==N) ++counter.full;
    else ++counter.proper;
  }
  if (g <= 1 || g >= N) return false;
  result.any_factor = true;
  if (carry) result.carry_factor = true;
  else result.early_factor = true;
  if (result.first_factor == 1) {
    result.first_factor = g;
    result.first_candidate = candidate;
    result.first_channel = channel;
  }
  return true;
}

bool record_ticket(BankResult& result, const cpp_int& candidate, const cpp_int& N,
                   const std::string& channel, const std::vector<Row>& witnesses = {},
                   const cpp_int& numerator = 0, const cpp_int& divisor = 1,
                   bool carry = false, int direct_stage = -1) {
  bool first = result.first_factor == 1;
  bool useful = record_factor(result,candidate,N,channel,carry,direct_stage);
  if (useful && first) {
    result.first_certificate.present = true;
    result.first_certificate.kind = carry ? "CARRY_TICKET" : "DIRECT_TICKET";
    result.first_certificate.label = channel;
    result.first_certificate.numerator = numerator == 0 ? candidate : numerator;
    result.first_certificate.divisor = divisor;
    result.first_certificate.candidate = candidate;
    result.first_certificate.factor = result.first_factor;
    result.first_certificate.witnesses = witnesses;
  }
  return useful;
}

bool screened_unit(const cpp_int& value, const cpp_int& N, BankResult& result,
                   const std::string& channel) {
  cpp_int g = gcdz(value,N);
  record_ticket(result,value,N,channel,{},0,1,false,DIRECT_SOURCE);
  if (g == 1) return true;
  return false;
}

BaseSource choose_base(const cpp_int& N, const Family& family, int base_id,
                       BankResult& result) {
  Rng rng(hash_cpp(N, MASTER_SEED ^ mix64(static_cast<u64>(family.id * 4099 + base_id))));
  int n = bitlen(N);
  for (int attempt = 0; attempt < 128; ++attempt) {
    cpp_int a = 1 + random_below(rng,N-1);
    if (!screened_unit(a,N,result,"SOURCE_A")) {
      if (result.any_factor) return {};
      continue;
    }
    cpp_int r, s;
    std::string mode=family.mode;
    if (mode=="small") {
      cpp_int bound=cpp_int(n)*n*n+31;
      if (bound>N-1) bound=N-1;
      r=1+random_below(rng,bound);
      s=1+random_below(rng,bound);
    } else if (mode=="central") {
      cpp_int lo=N/4, width=N/2;
      if (width<1) width=1;
      r=lo+random_below(rng,width);
      s=lo+random_below(rng,width);
    } else {
      cpp_int u=1+random_below(rng,N-1);
      if (mode=="adjacent") { r=u; s=modz(u+1,N); }
      else if (mode=="symmetric") { r=u; s=modz(-u,N); }
      else if (mode=="inverse") {
        if (!screened_unit(u,N,result,"SOURCE_INVERSE_SEED")) {
          if (result.any_factor) return {};
          continue;
        }
        r=u; s=invmod(u,N);
      } else if (mode=="affine") { r=u; s=modz(2*u+1,N); }
      else if (mode=="power") { r=modz(u*u,N); s=modz(r*u,N); }
      else { r=u; s=1+random_below(rng,N-1); }
    }
    bool ok=true;
    for (const auto& item : std::array<std::pair<cpp_int,std::string>,3>{{
           {r,"SOURCE_R"},{s,"SOURCE_S"},{r-s,"SOURCE_ROOT_DIFFERENCE"}}}) {
      if (!screened_unit(item.first,N,result,item.second)) {
        if (result.any_factor) return {};
        ok=false;
      }
    }
    if (!ok || modz(r-s,N)==0) continue;
    r=modz(r,N); s=modz(s,N);
    if (s<r) std::swap(r,s);
    Rng lift(hash_cpp(N, MASTER_SEED ^ 0x4c4946545f424153ULL ^
                     mix64(static_cast<u64>(family.id * 4099 + base_id))));
    cpp_int lifted_a=a+N*random_below(lift,N);
    cpp_int lifted_r=r+N*random_below(lift,N);
    cpp_int lifted_s=s+N*random_below(lift,N);
    return {base_id,a,r,s,lifted_a,lifted_r,lifted_s};
  }
  result.resource_reject=true;
  result.error="SOURCE_ATTEMPT_CAP";
  return {};
}

cpp_int determinant_bareiss(std::vector<std::vector<cpp_int>> a) {
  int n=static_cast<int>(a.size());
  require(n>0,"empty determinant");
  for (const auto& row:a) require(static_cast<int>(row.size())==n,"nonsquare determinant");
  cpp_int denominator=1;
  int sign=1;
  for (int k=0;k<n-1;++k) {
    int pivot=k;
    while (pivot<n && a[pivot][k]==0) ++pivot;
    if (pivot==n) return 0;
    if (pivot!=k) { std::swap(a[pivot],a[k]); sign=-sign; }
    cpp_int p=a[k][k];
    for (int i=k+1;i<n;++i) {
      for (int j=k+1;j<n;++j) {
        cpp_int numerator=a[i][j]*p-a[i][k]*a[k][j];
        require(numerator%denominator==0,"Bareiss nonexact division");
        a[i][j]=numerator/denominator;
      }
    }
    denominator=p;
    for (int i=k+1;i<n;++i) a[i][k]=0;
  }
  return sign*a[n-1][n-1];
}

cpp_int quadratic_resultant(const Row& x, const Row& y) {
  return determinant_bareiss({
    {x.A,x.B,x.C,0}, {0,x.A,x.B,x.C},
    {y.A,y.B,y.C,0}, {0,y.A,y.B,y.C}
  });
}

cpp_int quadratic_resultant_formula(const Row& x, const Row& y) {
  cpp_int u=x.A*y.C-x.C*y.A;
  cpp_int v=x.A*y.B-x.B*y.A;
  cpp_int w=x.B*y.C-x.C*y.B;
  return u*u-v*w;
}

std::array<cpp_int,3> coefficient_key_values(const Row& row) {
  return {row.A,row.B,row.C};
}

Row make_row(const cpp_int& N, const BaseSource& base,
             const WordMatrix& word, int level) {
  cpp_int m=N;
  if (level==2) m*=N;
  cpp_int a=level==1 ? base.a : base.lifted_a;
  cpp_int r=level==1 ? base.r : base.lifted_r;
  cpp_int s=level==1 ? base.s : base.lifted_s;
  cpp_int A0=modz(a,m);
  cpp_int B0=modz(-a*(r+s),m);
  cpp_int C0=modz(a*r*s,m);
  cpp_int delta0=B0*B0-4*A0*C0;
  cpp_int root=modz(base.a*(base.r-base.s),N);
  if (N-root<root) root=N-root;
  const Mat2& q=word.matrix;
  cpp_int Astar=A0*q.a*q.a+B0*q.a*q.c+C0*q.c*q.c;
  cpp_int Bstar=2*A0*q.a*q.b+B0*(q.a*q.d+q.b*q.c)+2*C0*q.c*q.d;
  cpp_int Cstar=A0*q.b*q.b+B0*q.b*q.d+C0*q.d*q.d;
  require(Bstar*Bstar-4*Astar*Cstar==delta0,"exact discriminant invariance");
  cpp_int A=modz(Astar,m),B=modz(Bstar,m),C=modz(Cstar,m);
  cpp_int D=B*B-4*A*C;
  require((D-delta0)%m==0,"canonical discriminant divisibility");
  cpp_int value=D;
  if (D<=0) value+=4*m*m;
  require(value>0 && value<=4*m*m,"positive row bound");
  int n=bitlen(N);
  require(bitlen(value)<=2*level*n+2,"row bit bound");
  require(modz(value-root*root,N)==0,"supplied root congruence");
  cpp_int carry=(value-delta0)/m;
  ProjectiveRoot pr{modz(cpp_int(q.d)*base.r-q.b,N),
                    modz(cpp_int(q.a)-cpp_int(q.c)*base.r,N)};
  ProjectiveRoot ps{modz(cpp_int(q.d)*base.s-q.b,N),
                    modz(cpp_int(q.a)-cpp_int(q.c)*base.s,N)};
  require(!(pr.numerator==0 && pr.denominator==0),"zero first projective root");
  require(!(ps.numerator==0 && ps.denominator==0),"zero second projective root");
  cpp_int projective_delta=pr.numerator*ps.denominator-ps.numerator*pr.denominator;
  require(modz(projective_delta-(base.r-base.s),N)==0,"projective determinant identity");
  Row row;
  row.base_id=base.base_id; row.level=level; row.identity=word.length==0;
  row.syntax=word.syntax; row.matrix=q; row.modulus=m;
  row.A0=A0;row.B0=B0;row.C0=C0;row.delta0=delta0;
  row.A=A;row.B=B;row.C=C;row.discriminant=D;row.value=value;
  row.root=root;row.carry=carry;row.pr=pr;row.ps=ps;
  return row;
}

void generate_rows(const cpp_int& N, const Family& family, BankResult& result) {
  std::set<std::tuple<int,int,cpp_int,cpp_int,cpp_int>> coefficient_seen;
  std::set<std::tuple<int,long long,long long,long long,long long>> matrix_seen;
  std::vector<BaseSource> bases;
  for (int base_id=0;base_id<2;++base_id) {
    BaseSource base=choose_base(N,family,base_id,result);
    if (result.resource_reject || result.any_factor || base.a==0) return;
    bases.push_back(std::move(base));
  }
  for (const BaseSource& base:bases) {
    int base_id=base.base_id;
    std::vector<WordMatrix> matrices=select_matrices(N,family,base_id);
    for (const auto& word:matrices) {
      auto mt=matrix_tuple(word.matrix);
      auto mk=std::make_tuple(base_id,mt[0],mt[1],mt[2],mt[3]);
      if (!matrix_seen.insert(mk).second) { ++result.matrix_aliases; continue; }
      for (int level=1;level<=2;++level) {
        Row row=make_row(N,base,word,level);
        ++result.generated_rows;
        auto key=std::make_tuple(base_id,level,row.A,row.B,row.C);
        if (!coefficient_seen.insert(key).second) { ++result.coefficient_aliases; continue; }
        result.rows.push_back(std::move(row));
      }
    }
  }
  require(result.rows.size()<=MAX_ROWS,"static row cap");
}

std::string classify_root(const cpp_int& exact_root, const cpp_int& supplied,
                          const cpp_int& N, cpp_int& gm, cpp_int& gp,
                          cpp_int& normalized) {
  cpp_int r=modz(exact_root,N),x=modz(supplied,N);
  require(gcdz(x,N)==1,"nonunit supplied root");
  gm=gcdz(r-x,N); gp=gcdz(r+x,N);
  normalized=modz(r*invmod(x,N),N);
  if (r==x) return "GLOBAL_PLUS";
  if (r==modz(-x,N)) return "GLOBAL_MINUS";
  if ((gm>1 && gm<N)||(gp>1 && gp<N)) return "USEFUL";
  fail("invalid square-root classification");
}

bool same_square_class(const cpp_int& a, const cpp_int& b, cpp_int* exact_root=nullptr) {
  cpp_int g=gcdz(a,b),ra=a/g,rb=b/g,sa,sb;
  if (!squarez(ra,&sa)||!squarez(rb,&sb)) return false;
  cpp_int root=g*sa*sb;
  require(root*root==a*b,"square-class product verification");
  if (exact_root) *exact_root=root;
  return true;
}

struct Block {
  cpp_int value;
  std::vector<std::uint32_t> exponents;
};

struct Decoder {
  bool ok=false, resource_reject=false;
  std::string error;
  std::vector<Block> blocks;
  std::vector<std::vector<u64>> kernel;
  u64 steps=0, rank=0, private_columns=0;
};

bool bit_get(const std::vector<u64>& row, int column) {
  return ((row[column>>6]>>(column&63))&1ULL)!=0;
}

void bit_flip(std::vector<u64>& row, int column) {
  row[column>>6]^=1ULL<<(column&63);
}

void bit_xor(std::vector<u64>& a, const std::vector<u64>& b) {
  for (std::size_t i=0;i<a.size();++i) a[i]^=b[i];
}

int bit_weight(const std::vector<u64>& row) {
  int out=0;
  for (u64 word:row) out+=__builtin_popcountll(word);
  return out;
}

Decoder decode_rows(const std::vector<Row>& rows) {
  Decoder decoder;
  int m=static_cast<int>(rows.size());
  int total_bits=0;
  for (const Row& row:rows) total_bits+=bitlen(row.value);
  if (total_bits>MAX_TOTAL_ROW_BITS) {
    decoder.resource_reject=true; decoder.error="TOTAL_ROW_BITS_CAP"; return decoder;
  }
  for (int i=0;i<m;++i) {
    require(rows[i].value>0,"nonpositive decoder row");
    if (rows[i].value==1) continue;
    Block block{rows[i].value,std::vector<std::uint32_t>(m,0)};
    block.exponents[i]=1;
    decoder.blocks.push_back(std::move(block));
  }
  bool changed=true;
  while (changed) {
    changed=false;
    for (std::size_t i=0;i<decoder.blocks.size()&&!changed;++i) {
      for (std::size_t j=i+1;j<decoder.blocks.size();++j) {
        cpp_int g=gcdz(decoder.blocks[i].value,decoder.blocks[j].value);
        if (g==1) continue;
        Block left=decoder.blocks[i],right=decoder.blocks[j];
        cpp_int left_cofactor=left.value/g,right_cofactor=right.value/g;
        std::vector<std::uint32_t> shared(m);
        for (int k=0;k<m;++k) {
          u64 sum=static_cast<u64>(left.exponents[k])+right.exponents[k];
          require(sum<=std::numeric_limits<std::uint32_t>::max(),"exponent overflow");
          shared[k]=static_cast<std::uint32_t>(sum);
        }
        decoder.blocks.erase(decoder.blocks.begin()+j);
        decoder.blocks.erase(decoder.blocks.begin()+i);
        if (left_cofactor>1) decoder.blocks.push_back({left_cofactor,std::move(left.exponents)});
        if (right_cofactor>1) decoder.blocks.push_back({right_cofactor,std::move(right.exponents)});
        decoder.blocks.push_back({g,std::move(shared)});
        ++decoder.steps;
        if (decoder.steps>MAX_GCD_FREE_STEPS||decoder.blocks.size()>MAX_BLOCKS) {
          decoder.resource_reject=true;decoder.error="GCD_FREE_CAP";return decoder;
        }
        changed=true;
        break;
      }
    }
  }
  std::sort(decoder.blocks.begin(),decoder.blocks.end(),
            [](const Block& x,const Block& y){return x.value<y.value;});
  for (std::size_t i=0;i<decoder.blocks.size();++i)
    for (std::size_t j=i+1;j<decoder.blocks.size();++j)
      require(gcdz(decoder.blocks[i].value,decoder.blocks[j].value)==1,
              "final opaque blocks not coprime");
  for (int column=0;column<m;++column) {
    cpp_int rebuilt=1;
    for (const Block& block:decoder.blocks)
      if (block.exponents[column]) rebuilt*=powz(block.value,block.exponents[column]);
    require(rebuilt==rows[column].value,"decoder row reconstruction");
  }
  int words=(m+63)/64;
  std::vector<std::vector<u64>> matrix;
  std::set<int> private_columns;
  for (const Block& block:decoder.blocks) {
    if (squarez(block.value)) continue;
    std::vector<u64> equation(words,0);
    for (int column=0;column<m;++column)
      if (block.exponents[column]&1U) bit_flip(equation,column);
    int weight=bit_weight(equation);
    if (weight==1)
      for (int column=0;column<m;++column)
        if (bit_get(equation,column)) private_columns.insert(column);
    if (weight) matrix.push_back(std::move(equation));
  }
  std::vector<int> pivots;
  int rank=0;
  for (int column=0;column<m;++column) {
    int selected=-1;
    for (int row=rank;row<static_cast<int>(matrix.size());++row)
      if (bit_get(matrix[row],column)) {selected=row;break;}
    if (selected<0) continue;
    std::swap(matrix[rank],matrix[selected]);
    for (int row=0;row<static_cast<int>(matrix.size());++row)
      if (row!=rank&&bit_get(matrix[row],column)) bit_xor(matrix[row],matrix[rank]);
    pivots.push_back(column);
    ++rank;
  }
  std::vector<char> is_pivot(m,0);
  for (int column:pivots) is_pivot[column]=1;
  for (int free_column=0;free_column<m;++free_column) {
    if (is_pivot[free_column]) continue;
    std::vector<u64> vector(words,0);
    bit_flip(vector,free_column);
    for (int row=0;row<rank;++row)
      if (bit_get(matrix[row],free_column)) bit_flip(vector,pivots[row]);
    decoder.kernel.push_back(std::move(vector));
  }
  for (const auto& vector:decoder.kernel)
    for (const auto& equation:matrix) {
      unsigned parity=0;
      for (int word=0;word<words;++word)
        parity^=static_cast<unsigned>(__builtin_parityll(vector[word]&equation[word]));
      require(parity==0,"kernel verification");
    }
  decoder.rank=rank;
  decoder.private_columns=private_columns.size();
  decoder.ok=true;
  return decoder;
}

void screen_base_channels(const cpp_int& N, BankResult& result) {
  std::set<std::pair<int,int>> seen;
  for (const Row& row:result.rows) {
    if (!seen.insert({row.base_id,row.level}).second) continue;
    for (const auto& item : std::array<std::pair<cpp_int,std::string>,5>{{
           {row.A0,"BASE_COEFFICIENT_A"},{row.B0,"BASE_COEFFICIENT_B"},
           {row.C0,"BASE_COEFFICIENT_C"},{row.delta0,"BASE_DISCRIMINANT"},
           {row.root,"SUPPLIED_DISCRIMINANT_ROOT"}}})
      record_ticket(result,item.first,N,item.second,{row},0,1,false,DIRECT_BASE);
  }
}

void screen_transformed_channels(const cpp_int& N, BankResult& result) {
  for (const Row& row:result.rows)
    for (const auto& item : std::array<std::pair<cpp_int,std::string>,4>{{
           {row.A,"TRANSFORMED_COEFFICIENT_A"},{row.B,"TRANSFORMED_COEFFICIENT_B"},
           {row.C,"TRANSFORMED_COEFFICIENT_C"},{row.discriminant,"TRANSFORMED_DISCRIMINANT"}}})
      record_ticket(result,item.first,N,item.second,{row},0,1,false,DIRECT_TRANSFORMED);
}

void screen_projective_channels(const cpp_int& N, BankResult& result) {
  for (const Row& row:result.rows) {
    for (const auto& item : std::array<std::pair<cpp_int,std::string>,4>{{
           {row.pr.numerator,"PROJECTIVE_ROOT_NUMERATOR"},
           {row.pr.denominator,"PROJECTIVE_ROOT_DENOMINATOR"},
           {row.ps.numerator,"PROJECTIVE_ROOT_NUMERATOR"},
           {row.ps.denominator,"PROJECTIVE_ROOT_DENOMINATOR"}}})
      record_ticket(result,item.first,N,item.second,{row},0,1,false,DIRECT_PROJECTIVE);
    cpp_int determinant=row.pr.numerator*row.ps.denominator-
                        row.ps.numerator*row.pr.denominator;
    ++result.root_determinants;
    record_ticket(result,determinant,N,"PROJECTIVE_ROOT_DIFFERENCE",{row},0,1,false,
                  DIRECT_PROJECTIVE);
  }
  for (std::size_t i=0;i<result.rows.size();++i) {
    for (std::size_t j=i+1;j<result.rows.size();++j) {
      const Row& x=result.rows[i]; const Row& y=result.rows[j];
      std::array<ProjectiveRoot,2> xr{{x.pr,x.ps}},yr{{y.pr,y.ps}};
      for (const auto& a:xr) for (const auto& b:yr) {
        cpp_int cross=a.numerator*b.denominator-b.numerator*a.denominator;
        ++result.root_determinants;
        record_ticket(result,cross,N,"CROSS_PROJECTIVE_ROOT",{x,y},0,1,false,
                      DIRECT_PROJECTIVE);
      }
    }
  }
}

void screen_resultants(const cpp_int& N, BankResult& result) {
  for (std::size_t i=0;i<result.rows.size();++i) {
    for (std::size_t j=i+1;j<result.rows.size();++j) {
      ++result.pairs;
      const Row& x=result.rows[i]; const Row& y=result.rows[j];
      cpp_int res=quadratic_resultant(x,y);
      require(res==quadratic_resultant_formula(x,y),"quadratic resultant formula");
      ++result.resultants;
      record_ticket(result,res,N,"QUADRATIC_RESULTANT",{x,y},0,1,false,
                    DIRECT_RESULTANT);
    }
  }
}

void screen_carries(const cpp_int& N, BankResult& result) {
  for (const Row& row:result.rows) {
    ++result.carry_tests;
    bool before=result.any_factor;
    record_ticket(result,row.carry,N,"INVARIANT_CARRY",{row},
                  row.value-row.delta0,row.modulus,true,DIRECT_CARRY);
    if (!before&&result.any_factor) {
      result.strict_carry=true;
    }
  }
  for (std::size_t i=0;i<result.rows.size();++i) {
    for (std::size_t j=i+1;j<result.rows.size();++j) {
      const Row& x=result.rows[i];const Row& y=result.rows[j];
      if (x.base_id!=y.base_id) continue;
      cpp_int quotient;
      if (x.level==y.level) {
        require((x.value-y.value)%x.modulus==0,"same-level carry quotient");
        quotient=(x.value-y.value)/x.modulus;
      } else {
        require((x.value-y.value)%N==0,"cross-level carry quotient");
        quotient=(x.value-y.value)/N;
      }
      ++result.carry_tests;
      bool before=result.any_factor;
      cpp_int divisor=x.level==y.level ? x.modulus : N;
      record_ticket(result,quotient,N,x.level==y.level ?
                    "SAME_LEVEL_CARRY_QUOTIENT":"CROSS_LEVEL_CARRY_QUOTIENT",
                    {x,y},x.value-y.value,divisor,true,DIRECT_CARRY);
      if (!before&&result.any_factor) {
        result.strict_carry=true;
      }
    }
  }
}

void screen_singletons_and_square_classes(const cpp_int& N, BankResult& result) {
  for (const Row& row:result.rows) {
    cpp_int exact;
    if (!squarez(row.value,&exact)) continue;
    cpp_int gm,gp,normalized;
    std::string cls=classify_root(exact,row.root,N,gm,gp,normalized);
    require(exact*exact==row.value,"singleton square verification");
    if (row.identity) ++result.base_singletons;
    else ++result.orbit_singletons;
    bool prior=result.any_factor;
    bool first=result.first_factor==1;
    record_factor(result,exact-row.root,N,
                  row.identity?"BASE_SINGLETON_MINUS":"ORBIT_SINGLETON_MINUS",
                  false,DIRECT_SINGLETON);
    record_factor(result,exact+row.root,N,
                  row.identity?"BASE_SINGLETON_PLUS":"ORBIT_SINGLETON_PLUS",
                  false,DIRECT_SINGLETON);
    if (cls=="USEFUL") {
      if (row.identity) ++result.useful_base_singletons;
      else ++result.useful_orbit_singletons;
      std::string label=row.identity?"BASE_SINGLETON":"ORBIT_SINGLETON";
      EvidenceCertificate certificate;
      certificate.present=true;certificate.kind="NORMALIZED_ROOT";certificate.label=label;
      certificate.root_class=cls;certificate.exact_root=exact;
      certificate.supplied_root=row.root;certificate.normalized_root=normalized;
      certificate.gcd_minus=gm;certificate.gcd_plus=gp;
      certificate.candidate=(gm>1&&gm<N) ? exact-row.root : exact+row.root;
      certificate.factor=(gm>1&&gm<N) ? gm : gp;certificate.witnesses={row};
      if (first) result.first_certificate=certificate;
      if (!prior) {
        if (row.identity) result.strict_base_singleton=true;
        else result.strict_orbit_singleton=true;
      }
    }
  }
  for (std::size_t i=0;i<result.rows.size();++i) {
    for (std::size_t j=i+1;j<result.rows.size();++j) {
      cpp_int exact;
      if (!same_square_class(result.rows[i].value,result.rows[j].value,&exact)) continue;
      if (result.rows[i].value==result.rows[j].value) ++result.equal_rows;
      else ++result.square_multiples;
      cpp_int supplied=modz(result.rows[i].root*result.rows[j].root,N);
      cpp_int gm,gp,normalized;
      std::string cls=classify_root(exact,supplied,N,gm,gp,normalized);
      bool prior=result.any_factor;
      bool first=result.first_factor==1;
      bool equal=result.rows[i].value==result.rows[j].value;
      std::string label=equal?"EQUAL_ROW_DECOY":"SQUARE_MULTIPLE_TEMPLATE";
      record_factor(result,exact-supplied,N,label+"_MINUS",false,
                    DIRECT_EQUAL_OR_TEMPLATE);
      record_factor(result,exact+supplied,N,label+"_PLUS",false,
                    DIRECT_EQUAL_OR_TEMPLATE);
      if (cls=="USEFUL") {
        if (!equal) ++result.useful_square_multiples;
        EvidenceCertificate certificate;
        certificate.present=true;certificate.kind="NORMALIZED_ROOT";certificate.label=label;
        certificate.root_class=cls;certificate.exact_root=exact;
        certificate.supplied_root=supplied;certificate.normalized_root=normalized;
        certificate.gcd_minus=gm;certificate.gcd_plus=gp;
        certificate.candidate=(gm>1&&gm<N) ? exact-supplied : exact+supplied;
        certificate.factor=(gm>1&&gm<N) ? gm : gp;
        certificate.witnesses={result.rows[i],result.rows[j]};
        if (first) result.first_certificate=certificate;
        if (!prior) {
          if (equal) result.strict_equal_row=true;
          else result.strict_square_multiple=true;
        }
      }
    }
  }
}

void canonicalize_square_classes(BankResult& result) {
  std::vector<Row> kept;
  for (Row row:result.rows) {
    if (squarez(row.value)) continue;
    bool duplicate=false;
    for (const Row& old:kept)
      if (same_square_class(row.value,old.value)) {duplicate=true;break;}
    if (!duplicate) kept.push_back(std::move(row));
  }
  result.rows.swap(kept);
  result.residual_rows=result.rows.size();
}

Relation verify_relation(const std::vector<u64>& bits,const cpp_int& N,
                         const std::vector<Row>& rows) {
  Relation relation;
  cpp_int product=1,supplied=1;
  bool cross_base=false,cross_level=false;
  int first_base=-1,first_level=-1;
  for (int i=0;i<static_cast<int>(rows.size());++i) {
    if (!bit_get(bits,i)) continue;
    relation.columns.push_back(i);
    product*=rows[i].value;
    supplied=modz(supplied*rows[i].root,N);
    if (first_base<0) {first_base=rows[i].base_id;first_level=rows[i].level;}
    else {
      cross_base|=first_base!=rows[i].base_id;
      cross_level|=first_level!=rows[i].level;
    }
  }
  require(relation.columns.size()>=2,"residual singleton relation");
  cpp_int exact;
  require(squarez(product,&exact),"kernel product is not square");
  require(exact*exact==product,"relation product verification");
  relation.exact_root=exact;relation.supplied_root=supplied;
  relation.root_class=classify_root(exact,supplied,N,relation.gcd_minus,
                                    relation.gcd_plus,relation.normalized_root);
  if (cross_base) relation.label="CROSS_BASE_MULTIROW";
  else if (cross_level) relation.label="CROSS_LEVEL_MULTIROW";
  else relation.label="SAME_BASE_MULTIROW";
  return relation;
}

BankResult analyze_public(const cpp_int& N,const Family& family) {
  BankResult result; result.family=family.id;
  generate_rows(N,family,result);
  if (result.resource_reject||result.rows.empty()) return result;
  result.tested_rows=result.rows.size();
  std::set<cpp_int> distinct_values;
  for (const Row& row:result.rows) distinct_values.insert(row.value);
  result.baseline_rows=distinct_values.size();
  screen_base_channels(N,result);
  screen_transformed_channels(N,result);
  screen_projective_channels(N,result);
  screen_resultants(N,result);
  screen_carries(N,result);
  screen_singletons_and_square_classes(N,result);
  canonicalize_square_classes(result);
  Decoder decoder=decode_rows(result.rows);
  if (decoder.resource_reject) {
    result.resource_reject=true;result.error=decoder.error;return result;
  }
  require(decoder.ok,decoder.error);
  result.blocks=decoder.blocks.size();result.gcd_free_steps=decoder.steps;
  result.rank=decoder.rank;result.nullity=decoder.kernel.size();
  result.private_columns=decoder.private_columns;
  for (const Block& source:decoder.blocks) {
    OpaqueBlock block;
    block.value=source.value;block.square=squarez(source.value);
    block.status=block.square?"EXACT_SQUARE_BLOCK":"UNKNOWN_OPAQUE_NOT_NEEDED";
    for (std::size_t column=0;column<source.exponents.size();++column)
      if (source.exponents[column])
        block.exponents.push_back({static_cast<int>(column),source.exponents[column]});
    result.opaque_blocks.push_back(std::move(block));
  }
  result.eligible=true;
  for (const auto& bits:decoder.kernel) {
    bool prior=result.any_factor;
    Relation relation=verify_relation(bits,N,result.rows);
    ++result.relations;
    if (relation.root_class=="GLOBAL_PLUS") ++result.global_plus;
    else if (relation.root_class=="GLOBAL_MINUS") ++result.global_minus;
    else {
      ++result.useful_relations;
      bool first=result.first_factor==1;
      record_factor(result,relation.exact_root-relation.supplied_root,N,
                    "MULTIROW_P66_MINUS");
      record_factor(result,relation.exact_root+relation.supplied_root,N,
                    "MULTIROW_P66_PLUS");
      EvidenceCertificate certificate;
      certificate.present=true;certificate.kind="MULTIROW_P66";
      certificate.label=relation.label;certificate.root_class=relation.root_class;
      certificate.exact_root=relation.exact_root;
      certificate.supplied_root=relation.supplied_root;
      certificate.normalized_root=relation.normalized_root;
      certificate.gcd_minus=relation.gcd_minus;certificate.gcd_plus=relation.gcd_plus;
      certificate.candidate=(relation.gcd_minus>1&&relation.gcd_minus<N) ?
                            relation.exact_root-relation.supplied_root :
                            relation.exact_root+relation.supplied_root;
      certificate.factor=(relation.gcd_minus>1&&relation.gcd_minus<N) ?
                         relation.gcd_minus : relation.gcd_plus;
      for (int column:relation.columns) certificate.witnesses.push_back(result.rows[column]);
      if (first) result.first_certificate=certificate;
      if (!prior) {
        ++result.strict_multirow;
      }
    }
  }
  return result;
}

struct Evaluated {
  std::size_t case_index=0;
  int family=0;
  BankResult bank;
  std::string factor_label="NONE";
};

struct Stats {
  u64 intended=0,eligible=0,resource_reject=0,any_factor=0;
  u64 strict_carry_banks=0,strict_base_singleton_banks=0;
  u64 strict_orbit_singleton_banks=0,strict_square_banks=0;
  u64 strict_multirow_banks=0,strict_multirow_relations=0;
  u64 useful_relations=0,relations=0,nullity=0,private_deficit=0;
  u64 rows=0,safe_eligible=0;
};

void add_stats(Stats& stats,const Case& c,const BankResult& bank) {
  ++stats.intended;
  stats.any_factor+=bank.any_factor;
  if (bank.resource_reject) ++stats.resource_reject;
  if (!bank.eligible) return;
  ++stats.eligible;
  if (c.shape=="safe-safe") ++stats.safe_eligible;
  stats.strict_carry_banks+=bank.strict_carry;
  stats.strict_base_singleton_banks+=bank.strict_base_singleton;
  stats.strict_orbit_singleton_banks+=bank.strict_orbit_singleton;
  stats.strict_square_banks+=bank.strict_square_multiple;
  stats.strict_multirow_banks+=bank.strict_multirow>0;
  stats.strict_multirow_relations+=bank.strict_multirow;
  stats.useful_relations+=bank.useful_relations;
  stats.relations+=bank.relations;
  stats.nullity+=bank.nullity;
  stats.private_deficit+=bank.residual_rows>=bank.private_columns ?
                         bank.residual_rows-bank.private_columns : 0;
  stats.rows+=bank.tested_rows;
}

std::vector<Evaluated> evaluate(const std::vector<Case>& cases,
                                const std::vector<int>& family_ids,int workers) {
  require(workers>=1&&workers<=MAX_WORKERS,"worker range");
  struct Task {std::size_t case_index;int family;};
  std::vector<Task> tasks;
  for (std::size_t i=0;i<cases.size();++i)
    for (int family:family_ids) tasks.push_back({i,family});
  std::vector<Evaluated> output(tasks.size());
  std::atomic<std::size_t> next{0};
  std::mutex error_mutex;
  std::exception_ptr error;
  auto worker=[&] {
    try {
      for (;;) {
        std::size_t index=next.fetch_add(1);
        if (index>=tasks.size()) break;
        const Task task=tasks[index];
        const Case& c=cases[task.case_index];
        BankResult bank=analyze_public(c.N,FAMILIES[task.family]);
        std::string label="NONE";
        if (bank.first_factor>1) {
          require(c.N%bank.first_factor==0,"reported factor does not divide N");
          if (bank.first_factor==c.p) label="p";
          else if (bank.first_factor==c.q) label="q";
          else label="COMPOSITE_DIVISOR";
        }
        output[index]={task.case_index,task.family,std::move(bank),label};
      }
    } catch (...) {
      std::lock_guard<std::mutex> lock(error_mutex);
      if (!error) error=std::current_exception();
    }
  };
  std::vector<std::thread> threads;
  for (int i=0;i<workers;++i) threads.emplace_back(worker);
  for (auto& thread:threads) thread.join();
  if (error) std::rethrow_exception(error);
  return output;
}

std::string join_path(const std::string& directory,const std::string& name) {
  return directory.empty() ? name : directory+"/"+name;
}

bool path_exists(const std::string& path) {
  struct stat info{};
  return stat(path.c_str(),&info)==0;
}

u64& written_bytes() {static u64 value=0;return value;}

void write_text(const std::string& path,const std::string& bytes) {
  require(!path_exists(path),"refuse overwrite: "+path);
  require(bytes.size()<=OUTPUT_CAP-written_bytes(),"aggregate output cap");
  std::ofstream output(path,std::ios::binary|std::ios::out);
  require(bool(output),"open output: "+path);
  output.write(bytes.data(),static_cast<std::streamsize>(bytes.size()));
  output.close();
  require(bool(output),"close output: "+path);
  written_bytes()+=bytes.size();
}

void account_existing_file(const std::string& path) {
  struct stat info{};
  require(stat(path.c_str(),&info)==0&&S_ISREG(info.st_mode),"missing existing evidence: "+path);
  require(info.st_size>=0&&static_cast<u64>(info.st_size)<=OUTPUT_CAP-written_bytes(),
          "existing evidence exceeds aggregate output cap");
  written_bytes()+=static_cast<u64>(info.st_size);
}

u64 line_count(const std::string& bytes) {
  return std::count(bytes.begin(),bytes.end(),'\n');
}

std::string json_string(const std::string& value) {
  std::ostringstream out;out<<'"';
  for (unsigned char c:value) {
    if (c=='"'||c=='\\') out<<'\\'<<c;
    else if (c=='\n') out<<"\\n";
    else if (c<32) out<<"\\u"<<std::hex<<std::setw(4)<<std::setfill('0')<<int(c)<<std::dec;
    else out<<c;
  }
  out<<'"';return out.str();
}

std::string corpus_bytes(const std::vector<Case>& cases) {
  std::ostringstream out;
  out<<"version\tsplit\tshape\tfactor_bits\tindex\tN\n";
  for (const Case& c:cases)
    out<<"F266-D04\t"<<c.split<<'\t'<<c.shape<<'\t'<<c.factor_bits<<'\t'
       <<c.index<<'\t'<<c.N<<'\n';
  return out.str();
}

std::string bank_bytes(const std::vector<Case>& cases,const std::vector<Evaluated>& rows) {
  std::ostringstream out;
  out<<"split\tshape\tfactor_bits\tcase_index\tN\tfamily\teligible\tresource_reject"
       "\tany_factor\tfactor\tfactor_label\tfirst_channel\tfirst_candidate"
       "\tgenerated_rows\ttested_rows\tresidual_rows\tcoefficient_aliases\tmatrix_aliases"
       "\tpairs\tresultants\troot_determinants\tcarry_tests\tstrict_carry"
       "\tbase_singletons\torbit_singletons\tuseful_base_singletons"
       "\tuseful_orbit_singletons\tstrict_base_singleton\tstrict_orbit_singleton"
       "\tequal_rows\tsquare_multiples\tuseful_square_multiples\tstrict_square_multiple"
       "\tstrict_equal_row\tbaseline_distinct_rows"
       "\tblocks\tgcd_free_steps\trank\tnullity\tprivate_columns\trelations"
       "\tuseful_relations\tstrict_multirow\tglobal_plus\tglobal_minus"
       "\tuniform_principal_baseline_num\tuniform_principal_baseline_den";
  for (const char* stage:DIRECT_STAGE_NAMES)
    out<<"\tdirect_"<<stage<<"_tests\tdirect_"<<stage<<"_unit"
       <<"\tdirect_"<<stage<<"_full\tdirect_"<<stage<<"_proper";
  out<<"\terror\n";
  for (const Evaluated& evaluated:rows) {
    const Case& c=cases[evaluated.case_index];const BankResult& b=evaluated.bank;
    out<<c.split<<'\t'<<c.shape<<'\t'<<c.factor_bits<<'\t'<<c.index<<'\t'<<c.N<<'\t'
       <<evaluated.family<<'\t'<<b.eligible<<'\t'<<b.resource_reject<<'\t'<<b.any_factor<<'\t'
       <<b.first_factor<<'\t'<<evaluated.factor_label<<'\t'<<b.first_channel<<'\t'
       <<b.first_candidate<<'\t'<<b.generated_rows<<'\t'<<b.tested_rows<<'\t'
       <<b.residual_rows<<'\t'<<b.coefficient_aliases<<'\t'<<b.matrix_aliases<<'\t'
       <<b.pairs<<'\t'<<b.resultants<<'\t'<<b.root_determinants<<'\t'<<b.carry_tests<<'\t'
       <<b.strict_carry<<'\t'<<b.base_singletons<<'\t'<<b.orbit_singletons<<'\t'
       <<b.useful_base_singletons<<'\t'<<b.useful_orbit_singletons<<'\t'
       <<b.strict_base_singleton<<'\t'<<b.strict_orbit_singleton<<'\t'
       <<b.equal_rows<<'\t'<<b.square_multiples<<'\t'<<b.useful_square_multiples<<'\t'
       <<b.strict_square_multiple<<'\t'<<b.strict_equal_row<<'\t'<<b.baseline_rows<<'\t'
       <<b.blocks<<'\t'<<b.gcd_free_steps<<'\t'
       <<b.rank<<'\t'<<b.nullity<<'\t'<<b.private_columns<<'\t'<<b.relations<<'\t'
       <<b.useful_relations<<'\t'<<b.strict_multirow<<'\t'<<b.global_plus<<'\t'
       <<b.global_minus<<'\t'<<(b.eligible?2*b.baseline_rows:0)<<'\t'<<c.N;
    for (const DirectCounter& counter:b.direct) {
      require(counter.tests==counter.unit+counter.full+counter.proper,
              "direct counter partition");
      out<<'\t'<<counter.tests<<'\t'<<counter.unit<<'\t'<<counter.full<<'\t'
         <<counter.proper;
    }
    out<<'\t'<<b.error<<'\n';
  }
  return out.str();
}

using CellKey=std::tuple<int,int,std::string>;

std::map<CellKey,Stats> collect_cells(const std::vector<Case>& cases,
                                      const std::vector<Evaluated>& rows,
                                      std::array<Stats,8>& totals) {
  std::map<CellKey,Stats> cells;
  for (const Evaluated& evaluated:rows) {
    const Case& c=cases[evaluated.case_index];
    add_stats(totals[evaluated.family],c,evaluated.bank);
    add_stats(cells[{evaluated.family,c.factor_bits,c.shape}],c,evaluated.bank);
  }
  return cells;
}

std::string family_bytes(const std::map<CellKey,Stats>& cells,
                         const std::array<Stats,8>& totals,
                         const std::vector<int>& family_ids) {
  std::ostringstream out;
  out<<"family\tfactor_bits\tshape\tintended\teligible\tresource_reject\tany_factor"
       "\tstrict_carry_banks\tstrict_base_singleton_banks\tstrict_orbit_singleton_banks"
       "\tstrict_square_banks\tstrict_multirow_banks\tstrict_multirow_relations"
       "\tuseful_relations\trelations\tnullity\tprivate_deficit\trows\tsafe_eligible\n";
  auto emit=[&](int family,const std::string& bits,const std::string& shape,const Stats& s) {
    out<<family<<'\t'<<bits<<'\t'<<shape<<'\t'<<s.intended<<'\t'<<s.eligible<<'\t'
       <<s.resource_reject<<'\t'<<s.any_factor<<'\t'<<s.strict_carry_banks<<'\t'
       <<s.strict_base_singleton_banks<<'\t'<<s.strict_orbit_singleton_banks<<'\t'
       <<s.strict_square_banks<<'\t'<<s.strict_multirow_banks<<'\t'
       <<s.strict_multirow_relations<<'\t'<<s.useful_relations<<'\t'<<s.relations<<'\t'
       <<s.nullity<<'\t'<<s.private_deficit<<'\t'<<s.rows<<'\t'<<s.safe_eligible<<'\n';
  };
  for (int family:family_ids) {
    for (const auto& item:cells)
      if (std::get<0>(item.first)==family)
        emit(family,std::to_string(std::get<1>(item.first)),std::get<2>(item.first),item.second);
    emit(family,"ALL","ALL",totals[family]);
  }
  return out.str();
}

void emit_row_json(std::ostringstream& out,const Row& row) {
  out<<"{\"base\":"<<row.base_id<<",\"level\":"<<row.level
     <<",\"identity\":"<<(row.identity?"true":"false")
     <<",\"syntax\":"<<json_string(row.syntax)
     <<",\"matrix\":["<<row.matrix.a<<','<<row.matrix.b<<','<<row.matrix.c<<','<<row.matrix.d<<']'
     <<",\"modulus\":"<<json_string(row.modulus.convert_to<std::string>())
     <<",\"A0\":"<<json_string(row.A0.convert_to<std::string>())
     <<",\"B0\":"<<json_string(row.B0.convert_to<std::string>())
     <<",\"C0\":"<<json_string(row.C0.convert_to<std::string>())
     <<",\"delta0\":"<<json_string(row.delta0.convert_to<std::string>())
     <<",\"A\":"<<json_string(row.A.convert_to<std::string>())
     <<",\"B\":"<<json_string(row.B.convert_to<std::string>())
     <<",\"C\":"<<json_string(row.C.convert_to<std::string>())
     <<",\"discriminant\":"<<json_string(row.discriminant.convert_to<std::string>())
     <<",\"value\":"<<json_string(row.value.convert_to<std::string>())
     <<",\"root\":"<<json_string(row.root.convert_to<std::string>())
     <<",\"carry\":"<<json_string(row.carry.convert_to<std::string>())
     <<",\"pr\":["<<json_string(row.pr.numerator.convert_to<std::string>())<<','
                    <<json_string(row.pr.denominator.convert_to<std::string>())<<']'
     <<",\"ps\":["<<json_string(row.ps.numerator.convert_to<std::string>())<<','
                    <<json_string(row.ps.denominator.convert_to<std::string>())<<"]}";
}

void emit_certificate_json(std::ostringstream& out,const Case& c,int family,
                           const EvidenceCertificate& certificate) {
  require(certificate.present,"serialize absent certificate");
  require(certificate.factor>1&&certificate.factor<c.N&&
          c.N%certificate.factor==0,"certificate factor replay");
  if (certificate.kind=="DIRECT_TICKET"||certificate.kind=="CARRY_TICKET") {
    require(certificate.divisor!=0&&certificate.numerator%certificate.divisor==0,
            "ticket exact division replay");
    require(certificate.numerator/certificate.divisor==certificate.candidate,
            "ticket quotient replay");
    require(gcdz(certificate.candidate,c.N)==certificate.factor,
            "ticket gcd replay");
  } else {
    cpp_int product=1,supplied=1;
    require(!certificate.witnesses.empty(),"root certificate without rows");
    for (const Row& row:certificate.witnesses) {
      require(row.value>0&&modz(row.root*row.root-row.value,c.N)==0,
              "root certificate row replay");
      product*=row.value;supplied=modz(supplied*row.root,c.N);
    }
    require(certificate.exact_root*certificate.exact_root==product,
            "root certificate square replay");
    require(certificate.supplied_root==supplied,"root certificate supplied replay");
    require(certificate.normalized_root==
            modz(certificate.exact_root*invmod(supplied,c.N),c.N),
            "root certificate normalization replay");
    require(certificate.gcd_minus==gcdz(certificate.exact_root-supplied,c.N)&&
            certificate.gcd_plus==gcdz(certificate.exact_root+supplied,c.N),
            "root certificate signed gcd replay");
    require(certificate.factor==certificate.gcd_minus||
            certificate.factor==certificate.gcd_plus,"root certificate factor replay");
  }
  std::string factor_label="COMPOSITE_DIVISOR";
  if (certificate.factor==c.p) factor_label="p";
  else if (certificate.factor==c.q) factor_label="q";
  out<<"{\"version\":\"F266-D04\",\"split\":"<<json_string(c.split)
     <<",\"shape\":"<<json_string(c.shape)<<",\"factor_bits\":"<<c.factor_bits
     <<",\"index\":"<<c.index<<",\"N\":"<<json_string(c.N.convert_to<std::string>())
     <<",\"family\":"<<family<<",\"kind\":"<<json_string(certificate.kind)
     <<",\"label\":"<<json_string(certificate.label)
     <<",\"root_class\":"<<json_string(certificate.root_class)
     <<",\"numerator\":"<<json_string(certificate.numerator.convert_to<std::string>())
     <<",\"divisor\":"<<json_string(certificate.divisor.convert_to<std::string>())
     <<",\"candidate\":"<<json_string(certificate.candidate.convert_to<std::string>())
     <<",\"factor\":"<<json_string(certificate.factor.convert_to<std::string>())
     <<",\"factor_label\":"<<json_string(factor_label)
     <<",\"exact_root\":"<<json_string(certificate.exact_root.convert_to<std::string>())
     <<",\"supplied_root\":"<<json_string(certificate.supplied_root.convert_to<std::string>())
     <<",\"normalized_root\":"<<json_string(certificate.normalized_root.convert_to<std::string>())
     <<",\"gcd_minus\":"<<json_string(certificate.gcd_minus.convert_to<std::string>())
     <<",\"gcd_plus\":"<<json_string(certificate.gcd_plus.convert_to<std::string>())
     <<",\"rows\":[";
  for (std::size_t i=0;i<certificate.witnesses.size();++i) {
    if (i) out<<',';
    emit_row_json(out,certificate.witnesses[i]);
  }
  out<<"]}\n";
}

std::string certificate_bytes(const std::vector<Case>& cases,
                              std::vector<Evaluated>& rows) {
  std::array<int,8> saved{};
  std::ostringstream out;
  for (Evaluated& evaluated:rows) {
    if (saved[evaluated.family]>=MAX_CERTIFICATES) continue;
    const Case& c=cases[evaluated.case_index];BankResult& b=evaluated.bank;
    if (b.first_certificate.present) {
      emit_certificate_json(out,c,evaluated.family,b.first_certificate);
      bool strict=b.strict_carry||b.strict_base_singleton||b.strict_orbit_singleton||
                  b.strict_square_multiple||b.strict_equal_row||b.strict_multirow>0;
      if (strict) b.strict_certificate_emitted=true;
      ++saved[evaluated.family];
    }
  }
  return out.str();
}

std::string opaque_bytes(const std::vector<Case>& cases,
                         const std::vector<Evaluated>& rows) {
  std::ostringstream out;
  for (const Evaluated& evaluated:rows) {
    const Case& c=cases[evaluated.case_index];const BankResult& b=evaluated.bank;
    if (b.eligible) {
      out<<"{\"version\":\"F266-D04\",\"kind\":\"ROW_MAP\",\"split\":"
         <<json_string(c.split)<<",\"shape\":"<<json_string(c.shape)
         <<",\"factor_bits\":"<<c.factor_bits<<",\"index\":"<<c.index
         <<",\"N\":"<<json_string(c.N.convert_to<std::string>())
         <<",\"family\":"<<evaluated.family<<",\"rows\":[";
      for (std::size_t column=0;column<b.rows.size();++column) {
        if (column) out<<',';
        const Row& row=b.rows[column];
        out<<"{\"column\":"<<column<<",\"base\":"<<row.base_id
           <<",\"level\":"<<row.level<<",\"syntax\":"<<json_string(row.syntax)
           <<",\"value\":"<<json_string(row.value.convert_to<std::string>())
           <<",\"root\":"<<json_string(row.root.convert_to<std::string>())<<'}';
      }
      out<<"]}\n";
    }
    for (std::size_t block_index=0;block_index<b.opaque_blocks.size();++block_index) {
      const OpaqueBlock& block=b.opaque_blocks[block_index];
      out<<"{\"version\":\"F266-D04\",\"kind\":\"OPAQUE_BLOCK\",\"split\":"
         <<json_string(c.split)
         <<",\"shape\":"<<json_string(c.shape)<<",\"factor_bits\":"<<c.factor_bits
         <<",\"index\":"<<c.index<<",\"N\":"<<json_string(c.N.convert_to<std::string>())
         <<",\"family\":"<<evaluated.family<<",\"block\":"<<block_index
         <<",\"value\":"<<json_string(block.value.convert_to<std::string>())
         <<",\"square\":"<<(block.square?"true":"false")
         <<",\"status\":"<<json_string(block.status)<<",\"exponents\":[";
      bool first=true;
      for (const auto& exponent:block.exponents) {
        if (!first) out<<',';
        first=false;out<<'['<<exponent.first<<','<<exponent.second<<']';
      }
      out<<"]}\n";
    }
  }
  return out.str();
}

int compare_rate(u64 an,u64 ad,u64 bn,u64 bd) {
  u128 left=static_cast<u128>(an)*bd,right=static_cast<u128>(bn)*ad;
  return left<right ? -1 : left>right ? 1 : 0;
}

std::vector<int> rank_families(const std::array<Stats,8>& totals,
                               const std::vector<int>& family_ids) {
  std::vector<int> ranked=family_ids;
  std::sort(ranked.begin(),ranked.end(),[&](int a,int b) {
    const Stats& x=totals[a];const Stats& y=totals[b];
    u64 xd=std::max<u64>(1,x.eligible),yd=std::max<u64>(1,y.eligible);
    for (auto pair:std::array<std::pair<u64,u64>,4>{{
           {x.strict_multirow_banks,y.strict_multirow_banks},
           {x.strict_carry_banks,y.strict_carry_banks},
           {x.strict_orbit_singleton_banks,y.strict_orbit_singleton_banks},
           {x.strict_square_banks,y.strict_square_banks}}}) {
      int cmp=compare_rate(pair.first,xd,pair.second,yd);
      if (cmp) return cmp>0;
    }
    if (x.nullity!=y.nullity) return x.nullity>y.nullity;
    if (x.private_deficit!=y.private_deficit) return x.private_deficit>y.private_deficit;
    if (x.safe_eligible!=y.safe_eligible) return x.safe_eligible>y.safe_eligible;
    if (x.rows!=y.rows) return x.rows<y.rows;
    return a<b;
  });
  return ranked;
}

std::string selection_bytes(const std::string& corpus_digest,
                            const std::array<Stats,8>& totals,
                            const std::vector<int>& ranked) {
  require(ranked.size()==8,"discovery rank count");
  std::ostringstream out;
  out<<"F266-D04-selection-v1\n";
  out<<"corpus_sha256\t"<<corpus_digest<<"\n";
  out<<"family\trank\tid\teligible\tstrict_multirow_banks\tstrict_carry_banks"
       "\tstrict_orbit_singleton_banks\tstrict_square_banks\tnullity"
       "\tprivate_deficit\tsafe_eligible\trows\n";
  for (std::size_t rank=0;rank<ranked.size();++rank) {
    int id=ranked[rank];const Stats& s=totals[id];
    out<<"family\t"<<rank<<'\t'<<id<<'\t'<<s.eligible<<'\t'
       <<s.strict_multirow_banks<<'\t'<<s.strict_carry_banks<<'\t'
       <<s.strict_orbit_singleton_banks<<'\t'<<s.strict_square_banks<<'\t'
       <<s.nullity<<'\t'<<s.private_deficit<<'\t'<<s.safe_eligible<<'\t'<<s.rows<<'\n';
  }
  out<<"selected";
  for (int i=0;i<4;++i) out<<'\t'<<ranked[i];
  out<<'\n';
  return out.str();
}

struct Selection {
  std::string corpus_digest;
  std::vector<int> selected;
};

Selection parse_selection(const std::string& bytes,const std::string& expected_digest) {
  require(sha256_bytes(bytes)==expected_digest,"selection SHA-256 mismatch");
  std::istringstream input(bytes);std::string line;
  require(bool(std::getline(input,line))&&line=="F266-D04-selection-v1","selection header");
  require(bool(std::getline(input,line)),"selection corpus row");
  std::istringstream corpus(line);std::string tag,digest;
  require(bool(std::getline(corpus,tag,'\t'))&&tag=="corpus_sha256","selection corpus tag");
  require(bool(std::getline(corpus,digest,'\t'))&&digest.size()==64&&
          digest.find_first_not_of("0123456789abcdef")==std::string::npos,
          "selection corpus digest");
  require(bool(std::getline(input,line))&&
          line=="family\trank\tid\teligible\tstrict_multirow_banks\tstrict_carry_banks"
                "\tstrict_orbit_singleton_banks\tstrict_square_banks\tnullity"
                "\tprivate_deficit\tsafe_eligible\trows",
          "selection family header");
  std::set<int> ranked;
  std::vector<int> rank_order;
  std::array<Stats,8> parsed_totals{};
  for (int i=0;i<8;++i) {
    require(bool(std::getline(input,line)),"selection family row");
    std::istringstream row(line);std::vector<std::string> fields;std::string field;
    while (std::getline(row,field,'\t')) fields.push_back(field);
    require(fields.size()==12&&fields[0]=="family","selection family fields");
    require(std::stoi(fields[1])==i,"selection rank order");
    int id=std::stoi(fields[2]);require(id>=0&&id<8,"selection family id");
    require(ranked.insert(id).second,"duplicate ranked family");
    rank_order.push_back(id);
    for (int field_index=3;field_index<12;++field_index)
      require(!fields[field_index].empty()&&
              fields[field_index].find_first_not_of("0123456789")==std::string::npos,
              "selection metric syntax");
    Stats& stats=parsed_totals[id];
    stats.eligible=std::stoull(fields[3]);
    stats.strict_multirow_banks=std::stoull(fields[4]);
    stats.strict_carry_banks=std::stoull(fields[5]);
    stats.strict_orbit_singleton_banks=std::stoull(fields[6]);
    stats.strict_square_banks=std::stoull(fields[7]);
    stats.nullity=std::stoull(fields[8]);
    stats.private_deficit=std::stoull(fields[9]);
    stats.safe_eligible=std::stoull(fields[10]);
    stats.rows=std::stoull(fields[11]);
  }
  std::vector<int> all_ids{0,1,2,3,4,5,6,7};
  require(rank_families(parsed_totals,all_ids)==rank_order,
          "selection rank tuple does not reproduce rank order");
  require(bool(std::getline(input,line)),"selection selected row");
  std::istringstream selected_row(line);std::vector<std::string> fields;std::string field;
  while (std::getline(selected_row,field,'\t')) fields.push_back(field);
  require(fields.size()==5&&fields[0]=="selected","selection selected fields");
  Selection out;out.corpus_digest=digest;
  std::set<int> unique;
  for (int i=1;i<5;++i) {
    int id=std::stoi(fields[i]);require(ranked.count(id),"selected unknown family");
    require(unique.insert(id).second,"duplicate selected family");out.selected.push_back(id);
    require(id==rank_order[i-1],"selection is not the first four ranked families");
  }
  require(!std::getline(input,line),"selection trailing bytes");
  return out;
}

std::string manifest_bytes(const std::string& directory,
                           const std::vector<std::string>& names) {
  std::ostringstream out;out<<"filename\tbytes\tlines\tsha256\n";
  for (const std::string& name:names) {
    std::string bytes=read_file(join_path(directory,name));
    out<<name<<'\t'<<bytes.size()<<'\t'<<line_count(bytes)<<'\t'<<sha256_bytes(bytes)<<'\n';
  }
  return out.str();
}

std::pair<cpp_int,cpp_int> add_fraction(cpp_int numerator,cpp_int denominator,
                                        cpp_int add_numerator,cpp_int add_denominator) {
  cpp_int next_n=numerator*add_denominator+add_numerator*denominator;
  cpp_int next_d=denominator*add_denominator;
  cpp_int g=gcdz(next_n,next_d);
  return {next_n/g,next_d/g};
}

int find_coverage_family(
    const std::vector<int>& selected,
    const std::map<std::tuple<int,int,std::string>,u64>& eligible_cell,
    u64 minimum) {
  for (int family:selected) {
    bool covers_all=true;
    for (int bits:HELDOUT_BITS) for (const char* shape:SHAPES) {
      auto it=eligible_cell.find({family,bits,shape});
      u64 count=it==eligible_cell.end()?0:it->second;
      covers_all&=count>=minimum;
    }
    if (covers_all) return family;
  }
  return -1;
}

std::string lead_gate_bytes(const std::vector<Case>& cases,
                            const std::vector<Evaluated>& rows,
                            const std::vector<int>& selected) {
  u64 strict_multirow=0,strict_carry=0,strict_orbit=0,strict_square=0;
  u64 certified_multirow=0,certified_carry=0,eligible=0,intended=0,gain_banks=0;
  std::set<int> multi_sizes,carry_sizes;std::set<std::string> multi_shapes,carry_shapes;
  std::map<std::tuple<int,int,std::string>,u64> intended_cell,eligible_cell;
  struct Baseline {
    u64 intended=0,eligible=0,ineligible=0,base=0,orbit=0;
    cpp_int num=0,den=1;
  };
  std::map<std::pair<int,std::string>,Baseline> baselines;
  for (const Evaluated& evaluated:rows) {
    const Case& c=cases[evaluated.case_index];const BankResult& b=evaluated.bank;
    ++intended;eligible+=b.eligible;gain_banks+=b.any_factor;
    ++intended_cell[{evaluated.family,c.factor_bits,c.shape}];
    if (b.eligible) ++eligible_cell[{evaluated.family,c.factor_bits,c.shape}];
    if (b.strict_multirow) {
      ++strict_multirow;
      if (b.strict_certificate_emitted) {
        ++certified_multirow;multi_sizes.insert(c.factor_bits);multi_shapes.insert(c.shape);
      }
    }
    if (b.strict_carry&&c.factor_bits>=48) {
      ++strict_carry;
      if (b.strict_certificate_emitted) {
        ++certified_carry;carry_sizes.insert(c.factor_bits);carry_shapes.insert(c.shape);
      }
    }
    strict_orbit+=b.strict_orbit_singleton;strict_square+=b.strict_square_multiple;
    Baseline& base=baselines[{c.factor_bits,c.shape}];
    ++base.intended;base.base+=b.base_singletons;base.orbit+=b.orbit_singletons;
    if (b.eligible) {
      ++base.eligible;
      auto sum=add_fraction(base.num,base.den,cpp_int(2*b.baseline_rows),c.N);
      base.num=sum.first;base.den=sum.second;
    } else ++base.ineligible;
  }
  bool hostile_multi=multi_shapes.count("safe-safe")||multi_shapes.count("neighbor");
  bool strong=certified_multirow>=2&&multi_sizes.size()>=2&&hostile_multi;
  bool carry=certified_carry>=2&&carry_sizes.size()>=2&&carry_shapes.size()>=2;
  int coverage_family=find_coverage_family(selected,eligible_cell,24);
  bool cell_coverage=coverage_family>=0;
  bool no_gain=gain_banks==0;
  bool null_signal=no_gain&&10*eligible>=9*intended&&cell_coverage;
  std::ostringstream out;
  out<<"metric\tvalue\nstrong_orbit_lead\t"<<strong<<"\ncarry_lead\t"<<carry
     <<"\nfinite_null_signal\t"<<null_signal<<"\nstrict_multirow_banks\t"<<strict_multirow
     <<"\ncertified_strict_multirow_banks\t"<<certified_multirow
     <<"\ncertified_strict_carry_banks_48plus\t"<<certified_carry
     <<"\nstrict_carry_banks_48plus\t"<<strict_carry
     <<"\nstrict_orbit_singleton_banks\t"<<strict_orbit
     <<"\nstrict_square_multiple_banks\t"<<strict_square
     <<"\ngain_banks\t"<<gain_banks<<"\neligible\t"<<eligible
     <<"\nintended\t"<<intended<<"\ncell_coverage\t"<<cell_coverage
     <<"\ncoverage_family\t"<<coverage_family<<"\n";
  out<<"coverage\tfamily\tfactor_bits\tshape\tintended_banks\teligible_banks"
       "\tineligible_banks\tpasses_24\n";
  for (int family:selected) for (int bits:HELDOUT_BITS) for (const char* shape:SHAPES) {
    u64 cell_intended=intended_cell[{family,bits,shape}];
    u64 cell_eligible=eligible_cell[{family,bits,shape}];
    require(cell_eligible<=cell_intended,"cell eligibility partition");
    out<<"coverage\t"<<family<<'\t'<<bits<<'\t'<<shape<<'\t'<<cell_intended<<'\t'
       <<cell_eligible<<'\t'<<(cell_intended-cell_eligible)<<'\t'
       <<(cell_eligible>=24)<<'\n';
  }
  out<<"cell\tfactor_bits\tshape\tintended_banks\teligible_banks\tineligible_banks"
       "\tobserved_base_singletons"
       "\tobserved_orbit_singletons"
       "\tuniform_principal_baseline_num\tuniform_principal_baseline_den\n";
  for (int bits:HELDOUT_BITS) for (const char* shape:SHAPES) {
    const Baseline& b=baselines[{bits,shape}];
    require(b.intended==b.eligible+b.ineligible,"baseline eligibility partition");
    out<<"cell\t"<<bits<<'\t'<<shape<<'\t'<<b.intended<<'\t'<<b.eligible<<'\t'
       <<b.ineligible<<'\t'<<b.base<<'\t'<<b.orbit<<'\t'<<b.num<<'\t'<<b.den<<'\n';
  }
  return out.str();
}

std::set<std::string> parse_discovery_corpus(const std::string& bytes) {
  std::istringstream input(bytes);std::string line;
  require(bool(std::getline(input,line))&&
          line=="version\tsplit\tshape\tfactor_bits\tindex\tN","discovery corpus header");
  std::set<std::string> moduli;
  int rows=0;
  while (std::getline(input,line)) {
    if (line.empty()) continue;
    std::istringstream row(line);std::vector<std::string> fields;std::string field;
    while (std::getline(row,field,'\t')) fields.push_back(field);
    require(fields.size()==6&&fields[0]=="F266-D04"&&fields[1]=="discovery",
            "discovery corpus row");
    require(moduli.insert(fields[5]).second,"duplicate discovery modulus");
    ++rows;
  }
  require(rows==240,"discovery corpus row count");
  return moduli;
}

double timeval_seconds(const timeval& value) {
  return static_cast<double>(value.tv_sec)+static_cast<double>(value.tv_usec)/1e6;
}

void print_resources(const std::string& tag,
                     std::chrono::steady_clock::time_point start) {
  rusage usage{};require(getrusage(RUSAGE_SELF,&usage)==0,"getrusage");
  double wall=std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count();
  std::cout<<std::fixed<<std::setprecision(6)<<tag<<"_wall_seconds="<<wall
           <<' '<<tag<<"_user_seconds="<<timeval_seconds(usage.ru_utime)
           <<' '<<tag<<"_system_seconds="<<timeval_seconds(usage.ru_stime)
           <<' '<<tag<<"_maxrss_kib="<<usage.ru_maxrss<<'\n';
}

void run_discovery(const std::string& directory,int workers) {
  auto start=std::chrono::steady_clock::now();
  std::vector<Case> cases=make_cases("discovery");
  std::vector<int> family_ids{0,1,2,3,4,5,6,7};
  std::string corpus=corpus_bytes(cases),corpus_digest=sha256_bytes(corpus);
  std::vector<Evaluated> rows=evaluate(cases,family_ids,workers);
  std::array<Stats,8> totals{};
  auto cells=collect_cells(cases,rows,totals);
  std::string banks=bank_bytes(cases,rows);
  std::string families=family_bytes(cells,totals,family_ids);
  std::string certificates=certificate_bytes(cases,rows);
  std::string opaque=opaque_bytes(cases,rows);
  std::vector<int> ranked=rank_families(totals,family_ids);
  std::string selection=selection_bytes(corpus_digest,totals,ranked);
  std::string selection_digest=sha256_bytes(selection);
  const std::string corpus_name="F266-D04.discovery.corpus.tsv";
  const std::string corpus_sha_name="F266-D04.discovery.corpus.sha256";
  const std::string bank_name="F266-D04.discovery.banks.tsv";
  const std::string family_name="F266-D04.discovery.families.tsv";
  const std::string certificate_name="F266-D04.discovery.certificates.jsonl";
  const std::string opaque_name="F266-D04.discovery.opaque.jsonl";
  const std::string selection_name="F266-D04.selection.tsv";
  const std::string selection_sha_name="F266-D04.selection.sha256";
  write_text(join_path(directory,corpus_name),corpus);
  write_text(join_path(directory,corpus_sha_name),corpus_digest+"  "+corpus_name+"\n");
  write_text(join_path(directory,bank_name),banks);
  write_text(join_path(directory,family_name),families);
  write_text(join_path(directory,certificate_name),certificates);
  write_text(join_path(directory,opaque_name),opaque);
  write_text(join_path(directory,selection_name),selection);
  write_text(join_path(directory,selection_sha_name),selection_digest+"  "+selection_name+"\n");
  std::vector<std::string> names{corpus_name,corpus_sha_name,bank_name,family_name,
                                 certificate_name,opaque_name,selection_name,selection_sha_name};
  write_text(join_path(directory,"F266-D04.discovery.manifest.tsv"),manifest_bytes(directory,names));
  std::cout<<"DISCOVERY_PASS cases="<<cases.size()<<" banks="<<rows.size()
           <<" corpus_sha256="<<corpus_digest<<" selection_sha256="<<selection_digest<<'\n';
  print_resources("discovery",start);
}

void run_heldout(const std::string& directory,const std::string& selection_path,
                 const std::string& expected_selection_digest,
                 const std::string& discovery_corpus_path,
                 const std::string& expected_corpus_digest,int workers) {
  auto start=std::chrono::steady_clock::now();
  for (const char* name:{"F266-D04.discovery.corpus.tsv","F266-D04.discovery.corpus.sha256",
                         "F266-D04.discovery.banks.tsv","F266-D04.discovery.families.tsv",
                         "F266-D04.discovery.certificates.jsonl","F266-D04.discovery.opaque.jsonl",
                         "F266-D04.selection.tsv",
                         "F266-D04.selection.sha256","F266-D04.discovery.manifest.tsv"})
    account_existing_file(join_path(directory,name));
  std::string selection_bytes_once=read_file(selection_path);
  Selection selection=parse_selection(selection_bytes_once,expected_selection_digest);
  std::string corpus_once=read_file(discovery_corpus_path);
  std::string observed_corpus_digest=sha256_bytes(corpus_once);
  require(observed_corpus_digest==expected_corpus_digest,"discovery corpus expected SHA mismatch");
  require(observed_corpus_digest==selection.corpus_digest,"selection/corpus SHA mismatch");
  std::set<std::string> forbidden=parse_discovery_corpus(corpus_once);
  std::vector<Case> cases=make_cases("heldout",false,forbidden);
  std::vector<Evaluated> rows=evaluate(cases,selection.selected,workers);
  std::array<Stats,8> totals{};
  auto cells=collect_cells(cases,rows,totals);
  std::string corpus=corpus_bytes(cases);
  std::string banks=bank_bytes(cases,rows);
  std::string families=family_bytes(cells,totals,selection.selected);
  std::string certificates=certificate_bytes(cases,rows);
  std::string opaque=opaque_bytes(cases,rows);
  std::string lead=lead_gate_bytes(cases,rows,selection.selected);
  const std::string corpus_name="F266-D04.heldout.corpus.tsv";
  const std::string bank_name="F266-D04.heldout.banks.tsv";
  const std::string family_name="F266-D04.heldout.families.tsv";
  const std::string certificate_name="F266-D04.heldout.certificates.jsonl";
  const std::string opaque_name="F266-D04.heldout.opaque.jsonl";
  const std::string lead_name="F266-D04.heldout.lead_gate.tsv";
  write_text(join_path(directory,corpus_name),corpus);
  write_text(join_path(directory,bank_name),banks);
  write_text(join_path(directory,family_name),families);
  write_text(join_path(directory,certificate_name),certificates);
  write_text(join_path(directory,opaque_name),opaque);
  write_text(join_path(directory,lead_name),lead);
  std::vector<std::string> names{corpus_name,bank_name,family_name,certificate_name,
                                 opaque_name,lead_name};
  write_text(join_path(directory,"F266-D04.heldout.manifest.tsv"),manifest_bytes(directory,names));
  require(sha256_bytes(selection_bytes_once)==expected_selection_digest,
          "selection changed during heldout");
  std::cout<<"HELDOUT_PASS cases="<<cases.size()<<" banks="<<rows.size()
           <<" selection_sha256="<<expected_selection_digest<<'\n';
  print_resources("heldout",start);
}

void run_preflight(const std::string& output_path,int workers) {
  auto start=std::chrono::steady_clock::now();
  std::vector<Case> discovery=make_cases("discovery",true);
  std::set<std::string> forbidden;
  for (const Case& c:discovery) forbidden.insert(c.N.convert_to<std::string>());
  std::vector<Case> heldout=make_cases("heldout",true,forbidden);
  std::vector<Case> cases=discovery;
  cases.insert(cases.end(),heldout.begin(),heldout.end());
  std::vector<int> families{0,1,2,3,4,5,6,7};
  std::vector<Evaluated> rows=evaluate(cases,families,workers);
  double wall=std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count();
  rusage usage{};require(getrusage(RUSAGE_SELF,&usage)==0,"preflight getrusage");
  u64 pairs=0,resultants=0,steps=0,row_count=0,resource_reject=0,eligible=0;
  for (const auto& evaluated:rows) {
    pairs+=evaluated.bank.pairs;resultants+=evaluated.bank.resultants;
    steps+=evaluated.bank.gcd_free_steps;row_count+=evaluated.bank.tested_rows;
    resource_reject+=evaluated.bank.resource_reject;
    eligible+=evaluated.bank.eligible;
  }
  constexpr double full_tasks=240.0*8.0+384.0*4.0;
  double projected_wall=wall*full_tasks/std::max<double>(1,rows.size())/
                        8.0*2.0;
  std::array<Stats,8> totals{};
  auto cells=collect_cells(cases,rows,totals);
  std::string sample_corpus=corpus_bytes(cases);
  std::string sample_banks=bank_bytes(cases,rows);
  std::string sample_families=family_bytes(cells,totals,families);
  std::string sample_certificates=certificate_bytes(cases,rows);
  std::string sample_opaque=opaque_bytes(cases,rows);
  u64 sample_output=sample_corpus.size()+sample_banks.size()+sample_families.size()+
                    sample_certificates.size()+sample_opaque.size();
  u64 projected_output=static_cast<u64>(sample_output*full_tasks/
                                        std::max<double>(1,rows.size())*2.0+64*1024*1024);
  u64 projected_rss=static_cast<u64>(usage.ru_maxrss)*8;
  bool pass=projected_wall<=12600.0&&projected_rss<=3670016&&
            projected_output<=943718400&&resource_reject==0;
  std::ostringstream json;
  json<<"{\"version\":\"F266-D04\",\"pass\":"<<(pass?"true":"false")
      <<",\"workers\":"<<workers<<",\"sample_cases\":"<<cases.size()
      <<",\"sample_banks\":"<<rows.size()<<",\"wall_seconds\":"<<std::fixed
      <<std::setprecision(6)<<wall<<",\"user_seconds\":"<<timeval_seconds(usage.ru_utime)
      <<",\"system_seconds\":"<<timeval_seconds(usage.ru_stime)
      <<",\"maxrss_kib\":"<<usage.ru_maxrss
      <<",\"projected_eight_worker_rss_kib\":"<<projected_rss
      <<",\"rows\":"<<row_count<<",\"eligible_banks\":"<<eligible
      <<",\"pairs\":"<<pairs<<",\"resultants\":"<<resultants
      <<",\"gcd_free_steps\":"<<steps<<",\"resource_rejects\":"<<resource_reject
      <<",\"serialized_corpus_bytes\":"<<sample_corpus.size()
      <<",\"serialized_bank_bytes\":"<<sample_banks.size()
      <<",\"serialized_family_bytes\":"<<sample_families.size()
      <<",\"serialized_certificate_bytes\":"<<sample_certificates.size()
      <<",\"serialized_opaque_bytes\":"<<sample_opaque.size()
      <<",\"measured_serialized_evidence_bytes\":"<<sample_output
      <<",\"projected_wall_seconds\":"<<projected_wall
      <<",\"projected_output_bytes\":"<<projected_output<<"}\n";
  write_text(output_path,json.str());
  std::cout<<(pass?"PREFLIGHT_PASS":"PREFLIGHT_FAIL")<<" projected_wall="
           <<projected_wall<<" projected_output="<<projected_output<<'\n';
  print_resources("preflight",start);
  if (!pass) std::exit(75);
}

void self_test() {
  require(sha256_bytes("abc")=="ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad",
          "SHA-256 self-test");
  cpp_int N=15,A0=1,B0=5,C0=6,delta=B0*B0-4*A0*C0,x=4;
  require(delta==1&&modz(delta-x*x,N)==0,"split source example");
  cpp_int root;
  require(squarez(delta,&root)&&gcdz(root-x,N)==3,"mixed singleton example");
  Mat2 M{1,2,1,3};require(determinant(M)==1,"test matrix determinant");
  cpp_int A=A0*M.a*M.a+B0*M.a*M.c+C0*M.c*M.c;
  cpp_int B=2*A0*M.a*M.b+B0*(M.a*M.d+M.b*M.c)+2*C0*M.c*M.d;
  cpp_int C=A0*M.b*M.b+B0*M.b*M.d+C0*M.d*M.d;
  require(B*B-4*A*C==delta,"raw discriminant self-test");
  BaseSource shared{0,2,3,5,cpp_int(79),cpp_int(157),cpp_int(236)};
  WordMatrix identity{Mat2{},0,-1,"I"},changed{M,3,0,"TEST"};
  Row level_one=make_row(cpp_int(77),shared,identity,1);
  Row level_two_identity=make_row(cpp_int(77),shared,identity,2);
  Row level_two_changed=make_row(cpp_int(77),shared,changed,2);
  require(level_two_identity.delta0==level_two_changed.delta0,
          "shared N^2 base discriminant self-test");
  require((level_two_identity.value-level_two_changed.value)%level_two_identity.modulus==0,
          "same-level carry quotient self-test");
  require((level_two_identity.value-level_one.value)%77==0,
          "cross-level carry quotient self-test");
  ProjectiveRoot pr{modz(cpp_int(M.d)*7-M.b,N),modz(cpp_int(M.a)-cpp_int(M.c)*7,N)};
  ProjectiveRoot ps{modz(cpp_int(M.d)*3-M.b,N),modz(cpp_int(M.a)-cpp_int(M.c)*3,N)};
  require(modz(pr.numerator*ps.denominator-ps.numerator*pr.denominator,N)==4,
          "projective root determinant self-test");
  Row f,g;f.A=1;f.B=0;f.C=-1;g.A=1;g.B=0;g.C=-4;
  require(quadratic_resultant(f,g)==9&&quadratic_resultant_formula(f,g)==9,
          "resultant self-test");
  Row r1,r2;r1.value=15;r1.root=57;r1.base_id=0;r1.level=1;r1.syntax="R1";
  r2.value=60;r2.root=51;r2.base_id=1;r2.level=2;r2.syntax="R2";
  std::vector<Row> rows{r1,r2};Decoder decoder=decode_rows(rows);
  require(decoder.ok&&decoder.kernel.size()==1,"P66 decoder self-test");
  Relation relation=verify_relation(decoder.kernel[0],cpp_int(77),rows);
  require(relation.root_class=="USEFUL"&&relation.gcd_minus==7&&relation.gcd_plus==11,
          "P66 normalized-root self-test");
  std::array<Stats,8> totals{};std::vector<int> ranked{0,1,2,3,4,5,6,7};
  std::string selection=selection_bytes(std::string(64,'a'),totals,ranked);
  Selection parsed=parse_selection(selection,sha256_bytes(selection));
  require(parsed.selected==std::vector<int>({0,1,2,3}),"selection parser self-test");
  std::string tampered=selection;
  std::string selected_line="selected\t0\t1\t2\t3\n";
  std::size_t selected_position=tampered.find(selected_line);
  require(selected_position!=std::string::npos,"selection self-test row absent");
  tampered.replace(selected_position,selected_line.size(),"selected\t0\t1\t2\t4\n");
  bool rejected=false;
  try { (void)parse_selection(tampered,sha256_bytes(tampered)); }
  catch (const std::exception&) { rejected=true; }
  require(rejected,"selection semantic tamper accepted");
  BankResult counted;
  record_factor(counted,cpp_int(2),cpp_int(15),"COUNTER_UNIT",false,DIRECT_SOURCE);
  record_factor(counted,cpp_int(0),cpp_int(15),"COUNTER_FULL",false,DIRECT_SOURCE);
  record_factor(counted,cpp_int(3),cpp_int(15),"COUNTER_PROPER",false,DIRECT_SOURCE);
  const DirectCounter& direct=counted.direct[DIRECT_SOURCE];
  require(direct.tests==3&&direct.unit==1&&direct.full==1&&direct.proper==1,
          "direct counter partition self-test");
  const std::array<std::string,8> expected_stage_names = {{
    "source","base","transformed","projective","resultant","carry",
    "singleton","equal_or_template"
  }};
  for (std::size_t i=0;i<expected_stage_names.size();++i)
    require(expected_stage_names[i]==DIRECT_STAGE_NAMES[i],"direct stage schema self-test");
  BankResult chronology;
  for (const cpp_int& candidate:std::array<cpp_int,4>{{2,3,5,4}})
    require(screened_unit(candidate,cpp_int(77),chronology,"SOURCE_SELF_TEST"),
            "source-stage allocation self-test");
  Row base_counter_row;
  base_counter_row.base_id=0;base_counter_row.level=1;
  base_counter_row.A0=2;base_counter_row.B0=3;base_counter_row.C0=5;
  base_counter_row.delta0=1;base_counter_row.root=4;
  chronology.rows={base_counter_row};
  screen_base_channels(cpp_int(77),chronology);
  require(chronology.direct[DIRECT_SOURCE].tests==4&&
          chronology.direct[DIRECT_SOURCE].unit==4&&
          chronology.direct[DIRECT_BASE].tests==5&&
          chronology.direct[DIRECT_BASE].unit==5,
          "source/base stage allocation self-test");
  for (int stage=DIRECT_TRANSFORMED;stage<=DIRECT_EQUAL_OR_TEMPLATE;++stage)
    require(chronology.direct[stage].tests==0,"later-stage allocation self-test");
  std::map<std::tuple<int,int,std::string>,u64> coverage;
  for (int bits:HELDOUT_BITS) for (const char* shape:SHAPES) {
    coverage[{0,bits,shape}]=bits==60?0:24;
    coverage[{1,bits,shape}]=bits==60?24:0;
  }
  require(find_coverage_family({0,1},coverage,24)==-1,
          "mixed-family coverage accepted");
  for (int bits:HELDOUT_BITS) for (const char* shape:SHAPES)
    coverage[{2,bits,shape}]=24;
  require(find_coverage_family({0,1,2},coverage,24)==2,
          "one-family coverage rejected");
  require(word_pool().size()>100,"SL2 word pool self-test");
  std::cout<<"SELF_TEST_PASS singleton_gcd=3 decoder_gcds=7,11 word_pool="
           <<word_pool().size()<<'\n';
}

}  // namespace

int main(int argc,char** argv) {
  try {
    if (argc==2&&std::string(argv[1])=="--self-test") {self_test();return 0;}
    if (argc==4&&std::string(argv[1])=="--preflight") {
      run_preflight(argv[2],std::stoi(argv[3]));return 0;
    }
    if (argc==4&&std::string(argv[1])=="--discovery") {
      run_discovery(argv[2],std::stoi(argv[3]));return 0;
    }
    if (argc==8&&std::string(argv[1])=="--heldout") {
      run_heldout(argv[2],argv[3],argv[4],argv[5],argv[6],std::stoi(argv[7]));return 0;
    }
    std::cerr<<"usage: search --self-test | --preflight FILE WORKERS | "
               "--discovery DIR WORKERS | --heldout DIR SELECTION SELECTION_SHA "
               "DISCOVERY_CORPUS CORPUS_SHA WORKERS\n";
    return 64;
  } catch (const std::exception& error) {
    std::cerr<<"F266_FATAL "<<error.what()<<'\n';return 70;
  }
}
