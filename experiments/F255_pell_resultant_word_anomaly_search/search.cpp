#include <algorithm>
#include <atomic>
#include <chrono>
#include <cmath>
#include <cstdint>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <limits>
#include <map>
#include <mutex>
#include <numeric>
#include <set>
#include <sstream>
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
static constexpr int FACTOR_BITS[] = {12, 16, 20, 24, 28, 32, 40, 48, 56, 60};
static constexpr int RANDOM_PER_BITS = 4096;
static constexpr int SAFE_PER_BITS = 1024;
static constexpr int SAFE_12_BITS = 128;
static constexpr int MAX_PELL_INDEX = 480;

enum Channel {
  BASELINE,
  ROWS,
  SAME_RES,
  CROSS_RES,
  HASH_RES,
  NORM_MINUS,
  NORM_PLUS,
  CARRY3,
  CARRY5,
  COMBINED,
  CHANNEL_COUNT
};

static const char* CHANNEL_NAMES[] = {
    "baseline", "rows", "same_res", "cross_res", "hash_res",
    "norm_minus", "norm_plus", "carry3", "carry5", "combined"};

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

static u64 mul_mod(u64 a, u64 b, u64 m) {
  if (m == 1) return 0;
  return static_cast<u64>((static_cast<u128>(a) * b) % m);
}

static u64 add_mod(u64 a, u64 b, u64 m) {
  if (m == 1) return 0;
  return static_cast<u64>((static_cast<u128>(a) + b) % m);
}

static u64 sub_mod(u64 a, u64 b, u64 m) {
  if (m == 1) return 0;
  return a >= b ? a - b : static_cast<u64>(static_cast<u128>(a) + m - b);
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
    bool witness = true;
    for (u64 r = 1; r < s; ++r) {
      x = mul_mod(x, x, n);
      if (x == n - 1) {
        witness = false;
        break;
      }
    }
    if (witness) return false;
  }
  return true;
}

static u64 random_prime(int bits, Rng& rng) {
  require(bits >= 3 && bits <= 60, "prime bit range");
  const u64 low = 1ULL << (bits - 1);
  const u64 mask = (1ULL << bits) - 1;
  for (;;) {
    u64 x = (rng.next() & mask) | low | 1ULL;
    for (int step = 0; step < 4096 && x <= mask; ++step, x += 2) {
      if (is_prime(x)) return x;
    }
  }
}

static u64 random_safe_prime(int bits, Rng& rng) {
  for (;;) {
    const u64 r = random_prime(bits - 1, rng);
    const u64 p = 2 * r + 1;
    if ((p >> (bits - 1)) == 1 && is_prime(p)) return p;
  }
}

static int bit_length(const cpp_int& x) {
  require(x > 0, "positive bit length");
  return boost::multiprecision::msb(x) + 1;
}

static u64 mod_cpp(const cpp_int& x, u64 m) {
  if (m == 1) return 0;
  cpp_int r = x % m;
  if (r < 0) r += m;
  return r.convert_to<u64>();
}

struct PellFundamental {
  int D;
  cpp_int S;
  cpp_int T;
  std::vector<cpp_int> T_values;
};

static PellFundamental fundamental_pell(int D) {
  int a0 = static_cast<int>(std::sqrt(D));
  require(a0 * a0 != D, "nonsquare D");
  int m = 0, den_cf = 1, a = a0;
  cpp_int p_prev = 1, p = a;
  cpp_int q_prev = 0, q = 1;
  while (p * p - D * q * q != 1) {
    m = den_cf * a - m;
    den_cf = (D - m * m) / den_cf;
    a = (a0 + m) / den_cf;
    cpp_int p_next = a * p + p_prev;
    cpp_int q_next = a * q + q_prev;
    p_prev = p;
    q_prev = q;
    p = p_next;
    q = q_next;
  }
  return {D, p, q, {}};
}

