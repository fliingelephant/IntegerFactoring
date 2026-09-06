#include <algorithm>
#include <array>
#include <cerrno>
#include <chrono>
#include <cmath>
#include <cstdlib>
#include <cstdint>
#include <cstring>
#include <dirent.h>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <limits>
#include <map>
#include <memory>
#include <mutex>
#include <set>
#include <sstream>
#include <stdexcept>
#include <string>
#include <thread>
#include <tuple>
#include <unordered_map>
#include <utility>
#include <vector>

#include <sys/resource.h>
#include <sys/stat.h>

#include <boost/multiprecision/cpp_int.hpp>

using boost::multiprecision::cpp_int;
using u64 = std::uint64_t;
using u128 = __uint128_t;

static constexpr int DISCOVERY_BITS[] = {16, 24, 32};
static constexpr int HELDOUT_BITS[] = {40, 48, 56, 60};
static constexpr int ALL_BITS[] = {16, 24, 32, 40, 48, 56, 60};
static constexpr int D_VALUES[] = {2, 3, 5, 6, 7, 10, 11, 13};
static constexpr int MAX_SEQUENCE = 24;
static constexpr int MAX_PROGRAMS_PER_TYPE = 4096;
static constexpr int MAX_WORKERS = 8;
static constexpr int MAX_DPHI = 64;
static constexpr u64 MASTER_SEED = 0xF260D02A6C3E91B7ULL;
static constexpr u64 OUTPUT_CAP = 1073741824ULL;
static constexpr int COHORTS = 3;
static const char* COHORT_NAMES[] = {"random", "safe-safe", "consecutive"};
static const char* KIND_NAMES[] = {"sequence", "word", "factored"};

[[noreturn]] static void fail(const std::string& message) {
  throw std::runtime_error(message);
}

static void require(bool condition, const std::string& message) {
  if (!condition) fail(message);
}

static long double timeval_seconds(const timeval& t) {
  return static_cast<long double>(t.tv_sec) +
         static_cast<long double>(t.tv_usec) / 1000000.0L;
}

static void print_process_resources(const char* tag,
                                    std::chrono::steady_clock::time_point start) {
  rusage usage{};
  require(getrusage(RUSAGE_SELF, &usage) == 0, "getrusage");
  const double wall = std::chrono::duration<double>(
      std::chrono::steady_clock::now() - start).count();
  std::cout << std::fixed << std::setprecision(6)
            << tag << "_wall_seconds=" << wall << ' '
            << tag << "_user_seconds=" << timeval_seconds(usage.ru_utime) << ' '
            << tag << "_system_seconds=" << timeval_seconds(usage.ru_stime) << ' '
            << tag << "_maxrss_kib=" << usage.ru_maxrss << '\n';
}

static u64 mix64(u64 x) {
  x += 0x9e3779b97f4a7c15ULL;
  x = (x ^ (x >> 30)) * 0xbf58476d1ce4e5b9ULL;
  x = (x ^ (x >> 27)) * 0x94d049bb133111ebULL;
  return x ^ (x >> 31);
}

static u64 syntax_hash(const std::string& s) {
  u64 h = 0x243f6a8885a308d3ULL;
  for (unsigned char c : s) h = mix64(h ^ c);
  return h;
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

  void update(const unsigned char* data, std::size_t len) {
    total_ += len;
    while (len) {
      const std::size_t take = std::min<std::size_t>(len, 64 - used_);
      std::memcpy(block_.data() + used_, data, take);
      used_ += take;
      data += take;
      len -= take;
      if (used_ == 64) {
        compress(block_.data());
        used_ = 0;
      }
    }
  }

  void update(const std::string& s) {
    update(reinterpret_cast<const unsigned char*>(s.data()), s.size());
  }

  std::string final_hex() {
    const u64 bit_count = total_ * 8;
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
    for (u64 x : state_) out << std::setw(8) << static_cast<std::uint32_t>(x);
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
      0x19a4c116U,0x1e376c08U,0x2748774cU,0x34b0bcb5U,0x391c0cb3U,0x4ed8aa4aU,0x5b9cca4fU,0x682e6ff3U,
      0x748f82eeU,0x78a5636fU,0x84c87814U,0x8cc70208U,0x90befffaU,0xa4506cebU,0xbef9a3f7U,0xc67178f2U
    };
    std::uint32_t w[64];
    for (int i = 0; i < 16; ++i)
      w[i] = (std::uint32_t(b[4*i]) << 24) |
             (std::uint32_t(b[4*i+1]) << 16) |
             (std::uint32_t(b[4*i+2]) << 8) | b[4*i+3];
    for (int i = 16; i < 64; ++i) {
      const auto s0 = rotr(w[i-15],7) ^ rotr(w[i-15],18) ^ (w[i-15] >> 3);
      const auto s1 = rotr(w[i-2],17) ^ rotr(w[i-2],19) ^ (w[i-2] >> 10);
      w[i] = w[i-16] + s0 + w[i-7] + s1;
    }
    auto a=state_[0], b0=state_[1], c=state_[2], d=state_[3];
    auto e=state_[4], f=state_[5], g=state_[6], h=state_[7];
    for (int i = 0; i < 64; ++i) {
      const auto s1=rotr(e,6)^rotr(e,11)^rotr(e,25);
      const auto ch=(e&f)^((~e)&g);
      const auto t1=h+s1+ch+K[i]+w[i];
      const auto s0=rotr(a,2)^rotr(a,13)^rotr(a,22);
      const auto maj=(a&b0)^(a&c)^(b0&c);
      const auto t2=s0+maj;
      h=g; g=f; f=e; e=d+t1; d=c; c=b0; b0=a; a=t1+t2;
    }
    state_[0]+=a; state_[1]+=b0; state_[2]+=c; state_[3]+=d;
    state_[4]+=e; state_[5]+=f; state_[6]+=g; state_[7]+=h;
  }
};

static std::string sha256_bytes(const std::string& bytes) {
  Sha256 h;
  h.update(bytes);
  return h.final_hex();
}

static std::string read_binary_file(const std::string& path) {
  std::ifstream f(path, std::ios::binary);
  require(bool(f), "open input: " + path);
  std::ostringstream out;
  out << f.rdbuf();
  require(f.good() || f.eof(), "read input: " + path);
  return out.str();
}

static std::string sha256_file(const std::string& path) {
  std::ifstream f(path,std::ios::binary);
  require(bool(f),"open hash input: " + path);
  Sha256 hash;
  std::array<unsigned char,65536> buffer{};
  for (;;) {
    f.read(reinterpret_cast<char*>(buffer.data()),buffer.size());
    const std::streamsize got = f.gcount();
    if (got > 0) hash.update(buffer.data(),static_cast<std::size_t>(got));
    if (f.eof()) break;
    require(bool(f),"read hash input: " + path);
  }
  return hash.final_hex();
}

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
  for (u64 p : {2ULL,3ULL,5ULL,7ULL,11ULL,13ULL,17ULL,19ULL,
                23ULL,29ULL,31ULL,37ULL}) {
    if (n % p == 0) return n == p;
  }
  u64 d = n - 1;
  int s = 0;
  while ((d & 1) == 0) { d >>= 1; ++s; }
  for (u64 a : {2ULL,325ULL,9375ULL,28178ULL,450775ULL,
                9780504ULL,1795265022ULL}) {
    if (a % n == 0) continue;
    u64 x = pow_mod(a % n, d, n);
    if (x == 1 || x == n - 1) continue;
    bool witness = true;
    for (int r = 1; r < s; ++r) {
      x = mul_mod(x, x, n);
      if (x == n - 1) { witness = false; break; }
    }
    if (witness) return false;
  }
  return true;
}

static u64 random_prime(int bits, Rng& rng) {
  require(bits >= 3 && bits <= 60, "prime bit range");
  const u64 low = 1ULL << (bits - 1);
  const u64 high = (1ULL << bits) - 1;
  for (int draw = 0; draw < 200000; ++draw) {
    u64 x = (rng.next() & high) | low | 1ULL;
    for (int k = 0; k < 8192 && x <= high; ++k, x += 2)
      if (is_prime(x)) return x;
  }
  fail("random-prime retry cap");
}

static u64 random_safe_prime(int bits, Rng& rng) {
  for (int attempt = 0; attempt < 200000; ++attempt) {
    u64 r = random_prime(bits - 1, rng);
    u64 p = 2 * r + 1;
    if ((p >> (bits - 1)) == 1 && is_prime(p)) return p;
  }
  fail("safe-prime retry cap");
}

static u64 next_prime(u64 p) {
  u64 q = p + 2;
  for (int scan = 0; scan < 1000000; ++scan, q += 2)
    if (is_prime(q)) return q;
  fail("next-prime scan cap");
}

static u64 pollard_brent(u64 n, Rng& rng) {
  if ((n & 1) == 0) return 2;
  if (n % 3 == 0) return 3;
  for (int restart = 0; restart < 256; ++restart) {
    u64 y = 1 + rng.next() % (n - 1);
    u64 c = 1 + rng.next() % (n - 1);
    const u64 block = 128;
    u64 r = 1, qprod = 1, g = 1, x = 0, ys = 0;
    u64 steps = 0;
    while (g == 1 && steps < 10000000) {
      x = y;
      for (u64 i = 0; i < r && steps < 10000000; ++i, ++steps)
        y = (mul_mod(y, y, n) + c) % n;
      for (u64 k = 0; k < r && g == 1; k += block) {
        ys = y;
        const u64 lim = std::min(block, r - k);
        for (u64 i = 0; i < lim; ++i) {
          y = (mul_mod(y, y, n) + c) % n;
          const u64 diff = x > y ? x - y : y - x;
          qprod = mul_mod(qprod, diff, n);
        }
        g = std::gcd(qprod, n);
      }
      if (r > (1ULL << 32)) break;
      r <<= 1;
    }
    if (g == n) {
      g = 1;
      for (int tail = 0; tail < 1000000 && g == 1; ++tail) {
        ys = (mul_mod(ys, ys, n) + c) % n;
        const u64 diff = x > ys ? x - ys : ys - x;
        g = std::gcd(diff, n);
      }
    }
    if (g > 1 && g < n) return g;
  }
  fail("Pollard-Brent retry cap");
}

static void factor_rec(u64 n, std::map<u64,int>& out, Rng& rng, int depth=0) {
  require(depth <= 64, "factor recursion cap");
  if (n == 1) return;
  if (is_prime(n)) { ++out[n]; return; }
  u64 d = pollard_brent(n, rng);
  factor_rec(d, out, rng, depth + 1);
  factor_rec(n / d, out, rng, depth + 1);
}

