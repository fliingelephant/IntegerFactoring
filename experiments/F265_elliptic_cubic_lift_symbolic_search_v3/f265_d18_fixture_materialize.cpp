#include <algorithm>
#include <array>
#include <cerrno>
#include <cctype>
#include <clocale>
#include <cstdint>
#include <cstring>
#include <dirent.h>
#include <fcntl.h>
#include <iomanip>
#include <initializer_list>
#include <iostream>
#include <map>
#include <set>
#include <sstream>
#include <stdexcept>
#include <string>
#include <sys/stat.h>
#include <sys/types.h>
#include <tuple>
#include <unistd.h>
#include <utility>
#include <vector>

#include <boost/multiprecision/cpp_int.hpp>
#include <boost/multiprecision/integer.hpp>

// F265-D18 source draft.  This role only materializes public fixtures.  It has
// no corpus parser, private-label parser, scientific mode, or fixture-root
// placeholder.  Execution remains forbidden until the separately specified
// containment and source-audit gates have passed.

namespace {

using boost::multiprecision::cpp_int;

constexpr char kVersion[] = "F265-D18";
constexpr uint64_t kFnvOffset = UINT64_C(14695981039346656037);
constexpr uint64_t kFnvPrime = UINT64_C(1099511628211);
constexpr uint64_t kLogicalCap = UINT64_C(8388608);
constexpr uint64_t kResultRecordCap = UINT64_C(4194304);
constexpr uint64_t kResultByteCap = UINT64_C(134217728);
constexpr uint64_t kBigintCap = UINT64_C(33554432);
constexpr uint64_t kGf2Cap = UINT64_C(1048576);
constexpr uint64_t kPrimeCandidateCap = UINT64_C(65536);

struct Failure : std::runtime_error {
  using std::runtime_error::runtime_error;
};

struct Sha256 {
  std::array<uint32_t, 8> h{{0x6a09e667U, 0xbb67ae85U, 0x3c6ef372U,
                             0xa54ff53aU, 0x510e527fU, 0x9b05688cU,
                             0x1f83d9abU, 0x5be0cd19U}};
  std::array<unsigned char, 64> block{};
  uint64_t bytes = 0;
  size_t used = 0;

  static uint32_t rotr(uint32_t x, unsigned n) {
    return (x >> n) | (x << (32U - n));
  }
  void compress(const unsigned char* p) {
    static constexpr uint32_t k[64] = {
        0x428a2f98U, 0x71374491U, 0xb5c0fbcfU, 0xe9b5dba5U,
        0x3956c25bU, 0x59f111f1U, 0x923f82a4U, 0xab1c5ed5U,
        0xd807aa98U, 0x12835b01U, 0x243185beU, 0x550c7dc3U,
        0x72be5d74U, 0x80deb1feU, 0x9bdc06a7U, 0xc19bf174U,
        0xe49b69c1U, 0xefbe4786U, 0x0fc19dc6U, 0x240ca1ccU,
        0x2de92c6fU, 0x4a7484aaU, 0x5cb0a9dcU, 0x76f988daU,
        0x983e5152U, 0xa831c66dU, 0xb00327c8U, 0xbf597fc7U,
        0xc6e00bf3U, 0xd5a79147U, 0x06ca6351U, 0x14292967U,
        0x27b70a85U, 0x2e1b2138U, 0x4d2c6dfcU, 0x53380d13U,
        0x650a7354U, 0x766a0abbU, 0x81c2c92eU, 0x92722c85U,
        0xa2bfe8a1U, 0xa81a664bU, 0xc24b8b70U, 0xc76c51a3U,
        0xd192e819U, 0xd6990624U, 0xf40e3585U, 0x106aa070U,
        0x19a4c116U, 0x1e376c08U, 0x2748774cU, 0x34b0bcb5U,
        0x391c0cb3U, 0x4ed8aa4aU, 0x5b9cca4fU, 0x682e6ff3U,
        0x748f82eeU, 0x78a5636fU, 0x84c87814U, 0x8cc70208U,
        0x90befffaU, 0xa4506cebU, 0xbef9a3f7U, 0xc67178f2U};
    uint32_t w[64];
    for (unsigned i = 0; i != 16; ++i) {
      w[i] = (uint32_t(p[4 * i]) << 24) | (uint32_t(p[4 * i + 1]) << 16) |
             (uint32_t(p[4 * i + 2]) << 8) | uint32_t(p[4 * i + 3]);
    }
    for (unsigned i = 16; i != 64; ++i) {
      uint32_t s0 = rotr(w[i - 15], 7) ^ rotr(w[i - 15], 18) ^
                    (w[i - 15] >> 3);
      uint32_t s1 = rotr(w[i - 2], 17) ^ rotr(w[i - 2], 19) ^
                    (w[i - 2] >> 10);
      w[i] = w[i - 16] + s0 + w[i - 7] + s1;
    }
    uint32_t a = h[0], b = h[1], c = h[2], d = h[3];
    uint32_t e = h[4], f = h[5], g = h[6], z = h[7];
    for (unsigned i = 0; i != 64; ++i) {
      uint32_t s1 = rotr(e, 6) ^ rotr(e, 11) ^ rotr(e, 25);
      uint32_t ch = (e & f) ^ ((~e) & g);
      uint32_t t1 = z + s1 + ch + k[i] + w[i];
      uint32_t s0 = rotr(a, 2) ^ rotr(a, 13) ^ rotr(a, 22);
      uint32_t maj = (a & b) ^ (a & c) ^ (b & c);
      uint32_t t2 = s0 + maj;
      z = g;
      g = f;
      f = e;
      e = d + t1;
      d = c;
      c = b;
      b = a;
      a = t1 + t2;
    }
    h[0] += a; h[1] += b; h[2] += c; h[3] += d;
    h[4] += e; h[5] += f; h[6] += g; h[7] += z;
  }
  void update(const void* data, size_t n) {
    const auto* p = static_cast<const unsigned char*>(data);
    bytes += n;
    while (n != 0) {
      size_t take = std::min(n, block.size() - used);
      std::copy(p, p + take, block.begin() + static_cast<ptrdiff_t>(used));
      used += take;
      p += take;
      n -= take;
      if (used == block.size()) {
        compress(block.data());
        used = 0;
      }
    }
  }
  void update(const std::string& s) { update(s.data(), s.size()); }
  std::string finish() {
    const uint64_t bits = bytes * 8;
    block[used++] = 0x80;
    if (used > 56) {
      std::fill(block.begin() + static_cast<ptrdiff_t>(used), block.end(), 0);
      compress(block.data());
      used = 0;
    }
    std::fill(block.begin() + static_cast<ptrdiff_t>(used), block.begin() + 56,
              0);
    for (unsigned i = 0; i != 8; ++i)
      block[63 - i] = static_cast<unsigned char>(bits >> (8 * i));
    compress(block.data());
    std::ostringstream out;
    out << std::hex << std::setfill('0');
    for (uint32_t x : h) out << std::setw(8) << x;
    return out.str();
  }
};

std::string sha256(const std::string& s) {
  Sha256 h;
  h.update(s);
  return h.finish();
}

uint64_t fnv1a(const std::string& s) {
  uint64_t h = kFnvOffset;
  for (unsigned char c : s) h = (h ^ c) * kFnvPrime;
  return h;
}

std::string hex64(uint64_t x) {
  std::ostringstream out;
  out << std::hex << std::nouppercase << x;
  return out.str();
}

std::string mask64(uint64_t x) {
  std::ostringstream out;
  out << std::hex << std::nouppercase << std::setw(16) << std::setfill('0')
      << x;
  return out.str();
}

std::string hexz(const cpp_int& x) {
  if (x < 0) return "-" + hexz(-x);
  std::ostringstream out;
  out << std::hex << x;
  return out.str();
}

cpp_int modz(cpp_int x, const cpp_int& n) {
  x %= n;
  if (x < 0) x += n;
  return x;
}

cpp_int gcdz(cpp_int a, cpp_int b) {
  if (a < 0) a = -a;
  if (b < 0) b = -b;
  while (b != 0) {
    cpp_int r = a % b;
    a = b;
    b = r;
  }
  return a;
}

cpp_int powz(cpp_int a, unsigned e) {
  cpp_int r = 1;
  while (e != 0) {
    if ((e & 1U) != 0) r *= a;
    e >>= 1U;
    if (e != 0) a *= a;
  }
  return r;
}

cpp_int powmod(cpp_int a, cpp_int e, const cpp_int& n) {
  a = modz(a, n);
  cpp_int r = 1 % n;
  while (e != 0) {
    if ((e & 1) != 0) r = (r * a) % n;
    e >>= 1;
    if (e != 0) a = (a * a) % n;
  }
  return r;
}

unsigned bitlen(const cpp_int& x) {
  if (x <= 0) throw Failure("BITLEN_DOMAIN");
  return static_cast<unsigned>(boost::multiprecision::msb(x)) + 1;
}

cpp_int isqrtz(const cpp_int& n) {
  if (n < 0) throw Failure("ISQRT_DOMAIN");
  if (n < 2) return n;
  cpp_int x = cpp_int(1) << ((bitlen(n) + 1) / 2);
  for (;;) {
    cpp_int y = (x + n / x) >> 1;
    if (y >= x) return x;
    x = y;
  }
}

bool prime_small(uint64_t n) {
  if (n < 2) return false;
  if ((n & 1U) == 0) return n == 2;
  for (uint64_t d = 3; d <= n / d; d += 2)
    if (n % d == 0) return false;
  return true;
}

std::vector<uint64_t> support_primes(uint64_t& candidates) {
  std::vector<uint64_t> p;
  for (uint64_t n = 31; p.size() != 128; n += 30) {
    for (uint64_t x : {n, n + 15}) {
      if (x % 15 != 1) continue;
      if (++candidates > kPrimeCandidateCap) throw Failure("PRIME_CAP");
      if (prime_small(x)) p.push_back(x);
      if (p.size() == 128) break;
    }
  }
  return p;
}

const std::array<const char*, 37> kFixtures{{
    "CURVE_U32", "CURVE_POWER32", "RBELOW128", "FACTOR129",
    "RNG_SEMANTIC", "SOURCE_BRANCH", "SOURCE_CHRONO320",
    "SOURCE_AFFINE_STOP3", "SOURCE_ROW_STOP2", "DECODER_SUPPORT3",
    "DECODER_SUPPORT64", "DECODER_EMPTY", "DECODER_S0", "DECODER_S1",
    "DENSE_GF2", "EVENT130", "PACKET_EVENT60373", "RATE_GCD", "RATE_SAT",
    "RATE_DIV", "RATE_TREE", "RATE_RECON", "RATE_TERMINAL", "RATE_COMPARE",
    "RATE_IO", "RATE_NODE", "RATE_TOUCH", "RATE_LEAF", "RATE_EXP",
    "RATE_PARITY", "RATE_GF2", "RATE_EXACT_PRODUCT", "RATE_MOD_PRODUCT",
    "RATE_ISQRT", "RATE_INVERSE", "RATE_SIGNED", "RATE_BASIS_RECORD"}};

const std::array<const char*, 40> kCounters{{
    "CURVE_PROPOSALS", "RANDOM_BELOW_CALLS", "RANDOM_BELOW_ITERATIONS",
    "RNG_DRAWS", "ADMITTED_ROWS", "AFFINE_ADDITIONS",
    "AFFINE_SAFETY_GCDS", "DISCRIMINANT_GCDS", "ROW_ROOT_GCDS",
    "ROW_RECORDS", "PRODUCT_MULTIPLICATIONS", "PEEL_EXACT_DIVISIONS",
    "PEEL_BASE_REMAINDERS", "PEEL_MODULAR_MULTIPLICATIONS", "PEEL_GCDS",
    "PEEL_RESIDUAL_DIVISIONS", "PEEL_SQUARE_TESTS", "F271_SCALAR_GCDS",
    "F271_SATURATION_POWERS", "F271_REFINEMENT_DIVISIONS",
    "F271_RECURSION_NODES", "F271_TOUCHES", "F271_LEAF_ASSIGNMENTS",
    "F271_TREE_NODE_UPDATES", "F271_EXPONENT_COORD_UPDATES",
    "F271_RECONSTRUCTION_INCIDENCES", "F271_TERMINAL_BLOCKS",
    "F271_REPLACEMENT_COMPARISONS", "F271_FINAL_COMPARISONS",
    "F271_BLOCK_COMPARISONS", "F271_PARITY_CELLS",
    "F271_GF2_WORD_OPERATIONS", "SELECTED_EXACT_PRODUCTS",
    "SELECTED_MODULAR_PRODUCTS", "INTEGER_SQUARE_ROOTS", "MODULAR_INVERSIONS",
    "SIGNED_RELATION_GCDS", "BASIS_RECORDS", "FACTOR_EVENT_LINES", "IO_BYTES"}};

size_t fixture_rank(const std::string& name) {
  for (size_t i = 0; i != kFixtures.size(); ++i)
    if (name == kFixtures[i]) return i;
  throw Failure("FIXTURE_TOKEN");
}

size_t counter_rank(const std::string& name) {
  for (size_t i = 0; i != kCounters.size(); ++i)
    if (name == kCounters[i]) return i;
  throw Failure("COUNTER_TOKEN");
}

struct Operand {
  std::string fixture;
  uint64_t group = 0;
  uint64_t item = 0;
  uint64_t cycles = 1;
  std::string opcode;
  std::array<std::string, 16> arg{};
};

struct Semantic {
  std::string fixture;
  std::string kind;
  std::array<std::string, 8> value{};
};

struct Fixture {
  std::array<uint64_t, 40> counter{};
  std::vector<Semantic> semantic;
  Sha256 result_sha;
  uint64_t result_fnv = kFnvOffset;
  uint64_t result_records = 0;
  uint64_t result_bytes = 0;
  bool traced = false;
};

struct Packet {
  std::vector<Operand> source;
  std::vector<Operand> decoder;
  std::vector<Operand> rate;
  std::array<Fixture, 37> fixture;
  uint64_t bigint_ops = 0;
  uint64_t gf2_ops = 0;
  uint64_t prime_candidates = 0;
  uint64_t result_records = 0;
  uint64_t result_bytes = 0;