static void populate_pell_values(PellFundamental& fund) {
  fund.T_values.assign(MAX_PELL_INDEX + 1, 0);
  cpp_int S = 1, T = 0;
  for (int j = 1; j <= MAX_PELL_INDEX; ++j) {
    const cpp_int nextS = fund.S * S + fund.D * fund.T * T;
    const cpp_int nextT = fund.S * T + fund.T * S;
    S = nextS;
    T = nextT;
    fund.T_values[j] = T;
  }
}

struct Row {
  int D_index;
  int D;
  int j;
  cpp_int T;
  cpp_int k;
  cpp_int y;
  u64 tmod[2];
  u64 kmod[2];
  u64 ymod[2];
  u64 amod[2];
};

struct InputResult {
  int factor_bits;
  bool safe;
  u64 p;
  u64 q;
  cpp_int N;
  int n;
  u64 residual[2];
  u64 captured[CHANNEL_COUNT][2];
  long double quality[CHANNEL_COUNT];
};

static u64 resultant_mod(const Row& a, const Row& b, int side, u64 mod) {
  if (mod == 1) return 0;
  const u64 D = static_cast<u64>(a.D) % mod;
  const u64 E = static_cast<u64>(b.D) % mod;
  const u64 delta = sub_mod(mul_mod(a.tmod[side], b.kmod[side], mod),
                            mul_mod(b.tmod[side], a.kmod[side], mod), mod);
  const u64 delta2 = mul_mod(delta, delta, mod);
  const u64 ki2 = mul_mod(a.kmod[side], a.kmod[side], mod);
  const u64 kj2 = mul_mod(b.kmod[side], b.kmod[side], mod);
  u64 center = mul_mod(mul_mod(D, E, mod), delta2, mod);
  center = add_mod(center, mul_mod(E, kj2, mod), mod);
  center = add_mod(center, mul_mod(D, ki2, mod), mod);
  const u64 left = mul_mod(center, center, mod);
  u64 right = mul_mod(4 % mod, mul_mod(D, E, mod), mod);
  right = mul_mod(right, mul_mod(ki2, kj2, mod), mod);
  return sub_mod(left, right, mod);
}

static std::pair<u64, u64> same_norm_mod(const Row& a, const Row& b,
                                          int side, u64 mod) {
  if (mod == 1) return {0, 0};
  require(a.D == b.D, "same-D norm edge");
  const u64 D = static_cast<u64>(a.D) % mod;
  const u64 delta = sub_mod(mul_mod(a.tmod[side], b.kmod[side], mod),
                            mul_mod(b.tmod[side], a.kmod[side], mod), mod);
  const u64 base = mul_mod(D, mul_mod(delta, delta, mod), mod);
  const u64 minus = sub_mod(a.kmod[side], b.kmod[side], mod);
  const u64 plus = add_mod(a.kmod[side], b.kmod[side], mod);
  return {add_mod(base, mul_mod(minus, minus, mod), mod),
          add_mod(base, mul_mod(plus, plus, mod), mod)};
}

