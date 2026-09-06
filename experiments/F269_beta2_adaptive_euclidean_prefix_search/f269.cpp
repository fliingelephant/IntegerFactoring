#include <algorithm>
#include <array>
#include <atomic>
#include <chrono>
#include <cstdint>
#include <cstdlib>
#include <cstring>
#include <fstream>
#include <filesystem>
#include <functional>
#include <iomanip>
#include <iostream>
#include <limits>
#include <map>
#include <memory>
#include <mutex>
#include <numeric>
#include <optional>
#include <queue>
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
#include <sys/stat.h>
#include <unistd.h>

#include <boost/multiprecision/cpp_int.hpp>

using boost::multiprecision::cpp_int;
using u64 = std::uint64_t;
using u128 = __uint128_t;

namespace f269 {

namespace fs = std::filesystem;

constexpr u64 GRAMMAR_SEED = 0xF269ADAE0C1D5EEDULL;
constexpr u64 DIRECT_SEED = 0xF269D1AEC7C0FFEEULL;
constexpr u64 CORPUS_SEED = 0xF269C0A07E5EED01ULL;
constexpr std::size_t ROOT_CAP = 444;
constexpr std::size_t UNARY_ATTEMPTS = 1024;
constexpr std::size_t BINARY_ATTEMPTS = 3072;
constexpr std::size_t ADAPTIVE_ATTEMPTS = 1024;
constexpr std::size_t FINAL_ATTEMPTS = 5564;
constexpr std::size_t DIRECT_BANK = 1024;
constexpr std::size_t SELECTOR_COUNT = 192;
constexpr std::size_t DIRECT_HELDOUT = 64;
constexpr std::uint64_t REGISTERED_OUTPUT_BOUND = 277979136ULL;
constexpr std::uint64_t ORDINARY_WRITER_CAP = 535822336ULL;
constexpr std::uint64_t FAILURE_RESERVE = 1048576ULL;
constexpr std::uint64_t AGGREGATE_CAP = 536870912ULL;
constexpr std::uint64_t RLIMIT_AS_BYTES = 4294967296ULL;
constexpr std::uint64_t RLIMIT_FSIZE_BYTES = 536870912ULL;
constexpr std::uint64_t MEMORY_MAX_BYTES = 3758096384ULL;
constexpr const char* BASELINE_SHA =
    "ee5af083ba43236b92a4c52996e4134f7f40f10cb7db9997212c821482f097b4";

const char BASELINE_BYTES[] = R"F269(baseline_id	baseline_key	class	feature_id	orientation_id	prediction_a
0	CONST_0	BIT	CONST_0	NA	0
1	CONST_1	BIT	CONST_1	NA	1
2	KAPPA	BIT	KAPPA	NA	kappa
3	NOT_KAPPA	BIT	KAPPA	NA	1_xor_kappa
4	DELTA	BIT	DELTA	NA	delta
5	NOT_DELTA	BIT	DELTA	NA	1_xor_delta
6	KAPPA_XOR_DELTA	BIT	KAPPA_XOR_DELTA	NA	kappa_xor_delta
7	NOT_KAPPA_XOR_DELTA	BIT	KAPPA_XOR_DELTA	NA	1_xor_kappa_xor_delta
8	BIT_N_T	BIT	BIT_N_T	NA	bit_N(t)
9	NOT_BIT_N_T	BIT	BIT_N_T	NA	1_xor_bit_N(t)
10	BIT_N_T1	BIT	BIT_N_T1	NA	bit_N(t+1)
11	NOT_BIT_N_T1	BIT	BIT_N_T1	NA	1_xor_bit_N(t+1)
12	BIT_U_TM1	BIT	BIT_U_TM1	NA	bit_u(t-1)
13	NOT_BIT_U_TM1	BIT	BIT_U_TM1	NA	1_xor_bit_u(t-1)
14	PARITY_T	BIT	PARITY_T	NA	t_mod_2
15	NOT_PARITY_T	BIT	PARITY_T	NA	1_xor_t_mod_2
16	F210_FK_ARGMIN	F210	FK	0	ARGMIN
17	F210_FK_ARGMAX	F210	FK	1	ARGMAX
18	F210_FJ_ARGMIN	F210	FJ	0	ARGMIN
19	F210_FJ_ARGMAX	F210	FJ	1	ARGMAX
20	F210_BITLEN_FK_ARGMIN	F210	BITLEN_FK	0	ARGMIN
21	F210_BITLEN_FK_ARGMAX	F210	BITLEN_FK	1	ARGMAX
22	F210_BITLEN_FJ_ARGMIN	F210	BITLEN_FJ	0	ARGMIN
23	F210_BITLEN_FJ_ARGMAX	F210	BITLEN_FJ	1	ARGMAX
24	F210_SUM_FK_FJ_ARGMIN	F210	SUM_FK_FJ	0	ARGMIN
25	F210_SUM_FK_FJ_ARGMAX	F210	SUM_FK_FJ	1	ARGMAX
26	F210_MIN_FK_FJ_ARGMIN	F210	MIN_FK_FJ	0	ARGMIN
27	F210_MIN_FK_FJ_ARGMAX	F210	MIN_FK_FJ	1	ARGMAX
28	F210_MAX_FK_FJ_ARGMIN	F210	MAX_FK_FJ	0	ARGMIN
29	F210_MAX_FK_FJ_ARGMAX	F210	MAX_FK_FJ	1	ARGMAX
30	F210_PRODUCT_FK_FJ_ARGMIN	F210	PRODUCT_FK_FJ	0	ARGMIN
31	F210_PRODUCT_FK_FJ_ARGMAX	F210	PRODUCT_FK_FJ	1	ARGMAX
32	F210_GCD_FK_FJ_ARGMIN	F210	GCD_FK_FJ	0	ARGMIN
33	F210_GCD_FK_FJ_ARGMAX	F210	GCD_FK_FJ	1	ARGMAX
34	F210_DIV_LARGE_SMALL_ARGMIN	F210	DIV_LARGE_SMALL	0	ARGMIN
35	F210_DIV_LARGE_SMALL_ARGMAX	F210	DIV_LARGE_SMALL	1	ARGMAX
36	F210_REM_LARGE_SMALL_ARGMIN	F210	REM_LARGE_SMALL	0	ARGMIN
37	F210_REM_LARGE_SMALL_ARGMAX	F210	REM_LARGE_SMALL	1	ARGMAX
38	F210_ABSDIFF_FX_FY_ARGMIN	F210	ABSDIFF_FX_FY	0	ARGMIN
39	F210_ABSDIFF_FX_FY_ARGMAX	F210	ABSDIFF_FX_FY	1	ARGMAX
40	F210_SUM_FX_FY_ARGMIN	F210	SUM_FX_FY	0	ARGMIN
41	F210_SUM_FX_FY_ARGMAX	F210	SUM_FX_FY	1	ARGMAX
)F269";

[[noreturn]] void fail(const std::string& message) {
  throw std::runtime_error(message);
}

void require(bool condition, const std::string& message) {
  if (!condition) fail(message);
}

u64 splitmix64(u64 x) {
  u64 z = x + 0x9E3779B97F4A7C15ULL;
  z = (z ^ (z >> 30)) * 0xBF58476D1CE4E5B9ULL;
  z = (z ^ (z >> 27)) * 0x94D049BB133111EBULL;
  return z ^ (z >> 31);
}

u64 fnv1a64(const std::string& bytes) {
  u64 h = 14695981039346656037ULL;
  for (unsigned char b : bytes) h = (h ^ b) * 1099511628211ULL;
  return h;
}