  Fixture& f(const std::string& name) { return fixture[fixture_rank(name)]; }
  void count(const std::string& fixture_name, const std::string& name,
             uint64_t delta) {
    auto& v = f(fixture_name).counter[counter_rank(name)];
    if (UINT64_MAX - v < delta) throw Failure("COUNTER_OVERFLOW");
    v += delta;
  }
  void sem(const std::string& fixture_name, const std::string& kind,
           std::initializer_list<std::string> values) {
    Semantic s;
    s.fixture = fixture_name;
    s.kind = kind;
    s.value.fill("-");
    size_t i = 0;
    for (const auto& x : values) {
      if (i == 8) throw Failure("SEMANTIC_WIDTH");
      s.value[i++] = x;
    }
    f(fixture_name).semantic.push_back(std::move(s));
  }
  void pass(const std::string& fixture_name) {
    sem(fixture_name, "STATUS", {"FIXTURE", "0", "PASS"});
  }
  void operand(std::vector<Operand>& file, const std::string& fixture_name,
               uint64_t group, uint64_t item, uint64_t cycles,
               const std::string& opcode,
               std::initializer_list<std::string> args) {
    Operand r;
    r.fixture = fixture_name;
    r.group = group;
    r.item = item;
    r.cycles = cycles;
    r.opcode = opcode;
    r.arg.fill("-");
    size_t i = 0;
    for (const auto& x : args) {
      if (i == 16) throw Failure("OPERAND_WIDTH");
      r.arg[i++] = x;
    }
    file.push_back(std::move(r));
  }
  void trace(const std::string& fixture_name, const std::string& line) {
    auto& x = f(fixture_name);
    x.traced = true;
    uint64_t records = static_cast<uint64_t>(std::count(line.begin(),line.end(),'\n'));
    if (line.empty() || line.back()!='\n' || line.find('\r')!=std::string::npos ||
        result_records > kResultRecordCap-records ||
        line.size() > kResultByteCap ||
        result_bytes > kResultByteCap-static_cast<uint64_t>(line.size()))
      throw Failure("RESULT_CAP");
    result_records += records;
    result_bytes += line.size();
    x.result_records += records;
    x.result_bytes += line.size();
    for(unsigned char byte:line)x.result_fnv=(x.result_fnv^byte)*kFnvPrime;
    x.result_sha.update(line);
  }
};

std::string event_args(uint64_t ordinal, uint64_t nonce) {
  static const std::array<std::array<uint64_t, 7>, 10> k{{
      {{0, 0, 0, 0, 65535, 65535, 0}}, {{1, 1, 1, 0, 4, 9, 0}},
      {{1, 1, 2, 1, 164, 169, 0}}, {{1, 2, 0, 0, 4, 9, 0}},
      {{1, 2, 0, 1, 164, 164, 0}}, {{2, 3, 0, 1, 164, 65535, 0}},
      {{3, 4, 1, 65535, 65535, 65535, 1}},
      {{3, 4, 2, 65535, 65535, 65535, 1}},
      {{4, 5, 1, 65535, 65535, 65535, 1}},
      {{4, 5, 2, 65535, 65535, 65535, 1}}}};
  const auto& t = k[ordinal % 10];
  std::ostringstream out;
  out << t[0] << '\t' << t[1] << '\t' << t[2] << '\t' << t[3] << '\t'
      << t[4] << '\t' << t[5] << '\t' << t[6] << '\t'
      << (t[6] ? "0000000000000010" : "0000000000000000") << '\t'
      << "0000000000000000\t0000001000000000\t0000000000000000\t"
         "0000000000000000\t"
      << hexz(cpp_int("933956397855941843")) << '\t' << nonce;
  return out.str();
}

void build_source_fixtures(Packet& p) {
  const cpp_int nf("735592564497057472472983056100764157");
  const cpp_int proper("933956397855941843");
  const std::string nfh = hexz(nf);
  const std::string ph = hexz(proper);

  // The 32-slot screen tapes are literal after materialization.  Candidate
  // construction is deterministic and bounded here; preflight never searches.
  for (const std::string name : {"CURVE_U32", "CURVE_POWER32"}) {
    p.pass(name);
    for (uint64_t i = 0; i != 32; ++i) {
      if (name == "CURVE_U32")
        p.operand(p.source, name, 0, i, 1, "U_PROPOSAL",
                  {nfh, hex64(i + 1), hex64(2 * i + 1), hex64(3 * i + 1)});
      else
        p.operand(p.source, name, 0, i, 1, "POWER_PROPOSAL",
                  {nfh, hex64(i + 1)});
    }
    p.count(name, "CURVE_PROPOSALS", 32);
    p.count(name, "DISCRIMINANT_GCDS", 32);
    p.sem(name, "STATUS", {name == "CURVE_U32" ? "U_PROPOSAL" :
                           "POWER_PROPOSAL", "31", "RESOURCE_REJECT_CURVE_ATTEMPTS"});
    p.sem(name, "AGGREGATE", {"CALLS", "32"});
  }

  p.pass("RBELOW128");
  p.operand(p.source, "RBELOW128", 0, 0, 1, "RANDOM_BELOW",
            {"11", "11", "0", "0", "80"});
  p.operand(p.source, "RBELOW128", 1, 0, 1, "RANDOM_BELOW",
            {"11", "11", "0", "-", "80"});
  p.count("RBELOW128", "RANDOM_BELOW_CALLS", 2);
  p.count("RBELOW128", "RANDOM_BELOW_ITERATIONS", 256);
  p.count("RBELOW128", "RNG_DRAWS", 256);
  p.sem("RBELOW128", "RANDOM_RESULT",
        {"0", "11", "0", "128", "128", "PASS"});
  p.sem("RBELOW128", "RANDOM_RESULT",
        {"1", "11", "-", "128", "128", "RESOURCE_REJECT_RANDOM_BELOW_CAP"});
  p.sem("RBELOW128", "AGGREGATE", {"CALLS", "2"});
  p.sem("RBELOW128", "CERTIFICATE", {"TRACE_MATCH", "1"});

  p.pass("RNG_SEMANTIC");
  p.operand(p.source, "RNG_SEMANTIC", 0, 0, 1, "RANDOM_BELOW",
            {"11", "11", "0", "10", "2"});
  p.operand(p.source, "RNG_SEMANTIC", 1, 0, 1, "RANDOM_BELOW",
            {"20000000000000000", "ffffffffffffffff", "1",
             "1ffffffffffffffff", "1"});
  p.operand(p.source, "RNG_SEMANTIC", 2, 0, 1, "RANDOM_BELOW",
            {"11", "11", "0", "-", "80"});
  p.count("RNG_SEMANTIC", "RANDOM_BELOW_CALLS", 3);
  p.count("RNG_SEMANTIC", "RANDOM_BELOW_ITERATIONS", 131);
  p.count("RNG_SEMANTIC", "RNG_DRAWS", 132);
  p.sem("RNG_SEMANTIC", "RANDOM_RESULT",
        {"0", "11", "10", "2", "2", "PASS"});
  p.sem("RNG_SEMANTIC", "RANDOM_RESULT",
        {"1", "20000000000000000", "1ffffffffffffffff", "1", "2", "PASS"});
  p.sem("RNG_SEMANTIC", "RANDOM_RESULT",
        {"2", "11", "-", "128", "128", "RESOURCE_REJECT_RANDOM_BELOW_CAP"});
  p.sem("RNG_SEMANTIC", "AGGREGATE", {"OUTPUT_XOR", "1ffffffffffffffef"});
  p.sem("RNG_SEMANTIC", "CERTIFICATE",
        {"MIX64_ZERO", "1", "e220a8397b1dcdaf"});

  p.pass("SOURCE_BRANCH");
  const std::array<std::array<uint64_t, 7>, 4> affine{{
      {{35, 1, 1, 0, 1, 0, 34}}, {{35, 1, 1, 0, 1, 0, 6}},
      {{35, 1, 1, 0, 1, 7, 1}}, {{35, 1, 1, 0, 1, 9, 2}}}};
  for (uint64_t i = 0; i != affine.size(); ++i) {
    std::vector<std::string> a;
    for (uint64_t x : affine[i]) a.push_back(hex64(x));
    p.operand(p.source, "SOURCE_BRANCH", 0, i, 1, "AFFINE",
              {a[0],a[1],a[2],a[3],a[4],a[5],a[6],hex64(i),hex64(i+1)});
  }
  for (uint64_t i = 0; i != 3; ++i)
    p.operand(p.source, "SOURCE_BRANCH", 1, i, 1, "ROW_ROOT",
              {"23", i == 0 ? "5" : (i == 1 ? "0" : "1"), "0", hex64(i)});
  p.count("SOURCE_BRANCH", "AFFINE_ADDITIONS", 4);
  p.count("SOURCE_BRANCH", "AFFINE_SAFETY_GCDS", 3);
  p.count("SOURCE_BRANCH", "ROW_ROOT_GCDS", 3);
  p.count("SOURCE_BRANCH", "FACTOR_EVENT_LINES", 3);
  p.sem("SOURCE_BRANCH", "AFFINE_RESULT",
        {"0","GLOBAL_INFINITY","-","-","-","0","0","1"});
  p.sem("SOURCE_BRANCH", "AFFINE_RESULT",
        {"1","FACTOR_X_SIGN_MINUS","-","-","5","1","1","2"});
  p.sem("SOURCE_BRANCH", "AFFINE_RESULT",
        {"2","FACTOR_DENOMINATOR","-","-","7","1","2","3"});
  p.sem("SOURCE_BRANCH", "ROW_ROOT_RESULT", {"0","FACTOR_ROW_ROOT","5","0","0","1"});
  p.sem("SOURCE_BRANCH", "ROW_ROOT_RESULT", {"1","FULL_ROW_ROOT","-","0","1","1"});
  p.sem("SOURCE_BRANCH", "ROW_ROOT_RESULT", {"2","UNIT","-","0","2","1"});

  for (const std::string name : {"FACTOR129", "EVENT130"}) {
    p.pass(name);
    const uint64_t total = name == "FACTOR129" ? 129 : 130;
    for (uint64_t i = 0; i != total; ++i) {
      std::array<std::string, 14> a{};
      std::istringstream in(event_args(i, 0));
      for (auto& x : a) std::getline(in, x, '\t');
      p.operand(p.source, name, 0, i, 1, "EVENT",
                {a[0],a[1],a[2],a[3],a[4],a[5],a[6],a[7],a[8],a[9],a[10],a[11],ph,a[13]});
      if (i < 129) {
        p.count(name, "FACTOR_EVENT_LINES", 1);
        p.sem(name, "FACTOR_RESULT",
              {std::to_string(i),a[0],a[1],a[2],ph,a[3],a[4],a[5]});
      }
    }
    p.sem(name, "STATUS", {"EVENT_JOURNAL", "0",
          name == "FACTOR129" ? "PASS" : "INVARIANT_EVENT_CAP"});
    p.sem(name, "AGGREGATE", {"RESULT_RECORDS", "129"});
    p.sem(name, "CERTIFICATE", {"EVENT_DIGEST_UNCHANGED", "1"});
  }

  p.pass("PACKET_EVENT60373");
  p.operand(p.source, "PACKET_EVENT60373", 0, 0, 60373, "FACTOR_TOKEN",
            {"0","0","0","0","ffff","ffff","0",
             "0000000000000000","0000000000000000","0000000000000000",
             "0000000000000000","0000000000000000",ph,"0"});
  p.count("PACKET_EVENT60373", "FACTOR_EVENT_LINES", 60372);
  p.sem("PACKET_EVENT60373", "STATUS",
        {"PACKET_JOURNAL","0","INVARIANT_PACKET_EVENT_CAP"});
  p.sem("PACKET_EVENT60373", "AGGREGATE", {"RESULT_RECORDS", "60372"});
  p.sem("PACKET_EVENT60373", "CERTIFICATE",
        {"PACKET_DIGEST_UNCHANGED","1"});

  const cpp_int ns = (cpp_int(1) << 107) - 1;
  const std::string nsh = hexz(ns);
  p.pass("SOURCE_CHRONO320");
  for (uint64_t i = 0; i != 32; ++i) {
    if (i != 31)
      p.operand(p.source, "SOURCE_CHRONO320", 0, i, 1, "U_PROPOSAL",
                {nsh,hexz(ns-3),"1","0"});
    else
      p.operand(p.source, "SOURCE_CHRONO320", 0, i, 1, "U_PROPOSAL",
                {nsh,"1",hexz(ns-1),hexz(ns-1)});
  }
  p.operand(p.source, "SOURCE_CHRONO320", 1, 0, 159, "AFFINE",
            {nsh,"1","3",hexz(ns-1),hexz(ns-1),hexz(ns-1),hexz(ns-1),"0","0"});
  for (uint64_t i = 0; i != 160; ++i)
    p.operand(p.source, "SOURCE_CHRONO320", 2, i, 1, "ROW_ROOT",
              {nsh, i == 0 ? hexz(ns-1) : "f", "0", hex64(i)});
  for (uint64_t i = 0; i != 32; ++i)
    p.operand(p.source, "SOURCE_CHRONO320", 3, i, 1, "POWER_PROPOSAL",
              {nsh, i == 31 ? "1" : hexz(ns-1)});
  p.operand(p.source, "SOURCE_CHRONO320", 4, 0, 159, "AFFINE",
            {nsh,"2",hexz(ns-2),"1","1","1","1","160","160"});
  for (uint64_t i = 0; i != 160; ++i)
    p.operand(p.source, "SOURCE_CHRONO320", 5, i, 1, "ROW_ROOT",
              {nsh,"1","1",hex64(160+i)});
  for (uint64_t i = 0; i != 320; ++i) {
    cpp_int w = (cpp_int(1) << 180) + 2*i + 1;
    p.operand(p.source, "SOURCE_CHRONO320", 6, i, 1, "PEEL_ROW",
              {hex64(i),hexz(w),hexz(w*w)});
  }
  p.count("SOURCE_CHRONO320", "CURVE_PROPOSALS", 64);
  p.count("SOURCE_CHRONO320", "RANDOM_BELOW_CALLS", 128);
  p.count("SOURCE_CHRONO320", "RANDOM_BELOW_ITERATIONS", 128);
  p.count("SOURCE_CHRONO320", "RNG_DRAWS", 256);
  p.count("SOURCE_CHRONO320", "ADMITTED_ROWS", 320);
  p.count("SOURCE_CHRONO320", "AFFINE_ADDITIONS", 318);
  p.count("SOURCE_CHRONO320", "AFFINE_SAFETY_GCDS", 318);
  p.count("SOURCE_CHRONO320", "DISCRIMINANT_GCDS", 64);
  p.count("SOURCE_CHRONO320", "ROW_ROOT_GCDS", 320);
  p.count("SOURCE_CHRONO320", "ROW_RECORDS", 320);
  p.count("SOURCE_CHRONO320", "PRODUCT_MULTIPLICATIONS", 319);
  for (const char* c : {"PEEL_EXACT_DIVISIONS","PEEL_BASE_REMAINDERS",
                        "PEEL_GCDS","PEEL_RESIDUAL_DIVISIONS","PEEL_SQUARE_TESTS"})
    p.count("SOURCE_CHRONO320", c, 320);
  // bitlen(361)=9 and popcount(361)=5 for every square tape row.
  p.count("SOURCE_CHRONO320", "PEEL_MODULAR_MULTIPLICATIONS", 4480);
  p.sem("SOURCE_CHRONO320", "AGGREGATE", {"ROW_COUNT","320"});
  p.sem("SOURCE_CHRONO320", "AGGREGATE", {"SURVIVOR_COUNT","320"});
  p.sem("SOURCE_CHRONO320", "CERTIFICATE", {"LUCAS_LEHMER","1"});
  p.sem("SOURCE_CHRONO320", "CERTIFICATE", {"CURVE_EQUATIONS","1"});
  p.sem("SOURCE_CHRONO320", "CERTIFICATE", {"TRACE_MATCH","1"});

  // Build the exact D12 chronological result bytes independently of preflight.
  for (uint64_t curve = 0; curve != 2; ++curve) {
    for (uint64_t slot = 0; slot != 32; ++slot) {
      const bool accept = slot == 31;
      cpp_int A, B, x, y, d;
      if (curve == 0) {
        A = accept ? 1 : ns - 3; x = accept ? ns - 1 : 1;
        y = accept ? ns - 1 : 0; B = accept ? 3 : 2;
      } else {
        cpp_int s = accept ? 1 : ns - 1;
        x = s*s % ns; y = s*s%ns*s%ns; A = (s+1)%ns;
        B = modz(y*y-x*x*x-A*x,ns);
      }
      d = gcdz(4*A*A*A+27*B*B,ns);
      p.trace("SOURCE_CHRONO320", "SOURCE_CHRONO320\tPROPOSAL\t"+
              hex64(curve)+"\t"+hex64(slot)+"\t"+
              (accept?"ACCEPT":"REJECT_FULL_DISCRIMINANT")+"\t"+
              hexz(A)+"\t"+hexz(B)+"\t"+hexz(x)+"\t"+hexz(y)+"\t"+hexz(d)+"\n");
    }
    for (uint64_t scalar = 1; scalar <= 160; ++scalar) {
      cpp_int u, v, A, B;
      if (curve == 0) {
        A=1; B=3; u=scalar==1?ns-1:6; v=scalar==1?ns-1:15;
      } else {
        A=2; B=ns-2;
        if (scalar==1) { u=1; v=1; }
        else {
          cpp_int slope=5*((ns+1)/2)%ns;
          u=modz(slope*slope-2,ns); v=modz(slope*(1-u)-1,ns);
        }
      }
      if (scalar != 1)
        p.trace("SOURCE_CHRONO320", "SOURCE_CHRONO320\tAFFINE\t"+
                hex64(curve)+"\t"+hex64(scalar-1)+"\tOK\t"+hexz(u)+"\t"+
                hexz(v)+"\t1\n");
      p.trace("SOURCE_CHRONO320", "SOURCE_CHRONO320\tROW\t"+
              hex64(curve)+"\t"+hex64(scalar)+"\tUNIT\t1\n");
      cpp_int a=u*u*u+A*u+B;
      cpp_int carry=(a-v*v)/ns;
      p.trace("SOURCE_CHRONO320", "SOURCE_CHRONO320\tRENDER\t"+
              hex64(curve*160+scalar-1)+"\t"+hexz(u)+"\t"+hexz(v)+"\t"+
              hexz(a)+"\t"+hexz(carry)+"\n");
    }
  }
  std::vector<cpp_int> peel_rows;
  cpp_int peel_product = 1;
  for (uint64_t i=0;i!=320;++i) {
    cpp_int w=(cpp_int(1)<<180)+2*i+1;
    peel_rows.push_back(w*w);
    peel_product *= peel_rows.back();
  }
  for (uint64_t i=0;i!=320;++i) {
    const cpp_int& a=peel_rows[i];
    cpp_int complement=peel_product/a;
    cpp_int g=gcdz(a,powmod(complement%a,bitlen(a),a));
    cpp_int b=a/g, square_root=isqrtz(b);
    bool square=square_root*square_root==b;
    p.trace("SOURCE_CHRONO320", "SOURCE_CHRONO320\tPEEL\t"+hex64(i)+"\t"+
            hexz(g)+"\t"+hexz(b)+"\t"+(square?"1":"0")+"\t"+
            (square?"1":"0")+"\n");
  }

  p.pass("SOURCE_AFFINE_STOP3");
  const std::array<std::array<uint64_t,4>,3> stops{{{{0,1,0,34}},{{0,1,0,6}},{{0,1,7,1}}}};
  for (uint64_t i=0;i!=3;++i)
    p.operand(p.source,"SOURCE_AFFINE_STOP3",0,i,1,"AFFINE",
              {"23","1","1",hex64(stops[i][0]),hex64(stops[i][1]),
               hex64(stops[i][2]),hex64(stops[i][3]),hex64(i),hex64(i+1)});
  p.count("SOURCE_AFFINE_STOP3","AFFINE_ADDITIONS",3);
  p.count("SOURCE_AFFINE_STOP3","AFFINE_SAFETY_GCDS",2);
  p.count("SOURCE_AFFINE_STOP3","FACTOR_EVENT_LINES",2);
  p.trace("SOURCE_AFFINE_STOP3","SOURCE_AFFINE_STOP3\tAFFINE\t0\tGLOBAL_INFINITY\t-\t-\t1\n");
  p.trace("SOURCE_AFFINE_STOP3","SOURCE_AFFINE_STOP3\tAFFINE\t1\tFACTOR_X_SIGN_MINUS\t-\t-\t5\n");
  p.trace("SOURCE_AFFINE_STOP3","SOURCE_AFFINE_STOP3\tAFFINE\t2\tFACTOR_DENOMINATOR\t-\t-\t7\n");
  p.sem("SOURCE_AFFINE_STOP3","AFFINE_RESULT",{"0","GLOBAL_INFINITY","-","-","-","0","0","1"});
  p.sem("SOURCE_AFFINE_STOP3","AFFINE_RESULT",{"1","FACTOR_X_SIGN_MINUS","-","-","5","1","1","2"});
  p.sem("SOURCE_AFFINE_STOP3","AFFINE_RESULT",{"2","FACTOR_DENOMINATOR","-","-","7","1","2","3"});

  p.pass("SOURCE_ROW_STOP2");
  p.operand(p.source,"SOURCE_ROW_STOP2",0,0,1,"ROW_ROOT",{"23","5","0","0"});
  p.operand(p.source,"SOURCE_ROW_STOP2",0,1,1,"ROW_ROOT",{"23","0","0","1"});
  p.count("SOURCE_ROW_STOP2","ROW_ROOT_GCDS",2);
  p.trace("SOURCE_ROW_STOP2","SOURCE_ROW_STOP2\tROW\t0\tFACTOR_ROW_ROOT\t5\n");
  p.trace("SOURCE_ROW_STOP2","SOURCE_ROW_STOP2\tROW\t1\tFULL_ROW_ROOT\t23\n");
  p.sem("SOURCE_ROW_STOP2","ROW_ROOT_RESULT",{"0","FACTOR_ROW_ROOT","5","0","0","1"});
  p.sem("SOURCE_ROW_STOP2","ROW_ROOT_RESULT",{"1","FULL_ROW_ROOT","-","0","1","1"});
}

using ModelMask = std::array<uint64_t, 5>;

struct ModelPiece {
  cpp_int q;
  uint16_t left = 0;
  uint16_t right = 0;
};

struct ModelBlock {
  cpp_int q = 1;
  std::vector<uint16_t> exponent;
  bool square = false;
  cpp_int root = 0;
};

void model_flip(ModelMask& mask, size_t bit) {
  mask[bit / 64] ^= UINT64_C(1) << (bit % 64);
}

bool model_bit(const ModelMask& mask, size_t bit) {
  return ((mask[bit / 64] >> (bit % 64)) & 1U) != 0;
}

bool model_zero(const ModelMask& mask) {
  return std::all_of(mask.begin(), mask.end(), [](uint64_t x) { return x == 0; });
}

void model_xor(ModelMask& target, const ModelMask& source) {
  for (size_t i = 0; i != target.size(); ++i) target[i] ^= source[i];
}

cpp_int model_inverse(cpp_int a, const cpp_int& modulus) {
  cpp_int old_r = modulus, r = modz(a, modulus), old_t = 0, t = 1;
  while (r != 0) {
    cpp_int q = old_r / r;
    cpp_int next_r = old_r - q * r;
    cpp_int next_t = old_t - q * t;
    old_r = r;
    r = next_r;
    old_t = t;
    t = next_t;
  }
  if (old_r != 1) throw Failure("MODEL_INVERSE");
  return modz(old_t, modulus);
}

class CounterModel {
 public:
  CounterModel(Packet& packet, std::string fixture, cpp_int modulus,
               const std::vector<cpp_int>& rows,
               const std::vector<cpp_int>& square_roots)
      : packet_(packet), fixture_(std::move(fixture)), modulus_(std::move(modulus)),
        rows_(rows), roots_(square_roots), row_count_(rows.size()) {
    if (rows_.size() != roots_.size() || rows_.size() > 64)
      throw Failure("MODEL_INPUT_WIDTH");
    tree_.fill(1);
  }