static InputResult process_input(int factor_bits, bool safe, u64 p, u64 q,
                                 const std::vector<PellFundamental>& funds) {
  if (p > q) std::swap(p, q);
  require(p < q && q < 2 * p, "balanced input");
  require(is_prime(p) && is_prime(q), "prime labels");
  cpp_int N = cpp_int(p) * q;
  const int n = bit_length(N);
  const u64 d = std::gcd(p - 1, q - 1);
  const u64 residuals[2] = {(p - 1) / d, (q - 1) / d};
  const u64 mods[2] = {residuals[0], residuals[1]};
  const int J = 4 * n;

  std::vector<Row> rows;
  std::vector<std::vector<int>> ids(std::size(D_VALUES));
  for (std::size_t di = 0; di < std::size(D_VALUES); ++di) {
    ids[di].assign(J + 1, -1);
    require(J <= MAX_PELL_INDEX, "Pell table range");
    for (int j = 1; j <= J; ++j) {
      const cpp_int& T = funds[di].T_values[j];
      cpp_int k = T / N;
      if (k == 0) continue;
      cpp_int y = T - k * N;
      require(y >= 0 && y < N, "canonical Pell remainder");
      Row row;
      row.D_index = static_cast<int>(di);
      row.D = D_VALUES[di];
      row.j = j;
      row.T = T;
      row.k = k;
      row.y = y;
      for (int side = 0; side < 2; ++side) {
        const u64 mod = mods[side];
        row.tmod[side] = mod_cpp(T, mod);
        row.kmod[side] = mod_cpp(k, mod);
        row.ymod[side] = mod_cpp(y, mod);
        if (mod == 1) {
          row.amod[side] = 0;
        } else {
          row.amod[side] = add_mod(
              1 % mod,
              mul_mod(static_cast<u64>(row.D) % mod,
                      mul_mod(row.ymod[side], row.ymod[side], mod), mod),
              mod);
        }
      }
      ids[di][j] = static_cast<int>(rows.size());
      rows.push_back(std::move(row));
    }
  }
  require(!rows.empty(), "post-wrap bank nonempty");

  u64 accum[CHANNEL_COUNT][2];
  for (int ch = 0; ch < CHANNEL_COUNT; ++ch) {
    for (int side = 0; side < 2; ++side) {
      accum[ch][side] = mod_cpp(N - 1, mods[side]);
    }
  }

  auto add_factor = [&](Channel ch, u64 fp, u64 fq) {
    const u64 values[2] = {fp, fq};
    for (int side = 0; side < 2; ++side) {
      accum[ch][side] = mul_mod(accum[ch][side], values[side], mods[side]);
      accum[COMBINED][side] = mul_mod(accum[COMBINED][side], values[side], mods[side]);
    }
  };

  for (const Row& row : rows) add_factor(ROWS, row.amod[0], row.amod[1]);

  auto add_same_edge = [&](const Row& a, const Row& b) {
    u64 r[2], minus[2], plus[2];
    for (int side = 0; side < 2; ++side) {
      r[side] = resultant_mod(a, b, side, mods[side]);
      auto values = same_norm_mod(a, b, side, mods[side]);
      minus[side] = values.first;
      plus[side] = values.second;
    }
    add_factor(SAME_RES, r[0], r[1]);
    add_factor(NORM_MINUS, minus[0], minus[1]);
    add_factor(NORM_PLUS, plus[0], plus[1]);
  };

  for (std::size_t di = 0; di < ids.size(); ++di) {
    for (int j = 1; j <= J; ++j) {
      if (ids[di][j] < 0) continue;
      for (int off : OFFSETS) {
        if (j + off <= J && ids[di][j + off] >= 0)
          add_same_edge(rows[ids[di][j]], rows[ids[di][j + off]]);
      }
      for (int mult : {3, 5}) {
        if (mult * j <= J && ids[di][mult * j] >= 0)
          add_same_edge(rows[ids[di][j]], rows[ids[di][mult * j]]);
      }
    }
  }

  for (int j = 1; j <= J; ++j) {
    for (std::size_t da = 0; da < ids.size(); ++da) {
      if (ids[da][j] < 0) continue;
      for (std::size_t db = da + 1; db < ids.size(); ++db) {
        if (ids[db][j] < 0) continue;
        const Row& a = rows[ids[da][j]];
        const Row& b = rows[ids[db][j]];
        add_factor(CROSS_RES,
                   resultant_mod(a, b, 0, mods[0]),
                   resultant_mod(a, b, 1, mods[1]));
      }
    }
  }

  const cpp_int low_mask = (cpp_int(1) << 64) - 1;
  const u64 n_low = static_cast<u64>(N & low_mask);
  for (std::size_t i = 0; i < rows.size(); ++i) {
    for (u64 h = 0; h < 4; ++h) {
      const u64 key = n_low ^ (static_cast<u64>(i) * 0xd6e8feb86659fd93ULL)
                      ^ (h * 0xa0761d6478bd642fULL);
      std::size_t j = splitmix64(key) % rows.size();
      if (j == i) j = (j + 1) % rows.size();
      add_factor(HASH_RES,
                 resultant_mod(rows[i], rows[j], 0, mods[0]),
                 resultant_mod(rows[i], rows[j], 1, mods[1]));
    }
  }

  for (std::size_t di = 0; di < ids.size(); ++di) {
    const int D = D_VALUES[di];
    for (int j = 1; j <= J; ++j) {
      if (ids[di][j] < 0) continue;
      const cpp_int& y = rows[ids[di][j]].y;
      if (3 * j <= J && ids[di][3 * j] >= 0) {
        cpp_int F = y * (3 + 4 * D * y * y);
        cpp_int diff = F - rows[ids[di][3 * j]].y;
        require(diff >= 0 && diff % N == 0, "triple carry identity");
        cpp_int c = diff / N;
        cpp_int factor = c == 0 ? cpp_int(1)
                                : cpp_int(D) * c * (2 * rows[ids[di][3 * j]].y + c * N);
        add_factor(CARRY3, mod_cpp(factor, mods[0]), mod_cpp(factor, mods[1]));
      }
      if (5 * j <= J && ids[di][5 * j] >= 0) {
        cpp_int y2 = y * y;
        cpp_int F = y * (5 + 20 * D * y2 + 16 * D * D * y2 * y2);
        cpp_int diff = F - rows[ids[di][5 * j]].y;
        require(diff >= 0 && diff % N == 0, "quintuple carry identity");
        cpp_int c = diff / N;
        cpp_int factor = c == 0 ? cpp_int(1)
                                : cpp_int(D) * c * (2 * rows[ids[di][5 * j]].y + c * N);
        add_factor(CARRY5, mod_cpp(factor, mods[0]), mod_cpp(factor, mods[1]));
      }
    }
  }

  InputResult result;
  result.factor_bits = factor_bits;
  result.safe = safe;
  result.p = p;
  result.q = q;
  result.N = N;
  result.n = n;
  result.residual[0] = residuals[0];
  result.residual[1] = residuals[1];
  for (int ch = 0; ch < CHANNEL_COUNT; ++ch) {
    long double best = 0;
    for (int side = 0; side < 2; ++side) {
      const u64 s = residuals[side];
      const u64 powered = s == 1 ? 0 : pow_mod(accum[ch][side], n, s);
      const u64 g = s == 1 ? 1 : std::gcd(powered, s);
      result.captured[ch][side] = g;
      best = std::max(best, static_cast<long double>(g) / s);
    }
    result.quality[ch] = best;
  }
  return result;
}