class Sha256 {
 public:
  Sha256() { reset(); }
  void update(const unsigned char* data, std::size_t length) {
    total_ += length;
    while (length) {
      const std::size_t take = std::min<std::size_t>(length, 64 - used_);
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
    for (auto x : state_) out << std::setw(8) << x;
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

std::string sha256_bytes(const std::string& bytes) {
  Sha256 h;
  h.update(bytes);
  return h.final_hex();
}

std::string read_file(const std::string& path) {
  std::ifstream in(path, std::ios::binary);
  require(bool(in), "open input " + path);
  std::ostringstream out;
  out << in.rdbuf();
  require(in.good() || in.eof(), "read input " + path);
  return out.str();
}

std::string sha256_file(const std::string& path) {
  std::ifstream in(path, std::ios::binary);
  require(bool(in), "open hash input " + path);
  Sha256 h;
  std::array<unsigned char, 65536> buffer{};
  for (;;) {
    in.read(reinterpret_cast<char*>(buffer.data()), buffer.size());
    const auto got = in.gcount();
    if (got > 0) h.update(buffer.data(), static_cast<std::size_t>(got));
    if (in.eof()) break;
    require(bool(in), "hash read " + path);
  }
  return h.final_hex();
}

cpp_int abs_cpp(const cpp_int& x) { return x < 0 ? -x : x; }

std::size_t bitlength(const cpp_int& x) {
  cpp_int a = abs_cpp(x);
  if (a == 0) return 0;
  return static_cast<std::size_t>(boost::multiprecision::msb(a)) + 1;
}

cpp_int gcd_abs(cpp_int a, cpp_int b) {
  a = abs_cpp(a); b = abs_cpp(b);
  while (b != 0) { cpp_int r = a % b; a = b; b = r; }
  return a;
}

struct DivResult { cpp_int q; cpp_int r; };

DivResult floor_divmod(const cpp_int& x, const cpp_int& d) {
  require(d != 0, "zero denominator");
  const cpp_int D = abs_cpp(d);
  cpp_int q = x / D;
  cpp_int r = x % D;
  if (r < 0) { r += D; --q; }
  require(x == q * D + r && r >= 0 && r < D, "floor division identity");
  return {q, r};
}

cpp_int centered_rem(const cpp_int& x, const cpp_int& d) {
  const cpp_int D = abs_cpp(d);
  auto qr = floor_divmod(x, D);
  return 2 * qr.r > D ? qr.r - D : qr.r;
}

unsigned v2_nonzero(cpp_int x) {
  x = abs_cpp(x);
  require(x != 0, "v2 zero");
  unsigned v = 0;
  while ((x & 1) == 0) { x >>= 1; ++v; }
  return v;
}

cpp_int isqrt(const cpp_int& x) {
  require(x >= 0, "negative square root");
  if (x == 0) return 0;
  cpp_int r = cpp_int(1) << ((bitlength(x) + 1) / 2);
  for (;;) {
    cpp_int y = (r + x / r) >> 1;
    if (y >= r) break;
    r = y;
  }
  while ((r + 1) * (r + 1) <= x) ++r;
  while (r * r > x) --r;
  return r;
}

bool is_square(const cpp_int& x, cpp_int* root = nullptr) {
  if (x < 0) return false;
  cpp_int r = isqrt(x);
  if (root) *root = r;
  return r * r == x;
}

u64 mul_mod(u64 a, u64 b, u64 m) {
  return static_cast<u64>((static_cast<u128>(a) * b) % m);
}

u64 pow_mod(u64 a, u64 e, u64 m) {
  u64 out = 1 % m;
  while (e) {
    if (e & 1) out = mul_mod(out, a, m);
    a = mul_mod(a, a, m);
    e >>= 1;
  }
  return out;
}

bool is_prime64(u64 n) {
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
    a %= n;
    if (a == 0) continue;
    u64 x = pow_mod(a, d, n);
    if (x == 1 || x == n - 1) continue;
    bool composite = true;
    for (int r = 1; r < s; ++r) {
      x = mul_mod(x, x, n);
      if (x == n - 1) { composite = false; break; }
    }
    if (composite) return false;
  }
  return true;
}

u64 inverse_pow2(u64 a, u64 m) {
  require(m >= 2 && (m & (m - 1)) == 0 && (a & 1), "inverse_pow2 domain");
  std::int64_t t = 0, nt = 1;
  std::int64_t r = static_cast<std::int64_t>(m);
  std::int64_t nr = static_cast<std::int64_t>(a % m);
  while (nr) {
    const std::int64_t q = r / nr;
    const std::int64_t tt = t - q * nt; t = nt; nt = tt;
    const std::int64_t rr = r - q * nr; r = nr; nr = rr;
  }
  require(r == 1, "inverse_pow2 gcd");
  t %= static_cast<std::int64_t>(m);
  if (t < 0) t += static_cast<std::int64_t>(m);
  return static_cast<u64>(t);
}

std::string dec(const cpp_int& x) { return x.convert_to<std::string>(); }

std::string join_tsv(const std::vector<std::string>& fields) {
  std::ostringstream out;
  for (std::size_t i = 0; i < fields.size(); ++i) {
    if (i) out << '\t';
    out << fields[i];
  }
  out << '\n';
  return out.str();
}

void check_rlimits() {
  rlimit as{}, fs{};
  require(getrlimit(RLIMIT_AS, &as) == 0, "getrlimit AS");
  require(getrlimit(RLIMIT_FSIZE, &fs) == 0, "getrlimit FSIZE");
  require(as.rlim_cur == RLIMIT_AS_BYTES && as.rlim_max == RLIMIT_AS_BYTES,
          "RLIMIT_AS mismatch");
  require(fs.rlim_cur == RLIMIT_FSIZE_BYTES && fs.rlim_max == RLIMIT_FSIZE_BYTES,
          "RLIMIT_FSIZE mismatch");
}

struct Deadline {
  std::chrono::steady_clock::time_point absolute;
  void check(const std::string& where) const {
    if (std::chrono::steady_clock::now() >= absolute)
      fail("PACKET_DEADLINE " + where);
  }
};

std::optional<Deadline> packet_deadline;

void initialize_packet_deadline() {
  const char* raw=std::getenv("F269_DEADLINE_SECONDS");
  require(raw&&*raw,"missing F269_DEADLINE_SECONDS");
  const std::string text(raw);
  require(text.find_first_not_of("0123456789")==std::string::npos,
          "bad F269_DEADLINE_SECONDS");
  const u64 seconds=std::stoull(text);require(seconds>0&&seconds<=14370,
          "deadline seconds range");
  packet_deadline=Deadline{std::chrono::steady_clock::now()+
                           std::chrono::seconds(seconds)};
}

void deadline_check(const std::string& where) {
  require(packet_deadline.has_value(),"packet deadline not initialized");
  packet_deadline->check(where);
}

struct PairShell {
  bool zero = false;
  cpp_int quotient = 0;
  cpp_int remainder = 0;
};

struct FermatControl {
  cpp_int A, D, s;
  bool square = false;
  cpp_int minus = 0, plus = 0;
  bool proper = false;
};

struct PublicStage {
  cpp_int N;
  int n = 0;
  int t_terminal = 0;
  int t = 0;
  u64 m = 0, u = 0, r = 0, c = 0;
  cpp_int K;
  int delta = 0, kappa = 0;
  cpp_int S;
  std::array<u64, 2> R{}, C{};
  std::array<cpp_int, 4> Z{};
  std::array<cpp_int, 12> own_gcd{};
  std::array<cpp_int, 6> gaps{};
  std::array<PairShell, 6> pair_shell{};
  std::array<cpp_int, 4> j_signed{};
  std::array<cpp_int, 3> rq{}, rp{};
  std::array<cpp_int, 6> rq_eval{}, rp_eval{};
  cpp_int disc_q, disc_p;
  FermatControl fermat;
};

constexpr std::array<std::pair<int,int>,6> CORNER_PAIRS =
    {{{0,1},{0,2},{0,3},{1,2},{1,3},{2,3}}};

int z_index(int x, int y) {
  if (x == 0 && y == 0) return 0;
  if (x == 1 && y == 0) return 1;
  if (x == 0 && y == 1) return 2;
  return 3;
}

PublicStage analyze_public(const cpp_int& N, int t, u64 u) {
  deadline_check("analyze_public");
  PublicStage s;
  s.N = N;
  s.n = static_cast<int>(bitlength(N));
  s.t_terminal = (s.n - 1) / 4;
  s.t = t;
  require(t >= 1 && t <= 62, "stage t range");
  s.m = u64(1) << t;
  require((u & 1) && u < s.m, "prefix unit range");
  s.u = u;
  s.r = inverse_pow2(u, s.m);
  s.c = static_cast<u64>((N * u % s.m).convert_to<u64>());
  require(s.r >= 1 && s.r < s.m && (s.r & 1), "r canonical odd");
  require(s.c >= 1 && s.c < s.m && (s.c & 1), "c canonical odd");
  const cpp_int ur_minus = cpp_int(u) * s.r - 1;
  require(ur_minus % s.m == 0, "ur divisibility");
  s.kappa = static_cast<int>(((ur_minus / s.m) & 1).convert_to<unsigned>());
  const cpp_int numerator = N - cpp_int(s.r) * s.c;
  require(numerator % s.m == 0, "K divisibility");
  s.K = numerator / s.m;
  s.delta = static_cast<int>((s.K & 1).convert_to<unsigned>());
  s.S = cpp_int(s.r) + s.c + s.m;
  s.R = {s.r, s.r + s.m};
  s.C = {s.c, s.c + s.m};
  s.Z = {s.K, s.K-s.c, s.K-s.r, s.K-s.r-s.c-s.m};
  require(N > cpp_int(8) * s.m * s.m || t == s.t_terminal,
          "nonterminal shell bound");
  for (int x = 0; x < 2; ++x) for (int y = 0; y < 2; ++y) {
    const int i = z_index(x,y);
    require(s.Z[i] == (N - cpp_int(s.R[x]) * s.C[y]) / s.m,
            "rectangle identity");
    require((N - cpp_int(s.R[x]) * s.C[y]) % s.m == 0,
            "corner divisibility");
    require(cpp_int(s.R[x]) * s.C[y] < N && s.Z[i] > 0,
            "corner positivity");
    s.own_gcd[3*i+0] = gcd_abs(s.Z[i], N);
    s.own_gcd[3*i+1] = gcd_abs(s.Z[i], cpp_int(s.R[x]));
    s.own_gcd[3*i+2] = gcd_abs(s.Z[i], cpp_int(s.C[y]));
    require(s.own_gcd[3*i] == 1 && s.own_gcd[3*i+1] == 1 &&
            s.own_gcd[3*i+2] == 1, "corner unit gcd");
  }
  s.gaps = {cpp_int(s.c), cpp_int(s.r), s.S,
            abs_cpp(cpp_int(s.r)-s.c), cpp_int(s.r)+s.m,
            cpp_int(s.c)+s.m};
  for (int i = 0; i < 6; ++i) {
    const auto [j,k] = CORNER_PAIRS[i];
    require(abs_cpp(s.Z[j]-s.Z[k]) == s.gaps[i], "gap identity");
    if (s.gaps[i] == 0) {
      s.pair_shell[i].zero = true;
      require(s.Z[j] == s.Z[k], "zero gap equality");
    } else {
      const cpp_int larger = std::max(s.Z[j],s.Z[k]);
      const cpp_int smaller = std::min(s.Z[j],s.Z[k]);
      auto qr = floor_divmod(larger, smaller);
      require(qr.q == 1 && qr.r == s.gaps[i], "forced quotient one");
      s.pair_shell[i] = {false,qr.q,qr.r};
    }
  }
  for (int a = 0; a < 2; ++a) {
    const int b = a ^ s.delta;
    const cpp_int zcompat = s.Z[z_index(a,b)];
    const cpp_int ja = s.Z[z_index(a,1-b)];
    const int oa = 1-a;
    const int ob = oa ^ s.delta;
    const cpp_int jo = s.Z[z_index(oa,1-ob)];
    s.j_signed[2*a] = ja-zcompat;
    s.j_signed[2*a+1] = jo-zcompat;
    require(abs_cpp(s.j_signed[2*a]) == s.R[a], "J local R identity");
    require(abs_cpp(s.j_signed[2*a+1]) == s.C[b], "J local C identity");
  }
  const cpp_int h = cpp_int(2)*s.m;
  if (s.delta == 0) {
    s.rq = {cpp_int(s.r)*s.r+cpp_int(s.m)*s.r+N,
            h*(cpp_int(2)*s.r+s.m), h*h};
    s.rp = {cpp_int(s.c)*s.c+cpp_int(s.m)*s.c+N,
            h*(cpp_int(2)*s.c+s.m), h*h};
    s.disc_q = s.disc_p = cpp_int(s.m)*s.m-4*N;
  } else {
    s.rq = {N-cpp_int(s.r)*s.r-cpp_int(s.m)*s.r,
            -h*(cpp_int(2)*s.r+s.m), -h*h};
    s.rp = {cpp_int(s.c)*s.c+cpp_int(s.m)*s.c-N,
            h*(cpp_int(2)*s.c+s.m), h*h};
    s.disc_q = s.disc_p = cpp_int(s.m)*s.m+4*N;
  }
  require(s.Z[z_index(0,s.delta)]%2==0 &&
          s.Z[z_index(1,1^s.delta)]%2==0,
          "compatible K integrality");
  const std::array<cpp_int,2> compatible_k = {
      s.Z[z_index(0,s.delta)]/2,
      s.Z[z_index(1,1^s.delta)]/2};
  const cpp_int cb0=s.C[s.delta], cb1=s.C[1^s.delta];
  const std::array<cpp_int,3> rq_from_ordered_determinant = {
      cpp_int(2)*(-cpp_int(s.R[0])*compatible_k[1]
                  +cpp_int(s.R[1])*compatible_k[0]),
      cpp_int(2)*(-h*compatible_k[1]+cpp_int(s.R[0])*cb1
                  +h*compatible_k[0]-cpp_int(s.R[1])*cb0),
      cpp_int(2)*h*(cb1-cb0)};
  const std::array<cpp_int,3> rp_from_ordered_determinant = {
      cpp_int(2)*(-cb0*compatible_k[1]+cb1*compatible_k[0]),
      cpp_int(2)*(-h*compatible_k[1]+cb0*s.R[1]
                  +h*compatible_k[0]-cb1*s.R[0]),
      cpp_int(2)*h*(cpp_int(s.R[1])-s.R[0])};
  require(s.rq==rq_from_ordered_determinant &&
          s.rp==rp_from_ordered_determinant,
          "ordered resultant coefficient determinant");
  const std::array<int,6> points{{-2,-1,0,1,2,3}};
  for (int i = 0; i < 6; ++i) {
    cpp_int x = points[i];
    s.rq_eval[i] = s.rq[0]+s.rq[1]*x+s.rq[2]*x*x;
    s.rp_eval[i] = s.rp[0]+s.rp[1]*x+s.rp[2]*x*x;
    const cpp_int X = h*x+s.r;
    const cpp_int Y = h*x+s.c;
    const cpp_int rq_expected = s.delta==0 ? X*X+s.m*X+N
                                           : N-X*X-s.m*X;
    const cpp_int rp_expected = s.delta==0 ? Y*Y+s.m*Y+N
                                           : Y*Y+s.m*Y-N;
    require(s.rq_eval[i] == rq_expected && s.rp_eval[i] == rp_expected,
            "ordered resultant evaluation");
  }
  s.fermat.A = isqrt(N);
  if (s.fermat.A*s.fermat.A < N) ++s.fermat.A;
  s.fermat.D = s.fermat.A*s.fermat.A-N;
  s.fermat.square = is_square(s.fermat.D,&s.fermat.s);
  if (s.fermat.square) {
    s.fermat.minus=s.fermat.A-s.fermat.s;
    s.fermat.plus=s.fermat.A+s.fermat.s;
    s.fermat.proper=s.fermat.minus>1 && s.fermat.minus<N &&
                    N%s.fermat.minus==0;
  }
  return s;
}

const std::string& transcript_header() {
  static const std::string h =
    "fixture\tN\tn\tt_terminal\tt\tm\tu\tr\tc\tK\tdelta\tkappa\tS\tR0\tR1\tC0\tC1\tZ00\tZ10\tZ01\tZ11\t"
    "gZ00N\tgZ00R\tgZ00C\tgZ10N\tgZ10R\tgZ10C\tgZ01N\tgZ01R\tgZ01C\tgZ11N\tgZ11R\tgZ11C\t"
    "G00_10\tG00_01\tG00_11\tG10_01\tG10_11\tG01_11\t"
    "P00_10_status\tP00_10_q\tP00_10_rem\tP00_01_status\tP00_01_q\tP00_01_rem\t"
    "P00_11_status\tP00_11_q\tP00_11_rem\tP10_01_status\tP10_01_q\tP10_01_rem\t"
    "P10_11_status\tP10_11_q\tP10_11_rem\tP01_11_status\tP01_11_q\tP01_11_rem\t"
    "J0_R_signed\tJ0_C_signed\tJ1_R_signed\tJ1_C_signed\t"
    "RQ_c0\tRQ_c1\tRQ_c2\tRP_c0\tRP_c1\tRP_c2\t"
    "RQ_at_-2\tRQ_at_-1\tRQ_at_0\tRQ_at_1\tRQ_at_2\tRQ_at_3\t"
    "RP_at_-2\tRP_at_-1\tRP_at_0\tRP_at_1\tRP_at_2\tRP_at_3\t"
    "disc_Q\tdisc_P\tfermat_A\tfermat_D\tfermat_s\tfermat_square\tfermat_minus\tfermat_plus\n";
  return h;
}

std::string transcript_row(char fixture, const PublicStage& s) {
  std::vector<std::string> f;
  f.reserve(87);
  f.push_back(std::string(1,fixture)); f.push_back(dec(s.N));
  f.push_back(std::to_string(s.n)); f.push_back(std::to_string(s.t_terminal));
  f.push_back(std::to_string(s.t)); f.push_back(std::to_string(s.m));
  f.push_back(std::to_string(s.u)); f.push_back(std::to_string(s.r));
  f.push_back(std::to_string(s.c)); f.push_back(dec(s.K));
  f.push_back(std::to_string(s.delta)); f.push_back(std::to_string(s.kappa));
  f.push_back(dec(s.S));
  for (u64 x : s.R) f.push_back(std::to_string(x));
  for (u64 x : s.C) f.push_back(std::to_string(x));
  for (const auto& x : s.Z) f.push_back(dec(x));
  for (const auto& x : s.own_gcd) f.push_back(dec(x));
  for (const auto& x : s.gaps) f.push_back(dec(x));
  for (const auto& p : s.pair_shell) {
    if (p.zero) { f.push_back("ZERO_GAP"); f.push_back("NA"); f.push_back("NA"); }
    else { f.push_back("QUOTIENT_ONE"); f.push_back(dec(p.quotient)); f.push_back(dec(p.remainder)); }
  }
  for (const auto& x : s.j_signed) f.push_back(dec(x));
  for (const auto& x : s.rq) f.push_back(dec(x));
  for (const auto& x : s.rp) f.push_back(dec(x));
  for (const auto& x : s.rq_eval) f.push_back(dec(x));
  for (const auto& x : s.rp_eval) f.push_back(dec(x));
  f.push_back(dec(s.disc_q)); f.push_back(dec(s.disc_p));
  f.push_back(dec(s.fermat.A)); f.push_back(dec(s.fermat.D));
  f.push_back(dec(s.fermat.s)); f.push_back(s.fermat.square?"1":"0");
  f.push_back(s.fermat.square?dec(s.fermat.minus):"NA");
  f.push_back(s.fermat.square?dec(s.fermat.plus):"NA");
  require(f.size()==87,"transcript field count");
  return join_tsv(f);
}

enum Reason : std::uint8_t {
  VALID=0, ZERO_GAP=1, DEPTH_MISSING=2, CONTROL_CASE=3,
  TAIL_STATE_ALIAS=4, EQUAL_OPERAND_VALUE=5, ZERO_DENOMINATOR=6,
  V2_ZERO=7, VALUE_CAP=8, ROW_CONTROL_EQUALITY=9
};

struct Tail {
  bool zero_gap = false;
  int tail_id = -1;
  std::vector<cpp_int> x;
  std::vector<cpp_int> q;
  std::array<bool,9> strict{};
  std::array<cpp_int,9> P{}, Q{};
  std::string serialization;
  int alias_id = -1;
};

struct RootValue {
  bool valid = false;
  Reason reason = DEPTH_MISSING;
  cpp_int value = 0;
};

struct BranchPublic {
  std::array<Tail,14> tails;
  std::array<RootValue,444> roots;
};

struct RowPublic {
  PublicStage stage;
  std::array<BranchPublic,2> branch;
  std::set<cpp_int> controls;
};

std::vector<cpp_int> continuant_q(const Tail& tail, int depth) {
  require(depth >= 1 && static_cast<int>(tail.q.size()) >= depth,
          "continuant depth");
  cpp_int pm2=1, qm2=0;
  cpp_int pm1=tail.q[0], qm1=1;
  if (depth == 1) return {pm1,qm1,pm2,qm2};
  for (int j=2;j<=depth;++j) {
    cpp_int p=tail.q[j-1]*pm1+pm2;
    cpp_int q=tail.q[j-1]*qm1+qm2;
    pm2=pm1; qm2=qm1; pm1=p; qm1=q;
  }
  require(pm1*qm2-pm2*qm1 == (depth%2 ? -1 : 1),
          "continuant determinant");
  return {pm1,qm1,pm2,qm2};
}

Tail build_tail(int id, const cpp_int& x0, const cpp_int& x1, bool zero) {
  Tail t;
  t.tail_id=id;
  t.zero_gap=zero;
  if (zero) {
    t.serialization="ZERO_GAP";
    return t;
  }
  require(x0>x1 && x1>0,"tail ordered positive");
  t.x.push_back(x0); t.x.push_back(x1);
  for (int j=1;j<=9;++j) {
    if (t.x[j]==0) break;
    auto dr=floor_divmod(t.x[j-1],t.x[j]);
    require(dr.q>=1 && dr.r>=0 && dr.r<t.x[j],"Euclidean division");
    t.q.push_back(dr.q);
    t.x.push_back(dr.r);
    if (dr.r==0) break;
  }
  for (int d=1;d<=8;++d) {
    t.strict[d]=static_cast<int>(t.x.size())>d+2 && t.x[d+2]>0;
    if (static_cast<int>(t.q.size())>=d) {
      auto k=continuant_q(t,d);
      t.P[d]=k[0]; t.Q[d]=k[1];
    }
  }
  std::ostringstream ser;
  ser << dec(x0) << ',' << dec(x1) << '|';
  for (const auto& x:t.x) ser << dec(x) << ',';
  ser << '|'; for (const auto& q:t.q) ser << dec(q) << ',';
  t.serialization=ser.str();
  return t;
}

std::array<int,2> role_corner_xy(int role, int a, int delta) {
  const int ba=a^delta, oa=1-a, oba=oa^delta;
  if (role==0) return {a,ba};
  if (role==1) return {oa,oba};
  if (role==2) return {a,1-ba};
  return {oa,1-oba};
}

std::uint64_t tail_provenance(int tail_id) {
  static constexpr std::array<std::pair<int,int>,6> pair_roles =
      {{{0,1},{0,2},{0,3},{1,2},{1,3},{2,3}}};
  std::uint64_t p=std::uint64_t(1) << tail_id;
  if (tail_id<6) {
    p|=std::uint64_t(1)<<(16+pair_roles[tail_id].first);
    p|=std::uint64_t(1)<<(16+pair_roles[tail_id].second);
    p|=std::uint64_t(1)<<(20+tail_id);
  } else {
    const int k=tail_id-6, role=k/2, coordinate=k%2;
    p|=std::uint64_t(1)<<(16+role);
    p|=std::uint64_t(1)<<(32+2*role+coordinate);
  }
  return p;
}

bool is_row_control(const std::set<cpp_int>& controls,const cpp_int& v) {
  return controls.count(v)||controls.count(-v);
}

RootValue ordinary_root(const Tail& t,int offset,const std::set<cpp_int>& controls) {
  if (t.zero_gap) return {false,ZERO_GAP,0};
  int kind=-1,param=-1,depth=0;
  if (offset<8) {kind=0;param=offset+1;}
  else if(offset<16){kind=1;param=offset-7;}
  else if(offset<18){kind=2;param=offset-15;}
  else {
    static const int depths[3]={2,4,8};
    const int group=(offset-18)/3;
    depth=depths[(offset-18)%3]; kind=3+group;
  }
  const int d=kind<=2?param:depth;
  if (!t.strict[d]) return {false,DEPTH_MISSING,0};
  cpp_int v=0;
  if(kind==0) v=t.q[param-1];
  else if(kind==1) v=t.x[param+1];
  else if(kind==2) v=centered_rem(t.x[param-1],t.x[param]);
  else if(kind==3) for(int j=0;j<depth;++j) v+=t.q[j];
  else if(kind==4) {v=t.q[0];for(int j=1;j<depth;++j)v=std::max(v,t.q[j]);}
  else if(kind==5) v=t.P[depth];
  else if(kind==6) v=t.Q[depth];
  else fail("ordinary root kind");
  if(is_row_control(controls,v))return {false,ROW_CONTROL_EQUALITY,0};
  return {true,VALID,v};
}

RootValue cross_root(const Tail& left,const Tail& right,int depth,
                     const std::set<cpp_int>& controls) {
  if(left.zero_gap||right.zero_gap)return {false,ZERO_GAP,0};
  if(!left.strict[depth]||!right.strict[depth])
    return {false,DEPTH_MISSING,0};
  if(left.alias_id==right.alias_id)return {false,TAIL_STATE_ALIAS,0};
  cpp_int value=left.P[depth]*right.Q[depth]
                -left.Q[depth]*right.P[depth];
  if(is_row_control(controls,value))return {false,ROW_CONTROL_EQUALITY,0};
  return {true,VALID,value};
}

RowPublic build_row_public(const PublicStage& s) {
  RowPublic row;
  row.stage=s;
  auto add_control=[&](cpp_int x){row.controls.insert(x);};
  add_control(0);add_control(1);add_control(s.m);add_control(s.r);add_control(s.c);
  add_control(s.S);for(auto x:s.R)add_control(x);for(auto x:s.C)add_control(x);
  for(auto x:s.Z)add_control(x);for(auto x:s.gaps)add_control(x);
  for(auto x:s.j_signed)add_control(x);
  add_control(s.fermat.A);add_control(s.fermat.D);
  if(s.fermat.square){add_control(s.fermat.minus);add_control(s.fermat.plus);}
  static constexpr std::array<std::pair<int,int>,6> pairs =
      {{{0,1},{0,2},{0,3},{1,2},{1,3},{2,3}}};
  static constexpr std::array<std::pair<int,int>,8> cross =
      {{{1,4},{2,3},{6,8},{7,9},{10,12},{11,13},{6,11},{7,10}}};
  for(int a=0;a<2;++a){
    auto& bp=row.branch[a];
    std::array<cpp_int,4> cv;
    std::array<std::array<int,2>,4> xy;
    for(int role=0;role<4;++role){
      xy[role]=role_corner_xy(role,a,s.delta);
      cv[role]=s.Z[z_index(xy[role][0],xy[role][1])];
    }
    for(int id=0;id<6;++id){
      const auto [x,y]=pairs[id];
      cpp_int gap=abs_cpp(cv[x]-cv[y]);
      if(gap==0) bp.tails[id]=build_tail(id,0,0,true);
      else bp.tails[id]=build_tail(id,std::min(cv[x],cv[y]),gap,false);
    }
    for(int id=6;id<14;++id){
      const int k=id-6,role=k/2,coord=k%2;
      const u64 own=coord==0?s.R[xy[role][0]]:s.C[xy[role][1]];
      bp.tails[id]=build_tail(id,cv[role],own,false);
    }
    std::map<std::string,int> alias;
    for(auto& t:bp.tails){
      if(t.zero_gap)continue;
      auto [it,inserted]=alias.emplace(t.serialization,t.tail_id);
      if(!inserted)it->second=std::min(it->second,t.tail_id);
    }
    for(auto& t:bp.tails)if(!t.zero_gap)t.alias_id=alias[t.serialization];
    for(int tail=0;tail<14;++tail)for(int off=0;off<30;++off)
      bp.roots[30*tail+off]=ordinary_root(bp.tails[tail],off,row.controls);
    for(int cp=0;cp<8;++cp)for(int di=0;di<3;++di){
      const int d=di==0?2:di==1?4:8;
      const auto [l,r]=cross[cp];
      bp.roots[420+3*cp+di]=cross_root(bp.tails[l],bp.tails[r],d,row.controls);
    }
  }
  return row;
}

enum class FormKind { CONST, AFF, ABS_AFF, TAG, OPAQUE, INVALID };
struct Form {
  FormKind kind=FormKind::OPAQUE;
  std::array<long long,5> a{};
  long long constant=0;
  int tag=-1;
  static Form opaque(){return {};}
  static Form cnst(long long x){Form f;f.kind=FormKind::CONST;f.constant=x;return f;}
  static Form aff(std::array<long long,5> x){Form f;f.kind=FormKind::AFF;f.a=x;return f;}
};

struct Chamber {int a,delta,kappa,order;};

bool form_equal(const Form&x,const Form&y){
  return x.kind==y.kind&&x.a==y.a&&x.constant==y.constant&&x.tag==y.tag;
}

Form affine_form(std::array<long long,5> a) {
  if(a[0]==0&&a[1]==0&&a[2]==0&&a[3]==0)return Form::cnst(a[4]);
  return Form::aff(a);
}

bool affine_coefficients(const Form& f,std::array<long long,5>* out) {
  if(f.kind==FormKind::AFF||f.kind==FormKind::ABS_AFF){*out=f.a;return true;}
  if(f.kind==FormKind::CONST){*out={0,0,0,0,f.constant};return true;}
  return false;
}

Form negate_affine(const Form& f) {
  std::array<long long,5> a{};require(affine_coefficients(f,&a),"negate affine");
  for(auto& x:a)x=-x;
  Form out=affine_form(a);
  if(f.kind==FormKind::ABS_AFF&&out.kind==FormKind::AFF)out.kind=FormKind::ABS_AFF;
  return out;
}

std::array<long long,5> canonical_abs_coefficients(std::array<long long,5> a) {
  for(long long x:a)if(x!=0){if(x<0)for(auto& y:a)y=-y;break;}
  return a;
}

int proved_sign(const Form& f,const Chamber& c) {
  if(f.kind==FormKind::CONST)return (f.constant>0)-(f.constant<0);
  if(f.kind==FormKind::ABS_AFF)return 2;
  if(f.kind!=FormKind::AFF)return 2;
  if(f.a==std::array<long long,5>{0,0,0,0,0})return 0;
  static const std::array<std::array<long long,5>,10> positive={{
    {{0,0,0,1,0}},{{0,1,0,0,0}},{{0,0,1,0,0}},{{0,1,1,1,0}},
    {{0,1,0,1,0}},{{0,0,1,1,0}},{{1,0,0,0,0}},{{1,0,-1,0,0}},
    {{1,-1,0,0,0}},{{1,-1,-1,-1,0}}
  }};
  for(const auto& v:positive){
    if(f.a==v)return 1;
    std::array<long long,5> neg=v;for(auto& x:neg)x=-x;if(f.a==neg)return -1;
  }
  const std::array<long long,5> rc={0,1,-1,0,0};
  if(f.a==rc)return c.order==0?-1:c.order==1?0:1;
  std::array<long long,5> cr=rc;for(auto& x:cr)x=-x;
  if(f.a==cr)return c.order==0?1:c.order==1?0:-1;
  return 2;
}

Form abs_form(const Form& x,const Chamber& c) {
  if(x.kind==FormKind::CONST)return Form::cnst(std::llabs(x.constant));
  if(x.kind==FormKind::ABS_AFF)return x;
  if(x.kind!=FormKind::AFF)return Form::opaque();
  const int sign=proved_sign(x,c);
  if(sign==0)return Form::cnst(0);
  if(sign==1)return x;
  if(sign==-1)return negate_affine(x);
  Form out=x;out.kind=FormKind::ABS_AFF;
  out.a=canonical_abs_coefficients(out.a);return out;
}

bool static_control(const Form& f){
  if(f.kind==FormKind::CONST||f.kind==FormKind::TAG)return true;
  if(f.kind!=FormKind::AFF&&f.kind!=FormKind::ABS_AFF)return false;
  static const std::vector<std::array<long long,5>> table={
    {0,0,0,1,0},{0,1,0,0,0},{0,0,1,0,0},{0,1,1,1,0},
    {0,1,0,1,0},{0,0,1,1,0},{1,0,0,0,0},{1,0,-1,0,0},
    {1,-1,0,0,0},{1,-1,-1,-1,0},{0,1,-1,0,0}
  };
  for(auto v:table)if(f.a==v||f.a==std::array<long long,5>{-v[0],-v[1],-v[2],-v[3],-v[4]})return true;
  return false;
}

Form normalize_unary(int op,const Form&x,const Chamber&c){
  if(x.kind==FormKind::CONST){
    if(op==0)return Form::cnst(std::llabs(x.constant));
    if(op==1){unsigned long long a=x.constant<0?-x.constant:x.constant;int b=0;while(a){++b;a>>=1;}return Form::cnst(b);}
    if(op==2){if(x.constant==0){Form f;f.kind=FormKind::INVALID;return f;}unsigned long long a=x.constant<0?-x.constant:x.constant;int v=0;while((a&1)==0){++v;a>>=1;}return Form::cnst(v);}
  }
  if(op==0&&(x.kind==FormKind::AFF||x.kind==FormKind::ABS_AFF))return abs_form(x,c);
  return Form::opaque();
}

Form normalize_binary(int op,const Form&x,const Form&y,const Chamber&c){
  if(x.kind==FormKind::CONST&&y.kind==FormKind::CONST){
    long long a=x.constant,b=y.constant;
    if(op==0)return Form::cnst(a+b);
    if(op==1)return Form::cnst(std::llabs(a-b));
    if(op==2)return Form::cnst(std::min(a,b));
    if(op==3)return Form::cnst(std::max(a,b));
    if(op==4)return Form::cnst(std::gcd(std::llabs(a),std::llabs(b)));
    if(op==5)return Form::cnst(a*b);
    if((op==6||op==7||op==8)&&b!=0){
      long long D=std::llabs(b),q=a/D,r=a%D;if(r<0){r+=D;--q;}
      if(op==6)return Form::cnst(q);
      if(op==7)return Form::cnst(r);
      return Form::cnst(2*r>D?r-D:r);
    }
  }
  std::array<long long,5> xa{},ya{};
  const bool xaff=affine_coefficients(x,&xa)&&x.kind!=FormKind::ABS_AFF;
  const bool yaff=affine_coefficients(y,&ya)&&y.kind!=FormKind::ABS_AFF;
  if(op==0&&xaff&&yaff){for(int i=0;i<5;++i)xa[i]+=ya[i];return affine_form(xa);}
  if(op==1&&xaff&&yaff){for(int i=0;i<5;++i)xa[i]-=ya[i];return abs_form(affine_form(xa),c);}
  if((op==2||op==3)&&form_equal(x,y))return x;
  if((op==2||op==3)&&xaff&&yaff){
    std::array<long long,5> difference=xa;for(int i=0;i<5;++i)difference[i]-=ya[i];
    const int sign=proved_sign(affine_form(difference),c);
    if(sign!=2){
      if(op==2)return sign<=0?x:y;
      return sign>=0?x:y;
    }
  }
  if(op==4&&form_equal(x,y))return abs_form(x,c);
  if(op==4&&x.kind==FormKind::CONST&&x.constant==0)return abs_form(y,c);
  if(op==4&&y.kind==FormKind::CONST&&y.constant==0)return abs_form(x,c);
  if(op==5&&x.kind==FormKind::CONST){if(x.constant==0)return x;if(x.constant==1)return y;}
  if(op==5&&y.kind==FormKind::CONST){if(y.constant==0)return y;if(y.constant==1)return x;}
  if(op==5&&x.kind==FormKind::CONST&&x.constant==-1&&yaff)return negate_affine(y);
  if(op==5&&y.kind==FormKind::CONST&&y.constant==-1&&xaff)return negate_affine(x);
  if(op>=6&&op<=8){
    if(x.kind==FormKind::CONST&&x.constant==0&&proved_sign(y,c)!=0&&proved_sign(y,c)!=2)
      return Form::cnst(0);
    if(y.kind==FormKind::CONST&&(y.constant==1||y.constant==-1)){
      if(op==6)return x;
      return Form::cnst(0);
    }
  }
  return Form::opaque();
}

std::array<Chamber,24> chambers(){
  std::array<Chamber,24> c{};
  for(int a=0;a<2;++a)for(int d=0;d<2;++d)for(int k=0;k<2;++k)for(int o=0;o<3;++o){
    int i=12*a+6*d+3*k+o;c[i]={a,d,k,o};
  }
  return c;
}

enum class NodeKind { ROOT, UNARY, BINARY, ADAPTIVE };
struct Node {
  NodeKind kind=NodeKind::ROOT;
  int op=0,param=0,attempt_id=0,typed_layer=0;
  std::vector<std::shared_ptr<Node>> child;
  std::string syntax;
  std::uint64_t provenance=0;
  std::uint32_t control_mask=0;
  int node_count=1;
  int eval_index=-1;
  int syntax_id=-1;
  Form root_form=Form::opaque();
};

Form normalize_node(const std::shared_ptr<Node>&node,const Chamber&c,
                    std::unordered_map<const Node*,Form>&memo){
  auto it=memo.find(node.get());if(it!=memo.end())return it->second;
  Form f=Form::opaque();
  if(node->kind==NodeKind::ROOT)f=node->root_form;
  else if(node->kind==NodeKind::UNARY)f=normalize_unary(node->op,normalize_node(node->child[0],c,memo),c);
  else if(node->kind==NodeKind::BINARY)f=normalize_binary(node->op,normalize_node(node->child[0],c,memo),normalize_node(node->child[1],c,memo),c);
  else{
    if(node->op<=2){
      int bit=node->op==0?c.kappa:node->op==1?c.delta:(c.kappa^c.delta);
      f=normalize_node(node->child[bit?1:0],c,memo);
    }else if(node->op==3){
      Form guard=normalize_node(node->child[0],c,memo);
      Form x=normalize_node(node->child[1],c,memo);
      Form y=normalize_node(node->child[2],c,memo);
      if(form_equal(x,y))f=x;
      else{const int sign=proved_sign(guard,c);if(sign!=2)f=sign<0?x:y;}
    }else{
      Form g=normalize_node(node->child[0],c,memo);
      Form h=normalize_node(node->child[1],c,memo);
      Form x=normalize_node(node->child[2],c,memo);
      Form y=normalize_node(node->child[3],c,memo);
      if(form_equal(x,y))f=x;
      else{
        std::array<long long,5> ga{},ha{};
        if(affine_coefficients(g,&ga)&&g.kind!=FormKind::ABS_AFF&&
           affine_coefficients(h,&ha)&&h.kind!=FormKind::ABS_AFF){
          for(int i=0;i<5;++i)ga[i]-=ha[i];
          const int sign=proved_sign(affine_form(ga),c);
          if(sign!=2)f=sign<0?x:y;
        }
      }
    }
  }
  memo.emplace(node.get(),f);return f;
}

std::uint32_t compute_control_mask(const std::shared_ptr<Node>&node){
  std::uint32_t mask=0;auto cs=chambers();
  for(int i=0;i<24;++i){std::unordered_map<const Node*,Form> memo;Form f=normalize_node(node,cs[i],memo);if(static_control(f))mask|=std::uint32_t(1)<<i;}
  return mask;
}

int distinct_node_count(const std::shared_ptr<Node>&n){
  std::unordered_set<const Node*>seen;
  std::function<void(const std::shared_ptr<Node>&)>walk=[&](const std::shared_ptr<Node>&x){if(!seen.insert(x.get()).second)return;for(auto&c:x->child)walk(c);};
  walk(n);return static_cast<int>(seen.size());
}

struct GrammarStats {
  std::size_t root_retained=0,tuple_retained=0,type_reject=0;
  std::size_t provenance_reject=0,duplicate_reject=0,control_reject=0;
};

struct Grammar {
  std::vector<std::shared_ptr<Node>> eval_order;
  std::vector<std::shared_ptr<Node>> syntax_order;
  GrammarStats stats;
  std::string serialized;
  std::array<std::size_t,4> layer_end{};
};

std::vector<u64> tuple_words(int layer,u64 j,int count){
  std::vector<u64>w(count);w[0]=splitmix64(GRAMMAR_SEED^(u64(layer)<<56)^j);
  for(int k=0;k+1<count;++k)w[k+1]=splitmix64(w[k]+u64(k));return w;
}

bool disjoint_provenance(const std::vector<std::shared_ptr<Node>>&v){
  for(std::size_t i=0;i<v.size();++i)for(std::size_t j=i+1;j<v.size();++j)if(v[i]->provenance&v[j]->provenance)return false;return true;
}

Grammar build_grammar(){
  Grammar g;std::unordered_set<std::string>seen;
  for(int tail=0;tail<14;++tail)for(int off=0;off<30;++off){
    auto n=std::make_shared<Node>();n->kind=NodeKind::ROOT;n->attempt_id=30*tail+off;
    int kind,param;if(off<8){kind=0;param=off+1;}else if(off<16){kind=1;param=off-7;}else if(off<18){kind=2;param=off-15;}else{kind=3+(off-18)/3;param=(off-18)%3==0?2:(off-18)%3==1?4:8;}
    n->op=kind;n->param=param;n->syntax="r("+std::to_string(tail)+","+std::to_string(kind)+","+std::to_string(param)+")";
    n->provenance=tail_provenance(tail);n->eval_index=g.eval_order.size();seen.insert(n->syntax);g.eval_order.push_back(n);
  }
  static constexpr std::array<std::pair<int,int>,8> cp={{{1,4},{2,3},{6,8},{7,9},{10,12},{11,13},{6,11},{7,10}}};
  for(int p=0;p<8;++p)for(int di=0;di<3;++di){
    int d=di==0?2:di==1?4:8;auto n=std::make_shared<Node>();n->kind=NodeKind::ROOT;n->attempt_id=420+3*p+di;n->op=7;n->param=d;
    n->syntax="x("+std::to_string(p)+","+std::to_string(d)+")";n->provenance=tail_provenance(cp[p].first)|tail_provenance(cp[p].second);n->eval_index=g.eval_order.size();seen.insert(n->syntax);g.eval_order.push_back(n);
  }
  require(g.eval_order.size()==444,"root grammar size");g.stats.root_retained=444;
  g.layer_end[0]=g.eval_order.size();
  auto sorted_pool=[&](std::size_t end){std::vector<std::shared_ptr<Node>>p(g.eval_order.begin(),g.eval_order.begin()+end);std::sort(p.begin(),p.end(),[](auto&a,auto&b){return a->syntax<b->syntax;});return p;};
  for(int layer=1;layer<=3;++layer){
    const std::size_t attempts=layer==1?UNARY_ATTEMPTS:layer==2?BINARY_ATTEMPTS:ADAPTIVE_ATTEMPTS;
    const std::size_t immutable_end=g.eval_order.size();auto pool=sorted_pool(immutable_end);require(!pool.empty(),"empty operand pool");
    for(std::size_t j=0;j<attempts;++j){
      if((j&255)==0)deadline_check("grammar construction");
      auto n=std::make_shared<Node>();n->typed_layer=layer;n->attempt_id=(layer==1?444:layer==2?1468:4540)+j;
      std::vector<std::shared_ptr<Node>>operands;
      if(layer==1){auto w=tuple_words(layer,j,2);n->kind=NodeKind::UNARY;n->op=w[0]%3;operands={pool[w[1]%pool.size()]};n->syntax="u("+std::to_string(n->op)+","+operands[0]->syntax+")";}
      else if(layer==2){auto w=tuple_words(layer,j,3);n->kind=NodeKind::BINARY;n->op=w[0]%9;operands={pool[w[1]%pool.size()],pool[w[2]%pool.size()]};if(n->op<=5&&operands[1]->syntax<operands[0]->syntax)std::swap(operands[0],operands[1]);n->syntax="b("+std::to_string(n->op)+","+operands[0]->syntax+","+operands[1]->syntax+")";}
      else{auto w=tuple_words(layer,j,5);n->kind=NodeKind::ADAPTIVE;n->op=w[0]%5;if(n->op<=2){operands={pool[w[1]%pool.size()],pool[w[2]%pool.size()]};n->syntax="a("+std::to_string(n->op)+","+operands[0]->syntax+","+operands[1]->syntax+")";}else if(n->op==3){operands={pool[w[1]%pool.size()],pool[w[2]%pool.size()],pool[w[3]%pool.size()]};n->syntax="a(3,"+operands[0]->syntax+","+operands[1]->syntax+","+operands[2]->syntax+")";}else{operands={pool[w[1]%pool.size()],pool[w[2]%pool.size()],pool[w[3]%pool.size()],pool[w[4]%pool.size()]};n->syntax="a(4,"+operands[0]->syntax+","+operands[1]->syntax+","+operands[2]->syntax+","+operands[3]->syntax+")";}}
      if(!disjoint_provenance(operands)){++g.stats.provenance_reject;continue;}
      if(!seen.insert(n->syntax).second){++g.stats.duplicate_reject;continue;}
      n->child=operands;n->provenance=0;for(auto&x:operands)n->provenance|=x->provenance;n->control_mask=compute_control_mask(n);
      if(n->control_mask==0x00ffffffU){++g.stats.control_reject;seen.erase(n->syntax);continue;}
      n->node_count=distinct_node_count(n);n->eval_index=g.eval_order.size();g.eval_order.push_back(n);++g.stats.tuple_retained;
    }
    g.layer_end[layer]=g.eval_order.size();
  }
  require(g.stats.tuple_retained+g.stats.type_reject+g.stats.provenance_reject+g.stats.duplicate_reject+g.stats.control_reject==5120,"tuple partition");
  require(g.eval_order.size()==444+g.stats.tuple_retained,"retained partition");
  g.syntax_order=g.eval_order;std::sort(g.syntax_order.begin(),g.syntax_order.end(),[](auto&a,auto&b){return a->syntax<b->syntax;});
  std::ostringstream serial;serial<<"syntax_id\tgrammar_attempt_id\ttyped_layer\tnode_count\tcontrol_case_mask\tcanonical_syntax\n";
  for(std::size_t i=0;i<g.syntax_order.size();++i){auto&n=g.syntax_order[i];n->syntax_id=i;serial<<i<<'\t'<<n->attempt_id<<'\t'<<n->typed_layer<<'\t'<<n->node_count<<'\t'<<std::hex<<std::setfill('0')<<std::setw(8)<<n->control_mask<<std::dec<<'\t'<<n->syntax<<'\n';}
  g.serialized=serial.str();return g;
}

struct Eval {
  bool valid=false;Reason reason=DEPTH_MISSING;cpp_int value=0;
  int value_alias_id=-1;std::uint16_t reason_mask=0;
  Eval(bool valid_value=false,Reason reason_value=DEPTH_MISSING,cpp_int integer=0,
       int alias=-1,std::uint16_t mask=0):valid(valid_value),reason(reason_value),
       value(std::move(integer)),value_alias_id(alias),
       reason_mask(mask?mask:(reason_value==VALID?0:std::uint16_t(1U<<reason_value))){}
};

Reason min_reason(Reason a,Reason b){if(a==VALID)return b;if(b==VALID)return a;return static_cast<Reason>(std::min<int>(a,b));}

bool cap_ok(const cpp_int&v,int n){return bitlength(v)<=std::size_t(8*n+256);}

bool tail_alias_conflict(const Node&n,const BranchPublic&bp){
  for(std::size_t i=0;i<n.child.size();++i)for(std::size_t j=i+1;j<n.child.size();++j)
    for(int ti=0;ti<14;++ti)if(n.child[i]->provenance&(std::uint64_t(1)<<ti))
      for(int tj=0;tj<14;++tj)if(n.child[j]->provenance&(std::uint64_t(1)<<tj)){
        const auto&a=bp.tails[ti],&b=bp.tails[tj];
        if(ti!=tj&&!a.zero_gap&&!b.zero_gap&&a.alias_id==b.alias_id)return true;
      }
  return false;
}

Eval evaluate_node(const Node&n,const RowPublic&row,int a,const std::vector<Eval>&ev){
  const auto&stage=row.stage;const auto&bp=row.branch[a];
  if(n.kind==NodeKind::ROOT){const auto&r=bp.roots[n.attempt_id];return {r.valid,r.reason,r.value,-1};}
  const int order=stage.r<stage.c?0:stage.r==stage.c?1:2;const int ci=12*a+6*stage.delta+3*stage.kappa+order;
  Reason child_reason=VALID;std::uint16_t child_mask=0;std::vector<cpp_int>v;
  for(auto&c:n.child){const auto&e=ev[c->eval_index];if(!e.valid)child_reason=min_reason(child_reason,e.reason);child_mask|=e.reason_mask;v.push_back(e.value);}
  if(child_reason!=VALID)return {false,child_reason,0,-1,child_mask};
  if(n.control_mask&(std::uint32_t(1)<<ci))return {false,CONTROL_CASE,0,-1};
  if(n.child.size()>1&&tail_alias_conflict(n,bp))return {false,TAIL_STATE_ALIAS,0,-1};
  for(std::size_t i=0;i<v.size();++i)for(std::size_t j=i+1;j<v.size();++j)if(v[i]==v[j])return {false,EQUAL_OPERAND_VALUE,0,-1};
  cpp_int out=0;
  if(n.kind==NodeKind::UNARY){if(n.op==0)out=abs_cpp(v[0]);else if(n.op==1)out=bitlength(v[0]);else{if(v[0]==0)return {false,V2_ZERO,0,-1};out=v2_nonzero(v[0]);}}
  else if(n.kind==NodeKind::BINARY){if(n.op==0)out=v[0]+v[1];else if(n.op==1)out=abs_cpp(v[0]-v[1]);else if(n.op==2)out=std::min(v[0],v[1]);else if(n.op==3)out=std::max(v[0],v[1]);else if(n.op==4)out=gcd_abs(v[0],v[1]);else if(n.op==5)out=v[0]*v[1];else{if(v[1]==0)return {false,ZERO_DENOMINATOR,0,-1};auto d=floor_divmod(v[0],v[1]);out=n.op==6?d.q:n.op==7?d.r:centered_rem(v[0],v[1]);}}
  else{if(n.op<=2){int bit=n.op==0?stage.kappa:n.op==1?stage.delta:(stage.kappa^stage.delta);out=v[bit?1:0];}else if(n.op==3)out=v[0]<0?v[1]:v[2];else out=v[0]<v[1]?v[2]:v[3];}
  if(!cap_ok(out,stage.n))return {false,VALUE_CAP,0,-1};if(is_row_control(row.controls,out))return {false,ROW_CONTROL_EQUALITY,0,-1};return {true,VALID,out,-1};
}

struct EvaluatedRow {std::array<std::vector<Eval>,2> branch;};

EvaluatedRow evaluate_all(const Grammar&g,const RowPublic&row){
  EvaluatedRow out;
  for(int a=0;a<2;++a){
    auto&v=out.branch[a];v.resize(g.eval_order.size());
    std::size_t begin=0;
    for(int layer=0;layer<4;++layer){
      for(std::size_t i=begin;i<g.layer_end[layer];++i){auto&n=g.eval_order[i];v[i]=evaluate_node(*n,row,a,v);}
      std::map<cpp_int,int> aliases;
      for(std::size_t i=begin;i<g.layer_end[layer];++i)if(v[i].valid){
        const int syntax_id=g.eval_order[i]->syntax_id;
        auto [it,inserted]=aliases.emplace(v[i].value,syntax_id);
        if(!inserted)it->second=std::min(it->second,syntax_id);
      }
      for(std::size_t i=begin;i<g.layer_end[layer];++i)if(v[i].valid)
        v[i].value_alias_id=aliases[v[i].value];
      begin=g.layer_end[layer];
    }
  }
  return out;
}

bool static_ticket_control(const std::shared_ptr<Node>& node,int ticket,
                           const PublicStage& stage) {
  const int order=stage.r<stage.c?0:stage.r==stage.c?1:2;
  Chamber c0{0,stage.delta,stage.kappa,order},c1{1,stage.delta,stage.kappa,order};
  std::unordered_map<const Node*,Form> memo0,memo1;
  Form f0=normalize_node(node,c0,memo0),f1=normalize_node(node,c1,memo1),ticket_form;
  if(ticket==0)ticket_form=f0;
  else if(ticket==1)ticket_form=f1;
  else{
    std::array<long long,5> a{},b{};
    if(!affine_coefficients(f0,&a)||f0.kind==FormKind::ABS_AFF||
       !affine_coefficients(f1,&b)||f1.kind==FormKind::ABS_AFF)return false;
    for(int i=0;i<5;++i)a[i]+=ticket==2?-b[i]:b[i];
    ticket_form=affine_form(a);
  }
  return static_control(ticket_form);
}

std::string evaluation_reason_digest(const std::vector<Eval>& values) {
  std::string bytes((values.size()+1)/2,'\0');
  for(std::size_t i=0;i<values.size();++i){const unsigned char reason=values[i].reason;
    if(i&1)bytes[i/2]=char(static_cast<unsigned char>(bytes[i/2])|(reason<<4));
    else bytes[i/2]=char(reason);}
  return sha256_bytes(bytes);
}

std::string evaluation_reason_histogram(const std::vector<Eval>& values) {
  std::array<u64,10> histogram{};for(const auto& value:values)++histogram[value.reason];
  std::ostringstream out;for(std::size_t i=0;i<histogram.size();++i){if(i)out<<',';out<<histogram[i];}
  return out.str();
}

std::string evaluation_alias_digest(const std::vector<Eval>& values) {
  std::ostringstream bytes;for(const auto& value:values)
    bytes<<(value.valid?std::to_string(value.value_alias_id):"NA")<<'\n';
  return sha256_bytes(bytes.str());
}

std::string evaluation_invalid_mask_digest(const std::vector<Eval>& values) {
  std::string bytes;bytes.resize(2*values.size());
  for(std::size_t i=0;i<values.size();++i){bytes[2*i]=char(values[i].reason_mask&255);
    bytes[2*i+1]=char(values[i].reason_mask>>8);}return sha256_bytes(bytes);
}

std::string root_mask(const BranchPublic&b){std::array<unsigned char,56>x{};for(int i=0;i<444;++i)if(b.roots[i].valid)x[i/8]|=1u<<(i%8);std::ostringstream o;o<<std::hex<<std::setfill('0');for(auto c:x)o<<std::setw(2)<<int(c);return o.str();}

std::string packed_reason_digest(const BranchPublic&b){std::string bytes(222,'\0');for(int i=0;i<444;++i){unsigned char r=b.roots[i].reason;if(i&1)bytes[i/2]=char(static_cast<unsigned char>(bytes[i/2])|(r<<4));else bytes[i/2]=char(r);}return sha256_bytes(bytes);}

std::array<u64,10> reason_histogram(const BranchPublic&b){std::array<u64,10>h{};for(auto&r:b.roots)++h[r.reason];return h;}

std::string branch_mask(const Eval& a0,const Eval& a1) {
  const unsigned mask=(a0.valid?1U:0U)|(a1.valid?2U:0U);
  std::ostringstream out;out<<std::hex<<std::setfill('0')<<std::setw(2)<<mask;
  return out.str();
}

bool depends_on_cross_root(const std::shared_ptr<Node>& node) {
  if(node->kind==NodeKind::ROOT)return node->attempt_id>=420;
  for(const auto& child:node->child)if(depends_on_cross_root(child))return true;
  return false;
}

enum class PairDomainStatus {
  OK,
  OUT_OF_DOMAIN_COMPOSITE_P,
  OUT_OF_DOMAIN_COMPOSITE_Q,
  OUT_OF_DOMAIN_NOT_DISTINCT,
  OUT_OF_DOMAIN_UNBALANCED
};

PairDomainStatus validate_stress_pair(u64 p,u64 q) {
  if(!is_prime64(p))return PairDomainStatus::OUT_OF_DOMAIN_COMPOSITE_P;
  if(!is_prime64(q))return PairDomainStatus::OUT_OF_DOMAIN_COMPOSITE_Q;
  if(p==q)return PairDomainStatus::OUT_OF_DOMAIN_NOT_DISTINCT;
  if(!(p<q&&q<2*p))return PairDomainStatus::OUT_OF_DOMAIN_UNBALANCED;
  return PairDomainStatus::OK;
}

u64 steady_nanoseconds() {
  return std::chrono::duration_cast<std::chrono::nanoseconds>(
      std::chrono::steady_clock::now().time_since_epoch()).count();
}

u64 proc_status_kib(const std::string& key) {
  std::ifstream in("/proc/self/status");
  require(bool(in),"open /proc/self/status");
  std::string line;
  while(std::getline(in,line))if(line.rfind(key+":",0)==0){
    std::istringstream fields(line.substr(key.size()+1));u64 value;std::string unit;
    require(bool(fields>>value>>unit)&&unit=="kB","bad /proc status value");return value;
  }
  fail("missing /proc status key "+key);
}

void hash_u64(Sha256& hash,u64 value) {
  std::array<unsigned char,8> bytes{};
  for(int i=0;i<8;++i)bytes[i]=static_cast<unsigned char>(value>>(8*i));
  hash.update(bytes.data(),bytes.size());
}

void hash_cpp_int(Sha256& hash,const cpp_int& value) {
  const unsigned char sign=value<0?1:0;hash.update(&sign,1);
  std::vector<unsigned char> bytes;
  export_bits(abs_cpp(value),std::back_inserter(bytes),8,false);
  hash_u64(hash,bytes.size());
  if(!bytes.empty())hash.update(bytes.data(),bytes.size());
}

std::uint64_t evidence_regular_bytes(const fs::path& directory) {
  require(fs::is_directory(directory),"evidence directory missing");
  std::uint64_t total=0;
  for(const auto& entry:fs::recursive_directory_iterator(directory)){
    const auto status=entry.symlink_status();
    require(!fs::is_symlink(status),"evidence symlink forbidden");
    if(!fs::is_regular_file(status))continue;
    require(fs::hard_link_count(entry.path())==1,"evidence hard link forbidden");
    struct stat st{};require(::stat(entry.path().c_str(),&st)==0,"evidence stat");
    require(st.st_size==0||std::uint64_t(st.st_blocks)*512>=std::uint64_t(st.st_size),
            "sparse evidence file forbidden");
    require(std::uint64_t(st.st_size)<=AGGREGATE_CAP-total,"evidence byte overflow");
    total+=std::uint64_t(st.st_size);
  }
  return total;
}

fs::path checked_evidence_path(const fs::path& directory,const fs::path& path) {
  require(path.is_absolute(),"evidence path must be absolute");
  const fs::path base=fs::canonical(directory);
  const fs::path parent=fs::canonical(path.parent_path());
  const fs::path relative=fs::relative(parent,base);
  require(!relative.empty()&&*relative.begin()!="..","evidence path outside evidence directory");
  if(fs::exists(path)){
    require(fs::is_regular_file(path)&&!fs::is_symlink(path),"bad evidence target");
    require(fs::hard_link_count(path)==1,"evidence target hard link");
  }
  return path;
}

void checked_write_file(const fs::path& directory,const fs::path& path,
                        const std::string& bytes) {
  checked_evidence_path(directory,path);
  const std::uint64_t before=evidence_regular_bytes(directory);
  const std::uint64_t old=fs::exists(path)?fs::file_size(path):0;
  require(before>=old&&before-old<=ORDINARY_WRITER_CAP&&
          bytes.size()<=ORDINARY_WRITER_CAP-(before-old),
          "ordinary writer aggregate cap");
  std::ofstream out(path,std::ios::binary|std::ios::trunc);
  require(bool(out),"open checked output");out.write(bytes.data(),bytes.size());
  require(bool(out),"checked output write");out.close();require(bool(out),"checked output close");
  require(fs::file_size(path)==bytes.size(),"checked output size");
  require(evidence_regular_bytes(directory)==before-old+bytes.size(),
          "checked writer ledger mismatch");
}

void checked_truncate_file(const fs::path& directory,const fs::path& path) {
  checked_evidence_path(directory,path);require(fs::exists(path),"truncate target missing");
  const auto before=evidence_regular_bytes(directory),old=fs::file_size(path);
  std::ofstream out(path,std::ios::binary|std::ios::trunc);
  require(bool(out),"open checked truncate");out.close();require(bool(out),"close checked truncate");
  require(fs::file_size(path)==0&&evidence_regular_bytes(directory)==before-old,
          "checked truncate ledger");
}

struct GrammarMeasurement {
  u64 nanoseconds=0;
  GrammarStats stats;
  std::size_t final_count=0,bytes=0;
  std::string digest;
};

GrammarMeasurement measure_grammar_once() {
  GrammarMeasurement measured;const u64 start=steady_nanoseconds();
  {
    Grammar grammar=build_grammar();
    measured.stats=grammar.stats;measured.final_count=grammar.eval_order.size();
    measured.bytes=grammar.serialized.size();measured.digest=sha256_bytes(grammar.serialized);
  }
  measured.nanoseconds=steady_nanoseconds()-start;
  return measured;
}

struct StressWitness {
  cpp_int N;
  u64 t=0,ticket=0,family=0;
  cpp_int abs_ticket,proper_factor;
  bool operator<(const StressWitness& other)const{
    return std::tie(N,t,ticket,family,abs_ticket,proper_factor)<
           std::tie(other.N,other.t,other.ticket,other.family,
                    other.abs_ticket,other.proper_factor);
  }
};

struct BoundedWitnessHeap {
  std::size_t cap=0,replacements=0;
  std::priority_queue<StressWitness> heap;
  explicit BoundedWitnessHeap(std::size_t c=0):cap(c){}
  void insert(const StressWitness& witness){
    if(heap.size()<cap){heap.push(witness);return;}
    if(witness<heap.top()){heap.pop();heap.push(witness);++replacements;}
  }
};

struct MaxWorkerResult {
  u64 tail_divisions=0,value_checks=0,primitive_maps=0;
  u64 canonicalizations=0,selector_updates=0,tickets=0;
  u64 replacements4=0,replacements16=0;
  std::string digest;
};

MaxWorkerResult maximum_worker(unsigned round,unsigned worker,unsigned workers,
                               const std::vector<cpp_int>& fib,std::size_t k) {
  constexpr int B=1216;
  const cpp_int Nstar("726921560194875913822899294212981087");
  constexpr u64 P=720575940379279399ULL,Q=1008806316530991113ULL;
  std::vector<u64> selector_aggregates(11128);
  std::vector<std::array<u64,6>> direct_aggregates(DIRECT_BANK);
  std::vector<BoundedWitnessHeap> heap4,heap16;
  heap4.reserve(DIRECT_BANK);heap16.reserve(DIRECT_BANK);
  for(std::size_t i=0;i<DIRECT_BANK;++i){heap4.emplace_back(4);heap16.emplace_back(16);}
  std::array<std::vector<cpp_int>,2> branch_values;
  for(auto& values:branch_values)values.resize(FINAL_ATTEMPTS);
  Sha256 hash;MaxWorkerResult result;
  for(unsigned ell=0;ell<8;++ell){
    deadline_check("maximum-work stage");
    const u64 stage_serial=((u64(round)*workers+worker)*8)+(7-ell);
    const u64 t_fixture=stage_serial+1;
    for(int s=0;s<14;++s){
      Tail tail=build_tail(s,fib[k-2*s],fib[k-2*s-1],false);
      require(tail.q.size()==9&&tail.x.size()==11&&tail.x[10]>0,
              "maximum-work tail depth");
      result.tail_divisions+=9;
      for(const auto& q:tail.q)hash_cpp_int(hash,q);
    }
    for(int a=0;a<2;++a)for(std::size_t i=0;i<FINAL_ATTEMPTS;++i){
      if((i&1023)==0)deadline_check("maximum-work primitive map");
      cpp_int magnitude=(cpp_int(1)<<(B-1))+2*(2*i+a)+1;
      cpp_int value=((a+i)&1)?-magnitude:magnitude;
      const std::size_t j=(i+7*a)%14;
      const cpp_int& G=fib[k-2*j];const cpp_int& H=fib[k-2*j-1];
      require(bitlength(magnitude)==B&&cap_ok(value,120),"maximum-work V cap");
      branch_values[a][i]=value;++result.value_checks;
      hash_cpp_int(hash,value);hash_u64(hash,value<G);
      const cpp_int add=value+G,product=value*H,gcd=gcd_abs(value,G);
      const cpp_int quotient=floor_divmod(value,G).q;
      const cpp_int remainder=floor_divmod(value,G).r;
      const cpp_int centered=centered_rem(value,G);
      for(const cpp_int* x:{&add,&product,&gcd,&quotient,&remainder,&centered}){
        hash_cpp_int(hash,*x);hash_u64(hash,cap_ok(*x,120));
      }
      ++result.primitive_maps;
    }
    const std::array<std::size_t,5> cuts{{0,444,1468,4540,5564}};
    for(int a=0;a<2;++a)for(int layer=0;layer<4;++layer){
      std::vector<std::pair<cpp_int,int>> ordered;
      ordered.reserve(cuts[layer+1]-cuts[layer]);
      for(std::size_t i=cuts[layer];i<cuts[layer+1];++i)
        ordered.emplace_back(branch_values[a][i],int(i));
      std::sort(ordered.begin(),ordered.end());
      for(const auto& item:ordered){hash_cpp_int(hash,item.first);hash_u64(hash,item.second);}
      ++result.canonicalizations;
    }
    for(std::size_t i=0;i<FINAL_ATTEMPTS;++i){
      const bool less=branch_values[0][i]<branch_values[1][i];
      const bool greater=branch_values[0][i]>branch_values[1][i];
      selector_aggregates[2*i]+=less?1:0;
      selector_aggregates[2*i+1]+=greater?1:0;
      hash_u64(hash,less?0:1);hash_u64(hash,greater?0:1);
      result.selector_updates+=2;
    }
    for(std::size_t family=0;family<DIRECT_BANK;++family)for(u64 ticket=0;ticket<4;++ticket){
      const u64 v=1+4*(1024*stage_serial+family)+ticket;
      const cpp_int ticket_value=cpp_int(P)*(cpp_int(v)*Q+1);
      const cpp_int factor=gcd_abs(ticket_value,Nstar);
      require(factor==P&&factor>1&&factor<Nstar&&Nstar%factor==0,
              "maximum-work proper certificate");
      StressWitness witness{Nstar,t_fixture,ticket,family,abs_cpp(ticket_value),factor};
      heap4[family].insert(witness);heap16[family].insert(witness);
      ++direct_aggregates[family][5];++result.tickets;
      hash_cpp_int(hash,ticket_value);hash_cpp_int(hash,factor);
    }
  }
  for(u64 count:selector_aggregates)hash_u64(hash,count);
  for(const auto& counts:direct_aggregates)for(u64 count:counts)hash_u64(hash,count);
  for(std::size_t family=0;family<DIRECT_BANK;++family){
    result.replacements4+=heap4[family].replacements;
    result.replacements16+=heap16[family].replacements;
    auto consume=[&](auto heap){while(!heap.empty()){const auto& w=heap.top();
      hash_cpp_int(hash,w.N);hash_u64(hash,w.t);hash_u64(hash,w.ticket);
      hash_u64(hash,w.family);hash_cpp_int(hash,w.abs_ticket);
      hash_cpp_int(hash,w.proper_factor);heap.pop();}};
    consume(heap4[family].heap);consume(heap16[family].heap);
  }
  require(result.tail_divisions==14*9*8,"maximum-work tail count");
  require(result.value_checks==2*FINAL_ATTEMPTS*8,"maximum-work value count");
  require(result.primitive_maps==2*FINAL_ATTEMPTS*8,"maximum-work primitive count");
  require(result.canonicalizations==2*4*8,"maximum-work canonicalization count");
  require(result.selector_updates==11128*8,"maximum-work selector count");
  require(result.tickets==DIRECT_BANK*4*8,"maximum-work ticket count");
  require(result.replacements4>0&&result.replacements16>0,
          "maximum-work heap replacement pressure");
  result.digest=hash.final_hex();return result;
}

struct RoundMeasurement {
  u64 nanoseconds=0,vmhwm_bytes=0;
  MaxWorkerResult totals;
  std::string digest;
};

RoundMeasurement measure_maximum_round(unsigned round,unsigned workers) {
  require(workers==1||workers==2||workers==4||workers==8,"worker count");
  std::vector<cpp_int> fib{0,1};
  while(bitlength(fib.back())<=1216)fib.push_back(fib[fib.size()-1]+fib[fib.size()-2]);
  fib.pop_back();const std::size_t k=fib.size()-1;
  require(bitlength(fib[k])<=1216&&
          bitlength(fib[k]+fib[k-1])>1216,"largest Fibonacci fixture");
  RoundMeasurement measured;const u64 start=steady_nanoseconds();
  {
    std::string maximum_serialization_buffer(REGISTERED_OUTPUT_BOUND,'S');
    std::vector<MaxWorkerResult> results(workers);
    std::vector<std::thread> threads;threads.reserve(workers);
    for(unsigned worker=0;worker<workers;++worker)
      threads.emplace_back([&,worker]{results[worker]=maximum_worker(round,worker,workers,fib,k);});
    for(auto& thread:threads)thread.join();
    Sha256 combined;hash_u64(combined,maximum_serialization_buffer.size());
    combined.update(reinterpret_cast<const unsigned char*>(maximum_serialization_buffer.data()),1);
    combined.update(reinterpret_cast<const unsigned char*>(maximum_serialization_buffer.data()+maximum_serialization_buffer.size()-1),1);
    for(const auto& r:results){
      measured.totals.tail_divisions+=r.tail_divisions;
      measured.totals.value_checks+=r.value_checks;
      measured.totals.primitive_maps+=r.primitive_maps;
      measured.totals.canonicalizations+=r.canonicalizations;
      measured.totals.selector_updates+=r.selector_updates;
      measured.totals.tickets+=r.tickets;
      measured.totals.replacements4+=r.replacements4;
      measured.totals.replacements16+=r.replacements16;
      combined.update(r.digest);
    }
    measured.digest=combined.final_hex();
    measured.vmhwm_bytes=proc_status_kib("VmHWM")*1024;
  }
  measured.nanoseconds=steady_nanoseconds()-start;
  return measured;
}

std::string maximum_serialization_image() {
  struct Component {const char* name;std::size_t count,width;};
  static constexpr std::array<Component,13> components={{
    {"PRIMARY",41472,2048},{"CONTROL_ALIAS",42432,1024},
    {"DISCOVERY_SELECTOR",11128,8192},{"DISCOVERY_DIRECT",1024,8192},
    {"HELDOUT",256,8192},{"SELECTION",256,8192},{"BASELINES",1,8192},
    {"BASELINE_AGGREGATE",2016,1024},{"CERTIFICATE",5120,2048},
    {"COUNTEREXAMPLE",3840,2048},{"LEAD_GATE",256,1024},
    {"MANIFEST_SIDECAR",1024,8192},{"LOG",2048,8192}
  }};
  std::string image;image.reserve(REGISTERED_OUTPUT_BOUND);
  for(const auto& component:components)for(std::size_t i=0;i<component.count;++i){
    if((i&4095)==0)deadline_check("maximum serialization construction");
    std::string record(component.width,'9');
    const std::string prefix=std::string(component.name)+"\t"+std::to_string(i)+"\t";
    require(prefix.size()+1<=record.size(),"serialization record prefix");
    std::copy(prefix.begin(),prefix.end(),record.begin());record.back()='\n';image+=record;
  }
  require(image.size()==REGISTERED_OUTPUT_BOUND,"registered serialization image bytes");
  return image;
}

void write_serialization_fixture(const fs::path& directory,const fs::path& path) {
  const std::string image=maximum_serialization_image();
  checked_write_file(directory,path,image);
  require(fs::file_size(path)==REGISTERED_OUTPUT_BOUND,"serialization fixture size");
  std::cout<<"serialization_bytes\t"<<image.size()<<"\nserialization_sha256\t"
           <<sha256_bytes(image)<<'\n';
}

void write_splitmix_stream(const fs::path& directory,const fs::path& path) {
  constexpr std::size_t size=67108864;
  std::string bytes(size,'\0');u64 state=0xF2695A17C0A0B17EULL;
  for(std::size_t i=0;i<size;i+=8){if((i&((1U<<20)-1))==0)deadline_check("SplitMix stream");state=splitmix64(state);
    for(int j=0;j<8;++j)bytes[i+j]=char(static_cast<unsigned char>(state>>(8*j)));}
  checked_write_file(directory,path,bytes);
  std::cout<<"stream_bytes\t"<<bytes.size()<<"\nstream_sha256\t"
           <<sha256_bytes(bytes)<<'\n';
}

std::map<std::string,u64> read_metric_map(const std::string& path) {
  std::ifstream in(path);require(bool(in),"open gate metrics");
  std::map<std::string,u64> values;std::string line;
  while(std::getline(in,line)){
    const auto tab=line.find('\t');require(tab!=std::string::npos,"gate metric schema");
    const std::string key=line.substr(0,tab),text=line.substr(tab+1);
    require(!key.empty()&&!text.empty()&&text.find_first_not_of("0123456789")==std::string::npos,
            "gate metric integer");
    require(values.emplace(key,std::stoull(text)).second,"duplicate gate metric");
  }
  return values;
}

u64 ceil_ratio_u128(u128 numerator,u64 denominator) {
  return static_cast<u64>((numerator+denominator-1)/denominator);
}

void evaluate_preflight_gate(const std::string& input,u64 Egate,
                             const fs::path& directory,const fs::path& output) {
  auto m=read_metric_map(input);auto need=[&](const std::string& key)->u64{
    auto it=m.find(key);require(it!=m.end(),"missing gate metric "+key);return it->second;};
  const u64 W=need("workers");require(W==1||W==2||W==4||W==8,"gate workers");
  std::array<u64,7> G{},S{},Z{};std::array<u64,4> R{};
  for(int i=0;i<7;++i){G[i]=need("G"+std::to_string(i+1)+"_ns");S[i]=need("S"+std::to_string(i+1)+"_ns");Z[i]=need("Z"+std::to_string(i+1)+"_ns");}
  for(int i=0;i<4;++i)R[i]=need("R"+std::to_string(i+1)+"_ns");
  auto sum=[](const auto& array){return std::accumulate(array.begin(),array.end(),u64(0));};
  const u64 Graw=sum(G),Rraw=sum(R),Sraw=sum(S),Zraw=sum(Z);
  const u64 Gprod=*std::max_element(G.begin()+1,G.end());
  const u64 Rprod=*std::max_element(R.begin()+1,R.end());
  const u64 Sprod=*std::max_element(S.begin()+1,S.end());
  const u64 Zprod=*std::max_element(Z.begin()+1,Z.end());
  const u64 batches=(41472+8*W-1)/(8*W);
  const u64 eval_forecast=ceil_ratio_u128(u128(batches)*Rprod*4,3);
  const u64 zip_chunks=(REGISTERED_OUTPUT_BOUND+67108864-1)/67108864;
  const u64 zip_forecast=ceil_ratio_u128(u128(zip_chunks)*Zprod*5,4);
  const u64 raw=Graw+Rraw+Sraw+Zraw;
  require(Egate>=raw,"negative E0");const u64 E0=Egate-raw;
  const u64 production=Gprod+eval_forecast+Sprod+zip_forecast;
  const u64 projected=E0+raw+production;
  const u64 cgroup=need("cgroup_memory_peak_bytes");
  const u64 vmhwm=need("process_vmhwm_bytes");
  const u64 time_rss=need("time_maxrss_bytes");
  const u64 memory=std::max({cgroup,vmhwm,time_rss});
  const u64 memory_projected=ceil_ratio_u128(u128(5)*memory,4);
  const u64 rss_difference=vmhwm>time_rss?vmhwm-time_rss:time_rss-vmhwm;
  const bool pass=projected<=10800ULL*1000000000ULL&&
      memory_projected<=MEMORY_MAX_BYTES&&rss_difference<=67108864ULL&&
      need("registered_serialization_bytes")==REGISTERED_OUTPUT_BOUND&&
      need("evidence_regular_bytes")<=AGGREGATE_CAP&&need("du_bytes")<=AGGREGATE_CAP&&
      need("free_disk_bytes")>=5ULL*1024*1024*1024;
  std::ostringstream report;
  auto line=[&](const std::string& k,u64 v){report<<k<<'\t'<<v<<'\n';};
  line("pass",pass?1:0);line("workers",W);line("G_raw_ns",Graw);line("R_raw_ns",Rraw);
  line("S_raw_ns",Sraw);line("Z_raw_ns",Zraw);line("E_gate_ns",Egate);line("E_0_ns",E0);
  line("G_prod_ns",Gprod);line("R_prod_ns",Rprod);line("S_prod_ns",Sprod);line("Z_prod_ns",Zprod);
  line("evaluation_batches",batches);line("T_eval_forecast_ns",eval_forecast);
  line("compression_chunks",zip_chunks);line("T_zip_forecast_ns",zip_forecast);
  line("T_production_forecast_ns",production);line("readiness_total_ns",projected);
  line("readiness_limit_ns",10800ULL*1000000000ULL);line("cgroup_memory_peak_bytes",cgroup);
  line("process_vmhwm_bytes",vmhwm);line("time_maxrss_bytes",time_rss);
  line("rss_difference_bytes",rss_difference);line("memory_M_bytes",memory);
  line("memory_5_over_4_bytes",memory_projected);line("memory_limit_bytes",MEMORY_MAX_BYTES);
  line("registered_output_bound",REGISTERED_OUTPUT_BOUND);line("aggregate_cap",AGGREGATE_CAP);
  line("ordinary_writer_cap",ORDINARY_WRITER_CAP);line("failure_reserve",FAILURE_RESERVE);
  line("rlimit_as_bytes",RLIMIT_AS_BYTES);line("rlimit_fsize_bytes",RLIMIT_FSIZE_BYTES);
  line("primary_moduli",2176);line("primary_stage_rows",41472);
  line("discovery_direct_ticket_cap",44040192);line("heldout_direct_ticket_cap",7864320);
  line("total_direct_ticket_cap",51904512);line("child_factorizations",0);
  line("ordinary_rows",1632);line("ordinary_pair_attempt_cap",417792);
  line("ordinary_prime_word_cap",54760833024ULL);line("safe_candidate_cap",48000000);
  line("safe_primality_test_cap",96000000);line("safe_pair_attempt_cap",2400000);
  line("consecutive_odd_candidate_cap",2097088);
  checked_write_file(directory,output,report.str());
  require(pass,"preflight readiness gate");
}

u64 corpus_word(const std::array<u64,7>& fields) {
  u64 h=CORPUS_SEED;
  for(u64 field:fields)h=splitmix64(h^splitmix64(field));
  return h;
}

u64 fold_corpus_fields(std::initializer_list<u64> fields) {
  u64 h=CORPUS_SEED;for(u64 field:fields)h=splitmix64(h^splitmix64(field));return h;
}

u64 odd_from_word(u64 word,u64 low,u64 high) {
  const u64 first=low|(u64(1));require(first<=high,"empty odd interval");
  const u64 count=(high-first)/2+1;return first+2*(word%count);
}

bool first_fermat_control(const cpp_int& N) {
  cpp_int A=isqrt(N);if(A*A<N)++A;cpp_int root;
  const cpp_int D=A*A-N;
  return is_square(D,&root)&&A-root>1&&A-root<N&&N%(A-root)==0;
}

struct GenerationCell {
  int phase=0,factor_bits=0,shape=0,requested=0,retained=0;
  u64 pair_attempts=0,prime_candidates=0,safe_candidates=0;
  u64 safe_primality_tests=0,safe_pair_attempts=0;
  u64 fermat_exclusions=0,duplicates=0;
  std::string modulus_digest;
};

struct ModulusRecord {
  int phase=0,factor_bits=0,shape=0,row_serial=0;
  u64 p=0,q=0;
  cpp_int N;
};

struct Cohort {
  std::vector<ModulusRecord> moduli;
  std::vector<GenerationCell> cells;
};

std::optional<u64> request_prime(int phase,int factor_bits,int shape,u64 row_serial,
                                 u64 pair_attempt,u64 role,u64 low,u64 high,
                                 u64& candidate_counter) {
  for(u64 attempt=0;attempt<65536;++attempt){
    deadline_check("ordinary prime request");++candidate_counter;
    const u64 word=corpus_word({u64(phase),u64(factor_bits),u64(shape),row_serial,
                                pair_attempt,role,attempt});
    const u64 candidate=odd_from_word(word,low,high);
    if(is_prime64(candidate))return candidate;
  }
  return std::nullopt;
}

Cohort generate_primary_cohort(int phase) {
  require(phase==0||phase==1,"primary phase");
  static const std::array<int,7> discovery_bits{{16,20,24,28,32,36,40}};
  static const std::array<int,5> heldout_bits{{44,48,52,56,60}};
  const int count=phase==0?32:64;
  const int size_count=phase==0?7:5;
  Cohort cohort;std::set<cpp_int> seen;
  for(int size_index=0;size_index<size_count;++size_index){
    const int f=phase==0?discovery_bits[size_index]:heldout_bits[size_index];
    const u64 lower=u64(1)<<(f-1),upper=(u64(1)<<f)-1;
    for(int shape=0;shape<4;++shape){
      GenerationCell cell;cell.phase=phase;cell.factor_bits=f;cell.shape=shape;cell.requested=count;
      Sha256 cell_hash;
      if(shape<3){
        for(int row=0;row<count;++row){
          bool retained=false;
          for(u64 pair_attempt=0;pair_attempt<256&&!retained;++pair_attempt){
            deadline_check("ordinary pair generation");++cell.pair_attempts;
            u64 p_low=lower,p_high=upper;
            if(shape==2)p_high=static_cast<u64>((u128(upper)*32)/63);
            auto p=request_prime(phase,f,shape,row,pair_attempt,0,p_low,p_high,
                                 cell.prime_candidates);
            if(!p)fail("ordinary p candidate cap phase="+std::to_string(phase)+
                       " bits="+std::to_string(f)+" shape="+std::to_string(shape));
            u64 q_low=lower,q_high=upper;
            if(shape==1){q_low=*p+2;q_high=std::min(upper,static_cast<u64>((u128(33)*(*p))/32));}
            if(shape==2){q_low=std::max(lower,static_cast<u64>((u128(63)*(*p)+31)/32));
                         q_high=std::min(upper,2*(*p)-1);}
            if(q_low>q_high)continue;
            auto q=request_prime(phase,f,shape,row,pair_attempt,1,q_low,q_high,
                                 cell.prime_candidates);
            if(!q)fail("ordinary q candidate cap phase="+std::to_string(phase)+
                       " bits="+std::to_string(f)+" shape="+std::to_string(shape));
            if(!(*p<*q&&*q<2*(*p)))continue;
            const cpp_int N=cpp_int(*p)*(*q);
            if(bitlength(N)!=std::size_t(2*f))continue;
            if(first_fermat_control(N)){++cell.fermat_exclusions;continue;}
            if(!seen.insert(N).second){++cell.duplicates;continue;}
            cohort.moduli.push_back({phase,f,shape,row,*p,*q,N});
            hash_cpp_int(cell_hash,N);++cell.retained;retained=true;
          }
          require(retained,"ordinary pair-attempt cap phase="+std::to_string(phase)+
                  " bits="+std::to_string(f)+" shape="+std::to_string(shape)+
                  " row="+std::to_string(row));
        }
      }else{
        const int pool_size=2*count+32;std::vector<u64> pool;pool.reserve(pool_size);
        std::set<u64> pool_seen;
        for(int pool_index=0;pool_index<pool_size;++pool_index){
          bool filled=false;
          for(u64 attempt=0;!filled;++attempt){
            deadline_check("safe-prime pool");
            require(cell.safe_candidates<4000000,"safe-prime candidate cap");
            ++cell.safe_candidates;
            const u64 word=corpus_word({u64(phase),u64(f),u64(shape),u64(pool_index),
                                        0,2,attempt});
            const u64 s=odd_from_word(word,u64(1)<<(f-2),(u64(1)<<(f-1))-1);
            ++cell.safe_primality_tests;if(!is_prime64(s))continue;
            const u64 z=2*s+1;++cell.safe_primality_tests;
            if(bitlength(cpp_int(z))!=std::size_t(f)||!is_prime64(z))continue;
            if(!pool_seen.insert(z).second){++cell.duplicates;continue;}
            pool.push_back(z);filled=true;
          }
        }
        const u64 cell_tag=fold_corpus_fields({u64(phase),u64(f),u64(shape)});
        std::sort(pool.begin(),pool.end(),[&](u64 x,u64 y){
          return std::make_pair(splitmix64(cell_tag^x),x)<
                 std::make_pair(splitmix64(cell_tag^y),y);});
        u64 total_pair_attempts=0;
        for(int row=0;row<count;++row){
          bool retained=false;
          for(u64 pair_attempt=0;!retained;++pair_attempt){
            deadline_check("safe-prime pairing");
            require(total_pair_attempts<200000,"safe-pair attempt cap");
            ++total_pair_attempts;++cell.safe_pair_attempts;
            const u64 wi=corpus_word({u64(phase),u64(f),u64(shape),u64(row),pair_attempt,3,0});
            const u64 wj=corpus_word({u64(phase),u64(f),u64(shape),u64(row),pair_attempt,3,1});
            const std::size_t i=wi%pool.size(),j=wj%pool.size();if(i==j)continue;
            const u64 p=std::min(pool[i],pool[j]),q=std::max(pool[i],pool[j]);
            if(!(p<q&&q<2*p))continue;const cpp_int N=cpp_int(p)*q;
            if(bitlength(N)!=std::size_t(2*f))continue;
            if(first_fermat_control(N)){++cell.fermat_exclusions;continue;}
            if(!seen.insert(N).second){++cell.duplicates;continue;}
            cohort.moduli.push_back({phase,f,shape,row,p,q,N});
            hash_cpp_int(cell_hash,N);++cell.retained;retained=true;
          }
        }
      }
      require(cell.retained==count,"primary cell retained count");
      cell.modulus_digest=cell_hash.final_hex();cohort.cells.push_back(cell);
    }
  }
  const std::size_t expected=phase==0?896:1280;
  require(cohort.moduli.size()==expected,"primary cohort modulus count");
  return cohort;
}

int cell_index(int phase,int factor_bits,int shape) {
  static const std::array<int,7> d{{16,20,24,28,32,36,40}};
  static const std::array<int,5> h{{44,48,52,56,60}};
  if(phase==0){auto it=std::find(d.begin(),d.end(),factor_bits);require(it!=d.end(),"discovery cell bits");return int(it-d.begin())*4+shape;}
  auto it=std::find(h.begin(),h.end(),factor_bits);require(it!=h.end(),"heldout cell bits");return int(it-h.begin())*4+shape;
}

std::string histogram_text(const std::array<u64,10>& histogram) {
  std::ostringstream out;for(std::size_t i=0;i<histogram.size();++i){if(i)out<<',';out<<histogram[i];}return out.str();
}

std::string tail_alias_digest(const BranchPublic& branch) {
  std::ostringstream bytes;
  for(const auto& tail:branch.tails)bytes<<tail.tail_id<<'\t'<<tail.zero_gap<<'\t'
      <<tail.alias_id<<'\t'<<tail.serialization<<'\n';
  return sha256_bytes(bytes.str());
}

std::string tail_alias_ids(const BranchPublic& branch) {
  std::ostringstream out;for(int i=0;i<14;++i){if(i)out<<',';
    if(branch.tails[i].zero_gap)out<<"NA";else out<<branch.tails[i].alias_id;}return out.str();
}

std::string public_corpus_row(const ModulusRecord& modulus,const RowPublic& row,
                              const EvaluatedRow& evaluated) {
  const auto& s=row.stage;std::vector<std::string> f={
    std::to_string(modulus.phase),std::to_string(modulus.factor_bits),
    std::to_string(modulus.shape),std::to_string(modulus.row_serial),dec(s.N),
    std::to_string(s.n),std::to_string(s.t_terminal),std::to_string(s.t),
    std::to_string(s.m),std::to_string(s.u),std::to_string(s.r),std::to_string(s.c),
    dec(s.K),std::to_string(s.delta),std::to_string(s.kappa),root_mask(row.branch[0]),
    root_mask(row.branch[1]),packed_reason_digest(row.branch[0]),
    packed_reason_digest(row.branch[1]),histogram_text(reason_histogram(row.branch[0])),
    histogram_text(reason_histogram(row.branch[1])),tail_alias_digest(row.branch[0]),
    tail_alias_digest(row.branch[1]),tail_alias_ids(row.branch[0]),tail_alias_ids(row.branch[1]),
    evaluation_reason_digest(evaluated.branch[0]),evaluation_reason_digest(evaluated.branch[1]),
    evaluation_reason_histogram(evaluated.branch[0]),evaluation_reason_histogram(evaluated.branch[1]),
    evaluation_alias_digest(evaluated.branch[0]),evaluation_alias_digest(evaluated.branch[1]),
    evaluation_invalid_mask_digest(evaluated.branch[0]),
    evaluation_invalid_mask_digest(evaluated.branch[1]),
    s.fermat.proper?"1":"0"};
  const std::string record=join_tsv(f);require(record.size()<=2048,"primary corpus record bound");return record;
}

struct PublicPass {
  std::string corpus_bytes,corpus_digest;
  std::vector<unsigned char> collision;
  std::size_t stage_rows=0;
};

PublicPass run_public_pass(const Cohort& cohort,const Grammar& grammar,unsigned workers) {
  require(workers==1||workers==2||workers==4||workers==8,"public-pass workers");
  std::vector<std::string> modulus_rows(cohort.moduli.size());
  std::vector<std::vector<unsigned char>> local_collision(
      workers,std::vector<unsigned char>(grammar.eval_order.size()));
  std::vector<std::size_t> local_stages(workers);std::atomic<std::size_t> next{0};
  std::vector<std::thread> threads;
  for(unsigned worker=0;worker<workers;++worker)threads.emplace_back([&,worker]{
    for(;;){const std::size_t index=next.fetch_add(1);if(index>=cohort.moduli.size())break;
      deadline_check("public corpus pass");const auto& modulus=cohort.moduli[index];
      std::string rows;const int terminal=(int(bitlength(modulus.N))-1)/4;
      for(int t=1;t<terminal;++t){
        const u64 m=u64(1)<<t,u=inverse_pow2(modulus.p%m,m);
        RowPublic row=build_row_public(analyze_public(modulus.N,t,u));
        EvaluatedRow evaluated=evaluate_all(grammar,row);rows+=public_corpus_row(modulus,row,evaluated);
        for(std::size_t i=0;i<grammar.eval_order.size();++i)for(int a=0;a<2;++a){
          const std::uint16_t mask=evaluated.branch[a][i].reason_mask;
          if(mask&((1U<<TAIL_STATE_ALIAS)|(1U<<EQUAL_OPERAND_VALUE)|(1U<<ROW_CONTROL_EQUALITY)))
            local_collision[worker][i]=1;
        }
        ++local_stages[worker];
      }
      modulus_rows[index]=std::move(rows);
    }
  });
  for(auto& thread:threads)thread.join();
  PublicPass pass;
  pass.corpus_bytes="phase\tfactor_bits\tshape_id\trow_serial\tN\tn\tt_terminal\tt\tm\tu\tr\tc\tK\tdelta\tkappa\troot_valid_mask_a0\troot_valid_mask_a1\troot_reason_sha256_a0\troot_reason_sha256_a1\troot_reason_histogram_a0\troot_reason_histogram_a1\ttail_alias_sha256_a0\ttail_alias_sha256_a1\ttail_alias_ids_a0\ttail_alias_ids_a1\texpression_reason_sha256_a0\texpression_reason_sha256_a1\texpression_reason_histogram_a0\texpression_reason_histogram_a1\tvalue_alias_sha256_a0\tvalue_alias_sha256_a1\tinvalid_reason_mask_sha256_a0\tinvalid_reason_mask_sha256_a1\tfirst_fermat_control\n";
  for(const auto& rows:modulus_rows)pass.corpus_bytes+=rows;
  pass.collision.assign(grammar.eval_order.size(),0);
  for(unsigned worker=0;worker<workers;++worker)for(std::size_t i=0;i<pass.collision.size();++i)
    pass.collision[i]|=local_collision[worker][i];
  pass.stage_rows=std::accumulate(local_stages.begin(),local_stages.end(),std::size_t(0));
  const std::size_t expected=cohort.moduli.front().phase==0?10752:30720;
  require(pass.stage_rows==expected,"primary stage row count");
  pass.corpus_digest=sha256_bytes(pass.corpus_bytes);return pass;
}

std::string generation_manifest_rows(const Cohort& cohort) {
  std::ostringstream out;
  for(const auto& c:cohort.cells){
    out<<"GENERATION_CELL\t"<<c.phase<<'\t'<<c.factor_bits<<'\t'<<c.shape<<'\t'
       <<c.requested<<'\t'<<c.retained<<'\t'<<c.pair_attempts<<'\t'
       <<c.prime_candidates<<'\t'<<c.safe_candidates<<'\t'
       <<c.safe_primality_tests<<'\t'<<c.safe_pair_attempts<<'\t'
       <<c.fermat_exclusions<<'\t'<<c.duplicates<<'\t'<<c.modulus_digest<<'\n';
  }
  return out.str();
}

struct CellStats {
  std::uint32_t rows=0,n0=0,n1=0,valid=0,invalid=0,c0=0,c1=0,errors=0;
  std::uint16_t invalid_reason_mask=0;
  std::array<std::uint32_t,10> invalid_reason_counts{};
  void add(const CellStats& other){
    rows+=other.rows;n0+=other.n0;n1+=other.n1;valid+=other.valid;
    invalid+=other.invalid;c0+=other.c0;c1+=other.c1;errors+=other.errors;
    invalid_reason_mask|=other.invalid_reason_mask;
    for(int i=0;i<10;++i)invalid_reason_counts[i]+=other.invalid_reason_counts[i];
  }
};

struct Rational {
  u64 numerator=0,denominator=1;
};

Rational balanced_accuracy(u64 n0,u64 n1,u64 c0,u64 c1) {
  require(n0>0&&n1>0,"nonempty label classes");
  u64 numerator=c0*n1+c1*n0,denominator=2*n0*n1;
  const u64 divisor=std::gcd(numerator,denominator);
  return {numerator/divisor,denominator/divisor};
}

Rational balanced_accuracy(const CellStats& stats) {
  return balanced_accuracy(stats.n0,stats.n1,stats.c0,stats.c1);
}

int compare_rational(const Rational& x,const Rational& y) {
  const u128 left=u128(x.numerator)*y.denominator,right=u128(y.numerator)*x.denominator;
  return (left>right)-(left<right);
}

std::vector<std::shared_ptr<Node>> direct_bank_nodes(const Grammar& grammar) {
  require(grammar.syntax_order.size()>=DIRECT_BANK,"direct-bank population");
  auto nodes=grammar.syntax_order;
  std::sort(nodes.begin(),nodes.end(),[](const auto& x,const auto& y){
    const auto xkey=splitmix64(DIRECT_SEED^fnv1a64(x->syntax));
    const auto ykey=splitmix64(DIRECT_SEED^fnv1a64(y->syntax));
    return xkey!=ykey?xkey<ykey:x->syntax<y->syntax;
  });
  nodes.resize(DIRECT_BANK);return nodes;
}

std::array<int,42> baseline_predictions(const RowPublic& row) {
  const auto& s=row.stage;std::array<int,42> prediction{};
  prediction[0]=0;prediction[1]=1;prediction[2]=s.kappa;prediction[3]=1^s.kappa;
  prediction[4]=s.delta;prediction[5]=1^s.delta;
  prediction[6]=s.kappa^s.delta;prediction[7]=1^s.kappa^s.delta;
  const int bit_nt=int(((s.N>>s.t)&1).convert_to<unsigned>());
  const int bit_nt1=int(((s.N>>(s.t+1))&1).convert_to<unsigned>());
  const int bit_u=int((s.u>>(s.t-1))&1),parity=s.t&1;
  prediction[8]=bit_nt;prediction[9]=1^bit_nt;prediction[10]=bit_nt1;
  prediction[11]=1^bit_nt1;prediction[12]=bit_u;prediction[13]=1^bit_u;
  prediction[14]=parity;prediction[15]=1^parity;
  std::array<std::array<cpp_int,13>,2> scalar;
  for(int a=0;a<2;++a){
    const int b=a^s.delta;const cpp_int compatible=s.Z[z_index(a,b)];
    require(compatible%2==0,"F210 compatible quotient integrality");
    const cpp_int FK=compatible/2,FJ=s.Z[z_index(a,1-b)];
    const cpp_int FX=s.R[a],FY=s.C[b];
    const cpp_int larger=std::max(FK,FJ),smaller=std::min(FK,FJ);
    require(smaller>0,"F210 baseline divisor");const auto divided=floor_divmod(larger,smaller);
    scalar[a]={FK,FJ,cpp_int(bitlength(FK)),cpp_int(bitlength(FJ)),FK+FJ,
               std::min(FK,FJ),std::max(FK,FJ),FK*FJ,gcd_abs(FK,FJ),
               divided.q,divided.r,abs_cpp(FX-FY),FX+FY};
  }
  for(int feature=0;feature<13;++feature){
    prediction[16+2*feature]=scalar[1][feature]<scalar[0][feature]?1:0;
    prediction[17+2*feature]=scalar[0][feature]>scalar[1][feature]?0:1;
  }
  return prediction;
}

void update_cell(CellStats& stats,int label,const std::optional<int>& prediction,
                 Reason reason=VALID,std::uint16_t reason_mask=0) {
  ++stats.rows;if(label==0)++stats.n0;else ++stats.n1;
  if(!prediction){++stats.invalid;++stats.errors;
    if(reason!=VALID){if(reason_mask==0)reason_mask=std::uint16_t(1U<<reason);
      stats.invalid_reason_mask|=reason_mask;
      ++stats.invalid_reason_counts[reason];}return;}
  ++stats.valid;
  if(*prediction==label){if(label==0)++stats.c0;else ++stats.c1;}
  else ++stats.errors;
}

struct DiscoveryRuleAggregate {std::array<CellStats,28> cells{};};

struct DirectAggregate {
  u64 attempts=0,control_reintroduction=0,row_control_equality=0,invalid_value=0;
  u64 gcd_unit=0,gcd_full=0,gcd_proper=0;
  std::set<std::string> hit_moduli;
  std::set<int> hit_factor_sizes,hit_shapes;
  BoundedWitnessHeap certificates;
  explicit DirectAggregate(std::size_t certificate_cap=4):certificates(certificate_cap){}
  void merge(DirectAggregate& other){
    attempts+=other.attempts;control_reintroduction+=other.control_reintroduction;
    row_control_equality+=other.row_control_equality;invalid_value+=other.invalid_value;
    gcd_unit+=other.gcd_unit;gcd_full+=other.gcd_full;gcd_proper+=other.gcd_proper;
    hit_moduli.insert(other.hit_moduli.begin(),other.hit_moduli.end());
    hit_factor_sizes.insert(other.hit_factor_sizes.begin(),other.hit_factor_sizes.end());
    hit_shapes.insert(other.hit_shapes.begin(),other.hit_shapes.end());
    while(!other.certificates.heap.empty()){
      certificates.insert(other.certificates.heap.top());other.certificates.heap.pop();
    }
  }
  void check_partition()const{
    require(attempts==control_reintroduction+row_control_equality+invalid_value+
            gcd_unit+gcd_full+gcd_proper,"direct ticket partition");
  }
};

struct DiscoveryWorker {
  std::vector<DiscoveryRuleAggregate> rules;
  std::vector<DirectAggregate> direct;
  std::array<std::array<CellStats,28>,42> baselines{};
  DiscoveryWorker(std::size_t syntax_count):rules(2*syntax_count){
    direct.reserve(DIRECT_BANK);for(std::size_t i=0;i<DIRECT_BANK;++i)direct.emplace_back(4);
  }
};

struct DiscoveryAggregates {
  std::vector<DiscoveryRuleAggregate> rules;
  std::vector<DirectAggregate> direct;
  std::array<std::array<CellStats,28>,42> baselines{};
  DiscoveryAggregates(std::size_t syntax_count):rules(2*syntax_count){
    direct.reserve(DIRECT_BANK);for(std::size_t i=0;i<DIRECT_BANK;++i)direct.emplace_back(4);
  }
};

Reason required_branch_reason(const Eval& e0,const Eval& e1,int ticket) {
  if(ticket==0)return e0.valid?VALID:e0.reason;
  if(ticket==1)return e1.valid?VALID:e1.reason;
  if(e0.valid&&e1.valid)return VALID;
  if(!e0.valid&&!e1.valid)return min_reason(e0.reason,e1.reason);
  return e0.valid?e1.reason:e0.reason;
}

DiscoveryAggregates score_discovery(const Cohort& cohort,const Grammar& grammar,
                                    const std::vector<std::shared_ptr<Node>>& direct_nodes,
                                    unsigned workers) {
  std::vector<DiscoveryWorker> local;local.reserve(workers);
  for(unsigned w=0;w<workers;++w)local.emplace_back(grammar.eval_order.size());
  std::atomic<std::size_t> next{0};std::vector<std::thread> threads;
  for(unsigned worker=0;worker<workers;++worker)threads.emplace_back([&,worker]{
    auto& out=local[worker];
    for(;;){const std::size_t index=next.fetch_add(1);if(index>=cohort.moduli.size())break;
      deadline_check("discovery labelled scoring");const auto& modulus=cohort.moduli[index];
      const int cell=cell_index(0,modulus.factor_bits,modulus.shape);
      const int terminal=(int(bitlength(modulus.N))-1)/4;
      for(int t=1;t<terminal;++t){
        const u64 m=u64(1)<<t,u=inverse_pow2(modulus.p%m,m);
        RowPublic row=build_row_public(analyze_public(modulus.N,t,u));
        EvaluatedRow evaluated=evaluate_all(grammar,row);
        require((cpp_int(modulus.p)-row.stage.r)%m==0&&
                (cpp_int(modulus.q)-row.stage.c)%m==0,"hidden label divisibility");
        const int label_a=int((((cpp_int(modulus.p)-row.stage.r)/m)&1).convert_to<unsigned>());
        const int label_b=int((((cpp_int(modulus.q)-row.stage.c)/m)&1).convert_to<unsigned>());
        const u64 inverse2=inverse_pow2(modulus.p%(2*m),2*m);
        require(inverse2>=u&&(inverse2-u)%m==0,"hidden reciprocal label divisibility");
        const int label_e=int((inverse2-u)/m);
        require(label_b==(label_a^row.stage.delta)&&label_e==(label_a^row.stage.kappa),
                "hidden/public label conversion");
        for(std::size_t i=0;i<grammar.eval_order.size();++i){
          const auto& e0=evaluated.branch[0][i];const auto& e1=evaluated.branch[1][i];
          for(int orientation=0;orientation<2;++orientation){
            std::optional<int> prediction;Reason reason=VALID;
            if(e0.valid&&e1.valid){
              prediction=orientation==0?(e1.value<e0.value?1:0):(e0.value>e1.value?0:1);
              require(((*prediction^row.stage.kappa)==label_e)==(*prediction==label_a),
                      "selector coordinate agreement");
            }else reason=!e0.valid&&!e1.valid?min_reason(e0.reason,e1.reason):
                          (e0.valid?e1.reason:e0.reason);
            update_cell(out.rules[2*i+orientation].cells[cell],label_a,prediction,reason,
                        e0.reason_mask|e1.reason_mask);
          }
        }
        const auto baseline=baseline_predictions(row);
        for(int id=0;id<42;++id){
          require(((baseline[id]^row.stage.kappa)==label_e)==(baseline[id]==label_a),
                  "baseline coordinate agreement");
          update_cell(out.baselines[id][cell],label_a,baseline[id]);
        }
        for(std::size_t family=0;family<direct_nodes.size();++family){
          auto& aggregate=out.direct[family];const auto& node=*direct_nodes[family];
          const auto& e0=evaluated.branch[0][node.eval_index];
          const auto& e1=evaluated.branch[1][node.eval_index];
          for(int ticket=0;ticket<4;++ticket){
            ++aggregate.attempts;const Reason missing=required_branch_reason(e0,e1,ticket);
            if(missing!=VALID){++aggregate.invalid_value;continue;}
            if(static_ticket_control(direct_nodes[family],ticket,row.stage)){
              ++aggregate.control_reintroduction;continue;
            }
            cpp_int value=ticket==0?e0.value:ticket==1?e1.value:
                          ticket==2?e0.value-e1.value:e0.value+e1.value;
            if(is_row_control(row.controls,value)){++aggregate.row_control_equality;continue;}
            const cpp_int factor=gcd_abs(value,modulus.N);
            if(factor==1)++aggregate.gcd_unit;
            else if(factor==modulus.N)++aggregate.gcd_full;
            else{
              require(factor>1&&factor<modulus.N&&modulus.N%factor==0,
                      "discovery proper certificate");
              ++aggregate.gcd_proper;aggregate.hit_moduli.insert(dec(modulus.N));
              aggregate.hit_factor_sizes.insert(modulus.factor_bits);
              aggregate.hit_shapes.insert(modulus.shape);
              aggregate.certificates.insert({modulus.N,u64(t),u64(ticket),
                  u64(node.syntax_id),abs_cpp(value),factor});
            }
          }
        }
      }
    }
  });
  for(auto& thread:threads)thread.join();
  DiscoveryAggregates merged(grammar.eval_order.size());
  for(auto& worker:local){
    for(std::size_t r=0;r<merged.rules.size();++r)
      for(int c=0;c<28;++c)merged.rules[r].cells[c].add(worker.rules[r].cells[c]);
    for(std::size_t f=0;f<DIRECT_BANK;++f)merged.direct[f].merge(worker.direct[f]);
    for(int b=0;b<42;++b)for(int c=0;c<28;++c)
      merged.baselines[b][c].add(worker.baselines[b][c]);
  }
  for(auto& family:merged.direct){family.check_partition();require(family.attempts==10752*4,"discovery direct attempt count");}
  for(const auto& rule:merged.rules)for(const auto& cell:rule.cells)
    require(cell.n0>0&&cell.n1>0,"discovery cell label classes");
  return merged;
}

CellStats pool_discovery_cells(const std::array<CellStats,28>& cells,
                               const std::function<bool(int)>& include) {
  CellStats pooled;for(int i=0;i<28;++i)if(include(i))pooled.add(cells[i]);return pooled;
}

struct SelectorRankFields {
  u64 invalid_rows=0,exact_cells=0,errors=0;
  Rational minimum_shape,total;
};

SelectorRankFields selector_rank_fields(const DiscoveryRuleAggregate& aggregate) {
  SelectorRankFields fields;bool first=true;
  CellStats total_stats;
  for(const auto& cell:aggregate.cells){
    fields.invalid_rows+=cell.invalid;fields.errors+=cell.errors;
    if(cell.invalid==0&&cell.errors==0)++fields.exact_cells;total_stats.add(cell);
  }
  for(int shape=0;shape<4;++shape){
    const CellStats pooled=pool_discovery_cells(aggregate.cells,
                                                [=](int i){return i%4==shape;});
    const Rational accuracy=balanced_accuracy(pooled);
    if(first||compare_rational(accuracy,fields.minimum_shape)<0){fields.minimum_shape=accuracy;first=false;}
  }
  fields.total=balanced_accuracy(total_stats);return fields;
}

struct RankedSelector {
  std::shared_ptr<Node> node;
  int orientation=0;
  SelectorRankFields fields;
};

std::vector<RankedSelector> rank_discovery_selectors(
    const Grammar& grammar,const DiscoveryAggregates& aggregates,
    const std::vector<unsigned char>& collision) {
  std::vector<RankedSelector> ranked;
  for(const auto& node:grammar.eval_order)if(!collision[node->eval_index])
    for(int orientation=0;orientation<2;++orientation)
      ranked.push_back({node,orientation,
          selector_rank_fields(aggregates.rules[2*node->eval_index+orientation])});
  std::sort(ranked.begin(),ranked.end(),[](const auto& x,const auto& y){
    if(x.fields.invalid_rows!=y.fields.invalid_rows)return x.fields.invalid_rows<y.fields.invalid_rows;
    const int min_compare=compare_rational(x.fields.minimum_shape,y.fields.minimum_shape);
    if(min_compare)return min_compare>0;
    if(x.fields.exact_cells!=y.fields.exact_cells)return x.fields.exact_cells>y.fields.exact_cells;
    const int total_compare=compare_rational(x.fields.total,y.fields.total);
    if(total_compare)return total_compare>0;
    if(x.fields.errors!=y.fields.errors)return x.fields.errors<y.fields.errors;
    if(x.node->typed_layer!=y.node->typed_layer)return x.node->typed_layer<y.node->typed_layer;
    if(x.node->node_count!=y.node->node_count)return x.node->node_count<y.node->node_count;
    if(x.node->syntax!=y.node->syntax)return x.node->syntax<y.node->syntax;
    return x.orientation<y.orientation;
  });
  return ranked;
}

struct RankedDirect {
  std::size_t family=0;
  std::shared_ptr<Node> node;
};

std::vector<RankedDirect> rank_discovery_direct(
    const std::vector<std::shared_ptr<Node>>& nodes,
    const std::vector<DirectAggregate>& aggregates,
    const std::vector<unsigned char>& collision) {
  std::vector<RankedDirect> ranked;
  for(std::size_t family=0;family<nodes.size();++family)
    if(!collision[nodes[family]->eval_index])ranked.push_back({family,nodes[family]});
  std::sort(ranked.begin(),ranked.end(),[&](const auto& x,const auto& y){
    const auto& a=aggregates[x.family];const auto& b=aggregates[y.family];
    if(a.hit_moduli.size()!=b.hit_moduli.size())return a.hit_moduli.size()>b.hit_moduli.size();
    if(a.hit_factor_sizes.size()!=b.hit_factor_sizes.size())return a.hit_factor_sizes.size()>b.hit_factor_sizes.size();
    if(a.hit_shapes.size()!=b.hit_shapes.size())return a.hit_shapes.size()>b.hit_shapes.size();
    if(a.gcd_proper!=b.gcd_proper)return a.gcd_proper>b.gcd_proper;
    const u64 ai=a.control_reintroduction+a.row_control_equality+a.invalid_value;
    const u64 bi=b.control_reintroduction+b.row_control_equality+b.invalid_value;
    if(ai!=bi)return ai<bi;
    if(x.node->typed_layer!=y.node->typed_layer)return x.node->typed_layer<y.node->typed_layer;
    if(x.node->node_count!=y.node->node_count)return x.node->node_count<y.node->node_count;
    return x.node->syntax<y.node->syntax;
  });
  return ranked;
}

std::string cell_stats_text(const CellStats& cell) {
  const Rational accuracy=balanced_accuracy(cell);
  std::ostringstream out;out<<cell.rows<<','<<cell.n0<<','<<cell.n1<<','<<cell.valid
    <<','<<cell.invalid<<','<<cell.c0<<','<<cell.c1<<','<<cell.errors<<','
    <<accuracy.numerator<<'/'<<accuracy.denominator<<','<<std::hex<<std::setfill('0')
    <<std::setw(4)<<cell.invalid_reason_mask<<std::dec<<',';
  for(int reason=0;reason<10;++reason){if(reason)out<<':';out<<cell.invalid_reason_counts[reason];}
  return out.str();
}

std::string discovery_rules_bytes(const Grammar& grammar,
                                  const DiscoveryAggregates& aggregates,
                                  const std::vector<std::shared_ptr<Node>>& direct_nodes,
                                  const std::vector<unsigned char>& collision,
                                  const std::vector<RankedSelector>& selectors,
                                  const std::vector<RankedDirect>& direct_ranked) {
  std::vector<long long> selector_rank(2*grammar.eval_order.size(),-1);
  for(std::size_t rank=0;rank<selectors.size();++rank)
    selector_rank[2*selectors[rank].node->eval_index+selectors[rank].orientation]=
        static_cast<long long>(rank);
  std::vector<long long> direct_position(DIRECT_BANK,-1);
  for(std::size_t rank=0;rank<direct_ranked.size();++rank)direct_position[direct_ranked[rank].family]=rank;
  std::ostringstream out;
  out<<"record_type\trank\tsyntax_id\torientation_id\tgrammar_attempt_id\ttyped_layer\tnode_count\tdiscovery_public_collision\tinvalid_rows\tminimum_shape_accuracy\texact_cells\ttotal_accuracy\terrors\tticket_attempts\tcontrol_reintroduction\trow_control_equality\tinvalid_value\tgcd_unit\tgcd_full\tgcd_proper\thit_moduli\thit_factor_sizes\thit_shapes\tcells\tcanonical_syntax\n";
  for(const auto& node:grammar.syntax_order)for(int orientation=0;orientation<2;++orientation){
    const auto& aggregate=aggregates.rules[2*node->eval_index+orientation];
    const auto fields=selector_rank_fields(aggregate);std::ostringstream cells;
    for(int c=0;c<28;++c){if(c)cells<<';';cells<<cell_stats_text(aggregate.cells[c]);}
    std::vector<std::string> row={"SELECTOR",
      selector_rank[2*node->eval_index+orientation]<0?"NA":std::to_string(selector_rank[2*node->eval_index+orientation]),
      std::to_string(node->syntax_id),std::to_string(orientation),std::to_string(node->attempt_id),
      std::to_string(node->typed_layer),std::to_string(node->node_count),
      collision[node->eval_index]?"1":"0",std::to_string(fields.invalid_rows),
      std::to_string(fields.minimum_shape.numerator)+"/"+std::to_string(fields.minimum_shape.denominator),
      std::to_string(fields.exact_cells),
      std::to_string(fields.total.numerator)+"/"+std::to_string(fields.total.denominator),
      std::to_string(fields.errors),"NA","NA","NA","NA","NA","NA","NA","NA","NA","NA",
      cells.str(),node->syntax};
    const std::string record=join_tsv(row);require(record.size()<=8192,"discovery selector record bound");out<<record;
  }
  for(std::size_t family=0;family<direct_nodes.size();++family){
    const auto& node=direct_nodes[family];const auto& a=aggregates.direct[family];
    std::vector<std::string> row={"DIRECT",direct_position[family]<0?"NA":std::to_string(direct_position[family]),
      std::to_string(node->syntax_id),"NA",std::to_string(node->attempt_id),
      std::to_string(node->typed_layer),std::to_string(node->node_count),
      collision[node->eval_index]?"1":"0","NA","NA","NA","NA","NA",
      std::to_string(a.attempts),std::to_string(a.control_reintroduction),
      std::to_string(a.row_control_equality),std::to_string(a.invalid_value),
      std::to_string(a.gcd_unit),std::to_string(a.gcd_full),std::to_string(a.gcd_proper),
      std::to_string(a.hit_moduli.size()),std::to_string(a.hit_factor_sizes.size()),
      std::to_string(a.hit_shapes.size()),"NA",node->syntax};
    const std::string record=join_tsv(row);require(record.size()<=8192,"discovery direct record bound");out<<record;
  }
  return out.str();
}

std::vector<StressWitness> sorted_witnesses(BoundedWitnessHeap heap) {
  std::vector<StressWitness> witnesses;while(!heap.heap.empty()){
    witnesses.push_back(heap.heap.top());heap.heap.pop();}
  std::sort(witnesses.begin(),witnesses.end());return witnesses;
}

std::vector<std::string> split_tabs(const std::string& line);
u64 parse_u64_field(const std::string& text,const std::string& name);

std::map<std::pair<std::string,int>,u64> public_stage_inputs(const std::string& corpus) {
  std::istringstream input(corpus);std::string line;require(bool(std::getline(input,line)),"corpus replay header");
  std::map<std::pair<std::string,int>,u64> stages;
  while(std::getline(input,line)){auto fields=split_tabs(line);require(fields.size()==34,"corpus replay fields");
    const int t=int(parse_u64_field(fields[7],"corpus t"));const u64 u=parse_u64_field(fields[9],"corpus u");
    require(stages.emplace(std::make_pair(fields[4],t),u).second,"duplicate corpus replay stage");}
  return stages;
}

void replay_certificate(const Grammar& grammar,
                        const std::map<std::pair<std::string,int>,u64>& stages,
                        const StressWitness& witness) {
  deadline_check("certificate replay");const std::string N_text=dec(witness.N);
  auto input=stages.find({N_text,int(witness.t)});require(input!=stages.end(),"certificate stage lookup");
  require(witness.family<grammar.syntax_order.size(),"certificate syntax range");
  const auto node=grammar.syntax_order[witness.family];
  RowPublic row=build_row_public(analyze_public(witness.N,int(witness.t),input->second));
  EvaluatedRow evaluated=evaluate_all(grammar,row);
  const auto& e0=evaluated.branch[0][node->eval_index];const auto& e1=evaluated.branch[1][node->eval_index];
  require(required_branch_reason(e0,e1,int(witness.ticket))==VALID,"certificate branch replay");
  const cpp_int value=witness.ticket==0?e0.value:witness.ticket==1?e1.value:
                      witness.ticket==2?e0.value-e1.value:e0.value+e1.value;
  require(!is_row_control(row.controls,value)&&abs_cpp(value)==witness.abs_ticket,
          "certificate ticket replay");
  const cpp_int factor=gcd_abs(value,witness.N);
  require(factor==witness.proper_factor&&factor>1&&factor<witness.N&&witness.N%factor==0,
          "certificate gcd replay");
}

void replay_discovery_certificates(const Grammar& grammar,const std::string& corpus,
                                   const DiscoveryAggregates& aggregates) {
  const auto stages=public_stage_inputs(corpus);
  for(const auto& aggregate:aggregates.direct)
    for(const auto& witness:sorted_witnesses(aggregate.certificates))
      replay_certificate(grammar,stages,witness);
}

std::string discovery_certificates_bytes(const DiscoveryAggregates& aggregates) {
  std::ostringstream out;
  for(const auto& aggregate:aggregates.direct)for(const auto& w:sorted_witnesses(aggregate.certificates)){
    std::ostringstream row;row<<"{\"N\":\""<<dec(w.N)<<"\",\"t\":"<<w.t
      <<",\"ticket_id\":"<<w.ticket<<",\"syntax_id\":"<<w.family
      <<",\"abs_ticket\":\""<<dec(w.abs_ticket)<<"\",\"proper_factor\":\""
      <<dec(w.proper_factor)<<"\"}\n";
    require(row.str().size()<=2048,"discovery certificate record bound");out<<row.str();
  }
  return out.str();
}

std::string baseline_aggregate_bytes(const std::array<std::array<CellStats,28>,42>& baseline) {
  static const std::array<int,7> sizes{{16,20,24,28,32,36,40}};
  std::ostringstream out;
  out<<"baseline_id\tphase\tfactor_bits\tshape_id\trows\tn0\tn1\tvalid_rows\tinvalid_rows\tc0\tc1\terrors\tbalanced_accuracy_num\tbalanced_accuracy_den\n";
  for(int id=0;id<42;++id)for(int size_index=0;size_index<7;++size_index)for(int shape=0;shape<4;++shape){
    const auto& c=baseline[id][4*size_index+shape];const auto accuracy=balanced_accuracy(c);
    require(c.valid==c.rows&&c.invalid==0,"baseline total validity");
    out<<id<<"\t0\t"<<sizes[size_index]<<'\t'<<shape<<'\t'<<c.rows<<'\t'<<c.n0<<'\t'
       <<c.n1<<'\t'<<c.valid<<'\t'<<c.invalid<<'\t'<<c.c0<<'\t'<<c.c1<<'\t'
       <<c.errors<<'\t'<<accuracy.numerator<<'\t'<<accuracy.denominator<<'\n';
  }
  return out.str();
}

std::string selection_bytes(const std::vector<RankedSelector>& selectors,
                            const std::vector<RankedDirect>& direct,
                            const DiscoveryAggregates& aggregates,
                            const std::string& corpus_digest) {
  require(selectors.size()>=SELECTOR_COUNT&&direct.size()>=DIRECT_HELDOUT,
          "selection population");
  std::ostringstream out;
  out<<"selection_type\trank\tsyntax_id\torientation_id\tgrammar_attempt_id\ttyped_layer\tnode_count\tinvalid_rows\tminimum_shape_accuracy_num\tminimum_shape_accuracy_den\texact_cells\ttotal_accuracy_num\ttotal_accuracy_den\terrors\thit_moduli\thit_factor_sizes\thit_shapes\tproper_ticket_count\tinvalid_ticket_count\tdiscovery_corpus_sha256\tcanonical_syntax\n";
  for(std::size_t rank=0;rank<SELECTOR_COUNT;++rank){const auto& selected=selectors[rank];
    const auto& f=selected.fields;
    std::vector<std::string> row={"SELECTOR",std::to_string(rank),std::to_string(selected.node->syntax_id),
      std::to_string(selected.orientation),std::to_string(selected.node->attempt_id),
      std::to_string(selected.node->typed_layer),std::to_string(selected.node->node_count),
      std::to_string(f.invalid_rows),std::to_string(f.minimum_shape.numerator),
      std::to_string(f.minimum_shape.denominator),std::to_string(f.exact_cells),
      std::to_string(f.total.numerator),std::to_string(f.total.denominator),
      std::to_string(f.errors),"NA","NA","NA","NA","NA",corpus_digest,selected.node->syntax};
    const auto record=join_tsv(row);require(record.size()<=8192,"selector selection bound");out<<record;
  }
  for(std::size_t rank=0;rank<DIRECT_HELDOUT;++rank){const auto& selected=direct[rank];
    const auto& a=aggregates.direct[selected.family];
    const u64 invalid=a.control_reintroduction+a.row_control_equality+a.invalid_value;
    std::vector<std::string> row={"DIRECT",std::to_string(rank),std::to_string(selected.node->syntax_id),
      "NA",std::to_string(selected.node->attempt_id),std::to_string(selected.node->typed_layer),
      std::to_string(selected.node->node_count),"NA","NA","NA","NA","NA","NA","NA",
      std::to_string(a.hit_moduli.size()),std::to_string(a.hit_factor_sizes.size()),
      std::to_string(a.hit_shapes.size()),std::to_string(a.gcd_proper),std::to_string(invalid),
      corpus_digest,selected.node->syntax};
    const auto record=join_tsv(row);require(record.size()<=8192,"direct selection bound");out<<record;
  }
  return out.str();
}

struct ControlStream {
  std::string bytes,manifest_rows;
  u64 odd_candidates=0,pairs=0,shortfalls=0;
};

ControlStream generate_consecutive_controls() {
  ControlStream controls;
  std::ostringstream output,manifest;
  output<<"record_type\tfactor_bits\trow_serial\tp\tq\tN\tfirst_fermat_control\tfermat_minus\tfermat_plus\n";
  for(int f=8;f<=22;++f){
    const u64 cell_candidate_start=controls.odd_candidates;
    const u64 lower=u64(1)<<(f-1),upper=(u64(1)<<f)-1;
    const u64 p_limit=std::min(upper,lower+(u64(1)<<20));
    std::optional<u64> previous;int retained=0;
    for(u64 candidate=lower+1;candidate<=upper&&retained<64;candidate+=2){
      deadline_check("consecutive control scan");++controls.odd_candidates;
      if(!is_prime64(candidate))continue;
      if(previous&&*previous<=p_limit){
        const u64 p=*previous,q=candidate;
        if(bitlength(cpp_int(p))==std::size_t(f)&&bitlength(cpp_int(q))==std::size_t(f)&&
           p<q&&q<2*p){
          const cpp_int N=cpp_int(p)*q;cpp_int A=isqrt(N);if(A*A<N)++A;
          cpp_int root;const bool square=is_square(A*A-N,&root);
          const bool proper=square&&A-root>1&&A-root<N&&N%(A-root)==0;
          output<<"PAIR\t"<<f<<'\t'<<retained<<'\t'<<p<<'\t'<<q<<'\t'<<dec(N)
                <<'\t'<<(proper?1:0)<<'\t'<<(square?dec(A-root):"NA")
                <<'\t'<<(square?dec(A+root):"NA")<<'\n';
          ++retained;++controls.pairs;
        }
      }
      previous=candidate;
      if(previous&&*previous>p_limit&&retained<64)break;
    }
    if(retained<64){++controls.shortfalls;
      output<<"SHORTFALL\t"<<f<<'\t'<<retained<<"\tNA\tNA\tNA\tNA\tNA\tNA\n";}
    manifest<<"CONTROL_CELL\t2\t"<<f<<"\tNA\t64\t"<<retained
            <<'\t'<<(controls.odd_candidates-cell_candidate_start)
            <<"\tNA\tNA\tNA\tNA\tNA\t"<<(retained<64?1:0)<<"\tNA\n";
  }
  require(controls.pairs<=960&&controls.odd_candidates<=2097088,
          "consecutive control caps");
  controls.bytes=output.str();controls.manifest_rows=manifest.str();return controls;
}

std::string discovery_manifest_bytes(const Cohort& cohort,const Grammar& grammar,
                                     const PublicPass& public_pass,
                                     const std::string& selection_digest,
                                     const ControlStream& controls) {
  std::ostringstream out;
  out<<"record_type\tphase\tfactor_bits\tshape_id\trequested\tretained\tpair_attempts\tprime_candidates\tsafe_candidates\tsafe_primality_tests\tsafe_pair_attempts\tfermat_exclusions\tduplicates\tdigest_or_value\n";
  out<<generation_manifest_rows(cohort)<<controls.manifest_rows;
  out<<"GRAMMAR\tNA\tNA\tNA\t5564\t"<<grammar.eval_order.size()
     <<"\t5120\t"<<grammar.stats.tuple_retained<<'\t'<<grammar.stats.type_reject
     <<'\t'<<grammar.stats.provenance_reject<<'\t'<<grammar.stats.duplicate_reject
     <<'\t'<<grammar.stats.control_reject<<"\t444\t"<<sha256_bytes(grammar.serialized)<<'\n';
  out<<"CORPUS\t0\tNA\tNA\t896\t"<<public_pass.stage_rows
     <<"\tNA\tNA\tNA\tNA\tNA\tNA\tNA\t"<<public_pass.corpus_digest<<'\n';
  out<<"SELECTION\t0\tNA\tNA\t256\t256\tNA\tNA\tNA\tNA\tNA\tNA\tNA\t"
     <<selection_digest<<'\n';
  out<<"CONTROL_TOTAL\t2\tNA\tNA\t960\t"<<controls.pairs
     <<"\t"<<controls.odd_candidates<<"\tNA\tNA\tNA\tNA\tNA\t"
     <<controls.shortfalls<<"\t"<<sha256_bytes(controls.bytes)<<'\n';
  return out.str();
}

void refuse_existing_outputs(const fs::path& directory,
                             const std::vector<std::string>& names) {
  for(const auto& name:names)require(!fs::exists(directory/name),"existing production evidence "+name);
}

void run_discovery_mode(const std::string& baseline_path,const fs::path& directory,
                        unsigned workers) {
  check_rlimits();require(read_file(baseline_path)==std::string(BASELINE_BYTES,sizeof(BASELINE_BYTES)-1),
                          "discovery baseline bytes");
  refuse_existing_outputs(directory,{"F269-D01.discovery.corpus.tsv",
      "F269-D01.discovery.rules.tsv","F269-D01.discovery.certificates.jsonl",
      "F269-D01.selection.tsv","F269-D01.baselines.tsv",
      "F269-D01.baseline_aggregates.tsv","F269-D01.controls.tsv",
      "F269-D01.grammar.tsv","F269-D01.manifest.tsv"});
  Grammar grammar=build_grammar();const auto direct_nodes=direct_bank_nodes(grammar);
  Cohort cohort=generate_primary_cohort(0);
  PublicPass public_pass=run_public_pass(cohort,grammar,workers);
  checked_write_file(directory,directory/"F269-D01.discovery.corpus.tsv",public_pass.corpus_bytes);
  checked_write_file(directory,directory/"F269-D01.grammar.tsv",grammar.serialized);
  checked_write_file(directory,directory/"F269-D01.baselines.tsv",
                     std::string(BASELINE_BYTES,sizeof(BASELINE_BYTES)-1));
  ControlStream controls=generate_consecutive_controls();
  checked_write_file(directory,directory/"F269-D01.controls.tsv",controls.bytes);
  std::size_t selector_survivors=0,direct_survivors=0;
  for(const auto& node:grammar.eval_order)if(!public_pass.collision[node->eval_index])selector_survivors+=2;
  for(const auto& node:direct_nodes)if(!public_pass.collision[node->eval_index])++direct_survivors;
  require(selector_survivors>=SELECTOR_COUNT&&direct_survivors>=DIRECT_HELDOUT,
          "discovery public-collision survivor gate");
  const std::string public_manifest=discovery_manifest_bytes(
      cohort,grammar,public_pass,"PENDING",controls);
  checked_write_file(directory,directory/"F269-D01.manifest.tsv",public_manifest);

  DiscoveryAggregates aggregates=score_discovery(cohort,grammar,direct_nodes,workers);
  const auto selectors=rank_discovery_selectors(grammar,aggregates,public_pass.collision);
  const auto direct=rank_discovery_direct(direct_nodes,aggregates.direct,public_pass.collision);
  require(selectors.size()>=SELECTOR_COUNT&&direct.size()>=DIRECT_HELDOUT,
          "ranked selection population");
  const std::string rules=discovery_rules_bytes(grammar,aggregates,direct_nodes,
                                                 public_pass.collision,selectors,direct);
  const std::string certificates=discovery_certificates_bytes(aggregates);
  replay_discovery_certificates(grammar,public_pass.corpus_bytes,aggregates);
  const std::string selected=selection_bytes(selectors,direct,aggregates,public_pass.corpus_digest);
  const std::string selection_digest=sha256_bytes(selected);
  checked_write_file(directory,directory/"F269-D01.discovery.rules.tsv",rules);
  checked_write_file(directory,directory/"F269-D01.discovery.certificates.jsonl",certificates);
  checked_write_file(directory,directory/"F269-D01.selection.tsv",selected);
  checked_write_file(directory,directory/"F269-D01.baseline_aggregates.tsv",
                     baseline_aggregate_bytes(aggregates.baselines));
  checked_write_file(directory,directory/"F269-D01.manifest.tsv",
      discovery_manifest_bytes(cohort,grammar,public_pass,selection_digest,controls));
  std::cout<<"DISCOVERY_PASS corpus_sha256="<<public_pass.corpus_digest
           <<" selection_sha256="<<selection_digest
           <<" selector_survivors="<<selectors.size()
           <<" direct_survivors="<<direct.size()<<'\n';
}

std::vector<std::string> split_tabs(const std::string& line) {
  std::vector<std::string> fields;std::size_t begin=0;
  for(;;){const auto tab=line.find('\t',begin);
    if(tab==std::string::npos){fields.push_back(line.substr(begin));break;}
    fields.push_back(line.substr(begin,tab-begin));begin=tab+1;}
  return fields;
}

struct SelectedSelector {std::shared_ptr<Node> node;int orientation=0;};
struct SelectedDirect {std::shared_ptr<Node> node;};
struct AuthenticatedSelection {
  std::vector<SelectedSelector> selectors;
  std::vector<SelectedDirect> direct;
};

u64 parse_u64_field(const std::string& text,const std::string& name) {
  require(!text.empty()&&text.find_first_not_of("0123456789")==std::string::npos,
          "selection unsigned field "+name);
  require(text=="0"||text[0]!='0',"selection leading zero "+name);return std::stoull(text);
}

AuthenticatedSelection authenticate_selection(const Grammar& grammar,
    const std::string& path,const std::string& expected_digest,
    const std::string& discovery_corpus_digest) {
  const std::string bytes=read_file(path);
  require(expected_digest.size()==64&&sha256_bytes(bytes)==expected_digest,
          "selection digest authentication");
  std::istringstream input(bytes);std::string line;
  require(bool(std::getline(input,line)),"selection header missing");
  require(line=="selection_type\trank\tsyntax_id\torientation_id\tgrammar_attempt_id\ttyped_layer\tnode_count\tinvalid_rows\tminimum_shape_accuracy_num\tminimum_shape_accuracy_den\texact_cells\ttotal_accuracy_num\ttotal_accuracy_den\terrors\thit_moduli\thit_factor_sizes\thit_shapes\tproper_ticket_count\tinvalid_ticket_count\tdiscovery_corpus_sha256\tcanonical_syntax",
          "selection header");
  AuthenticatedSelection selected;std::set<std::pair<int,int>> selector_seen;
  std::set<int> direct_seen;
  while(std::getline(input,line)){
    require(!line.empty(),"empty selection row");auto f=split_tabs(line);require(f.size()==21,"selection field count");
    const u64 syntax_word=parse_u64_field(f[2],"syntax_id");
    require(syntax_word<grammar.syntax_order.size(),"selection syntax range");
    const int syntax_id=int(syntax_word);
    const auto node=grammar.syntax_order[syntax_id];
    require(node->syntax_id==syntax_id&&f[4]==std::to_string(node->attempt_id)&&
            f[5]==std::to_string(node->typed_layer)&&f[6]==std::to_string(node->node_count)&&
            f[19]==discovery_corpus_digest&&f[20]==node->syntax,
            "selection grammar reconstruction");
    if(f[0]=="SELECTOR"){
      const int rank=int(parse_u64_field(f[1],"selector rank"));
      const int orientation=int(parse_u64_field(f[3],"orientation"));
      require(rank==int(selected.selectors.size())&&rank<int(SELECTOR_COUNT)&&orientation<2,
              "selector selection order");
      require(selector_seen.insert({syntax_id,orientation}).second,"duplicate selected rule");
      selected.selectors.push_back({node,orientation});
    }else if(f[0]=="DIRECT"){
      const int rank=int(parse_u64_field(f[1],"direct rank"));
      require(f[3]=="NA"&&rank==int(selected.direct.size())&&rank<int(DIRECT_HELDOUT),
              "direct selection order");
      require(direct_seen.insert(syntax_id).second,"duplicate selected direct");
      selected.direct.push_back({node});
    }else fail("selection type");
  }
  require(selected.selectors.size()==SELECTOR_COUNT&&selected.direct.size()==DIRECT_HELDOUT,
          "selection row partition");return selected;
}

struct Counterexample {
  cpp_int N;u64 t=0,syntax_id=0,orientation=0,reason=0,prediction_code=2,target=0;
  int kappa=0;
  bool operator<(const Counterexample& other)const{
    return std::tie(N,t,syntax_id,orientation,reason,prediction_code,target)<
           std::tie(other.N,other.t,other.syntax_id,other.orientation,other.reason,
                    other.prediction_code,other.target);
  }
};

struct HeldoutRuleAggregate {
  std::array<CellStats,20> cells{};
  std::array<std::optional<Counterexample>,20> counterexample{};
  void merge(const HeldoutRuleAggregate& other){
    for(int c=0;c<20;++c){cells[c].add(other.cells[c]);
      if(other.counterexample[c]&&(!counterexample[c]||*other.counterexample[c]<*counterexample[c]))
        counterexample[c]=other.counterexample[c];}
  }
};

struct HeldoutDirectAggregate {
  DirectAggregate tickets{16};u64 expression_invalid_rows=0;
  void merge(HeldoutDirectAggregate& other){
    expression_invalid_rows+=other.expression_invalid_rows;tickets.merge(other.tickets);
  }
};

struct HeldoutWorker {
  std::vector<HeldoutRuleAggregate> rules;
  std::vector<HeldoutDirectAggregate> direct;
  std::array<std::array<CellStats,20>,42> baselines{};
  HeldoutWorker():rules(SELECTOR_COUNT),direct(DIRECT_HELDOUT){}
};

struct HeldoutAggregates {
  std::vector<HeldoutRuleAggregate> rules;
  std::vector<HeldoutDirectAggregate> direct;
  std::array<std::array<CellStats,20>,42> baselines{};
  HeldoutAggregates():rules(SELECTOR_COUNT),direct(DIRECT_HELDOUT){}
};

HeldoutAggregates score_heldout(const Cohort& cohort,const Grammar& grammar,
                                const AuthenticatedSelection& selected,unsigned workers) {
  std::vector<HeldoutWorker> local(workers);std::atomic<std::size_t> next{0};
  std::vector<std::thread> threads;
  for(unsigned worker=0;worker<workers;++worker)threads.emplace_back([&,worker]{
    auto& out=local[worker];
    for(;;){const std::size_t index=next.fetch_add(1);if(index>=cohort.moduli.size())break;
      deadline_check("heldout labelled scoring");const auto& modulus=cohort.moduli[index];
      const int cell=cell_index(1,modulus.factor_bits,modulus.shape);
      const int terminal=(int(bitlength(modulus.N))-1)/4;
      for(int t=1;t<terminal;++t){
        const u64 m=u64(1)<<t,u=inverse_pow2(modulus.p%m,m);
        RowPublic row=build_row_public(analyze_public(modulus.N,t,u));
        EvaluatedRow evaluated=evaluate_all(grammar,row);
        require((cpp_int(modulus.p)-row.stage.r)%m==0&&
                (cpp_int(modulus.q)-row.stage.c)%m==0,"heldout hidden label divisibility");
        const int label_a=int((((cpp_int(modulus.p)-row.stage.r)/m)&1).convert_to<unsigned>());
        const int label_b=int((((cpp_int(modulus.q)-row.stage.c)/m)&1).convert_to<unsigned>());
        const u64 inverse2=inverse_pow2(modulus.p%(2*m),2*m);
        require(inverse2>=u&&(inverse2-u)%m==0,"heldout reciprocal label");
        const int label_e=int((inverse2-u)/m);
        require(label_b==(label_a^row.stage.delta)&&label_e==(label_a^row.stage.kappa),
                "heldout label conversion");
        for(std::size_t rule_id=0;rule_id<selected.selectors.size();++rule_id){
          const auto& selection=selected.selectors[rule_id];
          const auto& e0=evaluated.branch[0][selection.node->eval_index];
          const auto& e1=evaluated.branch[1][selection.node->eval_index];
          std::optional<int> prediction;Reason reason=VALID;
          if(e0.valid&&e1.valid)
            prediction=selection.orientation==0?(e1.value<e0.value?1:0):(e0.value>e1.value?0:1);
          else reason=!e0.valid&&!e1.valid?min_reason(e0.reason,e1.reason):(e0.valid?e1.reason:e0.reason);
          update_cell(out.rules[rule_id].cells[cell],label_a,prediction,reason,
                      e0.reason_mask|e1.reason_mask);
          if(!prediction||*prediction!=label_a){
            Counterexample witness{modulus.N,u64(t),u64(selection.node->syntax_id),
                u64(selection.orientation),u64(reason),prediction?u64(*prediction):2ULL,
                u64(label_a),row.stage.kappa};
            auto& retained=out.rules[rule_id].counterexample[cell];
            if(!retained||witness<*retained)retained=witness;
          }
          if(prediction)require(((*prediction^row.stage.kappa)==label_e)==(*prediction==label_a),
                                "heldout selector coordinate agreement");
        }
        const auto baseline=baseline_predictions(row);
        for(int id=0;id<42;++id)update_cell(out.baselines[id][cell],label_a,baseline[id]);
        for(std::size_t family=0;family<selected.direct.size();++family){
          auto& aggregate=out.direct[family];const auto& node=*selected.direct[family].node;
          const auto& e0=evaluated.branch[0][node.eval_index];
          const auto& e1=evaluated.branch[1][node.eval_index];
          if(!e0.valid||!e1.valid)++aggregate.expression_invalid_rows;
          for(int ticket=0;ticket<4;++ticket){
            ++aggregate.tickets.attempts;const Reason missing=required_branch_reason(e0,e1,ticket);
            if(missing!=VALID){++aggregate.tickets.invalid_value;continue;}
            if(static_ticket_control(selected.direct[family].node,ticket,row.stage)){
              ++aggregate.tickets.control_reintroduction;continue;
            }
            cpp_int value=ticket==0?e0.value:ticket==1?e1.value:
                          ticket==2?e0.value-e1.value:e0.value+e1.value;
            if(is_row_control(row.controls,value)){++aggregate.tickets.row_control_equality;continue;}
            const cpp_int factor=gcd_abs(value,modulus.N);
            if(factor==1)++aggregate.tickets.gcd_unit;
            else if(factor==modulus.N)++aggregate.tickets.gcd_full;
            else{
              require(factor>1&&factor<modulus.N&&modulus.N%factor==0,
                      "heldout proper certificate");
              ++aggregate.tickets.gcd_proper;aggregate.tickets.hit_moduli.insert(dec(modulus.N));
              aggregate.tickets.hit_factor_sizes.insert(modulus.factor_bits);
              aggregate.tickets.hit_shapes.insert(modulus.shape);
              aggregate.tickets.certificates.insert({modulus.N,u64(t),u64(ticket),
                  u64(node.syntax_id),abs_cpp(value),factor});
            }
          }
        }
      }
    }
  });
  for(auto& thread:threads)thread.join();HeldoutAggregates merged;
  for(auto& worker:local){
    for(std::size_t r=0;r<SELECTOR_COUNT;++r)merged.rules[r].merge(worker.rules[r]);
    for(std::size_t f=0;f<DIRECT_HELDOUT;++f)merged.direct[f].merge(worker.direct[f]);
    for(int b=0;b<42;++b)for(int c=0;c<20;++c)merged.baselines[b][c].add(worker.baselines[b][c]);
  }
  for(auto& family:merged.direct){family.tickets.check_partition();
    require(family.tickets.attempts==30720*4,"heldout direct attempt count");}
  for(const auto& rule:merged.rules)for(const auto& cell:rule.cells)
    require(cell.n0>0&&cell.n1>0,"heldout cell label classes");
  return merged;
}

CellStats pool_heldout_cells(const std::array<CellStats,20>& cells,
                             const std::function<bool(int)>& include) {
  CellStats pooled;for(int i=0;i<20;++i)if(include(i))pooled.add(cells[i]);return pooled;
}

bool selector_total_valid(const HeldoutRuleAggregate& aggregate) {
  for(const auto& cell:aggregate.cells)if(cell.invalid!=0)return false;return true;
}

bool finite_exact_selector(const HeldoutRuleAggregate& aggregate) {
  if(!selector_total_valid(aggregate))return false;
  for(const auto& cell:aggregate.cells)if(cell.errors!=0)return false;return true;
}

Rational minimum_cell_accuracy_for_size(const HeldoutRuleAggregate& aggregate,int size_index) {
  Rational minimum=balanced_accuracy(aggregate.cells[4*size_index]);
  for(int shape=1;shape<4;++shape){const Rational value=balanced_accuracy(aggregate.cells[4*size_index+shape]);
    if(compare_rational(value,minimum)<0)minimum=value;}
  return minimum;
}

bool correlation_lead(const HeldoutRuleAggregate& aggregate,
                      const std::array<std::array<CellStats,20>,42>& baselines) {
  if(!selector_total_valid(aggregate))return false;const Rational threshold{3,5};
  for(int shape=0;shape<4;++shape){
    const Rational candidate=balanced_accuracy(pool_heldout_cells(
        aggregate.cells,[=](int i){return i%4==shape;}));
    if(compare_rational(candidate,threshold)<0)return false;
    for(int baseline=0;baseline<42;++baseline){
      const Rational reference=balanced_accuracy(pool_heldout_cells(
          baselines[baseline],[=](int i){return i%4==shape;}));
      if(compare_rational(candidate,reference)<=0)return false;
    }
  }
  for(int size_index:{2,3,4}){
    const Rational candidate=balanced_accuracy(pool_heldout_cells(
        aggregate.cells,[=](int i){return i/4==size_index;}));
    if(compare_rational(candidate,threshold)<0)return false;
  }
  const Rational size52=minimum_cell_accuracy_for_size(aggregate,2);
  const Rational size56=minimum_cell_accuracy_for_size(aggregate,3);
  const Rational size60=minimum_cell_accuracy_for_size(aggregate,4);
  return compare_rational(size56,size52)>=0&&compare_rational(size60,size56)>=0;
}

bool direct_heldout_lead(const HeldoutDirectAggregate& aggregate) {
  const auto& a=aggregate.tickets;
  return aggregate.expression_invalid_rows==0&&a.hit_moduli.size()>=16&&
         a.hit_factor_sizes.size()>=3&&a.hit_shapes.size()>=3&&
         (a.hit_factor_sizes.count(56)||a.hit_factor_sizes.count(60));
}

std::string heldout_rules_bytes(const AuthenticatedSelection& selected,
                                const HeldoutAggregates& aggregates) {
  std::ostringstream out;
  out<<"record_type\tselection_rank\tsyntax_id\torientation_id\ttyped_layer\tnode_count\ttotal_valid\terrors\tbalanced_accuracy_num\tbalanced_accuracy_den\tfinite_exact_selector_candidate\tcorrelation_lead\texpression_invalid_rows\tticket_attempts\tcontrol_reintroduction\trow_control_equality\tinvalid_value\tgcd_unit\tgcd_full\tgcd_proper\thit_moduli\thit_factor_sizes\thit_shapes\tdirect_lead\tcells\tcanonical_syntax\n";
  for(std::size_t rank=0;rank<selected.selectors.size();++rank){
    const auto& selection=selected.selectors[rank];const auto& aggregate=aggregates.rules[rank];
    CellStats total;std::ostringstream cells;for(int c=0;c<20;++c){total.add(aggregate.cells[c]);if(c)cells<<';';cells<<cell_stats_text(aggregate.cells[c]);}
    const auto accuracy=balanced_accuracy(total);
    std::vector<std::string> row={"SELECTOR",std::to_string(rank),
      std::to_string(selection.node->syntax_id),std::to_string(selection.orientation),
      std::to_string(selection.node->typed_layer),std::to_string(selection.node->node_count),
      selector_total_valid(aggregate)?"1":"0",std::to_string(total.errors),
      std::to_string(accuracy.numerator),std::to_string(accuracy.denominator),
      finite_exact_selector(aggregate)?"1":"0",correlation_lead(aggregate,aggregates.baselines)?"1":"0",
      "NA","NA","NA","NA","NA","NA","NA","NA","NA","NA","NA","NA",
      cells.str(),selection.node->syntax};
    const auto record=join_tsv(row);require(record.size()<=8192,"heldout selector record bound");out<<record;
  }
  for(std::size_t rank=0;rank<selected.direct.size();++rank){
    const auto& selection=selected.direct[rank];const auto& held=aggregates.direct[rank];const auto& a=held.tickets;
    std::vector<std::string> row={"DIRECT",std::to_string(rank),
      std::to_string(selection.node->syntax_id),"NA",std::to_string(selection.node->typed_layer),
      std::to_string(selection.node->node_count),held.expression_invalid_rows==0?"1":"0","NA","NA","NA","NA","NA",
      std::to_string(held.expression_invalid_rows),std::to_string(a.attempts),
      std::to_string(a.control_reintroduction),std::to_string(a.row_control_equality),
      std::to_string(a.invalid_value),std::to_string(a.gcd_unit),std::to_string(a.gcd_full),
      std::to_string(a.gcd_proper),std::to_string(a.hit_moduli.size()),
      std::to_string(a.hit_factor_sizes.size()),std::to_string(a.hit_shapes.size()),
      direct_heldout_lead(held)?"1":"0","NA",selection.node->syntax};
    const auto record=join_tsv(row);require(record.size()<=8192,"heldout direct record bound");out<<record;
  }
  return out.str();
}

std::string heldout_certificates_bytes(const HeldoutAggregates& aggregates) {
  std::ostringstream out;
  for(const auto& held:aggregates.direct)for(const auto& w:sorted_witnesses(held.tickets.certificates)){
    std::ostringstream row;row<<"{\"N\":\""<<dec(w.N)<<"\",\"t\":"<<w.t
      <<",\"ticket_id\":"<<w.ticket<<",\"syntax_id\":"<<w.family
      <<",\"abs_ticket\":\""<<dec(w.abs_ticket)<<"\",\"proper_factor\":\""
      <<dec(w.proper_factor)<<"\"}\n";
    require(row.str().size()<=2048,"heldout certificate record bound");out<<row.str();
  }
  return out.str();
}

std::string heldout_counterexample_bytes(const HeldoutAggregates& aggregates) {
  std::vector<Counterexample> witnesses;
  for(const auto& rule:aggregates.rules)for(const auto& witness:rule.counterexample)
    if(witness)witnesses.push_back(*witness);
  require(witnesses.size()<=3840,"counterexample retention cap");
  std::sort(witnesses.begin(),witnesses.end());
  std::ostringstream out;
  out<<"N\tt\tsyntax_id\torientation_id\treason_id\tprediction_a\tprediction_e\ttarget_a\ttarget_e\n";
  for(const auto& w:witnesses){
    const std::string prediction_a=w.prediction_code==2?"NA":std::to_string(w.prediction_code);
    const std::string prediction_e=w.prediction_code==2?"NA":std::to_string(w.prediction_code^w.kappa);
    const std::string record=join_tsv({dec(w.N),std::to_string(w.t),std::to_string(w.syntax_id),
      std::to_string(w.orientation),std::to_string(w.reason),prediction_a,prediction_e,
      std::to_string(w.target),std::to_string(w.target^w.kappa)});
    require(record.size()<=2048,"counterexample record bound");out<<record;
  }
  return out.str();
}

std::string heldout_lead_gate_bytes(const AuthenticatedSelection& selected,
                                    const HeldoutAggregates& aggregates) {
  std::ostringstream out;
  out<<"record_type\tselection_rank\tsyntax_id\torientation_id\ttotal_valid\terrors\tfinite_exact_selector_candidate\tcorrelation_lead\thit_moduli\thit_factor_sizes\thit_shapes\tincludes_size_56_or_60\tdirect_lead\n";
  for(std::size_t rank=0;rank<selected.selectors.size();++rank){
    CellStats total;for(const auto& c:aggregates.rules[rank].cells)total.add(c);
    out<<"SELECTOR\t"<<rank<<'\t'<<selected.selectors[rank].node->syntax_id<<'\t'
       <<selected.selectors[rank].orientation<<'\t'<<selector_total_valid(aggregates.rules[rank])
       <<'\t'<<total.errors<<'\t'<<finite_exact_selector(aggregates.rules[rank])<<'\t'
       <<correlation_lead(aggregates.rules[rank],aggregates.baselines)
       <<"\tNA\tNA\tNA\tNA\tNA\n";
  }
  for(std::size_t rank=0;rank<selected.direct.size();++rank){const auto& held=aggregates.direct[rank];const auto& a=held.tickets;
    out<<"DIRECT\t"<<rank<<'\t'<<selected.direct[rank].node->syntax_id
       <<"\tNA\t"<<(held.expression_invalid_rows==0)<<"\tNA\tNA\tNA\t"
       <<a.hit_moduli.size()<<'\t'<<a.hit_factor_sizes.size()<<'\t'<<a.hit_shapes.size()
       <<'\t'<<(a.hit_factor_sizes.count(56)||a.hit_factor_sizes.count(60))
       <<'\t'<<direct_heldout_lead(held)<<'\n';
  }
  return out.str();
}

std::string combine_baseline_aggregates(const std::string& discovery_bytes,
    const std::array<std::array<CellStats,20>,42>& heldout) {
  static const std::string header="baseline_id\tphase\tfactor_bits\tshape_id\trows\tn0\tn1\tvalid_rows\tinvalid_rows\tc0\tc1\terrors\tbalanced_accuracy_num\tbalanced_accuracy_den";
  std::istringstream input(discovery_bytes);std::string line;require(bool(std::getline(input,line))&&line==header,"discovery baseline aggregate header");
  std::array<std::vector<std::string>,42> discovery;
  while(std::getline(input,line)){auto f=split_tabs(line);require(f.size()==14,"discovery baseline aggregate fields");
    const int id=int(parse_u64_field(f[0],"baseline id"));require(id<42&&f[1]=="0","discovery baseline aggregate phase");discovery[id].push_back(line);}
  static const std::array<int,5> sizes{{44,48,52,56,60}};std::ostringstream out;out<<header<<'\n';
  std::size_t records=0;
  for(int id=0;id<42;++id){require(discovery[id].size()==28,"discovery baseline aggregate count");
    for(const auto& row:discovery[id]){out<<row<<'\n';++records;}
    for(int size_index=0;size_index<5;++size_index)for(int shape=0;shape<4;++shape){
      const auto& c=heldout[id][4*size_index+shape];const auto accuracy=balanced_accuracy(c);
      require(c.valid==c.rows&&c.invalid==0,"heldout baseline validity");
      out<<id<<"\t1\t"<<sizes[size_index]<<'\t'<<shape<<'\t'<<c.rows<<'\t'<<c.n0<<'\t'
         <<c.n1<<'\t'<<c.valid<<'\t'<<c.invalid<<'\t'<<c.c0<<'\t'<<c.c1<<'\t'
         <<c.errors<<'\t'<<accuracy.numerator<<'\t'<<accuracy.denominator<<'\n';++records;
    }
  }
  require(records==2016,"combined baseline aggregate count");return out.str();
}

std::string append_heldout_manifest(const std::string& discovery_manifest,
                                    const Cohort& cohort,const PublicPass& public_pass,
                                    const std::string& selection_digest) {
  require(discovery_manifest.rfind("record_type\t",0)==0,"discovery manifest header");
  std::ostringstream out;out<<discovery_manifest<<generation_manifest_rows(cohort);
  out<<"CORPUS\t1\tNA\tNA\t1280\t"<<public_pass.stage_rows
     <<"\tNA\tNA\tNA\tNA\tNA\tNA\tNA\t"<<public_pass.corpus_digest<<'\n';
  out<<"SELECTION_AUTH\t1\tNA\tNA\t256\t256\tNA\tNA\tNA\tNA\tNA\tNA\tNA\t"
     <<selection_digest<<'\n';
  return out.str();
}

void run_heldout_mode(const std::string& baseline_path,const fs::path& directory,
                      unsigned workers,const std::string& selection_path,
                      const std::string& selection_digest,
                      const std::string& discovery_corpus_digest) {
  check_rlimits();require(read_file(baseline_path)==std::string(BASELINE_BYTES,sizeof(BASELINE_BYTES)-1),
                          "heldout source baseline bytes");
  require(read_file((directory/"F269-D01.baselines.tsv").string())==
          std::string(BASELINE_BYTES,sizeof(BASELINE_BYTES)-1),"heldout evidence baseline bytes");
  refuse_existing_outputs(directory,{"F269-D01.heldout.corpus.tsv",
      "F269-D01.heldout.rules.tsv","F269-D01.heldout.certificates.jsonl",
      "F269-D01.heldout.counterexamples.tsv","F269-D01.heldout.lead_gate.tsv"});
  require(sha256_file((directory/"F269-D01.discovery.corpus.tsv").string())==
          discovery_corpus_digest,"discovery corpus digest authentication");
  checked_evidence_path(directory,selection_path);
  Grammar grammar=build_grammar();
  require(sha256_file((directory/"F269-D01.grammar.tsv").string())==
          sha256_bytes(grammar.serialized),"heldout grammar authentication");
  const AuthenticatedSelection selected=authenticate_selection(
      grammar,selection_path,selection_digest,discovery_corpus_digest);

  Cohort cohort=generate_primary_cohort(1);
  PublicPass public_pass=run_public_pass(cohort,grammar,workers);
  checked_write_file(directory,directory/"F269-D01.heldout.corpus.tsv",public_pass.corpus_bytes);
  const std::string discovery_manifest=read_file((directory/"F269-D01.manifest.tsv").string());
  checked_write_file(directory,directory/"F269-D01.manifest.tsv",
      append_heldout_manifest(discovery_manifest,cohort,public_pass,selection_digest));

  HeldoutAggregates aggregates=score_heldout(cohort,grammar,selected,workers);
  const auto heldout_stages=public_stage_inputs(public_pass.corpus_bytes);
  for(const auto& family:aggregates.direct)
    for(const auto& witness:sorted_witnesses(family.tickets.certificates))
      replay_certificate(grammar,heldout_stages,witness);
  const std::string rules=heldout_rules_bytes(selected,aggregates);
  const std::string certificates=heldout_certificates_bytes(aggregates);
  const std::string counterexamples=heldout_counterexample_bytes(aggregates);
  const std::string lead_gate=heldout_lead_gate_bytes(selected,aggregates);
  checked_write_file(directory,directory/"F269-D01.heldout.rules.tsv",rules);
  checked_write_file(directory,directory/"F269-D01.heldout.certificates.jsonl",certificates);
  checked_write_file(directory,directory/"F269-D01.heldout.counterexamples.tsv",counterexamples);
  checked_write_file(directory,directory/"F269-D01.heldout.lead_gate.tsv",lead_gate);
  const std::string discovery_baselines=read_file(
      (directory/"F269-D01.baseline_aggregates.tsv").string());
  checked_write_file(directory,directory/"F269-D01.baseline_aggregates.tsv",
                     combine_baseline_aggregates(discovery_baselines,aggregates.baselines));
  const std::string public_manifest=append_heldout_manifest(
      discovery_manifest,cohort,public_pass,selection_digest);
  std::ostringstream final_manifest;final_manifest<<public_manifest;
  u64 exact=0,correlation=0,direct=0;
  for(const auto& rule:aggregates.rules){exact+=finite_exact_selector(rule);
    correlation+=correlation_lead(rule,aggregates.baselines);}
  for(const auto& family:aggregates.direct)direct+=direct_heldout_lead(family);
  final_manifest<<"VERDICT_COUNTS\t1\tNA\tNA\t256\t256\t"<<exact<<'\t'
                <<correlation<<'\t'<<direct<<"\t0\t0\tNA\tNA\t"
                <<sha256_bytes(lead_gate)<<'\n';
  checked_write_file(directory,directory/"F269-D01.manifest.tsv",final_manifest.str());
  std::cout<<"HELDOUT_PASS corpus_sha256="<<public_pass.corpus_digest
           <<" selection_sha256="<<selection_digest<<" finite_exact="<<exact
           <<" correlation_leads="<<correlation<<" direct_leads="<<direct<<'\n';
}

void reciprocal_orientation_fixture(u64 m,u64 u,u64 r,int expected_kappa) {
  require((u*r-1)%m==0,"reciprocal fixture divisibility");
  const int kappa=int(((u*r-1)/m)&1);
  require(kappa==expected_kappa,"reciprocal fixture kappa");
  for(int a=0;a<2;++a){
    const int postprocessed_e=a^kappa;
    const u64 lifted_factor=r+u64(a)*m;
    const u64 lifted_inverse=inverse_pow2(lifted_factor,2*m);
    require(lifted_inverse>=u&&(lifted_inverse-u)%m==0,
            "reciprocal hidden lift range");
    const int hidden_e=int((lifted_inverse-u)/m);
    require(hidden_e==postprocessed_e,"reciprocal hidden/public orientation");
    require(((u+u64(hidden_e)*m)*lifted_factor)%(2*m)==1,
            "reciprocal lifted product");
  }
}

void assert_zero_gap_fixture(const cpp_int& N,int t,u64 u,int expected_tail) {
  RowPublic row=build_row_public(analyze_public(N,t,u));
  for(int a=0;a<2;++a){
    int zero_count=0;
    for(int tail=0;tail<6;++tail)if(row.branch[a].tails[tail].zero_gap)++zero_count;
    require(zero_count==1&&row.branch[a].tails[expected_tail].zero_gap,
            "unique zero-gap tail");
    require(row.branch[a].tails[expected_tail].x.empty()&&
            row.branch[a].tails[expected_tail].q.empty(),
            "zero-gap performed division");
    for(int off=0;off<30;++off){
      const auto& root=row.branch[a].roots[30*expected_tail+off];
      require(!root.valid&&root.reason==ZERO_GAP,"zero-gap root reason");
    }
  }
}

Grammar exact_self_tests(const std::string& baseline_path) {
  require(sha256_bytes("")==
          "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
          "SHA-256 empty vector");
  require(sha256_bytes("abc")==
          "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad",
          "SHA-256 abc vector");

  constexpr u64 PA=720575940379279399ULL,QA=1008806316530991113ULL;
  constexpr u64 PB=792633534417207313ULL,QB=1080863910568919077ULL;
  const cpp_int NA("726921560194875913822899294212981087");
  const cpp_int NB("856728981658246606409659147429610101");
  const std::array<u64,4> factors{{PA,QA,PB,QB}};
  for(u64 z:factors){require(is_prime64(z),"replacement fixture primality");require(bitlength(cpp_int(z))==60,"replacement factor bits");}
  for(std::size_t i=0;i<factors.size();++i)for(std::size_t j=i+1;j<factors.size();++j)
    require(factors[i]!=factors[j],"replacement factors distinct");
  require(PA-1==2ULL*360287970189639699ULL,"PA decomposition");
  require(QA-1==8ULL*126100789566373889ULL,"QA decomposition");
  require(PB-1==16ULL*49539595901075457ULL,"PB decomposition");
  require(QB-1==4ULL*270215977642229769ULL,"QB decomposition");
  require(cpp_int(PA)*QA==NA&&cpp_int(PB)*QB==NB,"replacement products");
  require(PA<QA&&QA<2*PA&&PB<QB&&QB<2*PB,"replacement balance");
  require(bitlength(NA)==120&&bitlength(NB)==120,"replacement product bits");

  const std::string header=transcript_header();
  require(header.size()==659&&std::count(header.begin(),header.end(),'\t')==86,
          "transcript header schema");
  require(sha256_bytes(header)==
          "29d8676fa23d0e58f38db8e7ec7ee05d273a57d1ade1259d6c59e671385daa53",
          "transcript header digest");
  std::string transcript_a=header,transcript_b=header,combined=header;
  for(int which=0;which<2;++which){
    const cpp_int& N=which==0?NA:NB;const u64 p=which==0?PA:PB;
    require((int(bitlength(N))-1)/4==29,"fixture terminal stage");
    for(int t=1;t<=29;++t){
      const u64 m=u64(1)<<t,u=inverse_pow2(p%m,m);
      const auto stage=analyze_public(N,t,u);
      const std::string row=transcript_row(which==0?'A':'B',stage);
      (which==0?transcript_a:transcript_b)+=row;combined+=row;
    }
  }
  require(transcript_a.size()==33735&&sha256_bytes(transcript_a)==
          "99f17050d302872a1612b0d480799972423643a02afa1b435de55ba21a267668",
          "fixture A transcript");
  require(transcript_b.size()==33805&&sha256_bytes(transcript_b)==
          "8b8752e2e67827184eb07ad87950eec92a3084711e03aa09742350c13940db4f",
          "fixture B transcript");
  require(combined.size()==66881&&sha256_bytes(combined)==
          "fc7bfb1d9105d6a597d91f007ca3da18c2b1095e51ae0ff5b33408b62f655fe6",
          "combined transcript");

  reciprocal_orientation_fixture(4,1,1,0);
  reciprocal_orientation_fixture(8,3,3,1);
  assert_zero_gap_fixture(cpp_int(10541),1,1,5);
  assert_zero_gap_fixture(cpp_int(943),1,1,0);
  RowPublic alias_row=build_row_public(analyze_public(cpp_int(10541),2,3));
  require(alias_row.stage.r==3&&alias_row.stage.c==3&&alias_row.stage.K==2633&&
          alias_row.stage.delta==1,"alias fixture algebra");
  for(int a=0;a<2;++a){
    require(alias_row.branch[a].tails[0].zero_gap,"alias fixture PC:OC zero");
    require(alias_row.branch[a].tails[6].serialization==
            alias_row.branch[a].tails[9].serialization&&
            alias_row.branch[a].tails[6].alias_id==
            alias_row.branch[a].tails[9].alias_id,
            "alias fixture PC:R OC:C");
  }

  std::set<cpp_int> no_controls;
  Tail short_tail=build_tail(0,13,5,false);short_tail.alias_id=0;
  require(short_tail.x==std::vector<cpp_int>({13,5,3,2,1,0})&&
          short_tail.q==std::vector<cpp_int>({2,1,1,2}),"short tail trace");
  const std::set<int> valid_offsets={0,1,8,9,16,17,18,21,24,27};
  for(int off=0;off<30;++off){auto root=ordinary_root(short_tail,off,no_controls);
    require(root.valid==bool(valid_offsets.count(off)),"short tail validity mask");
    if(!root.valid)require(root.reason==DEPTH_MISSING,"short tail missing reason");
  }
  cpp_int f0=0,f1=1;for(int i=0;i<32;++i){cpp_int next=f0+f1;f0=f1;f1=next;}
  Tail long_tail=build_tail(1,f1,f0,false);long_tail.alias_id=1;
  require(cross_root(short_tail,long_tail,2,no_controls).valid,
          "short-long depth-two cross");
  require(cross_root(short_tail,long_tail,4,no_controls).reason==DEPTH_MISSING&&
          cross_root(short_tail,long_tail,8,no_controls).reason==DEPTH_MISSING,
          "short-long deep cross missing");
  Tail zero_tail=build_tail(2,0,0,true);
  require(cross_root(zero_tail,long_tail,2,no_controls).reason==ZERO_GAP,
          "zero-gap cross reason");
  Tail alias_tail=long_tail;alias_tail.tail_id=2;alias_tail.alias_id=1;
  require(cross_root(long_tail,alias_tail,2,no_controls).reason==TAIL_STATE_ALIAS,
          "tail-alias cross reason");

  auto const_zero=std::make_shared<Node>();const_zero->root_form=Form::cnst(0);
  auto opaque=std::make_shared<Node>();
  auto select=std::make_shared<Node>();select->kind=NodeKind::ADAPTIVE;select->op=0;
  select->child={const_zero,opaque};
  require(compute_control_mask(const_zero)==0x00ffffffU,"CONST chamber mask");
  require(compute_control_mask(opaque)==0,"OPAQUE chamber mask");
  require(compute_control_mask(select)==0x001c71c7U,"kappa select chamber mask");
  std::swap(select->child[0],select->child[1]);
  require(compute_control_mask(select)==0x00e38e38U,"swapped kappa chamber mask");
  require(branch_mask({true,VALID,1,-1},{true,VALID,2,-1})=="03"&&
          branch_mask({true,VALID,1,-1},{false,DEPTH_MISSING,0,-1})=="01"&&
          branch_mask({false,DEPTH_MISSING,0,-1},{true,VALID,2,-1})=="02"&&
          branch_mask({false,DEPTH_MISSING,0,-1},{false,DEPTH_MISSING,0,-1})=="00",
          "branch mask fixtures");

  constexpr u64 P_BAD=1152921504606846883ULL,Q_BAD=1152921504606846943ULL;
  const cpp_int N_BAD("1329227995784915727635697479817628669");
  require(cpp_int(P_BAD)*Q_BAD==N_BAD,"bad fixture product");
  require(Q_BAD==17ULL*2113ULL*308137ULL*104161559ULL,"bad Q decomposition");
  require(validate_stress_pair(P_BAD,Q_BAD)==PairDomainStatus::OUT_OF_DOMAIN_COMPOSITE_Q,
          "bad fixture validator classification");
  const u64 bad_m=1024,bad_u=11,bad_r=inverse_pow2(bad_u,bad_m);
  const u64 bad_c=(N_BAD*bad_u%bad_m).convert_to<u64>();
  const cpp_int bad_k=(N_BAD-cpp_int(bad_r)*bad_c)/bad_m;
  const cpp_int bad_z10=bad_k-bad_c,bad_z11=bad_k-bad_r-bad_c-bad_m;
  require(bad_r==931&&bad_c==991&&bad_k==cpp_int("1298074214633706765269235820133502")&&
          int((bad_k&1).convert_to<unsigned>())==0&&
          int((((cpp_int(bad_u)*bad_r-1)/bad_m)&1).convert_to<unsigned>())==0,
          "bad fixture stage arithmetic");
  require(bad_z10==cpp_int("1298074214633706765269235820132511")&&
          bad_z11==cpp_int("1298074214633706765269235820130556")&&
          gcd_abs(bad_z10,N_BAD)==17&&gcd_abs(bad_z11,N_BAD)==17,
          "bad fixture gcd-17 regression");

  const std::string baseline=read_file(baseline_path);
  require(baseline==std::string(BASELINE_BYTES,sizeof(BASELINE_BYTES)-1),
          "baseline embedded bytes");
  require(baseline.size()==2014&&sha256_bytes(baseline)==BASELINE_SHA,
          "baseline bytes and digest");

  Grammar grammar=build_grammar();
  require(grammar.stats.root_retained==444&&grammar.layer_end[0]==444,
          "grammar root partition");
  require(grammar.eval_order.size()>=1024&&grammar.eval_order.size()<=FINAL_ATTEMPTS,
          "grammar final bounds");
  require(grammar.layer_end[3]==grammar.eval_order.size(),"grammar layer boundary");
  for(std::size_t i=1;i<grammar.syntax_order.size();++i)
    require(grammar.syntax_order[i-1]->syntax<grammar.syntax_order[i]->syntax,
            "grammar syntax order");
  for(const auto& node:grammar.eval_order)if(node->kind==NodeKind::ROOT)
    require(node->control_mask==0,"root chamber mask");
  const std::string attempt_mask=std::string(110,'f')+"0f";
  require(attempt_mask.size()==112,"root attempt mask bytes");

  RowPublic all_missing;
  all_missing.stage.N=NA;all_missing.stage.n=120;
  all_missing.stage.r=1;all_missing.stage.c=3;
  for(int a=0;a<2;++a){
    for(int t=0;t<14;++t)all_missing.branch[a].tails[t].alias_id=t;
    for(auto& root:all_missing.branch[a].roots)root={false,DEPTH_MISSING,0};
    require(root_mask(all_missing.branch[a])==std::string(112,'0'),
            "all-roots-missing mask");
    auto hist=reason_histogram(all_missing.branch[a]);
    require(hist[DEPTH_MISSING]==444,"all-roots-missing histogram");
  }
  auto missing_eval=evaluate_all(grammar,all_missing);
  for(int a=0;a<2;++a)for(const auto& value:missing_eval.branch[a])
    require(!value.valid&&value.reason==DEPTH_MISSING,
            "all-roots-missing propagation");

  RowPublic cross_missing=all_missing;
  for(int a=0;a<2;++a){
    for(int i=0;i<420;++i)cross_missing.branch[a].roots[i]=
        {true,VALID,cpp_int(10000+1000*a+i)};
    for(int i=420;i<444;++i)cross_missing.branch[a].roots[i]=
        {false,DEPTH_MISSING,0};
  }
  auto cross_eval=evaluate_all(grammar,cross_missing);
  for(int a=0;a<2;++a)for(const auto& node:grammar.eval_order)
    if(depends_on_cross_root(node)){
      const auto& value=cross_eval.branch[a][node->eval_index];
      require(!value.valid&&value.reason==DEPTH_MISSING,
              "cross-root missing propagation");
    }

  return grammar;
}

}  // namespace f269

int main(int argc,char** argv) {
  try {
    f269::initialize_packet_deadline();
    if(argc==2&&std::string(argv[1])=="--grammar-once"){
      f269::check_rlimits();const auto m=f269::measure_grammar_once();
      std::cout<<"nanoseconds\t"<<m.nanoseconds<<"\nroot_retained\t"<<m.stats.root_retained
               <<"\ntuple_attempts\t5120\ntuple_retained\t"<<m.stats.tuple_retained
               <<"\ntype_reject\t"<<m.stats.type_reject
               <<"\nprovenance_reject\t"<<m.stats.provenance_reject
               <<"\nduplicate_reject\t"<<m.stats.duplicate_reject
               <<"\nall_chamber_control_reject\t"<<m.stats.control_reject
               <<"\nfinal_syntax_count\t"<<m.final_count
               <<"\ngrammar_bytes\t"<<m.bytes<<"\ngrammar_sha256\t"<<m.digest<<'\n';
      return 0;
    }
    if(argc==4&&std::string(argv[1])=="--max-work-round"){
      f269::check_rlimits();const unsigned workers=std::stoul(argv[2]);
      const unsigned round=std::stoul(argv[3]);f269::require(round<4,"round range");
      const auto m=f269::measure_maximum_round(round,workers);
      std::cout<<"nanoseconds\t"<<m.nanoseconds<<"\nvmhwm_bytes\t"<<m.vmhwm_bytes
               <<"\ntail_divisions\t"<<m.totals.tail_divisions
               <<"\nvalue_checks\t"<<m.totals.value_checks
               <<"\nprimitive_maps\t"<<m.totals.primitive_maps
               <<"\ncanonicalizations\t"<<m.totals.canonicalizations
               <<"\nselector_updates\t"<<m.totals.selector_updates
               <<"\ntickets\t"<<m.totals.tickets
               <<"\nheap4_replacements\t"<<m.totals.replacements4
               <<"\nheap16_replacements\t"<<m.totals.replacements16
               <<"\nfixture_sha256\t"<<m.digest<<'\n';
      return 0;
    }
    if(argc==4&&std::string(argv[1])=="--serialization-write"){
      f269::check_rlimits();f269::write_serialization_fixture(argv[2],argv[3]);return 0;
    }
    if(argc==4&&std::string(argv[1])=="--splitmix-stream-write"){
      f269::check_rlimits();f269::write_splitmix_stream(argv[2],argv[3]);return 0;
    }
    if(argc==4&&std::string(argv[1])=="--checked-truncate"){
      f269::check_rlimits();f269::checked_truncate_file(argv[2],argv[3]);return 0;
    }
    if(argc==6&&std::string(argv[1])=="--gate"){
      f269::check_rlimits();f269::evaluate_preflight_gate(
          argv[2],std::stoull(argv[3]),argv[4],argv[5]);return 0;
    }
    if(argc==3&&std::string(argv[1])=="--self-test"){
      f269::check_rlimits();
      auto grammar=f269::exact_self_tests(argv[2]);
      std::cout<<"SELF_TEST_PASS roots="<<grammar.stats.root_retained
               <<" tuples="<<grammar.stats.tuple_retained
               <<" type_reject="<<grammar.stats.type_reject
               <<" provenance_reject="<<grammar.stats.provenance_reject
               <<" duplicate_reject="<<grammar.stats.duplicate_reject
               <<" control_reject="<<grammar.stats.control_reject
               <<" final="<<grammar.eval_order.size()
               <<" grammar_bytes="<<grammar.serialized.size()
               <<" grammar_sha256="<<f269::sha256_bytes(grammar.serialized)<<'\n';
      return 0;
    }
    if(argc==5&&std::string(argv[1])=="--discovery"){
      f269::run_discovery_mode(argv[2],argv[3],std::stoul(argv[4]));return 0;
    }
    if(argc==8&&std::string(argv[1])=="--heldout"){
      f269::run_heldout_mode(argv[2],argv[3],std::stoul(argv[4]),argv[5],argv[6],argv[7]);
      return 0;
    }
    std::cerr<<"usage: f269 MODE [MODE_ARGUMENTS]\n";
    return 64;
  } catch(const std::exception& e) {
    std::cerr<<"F269_FAIL "<<e.what()<<'\n';
    return 70;
  }
}