static std::map<u64,int> factor_u64(u64 n, u64 seed) {
  require(n >= 1, "factor positive");
  std::map<u64,int> out;
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

static cpp_int gcd_cpp(cpp_int a, cpp_int b) {
  a = abs_cpp(a); b = abs_cpp(b);
  while (b != 0) { cpp_int r = a % b; a = b; b = r; }
  return a;
}

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
  while ((x & 1) == 0 && v < 128) { x >>= 1; ++v; }
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

static u64 integer_J(const cpp_int& N, int n) {
  cpp_int q = isqrt_cpp(isqrt_cpp(N));
  while ((q + 1) * (q + 1) * (q + 1) * (q + 1) <= N) ++q;
  while (q * q * q * q > N) --q;
  const bool exact = q * q * q * q == N;
  const u64 n2 = static_cast<u64>(n) * n;
  const u64 n4 = n2 * n2;
  const u64 floor_root = q.convert_to<u64>();
  u64 J = floor_root / n4;
  if (floor_root % n4 != 0 || !exact) ++J;
  return std::max<u64>(1, J);
}

static int phi_value(u64 J, u64 L) {
  if (J <= L) return 0;
  int k = 0;
  u64 x = L;
  while (x < J) {
    if (x > J / 2) x = J;
    else x *= 2;
    ++k;
  }
  return k;
}

static std::vector<cpp_int> canonical_sample(std::vector<cpp_int> values) {
  std::vector<cpp_int> unique;
  std::set<cpp_int> seen;
  for (auto& x : values)
    if (seen.insert(x).second) unique.push_back(std::move(x));
  if (static_cast<int>(unique.size()) <= MAX_SEQUENCE) return unique;
  std::vector<cpp_int> out;
  out.reserve(MAX_SEQUENCE);
  for (int i = 0; i < MAX_SEQUENCE; ++i) {
    const std::size_t at = static_cast<std::size_t>(i) * (unique.size() - 1) /
                           (MAX_SEQUENCE - 1);
    out.push_back(unique[at]);
  }
  return out;
}

static int bit_slot(int bits) {
  for (int i = 0; i < 7; ++i) if (ALL_BITS[i] == bits) return i;
  fail("unknown factor bit size");
}

static bool path_exists(const std::string& path) {
  struct stat st{};
  return stat(path.c_str(), &st) == 0;
}

static u64 directory_regular_bytes(const std::string& path) {
  DIR* raw = opendir(path.c_str());
  require(raw != nullptr, "open output directory");
  u64 total = 0;
  while (dirent* ent = readdir(raw)) {
    const std::string name = ent->d_name;
    if (name == "." || name == "..") continue;
    struct stat st{};
    const std::string full = path + "/" + name;
    require(stat(full.c_str(), &st) == 0, "stat output");
    if (S_ISREG(st.st_mode)) total += static_cast<u64>(st.st_size);
  }
  closedir(raw);
  return total;
}

struct OutputBudget {
  u64 bytes;
  explicit OutputBudget(u64 initial) : bytes(initial) {
    require(initial <= OUTPUT_CAP, "preexisting output exceeds cap");
  }
  void charge(std::size_t n) {
    require(n <= OUTPUT_CAP - bytes, "output cap before write");
    bytes += n;
  }
};

class CheckedFile {
 public:
  CheckedFile(const std::string& path, OutputBudget& budget)
      : path_(path), budget_(budget), out_(open_new(path)) {}

  void line(const std::string& s) {
    budget_.charge(s.size() + 1);
    out_ << s << '\n';
    require(bool(out_), "write output: " + path_);
    ++lines_;
  }

  void close() {
    if (closed_) return;
    out_.flush();
    require(bool(out_), "flush output: " + path_);
    out_.close();
    require(!out_.fail(), "close output: " + path_);
    closed_ = true;
  }

  u64 lines() const { return lines_; }
  ~CheckedFile() { if (!closed_) out_.close(); }

 private:
  std::string path_;
  OutputBudget& budget_;
  std::ofstream out_;
  u64 lines_ = 0;
  bool closed_ = false;

  static std::ofstream open_new(const std::string& path) {
    require(!path_exists(path), "refuse overwrite: " + path);
    std::ofstream f(path, std::ios::binary | std::ios::out);
    require(bool(f), "open output: " + path);
    return f;
  }
};

struct Ratio {
  cpp_int p = 1;
  cpp_int q = 1;
  bool valid = true;
};

static void reduce_ratio(Ratio& z) {
  cpp_int g = gcd_cpp(z.p, z.q);
  require(g != 0, "ratio zero pair");
  z.p /= g; z.q /= g;
  if (z.q < 0) { z.p = -z.p; z.q = -z.q; }
}

static Ratio binomial_ratio(u64 B, u64 H, int r, int c) {
  const long long top = static_cast<long long>(B) + c;
  const long long bot = static_cast<long long>(H) + r;
  if (top < 0 || bot < 0 || bot > top) return {0, 1, false};
  Ratio z;
  auto factorial_ratio = [&](long long a, long long b) {
    if (a > b) for (long long v = b + 1; v <= a; ++v) z.p *= v;
    else for (long long v = a + 1; v <= b; ++v) z.q *= v;
    reduce_ratio(z);
  };
  factorial_ratio(top, static_cast<long long>(B));
  factorial_ratio(static_cast<long long>(H), bot);
  factorial_ratio(static_cast<long long>(B - H), top - bot);
  reduce_ratio(z);
  return z;
}

struct ScalarLeaf {
  std::string syntax;
  cpp_int value;
};

struct BaseSequence {
  std::string name;
  std::vector<cpp_int> values;
  bool hyper = false;
};

struct PublicData {
  cpp_int N;
  int n = 0;
  u64 B2 = 0;
  u64 B = 0;
  std::vector<BaseSequence> base;
  std::vector<ScalarLeaf> scalars;
};

static std::pair<int,int> fundamental_pell(int D) {
  const int a0 = static_cast<int>(std::sqrt(D));
  int m = 0, den = 1, a = a0;
  long long pm = 1, p = a, qm = 0, q = 1;
  for (int steps = 0; steps < 100000; ++steps) {
    if (p * p - static_cast<long long>(D) * q * q == 1)
      return {static_cast<int>(p), static_cast<int>(q)};
    m = den * a - m;
    den = (D - m * m) / den;
    a = (a0 + m) / den;
    const long long pn = a * p + pm;
    const long long qn = a * q + qm;
    pm = p; qm = q; p = pn; q = qn;
  }
  fail("Pell period cap");
}

static PublicData build_public_data(const cpp_int& N) {
  PublicData d;
  d.N = N;
  d.n = bit_length(N);
  require(d.n >= 8 && d.n / 2 < 63, "public input bit range");
  d.B2 = 1ULL << (d.n / 2);
  d.B = isqrt_cpp(N).convert_to<u64>();

  auto scalar = [&](const std::string& syntax, const cpp_int& value) {
    d.scalars.push_back({syntax, value});
  };
  auto base = [&](const std::string& name, std::vector<cpp_int> values,
                  bool hyper=false) {
    d.base.push_back({name, canonical_sample(std::move(values)), hyper});
  };

  for (int k = 1; k <= d.n; ++k) scalar("const:" + std::to_string(k), k);
  const int prime_cap = d.n * d.n;
  std::vector<bool> sieve(prime_cap + 1, true);
  if (prime_cap >= 0) sieve[0] = false;
  if (prime_cap >= 1) sieve[1] = false;
  for (int p = 2; p * p <= prime_cap; ++p) if (sieve[p])
    for (int k = p * p; k <= prime_cap; k += p) sieve[k] = false;
  for (int p = 2; p <= prime_cap; ++p) if (sieve[p])
    scalar("prime:" + std::to_string(p), p);
  scalar("global:N-1", N - 1);
  scalar("global:N+1", N + 1);
  scalar("global:B", d.B);
  scalar("global:H", d.B / 2);
  scalar("global:N-B^2", N - cpp_int(d.B) * d.B);
  scalar("global:2B+1", cpp_int(2) * d.B + 1);

  std::set<int> js;
  for (int j = 1; j <= std::min(16, d.n - 1); ++j) js.insert(j);
  js.insert(std::max(1, d.n / 4));
  js.insert(std::max(1, d.n / 3));
  js.insert(std::max(1, d.n / 2));
  js.insert(std::max(1, 2 * (d.n / 3)));
  js.insert(std::max(1, 3 * (d.n / 4)));
  js.insert(std::max(1, d.n - 2));
  std::vector<cpp_int> dyq, dyr, dycenter, dycarry;
  for (int j : js) {
    if (j >= d.n) continue;
    const cpp_int mod = cpp_int(1) << j;
    const cpp_int q = N / mod;
    const cpp_int r = N % mod;
    cpp_int center = r;
    if (r * 2 >= mod) center -= mod;
    const cpp_int carry = q - 2 * (N / (cpp_int(mod) * 2));
    dyq.push_back(q); dyr.push_back(r); dycenter.push_back(center);
    dycarry.push_back(carry);
    const std::string tag = std::to_string(j);
    scalar("dyadic:q:" + tag, q);
    scalar("dyadic:r:" + tag, r);
    scalar("dyadic:center:" + tag, center);
    scalar("dyadic:carry:" + tag, carry);
  }
  base("dyadic_q", std::move(dyq));
  base("dyadic_r", std::move(dyr));
  base("dyadic_center", std::move(dycenter));
  base("dyadic_carry", std::move(dycarry));

  std::vector<cpp_int> halfq, halfr, halfcenter, halfadj;
  cpp_int prior = 0;
  for (int u = 1; u <= 31; u += 2) {
    const cpp_int value = cpp_int(u) * N;
    const cpp_int q = value / d.B2;
    const cpp_int r = value % d.B2;
    cpp_int center = r;
    if (r * 2 >= d.B2) center -= d.B2;
    halfq.push_back(q); halfr.push_back(r); halfcenter.push_back(center);
    scalar("half:q:" + std::to_string(u), q);
    scalar("half:r:" + std::to_string(u), r);
    scalar("half:center:" + std::to_string(u), center);
    if (u > 1) {
      const cpp_int diff = r - prior;
      halfadj.push_back(diff);
      scalar("half:adjacent_r:" + std::to_string(u - 2) + ":" +
             std::to_string(u), diff);
    }
    prior = r;
  }
  base("half_q", std::move(halfq));
  base("half_r", std::move(halfr));
  base("half_center", std::move(halfcenter));
  base("half_adjacent_r", std::move(halfadj));

  std::vector<cpp_int> sqrtq, sqrtr, sqrtcenter;
  for (int u = 1; u <= 16; ++u) for (int c = -8; c <= 8; ++c) {
    const long long den_ll = static_cast<long long>(d.B) + c;
    if (den_ll <= 0) continue;
    const u64 den = static_cast<u64>(den_ll);
    const cpp_int value = cpp_int(u) * N;
    const cpp_int q = value / den;
    const cpp_int r = value % den;
    cpp_int center = r;
    if (r * 2 >= den) center -= den;
    sqrtq.push_back(q); sqrtr.push_back(r); sqrtcenter.push_back(center);
    const std::string tag = std::to_string(u) + ":" + std::to_string(c);
    scalar("sqrt:q:" + tag, q);
    scalar("sqrt:r:" + tag, r);
    scalar("sqrt:center:" + tag, center);
  }
  base("sqrt_q", std::move(sqrtq));
  base("sqrt_r", std::move(sqrtr));
  base("sqrt_center", std::move(sqrtcenter));

  std::array<std::vector<cpp_int>,7> pell;
  for (int D : D_VALUES) {
    const auto [s0i,t0i] = fundamental_pell(D);
    cpp_int s = 1, t = 0, s0 = s0i, t0 = t0i;
    for (int j = 1; j <= std::min(32, 2 * d.n); ++j) {
      const cpp_int sn = s0 * s + D * t0 * t;
      const cpp_int tn = s0 * t + t0 * s;
      s = sn; t = tn;
      const cpp_int x = s % N, y = t % N;
      const cpp_int ell = (s - x) / N, k = (t - y) / N;
      const cpp_int gm = k * (x - 1) - y * ell;
      const cpp_int gp = k * (x + 1) - y * ell;
      const cpp_int norm = (x * x - D * y * y - 1) / N;
      const cpp_int vals[] = {x,y,k,ell,gm,gp,norm};
      const char* names[] = {"x","y","k","ell","gminus","gplus","norm"};
      for (int z = 0; z < 7; ++z) {
        pell[z].push_back(vals[z]);
        scalar("pell:" + std::to_string(D) + ":" + std::to_string(j) +
               ":" + names[z], vals[z]);
      }
    }
  }
  const char* pell_names[] = {"pell_x","pell_y","pell_k","pell_ell",
                              "pell_gminus","pell_gplus","pell_norm"};
  for (int i = 0; i < 7; ++i) base(pell_names[i], std::move(pell[i]));

  std::vector<cpp_int> hp, hq, hdet, vdet;
  std::map<std::pair<int,int>,Ratio> ratios;
  for (int c = -8; c <= 8; ++c) for (int r = -8; r <= 8; ++r) {
    Ratio z = binomial_ratio(d.B, d.B / 2, r, c);
    if (!z.valid) continue;
    ratios[{c,r}] = z;
    hp.push_back(z.p); hq.push_back(z.q);
    const std::string tag = std::to_string(c) + ":" + std::to_string(r);
    scalar("hyper:P:" + tag, z.p);
    scalar("hyper:Q:" + tag, z.q);
  }
  for (int c = -8; c <= 8; ++c) for (int r = -8; r < 8; ++r) {
    auto ia = ratios.find({c,r}), ib = ratios.find({c,r+1});
    if (ia == ratios.end() || ib == ratios.end()) continue;
    const cpp_int z = ia->second.p * ib->second.q -
                      ib->second.p * ia->second.q;
    hdet.push_back(z);
    scalar("hyper:det_h:" + std::to_string(c) + ":" + std::to_string(r), z);
  }
  for (int c = -8; c < 8; ++c) for (int r = -8; r <= 8; ++r) {
    auto ia = ratios.find({c,r}), ib = ratios.find({c+1,r});
    if (ia == ratios.end() || ib == ratios.end()) continue;
    const cpp_int z = ia->second.p * ib->second.q -
                      ib->second.p * ia->second.q;
    vdet.push_back(z);
    scalar("hyper:det_v:" + std::to_string(c) + ":" + std::to_string(r), z);
  }
  base("hyper_p", std::move(hp), true);
  base("hyper_q", std::move(hq), true);
  base("hyper_det_horizontal", std::move(hdet), true);
  base("hyper_det_vertical", std::move(vdet), true);

  require(d.base.size() == 22, "base source count");
  std::vector<ScalarLeaf> normalized;
  std::set<cpp_int> scalar_values;
  for (auto& x : d.scalars)
    if (scalar_values.insert(x.value).second) normalized.push_back(std::move(x));
  d.scalars = std::move(normalized);
  return d;
}

enum class Transform { ID, ADIFF, PDIFF, ASUM, AQUOT, AREM };
static const char* TRANSFORM_NAMES[] = {"id","adj_diff","pair_diff",
                                        "adj_sum","adj_quot","adj_rem"};

static std::vector<cpp_int> transform_sequence(const std::vector<cpp_int>& x,
                                                Transform t) {
  if (t == Transform::ID) return canonical_sample(x);
  std::vector<cpp_int> out;
  if (t == Transform::PDIFF) {
    for (std::size_t i = 0; i < x.size(); ++i)
      for (std::size_t j = i + 1; j < x.size(); ++j)
        out.push_back(abs_cpp(x[j] - x[i]));
    return canonical_sample(std::move(out));
  }
  for (std::size_t i = 1; i < x.size(); ++i) {
    cpp_int a = x[i-1], b = x[i];
    if (t == Transform::ADIFF) out.push_back(abs_cpp(b - a));
    if (t == Transform::ASUM) out.push_back(abs_cpp(a + b));
    if (t == Transform::AQUOT || t == Transform::AREM) {
      a = abs_cpp(a);
      b = abs_cpp(b);
      if (t == Transform::AQUOT)
        out.push_back(b == 0 ? cpp_int(0) : cpp_int(a / b));
      if (t == Transform::AREM)
        out.push_back(b == 0 ? cpp_int(0) : cpp_int(a % b));
    }
  }
  return canonical_sample(std::move(out));
}

static std::map<u64,int> smooth_factor_map(int cap) {
  require(cap >= 2 && cap <= 2000000, "smooth cap range");
  std::vector<bool> sieve(cap + 1, true);
  sieve[0] = sieve[1] = false;
  for (int p = 2; p * p <= cap; ++p) if (sieve[p])
    for (int k = p * p; k <= cap; k += p) sieve[k] = false;
  std::map<u64,int> out;
  for (int p = 2; p <= cap; ++p) if (sieve[p]) {
    u64 x = p;
    int e = 1;
    while (x <= static_cast<u64>(cap) / p) { x *= p; ++e; }
    out[p] = e;
  }
  return out;
}

static std::shared_ptr<const std::map<u64,int>> cached_smooth_factor_map(int cap) {
  static std::mutex mutex;
  static std::map<int,std::shared_ptr<const std::map<u64,int>>> cache;
  std::lock_guard<std::mutex> lock(mutex);
  auto it = cache.find(cap);
  if (it != cache.end()) return it->second;
  auto value = std::make_shared<const std::map<u64,int>>(smooth_factor_map(cap));
  cache.emplace(cap, value);
  return value;
}

struct SeqProgram {
  int base = 0;
  Transform transform = Transform::ID;
  int depth = 0;
  std::string name;
  std::array<u64,3> fingerprint{};
};

struct WordProgram {
  int a = -1;
  int b = -1;
  int depth = 0;
  std::string name;
  std::array<u64,3> fingerprint{};
};

enum class FactMode { SMOOTH, ORACLE };
struct FactProgram {
  FactMode mode = FactMode::SMOOTH;
  int parameter = 0;
  int depth = 0;
  std::string name;
  bool oracle = false;
  std::array<u64,3> fingerprint{};
};

enum class Kind { SEQUENCE=0, WORD=1, FACTORED=2 };
struct ProgramRef {
  Kind kind = Kind::SEQUENCE;
  int index = 0;
  int depth = 0;
  std::string name;
  bool operational = true;
  bool oracle = false;
  std::array<u64,3> fingerprint{};
  int global_id = -1;
};

struct Grammar {
  std::vector<SeqProgram> seq;
  std::vector<WordProgram> word;
  std::vector<FactProgram> fact;
  std::vector<ProgramRef> all;
  std::vector<std::string> controls;
};

static std::string fp_string(const std::array<u64,3>& fp) {
  std::ostringstream out;
  out << std::hex << std::setfill('0');
  for (u64 x : fp) out << std::setw(16) << x;
  return out.str();
}

static bool syntax_order(int da, const std::string& a,
                         int db, const std::string& b) {
  return std::make_tuple(da, a.size(), a) <
         std::make_tuple(db, b.size(), b);
}

static std::array<u64,3> fingerprint_seq(
    const SeqProgram& p, const std::vector<PublicData>& synthetic) {
  static constexpr u64 mods[] = {2305843009213693951ULL,
                                 2305843009213693921ULL,
                                 2305843009213693907ULL};
  std::array<u64,3> h = {mix64(1),mix64(2),mix64(3)};
  for (int t = 0; t < 24; ++t) {
    const auto values = transform_sequence(
        synthetic[t].base[p.base].values, p.transform);
    for (int k = 0; k < 3; ++k) {
      h[k] = mix64(h[k] ^ static_cast<u64>(values.size()) ^ (u64(t) << 32));
      for (const auto& x : values) h[k] = mix64(h[k] ^ mod_cpp(x, mods[k]));
    }
  }
  return h;
}

static std::array<u64,3> fingerprint_word(
    const WordProgram& p, const std::vector<SeqProgram>& seq,
    const std::vector<PublicData>& synthetic,
    const std::vector<std::array<std::array<u64,3>,24>>& residues) {
  static constexpr u64 mods[] = {2305843009213693951ULL,
                                 2305843009213693921ULL,
                                 2305843009213693907ULL};
  std::array<u64,3> h = {mix64(11),mix64(12),mix64(13)};
  (void)seq;
  for (int t = 0; t < 24; ++t) for (int k = 0; k < 3; ++k) {
    u64 value = pow_mod(mod_cpp(synthetic[t].N - 1, mods[k]),
                        synthetic[t].n, mods[k]);
    if (p.a >= 0) value = mul_mod(value, residues[p.a][t][k], mods[k]);
    if (p.b >= 0) value = mul_mod(value, residues[p.b][t][k], mods[k]);
    h[k] = mix64(h[k] ^ value ^ (u64(t) << 40));
  }
  return h;
}

static std::array<u64,3> fingerprint_fact(
    const FactProgram& p, const std::vector<PublicData>& synthetic) {
  static constexpr u64 mods[] = {2305843009213693951ULL,
                                 2305843009213693921ULL,
                                 2305843009213693907ULL};
  std::array<u64,3> h = {mix64(21),mix64(22),mix64(23)};
  for (int t = 0; t < 24; ++t) {
    std::array<u64,3> value = {1,1,1};
    if (p.mode == FactMode::SMOOTH) {
      int cap = synthetic[t].n;
      if (p.parameter == 2) cap *= synthetic[t].n;
      if (p.parameter == 3) cap *= synthetic[t].n * synthetic[t].n;
      const auto factors = cached_smooth_factor_map(cap);
      for (auto [ell,e] : *factors) for (int k = 0; k < 3; ++k)
        value[k] = mul_mod(value[k], pow_mod(ell % mods[k], e, mods[k]), mods[k]);
    } else {
      const auto& values = synthetic[t].base[p.parameter].values;
      cpp_int x = values.empty() ? cpp_int(1) : abs_cpp(values.front());
      const cpp_int bound = cpp_int(1) << ((synthetic[t].n + 1) / 2 + 2);
      if (!(x > 1 && x < bound && bit_length(x) <= 63)) x = 1;
      for (int k = 0; k < 3; ++k) value[k] = mod_cpp(x, mods[k]);
    }
    for (int k = 0; k < 3; ++k)
      h[k] = mix64(h[k] ^ value[k] ^ (u64(t) << 44));
  }
  return h;
}

static Grammar build_grammar() {
  std::vector<PublicData> synthetic;
  synthetic.reserve(24);
  for (int t = 0; t < 24; ++t)
    synthetic.push_back(build_public_data(
        cpp_int(1001 + 2 * t) * (2001 + 4 * t)));
  const auto& names = synthetic.front();

  std::vector<SeqProgram> raw_seq;
  for (int b = 0; b < static_cast<int>(names.base.size()); ++b) {
    const int transforms = names.base[b].hyper ? 1 : 6;
    for (int tr = 0; tr < transforms; ++tr) {
      SeqProgram p;
      p.base = b;
      p.transform = static_cast<Transform>(tr);
      p.depth = tr == 0 ? 0 : 1;
      p.name = "seq:" + names.base[b].name + ":" + TRANSFORM_NAMES[tr];
      p.fingerprint = fingerprint_seq(p, synthetic);
      raw_seq.push_back(std::move(p));
    }
  }
  Grammar g;
  std::map<std::array<u64,3>,SeqProgram> canonical_seq;
  for (auto& p : raw_seq) {
    auto it = canonical_seq.find(p.fingerprint);
    if (it == canonical_seq.end())
      canonical_seq.emplace(p.fingerprint,std::move(p));
    else if (p.name < it->second.name)
      it->second = std::move(p);
  }
  for (auto& [fingerprint,p] : canonical_seq) {
    (void)fingerprint;
    g.seq.push_back(std::move(p));
  }
  std::sort(g.seq.begin(), g.seq.end(), [](const auto& a, const auto& b) {
    return syntax_order(a.depth,a.name,b.depth,b.name);
  });
  if (g.seq.size() > MAX_PROGRAMS_PER_TYPE)
    g.seq.resize(MAX_PROGRAMS_PER_TYPE);
  require(!g.seq.empty(), "sequence grammar empty");

  static constexpr u64 mods[] = {2305843009213693951ULL,
                                 2305843009213693921ULL,
                                 2305843009213693907ULL};
  std::vector<std::array<std::array<u64,3>,24>> residues(g.seq.size());
  for (std::size_t i = 0; i < g.seq.size(); ++i) for (int t = 0; t < 24; ++t) {
    const auto values = transform_sequence(
        synthetic[t].base[g.seq[i].base].values, g.seq[i].transform);
    for (int k = 0; k < 3; ++k) {
      u64 value = 1;
      for (const auto& x : values) if (x != 0)
        value = mul_mod(value,
            pow_mod(mod_cpp(abs_cpp(x),mods[k]),synthetic[t].n,mods[k]),mods[k]);
      residues[i][t][k] = value;
    }
  }

  std::vector<WordProgram> raw_word;
  raw_word.push_back({-1,-1,0,"word:baseline",{}});
  for (int i = 0; i < static_cast<int>(g.seq.size()); ++i)
    raw_word.push_back({i,-1,1,"word:" + g.seq[i].name,{}});
  for (int i = 0; i < static_cast<int>(g.seq.size()); ++i)
    for (int j = i + 1; j < static_cast<int>(g.seq.size()); ++j) {
      const bool same_base = g.seq[i].base == g.seq[j].base;
      const bool both_id = g.seq[i].transform == Transform::ID &&
                           g.seq[j].transform == Transform::ID;
      int left = i, right = j;
      if (g.seq[right].name < g.seq[left].name) std::swap(left,right);
      const std::string name =
          "word:" + g.seq[left].name + "*" + g.seq[right].name;
      const bool sparse = syntax_hash(name) % 5 == 0;
      if (same_base || both_id || sparse)
        raw_word.push_back({left,right,2,name,{}});
    }
  for (auto& p : raw_word) {
    p.fingerprint = fingerprint_word(p,g.seq,synthetic,residues);
  }
  std::map<std::array<u64,3>,WordProgram> canonical_word;
  for (auto& p : raw_word) {
    auto it = canonical_word.find(p.fingerprint);
    if (it == canonical_word.end())
      canonical_word.emplace(p.fingerprint,std::move(p));
    else if (p.name < it->second.name)
      it->second = std::move(p);
  }
  for (auto& [fingerprint,p] : canonical_word) {
    (void)fingerprint;
    g.word.push_back(std::move(p));
  }
  std::sort(g.word.begin(), g.word.end(), [](const auto& a, const auto& b) {
    return syntax_order(a.depth,a.name,b.depth,b.name);
  });
  if (g.word.size() > MAX_PROGRAMS_PER_TYPE)
    g.word.resize(MAX_PROGRAMS_PER_TYPE);
  require(!g.word.empty(), "word grammar empty");

  std::map<std::string,int> base_id;
  for (int i = 0; i < static_cast<int>(names.base.size()); ++i)
    base_id[names.base[i].name] = i;
  std::vector<FactProgram> raw_fact = {
    {FactMode::SMOOTH,1,0,"factored:lcm_1_n",false,{}},
    {FactMode::SMOOTH,2,0,"factored:lcm_1_n2",false,{}},
    {FactMode::SMOOTH,3,0,"factored:lcm_1_n3",false,{}}
  };
  for (const std::string& name : {"dyadic_r","half_q","half_r",
                                  "sqrt_r","pell_y","hyper_p"}) {
    require(base_id.count(name) == 1, "oracle base name");
    raw_fact.push_back({FactMode::ORACLE,base_id[name],1,
                        "factored:recursive_first:" + name,true,{}});
  }
  for (auto& p : raw_fact) p.fingerprint = fingerprint_fact(p,synthetic);
  std::map<std::array<u64,3>,FactProgram> canonical_fact;
  for (auto& p : raw_fact) {
    auto it = canonical_fact.find(p.fingerprint);
    if (it == canonical_fact.end())
      canonical_fact.emplace(p.fingerprint,std::move(p));
    else if (p.name < it->second.name)
      it->second = std::move(p);
  }
  for (auto& [fingerprint,p] : canonical_fact) {
    (void)fingerprint;
    g.fact.push_back(std::move(p));
  }
  std::sort(g.fact.begin(), g.fact.end(), [](const auto& a, const auto& b) {
    return syntax_order(a.depth,a.name,b.depth,b.name);
  });
  if (g.fact.size() > MAX_PROGRAMS_PER_TYPE)
    g.fact.resize(MAX_PROGRAMS_PER_TYPE);
  require(g.fact.size() == 9, "factored canonical count");

  for (int i = 0; i < static_cast<int>(g.seq.size()); ++i)
    g.all.push_back({Kind::SEQUENCE,i,g.seq[i].depth,g.seq[i].name,true,false,
                     g.seq[i].fingerprint});
  for (int i = 0; i < static_cast<int>(g.word.size()); ++i)
    g.all.push_back({Kind::WORD,i,g.word[i].depth,g.word[i].name,true,false,
                     g.word[i].fingerprint});
  for (int i = 0; i < static_cast<int>(g.fact.size()); ++i)
    g.all.push_back({Kind::FACTORED,i,g.fact[i].depth,g.fact[i].name,
                     !g.fact[i].oracle,g.fact[i].oracle,g.fact[i].fingerprint});
  for (int i = 0; i < static_cast<int>(g.all.size()); ++i) g.all[i].global_id = i;
  g.controls.push_back("control:full_central_binomial:nonoperational:not_materialized");
  require(g.seq.size() <= MAX_PROGRAMS_PER_TYPE &&
          g.word.size() <= MAX_PROGRAMS_PER_TYPE &&
          g.fact.size() <= MAX_PROGRAMS_PER_TYPE, "grammar caps");
  return g;
}

struct CorpusRow {
  int bits = 0;
  int cohort = 0;
  int index = 0;
  u64 p = 0;
  u64 q = 0;
  cpp_int N;
};

static std::vector<CorpusRow> make_corpus(
    bool discovery, bool tiny=false,
    const std::set<std::string>& forbidden={}) {
  std::vector<CorpusRow> rows;
  std::set<std::string> seen = forbidden;
  const int* bits = discovery ? DISCOVERY_BITS : HELDOUT_BITS;
  const int nbits = discovery ? 3 : 4;
  for (int bi = 0; bi < nbits; ++bi) {
    const int b = bits[bi];
    int counts[3] = {discovery ? 2048 : 4096,
                     discovery ? (b == 16 ? 256 : 512) : 1024,
                     discovery ? 512 : 1024};
    if (tiny) counts[0] = counts[1] = counts[2] = 2;
    for (int cohort = 0; cohort < 3; ++cohort) {
      Rng rng(MASTER_SEED ^ (u64(discovery) << 63) ^ (u64(b) << 24) ^
              (u64(cohort) << 48));
      int accepted = 0;
      for (int attempts = 0; accepted < counts[cohort]; ++attempts) {
        require(attempts < 50000000, "corpus retry cap");
        u64 p = 0, q = 0;
        if (cohort == 1) {
          p = random_safe_prime(b,rng);
          q = random_safe_prime(b,rng);
          if (p == q) continue;
          if (p > q) std::swap(p,q);
        } else if (cohort == 2) {
          p = random_prime(b,rng);
          q = next_prime(p);
          if (bit_length(q) != b) continue;
        } else {
          p = random_prime(b,rng);
          q = random_prime(b,rng);
          if (p == q) continue;
          if (p > q) std::swap(p,q);
        }
        if (!(bit_length(p) == b && bit_length(q) == b && p < q && q < 2*p))
          continue;
        if (cohort == 1)
          require(is_prime((p-1)/2) && is_prime((q-1)/2), "safe cohort");
        if (cohort == 2) require(next_prime(p) == q, "consecutive cohort");
        const cpp_int N = cpp_int(p) * q;
        const std::string key = N.convert_to<std::string>();
        if (!seen.insert(key).second) continue;
        rows.push_back({b,cohort,accepted++,p,q,N});
      }
    }
  }
  return rows;
}

struct LocalLabels {
  u64 p=0, q=0, sp=0, sq=0, d=0;
  int vp2=0, vq2=0;
  std::map<u64,int> fp1, fq1, fd, fsp, fsq, hardp, hardq;
};

static std::map<u64,int> divide_factor_maps(const std::map<u64,int>& a,
                                             const std::map<u64,int>& b) {
  auto out = a;
  for (auto [p,e] : b) {
    auto it = out.find(p);
    require(it != out.end() && it->second >= e, "factor-map division");
    it->second -= e;
    if (it->second == 0) out.erase(it);
  }
  return out;
}

static LocalLabels make_labels(const CorpusRow& row) {
  LocalLabels z;
  z.p = row.p; z.q = row.q;
  z.fp1 = factor_u64(row.p - 1, MASTER_SEED ^ row.p);
  z.fq1 = factor_u64(row.q - 1, MASTER_SEED ^ row.q);
  z.d = std::gcd(row.p - 1,row.q - 1);
  z.fd = factor_u64(z.d, MASTER_SEED ^ z.d);
  z.sp = (row.p - 1) / z.d;
  z.sq = (row.q - 1) / z.d;
  z.fsp = divide_factor_maps(z.fp1,z.fd);
  z.fsq = divide_factor_maps(z.fq1,z.fd);
  z.hardp = z.fsp;
  z.hardq = z.fsq;
  for (auto it = z.hardp.begin(); it != z.hardp.end(); ) {
    if (mod_cpp(row.N - 1,it->first) == 0) it = z.hardp.erase(it);
    else ++it;
  }
  for (auto it = z.hardq.begin(); it != z.hardq.end(); ) {
    if (mod_cpp(row.N - 1,it->first) == 0) it = z.hardq.erase(it);
    else ++it;
  }
  z.vp2 = z.fp1.count(2) ? z.fp1.at(2) : 0;
  z.vq2 = z.fq1.count(2) ? z.fq1.at(2) : 0;
  return z;
}

struct GcdCertificate {
  int bits=0, cohort=0, index=0;
  std::string source;
  std::string factor;
};

struct GcdScreen {
  bool proper = false;
  u64 factor = 0;
  std::string source;
  u64 saturated = 0;
};

static GcdScreen screen_public_scalars(const PublicData& d,
                                       const CorpusRow& row,
                                       std::vector<GcdCertificate>& certs) {
  GcdScreen result;
  for (const auto& leaf : d.scalars) {
    const cpp_int g = gcd_cpp(abs_cpp(leaf.value),row.N);
    if (g == row.N) { ++result.saturated; continue; }
    if (g > 1) {
      const std::string factor = g.convert_to<std::string>();
      certs.push_back({row.bits,row.cohort,row.index,leaf.syntax,factor});
      if (!result.proper) {
        result.proper = true;
        result.factor = g.convert_to<u64>();
        result.source = leaf.syntax;
      }
    }
  }
  return result;
}

struct MillerScore {
  long double probability=0, H=0;
  u64 rp=1, rq=1;
};

static MillerScore miller_score(u64 wp, u64 wq, int v2_exponent,
                                const LocalLabels& z) {
  const u64 gp = std::gcd(z.sp,wp);
  const u64 gq = std::gcd(z.sq,wq);
  const u64 rp = z.sp / gp, rq = z.sq / gq;
  const long double ap = 1.0L / static_cast<long double>(rp);
  const long double aq = 1.0L / static_cast<long double>(rq);
  const int hp = std::min(z.vp2,v2_exponent);
  const int hq = std::min(z.vq2,v2_exponent);
  require(hp >= 1 && hq >= 1, "P205 two-primary support");
  const int a = std::min(hp,hq), b = std::max(hp,hq);
  const long double mu = 1.0L -
      (std::pow(4.0L,a) + 2.0L) /
      (3.0L * std::pow(2.0L,a+b));
  const long double probability = ap + aq - (2.0L-mu)*ap*aq;
  require(probability >= -1e-15L && probability <= 1+1e-12L,
          "P205 probability range");
  return {probability,std::max(ap,aq),rp,rq};
}

struct CollisionSide {
  long double captured_mass=0, captured_fraction=0, joint=0;
  u64 best_ell=0;
  int best_e=0;
  long double best_kappa=0, best_bits=0;
};

static u64 factor_map_value(const std::map<u64,int>& f) {
  u64 out = 1;
  for (auto [p,e] : f) for (int i = 0; i < e; ++i) {
    require(out <= std::numeric_limits<u64>::max()/p, "factor-map overflow");
    out *= p;
  }
  return out;
}

static CollisionSide collision_side(const std::vector<cpp_int>& values,
                                    const std::map<u64,int>& residual) {
  CollisionSide out;
  if (values.size() < 2) return out;
  const u64 pairs = static_cast<u64>(values.size()) * (values.size()-1);
  if (residual.empty()) {
    out.captured_fraction = 0;
    out.joint = 1;
    return out;
  }
  long double total_mass = 0;
  for (auto [ell,e] : residual) {
    std::unordered_map<u64,u64> buckets;
    for (const auto& x : values) ++buckets[mod_cpp(x,ell)];
    u64 collisions = 0;
    for (auto [r,c] : buckets) { (void)r; collisions += c*(c-1); }
    const long double kappa = static_cast<long double>(collisions)/pairs;
    const long double mass = e*std::log2(static_cast<long double>(ell));
    const long double contribution = kappa*mass;
    out.captured_mass += contribution;
    total_mass += mass;
    if (contribution > out.best_bits) {
      out.best_bits = contribution;
      out.best_ell = ell;
      out.best_e = e;
      out.best_kappa = kappa;
    }
  }
  out.captured_fraction = out.captured_mass/total_mass;
  const u64 residual_value = factor_map_value(residual);
  long double joint_sum = 0;
  for (std::size_t i = 0; i < values.size(); ++i)
    for (std::size_t j = 0; j < values.size(); ++j) if (i != j) {
      const cpp_int delta = abs_cpp(values[i]-values[j]);
      u64 captured = 1;
      for (auto [ell,e] : residual) if (mod_cpp(delta,ell) == 0)
        for (int k = 0; k < e; ++k) captured *= ell;
      joint_sum += static_cast<long double>(captured)/residual_value;
    }
  out.joint = joint_sum/pairs;
  return out;
}

struct SeqEval {
  std::vector<cpp_int> values;
  u64 prod_p=1, prod_q=1;
  int v2sum=0;
  bool direct=false, pair_direct=false;
  u64 factor=0, pair_factor=0, saturated=0, pair_saturated=0;
  long double pair_miller=0;
  CollisionSide cp, cq;
};

static SeqEval eval_sequence(const std::vector<cpp_int>& input,
                             const std::string& syntax,
                             const CorpusRow& row, const LocalLabels& z,
                             std::vector<GcdCertificate>& certs,
                             bool score_pairs) {
  SeqEval out;
  out.values = canonical_sample(input);
  for (const auto& raw : out.values) {
    const cpp_int x = abs_cpp(raw);
    const cpp_int g = gcd_cpp(x,row.N);
    if (g == row.N) ++out.saturated;
    else if (g > 1) {
      out.direct = true;
      out.factor = g.convert_to<u64>();
      certs.push_back({row.bits,row.cohort,row.index,syntax,g.convert_to<std::string>()});
    }
    if (x == 0) continue;
    out.prod_p = mul_mod(out.prod_p,mod_cpp(x,z.sp),z.sp);
    out.prod_q = mul_mod(out.prod_q,mod_cpp(x,z.sq),z.sq);
    out.v2sum = std::min(127,out.v2sum+v2_cpp(x));
  }
  if (!score_pairs) return out;
  out.cp = collision_side(out.values,z.hardp);
  out.cq = collision_side(out.values,z.hardq);
  if (out.values.size() < 2) return out;
  const u64 pairs = static_cast<u64>(out.values.size())*(out.values.size()-1);
  const int n = bit_length(row.N);
  const u64 basep = pow_mod(mod_cpp(row.N-1,z.sp),n,z.sp);
  const u64 baseq = pow_mod(mod_cpp(row.N-1,z.sq),n,z.sq);
  const int basev2 = std::min(127,(n+1)*v2_cpp(row.N-1));
  long double sum = 0;
  for (std::size_t i = 0; i < out.values.size(); ++i)
    for (std::size_t j = 0; j < out.values.size(); ++j) if (i != j) {
      const cpp_int delta = abs_cpp(out.values[i]-out.values[j]);
      require(delta != 0, "canonical distinct pair");
      const cpp_int gcd = gcd_cpp(delta,row.N);
      if (gcd == row.N) ++out.pair_saturated;
      if (gcd > 1 && gcd < row.N) {
        out.pair_direct = true;
        out.pair_factor = gcd.convert_to<u64>();
        certs.push_back({row.bits,row.cohort,row.index,syntax + ":pair:" +
                         std::to_string(i) + ":" + std::to_string(j),
                         gcd.convert_to<std::string>()});
      }
      const u64 dp = pow_mod(mod_cpp(delta,z.sp),n,z.sp);
      const u64 dq = pow_mod(mod_cpp(delta,z.sq),n,z.sq);
      const int vd = std::min(127,n*v2_cpp(delta));
      sum += miller_score(mul_mod(basep,dp,z.sp),mul_mod(baseq,dq,z.sq),
                          std::min(127,basev2+vd),z).probability;
    }
  out.pair_miller = sum/pairs;
  return out;
}

static int exponent_in(const std::map<u64,int>& f, u64 p) {
  auto it = f.find(p);
  return it == f.end() ? 0 : it->second;
}

static long double order_probability(u64 ell, int f, int t) {
  if (t == 0) return std::pow(static_cast<long double>(ell),-f);
  return (ell-1)*std::pow(static_cast<long double>(ell),t-1-f);
}

struct PrimaryLaw {
  u64 ell=0;
  int fp=0, fq=0;
  long double equal=0;
  std::vector<long double> equal_t;
};

struct StateScore {
  long double strict_growth=0;
  long double factor_or_growth=0;
  long double expected_log_gain=0;
};

struct DyadicLaw {
  int tbits=0, phi=0;
  long double expected=0;
  std::array<long double,MAX_DPHI+1> distribution{};
};

struct FactScore {
  long double direct_factor=0;
  long double factor_probability=0;
  StateScore m1, m2, hidden;
  std::array<DyadicLaw,3> dyadic;
  long double primary=0;
};

static u64 multiply_cap(u64 a, u64 b, u64 cap) {
  if (a >= cap || b >= cap) return cap;
  if (b != 0 && a > cap/b) return cap;
  return std::min(cap,a*b);
}

static u64 prime_power_cap(u64 p, int e, u64 cap) {
  u64 out = 1;
  for (int i = 0; i < e; ++i) out = multiply_cap(out,p,cap);
  return out;
}

static u64 lcm_cap(u64 a, u64 b, u64 cap) {
  if (a >= cap || b >= cap) return cap;
  const u64 g = std::gcd(a,b);
  return multiply_cap(a/g,b,cap);
}

static u64 state_lcm_cap(const std::map<u64,int>& M, int tbits, u64 cap) {
  u64 out = prime_power_cap(2,tbits,cap);
  for (auto [ell,e] : M) out = lcm_cap(out,prime_power_cap(ell,e,cap),cap);
  return out;
}

static StateScore score_state(const std::vector<PrimaryLaw>& laws,
                              const std::map<u64,int>& M,
                              long double direct, long double both,
                              long double equal_product) {
  long double stale_product = 1;
  long double gain_ratio_sum = 0;
  for (const auto& law : laws) {
    const int old = exponent_in(M,law.ell);
    long double stale = 0, gain = 0;
    for (int t = 0; t < static_cast<int>(law.equal_t.size()); ++t) {
      if (t <= old) stale += law.equal_t[t];
      if (t > old) gain += law.equal_t[t]*(t-old)*
          std::log2(static_cast<long double>(law.ell));
    }
    require(stale <= law.equal+1e-15L, "primary stale subset");
    stale_product *= stale;
    gain_ratio_sum += gain/law.equal;
  }
  StateScore out;
  out.strict_growth = both*(equal_product-stale_product);
  out.factor_or_growth = direct+both*(1-equal_product)+out.strict_growth;
  out.expected_log_gain = both*equal_product*gain_ratio_sum;
  require(out.strict_growth >= -1e-15L &&
          out.factor_or_growth >= -1e-15L && out.factor_or_growth <= 1+1e-12L,
          "state score range");
  return out;
}

static DyadicLaw score_dyadic(const std::vector<PrimaryLaw>& laws,
                              const std::map<u64,int>& M, int tbits,
                              u64 J, long double both,
                              long double equal_product) {
  DyadicLaw out;
  out.tbits = tbits;
  const u64 initial = state_lcm_cap(M,tbits,J);
  out.phi = phi_value(J,initial);
  if (out.phi == 0) {
    out.distribution[0] = both*equal_product;
    return out;
  }
  std::map<u64,long double> dp{{initial,1}};
  for (const auto& law : laws) {
    std::map<u64,long double> next;
    for (auto [state,mass] : dp)
      for (int t = 0; t < static_cast<int>(law.equal_t.size()); ++t) {
        const u64 primary = prime_power_cap(law.ell,t,J);
        const u64 updated = lcm_cap(state,primary,J);
        next[updated] += mass*law.equal_t[t];
      }
    dp.swap(next);
  }
  for (auto [state,mass] : dp) {
    const int delta = out.phi-phi_value(J,state);
    require(delta >= 0 && delta <= MAX_DPHI, "dyadic delta range");
    out.distribution[delta] += both*mass;
    out.expected += both*mass*delta;
  }
  return out;
}

static FactScore score_factored(const std::map<u64,int>& A,
                                const LocalLabels& z,
                                const cpp_int& N, int n) {
  u64 gcdp = 1, gcdq = 1;
  std::vector<PrimaryLaw> laws;
  auto ip = z.fp1.begin();
  auto iq = z.fq1.begin();
  while (ip != z.fp1.end() || iq != z.fq1.end()) {
    u64 ell = 0;
    if (iq == z.fq1.end() ||
        (ip != z.fp1.end() && ip->first < iq->first)) {
      ell = ip->first;
      ++ip;
    } else if (ip == z.fp1.end() || iq->first < ip->first) {
      ell = iq->first;
      ++iq;
    } else {
      ell = ip->first;
      ++ip;
      ++iq;
    }
    const auto admitted = A.find(ell);
    if (admitted == A.end()) continue;
    const int e = admitted->second;
    const int fp = std::min(e,exponent_in(z.fp1,ell));
    const int fq = std::min(e,exponent_in(z.fq1,ell));
    for (int k = 0; k < fp; ++k) gcdp *= ell;
    for (int k = 0; k < fq; ++k) gcdq *= ell;
    if (fp == 0 && fq == 0) continue;
    PrimaryLaw law;
    law.ell = ell; law.fp = fp; law.fq = fq;
    const int max_equal = std::min(fp,fq);
    law.equal_t.resize(max_equal+1);
    law.equal = 0;
    for (int t = 0; t <= max_equal; ++t) {
      law.equal_t[t] = order_probability(ell,fp,t)*order_probability(ell,fq,t);
      law.equal += law.equal_t[t];
    }
    require(law.equal > 0 && law.equal <= 1+1e-12L, "primary equality range");
    laws.push_back(std::move(law));
  }
  const long double ap = static_cast<long double>(gcdp)/(z.p-1);
  const long double aq = static_cast<long double>(gcdq)/(z.q-1);
  const long double both = ap*aq;
  const long double direct = ap+aq-2*both;
  long double equal_product = 1;
  for (const auto& law : laws) equal_product *= law.equal;
  FactScore out;
  out.direct_factor = direct;
  out.factor_probability = direct+both*(1-equal_product);
  static const std::map<u64,int> M1;
  static const std::map<u64,int> M2{{2,1}};
  out.m1 = score_state(laws,M1,direct,both,equal_product);
  out.m2 = score_state(laws,M2,direct,both,equal_product);
  out.hidden = score_state(laws,z.fd,direct,both,equal_product);
  const u64 J = integer_J(N,n);
  const int ts[] = {n/8,n/6,n/5};
  out.primary = std::max(out.m1.factor_or_growth,out.m2.factor_or_growth);
  for (int k = 0; k < 3; ++k) {
    out.dyadic[k] = score_dyadic(laws,M2,ts[k],J,both,equal_product);
    const long double channel = out.factor_probability +
        out.dyadic[k].expected/std::max(1,out.dyadic[k].phi);
    out.primary = std::max(out.primary,channel);
  }
  require(out.factor_probability >= -1e-12L && out.factor_probability <= 1+1e-9L,
          "factored factor range");
  require(out.primary >= -1e-12L && out.primary <= 1+1e-8L,
          "factored primary range");
  return out;
}

struct FactoredValue {
  std::shared_ptr<const std::map<u64,int>> shared;
  std::map<u64,int> owned;
  bool active = false;
  const std::map<u64,int>& get() const { return shared ? *shared : owned; }
};

static FactoredValue factored_program_value(const FactProgram& p,
                                            const PublicData& d) {
  FactoredValue out;
  if (p.mode == FactMode::SMOOTH) {
    int cap = d.n;
    if (p.parameter == 2) cap *= d.n;
    if (p.parameter == 3) cap *= d.n*d.n;
    out.shared = cached_smooth_factor_map(cap);
    out.active = true;
    return out;
  }
  const auto& values = d.base[p.parameter].values;
  if (values.empty()) return out;
  const cpp_int x = abs_cpp(values.front());
  const cpp_int bound = cpp_int(1) << ((d.n+1)/2+2);
  if (!(x > 1 && x < bound && bit_length(x) <= 63)) return out;
  const u64 seed = MASTER_SEED ^ syntax_hash(p.name) ^ mod_cpp(d.N,~u64(0));
  out.owned = factor_u64(x.convert_to<u64>(),seed);
  out.active = true;
  return out;
}

struct CollisionRecord {
  bool valid=false;
  int side=0, bits=0, cohort=0, index=0;
  u64 ell=0;
  int exponent=0;
  long double kappa=0, captured_bits=0;
};

struct Metrics {
  long double score=0, miller=0, H=0;
  long double collision=0, captured_p=0, captured_q=0, joint_p=0, joint_q=0;
  long double direct_probability=0, factor_probability=0;
  long double growth_m1=0, growth_m2=0, growth_hidden=0;
  long double factor_growth_m1=0, factor_growth_m2=0, factor_growth_hidden=0;
  long double gain_m1=0, gain_m2=0, gain_hidden=0;
  long double dyadic_expected=0;
  std::array<long double,3> dyadic_each{};
  std::array<std::array<long double,MAX_DPHI+1>,3> dphi_distribution{};
  long double residual_log_p=0, residual_log_q=0, baseline_improvement=0;
  long double expected_event=0;
  bool direct=false;
  u64 factor=0, saturated=0;
  CollisionRecord collision_record;
};

struct RowEvaluation {
  std::vector<Metrics> metrics;
  std::vector<GcdCertificate> certificates;
};

static RowEvaluation evaluate_row(const CorpusRow& row, const Grammar& g) {
  PublicData d = build_public_data(row.N);
  LocalLabels z = make_labels(row);
  RowEvaluation result;
  const GcdScreen common = screen_public_scalars(d,row,result.certificates);

  std::vector<bool> needed(g.seq.size(),false);
  std::vector<bool> selected_sequence(g.seq.size(),false);
  for (const auto& ref : g.all) {
    if (ref.kind == Kind::SEQUENCE) {
      needed[ref.index] = true;
      selected_sequence[ref.index] = true;
    }
    if (ref.kind == Kind::WORD) {
      const auto& p = g.word[ref.index];
      if (p.a >= 0) needed[p.a] = true;
      if (p.b >= 0) needed[p.b] = true;
    }
  }
  std::vector<SeqEval> seqeval(g.seq.size());
  for (std::size_t i = 0; i < g.seq.size(); ++i) if (needed[i]) {
    const auto& p = g.seq[i];
    seqeval[i] = eval_sequence(
        transform_sequence(d.base[p.base].values,p.transform),p.name,row,z,
        result.certificates,selected_sequence[i]);
  }

  const u64 baseline_p = pow_mod(mod_cpp(row.N-1,z.sp),d.n,z.sp);
  const u64 baseline_q = pow_mod(mod_cpp(row.N-1,z.sq),d.n,z.sq);
  const int baseline_v2 = std::min(127,(d.n+1)*v2_cpp(row.N-1));
  const MillerScore baseline = miller_score(
      baseline_p,baseline_q,baseline_v2,z);

  result.metrics.reserve(g.all.size());
  for (const auto& ref : g.all) {
    Metrics m;
    m.saturated = common.saturated;
    if (ref.kind == Kind::SEQUENCE) {
      const auto& e = seqeval[ref.index];
      m.direct = e.direct || e.pair_direct;
      m.factor = e.direct ? e.factor : e.pair_factor;
      m.saturated += e.saturated+e.pair_saturated;
      m.miller = m.direct ? 1 : e.pair_miller;
      m.score = m.miller;
      m.expected_event = m.miller;
      m.captured_p = e.cp.captured_mass;
      m.captured_q = e.cq.captured_mass;
      m.joint_p = e.cp.joint;
      m.joint_q = e.cq.joint;
      m.collision = std::min(e.cp.captured_fraction,e.cq.captured_fraction);
      const CollisionSide* best = &e.cp;
      int side = 0;
      if (e.cq.best_bits > e.cp.best_bits) { best = &e.cq; side = 1; }
      if (best->best_ell != 0) {
        m.collision_record = {true,side,row.bits,row.cohort,row.index,
                              best->best_ell,best->best_e,best->best_kappa,
                              best->best_bits};
      }
    } else if (ref.kind == Kind::WORD) {
      const auto& p = g.word[ref.index];
      u64 wp = baseline_p, wq = baseline_q;
      int v2w = baseline_v2;
      for (int idx : {p.a,p.b}) if (idx >= 0) {
        const auto& e = seqeval[idx];
        if (e.direct) { m.direct = true; m.factor = e.factor; }
        m.saturated += e.saturated;
        wp = mul_mod(wp,pow_mod(e.prod_p,d.n,z.sp),z.sp);
        wq = mul_mod(wq,pow_mod(e.prod_q,d.n,z.sq),z.sq);
        v2w = std::min(127,v2w+d.n*e.v2sum);
      }
      const MillerScore score = miller_score(wp,wq,v2w,z);
      m.miller = m.direct ? 1 : score.probability;
      m.score = m.miller;
      m.H = score.H;
      m.residual_log_p = std::log2(static_cast<long double>(score.rp));
      m.residual_log_q = std::log2(static_cast<long double>(score.rq));
      m.baseline_improvement = score.probability-baseline.probability;
      m.expected_event = m.miller;
    } else {
      const auto& p = g.fact[ref.index];
      FactoredValue value = factored_program_value(p,d);
      if (value.active) {
        if (p.mode == FactMode::ORACLE) {
          for (auto [ell,e] : value.get()) {
            (void)e;
            const cpp_int divisor_value = gcd_cpp(cpp_int(ell),row.N);
            if (divisor_value == row.N) ++m.saturated;
            if (divisor_value > 1 && divisor_value < row.N) {
              m.direct = true;
              m.factor = divisor_value.convert_to<u64>();
              result.certificates.push_back({row.bits,row.cohort,row.index,
                  p.name + ":factored_primary:" + std::to_string(ell),
                  divisor_value.convert_to<std::string>()});
            }
          }
        }
        if (p.mode == FactMode::SMOOTH && p.parameter == 3) {
          const u64 common_cap = static_cast<u64>(d.n)*d.n;
          const u64 cap = static_cast<u64>(d.n)*d.n*d.n;
          if (cpp_int(2)*cap*cap >= row.N) {
            cpp_int squarefree_residue = 1;
            for (auto [ell,e] : value.get()) if (ell > common_cap) {
              (void)e;
              squarefree_residue = (squarefree_residue*ell)%row.N;
            }
            const cpp_int divisor_value = gcd_cpp(squarefree_residue,row.N);
            if (divisor_value == row.N) ++m.saturated;
            if (divisor_value > 1 && divisor_value < row.N) {
              m.direct = true;
              m.factor = divisor_value.convert_to<u64>();
              result.certificates.push_back({row.bits,row.cohort,row.index,
                  p.name + ":squarefree_support_above_n2",
                  divisor_value.convert_to<std::string>()});
            }
          }
        }
        const FactScore f = score_factored(value.get(),z,row.N,d.n);
        m.score = m.direct ? 1 : f.primary;
        m.direct_probability = f.direct_factor;
        m.factor_probability = f.factor_probability;
        m.growth_m1 = f.m1.strict_growth;
        m.growth_m2 = f.m2.strict_growth;
        m.growth_hidden = f.hidden.strict_growth;
        m.factor_growth_m1 = f.m1.factor_or_growth;
        m.factor_growth_m2 = f.m2.factor_or_growth;
        m.factor_growth_hidden = f.hidden.factor_or_growth;
        m.gain_m1 = f.m1.expected_log_gain;
        m.gain_m2 = f.m2.expected_log_gain;
        m.gain_hidden = f.hidden.expected_log_gain;
        for (int k = 0; k < 3; ++k) {
          m.dyadic_each[k] = f.dyadic[k].expected;
          m.dyadic_expected += f.dyadic[k].expected/3;
          m.dphi_distribution[k] = f.dyadic[k].distribution;
        }
        m.expected_event = m.direct ? 1 : f.m2.factor_or_growth;
      }
    }
    if (common.proper) {
      m.direct = true;
      m.factor = common.factor;
      m.score = 1;
      m.miller = 1;
      m.expected_event = 1;
    }
    require(m.score >= -1e-12L && m.score <= 1+1e-8L,
            "row score range");
    result.metrics.push_back(std::move(m));
  }
  require(result.metrics.size() == g.all.size(), "row metric count");
  std::sort(result.certificates.begin(),result.certificates.end(),
      [](const auto& a,const auto& b) {
        return std::tie(a.bits,a.cohort,a.index,a.source,a.factor) <
               std::tie(b.bits,b.cohort,b.index,b.source,b.factor);
      });
  result.certificates.erase(std::unique(result.certificates.begin(),
      result.certificates.end(),[](const auto& a,const auto& b) {
        return a.bits==b.bits && a.cohort==b.cohort && a.index==b.index &&
               a.source==b.source && a.factor==b.factor;
      }),result.certificates.end());
  return result;
}

struct Cell {
  long double score=0, miller=0, H=0, collision=0;
  long double captured_p=0, captured_q=0, joint_p=0, joint_q=0;
  long double direct_probability=0, factor_probability=0;
  long double growth_m1=0, growth_m2=0, growth_hidden=0;
  long double factor_growth_m1=0, factor_growth_m2=0, factor_growth_hidden=0;
  long double gain_m1=0, gain_m2=0, gain_hidden=0;
  long double dyadic_expected=0;
  std::array<long double,3> dyadic_each{};
  std::array<std::vector<long double>,3> dphi_distribution;
  long double residual_log_p=0, residual_log_q=0, baseline_improvement=0;
  long double residual_log_p_min=0, residual_log_p_max=0;
  long double residual_log_q_min=0, residual_log_q_max=0;
  long double expected_event=0;
  u64 count=0, direct=0, saturated=0;
  bool have_residual_extrema=false;
  std::vector<double> collision_values;
  std::vector<double> score_values;
  CollisionRecord top_collision;
};

struct Aggregate {
  std::array<std::array<Cell,COHORTS>,7> cell;
};

struct CorpusEvaluation {
  std::vector<Aggregate> aggregate;
  std::vector<GcdCertificate> certificates;
};

static void add_metrics(Cell& c, const Metrics& m, bool keep_collision,
                        bool keep_score, bool is_sequence, bool is_word,
                        bool is_factored) {
  c.score += m.score; c.miller += m.miller; c.H += m.H;
  c.collision += m.collision;
  c.captured_p += m.captured_p; c.captured_q += m.captured_q;
  c.joint_p += m.joint_p; c.joint_q += m.joint_q;
  c.direct_probability += m.direct_probability;
  c.factor_probability += m.factor_probability;
  c.growth_m1 += m.growth_m1; c.growth_m2 += m.growth_m2;
  c.growth_hidden += m.growth_hidden;
  c.factor_growth_m1 += m.factor_growth_m1;
  c.factor_growth_m2 += m.factor_growth_m2;
  c.factor_growth_hidden += m.factor_growth_hidden;
  c.gain_m1 += m.gain_m1; c.gain_m2 += m.gain_m2;
  c.gain_hidden += m.gain_hidden;
  c.dyadic_expected += m.dyadic_expected;
  for (int k = 0; k < 3; ++k) {
    c.dyadic_each[k] += m.dyadic_each[k];
    if (is_factored) {
      if (c.dphi_distribution[k].empty())
        c.dphi_distribution[k].assign(MAX_DPHI+1,0);
      for (int d = 0; d <= MAX_DPHI; ++d)
        c.dphi_distribution[k][d] += m.dphi_distribution[k][d];
    }
  }
  c.residual_log_p += m.residual_log_p;
  c.residual_log_q += m.residual_log_q;
  if (is_word) {
    if (!c.have_residual_extrema) {
      c.residual_log_p_min = c.residual_log_p_max = m.residual_log_p;
      c.residual_log_q_min = c.residual_log_q_max = m.residual_log_q;
      c.have_residual_extrema = true;
    } else {
      c.residual_log_p_min = std::min(c.residual_log_p_min,m.residual_log_p);
      c.residual_log_p_max = std::max(c.residual_log_p_max,m.residual_log_p);
      c.residual_log_q_min = std::min(c.residual_log_q_min,m.residual_log_q);
      c.residual_log_q_max = std::max(c.residual_log_q_max,m.residual_log_q);
    }
  }
  c.baseline_improvement += m.baseline_improvement;
  c.expected_event += m.expected_event;
  ++c.count;
  if (m.direct) ++c.direct;
  c.saturated += m.saturated;
  if (keep_collision && is_sequence)
    c.collision_values.push_back(static_cast<double>(m.collision));
  if (keep_score) c.score_values.push_back(static_cast<double>(m.score));
  if (m.collision_record.valid &&
      (!c.top_collision.valid || m.collision_record.captured_bits >
                                 c.top_collision.captured_bits))
    c.top_collision = m.collision_record;
}

static CorpusEvaluation evaluate_corpus(const std::vector<CorpusRow>& rows,
                                        const Grammar& g, int workers,
                                        bool keep_collision,
                                        bool keep_score) {
  workers = std::max(1,std::min(workers,MAX_WORKERS));
  std::vector<std::vector<Aggregate>> local(
      workers,std::vector<Aggregate>(g.all.size()));
  std::vector<std::vector<GcdCertificate>> local_certificates(workers);
  std::vector<std::thread> threads;
  for (int w = 0; w < workers; ++w) threads.emplace_back([&,w]() {
    for (std::size_t at = w; at < rows.size(); at += workers) {
      RowEvaluation row = evaluate_row(rows[at],g);
      const int slot = bit_slot(rows[at].bits);
      const int cohort = rows[at].cohort;
      for (std::size_t i = 0; i < row.metrics.size(); ++i)
        add_metrics(local[w][i].cell[slot][cohort],row.metrics[i],
                    keep_collision,keep_score,
                    g.all[i].kind==Kind::SEQUENCE,
                    g.all[i].kind==Kind::WORD,
                    g.all[i].kind==Kind::FACTORED);
      local_certificates[w].insert(local_certificates[w].end(),
          row.certificates.begin(),row.certificates.end());
    }
  });
  for (auto& thread : threads) thread.join();

  CorpusEvaluation out;
  out.aggregate.resize(g.all.size());
  for (int w = 0; w < workers; ++w) {
    for (std::size_t i = 0; i < g.all.size(); ++i)
      for (int slot = 0; slot < 7; ++slot) for (int cohort = 0; cohort < 3; ++cohort) {
        Cell& a = out.aggregate[i].cell[slot][cohort];
        Cell& b = local[w][i].cell[slot][cohort];
        a.score += b.score; a.miller += b.miller; a.H += b.H;
        a.collision += b.collision;
        a.captured_p += b.captured_p; a.captured_q += b.captured_q;
        a.joint_p += b.joint_p; a.joint_q += b.joint_q;
        a.direct_probability += b.direct_probability;
        a.factor_probability += b.factor_probability;
        a.growth_m1 += b.growth_m1; a.growth_m2 += b.growth_m2;
        a.growth_hidden += b.growth_hidden;
        a.factor_growth_m1 += b.factor_growth_m1;
        a.factor_growth_m2 += b.factor_growth_m2;
        a.factor_growth_hidden += b.factor_growth_hidden;
        a.gain_m1 += b.gain_m1; a.gain_m2 += b.gain_m2;
        a.gain_hidden += b.gain_hidden;
        a.dyadic_expected += b.dyadic_expected;
        for (int k = 0; k < 3; ++k) {
          a.dyadic_each[k] += b.dyadic_each[k];
          if (!b.dphi_distribution[k].empty()) {
            if (a.dphi_distribution[k].empty())
              a.dphi_distribution[k].assign(MAX_DPHI+1,0);
            for (int d = 0; d <= MAX_DPHI; ++d)
              a.dphi_distribution[k][d] += b.dphi_distribution[k][d];
          }
        }
        a.residual_log_p += b.residual_log_p;
        a.residual_log_q += b.residual_log_q;
        if (b.have_residual_extrema) {
          if (!a.have_residual_extrema) {
            a.residual_log_p_min = b.residual_log_p_min;
            a.residual_log_p_max = b.residual_log_p_max;
            a.residual_log_q_min = b.residual_log_q_min;
            a.residual_log_q_max = b.residual_log_q_max;
            a.have_residual_extrema = true;
          } else {
            a.residual_log_p_min =
                std::min(a.residual_log_p_min,b.residual_log_p_min);
            a.residual_log_p_max =
                std::max(a.residual_log_p_max,b.residual_log_p_max);
            a.residual_log_q_min =
                std::min(a.residual_log_q_min,b.residual_log_q_min);
            a.residual_log_q_max =
                std::max(a.residual_log_q_max,b.residual_log_q_max);
          }
        }
        a.baseline_improvement += b.baseline_improvement;
        a.expected_event += b.expected_event;
        a.count += b.count; a.direct += b.direct; a.saturated += b.saturated;
        a.collision_values.insert(a.collision_values.end(),
                                  b.collision_values.begin(),b.collision_values.end());
        a.score_values.insert(a.score_values.end(),
                              b.score_values.begin(),b.score_values.end());
        if (b.top_collision.valid &&
            (!a.top_collision.valid || b.top_collision.captured_bits >
                                       a.top_collision.captured_bits))
          a.top_collision = b.top_collision;
      }
    out.certificates.insert(out.certificates.end(),local_certificates[w].begin(),
                            local_certificates[w].end());
  }
  std::sort(out.certificates.begin(),out.certificates.end(),
      [](const auto& a,const auto& b) {
        return std::tie(a.bits,a.cohort,a.index,a.source,a.factor) <
               std::tie(b.bits,b.cohort,b.index,b.source,b.factor);
      });
  out.certificates.erase(std::unique(out.certificates.begin(),out.certificates.end(),
      [](const auto& a,const auto& b) {
        return a.bits==b.bits && a.cohort==b.cohort && a.index==b.index &&
               a.source==b.source && a.factor==b.factor;
      }),out.certificates.end());
  return out;
}

static long double upper_median(std::vector<double> values) {
  if (values.empty()) return 0;
  std::sort(values.begin(),values.end());
  return values[values.size()/2];
}

static long double upper_median_loss(const std::vector<double>& scores) {
  if (scores.empty()) return std::numeric_limits<long double>::infinity();
  std::vector<double> losses;
  losses.reserve(scores.size());
  for (double score : scores)
    losses.push_back(score > 0 ? -std::log2(score) :
                     std::numeric_limits<double>::infinity());
  return upper_median(std::move(losses));
}

static long double cohort_mean(const Aggregate& a, int cohort, int field) {
  long double sum = 0;
  u64 count = 0;
  for (int slot = 0; slot < 3; ++slot) {
    const Cell& c = a.cell[slot][cohort];
    count += c.count;
    if (field == 0) sum += c.score;
    if (field == 1) sum += c.miller;
    if (field == 2) sum += c.collision;
    if (field == 3) sum += c.dyadic_expected;
  }
  return count ? sum/count : 0;
}

static long double min_cohort_mean(const Aggregate& a, int field) {
  long double out = std::numeric_limits<long double>::infinity();
  for (int cohort = 0; cohort < 3; ++cohort)
    out = std::min(out,cohort_mean(a,cohort,field));
  return std::isfinite(out) ? out : 0;
}

static long double min_collision_median(const Aggregate& a) {
  long double out = std::numeric_limits<long double>::infinity();
  for (int cohort = 0; cohort < 3; ++cohort) {
    std::vector<double> values;
    for (int slot = 0; slot < 3; ++slot) {
      const auto& v = a.cell[slot][cohort].collision_values;
      values.insert(values.end(),v.begin(),v.end());
    }
    out = std::min(out,upper_median(std::move(values)));
  }
  return std::isfinite(out) ? out : 0;
}

static std::vector<int> rank_programs(const Grammar& g,
                                      const std::vector<Aggregate>& a,
                                      int order) {
  std::vector<int> ids;
  for (int i = 0; i < static_cast<int>(g.all.size()); ++i)
    if (g.all[i].operational) ids.push_back(i);
  std::sort(ids.begin(),ids.end(),[&](int x,int y) {
    const long double sx = order == 1 ? min_cohort_mean(a[x],0) :
                           order == 2 ? min_collision_median(a[x]) :
                           order == 3 ? min_cohort_mean(a[x],1) :
                                        min_cohort_mean(a[x],3);
    const long double sy = order == 1 ? min_cohort_mean(a[y],0) :
                           order == 2 ? min_collision_median(a[y]) :
                           order == 3 ? min_cohort_mean(a[y],1) :
                                        min_cohort_mean(a[y],3);
    if (sx != sy) return sx > sy;
    return g.all[x].name < g.all[y].name;
  });
  return ids;
}

static std::vector<int> select_programs(const Grammar& g,
                                        const std::vector<Aggregate>& a) {
  std::array<std::vector<int>,4> ranks;
  for (int order = 1; order <= 4; ++order) ranks[order-1] = rank_programs(g,a,order);
  std::vector<int> selected;
  std::set<int> used;
  for (int order = 0; order < 4; ++order) {
    require(ranks[order].size() >= 8, "ranking has eight programs");
    for (int at = 0; at < 8; ++at)
      if (used.insert(ranks[order][at]).second) selected.push_back(ranks[order][at]);
  }
  for (int id : ranks[0]) {
    if (selected.size() == 32) break;
    if (used.insert(id).second) selected.push_back(id);
  }
  require(selected.size() == 32, "selection size");
  return selected;
}

static std::string number(long double x) {
  std::ostringstream out;
  out << std::setprecision(18) << x;
  return out.str();
}

static std::string distribution_string(const Cell& c, int k) {
  if (c.dphi_distribution[k].empty() || c.count == 0) return "";
  std::ostringstream out;
  out << std::setprecision(18);
  bool first = true;
  for (int d = 0; d <= MAX_DPHI; ++d) {
    const long double value = c.dphi_distribution[k][d]/c.count;
    if (value == 0) continue;
    if (!first) out << ';';
    first = false;
    out << d << ':' << value;
  }
  return out.str();
}

static u64 write_grammar(const std::string& path, const Grammar& g,
                         OutputBudget& budget) {
  CheckedFile f(path,budget);
  f.line("id\tkind\tdepth\toperational\toracle\tfingerprint\tsyntax");
  for (const auto& p : g.all) {
    f.line(std::to_string(p.global_id) + "\t" + KIND_NAMES[static_cast<int>(p.kind)] +
           "\t" + std::to_string(p.depth) + "\t" +
           std::to_string(p.operational) + "\t" + std::to_string(p.oracle) +
           "\t" + fp_string(p.fingerprint) + "\t" + p.name);
  }
  for (const auto& control : g.controls)
    f.line("-1\tcontrol\t0\t0\t1\t" +
           fp_string(std::array<u64,3>{
               syntax_hash(control),mix64(syntax_hash(control)),
               mix64(mix64(syntax_hash(control)))}) + "\t" + control);
  const u64 lines = f.lines();
  f.close();
  return lines;
}

static u64 write_corpus(const std::string& path,
                        const std::vector<CorpusRow>& rows,
                        OutputBudget& budget) {
  CheckedFile f(path,budget);
  f.line("factor_bits\tcohort\tindex\tN");
  for (const auto& row : rows)
    f.line(std::to_string(row.bits) + "\t" + COHORT_NAMES[row.cohort] + "\t" +
           std::to_string(row.index) + "\t" + row.N.convert_to<std::string>());
  const u64 lines = f.lines();
  f.close();
  return lines;
}

static u64 write_digest(const std::string& path, const std::string& digest,
                        const std::string& label, OutputBudget& budget) {
  require(digest.size() == 64, "digest length");
  CheckedFile f(path,budget);
  f.line(digest + "  " + label);
  f.close();
  return 1;
}

static u64 write_aggregates(const std::string& path, const std::string& split,
                            const Grammar& g,
                            const std::vector<Aggregate>& a,
                            const int* bits, int nbits,
                            OutputBudget& budget) {
  require(a.size() == g.all.size(), "aggregate program count");
  CheckedFile f(path,budget);
  f.line("id\tsyntax\tkind\toperational\toracle\tsplit\tfactor_bits\tcohort\tcount"
         "\tmean_score\tmean_miller\tmean_H\tmean_collision_fraction"
         "\tmean_captured_log_mass_p\tmean_captured_log_mass_q"
         "\tmean_joint_p\tmean_joint_q"
         "\tmean_direct_probability\tmean_factor_probability"
         "\tmean_strict_growth_M1\tmean_strict_growth_M2"
         "\tmean_strict_growth_hidden"
         "\tmean_factor_or_growth_M1\tmean_factor_or_growth_M2"
         "\tmean_factor_or_growth_hidden"
         "\tmean_expected_log_gain_M1\tmean_expected_log_gain_M2"
         "\tmean_expected_log_gain_hidden"
         "\tmean_dphi\tmean_dphi_t0\tmean_dphi_t1\tmean_dphi_t2"
         "\tdphi_dist_t0\tdphi_dist_t1\tdphi_dist_t2"
         "\tmean_log_rp\tmin_log_rp\tmax_log_rp"
         "\tmean_log_rq\tmin_log_rq\tmax_log_rq"
         "\tmean_baseline_improvement"
         "\texpected_certificate_mass\tdirect_gcds\tsaturated_gcds");
  for (std::size_t id = 0; id < g.all.size(); ++id) for (int bi = 0; bi < nbits; ++bi)
    for (int cohort = 0; cohort < 3; ++cohort) {
      const Cell& c = a[id].cell[bit_slot(bits[bi])][cohort];
      require(c.count > 0, "nonempty aggregate cell");
      const bool is_word = g.all[id].kind == Kind::WORD;
      require(!is_word || c.have_residual_extrema,
              "word residual extrema present");
      const long double den = c.count;
      const long double min_rp = is_word ? c.residual_log_p_min : 0;
      const long double max_rp = is_word ? c.residual_log_p_max : 0;
      const long double min_rq = is_word ? c.residual_log_q_min : 0;
      const long double max_rq = is_word ? c.residual_log_q_max : 0;
      std::ostringstream line;
      line << std::setprecision(18)
           << g.all[id].global_id << '\t' << g.all[id].name << '\t'
           << KIND_NAMES[static_cast<int>(g.all[id].kind)] << '\t'
           << g.all[id].operational << '\t' << g.all[id].oracle << '\t'
           << split << '\t' << bits[bi] << '\t' << COHORT_NAMES[cohort] << '\t'
           << c.count << '\t' << c.score/den << '\t' << c.miller/den << '\t'
           << c.H/den << '\t' << c.collision/den << '\t'
           << c.captured_p/den << '\t' << c.captured_q/den << '\t'
           << c.joint_p/den << '\t' << c.joint_q/den << '\t'
           << c.direct_probability/den << '\t' << c.factor_probability/den << '\t'
           << c.growth_m1/den << '\t' << c.growth_m2/den << '\t'
           << c.growth_hidden/den << '\t' << c.factor_growth_m1/den << '\t'
           << c.factor_growth_m2/den << '\t' << c.factor_growth_hidden/den << '\t'
           << c.gain_m1/den << '\t'
           << c.gain_m2/den << '\t' << c.gain_hidden/den << '\t'
           << c.dyadic_expected/den << '\t' << c.dyadic_each[0]/den << '\t'
           << c.dyadic_each[1]/den << '\t' << c.dyadic_each[2]/den << '\t'
           << distribution_string(c,0) << '\t' << distribution_string(c,1) << '\t'
           << distribution_string(c,2) << '\t' << c.residual_log_p/den << '\t'
           << min_rp << '\t' << max_rp << '\t' << c.residual_log_q/den << '\t'
           << min_rq << '\t' << max_rq << '\t' << c.baseline_improvement/den << '\t'
           << c.expected_event << '\t' << c.direct << '\t' << c.saturated;
      f.line(line.str());
    }
  const u64 lines = f.lines();
  f.close();
  return lines;
}

static u64 write_certificates(const std::string& path, const std::string& split,
                              const std::vector<GcdCertificate>& certificates,
                              OutputBudget& budget) {
  CheckedFile f(path,budget);
  f.line("split\tfactor_bits\tcohort\tindex\tsource\tfactor");
  for (const auto& c : certificates)
    f.line(split + "\t" + std::to_string(c.bits) + "\t" +
           COHORT_NAMES[c.cohort] + "\t" + std::to_string(c.index) + "\t" +
           c.source + "\t" + c.factor);
  const u64 lines = f.lines();
  f.close();
  return lines;
}

static u64 write_collisions(const std::string& path, const std::string& split,
                            const Grammar& g,
                            const std::vector<Aggregate>& a,
                            const int* bits, int nbits,
                            OutputBudget& budget) {
  CheckedFile f(path,budget);
  f.line("id\tsyntax\tsplit\tfactor_bits\tcohort\trow_index\tside\tell\texponent"
         "\tkappa\tcaptured_bits");
  for (std::size_t id = 0; id < g.all.size(); ++id) {
    if (g.all[id].kind != Kind::SEQUENCE) continue;
    for (int bi = 0; bi < nbits; ++bi) for (int cohort = 0; cohort < 3; ++cohort) {
      const auto& r = a[id].cell[bit_slot(bits[bi])][cohort].top_collision;
      if (!r.valid) continue;
      std::ostringstream line;
      line << std::setprecision(18) << g.all[id].global_id << '\t' << g.all[id].name
           << '\t' << split << '\t' << bits[bi] << '\t' << COHORT_NAMES[cohort]
           << '\t' << r.index << '\t' << (r.side==0 ? "p" : "q") << '\t'
           << r.ell << '\t' << r.exponent << '\t' << r.kappa << '\t'
           << r.captured_bits;
      f.line(line.str());
    }
  }
  const u64 lines = f.lines();
  f.close();
  return lines;
}

static u64 write_oracles(const std::string& path, const Grammar& g,
                         const std::vector<Aggregate>& a,
                         OutputBudget& budget) {
  std::vector<int> ids;
  for (int i = 0; i < static_cast<int>(g.all.size()); ++i)
    if (g.all[i].oracle) ids.push_back(i);
  std::sort(ids.begin(),ids.end(),[&](int x,int y) {
    const auto sx = min_cohort_mean(a[x],0), sy = min_cohort_mean(a[y],0);
    if (sx != sy) return sx > sy;
    return g.all[x].name < g.all[y].name;
  });
  CheckedFile f(path,budget);
  f.line("diagnostic_rank\tid\tfingerprint\tmin_mean_score\tsyntax");
  for (std::size_t rank = 0; rank < ids.size(); ++rank) {
    const int id = ids[rank];
    f.line(std::to_string(rank+1) + "\t" + std::to_string(g.all[id].global_id) +
           "\t" + fp_string(g.all[id].fingerprint) + "\t" +
           number(min_cohort_mean(a[id],0)) + "\t" + g.all[id].name);
  }
  const u64 lines = f.lines();
  f.close();
  return lines;
}

static std::string selection_header() {
  return "id\tkind\toperational\toracle\tfingerprint\tmin_score\tmin_miller"
         "\tmin_collision_mean\tmin_collision_median\tmin_dphi\tsyntax";
}

static u64 write_selection(const std::string& path, const Grammar& g,
                           const std::vector<Aggregate>& a,
                           const std::vector<int>& ids,
                           OutputBudget& budget) {
  require(ids.size() == 32, "write 32 selection rows");
  CheckedFile f(path,budget);
  f.line(selection_header());
  for (int id : ids) {
    const auto& p = g.all[id];
    std::ostringstream line;
    line << std::setprecision(18) << p.global_id << '\t'
         << KIND_NAMES[static_cast<int>(p.kind)] << '\t' << p.operational << '\t'
         << p.oracle << '\t' << fp_string(p.fingerprint) << '\t'
         << min_cohort_mean(a[id],0) << '\t' << min_cohort_mean(a[id],1) << '\t'
         << min_cohort_mean(a[id],2) << '\t' << min_collision_median(a[id]) << '\t'
         << min_cohort_mean(a[id],3) << '\t' << p.name;
    f.line(line.str());
  }
  const u64 lines = f.lines();
  f.close();
  return lines;
}

static std::string join_path(const std::string& directory,
                             const std::string& name) {
  return directory + "/" + name;
}

static std::vector<std::string> split_lines(const std::string& bytes) {
  require(!bytes.empty() && bytes.back() == '\n', "text requires final newline");
  std::vector<std::string> lines;
  std::size_t begin = 0;
  while (begin < bytes.size()) {
    const std::size_t end = bytes.find('\n',begin);
    require(end != std::string::npos, "unterminated text line");
    std::string line = bytes.substr(begin,end-begin);
    require(line.find('\r') == std::string::npos, "carriage return forbidden");
    lines.push_back(std::move(line));
    begin = end + 1;
  }
  return lines;
}

static std::vector<std::string> split_tabs(const std::string& line) {
  std::vector<std::string> fields;
  std::size_t begin = 0;
  for (;;) {
    const std::size_t end = line.find('\t',begin);
    if (end == std::string::npos) {
      fields.push_back(line.substr(begin));
      return fields;
    }
    fields.push_back(line.substr(begin,end-begin));
    begin = end + 1;
  }
}

static long long parse_integer(const std::string& text, long long low,
                               long long high, const std::string& label) {
  require(!text.empty(), "empty integer: " + label);
  errno = 0;
  char* end = nullptr;
  const long long value = std::strtoll(text.c_str(),&end,10);
  require(errno == 0 && end == text.c_str()+text.size() &&
          value >= low && value <= high, "invalid integer: " + label);
  return value;
}

static long double parse_finite(const std::string& text,
                                const std::string& label) {
  require(!text.empty(), "empty number: " + label);
  errno = 0;
  char* end = nullptr;
  const long double value = std::strtold(text.c_str(),&end);
  require(errno == 0 && end == text.c_str()+text.size() && std::isfinite(value),
          "invalid finite number: " + label);
  return value;
}

static cpp_int parse_decimal(const std::string& text,
                             const std::string& label) {
  require(!text.empty(), "empty decimal: " + label);
  cpp_int value = 0;
  for (unsigned char c : text) {
    require(c >= '0' && c <= '9', "invalid decimal: " + label);
    value *= 10;
    value += c-'0';
  }
  require(value.convert_to<std::string>() == text,
          "noncanonical decimal: " + label);
  return value;
}

static void require_digest(const std::string& digest,
                           const std::string& label) {
  require(digest.size() == 64, "digest length: " + label);
  for (unsigned char c : digest)
    require((c >= '0' && c <= '9') || (c >= 'a' && c <= 'f'),
            "digest syntax: " + label);
}

static std::vector<int> parse_selection_bytes(
    const std::string& bytes, const std::string& expected_digest,
    const Grammar& full) {
  require_digest(expected_digest,"selection");
  require(sha256_bytes(bytes) == expected_digest,
          "selection byte authentication");
  const auto lines = split_lines(bytes);
  require(lines.size() == 33, "selection exact line count");
  require(lines.front() == selection_header(), "selection exact header");
  std::vector<int> ids;
  std::set<int> unique;
  for (std::size_t row = 1; row < lines.size(); ++row) {
    const auto fields = split_tabs(lines[row]);
    require(fields.size() == 11, "selection exact field count");
    const int id = static_cast<int>(parse_integer(
        fields[0],0,static_cast<long long>(full.all.size())-1,"selection id"));
    require(unique.insert(id).second, "selection duplicate id");
    const auto& p = full.all[id];
    require(p.global_id == id, "selection global id mapping");
    require(fields[1] == KIND_NAMES[static_cast<int>(p.kind)],
            "selection kind mismatch");
    require(fields[2] == "1" && p.operational,
            "selection operational mismatch");
    require(fields[3] == "0" && !p.oracle, "selection oracle mismatch");
    require(fields[4] == fp_string(p.fingerprint),
            "selection fingerprint mismatch");
    const long double min_score = parse_finite(fields[5],"selection min_score");
    const long double min_miller = parse_finite(fields[6],"selection min_miller");
    const long double collision_mean =
        parse_finite(fields[7],"selection collision mean");
    const long double collision_median =
        parse_finite(fields[8],"selection collision median");
    const long double min_dphi = parse_finite(fields[9],"selection min_dphi");
    require(min_score >= 0 && min_score <= 1+1e-8L &&
            min_miller >= 0 && min_miller <= 1+1e-8L &&
            collision_mean >= 0 && collision_mean <= 1+1e-8L &&
            collision_median >= 0 && collision_median <= 1+1e-8L &&
            min_dphi >= 0, "selection numeric range");
    require(fields[10] == p.name, "selection syntax mismatch");
    ids.push_back(id);
  }
  require(ids.size() == 32, "selection 32 unique rows");
  return ids;
}

static std::set<std::string> parse_discovery_corpus_bytes(
    const std::string& bytes, const std::string& expected_digest, bool tiny) {
  require_digest(expected_digest,"discovery corpus");
  require(sha256_bytes(bytes) == expected_digest,
          "discovery corpus byte authentication");
  const auto lines = split_lines(bytes);
  const std::size_t expected_rows = tiny ? 18 : 8960;
  require(lines.size() == expected_rows+1,
          "discovery corpus exact line count");
  require(lines.front() == "factor_bits\tcohort\tindex\tN",
          "discovery corpus exact header");
  std::set<std::string> moduli;
  std::size_t line = 1;
  for (int bi = 0; bi < 3; ++bi) {
    const int bits = DISCOVERY_BITS[bi];
    int counts[3] = {tiny ? 2 : 2048,
                     tiny ? 2 : (bits == 16 ? 256 : 512),
                     tiny ? 2 : 512};
    for (int cohort = 0; cohort < 3; ++cohort)
      for (int index = 0; index < counts[cohort]; ++index,++line) {
        require(line < lines.size(), "discovery corpus truncated");
        const auto fields = split_tabs(lines[line]);
        require(fields.size() == 4, "discovery corpus exact field count");
        require(parse_integer(fields[0],bits,bits,"discovery factor bits") == bits,
                "discovery factor bit order");
        require(fields[1] == COHORT_NAMES[cohort],
                "discovery cohort order");
        require(parse_integer(fields[2],index,index,"discovery row index") == index,
                "discovery index order");
        const cpp_int N = parse_decimal(fields[3],"discovery modulus");
        require(N > 1 && (N & 1) != 0, "discovery modulus odd positive");
        const int nbits = bit_length(N);
        require(nbits == 2*bits-1 || nbits == 2*bits,
                "discovery modulus bit length");
        require(moduli.insert(fields[3]).second,
                "discovery duplicate modulus");
      }
  }
  require(line == lines.size(), "discovery corpus extra row");
  return moduli;
}

static Grammar restrict_grammar(const Grammar& full,
                                const std::vector<int>& ids) {
  Grammar out;
  std::map<int,int> seq_map, word_map, fact_map;
  auto add_sequence = [&](int old) {
    auto it = seq_map.find(old);
    if (it != seq_map.end()) return it->second;
    const int current = static_cast<int>(out.seq.size());
    out.seq.push_back(full.seq[old]);
    seq_map.emplace(old,current);
    return current;
  };
  for (int id : ids) {
    const auto& ref = full.all[id];
    if (ref.kind == Kind::SEQUENCE) add_sequence(ref.index);
    if (ref.kind == Kind::WORD) {
      WordProgram word = full.word[ref.index];
      if (word.a >= 0) word.a = add_sequence(word.a);
      if (word.b >= 0) word.b = add_sequence(word.b);
      const int current = static_cast<int>(out.word.size());
      out.word.push_back(std::move(word));
      word_map.emplace(ref.index,current);
    }
    if (ref.kind == Kind::FACTORED) {
      const int current = static_cast<int>(out.fact.size());
      out.fact.push_back(full.fact[ref.index]);
      fact_map.emplace(ref.index,current);
    }
  }
  for (int id : ids) {
    ProgramRef ref = full.all[id];
    if (ref.kind == Kind::SEQUENCE) ref.index = seq_map.at(ref.index);
    if (ref.kind == Kind::WORD) ref.index = word_map.at(ref.index);
    if (ref.kind == Kind::FACTORED) ref.index = fact_map.at(ref.index);
    require(ref.operational && !ref.oracle, "restricted grammar operational");
    out.all.push_back(std::move(ref));
  }
  require(out.all.size() == 32, "restricted grammar 32 programs");
  return out;
}

static std::set<std::string> directory_names(const std::string& path) {
  struct stat root{};
  require(stat(path.c_str(),&root) == 0 && S_ISDIR(root.st_mode),
          "output path must be an existing directory");
  DIR* raw = opendir(path.c_str());
  require(raw != nullptr, "open output directory names");
  std::set<std::string> names;
  while (dirent* ent = readdir(raw)) {
    const std::string name = ent->d_name;
    if (name == "." || name == "..") continue;
    struct stat st{};
    require(stat(join_path(path,name).c_str(),&st) == 0,
            "stat output entry");
    require(S_ISREG(st.st_mode), "nonregular output entry");
    require(names.insert(name).second, "duplicate output entry");
  }
  closedir(raw);
  return names;
}

static void require_output_names(const std::string& path,
                                 const std::vector<std::string>& expected) {
  const std::set<std::string> want(expected.begin(),expected.end());
  require(want.size() == expected.size(), "duplicate expected output name");
  require(directory_names(path) == want, "exact output set mismatch");
}

struct TextFileStats {
  u64 bytes=0, lines=0;
  std::string digest;
};

static TextFileStats inspect_text_file(const std::string& path) {
  std::ifstream f(path,std::ios::binary);
  require(bool(f),"open manifest input: " + path);
  Sha256 hash;
  std::array<unsigned char,65536> buffer{};
  bool have_last = false;
  unsigned char last = 0;
  TextFileStats stats;
  for (;;) {
    f.read(reinterpret_cast<char*>(buffer.data()),buffer.size());
    const std::streamsize got = f.gcount();
    if (got > 0) {
      hash.update(buffer.data(),static_cast<std::size_t>(got));
      stats.bytes += static_cast<u64>(got);
      for (std::streamsize i = 0; i < got; ++i)
        if (buffer[static_cast<std::size_t>(i)] == '\n') ++stats.lines;
      last = buffer[static_cast<std::size_t>(got-1)];
      have_last = true;
    }
    if (f.eof()) break;
    require(bool(f),"read manifest input: " + path);
  }
  require(have_last && last == '\n',"manifest input final newline: " + path);
  stats.digest = hash.final_hex();
  return stats;
}

static u64 write_manifest(const std::string& path,
                          const std::string& directory,
                          const std::vector<std::string>& names,
                          OutputBudget& budget) {
  CheckedFile f(path,budget);
  f.line("filename\tbytes\tlines\tsha256");
  for (const std::string& name : names) {
    const TextFileStats stats = inspect_text_file(join_path(directory,name));
    f.line(name + "\t" + std::to_string(stats.bytes) + "\t" +
           std::to_string(stats.lines) + "\t" + stats.digest);
  }
  const u64 lines = f.lines();
  f.close();
  return lines;
}

static std::vector<std::string> discovery_files(bool manifest) {
  std::vector<std::string> names = {
    "F260-D03.grammar.tsv",
    "F260-D03.discovery.corpus.tsv",
    "F260-D03.discovery.corpus.sha256",
    "F260-D03.discovery.aggregates.tsv",
    "F260-D03.discovery.certificates.tsv",
    "F260-D03.discovery.collisions.tsv",
    "F260-D03.discovery.oracle.tsv",
    "F260-D03.selection.tsv",
    "F260-D03.selection.sha256"
  };
  if (manifest) names.push_back("F260-D03.discovery.manifest.tsv");
  return names;
}

static std::vector<std::string> heldout_files(bool manifest) {
  std::vector<std::string> names = {
    "F260-D03.heldout.corpus.tsv",
    "F260-D03.heldout.aggregates.tsv",
    "F260-D03.heldout.certificates.tsv",
    "F260-D03.heldout.collisions.tsv",
    "F260-D03.heldout.lead_gate.tsv"
  };
  if (manifest) names.push_back("F260-D03.heldout.manifest.tsv");
  return names;
}

static u64 write_lead_gate(const std::string& path, const Grammar& g,
                           const std::vector<Aggregate>& a,
                           OutputBudget& budget) {
  require(g.all.size() == 32 && a.size() == 32, "lead gate 32 programs");
  std::ostringstream header;
  header << "id\tsyntax\tkind";
  for (int bits : HELDOUT_BITS) for (int cohort : {1,2})
    header << "\tmean_score_" << bits << '_' << COHORT_NAMES[cohort];
  for (int cohort : {1,2}) for (int bits : {40,60})
    header << "\tscore_at_upper_median_loss_" << bits << '_'
           << COHORT_NAMES[cohort]
           << "\tloss_" << bits << '_' << COHORT_NAMES[cohort];
  for (int cohort : {1,2})
    header << "\tloss_growth_40_60_" << COHORT_NAMES[cohort];
  for (int bits : {56,60}) for (int cohort : {1,2})
    header << "\texpected_mass_" << bits << '_' << COHORT_NAMES[cohort];
  for (int bits : HELDOUT_BITS) for (int cohort = 0; cohort < 3; ++cohort)
    header << "\tcollision_median_" << bits << '_' << COHORT_NAMES[cohort];
  header << "\tpositive_all\tloss_growth_all\tmass_all\toperational"
            "\tstrong_lead\tcollision_anomaly";

  CheckedFile f(path,budget);
  f.line(header.str());
  for (std::size_t id = 0; id < g.all.size(); ++id) {
    const auto& p = g.all[id];
    std::ostringstream line;
    line << std::setprecision(18) << p.global_id << '\t' << p.name << '\t'
         << KIND_NAMES[static_cast<int>(p.kind)];
    bool positive = true;
    for (int bits : HELDOUT_BITS) for (int cohort : {1,2}) {
      const Cell& c = a[id].cell[bit_slot(bits)][cohort];
      require(c.count > 0, "lead positive cell count");
      const long double mean = c.score/c.count;
      line << '\t' << mean;
      positive = positive && mean > 0;
    }
    std::array<std::array<long double,2>,2> losses{};
    bool loss_pass = true;
    int ci = 0;
    for (int cohort : {1,2}) {
      int bi = 0;
      for (int bits : {40,60}) {
        const Cell& c = a[id].cell[bit_slot(bits)][cohort];
        const long double loss = upper_median_loss(c.score_values);
        const long double median = std::isfinite(loss) ? std::exp2(-loss) : 0;
        losses[ci][bi++] = loss;
        line << '\t' << median << '\t' << number(loss);
      }
      ++ci;
    }
    for (int k = 0; k < 2; ++k) {
      const long double growth = losses[k][1]-losses[k][0];
      line << '\t' << number(growth);
      loss_pass = loss_pass && std::isfinite(growth) && growth < 15;
    }
    bool mass_pass = true;
    for (int bits : {56,60}) for (int cohort : {1,2}) {
      const Cell& c = a[id].cell[bit_slot(bits)][cohort];
      line << '\t' << c.expected_event;
      mass_pass = mass_pass && c.expected_event >= 16;
    }
    bool collision_anomaly = true;
    for (int bits : HELDOUT_BITS) for (int cohort = 0; cohort < 3; ++cohort) {
      const long double median = upper_median(
          a[id].cell[bit_slot(bits)][cohort].collision_values);
      line << '\t' << median;
      collision_anomaly = collision_anomaly && median >= 1.0L/64;
    }
    const bool operational = p.operational && !p.oracle;
    const bool lead = positive && loss_pass && mass_pass && operational;
    line << '\t' << positive << '\t' << loss_pass << '\t' << mass_pass
         << '\t' << operational << '\t' << lead << '\t' << collision_anomaly;
    f.line(line.str());
  }
  const u64 lines = f.lines();
  f.close();
  return lines;
}

static void run_discovery(const std::string& directory, int workers,
                          bool tiny) {
  require(workers >= 1 && workers <= MAX_WORKERS, "discovery worker boundary");
  require_output_names(directory,{});
  OutputBudget budget(0);
  const Grammar grammar = build_grammar();
  write_grammar(join_path(directory,"F260-D03.grammar.tsv"),grammar,budget);
  const std::vector<CorpusRow> corpus = make_corpus(true,tiny);
  require(corpus.size() == (tiny ? 18U : 8960U), "discovery corpus count");
  const std::string corpus_path =
      join_path(directory,"F260-D03.discovery.corpus.tsv");
  write_corpus(corpus_path,corpus,budget);
  const std::string corpus_digest = sha256_file(corpus_path);
  write_digest(join_path(directory,"F260-D03.discovery.corpus.sha256"),
               corpus_digest,"F260-D03.discovery.corpus.tsv",budget);

  const CorpusEvaluation result =
      evaluate_corpus(corpus,grammar,workers,true,false);
  write_aggregates(join_path(directory,"F260-D03.discovery.aggregates.tsv"),
                   "discovery",grammar,result.aggregate,DISCOVERY_BITS,3,budget);
  write_certificates(join_path(directory,"F260-D03.discovery.certificates.tsv"),
                     "discovery",result.certificates,budget);
  write_collisions(join_path(directory,"F260-D03.discovery.collisions.tsv"),
                   "discovery",grammar,result.aggregate,DISCOVERY_BITS,3,budget);
  write_oracles(join_path(directory,"F260-D03.discovery.oracle.tsv"),
                grammar,result.aggregate,budget);
  const std::vector<int> selected =
      select_programs(grammar,result.aggregate);
  const std::string selection_path =
      join_path(directory,"F260-D03.selection.tsv");
  write_selection(selection_path,grammar,result.aggregate,selected,budget);
  const std::string selection_digest = sha256_file(selection_path);
  write_digest(join_path(directory,"F260-D03.selection.sha256"),
               selection_digest,"F260-D03.selection.tsv",budget);

  const auto records = discovery_files(false);
  require_output_names(directory,records);
  write_manifest(join_path(directory,"F260-D03.discovery.manifest.tsv"),
                 directory,records,budget);
  require_output_names(directory,discovery_files(true));
  require(directory_regular_bytes(directory) == budget.bytes,
          "discovery output byte accounting");
  std::cout << "DISCOVERY_OK rows=" << corpus.size()
            << " programs=" << grammar.all.size()
            << " selection_sha256=" << selection_digest
            << " corpus_sha256=" << corpus_digest << '\n';
}

static void run_heldout(const std::string& directory,
                        const std::string& selection_path,
                        const std::string& expected_selection_digest,
                        const std::string& discovery_corpus_path,
                        const std::string& expected_corpus_digest,
                        int workers, bool tiny) {
  require(workers >= 1 && workers <= MAX_WORKERS, "heldout worker boundary");
  require(selection_path == join_path(directory,"F260-D03.selection.tsv"),
          "heldout selection path boundary");
  require(discovery_corpus_path ==
          join_path(directory,"F260-D03.discovery.corpus.tsv"),
          "heldout corpus path boundary");
  require_output_names(directory,discovery_files(true));

  const Grammar full = build_grammar();
  const std::string selection_bytes = read_binary_file(selection_path);
  const std::vector<int> selected = parse_selection_bytes(
      selection_bytes,expected_selection_digest,full);
  const std::string corpus_bytes = read_binary_file(discovery_corpus_path);
  const std::set<std::string> forbidden = parse_discovery_corpus_bytes(
      corpus_bytes,expected_corpus_digest,tiny);
  const Grammar grammar = restrict_grammar(full,selected);

  const std::vector<CorpusRow> corpus = make_corpus(false,tiny,forbidden);
  require(corpus.size() == (tiny ? 24U : 24576U), "heldout corpus count");
  OutputBudget budget(directory_regular_bytes(directory));
  write_corpus(join_path(directory,"F260-D03.heldout.corpus.tsv"),corpus,budget);
  const CorpusEvaluation result =
      evaluate_corpus(corpus,grammar,workers,true,true);
  write_aggregates(join_path(directory,"F260-D03.heldout.aggregates.tsv"),
                   "heldout",grammar,result.aggregate,HELDOUT_BITS,4,budget);
  write_certificates(join_path(directory,"F260-D03.heldout.certificates.tsv"),
                     "heldout",result.certificates,budget);
  write_collisions(join_path(directory,"F260-D03.heldout.collisions.tsv"),
                   "heldout",grammar,result.aggregate,HELDOUT_BITS,4,budget);
  write_lead_gate(join_path(directory,"F260-D03.heldout.lead_gate.tsv"),
                  grammar,result.aggregate,budget);

  std::vector<std::string> before_manifest = discovery_files(true);
  const auto held_records = heldout_files(false);
  before_manifest.insert(before_manifest.end(),held_records.begin(),held_records.end());
  require_output_names(directory,before_manifest);
  write_manifest(join_path(directory,"F260-D03.heldout.manifest.tsv"),
                 directory,held_records,budget);
  std::vector<std::string> complete = discovery_files(true);
  const auto held_complete = heldout_files(true);
  complete.insert(complete.end(),held_complete.begin(),held_complete.end());
  require_output_names(directory,complete);
  require(directory_regular_bytes(directory) == budget.bytes,
          "heldout output byte accounting");
  std::cout << "HELDOUT_OK rows=" << corpus.size()
            << " programs=" << grammar.all.size() << '\n';
}

static void self_test() {
  require(sha256_bytes("abc") ==
          "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad",
          "SHA-256 vector");
  require(is_prime(2) && is_prime(2305843009213693951ULL) &&
          !is_prime(341550071728321ULL), "deterministic primality vectors");
  const auto factors = factor_u64(8051,MASTER_SEED);
  require(factors == std::map<u64,int>({{83,1},{97,1}}),
          "bounded factorization vector");
  require(isqrt_cpp(cpp_int(15241578750190521ULL)) == 123456789,
          "integer square root vector");
  require(integer_J(cpp_int(16),1) == 2, "integer J exact vector");
  Ratio ratio = binomial_ratio(10,5,1,1);
  require(ratio.valid && ratio.p == 11 && ratio.q == 6 &&
          gcd_cpp(ratio.p,ratio.q) == 1,
          "short-product hypergeometric vector");

  const Grammar grammar = build_grammar();
  require(grammar.fact.size() == 9, "nine canonical factored programs");
  std::set<std::array<u64,3>> fact_fingerprints;
  for (const auto& p : grammar.fact)
    require(fact_fingerprints.insert(p.fingerprint).second,
            "factored semantic fingerprint uniqueness");
  const PublicData sample = build_public_data(cpp_int(1009)*2003);
  require(sample.base.size() == 22, "twenty-two public sequence bases");
  for (const auto& p : grammar.seq)
    if (sample.base[p.base].hyper)
      require(p.transform == Transform::ID, "hyper identity boundary");
  for (const auto& p : grammar.word) if (p.a >= 0 && p.b >= 0)
    require(grammar.seq[p.a].name < grammar.seq[p.b].name,
            "commutative word children use normalized syntax order");

  Cell extrema;
  Metrics first_residual, second_residual;
  first_residual.residual_log_p = 3;
  first_residual.residual_log_q = 7;
  second_residual.residual_log_p = 1;
  second_residual.residual_log_q = 11;
  add_metrics(extrema,first_residual,false,false,false,true,false);
  add_metrics(extrema,second_residual,false,false,false,true,false);
  require(extrema.have_residual_extrema &&
          extrema.residual_log_p_min == 1 &&
          extrema.residual_log_p_max == 3 &&
          extrema.residual_log_q_min == 7 &&
          extrema.residual_log_q_max == 11,
          "word residual extrema aggregation");

  std::vector<PrimaryLaw> laws;
  for (auto tuple : {std::make_tuple(3ULL,2,1),
                     std::make_tuple(5ULL,1,2)}) {
    PrimaryLaw law;
    law.ell = std::get<0>(tuple);
    law.fp = std::get<1>(tuple);
    law.fq = std::get<2>(tuple);
    law.equal = 0;
    const int top = std::min(law.fp,law.fq);
    law.equal_t.resize(top+1);
    for (int t = 0; t <= top; ++t) {
      law.equal_t[t] = order_probability(law.ell,law.fp,t)*
                       order_probability(law.ell,law.fq,t);
      law.equal += law.equal_t[t];
    }
    laws.push_back(std::move(law));
  }
  const long double both = 0.125L;
  const long double equal_product = laws[0].equal*laws[1].equal;
  const std::map<u64,int> state{{3,0},{5,1}};
  const StateScore linear = score_state(laws,state,0.25L,both,equal_product);
  long double brute_gain = 0;
  for (int a = 0; a < static_cast<int>(laws[0].equal_t.size()); ++a)
    for (int b = 0; b < static_cast<int>(laws[1].equal_t.size()); ++b) {
      const long double gain = a*std::log2(3.0L) +
          std::max(0,b-1)*std::log2(5.0L);
      brute_gain += both*laws[0].equal_t[a]*laws[1].equal_t[b]*gain;
    }
  require(std::abs(linear.expected_log_gain-brute_gain) < 1e-15L,
          "linear expected-gain identity");
  CorpusRow factored_row{4,0,0,13,19,cpp_int(13)*19};
  const LocalLabels factored_labels = make_labels(factored_row);
  const FactScore factored = score_factored({{2,2},{3,2}},factored_labels,
                                             factored_row.N,8);
  require(std::abs(factored.factor_probability-103.0L/108) < 1e-15L &&
          std::abs(factored.m1.factor_or_growth-215.0L/216) < 1e-15L &&
          std::abs(factored.m2.factor_or_growth-107.0L/108) < 1e-15L,
          "exact factored probability vector");
  const long double expected_m1 = 5.0L/108*
      (0.5L+0.8L*std::log2(3.0L));
  require(std::abs(factored.m1.expected_log_gain-expected_m1) < 1e-15L,
          "exact factored gain vector");
  const DyadicLaw dyadic = score_dyadic(laws,state,1,100,both,equal_product);
  long double distribution_mass = 0, distribution_expectation = 0;
  for (int d = 0; d <= MAX_DPHI; ++d) {
    distribution_mass += dyadic.distribution[d];
    distribution_expectation += d*dyadic.distribution[d];
  }
  require(std::abs(distribution_mass-both*equal_product) < 1e-15L &&
          std::abs(distribution_expectation-dyadic.expected) < 1e-15L,
          "exact dyadic distribution identity");

  const auto collision_values = canonical_sample({1,1,4,7});
  const CollisionSide collision = collision_side(collision_values,{{3,1}});
  require(collision_values.size() == 3 &&
          std::abs(collision.best_kappa-1) < 1e-15L &&
          std::abs(collision.joint-1) < 1e-15L,
          "distinct-value ordered-pair semantics");
  LocalLabels p205_labels;
  p205_labels.sp = 3;
  p205_labels.sq = 5;
  p205_labels.vp2 = 1;
  p205_labels.vq2 = 2;
  const MillerScore p205 = miller_score(1,1,10,p205_labels);
  require(std::abs(p205.probability-9.0L/20) < 1e-15L &&
          std::abs(p205.H-1.0L/3) < 1e-15L,
          "exact P205 vector");

  Grammar ranked;
  ranked.all.resize(40);
  std::vector<Aggregate> synthetic(40);
  for (int id = 0; id < 40; ++id) {
    std::ostringstream name;
    name << 'p' << std::setw(2) << std::setfill('0') << id;
    ranked.all[id] = {Kind::SEQUENCE,0,0,name.str(),true,false,{},id};
    for (int slot = 0; slot < 3; ++slot) for (int cohort = 0; cohort < 3; ++cohort) {
      Cell& c = synthetic[id].cell[slot][cohort];
      c.count = 1;
      c.score = 40-id;
      c.miller = 40-((id+32)%40);
      c.dyadic_expected = 40-((id+28)%40);
      c.collision_values.push_back(40-((id+36)%40));
    }
  }
  const std::vector<int> literal = select_programs(ranked,synthetic);
  require(literal.size() == 32, "literal selection length");
  for (int id = 0; id < 32; ++id)
    require(literal[id] == id, "literal top-eight union then order-one fill");

  std::vector<int> valid_ids;
  for (int id = 0; id < static_cast<int>(grammar.all.size()) &&
                       valid_ids.size() < 32; ++id)
    if (grammar.all[id].operational) valid_ids.push_back(id);
  require(valid_ids.size() == 32, "self-test selection candidates");
  std::ostringstream selection;
  selection << selection_header() << '\n';
  for (int id : valid_ids) {
    const auto& p = grammar.all[id];
    selection << p.global_id << '\t' << KIND_NAMES[static_cast<int>(p.kind)]
              << "\t1\t0\t" << fp_string(p.fingerprint)
              << "\t0\t0\t0\t0\t0\t" << p.name << '\n';
  }
  const std::string selection_bytes = selection.str();
  const std::string digest = sha256_bytes(selection_bytes);
  require(parse_selection_bytes(selection_bytes,digest,grammar) == valid_ids,
          "selection same-byte parse");
  std::string altered = selection_bytes;
  altered[altered.size()/2] ^= 1;
  bool rejected = false;
  try { (void)parse_selection_bytes(altered,digest,grammar); }
  catch (const std::runtime_error&) { rejected = true; }
  require(rejected, "selection alteration rejected");

  std::ostringstream public_corpus;
  public_corpus << "factor_bits\tcohort\tindex\tN\n";
  int serial = 0;
  for (int bits : DISCOVERY_BITS) for (int cohort = 0; cohort < 3; ++cohort)
    for (int index = 0; index < 2; ++index) {
      const cpp_int modulus = (cpp_int(1) << (2*bits-2)) + 2*serial++ + 1;
      public_corpus << bits << '\t' << COHORT_NAMES[cohort] << '\t' << index
                    << '\t' << modulus << '\n';
    }
  const std::string corpus_bytes = public_corpus.str();
  const std::string corpus_digest = sha256_bytes(corpus_bytes);
  require(parse_discovery_corpus_bytes(corpus_bytes,corpus_digest,true).size()==18,
          "public corpus same-byte parse");
  altered = corpus_bytes;
  altered[altered.size()/2] ^= 1;
  rejected = false;
  try { (void)parse_discovery_corpus_bytes(altered,corpus_digest,true); }
  catch (const std::runtime_error&) { rejected = true; }
  require(rejected, "public corpus alteration rejected");

  require(3*(2048+512+512)-256 == 8960,
          "discovery frozen count identity");
  require(4*(4096+1024+1024) == 24576,
          "heldout frozen count identity");
  require(is_prime(5) && is_prime(7) && is_prime((5-1)/2) &&
          is_prime((7-1)/2) && 5 < 7 && 7 < 2*5,
          "fixed safe-safe acceptance vector");
  require(is_prime(11) && next_prime(11) == 13 && bit_length(11) == 4 &&
          bit_length(13) == 4 && 11 < 13 && 13 < 2*11,
          "fixed consecutive acceptance vector");
  std::cout << "SELF_TEST_OK programs=" << grammar.all.size()
            << " sequence=" << grammar.seq.size()
            << " word=" << grammar.word.size()
            << " factored=" << grammar.fact.size() << '\n';
}

static CorpusRow fixed_validation_row(int bits, u64 seed) {
  Rng rng(seed);
  u64 p = random_prime(bits,rng), q = random_prime(bits,rng);
  for (int retry = 0; p == q && retry < 1024; ++retry)
    q = random_prime(bits,rng);
  require(p != q, "validation distinct primes");
  if (p > q) std::swap(p,q);
  require(bit_length(p) == bits && bit_length(q) == bits && p < q && q < 2*p,
          "fixed validation row boundary");
  return {bits,0,0,p,q,cpp_int(p)*q};
}

static void benchmark() {
  const Grammar full = build_grammar();
  const CorpusRow discovery = fixed_validation_row(32,MASTER_SEED^0xD15C0ULL);
  const auto discovery_start = std::chrono::steady_clock::now();
  const RowEvaluation discovery_result = evaluate_row(discovery,full);
  const long double discovery_seconds = std::chrono::duration<long double>(
      std::chrono::steady_clock::now()-discovery_start).count();
  require(discovery_result.metrics.size() == full.all.size(),
          "benchmark full discovery envelope");

  std::vector<int> envelope;
  for (int kind : {2,0,1}) for (int id = 0; id < static_cast<int>(full.all.size()); ++id)
    if (full.all[id].operational && static_cast<int>(full.all[id].kind) == kind &&
        envelope.size() < 32) envelope.push_back(id);
  require(envelope.size() == 32, "benchmark 32-program envelope");
  const Grammar restricted = restrict_grammar(full,envelope);
  const CorpusRow heldout = fixed_validation_row(60,MASTER_SEED^0x4E1D0ULL);
  const auto heldout_start = std::chrono::steady_clock::now();
  const RowEvaluation heldout_result = evaluate_row(heldout,restricted);
  const long double heldout_seconds = std::chrono::duration<long double>(
      std::chrono::steady_clock::now()-heldout_start).count();
  require(heldout_result.metrics.size() == 32,
          "benchmark heldout dependency envelope");

  rusage usage{};
  require(getrusage(RUSAGE_SELF,&usage) == 0, "benchmark getrusage");
  const long double projected_seconds =
      4*(8960*discovery_seconds+24576*heldout_seconds)/MAX_WORKERS;
  const u64 projected_peak_bytes = static_cast<u64>(usage.ru_maxrss)*1024ULL*8 +
                                   536870912ULL;
  const u64 projected_output_bytes = 536870912ULL;
  std::cout << std::setprecision(18)
            << "BENCHMARK_OK discovery_seconds=" << discovery_seconds
            << " heldout_seconds=" << heldout_seconds
            << " projected_seconds=" << projected_seconds
            << " projected_peak_bytes=" << projected_peak_bytes
            << " projected_output_bytes=" << projected_output_bytes
            << " discovery_N=" << discovery.N
            << " heldout_N=" << heldout.N << '\n';
}

static int parse_workers(const std::string& text) {
  return static_cast<int>(parse_integer(text,1,MAX_WORKERS,"workers"));
}

static bool parse_scale(const std::string& text) {
  require(text == "full" || text == "tiny", "scale must be full or tiny");
  return text == "tiny";
}

int main(int argc, char** argv) {
  const auto start = std::chrono::steady_clock::now();
  try {
    require(argc >= 2, "missing mode");
    const std::string mode = argv[1];
    if (mode == "--self-test") {
      require(argc == 2, "self-test argument count");
      self_test();
    } else if (mode == "--benchmark") {
      require(argc == 2, "benchmark argument count");
      benchmark();
    } else if (mode == "--discovery") {
      require(argc == 5, "discovery argument count");
      run_discovery(argv[2],parse_workers(argv[3]),parse_scale(argv[4]));
    } else if (mode == "--heldout") {
      require(argc == 9, "heldout argument count");
      run_heldout(argv[2],argv[3],argv[4],argv[5],argv[6],
                  parse_workers(argv[7]),parse_scale(argv[8]));
    } else {
      fail("unknown mode");
    }
    print_process_resources("F260_D03",start);
    return 0;
  } catch (const std::exception& e) {
    std::cerr << "F260_D03_ERROR " << e.what() << '\n';
    return 1;
  }
}
