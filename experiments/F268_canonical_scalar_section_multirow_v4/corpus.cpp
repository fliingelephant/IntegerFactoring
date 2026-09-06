#include <algorithm>
#include <array>
#include <cerrno>
#include <cstdint>
#include <cstring>
#include <fstream>
#include <iostream>
#include <limits>
#include <set>
#include <sstream>
#include <stdexcept>
#include <string>
#include <tuple>
#include <utility>
#include <vector>

#include <sys/stat.h>

using u64 = std::uint64_t;
using u128 = __uint128_t;

namespace {

constexpr u64 MASTER_SEED = 0xF268CA110A5E5EEDULL;
constexpr int DISCOVERY_BITS[] = {12, 16, 20, 24, 32};
constexpr int HELDOUT_BITS[] = {40, 48, 56, 60};
constexpr int DISCOVERY_MARKER_BITS[] = {12, 16, 20, 24};
constexpr int HELDOUT_MARKER_BITS[] = {20, 24, 28, 32};
constexpr const char* ORDINARY_SHAPES[] = {"random", "neighbor", "safe-safe"};
constexpr int MARKER_ROWS_PER_CELL = 2;
constexpr int MARKER_PAIR_ATTEMPTS_PER_ROW = 4096;
constexpr int MARKER_PRIME_CANDIDATES_PER_REQUEST = 128;

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

u64 gcd64(u64 a, u64 b) {
  while (b) {
    u64 r = a % b;
    a = b;
    b = r;
  }
  return a;
}

u64 mul_mod(u64 a, u64 b, u64 modulus) {
  return static_cast<u64>((static_cast<u128>(a) * b) % modulus);
}

u64 pow_mod(u64 a, u64 exponent, u64 modulus) {
  u64 out = 1 % modulus;
  while (exponent) {
    if (exponent & 1ULL) out = mul_mod(out, a, modulus);
    a = mul_mod(a, a, modulus);
    exponent >>= 1ULL;
  }
  return out;
}

bool is_prime(u64 n) {
  if (n < 2) return false;
  for (u64 p : {2ULL, 3ULL, 5ULL, 7ULL, 11ULL, 13ULL, 17ULL, 19ULL,
                23ULL, 29ULL, 31ULL, 37ULL}) {
    if (n % p == 0) return n == p;
  }
  u64 d = n - 1, s = 0;
  while ((d & 1ULL) == 0) {
    d >>= 1ULL;
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

int bit_length(u64 value) {
  int bits = 0;
  while (value) {
    ++bits;
    value >>= 1ULL;
  }
  return bits;
}

u64 random_exact_bit_prime(Rng& rng, int bits, int cap = 200000) {
  require(bits >= 3 && bits <= 60, "ordinary prime bit range");
  u64 lower = u64(1) << (bits - 1);
  u64 mask = (u64(1) << bits) - 1;
  for (int attempt = 0; attempt < cap; ++attempt) {
    u64 candidate = (rng.next() & mask) | lower | 1ULL;
    if (is_prime(candidate)) return candidate;
  }
  fail("ordinary prime cap");
}

u64 random_prime_class(Rng& rng, int bits, u64 modulus, u64 residue,
                       int cap) {
  require(bits >= 3 && bits <= 32, "class prime bit range");
  u64 lower = u64(1) << (bits - 1);
  u64 upper = u64(1) << bits;
  require(gcd64(modulus, residue) == 1, "nonreduced prime class");
  for (int attempt = 0; attempt < cap; ++attempt) {
    u64 candidate = lower + rng.next() % (upper - lower);
    candidate += (residue + modulus - candidate % modulus) % modulus;
    if (candidate < upper && is_prime(candidate)) return candidate;
  }
  fail("prime class cap");
}

u64 random_safe_prime(Rng& rng, int bits, int cap = 1000000) {
  require(bits >= 4 && bits <= 60, "safe prime bit range");
  u64 lower = u64(1) << (bits - 2);
  u64 mask = (u64(1) << (bits - 1)) - 1;
  for (int attempt = 0; attempt < cap; ++attempt) {
    u64 r = (rng.next() & mask) | lower | 1ULL;
    if (!is_prime(r)) continue;
    u64 p = 2 * r + 1;
    if (bit_length(p) == bits && is_prime(p)) return p;
  }
  fail("safe prime cap");
}

u64 next_prime_bounded(u64 start, int bits, int cap = 200000) {
  u64 lower = u64(1) << (bits - 1);
  u64 upper = u64(1) << bits;
  u64 candidate = std::max(start | 1ULL, lower | 1ULL);
  for (int attempt = 0; attempt < cap && candidate < upper;
       ++attempt, candidate += 2) {
    if (is_prime(candidate)) return candidate;
  }
  fail("neighbor prime cap");
}

std::vector<u64> distinct_prime_factors(u64 value) {
  std::vector<u64> out;
  if ((value & 1ULL) == 0) {
    out.push_back(2);
    do value >>= 1ULL; while ((value & 1ULL) == 0);
  }
  for (u64 p = 3; static_cast<u128>(p) * p <= value; p += 2) {
    if (value % p != 0) continue;
    out.push_back(p);
    do value /= p; while (value % p == 0);
  }
  if (value > 1) out.push_back(value);
  return out;
}

bool primitive_mod_prime(u64 value, u64 prime) {
  if (!is_prime(prime) || value % prime == 0) return false;
  for (u64 divisor : distinct_prime_factors(prime - 1)) {
    if (pow_mod(value % prime, (prime - 1) / divisor, prime) == 1)
      return false;
  }
  return true;
}

struct Markers {
  u64 lambda_plus = 0;
  u64 lambda_minus = 0;
  u64 rho_plus = 0;
  u64 rho_minus = 0;
};

bool find_markers(u64 p, u64 q, Markers& markers) {
  if (gcd64(p - 1, q - 1) != 2 || gcd64(p - 1, q + 1) != 12 ||
      gcd64(p + 1, q - 1) != 2 || gcd64(p + 1, q + 1) != 2)
    return false;
  std::vector<u64> lp, lm, rp, rm;
  for (u64 x : distinct_prime_factors(p - 1))
    if (x > 5 && primitive_mod_prime(q, x)) lp.push_back(x);
  for (u64 x : distinct_prime_factors(p + 1))
    if (x > 5 && primitive_mod_prime(q, x)) lm.push_back(x);
  for (u64 x : distinct_prime_factors(q - 1))
    if (x > 5 && primitive_mod_prime(p, x)) rp.push_back(x);
  for (u64 x : distinct_prime_factors(q + 1))
    if (x > 5 && primitive_mod_prime(p, x)) rm.push_back(x);
  for (u64 a : lp) for (u64 b : lm) for (u64 c : rp) for (u64 d : rm) {
    std::set<u64> distinct{a, b, c, d};
    if (distinct.size() == 4) {
      markers = {a, b, c, d};
      return true;
    }
  }
  return false;
}

struct Case {
  std::string split;
  std::string shape;
  int factor_bits = 0;
  int index = 0;
  u64 p = 0;
  u64 q = 0;
  Markers markers;
};

std::string decimal_u128(u128 value) {
  if (value == 0) return "0";
  std::string out;
  while (value) {
    out.push_back(char('0' + value % 10));
    value /= 10;
  }
  std::reverse(out.begin(), out.end());
  return out;
}

std::string modulus_key(u64 p, u64 q) {
  return decimal_u128(static_cast<u128>(p) * q);
}

Case ordinary_case(const std::string& split, const std::string& shape,
                   int bits, int index, int retry) {
  u64 domain = split == "discovery" ? 0x444953434f564552ULL
                                     : 0x48454c444f555421ULL;
  int shape_id = shape == "random" ? 0 : shape == "neighbor" ? 1 : 2;
  u64 seed = mix64(MASTER_SEED ^ domain ^ mix64(u64(bits) << 32) ^
                   mix64(u64(shape_id) << 48) ^ mix64(u64(index) << 16) ^
                   mix64(u64(retry)));
  Rng rng(seed);
  u64 p = 0, q = 0;
  if (shape == "safe-safe") {
    p = random_safe_prime(rng, bits);
    q = random_safe_prime(rng, bits);
  } else if (shape == "neighbor") {
    p = random_exact_bit_prime(rng, bits);
    u64 immediate = next_prime_bounded(p + 2, bits);
    u64 minimum_skip = u64(1) << std::max(2, bits / 4);
    u64 extra = 2 * (1 + rng.next() % std::max<u64>(2, minimum_skip));
    if (p > std::numeric_limits<u64>::max() - minimum_skip - extra)
      fail("neighbor start overflow");
    q = next_prime_bounded(p + minimum_skip + extra, bits);
    require(q != immediate, "neighbor is consecutive");
  } else {
    p = random_exact_bit_prime(rng, bits);
    q = random_exact_bit_prime(rng, bits);
  }
  if (p > q) std::swap(p, q);
  return {split, shape, bits, index, p, q, {}};
}

bool marker_case(const std::string& split, int bits, int index, int retry,
                 Case& output) {
  u64 domain = split == "discovery" ? 0x4d41524b44495343ULL
                                     : 0x4d41524b48454c44ULL;
  Rng rng(mix64(MASTER_SEED ^ domain ^ mix64(u64(bits) << 32) ^
                mix64(u64(index) << 16) ^ mix64(u64(retry))));
  u64 p = 0, q = 0;
  try {
    p = random_prime_class(rng, bits, 24, 13,
                           MARKER_PRIME_CANDIDATES_PER_REQUEST);
    q = random_prime_class(rng, bits, 72, 11,
                           MARKER_PRIME_CANDIDATES_PER_REQUEST);
  } catch (const std::exception&) {
    return false;
  }
  if (p >= q || static_cast<u128>(q) >= static_cast<u128>(2) * p)
    return false;
  Markers markers;
  if (!find_markers(p, q, markers)) return false;
  output = {split, "marker-control", bits, index, p, q, markers};
  return true;
}

void append_ordinary(const std::string& split, const int* bits, int bit_count,
                     int target, std::set<std::string>& used,
                     std::vector<Case>& cases) {
  for (int bi = 0; bi < bit_count; ++bi) {
    for (const char* shape_text : ORDINARY_SHAPES) {
      std::string shape = shape_text;
      for (int index = 0; index < target; ++index) {
        bool accepted = false;
        for (int retry = 0; retry < 128 && !accepted; ++retry) {
          Case c;
          try {
            c = ordinary_case(split, shape, bits[bi], index, retry);
          } catch (const std::exception&) {
            continue;
          }
          if (c.p == c.q || c.p >= c.q ||
              static_cast<u128>(c.q) >= static_cast<u128>(2) * c.p)
            continue;
          require(bit_length(c.p) == bits[bi] && bit_length(c.q) == bits[bi],
                  "ordinary exact-bit invariant");
          std::string key = modulus_key(c.p, c.q);
          if (!used.insert(key).second) continue;
          cases.push_back(c);
          accepted = true;
        }
        require(accepted, "ordinary corpus pair retry cap");
      }
    }
  }
}

void append_marker(const std::string& split, const int* bits, int bit_count,
                   std::set<std::string>& used, std::vector<Case>& cases,
                   std::vector<std::tuple<std::string, int, int>>& shortfalls) {
  for (int bi = 0; bi < bit_count; ++bi) {
    int found = 0;
    for (int index = 0; index < MARKER_ROWS_PER_CELL; ++index) {
      bool accepted = false;
      for (int retry = 0;
           retry < MARKER_PAIR_ATTEMPTS_PER_ROW && !accepted; ++retry) {
        Case c;
        if (!marker_case(split, bits[bi], index, retry, c)) continue;
        std::string key = modulus_key(c.p, c.q);
        if (!used.insert(key).second) continue;
        cases.push_back(c);
        ++found;
        accepted = true;
      }
    }
    if (found < MARKER_ROWS_PER_CELL)
      shortfalls.emplace_back(split, bits[bi], MARKER_ROWS_PER_CELL - found);
  }
}

std::string public_bytes(const std::vector<Case>& cases,
                         const std::string& split) {
  std::ostringstream out;
  out << "version\tsplit\tshape\tfactor_bits\tindex\tN\n";
  for (const Case& c : cases) if (c.split == split) {
    out << "F268-D04\t" << c.split << '\t' << c.shape << '\t'
        << c.factor_bits << '\t' << c.index << '\t'
        << modulus_key(c.p, c.q) << '\n';
  }
  return out.str();
}

std::string label_bytes(const std::vector<Case>& cases,
                        const std::string& split) {
  std::ostringstream out;
  out << "version\tsplit\tshape\tfactor_bits\tindex\tN\tp\tq"
         "\tlambda_plus\tlambda_minus\trho_plus\trho_minus\n";
  for (const Case& c : cases) if (c.split == split) {
    out << "F268-D04\t" << c.split << '\t' << c.shape << '\t'
        << c.factor_bits << '\t' << c.index << '\t'
        << modulus_key(c.p, c.q) << '\t' << c.p << '\t' << c.q << '\t'
        << c.markers.lambda_plus << '\t' << c.markers.lambda_minus << '\t'
        << c.markers.rho_plus << '\t' << c.markers.rho_minus << '\n';
  }
  return out.str();
}

std::string shortfall_bytes(
    const std::vector<std::tuple<std::string, int, int>>& shortfalls) {
  std::ostringstream out;
  out << "version\tsplit\tshape\tfactor_bits\tmissing\n";
  for (const auto& [split, bits, missing] : shortfalls)
    out << "F268-D04\t" << split << "\tmarker-control\t" << bits << '\t'
        << missing << '\n';
  return out.str();
}

void make_directory(const std::string& path) {
  if (::mkdir(path.c_str(), 0755) == 0) return;
  require(errno == EEXIST, "mkdir " + path + ": " + std::strerror(errno));
  struct stat info {};
  require(::stat(path.c_str(), &info) == 0 && S_ISDIR(info.st_mode),
          "output path is not directory");
}

std::string join_path(const std::string& directory, const std::string& name) {
  return directory + "/" + name;
}

void write_new(const std::string& path, const std::string& bytes, mode_t mode) {
  struct stat info {};
  require(::stat(path.c_str(), &info) != 0 && errno == ENOENT,
          "refuse overwrite: " + path);
  std::ofstream out(path, std::ios::binary);
  require(bool(out), "open output: " + path);
  out.write(bytes.data(), static_cast<std::streamsize>(bytes.size()));
  require(bool(out), "write output: " + path);
  out.close();
  require(bool(out), "close output: " + path);
  require(::chmod(path.c_str(), mode) == 0, "chmod output: " + path);
}

void generate(const std::string& directory) {
  make_directory(directory);
  std::set<std::string> used;
  std::vector<Case> cases;
  std::vector<std::tuple<std::string, int, int>> shortfalls;
  append_ordinary("discovery", DISCOVERY_BITS, 5, 12, used, cases);
  append_marker("discovery", DISCOVERY_MARKER_BITS, 4, used, cases, shortfalls);
  append_ordinary("heldout", HELDOUT_BITS, 4, 24, used, cases);
  append_marker("heldout", HELDOUT_MARKER_BITS, 4, used, cases, shortfalls);

  std::string discovery_public = public_bytes(cases, "discovery");
  std::string heldout_public = public_bytes(cases, "heldout");
  std::string discovery_labels = label_bytes(cases, "discovery");
  std::string heldout_labels = label_bytes(cases, "heldout");
  write_new(join_path(directory, "F268-D04.discovery.public.tsv"),
            discovery_public, 0644);
  write_new(join_path(directory, "F268-D04.heldout.public.tsv"),
            heldout_public, 0644);
  write_new(join_path(directory, "F268-D04.discovery.labels.tsv"),
            discovery_labels, 0600);
  write_new(join_path(directory, "F268-D04.heldout.labels.tsv"),
            heldout_labels, 0600);
  write_new(join_path(directory, "F268-D04.marker_shortfalls.tsv"),
            shortfall_bytes(shortfalls), 0644);
  std::cout << "CORPUS_PASS discovery_bytes=" << discovery_public.size()
            << " heldout_bytes=" << heldout_public.size()
            << " total_cases=" << cases.size()
            << " marker_shortfall_cells=" << shortfalls.size() << '\n';
}

void self_test() {
  require(is_prime(2) && is_prime(1847) && is_prime(2621),
          "primality positive self-test");
  require(!is_prime(1) && !is_prime(4840987), "primality negative self-test");
  require(pow_mod(5, 6, 7) == 1 && primitive_mod_prime(3, 7),
          "order self-test");
  Rng rng(123);
  u64 p = random_exact_bit_prime(rng, 12);
  require(bit_length(p) == 12 && is_prime(p), "prime generator self-test");
  u64 s = random_safe_prime(rng, 12);
  require(is_prime(s) && is_prime((s - 1) / 2), "safe prime self-test");
  std::cout << "CORPUS_SELF_TEST_PASS\n";
}

}  // namespace

int main(int argc, char** argv) {
  try {
    if (argc == 2 && std::string(argv[1]) == "--self-test") {
      self_test();
      return 0;
    }
    if (argc == 3 && std::string(argv[1]) == "--generate") {
      generate(argv[2]);
      return 0;
    }
    std::cerr << "usage: corpus --self-test | --generate DIRECTORY\n";
    return 64;
  } catch (const std::exception& error) {
    std::cerr << "F268_CORPUS_FATAL " << error.what() << '\n';
    return 70;
  }
}
