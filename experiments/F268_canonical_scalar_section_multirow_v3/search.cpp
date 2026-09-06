#include <algorithm>
#include <array>
#include <atomic>
#include <chrono>
#include <cerrno>
#include <cmath>
#include <cstdint>
#include <cstring>
#include <fstream>
#include <functional>
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

namespace {

constexpr u64 MASTER_SEED = 0xF268CA110A5E5EEDULL;
constexpr const char* FAMILY_SYNTAX_SHA =
    "aea7c29e0c077c701ba8201ec6acb6ff8ca26adbccf1e3096f97b659604bc6ce";
constexpr int FAMILY_COUNT = 12;
constexpr int TEMPLATE_COUNT = 12;
constexpr int DISCOVERY_ROWS = 24;
constexpr int HELDOUT_ROWS = 48;
constexpr int MAX_ROWS = HELDOUT_ROWS;
constexpr int MAX_GCD_FREE_STEPS = 25000;
constexpr int MAX_BLOCKS = 4096;
constexpr int MAX_TOTAL_ROW_BITS = 65536;
constexpr int MAX_LOW_GENERATORS = 1176;
constexpr int MAX_RELATIONS = 48;
constexpr int MAX_RELATION_BITS = 1500000;
constexpr std::size_t MAX_BANK_EVIDENCE = 2097152;
constexpr u64 OUTPUT_CAP = 805306368ULL;
constexpr double F265_OBSERVED_PAIR_BUNDLES_PER_WALL_SECOND =
    714.637358152448;

[[noreturn]] void fail(const std::string& message) {
  throw std::runtime_error(message);
}

class ResourceReject : public std::runtime_error {
 public:
  explicit ResourceReject(const std::string& message)
      : std::runtime_error(message) {}
};

[[noreturn]] void reject_resource(const std::string& message) {
  throw ResourceReject(message);
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
    for (std::uint32_t word : state_) out << std::setw(8) << word;
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
  void compress(const unsigned char* bytes) {
    static constexpr std::uint32_t constants[64] = {
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
      w[i] = (std::uint32_t(bytes[4*i]) << 24) |
             (std::uint32_t(bytes[4*i+1]) << 16) |
             (std::uint32_t(bytes[4*i+2]) << 8) | bytes[4*i+3];
    for (int i = 16; i < 64; ++i) {
      auto s0 = rotr(w[i-15],7) ^ rotr(w[i-15],18) ^ (w[i-15] >> 3);
      auto s1 = rotr(w[i-2],17) ^ rotr(w[i-2],19) ^ (w[i-2] >> 10);
      w[i] = w[i-16] + s0 + w[i-7] + s1;
    }
    auto a=state_[0],b=state_[1],c=state_[2],d=state_[3];
    auto e=state_[4],f=state_[5],g=state_[6],h=state_[7];
    for (int i = 0; i < 64; ++i) {
      auto s1=rotr(e,6)^rotr(e,11)^rotr(e,25);
      auto ch=(e&f)^((~e)&g);
      auto t1=h+s1+ch+constants[i]+w[i];
      auto s0=rotr(a,2)^rotr(a,13)^rotr(a,22);
      auto maj=(a&b)^(a&c)^(b&c);
      auto t2=s0+maj;
      h=g;g=f;f=e;e=d+t1;d=c;c=b;b=a;a=t1+t2;
    }
    state_[0]+=a;state_[1]+=b;state_[2]+=c;state_[3]+=d;
    state_[4]+=e;state_[5]+=f;state_[6]+=g;state_[7]+=h;
  }
};

std::string sha256_bytes(const std::string& bytes) {
  Sha256 hash;
  hash.update(bytes);
  return hash.final_hex();
}

std::string read_file(const std::string& path) {
  std::ifstream input(path, std::ios::binary);
  require(bool(input), "open input: " + path);
  std::ostringstream out;
  out << input.rdbuf();
  require(input.good() || input.eof(), "read input: " + path);
  return out.str();
}

cpp_int absz(cpp_int value) {
  if (value < 0) value = -value;
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

cpp_int pow_small(cpp_int base, unsigned exponent) {
  cpp_int out = 1;
  while (exponent) {
    if (exponent & 1U) out *= base;
    base *= base;
    exponent >>= 1U;
  }
  return out;
}

cpp_int powmod(cpp_int base, cpp_int exponent, const cpp_int& modulus) {
  base = modz(base, modulus);
  cpp_int out = 1 % modulus;
  while (exponent > 0) {
    if ((exponent & 1) != 0) out = modz(out * base, modulus);
    base = modz(base * base, modulus);
    exponent >>= 1;
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
  u64 hash = mix64(seed ^ static_cast<u64>(value < 0));
  while (x != 0) {
    u64 limb = static_cast<u64>(x & std::numeric_limits<u64>::max());
    hash = mix64(hash ^ limb);
    x >>= 64;
  }
  return mix64(hash ^ static_cast<u64>(bitlen(value)));
}

cpp_int public_residue(const cpp_int& N, u64 syntax) {
  int bits = bitlen(N - 1);
  cpp_int value = 0;
  int produced = 0;
  u64 state = hash_cpp(N, mix64(MASTER_SEED ^ syntax));
  while (produced < bits + 64) {
    state = mix64(state);
    value |= cpp_int(state) << produced;
    produced += 64;
  }
  return 1 + modz(value, N - 1);
}

cpp_int parse_positive(const std::string& text) {
  require(!text.empty() && text.find_first_not_of("0123456789") == std::string::npos,
          "invalid positive integer syntax");
  cpp_int value(text);
  require(value > 0, "nonpositive integer");
  return value;
}

std::vector<std::string> split_tab(const std::string& line) {
  std::istringstream input(line);
  std::vector<std::string> fields;
  std::string field;
  while (std::getline(input, field, '\t')) fields.push_back(field);
  return fields;
}

struct Case {
  std::string split;
  std::string shape;
  int factor_bits = 0;
  int index = 0;
  cpp_int N;
};

std::vector<Case> parse_public_corpus(const std::string& path,
                                      const std::string& expected_split,
                                      const std::string& expected_digest) {
  std::string bytes = read_file(path);
  require(sha256_bytes(bytes) == expected_digest, "public corpus SHA mismatch");
  std::istringstream input(bytes);
  std::string line;
  require(bool(std::getline(input, line)) &&
          line == "version\tsplit\tshape\tfactor_bits\tindex\tN",
          "public corpus header");
  std::vector<Case> out;
  std::set<std::string> seen;
  while (std::getline(input, line)) {
    if (line.empty()) continue;
    auto f = split_tab(line);
    require(f.size() == 6 && f[0] == "F268-D03" && f[1] == expected_split,
            "public corpus row");
    require(f[2] == "random" || f[2] == "neighbor" || f[2] == "safe-safe" ||
            f[2] == "marker-control", "public shape");
    require(f[3].find_first_not_of("0123456789") == std::string::npos &&
            f[4].find_first_not_of("0123456789") == std::string::npos,
            "public numeric field");
    require(seen.insert(f[5]).second, "duplicate public modulus");
    int bits=std::stoi(f[3]),index=std::stoi(f[4]);
    require(bits>=3&&bits<=60&&index>=0,"public corpus bits/index");
    out.push_back({f[1], f[2], bits,index,parse_positive(f[5])});
  }
  require(!out.empty(), "empty public corpus");
  const std::vector<int> ordinary_bits=expected_split=="discovery"
      ?std::vector<int>{12,16,20,24,32}:std::vector<int>{40,48,56,60};
  int ordinary_target=expected_split=="discovery"?12:24;
  std::set<std::tuple<int,std::string,int>> syntax_rows;
  std::map<std::pair<int,std::string>,int> counts;
  for (const Case& c:out) {
    require(c.index<(c.shape=="marker-control"?2:ordinary_target),
            "corpus cell index");
    require(c.index>=0&&syntax_rows.insert({c.factor_bits,c.shape,c.index}).second,
            "duplicate corpus syntax row");
    ++counts[{c.factor_bits,c.shape}];
  }
  for (int bits:ordinary_bits)
    for (const char* shape:{"random","neighbor","safe-safe"})
      require(counts[{bits,shape}]==ordinary_target,"ordinary corpus cell");
  const std::set<int> marker_bits=expected_split=="discovery"
      ?std::set<int>{12,16,20,24}:std::set<int>{20,24,28,32};
  for (const auto& [cell,count]:counts) {
    if (cell.second!="marker-control") {
      require(std::find(ordinary_bits.begin(),ordinary_bits.end(),cell.first)!=
                  ordinary_bits.end(),"unexpected ordinary corpus cell");
    } else {
      require(marker_bits.count(cell.first)&&count>=1&&count<=2,
              "marker corpus cell");
    }
  }
  return out;
}

void authenticate_family_syntax(const std::string& path,
                                const std::string& expected_argument) {
  require(expected_argument == FAMILY_SYNTAX_SHA, "family digest argument mismatch");
  std::string bytes = read_file(path);
  require(sha256_bytes(bytes) == FAMILY_SYNTAX_SHA, "family syntax SHA mismatch");
  std::istringstream input(bytes);
  std::string line;
  require(bool(std::getline(input, line)) &&
          line == "kind\tid\tname\tbase_grammar\texponent_grammar\tmax_rows",
          "family syntax header");
  std::set<int> families, templates;
  while (std::getline(input, line)) {
    auto f = split_tab(line);
    require(f.size() == 6, "family syntax row width");
    int id = std::stoi(f[1]);
    if (f[0] == "family") {
      require(id >= 0 && id < FAMILY_COUNT && families.insert(id).second,
              "family syntax family ID");
    } else {
      require(f[0] == "template" && id >= 0 && id < TEMPLATE_COUNT &&
              templates.insert(id).second, "family syntax template ID");
    }
  }
  require(families.size() == FAMILY_COUNT && templates.size() == TEMPLATE_COUNT,
          "family syntax coverage");
}

struct Counter {
  u64 tests = 0, unit = 0, full = 0, proper = 0;
};

enum class EdgeType { NONE, MULTIPLY, INVERSE, COMPLEMENT };

struct Node {
  cpp_int base;
  std::string syntax;
  int group = -1;
  int role = -1;
  int orbit_i = -1;
  int orbit_j = -1;
  EdgeType edge = EdgeType::NONE;
  int parent_a = -1;
  int parent_b = -1;
};

struct Row {
  int id = -1;
  int node = -1;
  int family = -1;
  int exponent_tag = -1;
  cpp_int base, exponent, value, root, low, high;
  std::string syntax;
};

using Bits = std::vector<u64>;

struct Relation {
  std::string kind;
  Bits bits;
  cpp_int exact_root, supplied_root, normalized, gcd_minus, gcd_plus;
  std::string root_class;
  std::vector<int> templates;
};

struct Block {
  cpp_int value;
  std::vector<std::uint32_t> exponents;
};

struct Decoder {
  bool ok = false, resource_reject = false;
  std::string error;
  std::vector<Block> blocks;
  std::vector<Bits> equations;
  std::vector<Bits> kernel;
  u64 steps = 0, rank = 0;
};

struct BankResult {
  bool eligible = false, resource_reject = false;
  bool low_complete = false;
  std::string reject_reason;
  int family = -1;
  std::array<Counter, 8> counters{};
  bool any_factor = false, earlier_factor = false, strict_factor = false;
  std::string first_factor_label;
  cpp_int first_factor = 0;
  std::vector<Node> nodes;
  std::vector<Row> rows;
  std::vector<Block> blocks;
  std::vector<Relation> low_relations;
  std::vector<Relation> residual_relations;
  u64 useful_singletons = 0, useful_support_two = 0;
  u64 singleton_square_tests = 0, support_two_squareclass_tests = 0;
  u64 gcd_free_steps = 0, rank = 0, kernel_dim = 0;
  u64 low_dim = 0, residual_dim = 0;
  int relation_bits = 0;
};

cpp_int record_gcd(BankResult& bank, int stage, const cpp_int& value,
                   const cpp_int& N, const std::string& label) {
  require(stage >= 0 && stage < 8, "direct stage");
  cpp_int gcd = gcdz(value, N);
  Counter& counter = bank.counters[stage];
  ++counter.tests;
  if (gcd == 1) ++counter.unit;
  else if (gcd == N) ++counter.full;
  else {
    ++counter.proper;
    bank.any_factor = true;
    if (stage < 6) bank.earlier_factor = true;
    if (bank.first_factor == 0) {
      bank.first_factor = gcd;
      bank.first_factor_label = label;
    }
  }
  return gcd;
}

cpp_int exponent_for_tag(int tag, const cpp_int& N) {
  require(tag >= 0 && tag < 5, "exponent tag");
  if (tag == 0) return N - 1;
  if (tag == 1) return N + 1;
  if (tag == 2) return N * N - 1;
  if (tag == 3) return 2 * (N - 1);
  return 2 * (N + 1);
}

int frozen_row_count(const std::string& split,int family) {
  require(split=="discovery"||split=="heldout","bank split");
  require(family>=0&&family<FAMILY_COUNT,"bank family");
  if (family==10) return split=="discovery"?20:45;
  return split=="discovery"?DISCOVERY_ROWS:HELDOUT_ROWS;
}

bool bit_get(const Bits& bits, int column) {
  return ((bits[column >> 6] >> (column & 63)) & 1ULL) != 0;
}

void bit_flip(Bits& bits, int column) {
  bits[column >> 6] ^= 1ULL << (column & 63);
}

void bit_xor(Bits& left, const Bits& right) {
  require(left.size() == right.size(), "bit width mismatch");
  for (std::size_t i = 0; i < left.size(); ++i) left[i] ^= right[i];
}

bool bit_zero(const Bits& bits) {
  for (u64 word : bits) if (word) return false;
  return true;
}

int bit_weight(const Bits& bits) {
  int weight = 0;
  for (u64 word : bits) weight += __builtin_popcountll(word);
  return weight;
}

int first_bit(const Bits& bits, int columns) {
  for (int i = 0; i < columns; ++i) if (bit_get(bits, i)) return i;
  return -1;
}

struct BitBasis {
  int columns = 0;
  std::vector<Bits> pivot;
  explicit BitBasis(int count) : columns(count), pivot(count) {}
  Bits reduce(Bits value) const {
    for (int column = 0; column < columns; ++column)
      if (bit_get(value, column) && !pivot[column].empty())
        bit_xor(value, pivot[column]);
    return value;
  }
  bool insert(Bits value) {
    value = reduce(std::move(value));
    int column = first_bit(value, columns);
    if (column < 0) return false;
    pivot[column] = std::move(value);
    return true;
  }
  int dimension() const {
    int count = 0;
    for (const Bits& row : pivot) count += !row.empty();
    return count;
  }
};

bool same_square_class(const cpp_int& a, const cpp_int& b,
                       cpp_int* exact_root = nullptr) {
  cpp_int gcd = gcdz(a, b), left = a / gcd, right = b / gcd;
  cpp_int s, t;
  if (!squarez(left, &s) || !squarez(right, &t)) return false;
  cpp_int root = gcd * s * t;
  require(root * root == a * b, "support-two root verification");
  if (exact_root) *exact_root = root;
  return true;
}

Decoder decode_rows(const std::vector<Row>& rows) {
  Decoder decoder;
  int count = static_cast<int>(rows.size());
  int total_bits = 0;
  for (const Row& row : rows) total_bits += bitlen(row.value);
  if (total_bits > MAX_TOTAL_ROW_BITS) {
    decoder.resource_reject = true;
    decoder.error = "TOTAL_ROW_BITS_CAP";
    return decoder;
  }
  for (int i = 0; i < count; ++i) {
    if (rows[i].value == 1) continue;
    Block block{rows[i].value, std::vector<std::uint32_t>(count, 0)};
    block.exponents[i] = 1;
    decoder.blocks.push_back(std::move(block));
  }
  bool changed = true;
  while (changed) {
    changed = false;
    for (std::size_t i = 0; i < decoder.blocks.size() && !changed; ++i) {
      for (std::size_t j = i + 1; j < decoder.blocks.size(); ++j) {
        cpp_int gcd = gcdz(decoder.blocks[i].value, decoder.blocks[j].value);
        if (gcd == 1) continue;
        Block left = decoder.blocks[i], right = decoder.blocks[j];
        cpp_int left_cofactor = left.value / gcd;
        cpp_int right_cofactor = right.value / gcd;
        std::vector<std::uint32_t> shared(count);
        for (int k = 0; k < count; ++k) {
          u64 sum = static_cast<u64>(left.exponents[k]) + right.exponents[k];
          require(sum <= std::numeric_limits<std::uint32_t>::max(),
                  "block exponent overflow");
          shared[k] = static_cast<std::uint32_t>(sum);
        }
        decoder.blocks.erase(decoder.blocks.begin() + j);
        decoder.blocks.erase(decoder.blocks.begin() + i);
        if (left_cofactor > 1)
          decoder.blocks.push_back({left_cofactor, std::move(left.exponents)});
        if (right_cofactor > 1)
          decoder.blocks.push_back({right_cofactor, std::move(right.exponents)});
        decoder.blocks.push_back({gcd, std::move(shared)});
        ++decoder.steps;
        if (decoder.steps > MAX_GCD_FREE_STEPS ||
            decoder.blocks.size() > MAX_BLOCKS) {
          decoder.resource_reject = true;
          decoder.error = "GCD_FREE_CAP";
          return decoder;
        }
        changed = true;
        break;
      }
    }
  }
  std::sort(decoder.blocks.begin(), decoder.blocks.end(),
            [](const Block& a, const Block& b) { return a.value < b.value; });
  for (std::size_t i = 0; i < decoder.blocks.size(); ++i)
    for (std::size_t j = i + 1; j < decoder.blocks.size(); ++j)
      require(gcdz(decoder.blocks[i].value, decoder.blocks[j].value) == 1,
              "opaque blocks not pairwise coprime");
  for (int column = 0; column < count; ++column) {
    cpp_int rebuilt = 1;
    for (const Block& block : decoder.blocks)
      if (block.exponents[column])
        rebuilt *= pow_small(block.value, block.exponents[column]);
    require(rebuilt == rows[column].value, "opaque row reconstruction");
  }
  int words = (count + 63) / 64;
  for (const Block& block : decoder.blocks) {
    if (squarez(block.value)) continue;
    Bits equation(words, 0);
    for (int column = 0; column < count; ++column)
      if (block.exponents[column] & 1U) bit_flip(equation, column);
    if (!bit_zero(equation)) decoder.equations.push_back(std::move(equation));
  }
  std::vector<int> pivots;
  int rank = 0;
  for (int column = 0; column < count; ++column) {
    int selected = -1;
    for (int row = rank; row < static_cast<int>(decoder.equations.size()); ++row)
      if (bit_get(decoder.equations[row], column)) { selected = row; break; }
    if (selected < 0) continue;
    std::swap(decoder.equations[rank], decoder.equations[selected]);
    for (int row = 0; row < static_cast<int>(decoder.equations.size()); ++row)
      if (row != rank && bit_get(decoder.equations[row], column))
        bit_xor(decoder.equations[row], decoder.equations[rank]);
    pivots.push_back(column);
    ++rank;
  }
  std::vector<char> is_pivot(count, 0);
  for (int column : pivots) is_pivot[column] = 1;
  for (int free_column = 0; free_column < count; ++free_column) {
    if (is_pivot[free_column]) continue;
    Bits vector(words, 0);
    bit_flip(vector, free_column);
    for (int row = 0; row < rank; ++row)
      if (bit_get(decoder.equations[row], free_column))
        bit_flip(vector, pivots[row]);
    decoder.kernel.push_back(std::move(vector));
  }
  for (const Bits& vector : decoder.kernel)
    for (const Bits& equation : decoder.equations) {
      unsigned parity = 0;
      for (int word = 0; word < words; ++word)
        parity ^= static_cast<unsigned>(__builtin_parityll(vector[word] & equation[word]));
      require(parity == 0, "kernel equation verification");
    }
  decoder.rank = rank;
  decoder.ok = true;
  return decoder;
}

bool is_kernel_vector(const Bits& vector, const Decoder& decoder) {
  for (const Bits& equation : decoder.equations) {
    unsigned parity = 0;
    for (std::size_t word = 0; word < vector.size(); ++word)
      parity ^= static_cast<unsigned>(__builtin_parityll(vector[word] & equation[word]));
    if (parity) return false;
  }
  return true;
}

bool accept_node_value(BankResult& bank, const cpp_int& N, const cpp_int& value,
                       const std::string& label, std::set<std::string>& used) {
  cpp_int candidate = modz(value, N);
  cpp_int gcd = record_gcd(bank, 0, candidate, N, label);
  if (gcd != 1 || candidate == 0) return false;
  return used.insert(candidate.convert_to<std::string>()).second;
}

cpp_int candidate_for(const cpp_int& N, int family, int group, int retry,
                      int role) {
  u64 syntax = mix64(u64(family + 1) << 56) ^ mix64(u64(group + 1) << 32) ^
               mix64(u64(retry + 1) << 8) ^ mix64(u64(role + 1));
  return public_residue(N, syntax);
}

void add_node(std::vector<Node>& nodes, const cpp_int& base,
              const std::string& syntax, int group, int role,
              EdgeType edge = EdgeType::NONE, int parent_a = -1,
              int parent_b = -1, int orbit_i = -1, int orbit_j = -1) {
  nodes.push_back({base, syntax, group, role, orbit_i, orbit_j,
                   edge, parent_a, parent_b});
}

std::vector<Node> make_nodes(const cpp_int& N,int family,int row_target,
                             BankResult& bank) {
  require(row_target==frozen_row_count("discovery",family)||
          row_target==frozen_row_count("heldout",family),"source row target");
  std::vector<Node> nodes;
  std::set<std::string> used;
  int attempts = 0;
  auto independent = [&](int target) {
    for (int slot = 0; slot < target; ++slot) {
      bool accepted = false;
      for (int retry = 0; retry < 256 && !accepted; ++retry) {
        if (++attempts > 8192) reject_resource("FAMILY_CANDIDATE_CAP");
        cpp_int a = candidate_for(N, family, slot, retry, 0);
        if (!accept_node_value(bank, N, a, "SOURCE_HASH_UNIT", used)) continue;
        add_node(nodes, a, "h" + std::to_string(slot), slot, 0);
        accepted = true;
      }
      if (!accepted) reject_resource("INDEPENDENT_SOURCE_EXHAUSTION");
    }
  };

  if (family <= 4) {
    independent(row_target);
  } else if (family == 5) {
    for (int group = 0; group < row_target/2; ++group) {
      bool accepted = false;
      for (int retry = 0; retry < 256 && !accepted; ++retry) {
        if (++attempts > 8192) reject_resource("COMPLEMENT_CANDIDATE_CAP");
        cpp_int a = candidate_for(N, family, group, retry, 0);
        cpp_int b = N - a;
        std::set<std::string> trial = used;
        if (!accept_node_value(bank, N, a, "COMPLEMENT_BASE", trial) ||
            !accept_node_value(bank, N, b, "COMPLEMENT_DERIVED", trial)) continue;
        int parent = static_cast<int>(nodes.size());
        add_node(nodes, a, "c" + std::to_string(group) + ":a", group, 0);
        add_node(nodes, b, "c" + std::to_string(group) + ":N-a", group, 1,
                 EdgeType::COMPLEMENT, parent);
        used = std::move(trial);
        accepted = true;
      }
      if (!accepted) reject_resource("COMPLEMENT_SOURCE_EXHAUSTION");
    }
  } else if (family == 6) {
    for (int group = 0; group < row_target/3; ++group) {
      bool accepted = false;
      for (int retry = 0; retry < 256 && !accepted; ++retry) {
        if (++attempts > 8192) reject_resource("MULTIPLY_CANDIDATE_CAP");
        cpp_int a = candidate_for(N, family, group, retry, 0);
        cpp_int b = candidate_for(N, family, group, retry, 1);
        cpp_int c = modz(a * b, N);
        std::set<std::string> trial = used;
        if (!accept_node_value(bank, N, a, "MULTIPLY_A", trial) ||
            !accept_node_value(bank, N, b, "MULTIPLY_B", trial) ||
            !accept_node_value(bank, N, c, "MULTIPLY_PRODUCT", trial)) continue;
        int pa = static_cast<int>(nodes.size()), pb = pa + 1;
        std::string prefix = "m" + std::to_string(group);
        add_node(nodes, a, prefix + ":a", group, 0);
        add_node(nodes, b, prefix + ":b", group, 1);
        add_node(nodes, c, prefix + ":ab", group, 2,
                 EdgeType::MULTIPLY, pa, pb);
        used = std::move(trial);
        accepted = true;
      }
      if (!accepted) reject_resource("MULTIPLY_SOURCE_EXHAUSTION");
    }
  } else if (family == 7) {
    for (int group = 0; group < row_target/4; ++group) {
      bool accepted = false;
      for (int retry = 0; retry < 256 && !accepted; ++retry) {
        if (++attempts > 8192) reject_resource("POWER_CANDIDATE_CAP");
        cpp_int a = candidate_for(N, family, group, retry, 0);
        cpp_int a2 = modz(a * a, N), a3 = modz(a2 * a, N);
        cpp_int a5 = modz(a2 * a3, N);
        std::array<cpp_int,4> value{a,a2,a3,a5};
        std::set<std::string> trial = used;
        bool clean = true;
        for (int role = 0; role < 4; ++role)
          clean &= accept_node_value(bank, N, value[role],
                                     "POWER_CHAIN_" + std::to_string(role), trial);
        if (!clean) continue;
        int p0 = static_cast<int>(nodes.size());
        std::string prefix = "p" + std::to_string(group);
        add_node(nodes,a,prefix+":a",group,0);
        add_node(nodes,a2,prefix+":a2",group,1,EdgeType::MULTIPLY,p0,p0);
        add_node(nodes,a3,prefix+":a3",group,2,EdgeType::MULTIPLY,p0,p0+1);
        add_node(nodes,a5,prefix+":a5",group,3,EdgeType::MULTIPLY,p0+1,p0+2);
        used = std::move(trial);
        accepted = true;
      }
      if (!accepted) reject_resource("POWER_SOURCE_EXHAUSTION");
    }
  } else if (family == 8) {
    for (int group = 0; group < row_target/2; ++group) {
      bool accepted = false;
      for (int retry = 0; retry < 256 && !accepted; ++retry) {
        if (++attempts > 8192) reject_resource("INVERSE_CANDIDATE_CAP");
        cpp_int a = candidate_for(N, family, group, retry, 0);
        cpp_int gcd = record_gcd(bank, 0, a, N, "INVERSE_BASE");
        if (gcd != 1) continue;
        cpp_int b = invmod(a, N);
        std::set<std::string> trial = used;
        if (!trial.insert(a.convert_to<std::string>()).second ||
            !accept_node_value(bank, N, b, "INVERSE_DERIVED", trial)) continue;
        int parent = static_cast<int>(nodes.size());
        std::string prefix = "i" + std::to_string(group);
        add_node(nodes,a,prefix+":a",group,0);
        add_node(nodes,b,prefix+":inv",group,1,EdgeType::INVERSE,parent);
        used = std::move(trial);
        accepted = true;
      }
      if (!accepted) reject_resource("INVERSE_SOURCE_EXHAUSTION");
    }
  } else if (family == 9) {
    for (int group = 0; group < row_target/4; ++group) {
      bool accepted = false;
      for (int retry = 0; retry < 256 && !accepted; ++retry) {
        if (++attempts > 8192) reject_resource("AFFINE_CANDIDATE_CAP");
        cpp_int a = candidate_for(N, family, group, retry, 0);
        std::array<cpp_int,4> value{a,N-a,modz(a+1,N),modz(2*a+1,N)};
        std::set<std::string> trial=used;
        bool clean=true;
        for (int role=0;role<4;++role)
          clean &= accept_node_value(bank,N,value[role],
                                     "AFFINE_"+std::to_string(role),trial);
        if (!clean) continue;
        int parent=static_cast<int>(nodes.size());
        std::string prefix="a"+std::to_string(group);
        add_node(nodes,value[0],prefix+":x",group,0);
        add_node(nodes,value[1],prefix+":N-x",group,1,
                 EdgeType::COMPLEMENT,parent);
        add_node(nodes,value[2],prefix+":x+1",group,2);
        add_node(nodes,value[3],prefix+":2x+1",group,3);
        used=std::move(trial);accepted=true;
      }
      if (!accepted) reject_resource("AFFINE_SOURCE_EXHAUSTION");
    }
  } else if (family == 10) {
    independent(row_target/5);
  } else {
    require(family == 11, "unknown family");
    std::vector<Node> seeds;
    std::set<std::string> seed_used;
    for (int slot=0;slot<2;++slot) {
      bool accepted=false;
      for (int retry=0;retry<256&&!accepted;++retry) {
        if (++attempts>8192) reject_resource("ORBIT_SEED_CAP");
        cpp_int a=candidate_for(N,family,slot,retry,0);
        if (!accept_node_value(bank,N,a,"ORBIT_SEED",seed_used)) continue;
        add_node(seeds,a,slot==0?"o:a":"o:b",0,slot,EdgeType::NONE,-1,-1,
                 slot==0?1:0,slot==0?0:1);
        accepted=true;
      }
      if (!accepted) reject_resource("ORBIT_SEED_EXHAUSTION");
    }
    cpp_int a=seeds[0].base,b=seeds[1].base;
    for (int degree=1;degree<64&&static_cast<int>(nodes.size())<row_target;++degree) {
      for (int i=degree;i>=0&&static_cast<int>(nodes.size())<row_target;--i) {
        if (++attempts>8192) reject_resource("ORBIT_CANDIDATE_CAP");
        int j=degree-i;
        cpp_int value=modz(powmod(a,cpp_int(i),N)*powmod(b,cpp_int(j),N),N);
        if (!accept_node_value(bank,N,value,"ORBIT_DERIVED",used)) continue;
        add_node(nodes,value,"o:"+std::to_string(i)+","+std::to_string(j),
                 degree,i,EdgeType::NONE,-1,-1,i,j);
      }
    }
    if (static_cast<int>(nodes.size())!=row_target)
      reject_resource("ORBIT_ROW_SOURCE_EXHAUSTION");
  }
  require(!nodes.empty()&&static_cast<int>(nodes.size())<=row_target,"node count");
  return nodes;
}

std::vector<Row> make_rows(const cpp_int& N, int family,
                           std::vector<Node>& nodes) {
  std::vector<Row> rows;
  cpp_int modulus=N*N;
  auto emit=[&](int node,int tag) {
    cpp_int exponent=exponent_for_tag(tag,N);
    require((exponent&1)==0&&gcdz(exponent,N)==1,"exponent invariant");
    cpp_int value=powmod(nodes[node].base,exponent,modulus);
    cpp_int root=powmod(nodes[node].base,exponent/2,N);
    cpp_int low=modz(value,N),high=(value-low)/N;
    require(root*root%N==low,"supplied row root");
    require(value>0&&value<modulus,"canonical row range");
    int id=static_cast<int>(rows.size());
    rows.push_back({id,node,family,tag,nodes[node].base,exponent,value,root,
                    low,high,nodes[node].syntax+":e"+std::to_string(tag)});
  };
  if (family<=4) {
    for (int node=0;node<static_cast<int>(nodes.size());++node) emit(node,family);
  } else if (family==5) {
    for (int node=0;node<static_cast<int>(nodes.size());++node) emit(node,0);
  } else if (family==6) {
    for (int node=0;node<static_cast<int>(nodes.size());++node) emit(node,1);
  } else if (family==7) {
    for (int node=0;node<static_cast<int>(nodes.size());++node) emit(node,2);
  } else if (family==8) {
    for (int node=0;node<static_cast<int>(nodes.size());++node) emit(node,3);
  } else if (family==9) {
    for (int node=0;node<static_cast<int>(nodes.size());++node) emit(node,4);
  } else if (family==10) {
    for (int node=0;node<static_cast<int>(nodes.size());++node)
      for (int tag=0;tag<5;++tag) emit(node,tag);
  } else {
    for (int node=0;node<static_cast<int>(nodes.size());++node) emit(node,node%5);
  }
  require(rows.size()<=MAX_ROWS,"row cap");
  return rows;
}

std::string classify_relation(BankResult& bank, int stage, const cpp_int& N,
                              const cpp_int& exact_root,
                              const cpp_int& supplied_root,
                              cpp_int& normalized, cpp_int& gcd_minus,
                              cpp_int& gcd_plus, const std::string& label) {
  cpp_int r=modz(exact_root,N),x=modz(supplied_root,N);
  require(gcdz(x,N)==1,"relation supplied root nonunit");
  gcd_minus=record_gcd(bank,stage,r-x,N,label+"_MINUS");
  gcd_plus=record_gcd(bank,stage,r+x,N,label+"_PLUS");
  normalized=modz(r*invmod(x,N),N);
  if (r==x) return "GLOBAL_PLUS";
  if (r==modz(-x,N)) return "GLOBAL_MINUS";
  require((gcd_minus>1&&gcd_minus<N)||(gcd_plus>1&&gcd_plus<N),
          "invalid normalized root class");
  return "USEFUL";
}

Relation verify_relation(BankResult& bank, int stage, const cpp_int& N,
                         const std::vector<Row>& rows, const Bits& bits,
                         const std::string& kind) {
  cpp_int product=1,supplied=1;
  for (int i=0;i<static_cast<int>(rows.size());++i) if (bit_get(bits,i)) {
    product*=rows[i].value;
    supplied=modz(supplied*rows[i].root,N);
  }
  cpp_int exact;
  require(squarez(product,&exact),"relation product not square");
  Relation relation;
  relation.kind=kind;relation.bits=bits;relation.exact_root=exact;
  relation.supplied_root=supplied;
  relation.root_class=classify_relation(bank,stage,N,exact,supplied,
      relation.normalized,relation.gcd_minus,relation.gcd_plus,kind);
  bank.relation_bits+=bitlen(exact)+bitlen(supplied)+bitlen(relation.normalized);
  if (bank.relation_bits>MAX_RELATION_BITS)
    reject_resource("RELATION_BITS_CAP");
  return relation;
}

std::vector<int> pattern_templates(const Relation& relation,
                                   const std::vector<Row>& rows,
                                   const std::vector<Node>& nodes,
                                   const cpp_int& N) {
  std::vector<int> selected;
  for (int i=0;i<static_cast<int>(rows.size());++i)
    if (bit_get(relation.bits,i)) selected.push_back(i);
  std::set<int> tags;
  std::map<std::pair<int,int>,std::set<int>> roles;
  std::set<std::pair<int,int>> orbit;
  for (int i:selected) {
    tags.insert(rows[i].exponent_tag);
    const Node& node=nodes[rows[i].node];
    roles[{rows[i].family,node.group}].insert(node.role);
    if (node.orbit_i>=0) orbit.insert({node.orbit_i,node.orbit_j});
  }
  std::vector<int> out;
  if (selected.size()==3) out.push_back(0);
  if (selected.size()==4) out.push_back(1);
  out.push_back(tags.size()==1?2:3);
  bool multiply=false,power=false,complement=false,inverse=false,affine=false;
  for (const auto& [key,rs]:roles) {
    int family=key.first;
    if (family==6&&rs.count(0)&&rs.count(1)&&rs.count(2)) multiply=true;
    if (family==7&&rs.size()>=3) power=true;
    if ((family==5||family==9)&&rs.count(0)&&rs.count(1)) complement=true;
    if (family==8&&rs.count(0)&&rs.count(1)) inverse=true;
    if (family==9&&rs.size()>=3) affine=true;
  }
  if (multiply) out.push_back(4);
  if (power) out.push_back(5);
  if (complement) out.push_back(6);
  if (inverse) out.push_back(7);
  if (affine) out.push_back(8);
  bool adjacent=false;
  for (const auto& x:orbit)
    for (const auto& y:orbit)
      adjacent|=(std::abs(x.first-y.first)+std::abs(x.second-y.second)==1);
  if (adjacent) out.push_back(9);
  bool same_low=!selected.empty();
  for (std::size_t i=1;i<selected.size();++i)
    same_low&=(rows[selected[i]].low==rows[selected[0]].low);
  if (same_low) out.push_back(10);
  if (!multiply&&!power&&!complement&&!inverse&&!affine&&!adjacent&&!same_low)
    out.push_back(11);
  (void)N;
  return out;
}

void stage_two_individual(BankResult& bank, const cpp_int& N) {
  for (const Row& row:bank.rows) {
    record_gcd(bank,1,row.high,N,"HIGH_DIGIT");
    record_gcd(bank,1,row.value-1,N,"ROW_MINUS_ONE");
    record_gcd(bank,1,row.value+1,N,"ROW_PLUS_ONE");
    record_gcd(bank,1,row.root-1,N,"ROOT_MINUS_ONE");
    record_gcd(bank,1,row.root+1,N,"ROOT_PLUS_ONE");
    cpp_int odd=row.exponent;
    int valuation=0;
    while ((odd&1)==0) {odd>>=1;++valuation;}
    cpp_int state=powmod(row.base,odd,N);
    for (int level=0;level<=valuation;++level) {
      record_gcd(bank,1,state-1,N,"MILLER_MINUS_LEVEL_"+std::to_string(level));
      record_gcd(bank,1,state+1,N,"MILLER_PLUS_LEVEL_"+std::to_string(level));
      if (level<valuation) state=modz(state*state,N);
    }
  }
}

void stage_three_pairs(BankResult& bank, const cpp_int& N) {
  for (std::size_t i=0;i<bank.rows.size();++i)
    for (std::size_t j=i+1;j<bank.rows.size();++j) {
      const Row& a=bank.rows[i];const Row& b=bank.rows[j];
      record_gcd(bank,2,a.base-b.base,N,"PAIR_BASE_MINUS");
      record_gcd(bank,2,a.base+b.base,N,"PAIR_BASE_PLUS");
      record_gcd(bank,2,a.value-b.value,N,"PAIR_ROW_MINUS");
      record_gcd(bank,2,a.value+b.value,N,"PAIR_ROW_PLUS");
      record_gcd(bank,2,a.root-b.root,N,"PAIR_ROOT_MINUS");
      record_gcd(bank,2,a.root+b.root,N,"PAIR_ROOT_PLUS");
      record_gcd(bank,2,a.high-b.high,N,"PAIR_HIGH_MINUS");
      record_gcd(bank,2,a.high+b.high,N,"PAIR_HIGH_PLUS");
    }
}

void verify_carry_identity(BankResult& bank,const cpp_int& N,const Row& child,
                           const Row& left,const Row* right,EdgeType edge) {
  cpp_int quotient,carry,multiplier;
  if (edge==EdgeType::MULTIPLY) {
    require(right,"multiply right parent");
    cpp_int numerator=left.value*right->value-child.value;
    require(numerator%N==0,"multiplication quotient divisibility");
    quotient=numerator/N;
    cpp_int base_numerator=left.base*right->base-child.base;
    require(base_numerator%N==0,"multiplication base carry divisibility");
    carry=base_numerator/N;
    multiplier=modz(child.exponent*carry*
        powmod(child.base,child.exponent-1,N),N);
  } else if (edge==EdgeType::INVERSE) {
    cpp_int numerator=left.value*child.value-1;
    require(numerator%N==0,"inverse quotient divisibility");
    quotient=numerator/N;
    cpp_int base_numerator=left.base*child.base-1;
    require(base_numerator%N==0,"inverse base carry divisibility");
    carry=base_numerator/N;
    multiplier=modz(child.exponent*carry,N);
  } else {
    require(edge==EdgeType::COMPLEMENT,"carry edge type");
    cpp_int numerator=child.value-left.value;
    require(numerator%N==0,"complement quotient divisibility");
    quotient=numerator/N;
    carry=1;
    multiplier=modz(-child.exponent*powmod(left.base,child.exponent-1,N),N);
  }
  require(modz(quotient,N)==multiplier,"carry quotient congruence");
  cpp_int qg=record_gcd(bank,3,quotient,N,"LIFT_CARRY_QUOTIENT");
  if (edge!=EdgeType::COMPLEMENT) {
    cpp_int kg=record_gcd(bank,3,carry,N,"BASE_CARRY");
    require(qg==kg,"lift/base carry gcd equality");
  } else {
    require(qg==1,"complement quotient is not a unit");
  }
}

void stage_four_carries(BankResult& bank,const cpp_int& N) {
  std::map<std::pair<int,int>,int> row_by_node_tag;
  for (const Row& row:bank.rows) row_by_node_tag[{row.node,row.exponent_tag}]=row.id;
  for (const Row& child:bank.rows) {
    const Node& node=bank.nodes[child.node];
    if (node.edge==EdgeType::NONE) continue;
    auto left_it=row_by_node_tag.find({node.parent_a,child.exponent_tag});
    if (left_it==row_by_node_tag.end()) continue;
    const Row& left=bank.rows[left_it->second];
    const Row* right=nullptr;
    if (node.edge==EdgeType::MULTIPLY) {
      auto right_it=row_by_node_tag.find({node.parent_b,child.exponent_tag});
      require(right_it!=row_by_node_tag.end(),"missing multiply parent row");
      right=&bank.rows[right_it->second];
    }
    verify_carry_identity(bank,N,child,left,right,node.edge);
  }
  if (bank.family==10) {
    for (int node=0;node<static_cast<int>(bank.nodes.size());++node) {
      int r0=row_by_node_tag.at({node,0});
      int r3=row_by_node_tag.at({node,3});
      int r1=row_by_node_tag.at({node,1});
      int r4=row_by_node_tag.at({node,4});
      for (const auto& pair:std::array<std::pair<int,int>,2>{{{r0,r3},{r1,r4}}}) {
        const Row& base_row=bank.rows[pair.first];
        const Row& doubled=bank.rows[pair.second];
        cpp_int c=modz(base_row.base*base_row.base,N);
        cpp_int control=powmod(c,base_row.exponent,N*N);
        cpp_int numerator=doubled.value-control;
        require(numerator%N==0,"power quotient divisibility");
        cpp_int carry=(base_row.base*base_row.base-c)/N;
        cpp_int expected=modz(base_row.exponent*carry*
                              powmod(c,base_row.exponent-1,N),N);
        require(modz(numerator/N,N)==expected,"power quotient congruence");
        cpp_int qg=record_gcd(bank,3,numerator/N,N,"POWER_QUOTIENT");
        cpp_int kg=record_gcd(bank,3,carry,N,"POWER_BASE_CARRY");
        require(qg==kg,"power/base carry gcd equality");
      }
    }
  }
}

std::vector<Bits> stage_five_six_low(BankResult& bank,const cpp_int& N) {
  int count=static_cast<int>(bank.rows.size()),words=(count+63)/64;
  std::vector<Bits> global_decoys;
  for (int i=0;i<count;++i) {
    ++bank.singleton_square_tests;
    cpp_int root;
    if (!squarez(bank.rows[i].value,&root)) continue;
    Bits bits(words,0);bit_flip(bits,i);
    Relation relation=verify_relation(bank,4,N,bank.rows,bits,"SINGLETON");
    bool global=relation.root_class!="USEFUL";
    if (!global) ++bank.useful_singletons;
    bank.low_relations.push_back(std::move(relation));
    if (global) global_decoys.push_back(std::move(bits));
  }
  for (int i=0;i<count;++i) for (int j=i+1;j<count;++j) {
    ++bank.support_two_squareclass_tests;
    cpp_int root;
    if (!same_square_class(bank.rows[i].value,bank.rows[j].value,&root)) continue;
    Bits bits(words,0);bit_flip(bits,i);bit_flip(bits,j);
    Relation relation=verify_relation(bank,5,N,bank.rows,bits,"SUPPORT_TWO");
    require(relation.exact_root==root,"support-two root path mismatch");
    bool global=relation.root_class!="USEFUL";
    if (!global) ++bank.useful_support_two;
    bank.low_relations.push_back(std::move(relation));
    if (global) global_decoys.push_back(std::move(bits));
    if (bank.low_relations.size()>MAX_LOW_GENERATORS)
      reject_resource("LOW_RELATION_CAP");
  }
  bank.low_complete=true;
  return global_decoys;
}

void validate_counters(const BankResult& bank) {
  for (const Counter& counter:bank.counters)
    require(counter.tests==counter.unit+counter.full+counter.proper,
            "direct counter partition");
}

bool apply_resource_rejection(BankResult& bank,const std::string& reason) {
  bank.eligible=false;bank.resource_reject=true;bank.reject_reason=reason;
  bank.strict_factor=false;
  bool preserve_terminal_low=bank.low_complete&&
      bank.useful_singletons+bank.useful_support_two>0;
  if (!preserve_terminal_low) {
    bank.low_complete=false;
    bank.nodes.clear();bank.rows.clear();bank.low_relations.clear();
    bank.useful_singletons=bank.useful_support_two=0;
    bank.singleton_square_tests=bank.support_two_squareclass_tests=0;
    bank.relation_bits=0;
  }
  bank.blocks.clear();bank.residual_relations.clear();
  bank.gcd_free_steps=bank.rank=bank.kernel_dim=0;
  bank.low_dim=bank.residual_dim=0;
  validate_counters(bank);
  return preserve_terminal_low;
}

BankResult evaluate_bank(const Case& c,int family) {
  BankResult bank;bank.family=family;
  try {
    bank.nodes=make_nodes(c.N,family,frozen_row_count(c.split,family),bank);
    bank.rows=make_rows(c.N,family,bank.nodes);
    if (bank.rows.empty()||
        static_cast<int>(bank.rows.size())!=frozen_row_count(c.split,family))
      reject_resource("ROW_CAP");
    stage_two_individual(bank,c.N);
    stage_three_pairs(bank,c.N);
    stage_four_carries(bank,c.N);

    // Classify and certify every rational square-class singleton and pair.
    // Only global-sign decoys may enter the quotient basis.
    std::vector<Bits> global_decoys=stage_five_six_low(bank,c.N);
    Decoder decoder=decode_rows(bank.rows);
    if (decoder.resource_reject) reject_resource(decoder.error);
    require(decoder.ok,"decoder failed without resource disposition");
    bank.blocks=decoder.blocks;bank.gcd_free_steps=decoder.steps;
    bank.rank=decoder.rank;bank.kernel_dim=decoder.kernel.size();
    for (const Relation& relation:bank.low_relations)
      require(is_kernel_vector(relation.bits,decoder),
              "low-support relation outside kernel");
    BitBasis low_basis(static_cast<int>(bank.rows.size()));
    for (const Bits& vector:global_decoys) {
      require(is_kernel_vector(vector,decoder),"global decoy outside kernel");
      low_basis.insert(vector);
    }
    bank.low_dim=low_basis.dimension();

    // A useful low-support certificate is already a complete factor
    // disposition. It is retained in evidence and is never quotiented away.
    if (bank.useful_singletons+bank.useful_support_two==0) {
      BitBasis full_basis=low_basis;
      std::vector<Bits> quotient;
      for (const Bits& vector:decoder.kernel) {
        Bits remainder=full_basis.reduce(vector);
        if (bit_zero(remainder)) continue;
        require(is_kernel_vector(remainder,decoder),
                "quotient representative outside kernel");
        require(bit_weight(remainder)>=3,"low-support vector survived quotient");
        require(full_basis.insert(remainder),"quotient insertion failure");
        quotient.push_back(std::move(remainder));
      }
      if (quotient.size()>MAX_RELATIONS)
        reject_resource("QUOTIENT_RELATION_CAP");
      require(bank.low_dim+quotient.size()==decoder.kernel.size(),
              "kernel quotient dimension identity");
      bank.residual_dim=quotient.size();
      for (Bits& vector:quotient) {
        Relation relation=verify_relation(bank,7,c.N,bank.rows,vector,"RESIDUAL");
        relation.templates=pattern_templates(relation,bank.rows,bank.nodes,c.N);
        if (relation.root_class=="USEFUL"&&!bank.earlier_factor)
          bank.strict_factor=true;
        bank.residual_relations.push_back(std::move(relation));
      }
    }
    validate_counters(bank);
    bank.eligible=true;
  } catch (const ResourceReject& rejection) {
    apply_resource_rejection(bank,rejection.what());
  }
  return bank;
}

struct Evaluated {
  int case_index=0;
  int family=0;
  BankResult bank;
};

std::string evidence_for_bank(const Case& c,const BankResult& bank,int case_index);

std::vector<Evaluated> evaluate(const std::vector<Case>& cases,
                                const std::vector<int>& families,int workers) {
  require(workers>=1&&workers<=8,"worker count");
  std::vector<std::pair<int,int>> tasks;
  for (int case_index=0;case_index<static_cast<int>(cases.size());++case_index)
    for (int family:families) tasks.push_back({case_index,family});
  std::vector<Evaluated> output(tasks.size());
  std::atomic<std::size_t> next{0};
  std::mutex error_mutex;
  std::exception_ptr error;
  auto worker=[&] {
    try {
      for (;;) {
        std::size_t task=next.fetch_add(1);
        if (task>=tasks.size()) break;
        auto [case_index,family]=tasks[task];
        BankResult bank=evaluate_bank(cases[case_index],family);
        if (evidence_for_bank(cases[case_index],bank,case_index).size()>
            MAX_BANK_EVIDENCE) {
          bool preserve_terminal_low=apply_resource_rejection(
              bank,"BANK_EVIDENCE_CAP");
          if (preserve_terminal_low)
            require(evidence_for_bank(cases[case_index],bank,case_index).size()<=
                        MAX_BANK_EVIDENCE,
                    "terminal low-support evidence exceeds bank cap");
        }
        output[task]={case_index,family,std::move(bank)};
      }
    } catch (...) {
      std::lock_guard<std::mutex> lock(error_mutex);
      if (!error) error=std::current_exception();
      next.store(tasks.size());
    }
  };
  std::vector<std::thread> pool;
  for (int i=0;i<workers;++i) pool.emplace_back(worker);
  for (auto& thread:pool) thread.join();
  if (error) std::rethrow_exception(error);
  return output;
}

std::string selected_indices(const Bits& bits,int columns) {
  std::ostringstream out;bool first=true;
  for (int i=0;i<columns;++i) if (bit_get(bits,i)) {
    if (!first) out<<',';first=false;out<<i;
  }
  return out.str();
}

std::string integer_vector(const std::vector<std::uint32_t>& values) {
  std::ostringstream out;bool first=true;
  for (int i=0;i<static_cast<int>(values.size());++i) if (values[i]) {
    if (!first) out<<',';first=false;out<<i<<':'<<values[i];
  }
  return out.str();
}

std::string template_vector(const std::vector<int>& values) {
  std::ostringstream out;
  for (std::size_t i=0;i<values.size();++i) {
    if (i) out<<',';out<<values[i];
  }
  return out.str();
}

std::string evidence_for_bank(const Case& c,const BankResult& bank,int case_index) {
  std::ostringstream out;
  auto prefix=[&](const std::string& record,int object) {
    out<<record<<'\t'<<c.split<<'\t'<<c.shape<<'\t'<<c.factor_bits<<'\t'
       <<case_index<<'\t'<<bank.family<<'\t'<<object<<'\t';
  };
  for (const Row& row:bank.rows) {
    const Node& node=bank.nodes[row.node];
    prefix("ROW",row.id);
    out<<row.value<<'\t'<<row.root<<'\t'<<row.base<<'\t'<<row.exponent<<'\t'
       <<row.low<<'\t'<<row.high<<'\t'<<row.exponent_tag<<'\t'<<node.group<<'\t'
       <<node.role<<'\t'<<node.orbit_i<<','<<node.orbit_j<<'\t'<<row.syntax<<"\t-\n";
  }
  for (int i=0;i<static_cast<int>(bank.blocks.size());++i) {
    prefix("BLOCK",i);
    out<<bank.blocks[i].value<<"\t-\t-\t-\t-\t-\t-\t-\t-\t"
       <<integer_vector(bank.blocks[i].exponents)<<"\tUNKNOWN_OPAQUE_NOT_NEEDED\t"
       <<(squarez(bank.blocks[i].value)?"SQUARE":"NONSQUARE")<<'\n';
  }
  auto emit_relation=[&](const Relation& relation,int id) {
    prefix(relation.kind,id);
    out<<relation.exact_root<<'\t'<<relation.supplied_root<<'\t'
       <<relation.normalized<<'\t'<<relation.gcd_minus<<'\t'<<relation.gcd_plus
       <<"\t-\t-\t-\t-\t"<<selected_indices(relation.bits,bank.rows.size())
       <<'\t'<<template_vector(relation.templates)<<'\t'<<relation.root_class<<'\n';
  };
  for (int i=0;i<static_cast<int>(bank.low_relations.size());++i)
    emit_relation(bank.low_relations[i],i);
  for (int i=0;i<static_cast<int>(bank.residual_relations.size());++i)
    emit_relation(bank.residual_relations[i],i);
  if (bank.resource_reject) {
    prefix("REJECT",0);
    out<<"-\t-\t-\t-\t-\t-\t-\t-\t-\t-\t"<<bank.reject_reason
       <<"\tRESOURCE_REJECT\n";
  }
  return out.str();
}

std::string evidence_bytes(const std::vector<Case>& cases,
                           const std::vector<Evaluated>& evaluated) {
  std::ostringstream out;
  out<<"record\tsplit\tshape\tfactor_bits\tcase_index\tfamily\tobject"
       "\tvalue1\tvalue2\tvalue3\tvalue4\tvalue5\tvalue6\tmeta1\tmeta2"
       "\tmeta3\tsparse\tsyntax_or_templates\tclass\n";
  for (const Evaluated& item:evaluated)
    out<<evidence_for_bank(cases[item.case_index],item.bank,item.case_index);
  return out.str();
}

std::string bank_bytes(const std::vector<Case>& cases,
                       const std::vector<Evaluated>& evaluated) {
  std::ostringstream out;
  out<<"version\tsplit\tshape\tfactor_bits\tcase_index\tN\tfamily\teligible"
       "\tresource_reject\treject_reason\tlow_complete\trows\tblocks\tgcd_free_steps\trank"
       "\tkernel_dim\tlow_dim\tresidual_dim\tlow_relations\tresidual_relations"
       "\tuseful_singletons\tuseful_support_two"
       "\tsingleton_square_tests\tsupport_two_squareclass_tests"
       "\tany_factor\tearlier_factor\tstrict_factor\tfirst_factor_label\tfirst_factor";
  for (int stage=1;stage<=8;++stage)
    out<<"\ts"<<stage<<"_tests\ts"<<stage<<"_unit\ts"<<stage
       <<"_full\ts"<<stage<<"_proper";
  out<<'\n';
  for (const Evaluated& item:evaluated) {
    const Case& c=cases[item.case_index];const BankResult& b=item.bank;
    out<<"F268-D03\t"<<c.split<<'\t'<<c.shape<<'\t'<<c.factor_bits<<'\t'
       <<item.case_index<<'\t'<<c.N<<'\t'<<item.family<<'\t'<<b.eligible<<'\t'
       <<b.resource_reject<<'\t'<<(b.reject_reason.empty()?"-":b.reject_reason)
       <<'\t'<<b.low_complete<<'\t'<<b.rows.size()<<'\t'<<b.blocks.size()<<'\t'
       <<b.gcd_free_steps<<'\t'
       <<b.rank<<'\t'<<b.kernel_dim<<'\t'<<b.low_dim<<'\t'<<b.residual_dim<<'\t'
       <<b.low_relations.size()<<'\t'<<b.residual_relations.size()<<'\t'
       <<b.useful_singletons<<'\t'<<b.useful_support_two<<'\t'
       <<b.singleton_square_tests<<'\t'<<b.support_two_squareclass_tests<<'\t'
       <<b.any_factor<<'\t'<<b.earlier_factor<<'\t'<<b.strict_factor<<'\t'
       <<(b.first_factor_label.empty()?"-":b.first_factor_label)<<'\t'
       <<b.first_factor;
    for (const Counter& counter:b.counters)
      out<<'\t'<<counter.tests<<'\t'<<counter.unit<<'\t'<<counter.full<<'\t'
         <<counter.proper;
    out<<'\n';
  }
  return out.str();
}

struct FamilyStats {
  u64 intended=0,eligible=0,strict_banks=0,positive_banks=0;
  u64 residual_dim=0,rows=0;
};

struct TemplateStats {
  u64 strict_bank_incidences=0,relation_incidences=0;
};

void collect_stats(const std::vector<Evaluated>& evaluated,
                   std::array<FamilyStats,FAMILY_COUNT>& families,
                   std::array<TemplateStats,TEMPLATE_COUNT>& templates) {
  for (const Evaluated& item:evaluated) {
    const BankResult& b=item.bank;
    FamilyStats& stats=families[item.family];
    ++stats.intended;
    if (!b.eligible) continue;
    ++stats.eligible;stats.strict_banks+=b.strict_factor;
    stats.positive_banks+=b.residual_dim>0;stats.residual_dim+=b.residual_dim;
    stats.rows+=b.rows.size();
    std::set<int> strict_seen;
    for (const Relation& relation:b.residual_relations) {
      for (int id:relation.templates) {
        require(id>=0&&id<TEMPLATE_COUNT,"template result ID");
        ++templates[id].relation_incidences;
        if (relation.root_class=="USEFUL"&&!b.earlier_factor) strict_seen.insert(id);
      }
    }
    for (int id:strict_seen) ++templates[id].strict_bank_incidences;
  }
}

int compare_rate(u64 a,u64 ad,u64 b,u64 bd) {
  cpp_int left=cpp_int(a)*bd,right=cpp_int(b)*ad;
  return left<right?-1:left>right?1:0;
}

std::vector<int> rank_families(
    const std::array<FamilyStats,FAMILY_COUNT>& stats) {
  std::vector<int> ids(FAMILY_COUNT);
  for (int i=0;i<FAMILY_COUNT;++i) ids[i]=i;
  std::sort(ids.begin(),ids.end(),[&](int a,int b) {
    const FamilyStats& x=stats[a];const FamilyStats& y=stats[b];
    int cmp=compare_rate(x.eligible,std::max<u64>(1,x.intended),
                         y.eligible,std::max<u64>(1,y.intended));
    if (cmp) return cmp>0;
    u64 xd=std::max<u64>(1,x.eligible),yd=std::max<u64>(1,y.eligible);
    cmp=compare_rate(x.strict_banks,xd,y.strict_banks,yd);
    if (cmp) return cmp>0;
    cmp=compare_rate(x.positive_banks,xd,y.positive_banks,yd);
    if (cmp) return cmp>0;
    cmp=compare_rate(x.residual_dim,xd,y.residual_dim,yd);
    if (cmp) return cmp>0;
    if (x.rows!=y.rows) return x.rows<y.rows;
    return a<b;
  });
  return ids;
}

std::vector<int> rank_templates(
    const std::array<TemplateStats,TEMPLATE_COUNT>& stats) {
  std::vector<int> ids(TEMPLATE_COUNT);
  for (int i=0;i<TEMPLATE_COUNT;++i) ids[i]=i;
  std::sort(ids.begin(),ids.end(),[&](int a,int b) {
    if (stats[a].strict_bank_incidences!=stats[b].strict_bank_incidences)
      return stats[a].strict_bank_incidences>stats[b].strict_bank_incidences;
    if (stats[a].relation_incidences!=stats[b].relation_incidences)
      return stats[a].relation_incidences>stats[b].relation_incidences;
    return a<b;
  });
  return ids;
}

std::string family_stats_bytes(
    const std::array<FamilyStats,FAMILY_COUNT>& families,
    const std::array<TemplateStats,TEMPLATE_COUNT>& templates) {
  std::ostringstream out;
  out<<"kind\tid\tintended\teligible\tstrict_banks\tpositive_banks"
       "\tresidual_dim\trows\n";
  for (int id=0;id<FAMILY_COUNT;++id) {
    const FamilyStats& s=families[id];
    out<<"family\t"<<id<<'\t'<<s.intended<<'\t'<<s.eligible<<'\t'
       <<s.strict_banks<<'\t'<<s.positive_banks<<'\t'<<s.residual_dim<<'\t'
       <<s.rows<<'\n';
  }
  for (int id=0;id<TEMPLATE_COUNT;++id)
    out<<"template\t"<<id<<"\t0\t0\t"<<templates[id].strict_bank_incidences
       <<'\t'<<templates[id].relation_incidences<<"\t0\t0\n";
  return out.str();
}

std::string selection_bytes(
    const std::string& corpus_digest,
    const std::array<FamilyStats,FAMILY_COUNT>& families,
    const std::array<TemplateStats,TEMPLATE_COUNT>& templates) {
  std::vector<int> family_rank=rank_families(families);
  std::vector<int> template_rank=rank_templates(templates);
  std::ostringstream out;
  out<<"F268-D03-selection-v1\nfamily_syntax_sha256\t"<<FAMILY_SYNTAX_SHA
     <<"\ndiscovery_corpus_sha256\t"<<corpus_digest<<'\n';
  out<<"family\trank\tid\tintended\teligible\tstrict_banks\tpositive_banks"
       "\tresidual_dim\trows\n";
  for (int rank=0;rank<FAMILY_COUNT;++rank) {
    int id=family_rank[rank];const FamilyStats& s=families[id];
    out<<"family\t"<<rank<<'\t'<<id<<'\t'<<s.intended<<'\t'<<s.eligible<<'\t'
       <<s.strict_banks<<'\t'<<s.positive_banks<<'\t'<<s.residual_dim<<'\t'
       <<s.rows<<'\n';
  }
  out<<"template\trank\tid\tstrict_bank_incidences\trelation_incidences\n";
  for (int rank=0;rank<TEMPLATE_COUNT;++rank) {
    int id=template_rank[rank];
    out<<"template\t"<<rank<<'\t'<<id<<'\t'
       <<templates[id].strict_bank_incidences<<'\t'
       <<templates[id].relation_incidences<<'\n';
  }
  out<<"selected_families";
  for (int i=0;i<4;++i) out<<'\t'<<family_rank[i];
  out<<"\nselected_templates";
  for (int i=0;i<6;++i) out<<'\t'<<template_rank[i];
  out<<'\n';
  return out.str();
}

struct Selection {
  std::string corpus_digest;
  std::vector<int> families;
  std::vector<int> templates;
};

bool decimal_field(const std::string& value) {
  return !value.empty()&&value.find_first_not_of("0123456789")==std::string::npos;
}

Selection parse_selection(const std::string& bytes,const std::string& digest) {
  require(sha256_bytes(bytes)==digest,"selection SHA mismatch");
  std::istringstream input(bytes);std::string line;
  require(bool(std::getline(input,line))&&line=="F268-D03-selection-v1",
          "selection header");
  require(bool(std::getline(input,line)),"selection family digest row");
  auto f=split_tab(line);
  require(f.size()==2&&f[0]=="family_syntax_sha256"&&f[1]==FAMILY_SYNTAX_SHA,
          "selection family syntax digest");
  require(bool(std::getline(input,line)),"selection corpus row");
  f=split_tab(line);
  require(f.size()==2&&f[0]=="discovery_corpus_sha256"&&f[1].size()==64,
          "selection corpus digest");
  Selection selection;selection.corpus_digest=f[1];
  require(bool(std::getline(input,line))&&
          line=="family\trank\tid\tintended\teligible\tstrict_banks\tpositive_banks"
                "\tresidual_dim\trows",
          "selection family header");
  std::array<FamilyStats,FAMILY_COUNT> families{};
  std::vector<int> observed_family_rank;
  std::set<int> unique;
  for (int rank=0;rank<FAMILY_COUNT;++rank) {
    require(bool(std::getline(input,line)),"selection family row absent");
    f=split_tab(line);
    require(f.size()==9&&f[0]=="family"&&std::stoi(f[1])==rank,
            "selection family row");
    int id=std::stoi(f[2]);
    require(id>=0&&id<FAMILY_COUNT&&unique.insert(id).second,
            "selection family ID");
    for (int i=3;i<9;++i) require(decimal_field(f[i]),"selection family metric");
    FamilyStats& s=families[id];
    s.intended=std::stoull(f[3]);s.eligible=std::stoull(f[4]);
    s.strict_banks=std::stoull(f[5]);s.positive_banks=std::stoull(f[6]);
    s.residual_dim=std::stoull(f[7]);s.rows=std::stoull(f[8]);
    observed_family_rank.push_back(id);
  }
  require(rank_families(families)==observed_family_rank,"selection family rerank");
  require(bool(std::getline(input,line))&&
          line=="template\trank\tid\tstrict_bank_incidences\trelation_incidences",
          "selection template header");
  std::array<TemplateStats,TEMPLATE_COUNT> templates{};
  std::vector<int> observed_template_rank;unique.clear();
  for (int rank=0;rank<TEMPLATE_COUNT;++rank) {
    require(bool(std::getline(input,line)),"selection template row absent");
    f=split_tab(line);
    require(f.size()==5&&f[0]=="template"&&std::stoi(f[1])==rank,
            "selection template row");
    int id=std::stoi(f[2]);
    require(id>=0&&id<TEMPLATE_COUNT&&unique.insert(id).second,
            "selection template ID");
    require(decimal_field(f[3])&&decimal_field(f[4]),"selection template metric");
    templates[id].strict_bank_incidences=std::stoull(f[3]);
    templates[id].relation_incidences=std::stoull(f[4]);
    observed_template_rank.push_back(id);
  }
  require(rank_templates(templates)==observed_template_rank,"selection template rerank");
  require(bool(std::getline(input,line)),"selected families absent");
  f=split_tab(line);require(f.size()==5&&f[0]=="selected_families",
                           "selected families row");
  for (int i=1;i<5;++i) {
    int id=std::stoi(f[i]);require(id==observed_family_rank[i-1],
                                  "selected family not rank prefix");
    selection.families.push_back(id);
  }
  require(bool(std::getline(input,line)),"selected templates absent");
  f=split_tab(line);require(f.size()==7&&f[0]=="selected_templates",
                           "selected templates row");
  for (int i=1;i<7;++i) {
    int id=std::stoi(f[i]);require(id==observed_template_rank[i-1],
                                  "selected template not rank prefix");
    selection.templates.push_back(id);
  }
  require(!std::getline(input,line),"selection trailing bytes");
  return selection;
}

void make_directory(const std::string& path) {
  if (::mkdir(path.c_str(),0755)==0) return;
  require(errno==EEXIST,"mkdir: "+path);
  struct stat info{};
  require(::stat(path.c_str(),&info)==0&&S_ISDIR(info.st_mode),"not directory");
}

std::string join_path(const std::string& directory,const std::string& name) {
  return directory+"/"+name;
}

void write_new(const std::string& path,const std::string& bytes) {
  struct stat info{};
  require(::stat(path.c_str(),&info)!=0&&errno==ENOENT,"refuse overwrite: "+path);
  std::ofstream output(path,std::ios::binary);
  require(bool(output),"open output: "+path);
  output.write(bytes.data(),static_cast<std::streamsize>(bytes.size()));
  require(bool(output),"write output: "+path);
  output.close();require(bool(output),"close output: "+path);
}

double timeval_seconds(const timeval& value) {
  return double(value.tv_sec)+double(value.tv_usec)/1e6;
}

struct ResourceSnapshot {
  double wall=0,user=0,system=0;
  u64 rss=0;
};

ResourceSnapshot resources(std::chrono::steady_clock::time_point start) {
  rusage usage{};require(getrusage(RUSAGE_SELF,&usage)==0,"getrusage");
  return {std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count(),
          timeval_seconds(usage.ru_utime),timeval_seconds(usage.ru_stime),
          static_cast<u64>(usage.ru_maxrss)};
}

std::string lead_bytes(const std::vector<Case>& cases,
                       const std::vector<Evaluated>& evaluated,
                       const Selection& selection) {
  u64 intended=evaluated.size(),eligible=0,strict=0,any=0;
  std::set<int> strict_sizes,strict_templates;
  std::set<std::string> strict_shapes;
  std::map<std::tuple<int,int,std::string>,u64> eligible_cell,intended_cell;
  std::set<int> selected_template_set(selection.templates.begin(),selection.templates.end());
  for (const Evaluated& item:evaluated) {
    const Case& c=cases[item.case_index];const BankResult& b=item.bank;
    eligible+=b.eligible;any+=b.any_factor;
    ++intended_cell[{item.family,c.factor_bits,c.shape}];
    if (b.eligible) ++eligible_cell[{item.family,c.factor_bits,c.shape}];
    bool counted=false;
    for (const Relation& relation:b.residual_relations) {
      if (relation.root_class!="USEFUL"||b.earlier_factor) continue;
      bool authenticated=false;
      for (int id:relation.templates) if (selected_template_set.count(id)) {
        authenticated=true;strict_templates.insert(id);
      }
      counted|=authenticated;
    }
    if (counted) {
      ++strict;strict_sizes.insert(c.factor_bits);strict_shapes.insert(c.shape);
    }
  }
  bool hostile=strict_shapes.count("safe-safe")||strict_shapes.count("neighbor")||
               strict_shapes.count("marker-control");
  bool finite_lead=strict>=2&&strict_sizes.size()>=2&&hostile&&strict_templates.size()>=2;
  bool coverage=false;
  for (int family:selection.families) {
    bool family_coverage=true;
    for (int bits:{40,48,56,60}) for (const char* shape:{"random","neighbor","safe-safe"})
      family_coverage&=eligible_cell[{family,bits,shape}]>=20;
    coverage|=family_coverage;
  }
  bool finite_null=any==0&&10*eligible>=9*intended&&coverage;
  std::ostringstream out;
  out<<"metric\tvalue\nstrict_finite_lead\t"<<finite_lead
     <<"\nfinite_null_signal\t"<<finite_null<<"\nstrict_authenticated_banks\t"<<strict
     <<"\nstrict_factor_sizes\t"<<strict_sizes.size()
     <<"\nstrict_templates\t"<<strict_templates.size()<<"\nhostile_shape\t"<<hostile
     <<"\nany_factor_banks\t"<<any<<"\neligible\t"<<eligible
     <<"\nintended\t"<<intended<<"\nordinary_cell_coverage\t"<<coverage<<'\n';
  out<<"coverage\tfamily\tfactor_bits\tshape\tintended\teligible\tpasses20\n";
  for (int family:selection.families)
    for (int bits:{40,48,56,60}) for (const char* shape:{"random","neighbor","safe-safe"}) {
      u64 i=intended_cell[{family,bits,shape}],e=eligible_cell[{family,bits,shape}];
      out<<"coverage\t"<<family<<'\t'<<bits<<'\t'<<shape<<'\t'<<i<<'\t'<<e
         <<'\t'<<(e>=20)<<'\n';
    }
  return out.str();
}

std::vector<std::uint32_t> parse_exponents(const std::string& text,int count) {
  std::vector<std::uint32_t> output(count,0);
  if (text.empty()||text=="-") return output;
  std::istringstream input(text);std::string token;
  while (std::getline(input,token,',')) {
    std::size_t colon=token.find(':');require(colon!=std::string::npos,"exponent token");
    int index=std::stoi(token.substr(0,colon));
    u64 exponent=std::stoull(token.substr(colon+1));
    require(index>=0&&index<count&&exponent<=std::numeric_limits<std::uint32_t>::max(),
            "exponent token range");
    require(output[index]==0,"duplicate exponent token");
    output[index]=static_cast<std::uint32_t>(exponent);
  }
  return output;
}

Bits parse_indices(const std::string& text,int count) {
  Bits bits((count+63)/64,0);
  if (text.empty()||text=="-") return bits;
  std::istringstream input(text);std::string token;
  while (std::getline(input,token,',')) {
    int index=std::stoi(token);require(index>=0&&index<count,"relation index");
    require(!bit_get(bits,index),"duplicate relation index");bit_flip(bits,index);
  }
  return bits;
}

std::vector<int> parse_template_ids(const std::string& text) {
  std::vector<int> output;
  std::set<int> seen;
  if (text.empty()||text=="-") return output;
  std::istringstream input(text);std::string token;
  while (std::getline(input,token,',')) {
    int id=std::stoi(token);require(id>=0&&id<TEMPLATE_COUNT,"template evidence ID");
    require(seen.insert(id).second,"duplicate template evidence ID");
    output.push_back(id);
  }
  return output;
}

struct ReplayBank {
  cpp_int N;
  int family=-1;
  bool rejected=false;
  std::string reject_reason;
  std::vector<Row> rows;
  std::vector<std::tuple<int,int,std::string>> row_metadata;
  std::vector<Block> blocks;
  std::vector<std::pair<std::string,Relation>> relations;
};

void validate_evidence_bytes(const std::vector<Case>& cases,
                             const std::string& bytes,
                             int expected_family_count) {
  require(expected_family_count==4||expected_family_count==FAMILY_COUNT,
          "expected evidence family count");
  std::istringstream input(bytes);std::string line;
  require(bool(std::getline(input,line))&&
          line=="record\tsplit\tshape\tfactor_bits\tcase_index\tfamily\tobject"
                "\tvalue1\tvalue2\tvalue3\tvalue4\tvalue5\tvalue6\tmeta1\tmeta2"
                "\tmeta3\tsparse\tsyntax_or_templates\tclass",
          "evidence header");
  std::map<std::pair<int,int>,ReplayBank> banks;
  while (std::getline(input,line)) {
    if (line.empty()) continue;
    auto f=split_tab(line);require(f.size()==19,"evidence row width");
    int case_index=std::stoi(f[4]),family=std::stoi(f[5]),object=std::stoi(f[6]);
    require(case_index>=0&&case_index<static_cast<int>(cases.size()),"evidence case");
    require(family>=0&&family<FAMILY_COUNT,"evidence family");
    const Case& c=cases[case_index];
    require(f[1]==c.split&&f[2]==c.shape&&std::stoi(f[3])==c.factor_bits,
            "evidence case metadata");
    ReplayBank& bank=banks[{case_index,family}];bank.N=c.N;bank.family=family;
    require(!bank.rejected,"evidence record after resource rejection");
    if (f[0]=="ROW") {
      require(object==static_cast<int>(bank.rows.size()),"evidence row order");
      Row row;row.id=object;row.family=family;
      row.value=parse_positive(f[7]);row.root=parse_positive(f[8]);
      row.base=parse_positive(f[9]);row.exponent=parse_positive(f[10]);
      row.low=parse_positive(f[11]);
      row.high=cpp_int(f[12]);require(row.high>=0,"negative high digit");
      row.exponent_tag=std::stoi(f[13]);row.syntax=f[17];
      require(powmod(row.base,row.exponent,c.N*c.N)==row.value,"replay row power");
      require(modz(row.value,c.N)==row.low&&
              (row.value-row.low)/c.N==row.high,"replay row digits");
      require(modz(row.root*row.root,c.N)==row.low,"replay row root");
      bank.rows.push_back(std::move(row));
      bank.row_metadata.push_back({std::stoi(f[14]),std::stoi(f[15]),f[16]});
    } else if (f[0]=="BLOCK") {
      require(!bank.rows.empty(),"block before rows");
      Block block;block.value=parse_positive(f[7]);
      block.exponents=parse_exponents(f[16],bank.rows.size());
      require(f[17]=="UNKNOWN_OPAQUE_NOT_NEEDED","opaque status");
      require((f[18]=="SQUARE")==squarez(block.value),"opaque square label");
      bank.blocks.push_back(std::move(block));
    } else if (f[0]=="REJECT") {
      require(object==0&&f[18]=="RESOURCE_REJECT"&&f[17]!="-",
              "resource rejection evidence");
      for (int i=7;i<=16;++i) require(f[i]=="-","resource rejection payload");
      bank.rejected=true;bank.reject_reason=f[17];
    } else {
      require(f[0]=="SINGLETON"||f[0]=="SUPPORT_TWO"||f[0]=="RESIDUAL",
              "evidence relation kind");
      Relation relation;relation.kind=f[0];
      relation.exact_root=parse_positive(f[7]);
      relation.supplied_root=parse_positive(f[8]);
      relation.normalized=parse_positive(f[9]);
      relation.gcd_minus=parse_positive(f[10]);relation.gcd_plus=parse_positive(f[11]);
      relation.bits=parse_indices(f[16],bank.rows.size());
      relation.templates=parse_template_ids(f[17]);relation.root_class=f[18];
      cpp_int product=1,supplied=1;
      for (int i=0;i<static_cast<int>(bank.rows.size());++i) if (bit_get(relation.bits,i)) {
        product*=bank.rows[i].value;supplied=modz(supplied*bank.rows[i].root,c.N);
      }
      require(relation.exact_root*relation.exact_root==product,"replay relation square");
      require(relation.supplied_root==supplied,"replay supplied root");
      require(relation.normalized==modz(relation.exact_root*invmod(supplied,c.N),c.N),
              "replay normalized root");
      require(relation.gcd_minus==gcdz(relation.exact_root-supplied,c.N)&&
              relation.gcd_plus==gcdz(relation.exact_root+supplied,c.N),
              "replay signed gcd");
      std::string expected=(modz(relation.exact_root,c.N)==supplied)?"GLOBAL_PLUS":
          (modz(relation.exact_root,c.N)==modz(-supplied,c.N))?"GLOBAL_MINUS":"USEFUL";
      require(relation.root_class==expected,"replay root class");
      if (f[0]=="SINGLETON") require(bit_weight(relation.bits)==1,"singleton weight");
      if (f[0]=="SUPPORT_TWO") require(bit_weight(relation.bits)==2,"pair weight");
      if (f[0]=="RESIDUAL") require(bit_weight(relation.bits)>=3,"residual weight");
      bank.relations.push_back({f[0],std::move(relation)});
    }
  }
  require(!banks.empty(),"no evidence banks");
  require(banks.size()==cases.size()*static_cast<std::size_t>(expected_family_count),
          "evidence bank matrix size");
  std::set<int> common_families;
  for (int family=0;family<FAMILY_COUNT;++family)
    if (banks.count({0,family})) common_families.insert(family);
  require(common_families.size()==static_cast<std::size_t>(expected_family_count),
          "evidence first-case family count");
  for (int case_index=0;case_index<static_cast<int>(cases.size());++case_index)
    for (int family=0;family<FAMILY_COUNT;++family)
      require(bool(banks.count({case_index,family}))==bool(common_families.count(family)),
              "evidence family matrix mismatch");
  for (auto& [key,bank]:banks) {
    if (bank.rejected&&bank.rows.empty()) {
      require(bank.blocks.empty()&&bank.relations.empty(),
              "empty rejected bank has arithmetic evidence");
      continue;
    }
    require(!bank.rows.empty(),"replay empty bank");
    BankResult source_bank;source_bank.family=bank.family;
    std::vector<Node> expected_nodes=make_nodes(
        bank.N,bank.family,frozen_row_count(cases[key.first].split,bank.family),
        source_bank);
    std::vector<Row> expected_rows=make_rows(bank.N,bank.family,expected_nodes);
    require(expected_rows.size()==bank.rows.size()&&
            bank.row_metadata.size()==bank.rows.size(),"replay source row count");
    for (int i=0;i<static_cast<int>(bank.rows.size());++i) {
      const Row& observed=bank.rows[i];const Row& expected=expected_rows[i];
      const Node& node=expected_nodes[expected.node];
      require(observed.base==expected.base&&observed.exponent==expected.exponent&&
              observed.value==expected.value&&observed.root==expected.root&&
              observed.low==expected.low&&observed.high==expected.high&&
              observed.exponent_tag==expected.exponent_tag&&
              observed.syntax==expected.syntax,"replay frozen source row");
      require(bank.row_metadata[i]==
                  std::make_tuple(node.group,node.role,
                                  std::to_string(node.orbit_i)+","+
                                  std::to_string(node.orbit_j)),
              "replay frozen source metadata");
    }
    for (const auto& [kind,relation]:bank.relations) {
      if (kind=="RESIDUAL")
        require(relation.templates==pattern_templates(
                    relation,expected_rows,expected_nodes,bank.N),
                "replay template classification");
      else
        require(relation.templates.empty(),"low-support template payload");
    }
    if (bank.rejected) {
      require(bank.blocks.empty(),"resource-rejected terminal low bank has blocks");
      std::set<std::string> observed_low;
      bool useful_low=false;
      for (const auto& [kind,relation]:bank.relations) {
        require(kind!="RESIDUAL","resource-rejected terminal bank has residual");
        observed_low.insert(selected_indices(relation.bits,bank.rows.size()));
        useful_low|=relation.root_class=="USEFUL";
      }
      int count=bank.rows.size(),words=(count+63)/64;
      std::set<std::string> expected_low;
      for (int i=0;i<count;++i) if (squarez(bank.rows[i].value)) {
        Bits bits(words,0);bit_flip(bits,i);
        expected_low.insert(selected_indices(bits,count));
      }
      for (int i=0;i<count;++i) for (int j=i+1;j<count;++j)
        if (same_square_class(bank.rows[i].value,bank.rows[j].value)) {
          Bits bits(words,0);bit_flip(bits,i);bit_flip(bits,j);
          expected_low.insert(selected_indices(bits,count));
        }
      require(useful_low&&observed_low==expected_low,
              "incomplete preserved terminal low-support evidence");
      continue;
    }
    Decoder decoder=decode_rows(bank.rows);
    require(decoder.ok&&!decoder.resource_reject,"replay decoder");
    require(decoder.blocks.size()==bank.blocks.size(),"replay block count");
    for (std::size_t i=0;i<bank.blocks.size();++i)
      require(decoder.blocks[i].value==bank.blocks[i].value&&
              decoder.blocks[i].exponents==bank.blocks[i].exponents,
              "replay block mismatch");
    std::set<std::string> observed_low,observed_residual;
    bool useful_low=false;
    for (const auto& [kind,relation]:bank.relations) {
      std::string key_text=selected_indices(relation.bits,bank.rows.size());
      if (kind=="RESIDUAL")
        require(observed_residual.insert(key_text).second,
                "duplicate residual evidence");
      else {
        require(is_kernel_vector(relation.bits,decoder),
                "replay low-support relation outside kernel");
        require(observed_low.insert(key_text).second,"duplicate low evidence");
        useful_low|=relation.root_class=="USEFUL";
      }
    }
    int count=bank.rows.size(),words=(count+63)/64;
    std::vector<Bits> low;
    for (int i=0;i<count;++i) if (squarez(bank.rows[i].value)) {
      Bits bits(words,0);bit_flip(bits,i);low.push_back(bits);
    }
    for (int i=0;i<count;++i) for (int j=i+1;j<count;++j)
      if (same_square_class(bank.rows[i].value,bank.rows[j].value)) {
        Bits bits(words,0);bit_flip(bits,i);bit_flip(bits,j);low.push_back(bits);
      }
    std::set<std::string> expected_low;
    for (const Bits& bits:low) {
      require(is_kernel_vector(bits,decoder),"replay low outside kernel");
      expected_low.insert(selected_indices(bits,count));
    }
    require(expected_low==observed_low,"complete low-support evidence mismatch");
    if (useful_low) {
      require(observed_residual.empty(),
              "residual evidence after useful low-support disposition");
      continue;
    }
    BitBasis basis(count);
    for (const Bits& bits:low) {
      cpp_int product=1,supplied=1,exact;
      for (int i=0;i<count;++i) if (bit_get(bits,i)) {
        product*=bank.rows[i].value;
        supplied=modz(supplied*bank.rows[i].root,bank.N);
      }
      require(squarez(product,&exact),"replay canonical low root");
      cpp_int reduced=modz(exact,bank.N);
      require(reduced==supplied||reduced==modz(-supplied,bank.N),
              "useful low relation escaped terminal disposition");
      require(basis.insert(bits)||bit_zero(basis.reduce(bits)),
              "replay canonical low-basis insertion");
    }
    std::set<std::string> expected_residual;
    for (const Bits& kernel:decoder.kernel) {
      Bits remainder=basis.reduce(kernel);
      if (bit_zero(remainder)) continue;
      require(bit_weight(remainder)>=3&&basis.insert(remainder),"replay quotient basis");
      expected_residual.insert(selected_indices(remainder,count));
    }
    require(expected_residual==observed_residual,"quotient evidence mismatch");
  }
}

std::string metric_bytes(const ResourceSnapshot& resource,u64 sample_cases,
                         u64 sample_tasks,u64 full_tasks,u64 sample_pair_bundles,
                         u64 full_pair_bundles,u64 sample_rows,u64 full_rows,
                         u64 sample_singleton_tests,u64 full_singleton_tests,
                         u64 sample_stage3_gcds,u64 full_stage3_gcds,
                         u64 sample_support_two_tests,u64 full_support_two_tests,
                         u64 resource_rejects,
                         u64 completed_large,u64 serialized_bytes,
                         u64 projected_bytes) {
  std::ostringstream out;
  out<<std::fixed<<std::setprecision(6)
     <<"bank_wall_seconds\t"<<resource.wall<<"\nbank_user_seconds\t"<<resource.user
     <<"\nbank_system_seconds\t"<<resource.system<<"\nbank_maxrss_kib\t"<<resource.rss
     <<"\nsample_cases\t"<<sample_cases<<"\nsample_tasks\t"<<sample_tasks
     <<"\nfull_tasks\t"<<full_tasks
     <<"\nsample_pair_bundles\t"<<sample_pair_bundles
     <<"\nfull_pair_bundles\t"<<full_pair_bundles
     <<"\nsample_row_power_tests\t"<<sample_rows
     <<"\nfull_row_power_tests\t"<<full_rows
     <<"\nsample_singleton_square_tests\t"<<sample_singleton_tests
     <<"\nfull_singleton_square_tests\t"<<full_singleton_tests
     <<"\nsample_stage3_pair_gcd_tests\t"<<sample_stage3_gcds
     <<"\nfull_stage3_pair_gcd_tests\t"<<full_stage3_gcds
     <<"\nsample_support_two_squareclass_tests\t"<<sample_support_two_tests
     <<"\nfull_support_two_squareclass_tests\t"<<full_support_two_tests
     <<"\nf265_observed_pair_bundles_per_wall_second\t"
     <<F265_OBSERVED_PAIR_BUNDLES_PER_WALL_SECOND
     <<"\nresource_rejects\t"<<resource_rejects
     <<"\ncompleted_large_banks\t"<<completed_large
     <<"\nserialized_sample_bytes\t"<<serialized_bytes
     <<"\nprojected_output_bytes\t"<<projected_bytes<<'\n';
  return out.str();
}

std::map<std::string,std::string> read_metrics(const std::string& path) {
  std::istringstream input(read_file(path));std::string line;
  std::map<std::string,std::string> output;
  while (std::getline(input,line)) {
    if (line.empty()) continue;
    auto f=split_tab(line);require(f.size()==2&&output.emplace(f[0],f[1]).second,
                                   "metric row");
  }
  return output;
}

void run_gate(const std::string& generation_path,const std::string& bank_time_path,
              const std::string& bank_path,const std::string& output_path) {
  auto generation=read_metrics(generation_path);
  auto bank_time=read_metrics(bank_time_path),bank=read_metrics(bank_path);
  double generation_wall=std::stod(generation.at("wall_seconds"));
  u64 generation_rss=std::stoull(generation.at("maxrss_kib"));
  double bank_wall=std::max(std::stod(bank_time.at("wall_seconds")),
                            std::stod(bank.at("bank_wall_seconds")));
  u64 bank_rss=std::max(std::stoull(bank_time.at("maxrss_kib")),
                        std::stoull(bank.at("bank_maxrss_kib")));
  u64 sample_tasks=std::stoull(bank.at("sample_tasks"));
  u64 full_tasks=std::stoull(bank.at("full_tasks"));
  u64 sample_pairs=std::stoull(bank.at("sample_pair_bundles"));
  u64 full_pairs=std::stoull(bank.at("full_pair_bundles"));
  u64 rejects=std::stoull(bank.at("resource_rejects"));
  u64 completed=std::stoull(bank.at("completed_large_banks"));
  u64 output=std::stoull(bank.at("projected_output_bytes"));
  double measured_pair_projection=2.0*bank_wall*full_pairs/
                                  std::max<u64>(1,sample_pairs);
  double measured_task_projection=2.0*bank_wall*full_tasks/
                                  std::max<u64>(1,sample_tasks);
  double measured_projection=std::max(measured_pair_projection,
                                      measured_task_projection);
  double empirical_floor=2.0*full_pairs/
                         F265_OBSERVED_PAIR_BUNDLES_PER_WALL_SECOND;
  double projected_analysis=std::max(measured_projection,empirical_floor);
  double projected_wall=2.0*generation_wall+projected_analysis;
  u64 projected_live_kib=524288ULL+(4*output+1023)/1024;
  u64 peak_rss=std::max({generation_rss,bank_rss,projected_live_kib});
  bool pass=projected_wall<=12600.0&&peak_rss<=3670016ULL&&
            output<=OUTPUT_CAP&&rejects==0&&completed>=1;
  std::ostringstream result;
  result<<std::fixed<<std::setprecision(6)
        <<"pass\t"<<pass<<"\ngeneration_wall_seconds\t"<<generation_wall
        <<"\nmeasured_pair_projection_seconds\t"<<measured_pair_projection
        <<"\nmeasured_task_projection_seconds\t"<<measured_task_projection
        <<"\nmeasured_analysis_projection_seconds\t"<<measured_projection
        <<"\nf265_empirical_analysis_floor_seconds\t"<<empirical_floor
        <<"\nprojected_total_wall_seconds\t"<<projected_wall
        <<"\nmeasured_peak_maxrss_kib\t"<<std::max(generation_rss,bank_rss)
        <<"\nprojected_live_kib\t"<<projected_live_kib
        <<"\npeak_maxrss_kib\t"<<peak_rss<<"\nprojected_output_bytes\t"<<output
        <<"\nresource_rejects\t"<<rejects
        <<"\ncompleted_large_banks\t"<<completed<<'\n';
  write_new(output_path,result.str());
  require(pass,"preflight resource gate failed");
  std::cout<<"RESOURCE_GATE_PASS projected_wall_seconds="<<projected_wall
           <<" peak_rss_kib="<<peak_rss<<" projected_output_bytes="<<output<<'\n';
}

void run_preflight(const std::string& discovery_path,const std::string& discovery_sha,
                   const std::string& heldout_path,const std::string& heldout_sha,
                   const std::string& family_path,const std::string& family_sha,
                   const std::string& directory,int workers) {
  auto start=std::chrono::steady_clock::now();
  authenticate_family_syntax(family_path,family_sha);
  std::vector<Case> discovery=parse_public_corpus(discovery_path,"discovery",discovery_sha);
  std::vector<Case> heldout=parse_public_corpus(heldout_path,"heldout",heldout_sha);
  std::vector<Case> all=discovery;all.insert(all.end(),heldout.begin(),heldout.end());
  std::map<std::string,Case> largest;
  for (const Case& c:all) {
    auto it=largest.find(c.shape);
    if (it==largest.end()||c.N>it->second.N) largest[c.shape]=c;
  }
  std::vector<Case> sample;
  for (const char* shape:{"random","neighbor","safe-safe","marker-control"})
    if (largest.count(shape)) sample.push_back(largest[shape]);
  require(sample.size()>=3,"preflight largest-shape coverage");
  std::vector<int> families(FAMILY_COUNT);for (int i=0;i<FAMILY_COUNT;++i) families[i]=i;
  std::vector<Evaluated> evaluated=evaluate(sample,families,workers);
  std::string banks=bank_bytes(sample,evaluated),evidence=evidence_bytes(sample,evaluated);
  validate_evidence_bytes(sample,evidence,FAMILY_COUNT);
  u64 rejects=0,completed=0,sample_pair_bundles=0,sample_rows=0;
  u64 sample_singleton_tests=0,sample_stage3_gcds=0,sample_support_two_tests=0;
  for (const Evaluated& item:evaluated) {
    rejects+=item.bank.resource_reject;
    completed+=item.bank.eligible&&item.bank.rows.size()==MAX_ROWS;
    u64 rows=item.bank.rows.size();
    sample_rows+=rows;
    sample_pair_bundles+=rows*(rows-1)/2;
    sample_singleton_tests+=item.bank.singleton_square_tests;
    sample_stage3_gcds+=item.bank.counters[2].tests;
    sample_support_two_tests+=item.bank.support_two_squareclass_tests;
  }
  if (rejects==0) {
    require(sample_singleton_tests==sample_rows,
            "preflight complete singleton chronology");
    require(sample_stage3_gcds==8*sample_pair_bundles,
            "preflight complete pair-gcd chronology");
    require(sample_support_two_tests==sample_pair_bundles,
            "preflight complete support-two chronology");
  }
  ResourceSnapshot resource=resources(start);
  u64 full_tasks=discovery.size()*FAMILY_COUNT+heldout.size()*4;
  u64 discovery_pairs_per_case=0,discovery_rows_per_case=0;
  std::vector<std::pair<u64,u64>> heldout_family_work;
  for (int family=0;family<FAMILY_COUNT;++family) {
    u64 d=frozen_row_count("discovery",family);
    u64 h=frozen_row_count("heldout",family);
    discovery_pairs_per_case+=d*(d-1)/2;
    discovery_rows_per_case+=d;
    heldout_family_work.push_back({h*(h-1)/2,h});
  }
  std::sort(heldout_family_work.begin(),heldout_family_work.end(),
            std::greater<std::pair<u64,u64>>());
  u64 heldout_pairs_per_case=0,heldout_rows_per_case=0;
  for (int i=0;i<4;++i) {
    heldout_pairs_per_case+=heldout_family_work[i].first;
    heldout_rows_per_case+=heldout_family_work[i].second;
  }
  u64 full_pair_bundles=discovery.size()*discovery_pairs_per_case+
                        heldout.size()*heldout_pairs_per_case;
  u64 full_rows=discovery.size()*discovery_rows_per_case+
                heldout.size()*heldout_rows_per_case;
  u64 full_stage3_gcds=8*full_pair_bundles;
  u64 full_singleton_tests=full_rows;
  u64 full_support_two_tests=full_pair_bundles;
  u64 sample_bytes=banks.size()+evidence.size();
  u64 projected=static_cast<u64>(2.0*sample_bytes*full_tasks/
                                 std::max<std::size_t>(1,evaluated.size()))+
                64ULL*1024*1024;
  make_directory(directory);
  write_new(join_path(directory,"F268-D03.preflight.banks.tsv"),banks);
  write_new(join_path(directory,"F268-D03.preflight.evidence.tsv"),evidence);
  write_new(join_path(directory,"F268-D03.preflight.metrics.tsv"),
            metric_bytes(resource,sample.size(),evaluated.size(),full_tasks,
                         sample_pair_bundles,full_pair_bundles,sample_rows,full_rows,
                         sample_singleton_tests,full_singleton_tests,
                         sample_stage3_gcds,full_stage3_gcds,
                         sample_support_two_tests,full_support_two_tests,
                         rejects,completed,sample_bytes,projected));
  std::cout<<"PREFLIGHT_BANKS_PASS sample_cases="<<sample.size()
           <<" sample_tasks="<<evaluated.size()
           <<" completed_large="<<completed
           <<" full_pair_bundles="<<full_pair_bundles<<'\n';
}

void run_discovery(const std::string& corpus_path,const std::string& corpus_sha,
                   const std::string& family_path,const std::string& family_sha,
                   const std::string& directory,int workers) {
  auto start=std::chrono::steady_clock::now();
  authenticate_family_syntax(family_path,family_sha);
  std::vector<Case> cases=parse_public_corpus(corpus_path,"discovery",corpus_sha);
  std::vector<int> family_ids(FAMILY_COUNT);
  for (int i=0;i<FAMILY_COUNT;++i) family_ids[i]=i;
  std::vector<Evaluated> evaluated=evaluate(cases,family_ids,workers);
  std::array<FamilyStats,FAMILY_COUNT> families{};
  std::array<TemplateStats,TEMPLATE_COUNT> templates{};
  collect_stats(evaluated,families,templates);
  std::string banks=bank_bytes(cases,evaluated);
  std::string evidence=evidence_bytes(cases,evaluated);
  validate_evidence_bytes(cases,evidence,FAMILY_COUNT);
  std::string stats=family_stats_bytes(families,templates);
  std::string selection=selection_bytes(corpus_sha,families,templates);
  std::string selection_sha=sha256_bytes(selection);
  u64 total=banks.size()+evidence.size()+stats.size()+selection.size();
  require(total<=OUTPUT_CAP,"discovery output cap");
  make_directory(directory);
  write_new(join_path(directory,"F268-D03.discovery.banks.tsv"),banks);
  write_new(join_path(directory,"F268-D03.discovery.evidence.tsv"),evidence);
  write_new(join_path(directory,"F268-D03.discovery.stats.tsv"),stats);
  write_new(join_path(directory,"F268-D03.selection.tsv"),selection);
  write_new(join_path(directory,"F268-D03.selection.sha256"),
            selection_sha+"  F268-D03.selection.tsv\n");
  ResourceSnapshot resource=resources(start);
  std::ostringstream metrics;
  metrics<<std::fixed<<std::setprecision(6)<<"wall_seconds\t"<<resource.wall
         <<"\nuser_seconds\t"<<resource.user<<"\nsystem_seconds\t"<<resource.system
         <<"\nmaxrss_kib\t"<<resource.rss<<"\noutput_bytes\t"<<total<<'\n';
  write_new(join_path(directory,"F268-D03.discovery.metrics.tsv"),metrics.str());
  std::cout<<"DISCOVERY_PASS cases="<<cases.size()<<" banks="<<evaluated.size()
           <<" corpus_sha256="<<corpus_sha<<" selection_sha256="<<selection_sha<<'\n';
}

void run_heldout(const std::string& corpus_path,const std::string& corpus_sha,
                 const std::string& family_path,const std::string& family_sha,
                 const std::string& selection_path,const std::string& selection_sha,
                 const std::string& discovery_corpus_sha,
                 const std::string& directory,int workers) {
  auto start=std::chrono::steady_clock::now();
  authenticate_family_syntax(family_path,family_sha);
  std::string selection_once=read_file(selection_path);
  Selection selection=parse_selection(selection_once,selection_sha);
  require(selection.corpus_digest==discovery_corpus_sha,
          "heldout discovery corpus digest mismatch");
  std::vector<Case> cases=parse_public_corpus(corpus_path,"heldout",corpus_sha);
  std::vector<Evaluated> evaluated=evaluate(cases,selection.families,workers);
  std::array<FamilyStats,FAMILY_COUNT> families{};
  std::array<TemplateStats,TEMPLATE_COUNT> templates{};
  collect_stats(evaluated,families,templates);
  std::string banks=bank_bytes(cases,evaluated);
  std::string evidence=evidence_bytes(cases,evaluated);
  validate_evidence_bytes(cases,evidence,4);
  std::string stats=family_stats_bytes(families,templates);
  std::string lead=lead_bytes(cases,evaluated,selection);
  u64 total=banks.size()+evidence.size()+stats.size()+lead.size();
  require(total<=OUTPUT_CAP,"heldout output cap");
  make_directory(directory);
  write_new(join_path(directory,"F268-D03.heldout.banks.tsv"),banks);
  write_new(join_path(directory,"F268-D03.heldout.evidence.tsv"),evidence);
  write_new(join_path(directory,"F268-D03.heldout.stats.tsv"),stats);
  write_new(join_path(directory,"F268-D03.heldout.lead.tsv"),lead);
  ResourceSnapshot resource=resources(start);
  std::ostringstream metrics;
  metrics<<std::fixed<<std::setprecision(6)<<"wall_seconds\t"<<resource.wall
         <<"\nuser_seconds\t"<<resource.user<<"\nsystem_seconds\t"<<resource.system
         <<"\nmaxrss_kib\t"<<resource.rss<<"\noutput_bytes\t"<<total<<'\n';
  write_new(join_path(directory,"F268-D03.heldout.metrics.tsv"),metrics.str());
  require(sha256_bytes(selection_once)==selection_sha,"selection changed during heldout");
  std::cout<<"HELDOUT_PASS cases="<<cases.size()<<" banks="<<evaluated.size()
           <<" selection_sha256="<<selection_sha<<'\n';
}

void run_validate(const std::string& corpus_path,const std::string& split,
                  const std::string& corpus_sha,const std::string& family_path,
                  const std::string& family_sha,const std::string& evidence_path) {
  authenticate_family_syntax(family_path,family_sha);
  std::vector<Case> cases=parse_public_corpus(corpus_path,split,corpus_sha);
  std::string evidence=read_file(evidence_path);
  validate_evidence_bytes(cases,evidence,split=="discovery"?FAMILY_COUNT:4);
  std::cout<<"EVIDENCE_VALIDATION_PASS split="<<split
           <<" cases="<<cases.size()<<" evidence_sha256="<<sha256_bytes(evidence)<<'\n';
}

void self_test(const std::string& family_path,const std::string& family_sha) {
  authenticate_family_syntax(family_path,family_sha);
  require(sha256_bytes("abc")==
          "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad",
          "SHA-256 self-test");
  for (const std::string& split:{std::string("discovery"),std::string("heldout")}) {
    Case syntax_case;syntax_case.split=split;
    syntax_case.shape="self-test";syntax_case.N=cpp_int(1000003)*1000033;
    for (int family=0;family<FAMILY_COUNT;++family) {
      BankResult syntax_bank;syntax_bank.family=family;
      std::vector<Node> nodes=make_nodes(
          syntax_case.N,family,frozen_row_count(split,family),syntax_bank);
      std::vector<Row> syntax_rows=make_rows(syntax_case.N,family,nodes);
      require(static_cast<int>(syntax_rows.size())==frozen_row_count(split,family),
              "frozen family tier row count");
      std::set<std::string> row_keys;
      for (const Row& row:syntax_rows)
        require(row_keys.insert(row.base.convert_to<std::string>()+":"+
                                row.exponent.convert_to<std::string>()).second,
                "frozen family duplicate row");
    }
  }
  Row first,second;
  first.id=0;first.value=15;first.root=57;first.base=2;first.exponent=2;
  first.low=15;first.high=0;
  second.id=1;second.value=60;second.root=51;second.base=3;second.exponent=2;
  second.low=60;second.high=0;
  std::vector<Row> rows{first,second};
  Decoder decoder=decode_rows(rows);
  require(decoder.ok&&decoder.kernel.size()==1,"decoder self-test");
  BankResult useful_bank;useful_bank.rows=rows;
  std::vector<Bits> useful_decoys=stage_five_six_low(useful_bank,cpp_int(77));
  require(useful_bank.low_relations.size()==1&&useful_decoys.empty()&&
          useful_bank.useful_singletons==0&&useful_bank.useful_support_two==1&&
          useful_bank.low_relations[0].root_class=="USEFUL"&&
          useful_bank.low_relations[0].gcd_minus==7&&
          useful_bank.low_relations[0].gcd_plus==11,
          "useful pair is certified and excluded from decoy quotient");
  useful_bank.blocks.push_back({cpp_int(15),{1,0}});
  useful_bank.residual_relations.push_back(useful_bank.low_relations[0]);
  require(apply_resource_rejection(useful_bank,"SELF_TEST_CAP")&&
          useful_bank.resource_reject&&!useful_bank.eligible&&
          useful_bank.low_complete&&useful_bank.rows.size()==2&&
          useful_bank.low_relations.size()==1&&useful_bank.blocks.empty()&&
          useful_bank.residual_relations.empty()&&
          useful_bank.useful_support_two==1,
          "useful low certificate survives later resource rejection");
  Row square;square.id=0;square.value=9;square.root=3;square.base=3;
  square.exponent=2;square.low=9;square.high=0;
  BankResult global_bank;global_bank.rows={square};
  std::vector<Bits> global_decoys=stage_five_six_low(global_bank,cpp_int(77));
  require(global_bank.low_relations.size()==1&&global_decoys.size()==1&&
          global_bank.useful_singletons==0&&
          global_bank.low_relations[0].root_class=="GLOBAL_PLUS",
          "global singleton enters decoy quotient");
  cpp_int root;
  require(same_square_class(cpp_int(15),cpp_int(60),&root)&&root==30,
          "support-two self-test");
  require(!same_square_class(cpp_int(15),cpp_int(21)),
          "support-two nonsquare self-test");
  cpp_int circuit_N=cpp_int(23)*47;
  std::vector<Row> circuit_rows;
  for (int value:{2,3,6}) {
    cpp_int supplied=0;
    for (cpp_int candidate=1;candidate<circuit_N&&supplied==0;++candidate)
      if (modz(candidate*candidate,circuit_N)==value) supplied=candidate;
    require(supplied!=0,"support-three supplied-root self-test");
    Row row;row.id=circuit_rows.size();row.value=value;row.root=supplied;
    row.base=1;row.exponent=2;row.low=value;row.high=0;
    circuit_rows.push_back(std::move(row));
  }
  BankResult circuit_bank;circuit_bank.rows=circuit_rows;
  require(stage_five_six_low(circuit_bank,circuit_N).empty()&&
          circuit_bank.low_relations.empty(),"support-three low screen self-test");
  Decoder circuit_decoder=decode_rows(circuit_rows);
  require(circuit_decoder.ok&&circuit_decoder.kernel.size()==1&&
          bit_weight(circuit_decoder.kernel[0])==3,
          "support-three quotient self-test");
  Relation circuit_relation=verify_relation(circuit_bank,7,circuit_N,circuit_rows,
                                             circuit_decoder.kernel[0],"RESIDUAL");
  require(circuit_relation.exact_root==6&&
          bit_weight(circuit_relation.bits)==3,
          "support-three exact certificate self-test");
  cpp_int N=77,E=76,a=2,b=3,c=6,modulus=N*N;
  Row left,right,child;
  left.base=a;left.exponent=E;left.value=powmod(a,E,modulus);
  right.base=b;right.exponent=E;right.value=powmod(b,E,modulus);
  child.base=c;child.exponent=E;child.value=powmod(c,E,modulus);
  BankResult carry_bank;
  verify_carry_identity(carry_bank,N,child,left,&right,EdgeType::MULTIPLY);
  validate_counters(carry_bank);
  std::array<FamilyStats,FAMILY_COUNT> family_stats{};
  std::array<TemplateStats,TEMPLATE_COUNT> template_stats{};
  std::string selection=selection_bytes(std::string(64,'a'),family_stats,template_stats);
  Selection parsed=parse_selection(selection,sha256_bytes(selection));
  require(parsed.families==std::vector<int>({0,1,2,3})&&
          parsed.templates==std::vector<int>({0,1,2,3,4,5}),
          "selection self-test");
  std::cout<<"F268_SELF_TEST_PASS\n";
}

}  // namespace

int main(int argc,char** argv) {
  try {
    if (argc==4&&std::string(argv[1])=="--self-test") {
      self_test(argv[2],argv[3]);return 0;
    }
    if (argc==3&&std::string(argv[1])=="--gate") {
      std::cerr<<"gate requires generation time, bank time, bank metrics, and output paths\n";
      return 64;
    }
    if (argc==6&&std::string(argv[1])=="--gate") {
      run_gate(argv[2],argv[3],argv[4],argv[5]);return 0;
    }
    if (argc==10&&std::string(argv[1])=="--preflight") {
      run_preflight(argv[2],argv[3],argv[4],argv[5],argv[6],argv[7],argv[8],
                    std::stoi(argv[9]));return 0;
    }
    if (argc==8&&std::string(argv[1])=="--discovery") {
      run_discovery(argv[2],argv[3],argv[4],argv[5],argv[6],std::stoi(argv[7]));
      return 0;
    }
    if (argc==11&&std::string(argv[1])=="--heldout") {
      run_heldout(argv[2],argv[3],argv[4],argv[5],argv[6],argv[7],argv[8],argv[9],
                  std::stoi(argv[10]));return 0;
    }
    if (argc==8&&std::string(argv[1])=="--validate") {
      run_validate(argv[2],argv[3],argv[4],argv[5],argv[6],argv[7]);return 0;
    }
    std::cerr<<"usage: search --self-test FAMILY FAMILY_SHA | "
               "--gate GENERATION_TIME BANK_TIME BANK_METRICS OUTPUT | "
               "--preflight DISC DISC_SHA HELD HELD_SHA FAMILY FAMILY_SHA OUT WORKERS | "
               "--discovery CORPUS CORPUS_SHA FAMILY FAMILY_SHA OUT WORKERS | "
               "--heldout CORPUS CORPUS_SHA FAMILY FAMILY_SHA SELECTION SELECTION_SHA "
               "DISCOVERY_SHA OUT WORKERS | "
               "--validate CORPUS SPLIT CORPUS_SHA FAMILY FAMILY_SHA EVIDENCE\n";
    return 64;
  } catch (const std::exception& error) {
    std::cerr<<"F268_SEARCH_FATAL "<<error.what()<<'\n';return 70;
  }
}