  void run() {
    for (size_t row = 0; row != rows_.size(); ++row) insert(row, rows_[row]);
    std::vector<ModelBlock> blocks = finish();
    std::vector<ModelMask> equations;
    std::map<std::vector<uint64_t>, std::vector<size_t>> signature;
    for (const ModelBlock& block : blocks) {
      if (block.square) continue;
      ModelMask equation{};
      for (size_t row = 0; row != row_count_; ++row) {
        add("F271_PARITY_CELLS");
        if ((block.exponent[row] & 1U) != 0) model_flip(equation, row);
      }
      if (!model_zero(equation)) equations.push_back(equation);
    }
    size_t words = (equations.size() + 63) / 64;
    for (size_t row = 0; row != row_count_; ++row) {
      std::vector<uint64_t> value(words);
      for (size_t equation = 0; equation != equations.size(); ++equation)
        if (model_bit(equations[equation], row))
          value[equation / 64] |= UINT64_C(1) << (equation % 64);
      signature[value].push_back(row);
    }
    std::vector<ModelMask> low;
    for (const auto& entry : signature) {
      const auto& value = entry.first;
      const auto& index = entry.second;
      bool zero = std::all_of(value.begin(), value.end(),
                              [](uint64_t x) { return x == 0; });
      if (zero) {
        for (size_t row : index) {
          ModelMask mask{};
          model_flip(mask, row);
          low.push_back(mask);
        }
      } else if (index.size() > 1) {
        for (size_t i = 1; i != index.size(); ++i) {
          ModelMask mask{};
          model_flip(mask, index.front());
          model_flip(mask, index[i]);
          low.push_back(mask);
        }
      }
    }
    low = rref(std::move(low));
    std::vector<ModelMask> full = nullspace(equations);
    std::vector<ModelMask> quotient;
    for (ModelMask value : full) {
      for (const ModelMask& basis : low) reduce_by_pivot(value, basis);
      for (const ModelMask& basis : quotient) reduce_by_pivot(value, basis);
      if (!model_zero(value)) quotient.push_back(value);
    }
    quotient = rref(std::move(quotient));
    classify(low);
    classify(quotient);
  }