struct Task {
  int factor_bits;
  bool safe;
  int index;
  u64 seed;
  u64 p;
  u64 q;
};

static std::pair<u64, u64> generate_pair(const Task& task) {
  Rng rng(task.seed);
  for (;;) {
    u64 p = task.safe ? random_safe_prime(task.factor_bits, rng)
                      : random_prime(task.factor_bits, rng);
    u64 q = task.safe ? random_safe_prime(task.factor_bits, rng)
                      : random_prime(task.factor_bits, rng);
    if (p == q) continue;
    if (p > q) std::swap(p, q);
    if (q < 2 * p) return {p, q};
  }
}

static std::string cpp_string(const cpp_int& x) {
  return x.convert_to<std::string>();
}

static long double neg_log2(long double x) {
  return -std::log2(x);
}

static long double quantile(std::vector<long double> values, long double q) {
  require(!values.empty(), "quantile nonempty");
  std::sort(values.begin(), values.end());
  const long double pos = q * (values.size() - 1);
  const std::size_t lo = static_cast<std::size_t>(std::floor(pos));
  const std::size_t hi = static_cast<std::size_t>(std::ceil(pos));
  if (lo == hi) return values[lo];
  const long double t = pos - lo;
  return values[lo] * (1 - t) + values[hi] * t;
}

