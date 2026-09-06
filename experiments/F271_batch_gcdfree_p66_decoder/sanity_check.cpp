#include <gmpxx.h>

#include <algorithm>
#include <cstdint>
#include <iostream>
#include <stdexcept>
#include <tuple>
#include <vector>

using cpp_int = mpz_class;

struct Block {
  cpp_int value;
  unsigned x_exp;
  unsigned y_exp;
};

struct Stats {
  uint64_t nodes = 0;
  uint64_t gcd_calls = 0;
};

cpp_int gcdz(cpp_int a, cpp_int b) {
  if (a < 0) a = -a;
  if (b < 0) b = -b;
  cpp_int answer;
  mpz_gcd(answer.get_mpz_t(), a.get_mpz_t(), b.get_mpz_t());
  return answer;
}

unsigned bitlen(const cpp_int& x) {
  if (x <= 0) throw std::runtime_error("bitlen domain");
  return static_cast<unsigned>(mpz_sizeinbase(x.get_mpz_t(), 2));
}

cpp_int powz(cpp_int base, unsigned exponent) {
  cpp_int answer = 1;
  while (exponent != 0) {
    if ((exponent & 1U) != 0) answer *= base;
    exponent >>= 1;
    if (exponent != 0) base *= base;
  }
  return answer;
}

cpp_int powmod(cpp_int base, unsigned exponent, const cpp_int& modulus) {
  cpp_int answer;
  mpz_powm_ui(answer.get_mpz_t(), base.get_mpz_t(), exponent,
              modulus.get_mpz_t());
  return answer;
}

cpp_int saturated_part(const cpp_int& u, const cpp_int& v, Stats& stats) {
  if (u <= 1 || v <= 1) throw std::runtime_error("saturation domain");
  ++stats.gcd_calls;
  return gcdz(u, powmod(v, bitlen(u), u));
}

std::vector<Block> same_support_base(const cpp_int& x, const cpp_int& y,
                                     const cpp_int* supplied_gcd,
                                     Stats& stats) {
  if (x <= 1 || y <= 1) throw std::runtime_error("same-support domain");
  ++stats.nodes;
  cpp_int d;
  if (supplied_gcd != nullptr) {
    d = *supplied_gcd;
  } else {
    ++stats.gcd_calls;
    d = gcdz(x, y);
  }
  if (d <= 1) throw std::runtime_error("same-support gcd");

  cpp_int x0 = x / d;
  cpp_int y0 = y / d;
  std::vector<Block> out;

  cpp_int a = 1;
  if (x0 > 1) {
    a = saturated_part(d, x0, stats);
    if (a <= 1) throw std::runtime_error("same-support x branch");
    auto branch = same_support_base(x0, a, nullptr, stats);
    for (Block& block : branch) {
      out.push_back(
          {block.value, block.x_exp + block.y_exp, block.y_exp});
    }
  }

  cpp_int b = 1;
  if (y0 > 1) {
    b = saturated_part(d, y0, stats);
    if (b <= 1) throw std::runtime_error("same-support y branch");
    auto branch = same_support_base(y0, b, nullptr, stats);
    for (Block& block : branch) {
      out.push_back(
          {block.value, block.y_exp, block.x_exp + block.y_exp});
    }
  }

  cpp_int c = d / (a * b);
  if (c > 1) out.push_back({c, 1, 1});
  return out;
}

std::vector<Block> two_base(const cpp_int& x, const cpp_int& y,
                            const cpp_int& supplied_gcd, Stats& stats) {
  if (x <= 1 || y <= 1 || supplied_gcd <= 1) {
    throw std::runtime_error("two-base domain");
  }

  cpp_int shared_x = saturated_part(x, y, stats);
  cpp_int shared_y = saturated_part(y, x, stats);
  cpp_int x_only = x / shared_x;
  cpp_int y_only = y / shared_y;
  // Checker-only oracle. This gcd is not part of TWO_BASE or Stats.
  if (gcdz(shared_x, shared_y) != supplied_gcd)
    throw std::runtime_error("supplied root gcd mismatch");

  std::vector<Block> out;
  if (x_only > 1) out.push_back({x_only, 1, 0});
  if (y_only > 1) out.push_back({y_only, 0, 1});
  auto shared = same_support_base(shared_x, shared_y, &supplied_gcd, stats);
  out.insert(out.end(), shared.begin(), shared.end());
  return out;
}

void verify_pair(const cpp_int& x, const cpp_int& y,
                 uint64_t valuation_mass_bound, uint64_t& maximum_nodes) {
  // Checker-only stand-in for the leaf gcd carried by the product tree.
  cpp_int d = gcdz(x, y);
  if (d == 1 || x == 1 || y == 1) return;
  Stats stats;
  std::vector<Block> blocks = two_base(x, y, d, stats);
  if (stats.nodes > valuation_mass_bound || stats.gcd_calls != 2 * stats.nodes)
    throw std::runtime_error("node or gcd bound");
  maximum_nodes = std::max(maximum_nodes, stats.nodes);

  cpp_int rebuilt_x = 1;
  cpp_int rebuilt_y = 1;
  for (size_t i = 0; i < blocks.size(); ++i) {
    if (blocks[i].value <= 1) throw std::runtime_error("unit block");
    if (blocks[i].x_exp == 0 && blocks[i].y_exp == 0)
      throw std::runtime_error("zero exponent block");
    rebuilt_x *= powz(blocks[i].value, blocks[i].x_exp);
    rebuilt_y *= powz(blocks[i].value, blocks[i].y_exp);
    // Checker-only quadratic oracle; the decoder uses terminal remainders.
    for (size_t j = 0; j < i; ++j) {
      if (gcdz(blocks[i].value, blocks[j].value) != 1)
        throw std::runtime_error("noncoprime output");
    }
  }
  if (rebuilt_x != x || rebuilt_y != y)
    throw std::runtime_error("reconstruction");
}