 private:
  Packet& packet_;
  std::string fixture_;
  cpp_int modulus_;
  const std::vector<cpp_int>& rows_;
  const std::vector<cpp_int>& roots_;
  size_t row_count_;
  std::array<ModelBlock, 2048> leaf_{};
  std::array<cpp_int, 4096> tree_{};

  void add(const std::string& counter, uint64_t amount = 1) {
    packet_.count(fixture_, counter, amount);
    if (counter == "F271_GF2_WORD_OPERATIONS") {
      if (packet_.gf2_ops > kGf2Cap - amount) throw Failure("GF2_CAP");
      packet_.gf2_ops += amount;
    }
  }

  cpp_int saturation(const cpp_int& u, const cpp_int& v) {
    add("F271_SATURATION_POWERS");
    add("F271_SCALAR_GCDS");
    return gcdz(u, powmod(v, bitlen(u), u));
  }

  std::vector<ModelPiece> same_support(const cpp_int& x, const cpp_int& y,
                                       const cpp_int* supplied) {
    add("F271_RECURSION_NODES");
    cpp_int d;
    if (supplied) d = *supplied;
    else {
      add("F271_SCALAR_GCDS");
      d = gcdz(x, y);
    }
    if (d <= 1) throw Failure("MODEL_SUPPORT_GCD");
    add("F271_REFINEMENT_DIVISIONS", 3);
    cpp_int x0 = x / d, y0 = y / d, A = 1, B = 1;
    if (x0 > 1) A = saturation(d, x0);
    if (y0 > 1) B = saturation(d, y0);
    cpp_int C = d / (A * B);
    std::vector<ModelPiece> result;
    if (A > 1) {
      auto child = same_support(x0, A, nullptr);
      for (const auto& z : child)
        result.push_back({z.q, uint16_t(z.left + z.right), z.right});
    }
    if (B > 1) {
      auto child = same_support(y0, B, nullptr);
      for (const auto& z : child)
        result.push_back({z.q, z.right, uint16_t(z.left + z.right)});
    }
    if (C > 1) result.push_back({C, 1, 1});
    return result;
  }

  std::vector<ModelPiece> two_base(const cpp_int& x, const cpp_int& y,
                                   const cpp_int& common) {
    add("F271_TOUCHES");
    cpp_int xs = saturation(x, y), ys = saturation(y, x);
    add("F271_REFINEMENT_DIVISIONS", 2);
    auto result = same_support(xs, ys, &common);
    if (x / xs > 1) result.push_back({x / xs, 1, 0});
    if (y / ys > 1) result.push_back({y / ys, 0, 1});
    return result;
  }

  void update(size_t slot) {
    size_t node = 2048 + slot;
    tree_[node] = leaf_[slot].q;
    while (node > 1) {
      node >>= 1;
      tree_[node] = tree_[2 * node] * tree_[2 * node + 1];
      add("F271_TREE_NODE_UPDATES");
    }
  }

  size_t vacant() const {
    for (size_t i = 0; i != leaf_.size(); ++i)
      if (leaf_[i].q == 1) return i;
    throw Failure("MODEL_TREE_FULL");
  }

  void assign(size_t slot, ModelBlock block) {
    add("F271_LEAF_ASSIGNMENTS");
    leaf_[slot] = std::move(block);
    update(slot);
  }

  void merge_sort(std::vector<ModelPiece>& value, bool final) {
    if (value.size() < 2) return;
    std::vector<ModelPiece> scratch(value.size());
    for (size_t width = 1; width < value.size(); width *= 2) {
      for (size_t begin = 0; begin < value.size(); begin += 2 * width) {
        size_t middle = std::min(begin + width, value.size());
        size_t end = std::min(begin + 2 * width, value.size());
        size_t left = begin, right = middle, target = begin;
        while (left < middle && right < end) {
          add(final ? "F271_FINAL_COMPARISONS" :
                      "F271_REPLACEMENT_COMPARISONS");
          add("F271_BLOCK_COMPARISONS");
          scratch[target++] = value[right].q < value[left].q ?
                              value[right++] : value[left++];
        }
        while (left < middle) scratch[target++] = value[left++];
        while (right < end) scratch[target++] = value[right++];
        for (size_t i = begin; i != end; ++i) value[i] = scratch[i];
      }
    }
  }

  void insert(size_t row, const cpp_int& input) {
    cpp_int residual = input;
    while (residual > 1) {
      add("F271_SCALAR_GCDS");
      cpp_int overlap = gcdz(residual, tree_[1]);
      if (overlap == 1) {
        std::vector<uint16_t> exponent(row_count_);
        exponent[row] = 1;
        assign(vacant(), {residual, std::move(exponent)});
        return;
      }
      size_t node = 1;
      cpp_int carried = overlap;
      for (unsigned depth = 0; depth != 11; ++depth) {
        add("F271_SCALAR_GCDS");
        cpp_int left = gcdz(residual, tree_[2 * node]);
        if (left > 1) {
          node *= 2;
          carried = left;
        } else {
          node = 2 * node + 1;
        }
      }
      size_t slot = node - 2048;
      if (leaf_[slot].q <= 1) throw Failure("MODEL_DESCENT");
      ModelBlock old = leaf_[slot];
      auto pieces = two_base(old.q, residual, carried);
      std::vector<ModelPiece> replacement;
      cpp_int next = 1;
      for (const auto& piece : pieces) {
        if (piece.left != 0) replacement.push_back(piece);
        else next *= powz(piece.q, piece.right);
      }
      merge_sort(replacement, false);
      if (replacement.empty()) throw Failure("MODEL_EMPTY_REPLACEMENT");
      bool first = true;
      for (const auto& piece : replacement) {
        std::vector<uint16_t> exponent(row_count_);
        for (size_t i = 0; i != row_count_; ++i) {
          uint32_t e = uint32_t(piece.left) * old.exponent[i] +
                       (i == row ? piece.right : 0);
          add("F271_EXPONENT_COORD_UPDATES");
          if (e > 360) throw Failure("MODEL_EXPONENT");
          exponent[i] = uint16_t(e);
        }
        size_t target = first ? slot : vacant();
        first = false;
        assign(target, {piece.q, std::move(exponent)});
      }
      residual = next;
    }
  }