static void self_test(const std::vector<PellFundamental>& funds) {
  require(is_prime(61) && is_prime(71) && !is_prime(4331), "primality self-test");
  InputResult r = process_input(7, false, 61, 71, funds);
  require(r.N == 4331, "N self-test");
  require(r.residual[0] == 6 && r.residual[1] == 7, "residual self-test");
  for (int ch = 0; ch < CHANNEL_COUNT; ++ch) {
    require(r.captured[ch][0] >= 1 && r.captured[ch][0] <= r.residual[0],
            "capture p range");
    require(r.captured[ch][1] >= 1 && r.captured[ch][1] <= r.residual[1],
            "capture q range");
  }
  std::cout << "SELF_TEST_PASS N=4331 channels=" << CHANNEL_COUNT << "\n";
}

int main(int argc, char** argv) try {
  std::vector<PellFundamental> funds;
  for (int D : D_VALUES) {
    funds.push_back(fundamental_pell(D));
    populate_pell_values(funds.back());
  }
  if (argc >= 2 && std::string(argv[1]) == "--self-test") {
    self_test(funds);
    return 0;
  }
  require(argc == 4, "usage: search THREADS OUT_JSON OUT_TSV");
  const int thread_count = std::stoi(argv[1]);
  require(thread_count >= 1 && thread_count <= 16, "thread count 1..16");
  const std::string json_path = argv[2];
  const std::string tsv_path = argv[3];

  std::vector<Task> tasks;
  for (int bits : FACTOR_BITS) {
    for (int safe_int = 0; safe_int <= 1; ++safe_int) {
      const bool safe = safe_int != 0;
      const int count = safe ? (bits == 12 ? SAFE_12_BITS : SAFE_PER_BITS)
                             : RANDOM_PER_BITS;
      const u64 cohort_tag = safe ? 0x534146455f463235ULL : 0x52414e445f463235ULL;
      std::set<std::pair<u64, u64>> seen;
      for (int i = 0; i < count; ++i) {
        const u64 base_seed = splitmix64(cohort_tag ^ (static_cast<u64>(bits) << 48)
                                         ^ static_cast<u64>(i));
        for (u64 attempt = 0;; ++attempt) {
          require(attempt < 1000000, "unique cohort generation exhausted");
          const u64 seed = splitmix64(base_seed ^
                                      (attempt * 0x9e3779b97f4a7c15ULL));
          Task task{bits, safe, i, seed, 0, 0};
          auto pair = generate_pair(task);
          if (!seen.insert(pair).second) continue;
          task.p = pair.first;
          task.q = pair.second;
          tasks.push_back(task);
          break;
        }
      }
    }
  }
  require(tasks.size() == 50304, "frozen task count");
  std::vector<InputResult> results(tasks.size());
  std::atomic<std::size_t> next{0};
  std::atomic<std::size_t> done{0};
  std::mutex io_mutex;
  const auto start = std::chrono::steady_clock::now();

  auto worker = [&]() {
    for (;;) {
      const std::size_t index = next.fetch_add(1);
      if (index >= tasks.size()) return;
      results[index] = process_input(tasks[index].factor_bits, tasks[index].safe,
                                     tasks[index].p, tasks[index].q, funds);
      const std::size_t completed = done.fetch_add(1) + 1;
      if (completed % 256 == 0 || completed == tasks.size()) {
        std::lock_guard<std::mutex> lock(io_mutex);
        const double seconds = std::chrono::duration<double>(
            std::chrono::steady_clock::now() - start).count();
        std::cerr << "progress=" << completed << "/" << tasks.size()
                  << " elapsed=" << std::fixed << std::setprecision(1)
                  << seconds << "s rate=" << completed / seconds << "/s\n";
      }
    }
  };

  std::vector<std::thread> threads;
  for (int i = 0; i < thread_count; ++i) threads.emplace_back(worker);
  for (auto& thread : threads) thread.join();
  const double elapsed = std::chrono::duration<double>(
      std::chrono::steady_clock::now() - start).count();

  std::ofstream tsv(tsv_path);
  require(static_cast<bool>(tsv), "open TSV");
  tsv << "factor_bits\tcohort\tp\tq\tN\tn\ts_p\ts_q";
  for (int ch = 0; ch < CHANNEL_COUNT; ++ch)
    tsv << '\t' << CHANNEL_NAMES[ch] << "_gp\t" << CHANNEL_NAMES[ch] << "_gq"
        << '\t' << CHANNEL_NAMES[ch] << "_neglog2H";
  tsv << '\n';
  tsv << std::setprecision(18);
  for (const auto& r : results) {
    tsv << r.factor_bits << '\t' << (r.safe ? "safe" : "random") << '\t'
        << r.p << '\t' << r.q << '\t' << cpp_string(r.N) << '\t' << r.n
        << '\t' << r.residual[0] << '\t' << r.residual[1];
    for (int ch = 0; ch < CHANNEL_COUNT; ++ch)
      tsv << '\t' << r.captured[ch][0] << '\t' << r.captured[ch][1]
          << '\t' << static_cast<double>(neg_log2(r.quality[ch]));
    tsv << '\n';
  }
  tsv.close();

  std::ofstream json(json_path);
  require(static_cast<bool>(json), "open JSON");
  json << std::setprecision(18);
  json << "{\n  \"experiment\": \"F255-D01\",\n"
       << "  \"threads\": " << thread_count << ",\n"
       << "  \"elapsed_seconds\": " << elapsed << ",\n"
       << "  \"input_count\": " << results.size() << ",\n"
       << "  \"summaries\": [\n";
  bool first_summary = true;
  for (int bits : FACTOR_BITS) {
    for (int safe_int = 0; safe_int <= 1; ++safe_int) {
      const bool safe = safe_int != 0;
      std::vector<const InputResult*> cohort;
      for (const auto& r : results)
        if (r.factor_bits == bits && r.safe == safe) cohort.push_back(&r);
      for (int ch = 0; ch < CHANNEL_COUNT; ++ch) {
        std::vector<long double> logs;
        long double mean = 0;
        std::size_t improved = 0, saturated = 0;
        const InputResult* worst = nullptr;
        for (const InputResult* r : cohort) {
          mean += r->quality[ch];
          logs.push_back(neg_log2(r->quality[ch]));
          if (r->quality[ch] > r->quality[BASELINE]) ++improved;
          if (r->captured[ch][0] == r->residual[0] ||
              r->captured[ch][1] == r->residual[1]) ++saturated;
          if (!worst || r->quality[ch] < worst->quality[ch]) worst = r;
        }
        mean /= cohort.size();
        if (!first_summary) json << ",\n";
        first_summary = false;
        json << "    {\"factor_bits\": " << bits
             << ", \"cohort\": \"" << (safe ? "safe" : "random")
             << "\", \"word\": \"" << CHANNEL_NAMES[ch]
             << "\", \"count\": " << cohort.size()
             << ", \"mean_H\": " << static_cast<double>(mean)
             << ", \"median_neglog2H\": " << static_cast<double>(quantile(logs, 0.5L))
             << ", \"p90_neglog2H\": " << static_cast<double>(quantile(logs, 0.9L))
             << ", \"p99_neglog2H\": " << static_cast<double>(quantile(logs, 0.99L))
             << ", \"worst_H\": " << static_cast<double>(worst->quality[ch])
             << ", \"improved_over_baseline\": " << improved
             << ", \"saturated\": " << saturated
             << ", \"worst\": {\"p\": " << worst->p
             << ", \"q\": " << worst->q
             << ", \"N\": \"" << cpp_string(worst->N)
             << "\", \"gp\": " << worst->captured[ch][0]
             << ", \"gq\": " << worst->captured[ch][1]
             << ", \"sp\": " << worst->residual[0]
             << ", \"sq\": " << worst->residual[1] << "}}";
      }
    }
  }
  json << "\n  ]\n}\n";
  json.close();
  std::cout << "F255_D01_PASS inputs=" << results.size()
            << " elapsed_seconds=" << std::fixed << std::setprecision(3)
            << elapsed << "\n";
  return 0;
} catch (const std::exception& e) {
  std::cerr << "F255_D01_FAIL " << e.what() << "\n";
  return 1;
}