uint64_t omega_with_multiplicity(uint64_t x) {
  uint64_t answer = 0;
  for (uint64_t p = 2; p * p <= x; ++p) {
    while (x % p == 0) {
      x /= p;
      ++answer;
    }
  }
  if (x > 1) ++answer;
  return answer;
}

std::vector<unsigned> primes_through_count(size_t wanted) {
  const unsigned limit = 20000;
  std::vector<bool> prime(limit + 1, true);
  prime[0] = prime[1] = false;
  for (unsigned p = 2; p * p <= limit; ++p) {
    if (!prime[p]) continue;
    for (unsigned q = p * p; q <= limit; q += p) prime[q] = false;
  }
  std::vector<unsigned> out;
  for (unsigned p = 2; p <= limit && out.size() < wanted; ++p) {
    if (prime[p]) out.push_back(p);
  }
  if (out.size() != wanted) throw std::runtime_error("prime sieve limit");
  return out;
}

int main() {
  uint64_t exhaustive_maximum_nodes = 0;
  uint64_t pair_count = 0;
  for (uint64_t x = 1; x <= 500; ++x) {
    for (uint64_t y = 1; y <= 500; ++y) {
      verify_pair(cpp_int(static_cast<unsigned long>(x)),
                  cpp_int(static_cast<unsigned long>(y)),
                  omega_with_multiplicity(x) + omega_with_multiplicity(y),
                  exhaustive_maximum_nodes);
      ++pair_count;
    }
  }

  cpp_int two360 = cpp_int(1) << 360;
  cpp_int two359 = cpp_int(1) << 359;
  cpp_int mixed_x = (cpp_int(1) << 100) * powz(cpp_int(3), 7);
  cpp_int mixed_y = (cpp_int(1) << 7) * powz(cpp_int(3), 100);
  const std::vector<std::tuple<cpp_int, cpp_int, uint64_t>> edges = {
      {cpp_int(64), cpp_int(64), 12},
      {two360, two359, 719},
      {two360, cpp_int(2), 361},
      {mixed_x, mixed_y, 214},
      {cpp_int(12), cpp_int(18), 6},
      {cpp_int(72), cpp_int(108), 10},
  };
  uint64_t edge_maximum_nodes = 0;
  for (const auto& [x, y, mass] : edges)
    verify_pair(x, y, mass, edge_maximum_nodes);

  if (exhaustive_maximum_nodes != 11 || edge_maximum_nodes != 360)
    throw std::runtime_error("maximum node certificate");

  std::vector<unsigned> primes = primes_through_count(1876);
  cpp_int primorial58 = 1;
  for (size_t i = 0; i < 58; ++i) primorial58 *= primes[i];
  unsigned bits58 = bitlen(primorial58);
  cpp_int primorial = 1;
  for (size_t i = 0; i < 1875; ++i) primorial *= primes[i];
  unsigned bits1875 = bitlen(primorial);
  primorial *= primes[1875];
  unsigned bits1876 = bitlen(primorial);
  if (primes[56] != 269 || primes[57] != 271 || bits58 != 368 ||
      primes[1874] != 16103 || primes[1875] != 16111 ||
      bits1875 != 23102 || bits1876 != 23116) {
    throw std::runtime_error("primorial certificate");
  }

  constexpr uint64_t m = 64;
  constexpr uint64_t valuation_mass = 23040;
  constexpr uint64_t touches = 63 * 57;
  constexpr uint64_t blocks = 1875;
  constexpr uint64_t tree_depth = 11;
  constexpr uint64_t gcd_calls =
      (tree_depth + 1) * touches + m + 2 * valuation_mass + blocks;
  constexpr uint64_t packet_calls = 768 * gcd_calls;
  static_assert(gcd_calls == 91111);
  static_assert(packet_calls == 69973248);

  std::cout << "PASS pairs=" << pair_count
            << " max_exhaustive_pair_nodes=" << exhaustive_maximum_nodes
            << " max_fixed_edge_nodes=" << edge_maximum_nodes
            << " p58=" << primes[57]
            << " primorial58_bits=" << bits58
            << " p1875=" << primes[1874]
            << " primorial1875_bits=" << bits1875
            << " p1876=" << primes[1875]
            << " primorial1876_bits=" << bits1876
            << " f265_gcd_calls_per_bank=" << gcd_calls
            << " f265_gcd_calls_packet=" << packet_calls << '\n';
}