  std::vector<ModelBlock> finish() {
    std::vector<ModelPiece> order;
    for (size_t i = 0; i != leaf_.size(); ++i)
      if (leaf_[i].q > 1) order.push_back({leaf_[i].q, uint16_t(i), 0});
    merge_sort(order, true);
    std::vector<ModelBlock> result;
    for (const auto& item : order) result.push_back(leaf_[item.left]);
    for (size_t row = 0; row != row_count_; ++row) {
      cpp_int rebuilt = 1;
      for (const auto& block : result) if (block.exponent[row] != 0) {
        add("F271_RECONSTRUCTION_INCIDENCES");
        rebuilt *= powz(block.q, block.exponent[row]);
      }
      if (rebuilt != rows_[row]) throw Failure("MODEL_RECONSTRUCTION");
    }
    cpp_int product = 1;
    for (const auto& block : result) product *= block.q;
    for (auto& block : result) {
      add("F271_TERMINAL_BLOCKS");
      add("F271_SCALAR_GCDS");
      if (gcdz(block.q, product / block.q) != 1)
        throw Failure("MODEL_TERMINAL");
      block.root = isqrtz(block.q);
      block.square = block.root * block.root == block.q;
    }
    return result;
  }

  void reduce_by_pivot(ModelMask& value, const ModelMask& basis) const {
    size_t pivot = 0;
    while (pivot < row_count_ && !model_bit(basis, pivot)) ++pivot;
    if (pivot < row_count_ && model_bit(value, pivot)) model_xor(value, basis);
  }

  std::vector<ModelMask> rref(std::vector<ModelMask> rows) {
    std::vector<ModelMask> output;
    std::array<int, 320> pivot;
    pivot.fill(-1);
    for (ModelMask value : rows) {
      for (size_t column = 0; column != row_count_; ++column) {
        add("F271_GF2_WORD_OPERATIONS");
        if (model_bit(value, column) && pivot[column] >= 0) {
          model_xor(value, output[size_t(pivot[column])]);
          add("F271_GF2_WORD_OPERATIONS", (row_count_ + 63) / 64);
        }
      }
      if (model_zero(value)) continue;
      size_t pc = 0;
      while (pc < row_count_ && !model_bit(value, pc)) ++pc;
      for (ModelMask& prior : output) if (model_bit(prior, pc)) {
        model_xor(prior, value);
        add("F271_GF2_WORD_OPERATIONS", (row_count_ + 63) / 64);
      }
      pivot[pc] = int(output.size());
      output.push_back(value);
    }
    std::sort(output.begin(), output.end(), [&](const ModelMask& a,
                                                const ModelMask& b) {
      size_t x = 0, y = 0;
      while (x < row_count_ && !model_bit(a, x)) ++x;
      while (y < row_count_ && !model_bit(b, y)) ++y;
      return x < y;
    });
    return output;
  }

  std::vector<ModelMask> nullspace(const std::vector<ModelMask>& equations) {
    std::array<ModelMask, 320> pivot{};
    std::array<bool, 320> used{};
    for (ModelMask value : equations) {
      for (size_t column = 0; column != row_count_; ++column) {
        add("F271_GF2_WORD_OPERATIONS");
        if (!model_bit(value, column)) continue;
        if (used[column]) {
          model_xor(value, pivot[column]);
          add("F271_GF2_WORD_OPERATIONS", (row_count_ + 63) / 64);
        } else {
          used[column] = true;
          pivot[column] = value;
          add("F271_GF2_WORD_OPERATIONS", (row_count_ + 63) / 64);
          break;
        }
      }
    }
    for (size_t column = row_count_; column-- > 0;) if (used[column]) {
      for (size_t lower = 0; lower != column; ++lower)
        if (used[lower] && model_bit(pivot[lower], column)) {
          model_xor(pivot[lower], pivot[column]);
          add("F271_GF2_WORD_OPERATIONS", (row_count_ + 63) / 64);
        }
    }
    std::vector<ModelMask> result;
    for (size_t free = 0; free != row_count_; ++free) if (!used[free]) {
      ModelMask value{};
      model_flip(value, free);
      for (size_t column = 0; column != row_count_; ++column)
        if (used[column] && model_bit(pivot[column], free))
          model_flip(value, column);
      result.push_back(value);
    }
    return result;
  }

  void classify(const std::vector<ModelMask>& basis) {
    for (const ModelMask& mask : basis) {
      cpp_int selected = 1, modular = 1;
      for (size_t row = 0; row != row_count_; ++row)
        if (model_bit(mask, row)) {
          add("SELECTED_EXACT_PRODUCTS");
          add("SELECTED_MODULAR_PRODUCTS");
          selected *= rows_[row];
          modular = modular * roots_[row] % modulus_;
        }
      add("INTEGER_SQUARE_ROOTS");
      cpp_int exact = isqrtz(selected);
      if (exact * exact != selected) throw Failure("MODEL_EXACT_ROOT");
      add("MODULAR_INVERSIONS");
      cpp_int rho = exact % modulus_ * model_inverse(modular, modulus_) % modulus_;
      if (rho * rho % modulus_ != 1) throw Failure("MODEL_NORMALIZED_ROOT");
      add("SIGNED_RELATION_GCDS", 2);
      cpp_int minus = gcdz(rho - 1, modulus_);
      cpp_int plus = gcdz(rho + 1, modulus_);
      if (rho != 1 && rho != modulus_ - 1) {
        if (!((minus > 1 && minus < modulus_) ||
              (plus > 1 && plus < modulus_)))
          throw Failure("MODEL_ROOT_CLASS");
        add("FACTOR_EVENT_LINES");
      }
      add("BASIS_RECORDS");
    }
  }
};

void build_decoder_fixtures(Packet& p, std::vector<uint64_t>& primes,
                            std::vector<unsigned>& exponents,
                            std::vector<cpp_int>& rows, cpp_int& root64) {
  p.pass("DECODER_SUPPORT3");
  const std::array<uint64_t,3> a3{{1891,4681,9211}}, v3{{1,1,4}};
  for (uint64_t i=0;i!=3;++i)
    p.operand(p.decoder,"DECODER_SUPPORT3",0,i,1,"DECODER_ROW",
              {hex64(i),"f",hex64(a3[i]),hex64(v3[i])});
  p.sem("DECODER_SUPPORT3","DECODER_SUMMARY",{"3","3","2","1","0","1","1","PASS"});
  p.sem("DECODER_SUPPORT3","KERNEL_VECTOR",{"0","0000000000000007","0000000000000000","0000000000000000","0000000000000000","0000000000000000","FULL"});
  p.sem("DECODER_SUPPORT3","BASIS_VECTOR",{"Q","0","0000000000000007","0000000000000000","0000000000000000","0000000000000000","0000000000000000","5"});
  p.sem("DECODER_SUPPORT3","BASIS_ROOT",{"Q","0","45b65","4","4","3","5","STRUCTURAL_Q_NON_GLOBAL"});
  p.sem("DECODER_SUPPORT3","CERTIFICATE",{"ROOT_CONGRUENCES","1"});
  CounterModel(p,"DECODER_SUPPORT3",15,
               {cpp_int(a3[0]),cpp_int(a3[1]),cpp_int(a3[2])},
               {cpp_int(v3[0]),cpp_int(v3[1]),cpp_int(v3[2])}).run();

  p.pass("DECODER_SUPPORT64");
  primes=support_primes(p.prime_candidates);
  exponents.resize(64);
  rows.resize(64);
  root64=1;
  for (uint64_t i=0;i!=128;++i)
    p.operand(p.decoder,"DECODER_SUPPORT64",0,i,1,"SUPPORT64_PRIME",
              {i<64?"0":"1",hex64(i%64),hex64(primes[i])});
  for (uint64_t i=0;i!=64;++i) {
    cpp_int base=cpp_int(primes[i])*primes[(i+1)%64];
    cpp_int r=primes[64+i];
    unsigned e=0;
    cpp_int row=base;
    while (bitlen(row*r*r)<=361) { row*=r*r; ++e; }
    if (e==0) throw Failure("SUPPORT64_EXPONENT");
    exponents[i]=e; rows[i]=row;
    root64*=cpp_int(primes[i])*powz(r,e);
    p.operand(p.decoder,"DECODER_SUPPORT64",1,i,1,"SUPPORT64_EXPONENT",
              {hex64(i),hex64(e)});
    p.operand(p.decoder,"DECODER_SUPPORT64",2,i,1,"DECODER_ROW",
              {hex64(i),"f",hexz(row),i==0?"4":"1"});
    p.sem("DECODER_SUPPORT64","EXPONENT",
          {std::to_string(i),std::to_string(e),std::to_string(bitlen(row)),"1",hexz(row)});
  }
  for (uint64_t i=0;i!=128;++i)
    p.sem("DECODER_SUPPORT64","PRIME",
          {i<64?"0":"1",std::to_string(i%64),hex64(primes[i]),"1","1"});
  p.sem("DECODER_SUPPORT64","DECODER_SUMMARY",{"64","128","63","1","0","1","1","PASS"});
  p.sem("DECODER_SUPPORT64","KERNEL_VECTOR",{"0","ffffffffffffffff","0000000000000000","0000000000000000","0000000000000000","0000000000000000","FULL"});
  p.sem("DECODER_SUPPORT64","BASIS_VECTOR",{"Q","0","ffffffffffffffff","0000000000000000","0000000000000000","0000000000000000","0000000000000000","5"});
  p.sem("DECODER_SUPPORT64","BASIS_ROOT",{"Q","0","1","4","4","3","5","STRUCTURAL_Q_NON_GLOBAL"});
  p.sem("DECODER_SUPPORT64","CERTIFICATE",{"SUPPORT64_PRIMES_COMPLETE","1"});
  p.sem("DECODER_SUPPORT64","CERTIFICATE",{"SUPPORT64_EXPONENTS_MAXIMAL","1"});
  p.sem("DECODER_SUPPORT64","CERTIFICATE",{"A64_EQUALS_R64_SQUARED","1"});
  std::vector<cpp_int> roots64(64,1);roots64[0]=4;
  CounterModel(p,"DECODER_SUPPORT64",15,rows,roots64).run();

  p.pass("DECODER_EMPTY");
  p.operand(p.decoder,"DECODER_EMPTY",0,0,1,"PEEL_ROW",{"0","1f","1f"});
  p.operand(p.decoder,"DECODER_EMPTY",0,1,1,"PEEL_ROW",{"1","3d","3d"});
  p.sem("DECODER_EMPTY","PEEL_RESULT",{"0","1","1f","0","0"});
  p.sem("DECODER_EMPTY","PEEL_RESULT",{"1","1","3d","0","0"});
  p.sem("DECODER_EMPTY","DECODER_SUMMARY",{"0","0","0","0","0","0","1","EMPTY_KERNEL"});
  p.sem("DECODER_EMPTY","CERTIFICATE",{"PEEL_EXACTNESS","1"});
  p.count("DECODER_EMPTY","PRODUCT_MULTIPLICATIONS",1);
  p.count("DECODER_EMPTY","PEEL_EXACT_DIVISIONS",2);
  p.count("DECODER_EMPTY","PEEL_BASE_REMAINDERS",2);
  p.count("DECODER_EMPTY","PEEL_MODULAR_MULTIPLICATIONS",10);
  p.count("DECODER_EMPTY","PEEL_GCDS",2);
  p.count("DECODER_EMPTY","PEEL_RESIDUAL_DIVISIONS",2);
  p.count("DECODER_EMPTY","PEEL_SQUARE_TESTS",2);

  p.pass("DECODER_S0");
  p.operand(p.decoder,"DECODER_S0",0,0,1,"DECODER_ROW",{"0","f","1","1"});
  p.sem("DECODER_S0","DECODER_SUMMARY",{"1","0","0","1","1","0","1","PASS"});
  p.sem("DECODER_S0","KERNEL_VECTOR",{"0","0000000000000001","0000000000000000","0000000000000000","0000000000000000","0000000000000000","L"});
  p.sem("DECODER_S0","BASIS_VECTOR",{"L","0","0000000000000001","0000000000000000","0000000000000000","0000000000000000","0000000000000000","4"});
  p.sem("DECODER_S0","BASIS_ROOT",{"L","0","1","1","1","15","1","GLOBAL_PLUS"});
  p.sem("DECODER_S0","CERTIFICATE",{"TERMINAL_COPRIMALITY","1"});
  CounterModel(p,"DECODER_S0",15,{cpp_int(1)},{cpp_int(1)}).run();

  p.pass("DECODER_S1");
  p.operand(p.decoder,"DECODER_S1",0,0,1,"DECODER_ROW",{"0","f","1f","1"});
  p.sem("DECODER_S1","DECODER_SUMMARY",{"1","1","1","0","0","0","1","ZERO_KERNEL"});
  p.sem("DECODER_S1","CERTIFICATE",{"TERMINAL_COPRIMALITY","1"});
  CounterModel(p,"DECODER_S1",15,{cpp_int(31)},{cpp_int(1)}).run();

  p.pass("DENSE_GF2");
  for (uint64_t i=0;i!=1875;++i) {
    uint64_t m=i<63?((UINT64_C(1)<<i)^ (UINT64_C(1)<<63)):UINT64_MAX;
    p.operand(p.decoder,"DENSE_GF2",0,i,1,"GF2_MASK",{hex64(i),mask64(m)});
  }
  p.count("DENSE_GF2","F271_GF2_WORD_OPERATIONS",524288);
  p.sem("DENSE_GF2","GF2_SUMMARY",{"1875","232205","524288","63","1","ffffffffffffffff","123456789abcdef","PASS"});
  p.sem("DENSE_GF2","KERNEL_VECTOR",{"0","ffffffffffffffff","0000000000000000","0000000000000000","0000000000000000","0000000000000000","GF2"});
  p.sem("DENSE_GF2","CERTIFICATE",{"DENSE_KERNEL","1"});
}

void build_rate_fixtures(Packet& p, const std::vector<uint64_t>& primes,
                         const std::vector<cpp_int>& rows,
                         const cpp_int& root64) {
  const cpp_int q=cpp_int(1)<<360;
  const cpp_int f520=[](){cpp_int a=0,b=1;for(int i=0;i<520;++i){cpp_int c=a+b;a=b;b=c;}return a;}();
  const cpp_int f521=[](){cpp_int a=0,b=1;for(int i=0;i<521;++i){cpp_int c=a+b;a=b;b=c;}return a;}();
  cpp_int W=1,A64=1;
  // The first 1,875 primes for terminal/rate fixtures are generated by a
  // deterministic complete sieve bounded by the registered candidate cap.
  std::vector<uint64_t> first;
  for(uint64_t n=2;first.size()!=1875;++n) {
    if(++p.prime_candidates>kPrimeCandidateCap) throw Failure("PRIME_CAP");
    if(prime_small(n)) first.push_back(n);
  }
  for(uint64_t x:first) W*=x;
  for(const cpp_int& x:rows) A64*=x;
  if(A64!=root64*root64) throw Failure("A64_ROOT");

  auto start=[&](const std::string& n){p.pass(n);};
  start("RATE_GCD");
  p.operand(p.rate,"RATE_GCD",0,0,65536,"GCD",{hexz(f520),hexz(f521)});
  p.operand(p.rate,"RATE_GCD",0,1,65536,"GCD",{hexz(W),hexz(f521)});
  p.operand(p.rate,"RATE_GCD",0,2,65536,"GCD",{hexz(q),hexz(cpp_int(1)<<359)});
  p.operand(p.rate,"RATE_GCD",0,3,65536,"GCD",{hexz((cpp_int(1)<<361)-1),hexz((cpp_int(1)<<360)+1)});
  p.count("RATE_GCD","F271_SCALAR_GCDS",262144);
  p.sem("RATE_GCD","AGGREGATE",{"CALLS","262144"});

  start("RATE_SAT");
  const std::array<std::pair<cpp_int,cpp_int>,4> sat{{{q,2},{3*(cpp_int(1)<<358),6},{powz(3,227),powz(3,226)},{(cpp_int(1)<<180)*powz(3,113),6}}};
  for(uint64_t i=0;i!=4;++i)p.operand(p.rate,"RATE_SAT",0,i,65536,"SAT",{hexz(sat[i].first),hexz(sat[i].second)});
  p.count("RATE_SAT","F271_SCALAR_GCDS",262144);p.count("RATE_SAT","F271_SATURATION_POWERS",262144);
  p.sem("RATE_SAT","AGGREGATE",{"CALLS","262144"});

  start("RATE_DIV");
  const std::array<std::pair<cpp_int,cpp_int>,4> div{{{q,cpp_int(1)<<180},{3*(cpp_int(1)<<358),3},{powz(3,227),powz(3,113)},{(cpp_int(1)<<180)*powz(3,113),6}}};
  for(uint64_t i=0;i!=4;++i)p.operand(p.rate,"RATE_DIV",0,i,65536,"DIV",{hexz(div[i].first),hexz(div[i].second)});
  p.count("RATE_DIV","F271_REFINEMENT_DIVISIONS",262144);p.sem("RATE_DIV","AGGREGATE",{"CALLS","262144"});

  start("RATE_TREE");
  p.operand(p.rate,"RATE_TREE",0,0,32768,"TREE_TOGGLE",{"0","2","4"});
  p.operand(p.rate,"RATE_TREE",0,1,32768,"TREE_TOGGLE",{"0","4","2"});
  p.count("RATE_TREE","F271_LEAF_ASSIGNMENTS",65536);p.count("RATE_TREE","F271_TREE_NODE_UPDATES",720896);
  p.sem("RATE_TREE","AGGREGATE",{"CALLS","720896"});

  start("RATE_RECON");
  const std::array<std::array<uint64_t,3>,4> rec{{{{3,2,358}},{{5,3,225}},{{7,5,152}},{{11,7,125}}}};
  for(uint64_t i=0;i!=4;++i)p.operand(p.rate,"RATE_RECON",0,i,65536,"RECON",{hex64(rec[i][0]),hex64(rec[i][1]),hex64(rec[i][2])});
  p.count("RATE_RECON","F271_RECONSTRUCTION_INCIDENCES",262144);p.sem("RATE_RECON","AGGREGATE",{"CALLS","262144"});

  start("RATE_TERMINAL");
  for(uint64_t i=0;i!=1875;++i)p.operand(p.rate,"RATE_TERMINAL",0,i,1,"TERMINAL_BLOCK",{hex64(i),hex64(first[i])});
  p.count("RATE_TERMINAL","F271_TERMINAL_BLOCKS",1875);p.count("RATE_TERMINAL","F271_SCALAR_GCDS",1875);
  p.sem("RATE_TERMINAL","AGGREGATE",{"CALLS","1875"});p.sem("RATE_TERMINAL","CERTIFICATE",{"TERMINAL_COPRIMALITY","1"});

  start("RATE_COMPARE");
  const std::array<std::pair<cpp_int,cpp_int>,4> cmp{{{q,q-1},{q-1,q},{powz(3,227),powz(3,227)-1},{powz(3,227)-1,powz(3,227)}}};
  for(uint64_t i=0;i!=4;++i)p.operand(p.rate,"RATE_COMPARE",0,i,65536,"COMPARE",{hexz(cmp[i].first),hexz(cmp[i].second)});
  p.count("RATE_COMPARE","F271_BLOCK_COMPARISONS",262144);p.sem("RATE_COMPARE","AGGREGATE",{"CALLS","262144"});

  start("RATE_IO");
  // 0xa5 is the single source-registered byte.  D18 permits any canonical
  // byte, but once emitted this literal becomes immutable fixture evidence.
  p.operand(p.rate,"RATE_IO",0,0,1,"IO_BYTES",{"4000000","a5"});
  p.count("RATE_IO","IO_BYTES",67108864);
  std::string chunk(1<<20,static_cast<char>(0xa5));Sha256 ios;
  for(int i=0;i!=64;++i)ios.update(chunk);
  p.sem("RATE_IO","AGGREGATE",{"BYTE_COUNT","67108864"});
  p.sem("RATE_IO","AGGREGATE",{"STREAM_SHA256",ios.finish()});
  p.sem("RATE_IO","CERTIFICATE",{"TRACE_MATCH","1"});

  start("RATE_NODE");
  p.operand(p.rate,"RATE_NODE",0,0,65536,"SAME_SUPPORT",{hexz(q),hexz(q),hexz(q)});
  p.count("RATE_NODE","F271_RECURSION_NODES",65536);
  p.count("RATE_NODE","F271_REFINEMENT_DIVISIONS",196608);
  p.sem("RATE_NODE","AGGREGATE",{"RETURNED_BLOCKS","65536"});
  for(uint64_t i=0;i!=65536;++i)p.trace("RATE_NODE","RATE_NODE\t"+hexz(q)+"\t1\t1\n");

  start("RATE_TOUCH");
  p.operand(p.rate,"RATE_TOUCH",0,0,65536,"TWO_BASE",{hexz(q),hexz(q),hexz(q)});
  p.count("RATE_TOUCH","F271_TOUCHES",65536);p.count("RATE_TOUCH","F271_RECURSION_NODES",65536);
  p.count("RATE_TOUCH","F271_SCALAR_GCDS",131072);p.count("RATE_TOUCH","F271_SATURATION_POWERS",131072);
  p.count("RATE_TOUCH","F271_REFINEMENT_DIVISIONS",327680);
  p.sem("RATE_TOUCH","AGGREGATE",{"RETURNED_BLOCKS","65536"});
  for(uint64_t i=0;i!=65536;++i)p.trace("RATE_TOUCH","RATE_TOUCH\t"+hexz(q)+"\t1\t1\n");

  start("RATE_LEAF");
  p.operand(p.rate,"RATE_LEAF",0,0,131072,"LEAF_ASSIGN",{"2","0000000000000001"});
  p.operand(p.rate,"RATE_LEAF",0,1,131072,"LEAF_ASSIGN",{"4","8000000000000000"});
  p.count("RATE_LEAF","F271_LEAF_ASSIGNMENTS",262144);
  p.sem("RATE_LEAF","AGGREGATE",{"FINAL_VALUE","4"});p.sem("RATE_LEAF","AGGREGATE",{"FINAL_MASK","8000000000000000"});
  for(uint64_t i=0;i!=262144;++i)p.trace("RATE_LEAF","RATE_LEAF\t"+hex64(i)+"\t"+(i%2?"4\t8000000000000000\n":"2\t0000000000000001\n"));

  start("RATE_EXP");
  const std::array<std::array<uint64_t,4>,4> exp{{{{1,359,1,0}},{{2,179,1,0}},{{1,1,359,1}},{{17,0,343,1}}}};
  const std::array<uint64_t,4> expout{{359,358,360,343}};
  for(uint64_t i=0;i!=4;++i)p.operand(p.rate,"RATE_EXP",0,i,65536,"EXP_UPDATE",{hex64(exp[i][0]),hex64(exp[i][1]),hex64(exp[i][2]),hex64(exp[i][3])});
  p.count("RATE_EXP","F271_EXPONENT_COORD_UPDATES",262144);p.sem("RATE_EXP","AGGREGATE",{"OUTPUT_SUM","93061120"});p.sem("RATE_EXP","AGGREGATE",{"OUTPUT_XOR","0"});
  for(uint64_t i=0;i!=262144;++i)p.trace("RATE_EXP","RATE_EXP\t"+hex64(i)+"\t"+hex64(expout[i%4])+"\n");

  start("RATE_PARITY");
  for(uint64_t i=0;i!=4;++i)p.operand(p.rate,"RATE_PARITY",0,i,65536,"PARITY_CELL",{hex64(i),hex64(std::array<uint64_t,4>{{0,1,359,360}}[i])});
  p.count("RATE_PARITY","F271_PARITY_CELLS",262144);p.sem("RATE_PARITY","AGGREGATE",{"ONE_BITS","131072"});p.sem("RATE_PARITY","AGGREGATE",{"EMITTED_MASKS","4096"});
  for(uint64_t i=0;i!=4096;++i)p.trace("RATE_PARITY","RATE_PARITY\t"+hex64(i)+"\t6666666666666666\n");

  start("RATE_GF2");
  for(uint64_t i=0;i!=1875;++i){uint64_t m=i<63?((UINT64_C(1)<<i)^(UINT64_C(1)<<63)):UINT64_MAX;p.operand(p.rate,"RATE_GF2",0,i,1,"GF2_MASK",{hex64(i),mask64(m)});}
  p.count("RATE_GF2","F271_GF2_WORD_OPERATIONS",524288);p.sem("RATE_GF2","AGGREGATE",{"RANK","63"});p.sem("RATE_GF2","AGGREGATE",{"KERNEL_DIMENSION","1"});
  p.trace("RATE_GF2","RATE_GF2\t232205\t3f\tffffffffffffffff\t123456789abcdef\n");

  start("RATE_EXACT_PRODUCT");
  for(uint64_t i=0;i!=64;++i)p.operand(p.rate,"RATE_EXACT_PRODUCT",0,i,1024,"EXACT_FACTOR",{hex64(i),hexz(rows[i])});
  p.count("RATE_EXACT_PRODUCT","SELECTED_EXACT_PRODUCTS",65536);p.sem("RATE_EXACT_PRODUCT","AGGREGATE",{"FINAL_VALUE",hexz(A64)});
  for(uint64_t i=0;i!=1024;++i)p.trace("RATE_EXACT_PRODUCT","RATE_EXACT_PRODUCT\t"+hex64(i)+"\t"+hexz(A64)+"\n");

  start("RATE_MOD_PRODUCT");
  for(uint64_t i=0;i!=64;++i)p.operand(p.rate,"RATE_MOD_PRODUCT",0,i,4096,"MOD_FACTOR",{hex64(i),i==0?"4":"1","f"});
  p.count("RATE_MOD_PRODUCT","SELECTED_MODULAR_PRODUCTS",262144);p.sem("RATE_MOD_PRODUCT","AGGREGATE",{"FINAL_VALUE","4"});
  for(uint64_t i=0;i!=4096;++i)p.trace("RATE_MOD_PRODUCT","RATE_MOD_PRODUCT\t"+hex64(i)+"\t4\n");

  start("RATE_ISQRT");
  p.operand(p.rate,"RATE_ISQRT",0,0,256,"ISQRT",{hexz(A64)});p.count("RATE_ISQRT","INTEGER_SQUARE_ROOTS",256);p.sem("RATE_ISQRT","AGGREGATE",{"FINAL_VALUE",hexz(root64)});
  for(uint64_t i=0;i!=256;++i)p.trace("RATE_ISQRT","RATE_ISQRT\t"+hex64(i)+"\t"+hexz(root64)+"\n");

  start("RATE_INVERSE");
  p.operand(p.rate,"RATE_INVERSE",0,0,262144,"INVERSE",{"4","f"});p.count("RATE_INVERSE","MODULAR_INVERSIONS",262144);p.sem("RATE_INVERSE","AGGREGATE",{"OUTPUT_SUM","1048576"});p.sem("RATE_INVERSE","AGGREGATE",{"OUTPUT_XOR","0"});
  for(uint64_t i=0;i!=262144;++i)p.trace("RATE_INVERSE","RATE_INVERSE\t"+hex64(i)+"\t4\n");

  start("RATE_SIGNED");
  p.operand(p.rate,"RATE_SIGNED",0,0,131072,"SIGNED",{"4","f"});p.count("RATE_SIGNED","SIGNED_RELATION_GCDS",262144);p.sem("RATE_SIGNED","AGGREGATE",{"CALLS","262144"});
  for(uint64_t i=0;i!=131072;++i)p.trace("RATE_SIGNED","RATE_SIGNED\t"+hex64(i)+"\t3\t5\n");

  start("RATE_BASIS_RECORD");
  p.operand(p.rate,"RATE_BASIS_RECORD",0,0,65536,"BASIS_RECORD",
            {"ffffffffffffffff","0000000000000000","0000000000000000","0000000000000000","0000000000000000","5","0","1","4","4","3","5","3"});
  p.count("RATE_BASIS_RECORD","BASIS_RECORDS",65536);p.sem("RATE_BASIS_RECORD","AGGREGATE",{"RESULT_RECORDS","65536"});
  const std::string br="F265-D18\tfixture\t60\trandom\t0\tQ\t0\tffffffffffffffff\t0000000000000000\t0000000000000000\t0000000000000000\t0000000000000000\t1\t4\t4\t3\t5\tSTRUCTURAL_Q_NON_GLOBAL\n";
  for(uint64_t i=0;i!=65536;++i)p.trace("RATE_BASIS_RECORD",br);
}

std::string theory_root() {
  static const std::array<std::pair<const char*,const char*>,23> lines{{
      {"D09_DRAFT_ALGEBRA.md","93ee6021b969a3624cf499df5e18ea9c262e2a095a6b0634644cc1d69ee8030d"},
      {"D09_DRAFT_PREREGISTRATION.md","3b499578678a0f71c75f52608e53f2fba7f390fb5a09a95bc20c61d09fe1c0a4"},
      {"D10_DRAFT_ALGEBRA.md","aab2397c601b645f71da0bc79a8f58ed9ef79ea984fa7f7458ab2a49582a17a7"},
      {"D10_DRAFT_PREREGISTRATION.md","be7e2a05a1eac6659000cdfe71469697d76b867b42cb60c1c244b06ec63afb6e"},
      {"D11_DRAFT_ALGEBRA.md","a177438e425a20550342e7efa94ec1f70d30f40fe204640f983435dc36554f27"},
      {"D11_DRAFT_PREREGISTRATION.md","9b477799e006a9b2bb49eebcf062917f1a3c91a9852ce8fbe825fcea1a1df23e"},
      {"D11_HOSTILE_THEORY_AUDIT.md","777ccd163959a7ec4e14bdcd3c9d12fc1d58732207f12520806e1ad2a2705246"},
      {"D12_DRAFT_ALGEBRA.md","eae660da5a5c5344b83ccd99301cfb4f2db89d5c259cf73194f85892e2d7dcb0"},
      {"D12_DRAFT_PREREGISTRATION.md","65682542478a2c2270f3657d2c741ea253445ad3cf160758449a0ce21e806ecd"},
      {"D13_DRAFT_ALGEBRA.md","915ec124f6be79a1530af3df628f8c65eaa5bde845f073f67f5077e66258ea9c"},
      {"D13_DRAFT_PREREGISTRATION.md","42667461ac3a21820f3ea1d5de545d17ff03c719a38cd405dbdb0e91ff083c17"},
      {"D14_DRAFT_ALGEBRA.md","42690a13d5a0fade1dd644bf29d299d9bab3b5cdd6a68d08354f1e9a5c6fb4f6"},
      {"D14_DRAFT_PREREGISTRATION.md","4b02e30cfe2986fbc04dbf8c4faf22743c18acb1a64d2a07b30eefe2c6338b9b"},
      {"D14_HOSTILE_THEORY_AUDIT.md","b7067c104eaf96dfa81d7bd08dcc9326e7616016fb66202c078bf1c2ea5ef03e"},
      {"D15_DRAFT_ALGEBRA.md","563293afda1cf4d183b4d70ec30da60d0339086a52d9395df8b4d70d1e7ceeb6"},
      {"D15_DRAFT_PREREGISTRATION.md","9c3b7cc4d855e906d8c9f35bcf7846631d28d728138df07f0e812cf59c12798d"},
      {"D16_DRAFT_ALGEBRA.md","10d0e74462aac944a32dbc68404aa30c730d1f5b919f1fb4dd9e5a76ae92f5b2"},
      {"D16_DRAFT_PREREGISTRATION.md","8a27d1d3af5b6f46d5f90e2f3545928cde55932c8012c6829b7c67207bd556a2"},
      {"D17_DRAFT_ALGEBRA.md","e784dfb9d151e816ef43644e480e705c7414d4af34114250da7d399c319d46d3"},
      {"D17_DRAFT_PREREGISTRATION.md","acd92da342f2f88667a6b3cbfc3be1c13e9f8fdeabf4789020f3472319ed62d3"},
      {"D17_HOSTILE_THEORY_AUDIT.md","fc068523f2d45f1a853aac1db860fc64ccb66f6ffbf8f8f8b372a2ed3937f638"},
      {"D18_DRAFT_ALGEBRA.md","6a163bb4a642760f41a5d0fab0b5bbea40e936eef2dff93921b65fe7c7ce815d"},
      {"D18_DRAFT_PREREGISTRATION.md","944b0ffce0036f2970cb56e097735622b1aaf97f186a40673d812d244f3709f6"}}};
  std::string preimage;
  for (const auto& x : lines) preimage += std::string(x.first)+"\t"+x.second+"\n";
  return sha256(preimage);
}

std::string operand_file(const std::vector<Operand>& rows, uint64_t& logical,
                         std::map<std::string,std::string>& operand_digest) {
  std::string out="version\tfixture\tgroup\titem\tcycle_count\topcode";
  for(int i=0;i!=16;++i)out+="\targ"+std::to_string(i);
  out+='\n';
  std::map<std::string,uint64_t> expanded;
  std::vector<const Operand*> ordered;
  ordered.reserve(rows.size());
  for (const auto& r : rows) ordered.push_back(&r);
  std::sort(ordered.begin(), ordered.end(), [](const Operand* a,const Operand* b) {
    return std::make_tuple(fixture_rank(a->fixture),a->group,a->item) <
           std::make_tuple(fixture_rank(b->fixture),b->group,b->item);
  });
  for(const Operand* rp:ordered) {
    const Operand& r=*rp;
    out+=std::string(kVersion)+"\t"+r.fixture+"\t"+std::to_string(r.group)+"\t"+
         std::to_string(r.item)+"\t"+std::to_string(r.cycles)+"\t"+r.opcode;
    for(const auto& a:r.arg)out+='\t'+a;
    out+='\n';
  }
  // Groups are already canonical.  Expand by fixture/group/cycle/item.
  for(const char* f:kFixtures) {
    Sha256 h;uint64_t idx=0;
    std::map<uint64_t,std::vector<const Operand*>> groups;
    for(const auto& r:rows)if(r.fixture==f)groups[r.group].push_back(&r);
    for(auto& [g,v]:groups) {
      (void)g;std::sort(v.begin(),v.end(),[](auto a,auto b){return a->item<b->item;});
      uint64_t cycles=v.empty()?0:v.front()->cycles;
      for(const auto* r:v)if(r->cycles!=cycles)throw Failure("GROUP_CYCLES");
      for(uint64_t c=0;c!=cycles;++c)for(const auto* r:v) {
        std::string line=std::string(f)+"\t"+std::to_string(idx++)+"\t"+r->opcode;
        for(const auto& a:r->arg)line+='\t'+a;
        line+='\n';h.update(line);
      }
    }
    if(!groups.empty()) {operand_digest[f]=h.finish();logical+=idx;}
  }
  return out;
}

std::string semantics_file(Packet& p, std::map<std::string,std::string>& digest) {
  static const std::array<const char*,15> kind{{"STATUS","RANDOM_RESULT","AFFINE_RESULT","ROW_ROOT_RESULT","PEEL_RESULT","FACTOR_RESULT","DECODER_SUMMARY","KERNEL_VECTOR","BASIS_VECTOR","BASIS_ROOT","PRIME","EXPONENT","GF2_SUMMARY","AGGREGATE","CERTIFICATE"}};
  auto rank=[&](const std::string& x){for(size_t i=0;i!=kind.size();++i)if(x==kind[i])return i;throw Failure("SEM_KIND");};
  std::string out="version\tfixture\tordinal\tkind\tvalue0\tvalue1\tvalue2\tvalue3\tvalue4\tvalue5\tvalue6\tvalue7\n";
  for(size_t fi=0;fi!=kFixtures.size();++fi) {
    auto& s=p.fixture[fi].semantic;
    std::stable_sort(s.begin(),s.end(),[&](const Semantic&a,const Semantic&b){return rank(a.kind)<rank(b.kind);});
    Sha256 h;
    for(size_t i=0;i!=s.size();++i) {
      std::string line=std::string(kVersion)+"\t"+kFixtures[fi]+"\t"+std::to_string(i)+"\t"+s[i].kind;
      for(const auto& x:s[i].value)line+='\t'+x;
      line+='\n';out+=line;h.update(line);
    }
    digest[kFixtures[fi]]=h.finish();
  }
  return out;
}

bool absolute_path(const std::string& p) {
  if(p.size()<2||p.size()>1024||p[0]!='/'||p.back()=='/')return false;
  std::string part;
  for(size_t i=1;i<=p.size();++i) {
    if(i==p.size()||p[i]=='/') {
      if(part.empty()||part=="."||part=="..")return false;
      part.clear();continue;
    }
    unsigned char c=p[i];
    if(!(std::isalnum(c)||c=='_'||c=='-'||c=='.'))return false;
    part.push_back(static_cast<char>(c));
  }
  return true;
}

int open_root(const std::string& path) {
  int fd=open("/",O_RDONLY|O_DIRECTORY|O_CLOEXEC);
  if(fd<0)throw Failure("OPEN_SLASH");
  size_t pos=1;
  while(pos<path.size()) {
    size_t end=path.find('/',pos);if(end==std::string::npos)end=path.size();
    std::string c=path.substr(pos,end-pos);
    int next=openat(fd,c.c_str(),O_RDONLY|O_DIRECTORY|O_NOFOLLOW|O_CLOEXEC);
    int saved=errno;close(fd);errno=saved;
    if(next<0)throw Failure("OPEN_COMPONENT");
    struct stat st{};if(fstat(next,&st)||!S_ISDIR(st.st_mode)){close(next);throw Failure("ROOT_TYPE");}
    fd=next;pos=end+1;
  }
  return fd;
}

std::vector<std::string> members(int root) {
  int copy=dup(root);if(copy<0)throw Failure("DUP_ROOT");
  DIR* d=fdopendir(copy);if(!d){close(copy);throw Failure("FDOPENDIR");}
  std::vector<std::string> out;errno=0;
  while(dirent* e=readdir(d)) {std::string n=e->d_name;if(n!="."&&n!="..")out.push_back(n);}
  int saved=errno;if(closedir(d)!=0||saved!=0)throw Failure("READDIR");
  std::sort(out.begin(),out.end());return out;
}

void write_all(int fd,const std::string& data) {
  size_t off=0;while(off<data.size()) {ssize_t n=write(fd,data.data()+off,data.size()-off);if(n<=0)throw Failure("WRITE");off+=static_cast<size_t>(n);}
}

void atomic_file(int root,const std::string& name,const std::string& data,size_t cap) {
  if(data.size()>cap)throw Failure("FILE_CAP");
  std::string tmp="."+name+".tmp";
  int fd=openat(root,tmp.c_str(),O_WRONLY|O_CREAT|O_EXCL|O_NOFOLLOW|O_CLOEXEC,0600);
  if(fd<0)throw Failure("CREATE_TEMP");
  try {struct stat st{};if(fstat(fd,&st)||!S_ISREG(st.st_mode)||st.st_nlink!=1||st.st_uid!=geteuid()||(st.st_mode&0777)!=0600)throw Failure("TEMP_META");write_all(fd,data);if(fsync(fd))throw Failure("FSYNC_FILE");if(close(fd)){fd=-1;throw Failure("CLOSE_FILE");}fd=-1;
    int rd=openat(root,tmp.c_str(),O_RDONLY|O_NOFOLLOW|O_CLOEXEC);if(rd<0)throw Failure("VERIFY_OPEN");std::string got;std::array<char,65536>b{};for(;;){ssize_t n=read(rd,b.data(),b.size());if(n<0){close(rd);throw Failure("VERIFY_READ");}if(n==0)break;got.append(b.data(),static_cast<size_t>(n));}if(close(rd)||got!=data)throw Failure("VERIFY_BYTES");
    struct stat absent{};if(fstatat(root,name.c_str(),&absent,AT_SYMLINK_NOFOLLOW)==0||errno!=ENOENT)throw Failure("FINAL_EXISTS");if(renameat(root,tmp.c_str(),root,name.c_str()))throw Failure("RENAME");if(fsync(root))throw Failure("FSYNC_DIR");
  } catch(...) {if(fd>=0)close(fd);unlinkat(root,tmp.c_str(),0);throw;}
}

int run(int argc,char**argv) {
  if(!std::setlocale(LC_ALL,"C"))throw Failure("LOCALE");umask(077);
  if(argc!=5||std::string(argv[1])!="--mode"||std::string(argv[2])!="materialize"||std::string(argv[3])!="--output-root")throw Failure("CLI");
  std::string output=argv[4];if(!absolute_path(output))throw Failure("ABS");
  int root=open_root(output);struct stat rs{};if(fstat(root,&rs)||rs.st_uid!=geteuid()||(rs.st_mode&077)!=0||!members(root).empty()){close(root);throw Failure("OUTPUT_ROOT");}
  Packet p;build_source_fixtures(p);std::vector<uint64_t> primes;std::vector<unsigned> exponents;std::vector<cpp_int> rows;cpp_int root64;build_decoder_fixtures(p,primes,exponents,rows,root64);build_rate_fixtures(p,primes,rows,root64);
  uint64_t logical=0;std::map<std::string,std::string> operand_sha;
  std::string source=operand_file(p.source,logical,operand_sha);std::string decoder=operand_file(p.decoder,logical,operand_sha);std::string rate=operand_file(p.rate,logical,operand_sha);if(logical>kLogicalCap)throw Failure("LOGICAL_CAP");
  std::string counters="version\tfixture\tcounter\tvalue\n";
  for(size_t i=0;i!=kFixtures.size();++i)for(size_t j=0;j!=kCounters.size();++j)counters+=std::string(kVersion)+"\t"+kFixtures[i]+"\t"+kCounters[j]+"\t"+std::to_string(p.fixture[i].counter[j])+"\n";
  std::map<std::string,std::string> semantic_sha;std::string semantics=semantics_file(p,semantic_sha);
  uint64_t records=p.result_records,record_bytes=p.result_bytes;std::string digests="version\tfixture\toperand_sha256\tresult_fnv1a64\tresult_sha256\tsemantic_sha256\n";
  for(size_t i=0;i!=kFixtures.size();++i)if(p.fixture[i].traced){const auto& name=std::string(kFixtures[i]);const auto& fixture=p.fixture[i];std::ostringstream fnv;fnv<<std::hex<<std::setw(16)<<std::setfill('0')<<fixture.result_fnv;Sha256 digest=fixture.result_sha;digests+=std::string(kVersion)+"\t"+name+"\t"+operand_sha.at(name)+"\t"+fnv.str()+"\t"+digest.finish()+"\t"+semantic_sha.at(name)+"\n";}
  uint64_t payload=source.size()+decoder.size()+rate.size()+counters.size()+semantics.size()+digests.size();
  std::string attest="version\ttheory_root\tlogical_operands\tresult_records\tresult_bytes\tpayload_bytes\tstatus\n"+std::string(kVersion)+"\t"+theory_root()+"\t"+std::to_string(logical)+"\t"+std::to_string(records)+"\t"+std::to_string(record_bytes)+"\t"+std::to_string(payload)+"\tPASS\n";
  const std::array<std::pair<std::string,const std::string*>,7> files{{
      {"F265-D18.source_operands.tsv",&source},{"F265-D18.decoder_operands.tsv",&decoder},{"F265-D18.rate_operands.tsv",&rate},{"F265-D18.expected_counters.tsv",&counters},{"F265-D18.expected_semantics.tsv",&semantics},{"F265-D18.expected_digests.tsv",&digests},{"F265-D18.materializer_attestation.tsv",&attest}}};
  const std::array<size_t,7> caps{{1048576,4194304,4194304,1048576,1048576,1048576,65536}};
  std::string manifest;for(size_t i=0;i!=files.size();++i){atomic_file(root,files[i].first,*files[i].second,caps[i]);manifest+=sha256(*files[i].second)+"  "+files[i].first+"\n";}
  atomic_file(root,"F265-D18.PAYLOAD.sha256",manifest,65536);
  std::vector<std::string> expect;for(const auto& x:files)expect.push_back(x.first);expect.push_back("F265-D18.PAYLOAD.sha256");std::sort(expect.begin(),expect.end());if(members(root)!=expect)throw Failure("FINAL_MEMBERSHIP");
  struct stat end{};if(fstat(root,&end)||end.st_dev!=rs.st_dev||end.st_ino!=rs.st_ino||end.st_uid!=rs.st_uid||(end.st_mode&07777)!=(rs.st_mode&07777)){close(root);throw Failure("ROOT_IDENTITY");}if(close(root))throw Failure("CLOSE_ROOT");return 0;
}

}  // namespace

int main(int argc,char**argv) {
  try{return run(argc,argv);}catch(const std::exception& e){std::cerr<<"F265-D18 fixture materialization failed: "<<e.what()<<'\n';return 1;}
}
