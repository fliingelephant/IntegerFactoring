#include <algorithm>
#include <array>
#include <atomic>
#include <cerrno>
#include <chrono>
#include <condition_variable>
#include <cstdint>
#include <cstring>
#include <dirent.h>
#include <exception>
#include <fcntl.h>
#include <functional>
#include <iomanip>
#include <limits>
#include <map>
#include <memory>
#include <mutex>
#include <new>
#include <optional>
#include <signal.h>
#include <set>
#include <sstream>
#include <stdexcept>
#include <string>
#include <sys/resource.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <thread>
#include <tuple>
#include <unistd.h>
#include <utility>
#include <vector>

#include <boost/multiprecision/cpp_int.hpp>

extern char** environ;

namespace {

using boost::multiprecision::cpp_int;
using u64 = std::uint64_t;

constexpr char VERSION[] = "F279-D06";
constexpr char ROLE[] = "f279_public";
constexpr u64 MAX_RAW_HITS_TOTAL = 131072;
constexpr u64 MAX_GLOBAL_ORDER_CHECKS_TOTAL = 131072;
constexpr u64 HARD_OUTPUT_CAP = 536870912;
constexpr u64 MAX_RECORD_CERTIFICATE = 1536;
constexpr u64 MAX_RECORD_SCORE = 256;
constexpr u64 MAX_RECORD_ROW = 512;
constexpr u64 MAX_RECORD_SELECTION = 256;
constexpr u64 MAX_RECORD_DIAGNOSTIC = 1024;
constexpr u64 MAX_JSON_BYTES = 1048576;
constexpr u64 MAX_STATUS_BYTES = 65536;
constexpr u64 TAPE_BYTES = 176947200;
constexpr int ROWS_PER_PHASE = 1024;
constexpr int SOURCES = 900;
constexpr int CANDIDATES = 25000;
constexpr int WORKERS = 4;
constexpr int K_BOX = 16;
constexpr int MAX_ATTEMPTS = 3;
constexpr int CONTROLS_PER_SOURCE = 2;

enum class Mode {
  Invalid,
  SelfTest,
  Benchmark,
  Discovery,
  Heldout,
  ReplayDiscovery,
  ReplayHeldout
};

struct Failure final : std::runtime_error {
  int exit_code;
  std::string error_code;
  Failure(int e, std::string c, const std::string& message)
      : std::runtime_error(message), exit_code(e), error_code(std::move(c)) {}
};

[[noreturn]] void fail(int exit_code, const std::string& error_code,
                       const std::string& message) {
  throw Failure(exit_code, error_code, message);
}

void require(bool ok, int exit_code, const std::string& error_code,
             const std::string& message) {
  if (!ok) fail(exit_code, error_code, message);
}

std::string mode_token(Mode mode) {
  switch (mode) {
    case Mode::SelfTest: return "self-test";
    case Mode::Benchmark: return "benchmark";
    case Mode::Discovery: return "discovery";
    case Mode::Heldout: return "heldout";
    case Mode::ReplayDiscovery: return "replay-discovery";
    case Mode::ReplayHeldout: return "replay-heldout";
    default: return "";
  }
}

std::string phase_token(Mode mode) {
  if (mode == Mode::Discovery || mode == Mode::ReplayDiscovery)
    return "discovery";
  if (mode == Mode::Heldout || mode == Mode::ReplayHeldout)
    return "heldout";
  return "";
}

bool scientific_mode(Mode mode) {
  return mode == Mode::Discovery || mode == Mode::Heldout ||
         mode == Mode::ReplayDiscovery || mode == Mode::ReplayHeldout;
}

class Sha256 {
 public:
  Sha256() { reset(); }

  void update(const unsigned char* data, std::size_t length) {
    total_ += length;
    while (length != 0) {
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

  void update(const std::string& bytes) {
    update(reinterpret_cast<const unsigned char*>(bytes.data()), bytes.size());
  }

  std::string final_hex() {
    const u64 bits = total_ * 8;
    block_[used_++] = 0x80;
    if (used_ > 56) {
      while (used_ < 64) block_[used_++] = 0;
      compress(block_.data());
      used_ = 0;
    }
    while (used_ < 56) block_[used_++] = 0;
    for (int i = 7; i >= 0; --i)
      block_[used_++] = static_cast<unsigned char>(bits >> (8 * i));
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

  void compress(const unsigned char* bytes) {
    static constexpr std::uint32_t k[64] = {
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
    for (int i = 0; i < 16; ++i) {
      w[i] = (std::uint32_t(bytes[4*i]) << 24) |
             (std::uint32_t(bytes[4*i+1]) << 16) |
             (std::uint32_t(bytes[4*i+2]) << 8) |
             std::uint32_t(bytes[4*i+3]);
    }
    for (int i = 16; i < 64; ++i) {
      const auto s0 = rotr(w[i-15],7) ^ rotr(w[i-15],18) ^ (w[i-15] >> 3);
      const auto s1 = rotr(w[i-2],17) ^ rotr(w[i-2],19) ^ (w[i-2] >> 10);
      w[i] = w[i-16] + s0 + w[i-7] + s1;
    }
    auto a=state_[0], b=state_[1], c=state_[2], d=state_[3];
    auto e=state_[4], f=state_[5], g=state_[6], h=state_[7];
    for (int i = 0; i < 64; ++i) {
      const auto s1=rotr(e,6)^rotr(e,11)^rotr(e,25);
      const auto ch=(e&f)^((~e)&g);
      const auto t1=h+s1+ch+k[i]+w[i];
      const auto s0=rotr(a,2)^rotr(a,13)^rotr(a,22);
      const auto maj=(a&b)^(a&c)^(b&c);
      const auto t2=s0+maj;
      h=g; g=f; f=e; e=d+t1; d=c; c=b; b=a; a=t1+t2;
    }
    state_[0]+=a; state_[1]+=b; state_[2]+=c; state_[3]+=d;
    state_[4]+=e; state_[5]+=f; state_[6]+=g; state_[7]+=h;
  }
};

std::string sha256(const std::string& bytes) {
  Sha256 hash;
  hash.update(bytes);
  return hash.final_hex();
}

bool lowercase_hash(const std::string& value) {
  if (value.size() != 64) return false;
  for (char c : value)
    if (!((c >= '0' && c <= '9') || (c >= 'a' && c <= 'f'))) return false;
  return true;
}

std::string decimal(const cpp_int& value) {
  return value.convert_to<std::string>();
}

std::string decimal(u64 value) { return std::to_string(value); }

cpp_int parse_cpp_uint(const std::string& text, const std::string& context) {
  require(!text.empty(), 65, "input_schema", context + ": empty integer");
  require(text == "0" || (text[0] >= '1' && text[0] <= '9'),
          65, "input_schema", context + ": noncanonical integer");
  cpp_int value = 0;
  for (char c : text) {
    require(c >= '0' && c <= '9', 65, "input_schema",
            context + ": nondigit");
    value *= 10;
    value += c - '0';
  }
  return value;
}

u64 parse_u64(const std::string& text, const std::string& context,
              int exit_code = 65, const std::string& error = "input_schema") {
  require(!text.empty(), exit_code, error, context + ": empty integer");
  require(text == "0" || (text[0] >= '1' && text[0] <= '9'),
          exit_code, error, context + ": noncanonical integer");
  u64 value = 0;
  for (char c : text) {
    require(c >= '0' && c <= '9', exit_code, error, context + ": nondigit");
    const unsigned digit = unsigned(c - '0');
    require(value <= (std::numeric_limits<u64>::max() - digit) / 10,
            exit_code, error, context + ": overflow");
    value = value * 10 + digit;
  }
  return value;
}

std::vector<std::string> split_lines(const std::string& bytes,
                                     const std::string& context) {
  require(!bytes.empty() && bytes.back() == '\n', 65, "input_schema",
          context + ": final LF");
  require(bytes.find('\r') == std::string::npos, 65, "input_schema",
          context + ": CR");
  std::vector<std::string> lines;
  std::size_t begin = 0;
  while (begin < bytes.size()) {
    const std::size_t end = bytes.find('\n', begin);
    require(end != std::string::npos, 65, "input_schema", context + ": LF");
    lines.push_back(bytes.substr(begin, end - begin));
    begin = end + 1;
  }
  return lines;
}

std::vector<std::string> split_tabs(const std::string& line) {
  std::vector<std::string> fields;
  std::size_t begin = 0;
  for (;;) {
    const std::size_t end = line.find('\t', begin);
    if (end == std::string::npos) {
      fields.push_back(line.substr(begin));
      return fields;
    }
    fields.push_back(line.substr(begin, end - begin));
    begin = end + 1;
  }
}

std::string read_fd_all(int fd, u64 maximum, const std::string& context) {
  struct stat st{};
  require(::fstat(fd, &st) == 0, 65, "input_io", context + ": fstat");
  require(st.st_size >= 0 && static_cast<u64>(st.st_size) <= maximum,
          65, "input_schema", context + ": byte bound");
  std::string bytes(static_cast<std::size_t>(st.st_size), '\0');
  std::size_t done = 0;
  while (done < bytes.size()) {
    const ssize_t got = ::pread(fd, bytes.data() + done, bytes.size() - done,
                                static_cast<off_t>(done));
    if (got < 0 && errno == EINTR) continue;
    require(got > 0, 65, "input_io", context + ": pread");
    done += static_cast<std::size_t>(got);
  }
  return bytes;
}

std::string hash_fd(int fd, u64 expected_bytes, const std::string& context) {
  struct stat st{};
  require(::fstat(fd, &st) == 0, 65, "input_io", context + ": fstat");
  require(st.st_size >= 0 && static_cast<u64>(st.st_size) == expected_bytes,
          65, "input_auth", context + ": byte length");
  Sha256 hash;
  std::array<unsigned char, 1048576> buffer{};
  u64 offset = 0;
  while (offset < expected_bytes) {
    const std::size_t want = static_cast<std::size_t>(
        std::min<u64>(buffer.size(), expected_bytes - offset));
    ssize_t got = ::pread(fd, buffer.data(), want, static_cast<off_t>(offset));
    if (got < 0 && errno == EINTR) continue;
    require(got > 0, 65, "input_io", context + ": pread");
    hash.update(buffer.data(), static_cast<std::size_t>(got));
    offset += static_cast<u64>(got);
  }
  return hash.final_hex();
}

class JsonCursor {
 public:
  JsonCursor(const std::string& bytes, std::string context)
      : bytes_(bytes), context_(std::move(context)) {
    require(!bytes_.empty() && bytes_.back() == '\n', 65, "input_schema",
            context_ + ": final LF");
    bytes_.pop_back();
  }

  void begin_object() { take('{'); first_ = true; }
  void end_object() { take('}'); }
  void finish() {
    require(pos_ == bytes_.size(), 65, "input_schema",
            context_ + ": trailing JSON");
  }

  void key(const std::string& expected) {
    if (!first_) take(',');
    first_ = false;
    require(string_value() == expected, 65, "input_schema",
            context_ + ": key order");
    take(':');
  }

  std::string string_value() {
    take('"');
    std::string value;
    while (pos_ < bytes_.size() && bytes_[pos_] != '"') {
      const unsigned char c = static_cast<unsigned char>(bytes_[pos_++]);
      require(c >= 0x20 && c <= 0x7e && c != '\\', 65, "input_schema",
              context_ + ": string byte");
      value.push_back(static_cast<char>(c));
    }
    take('"');
    return value;
  }

  u64 uint_value() {
    const std::size_t begin = pos_;
    while (pos_ < bytes_.size() && bytes_[pos_] >= '0' && bytes_[pos_] <= '9')
      ++pos_;
    return parse_u64(bytes_.substr(begin, pos_ - begin), context_);
  }

  bool bool_value() {
    if (bytes_.compare(pos_, 4, "true") == 0) { pos_ += 4; return true; }
    if (bytes_.compare(pos_, 5, "false") == 0) { pos_ += 5; return false; }
    fail(65, "input_schema", context_ + ": Boolean");
  }

  void null_value() {
    require(bytes_.compare(pos_, 4, "null") == 0, 65, "input_schema",
            context_ + ": null");
    pos_ += 4;
  }

  std::vector<std::string> string_array() {
    std::vector<std::string> values;
    take('[');
    if (peek(']')) { take(']'); return values; }
    for (;;) {
      values.push_back(string_value());
      if (peek(']')) { take(']'); return values; }
      take(',');
    }
  }

  void begin_nested_object() { take('{'); nested_first_.push_back(first_); first_ = true; }
  void end_nested_object() { take('}'); first_ = nested_first_.back(); nested_first_.pop_back(); }

 private:
  std::string bytes_;
  std::string context_;
  std::size_t pos_ = 0;
  bool first_ = true;
  std::vector<bool> nested_first_;

  bool peek(char c) const { return pos_ < bytes_.size() && bytes_[pos_] == c; }
  void take(char c) {
    require(pos_ < bytes_.size() && bytes_[pos_] == c, 65, "input_schema",
            context_ + ": JSON punctuation");
    ++pos_;
  }
};

std::string json_string(const std::string& value) {
  for (unsigned char c : value)
    require(c >= 0x20 && c <= 0x7e && c != '"' && c != '\\',
            66, "serialization", "JSON string byte");
  return "\"" + value + "\"";
}

std::string phase_json(Mode mode) {
  const std::string phase = phase_token(mode);
  return phase.empty() ? "null" : json_string(phase);
}

struct Cli {
  Mode mode = Mode::Invalid;
  std::string trusted_containment;
  std::string trusted_inputs;
  std::string trusted_selection;
  std::string trusted_discovery_manifest;
};

std::string basename_of(const std::string& path) {
  const std::size_t slash = path.find_last_of('/');
  return slash == std::string::npos ? path : path.substr(slash + 1);
}

void expect_arg(int argc, char** argv, int index, const char* expected) {
  require(index < argc && std::string(argv[index]) == expected,
          64, "cli", "argv mismatch");
}

Cli parse_cli(int argc, char** argv) {
  require(argc >= 3, 64, "cli", "argc");
  require(basename_of(argv[0]) == ROLE, 64, "cli", "role basename");
  expect_arg(argc, argv, 1, "--mode");
  const std::string mode = argv[2];
  Cli cli;
  if (mode == "self-test") cli.mode = Mode::SelfTest;
  else if (mode == "benchmark") cli.mode = Mode::Benchmark;
  else if (mode == "discovery") cli.mode = Mode::Discovery;
  else if (mode == "heldout") cli.mode = Mode::Heldout;
  else if (mode == "replay-discovery") cli.mode = Mode::ReplayDiscovery;
  else if (mode == "replay-heldout") cli.mode = Mode::ReplayHeldout;
  else fail(64, "cli", "mode");

  if (cli.mode == Mode::SelfTest) {
    require(argc == 5, 64, "cli", "self-test argc");
    expect_arg(argc, argv, 3, "--status-fd"); expect_arg(argc, argv, 4, "10");
    return cli;
  }
  if (cli.mode == Mode::Benchmark) {
    require(argc == 7, 64, "cli", "benchmark argc");
    expect_arg(argc, argv, 3, "--scratch-dir-fd"); expect_arg(argc, argv, 4, "9");
    expect_arg(argc, argv, 5, "--status-fd"); expect_arg(argc, argv, 6, "10");
    return cli;
  }

  int i = 3;
  expect_arg(argc, argv, i++, "--public-fixture-fd"); expect_arg(argc, argv, i++, "3");
  expect_arg(argc, argv, i++, "--tape-fd"); expect_arg(argc, argv, i++, "4");
  expect_arg(argc, argv, i++, "--promise-fd"); expect_arg(argc, argv, i++, "5");
  expect_arg(argc, argv, i++, "--inputs-manifest-fd"); expect_arg(argc, argv, i++, "6");
  expect_arg(argc, argv, i++, "--containment-manifest-fd"); expect_arg(argc, argv, i++, "7");
  const bool has_selection = cli.mode != Mode::Discovery;
  const bool has_carry = cli.mode == Mode::Heldout || cli.mode == Mode::ReplayHeldout;
  if (has_selection) {
    expect_arg(argc, argv, i++, "--selection-fd"); expect_arg(argc, argv, i++, "8");
  }
  if (has_carry) {
    expect_arg(argc, argv, i++, "--discovery-public-manifest-fd"); expect_arg(argc, argv, i++, "11");
    expect_arg(argc, argv, i++, "--discovery-summary-fd"); expect_arg(argc, argv, i++, "12");
  }
  if (cli.mode == Mode::Discovery || cli.mode == Mode::Heldout) {
    expect_arg(argc, argv, i++, "--output-dir-fd"); expect_arg(argc, argv, i++, "9");
  } else {
    expect_arg(argc, argv, i++, "--phase-dir-fd"); expect_arg(argc, argv, i++, "9");
  }
  expect_arg(argc, argv, i++, "--status-fd"); expect_arg(argc, argv, i++, "10");
  expect_arg(argc, argv, i++, "--trusted-containment-sha256");
  require(i < argc && lowercase_hash(argv[i]), 64, "cli", "containment hash");
  cli.trusted_containment = argv[i++];
  expect_arg(argc, argv, i++, "--trusted-inputs-manifest-sha256");
  require(i < argc && lowercase_hash(argv[i]), 64, "cli", "inputs hash");
  cli.trusted_inputs = argv[i++];
  if (has_selection) {
    expect_arg(argc, argv, i++, "--trusted-selection-sha256");
    require(i < argc && lowercase_hash(argv[i]), 64, "cli", "selection hash");
    cli.trusted_selection = argv[i++];
  }
  if (has_carry) {
    expect_arg(argc, argv, i++, "--trusted-discovery-public-manifest-sha256");
    require(i < argc && lowercase_hash(argv[i]), 64, "cli", "discovery manifest hash");
    cli.trusted_discovery_manifest = argv[i++];
  }
  require(i == argc, 64, "cli", "trailing argv");
  return cli;
}

std::set<int> expected_descriptors(Mode mode) {
  if (mode == Mode::SelfTest) return {2,10};
  if (mode == Mode::Benchmark) return {2,9,10};
  if (mode == Mode::Discovery) return {2,3,4,5,6,7,9,10};
  if (mode == Mode::Heldout) return {2,3,4,5,6,7,8,9,10,11,12};
  if (mode == Mode::ReplayDiscovery) return {2,3,4,5,6,7,8,9,10};
  return {2,3,4,5,6,7,8,9,10,11,12};
}

void validate_environment_and_descriptors(Mode mode) {
  require(environ != nullptr && environ[0] != nullptr &&
          std::string(environ[0]) == "LC_ALL=C" && environ[1] == nullptr,
          65, "descriptor", "environment");
  rlimit limit{};
  require(::getrlimit(RLIMIT_NOFILE, &limit) == 0 && limit.rlim_cur != RLIM_INFINITY,
          65, "descriptor", "RLIMIT_NOFILE");
  const auto expected = expected_descriptors(mode);
  for (u64 fd = 0; fd < static_cast<u64>(limit.rlim_cur); ++fd) {
    errno = 0;
    const int flags = ::fcntl(static_cast<int>(fd), F_GETFD);
    const bool open = flags != -1 || errno != EBADF;
    require(open == (expected.count(static_cast<int>(fd)) != 0),
            65, "descriptor", "open descriptor set");
  }
  for (int fd : expected) {
    if (fd == 2) continue;
    struct stat st{};
    require(::fstat(fd, &st) == 0, 65, "descriptor", "fstat descriptor");
    const int access = ::fcntl(fd, F_GETFL) & O_ACCMODE;
    if (fd == 9) {
      require(S_ISDIR(st.st_mode) && access == O_RDONLY,
              65, "descriptor", "directory descriptor");
    } else if (fd == 10) {
      require(S_ISFIFO(st.st_mode) && access == O_WRONLY,
              65, "descriptor", "status descriptor");
    } else {
      require(S_ISREG(st.st_mode) && access == O_RDONLY,
              65, "descriptor", "input descriptor");
    }
  }
  DIR* directory = ::opendir(".");
  require(directory != nullptr, 65, "descriptor", "scratch cwd");
  int entries = 0;
  while (dirent* item = ::readdir(directory)) {
    const std::string name = item->d_name;
    if (name != "." && name != "..") ++entries;
  }
  const int close_result = ::closedir(directory);
  require(close_result == 0 && entries == 0, 65, "descriptor", "nonempty cwd");
}

void write_status_bytes(const std::string& bytes) {
  require(!bytes.empty() && bytes.back() == '\n' && bytes.size() <= MAX_STATUS_BYTES,
          70, "internal", "status serialization");
  std::size_t done = 0;
  while (done < bytes.size()) {
    const ssize_t written = ::write(10, bytes.data() + done, bytes.size() - done);
    if (written < 0 && errno == EINTR) continue;
    if (written <= 0) _exit(70);
    done += static_cast<std::size_t>(written);
  }
  if (::close(10) != 0) _exit(70);
}

std::string failure_status(Mode mode, int exit_code, const std::string& error) {
  std::ostringstream out;
  out << "{\"version\":\"" << VERSION << "\",\"role\":\"" << ROLE
      << "\",\"mode\":";
  if (mode == Mode::Invalid) out << "null";
  else out << json_string(mode_token(mode));
  out << ",\"phase\":" << phase_json(mode)
      << ",\"status\":\"fail\",\"exit_code\":" << exit_code
      << ",\"error_code\":" << json_string(error) << "}\n";
  return out.str();
}

u64 checked_add(u64 a, u64 b, int exit_code = 70,
                const std::string& error = "internal") {
  require(a <= std::numeric_limits<u64>::max() - b, exit_code, error,
          "unsigned addition overflow");
  return a + b;
}

u64 checked_mul(u64 a, u64 b, int exit_code = 68,
                const std::string& error = "memory_cap") {
  require(a == 0 || b <= std::numeric_limits<u64>::max() / a,
          exit_code, error, "unsigned multiplication overflow");
  return a * b;
}

std::string pad_decimal(unsigned value, unsigned width) {
  std::string result = std::to_string(value);
  require(result.size() <= width, 70, "internal", "fixed decimal width");
  return std::string(width - result.size(), '0') + result;
}

std::string signed_decimal(int value) {
  return std::to_string(value);
}

std::string tsv(const std::vector<std::string>& fields) {
  require(!fields.empty(), 66, "serialization", "empty TSV record");
  std::string result;
  for (std::size_t i = 0; i < fields.size(); ++i) {
    if (i != 0) result.push_back('\t');
    for (unsigned char c : fields[i])
      require(c >= 0x20 && c <= 0x7e && c != '\t' && c != '\r' && c != '\n',
              66, "serialization", "TSV field byte");
    result += fields[i];
  }
  result.push_back('\n');
  return result;
}

cpp_int canonical_mod(cpp_int value, const cpp_int& modulus) {
  value %= modulus;
  if (value < 0) value += modulus;
  return value;
}

cpp_int gcd_plain(cpp_int a, cpp_int b) {
  if (a < 0) a = -a;
  if (b < 0) b = -b;
  while (b != 0) {
    const cpp_int r = a % b;
    a = b;
    b = r;
  }
  return a;
}

struct OperationCounts {
  u64 pair_muls = 0;
  u64 mod_muls = 0;
  u64 gcds = 0;
  u64 inverses = 0;
  u64 matrix_muls = 0;
  u64 sha256_contexts = 0;
  u64 sha256_updates = 0;
  u64 sha256_bytes = 0;
  u64 tape_blocks = 0;
  u64 endpoint_checksum_records = 0;
  u64 control_checksum_records = 0;
  u64 diagnostic_scan_records = 0;

  void add(const OperationCounts& other) {
    pair_muls = checked_add(pair_muls, other.pair_muls);
    mod_muls = checked_add(mod_muls, other.mod_muls);
    gcds = checked_add(gcds, other.gcds);
    inverses = checked_add(inverses, other.inverses);
    matrix_muls = checked_add(matrix_muls, other.matrix_muls);
    sha256_contexts = checked_add(sha256_contexts, other.sha256_contexts);
    sha256_updates = checked_add(sha256_updates, other.sha256_updates);
    sha256_bytes = checked_add(sha256_bytes, other.sha256_bytes);
    tape_blocks = checked_add(tape_blocks, other.tape_blocks);
    endpoint_checksum_records = checked_add(endpoint_checksum_records,
                                            other.endpoint_checksum_records);
    control_checksum_records = checked_add(control_checksum_records,
                                           other.control_checksum_records);
    diagnostic_scan_records = checked_add(diagnostic_scan_records,
                                          other.diagnostic_scan_records);
  }
};

cpp_int gcd_owned(const cpp_int& a, const cpp_int& b, OperationCounts* counts) {
  if (counts != nullptr) counts->gcds = checked_add(counts->gcds, 1);
  return gcd_plain(a, b);
}

cpp_int mod_product(const cpp_int& a, const cpp_int& b, const cpp_int& n,
                    OperationCounts* counts) {
  if (counts != nullptr) counts->mod_muls = checked_add(counts->mod_muls, 1);
  return canonical_mod(a * b, n);
}

cpp_int inverse_owned(const cpp_int& input, const cpp_int& n,
                      OperationCounts* counts) {
  if (counts != nullptr) counts->inverses = checked_add(counts->inverses, 1);
  cpp_int old_r = n;
  cpp_int r = canonical_mod(input, n);
  cpp_int old_s = 0;
  cpp_int s = 1;
  while (r != 0) {
    const cpp_int q = old_r / r;
    cpp_int next_r = old_r - q * r;
    old_r = r;
    r = std::move(next_r);
    cpp_int next_s = old_s - q * s;
    old_s = s;
    s = std::move(next_s);
  }
  require(old_r == 1, 67, "arithmetic", "inverse of nonunit");
  return canonical_mod(old_s, n);
}

unsigned bit_length(const cpp_int& value) {
  require(value > 0, 67, "arithmetic", "bit length of nonpositive value");
  return static_cast<unsigned>(boost::multiprecision::msb(value)) + 1;
}

cpp_int integer_sqrt(const cpp_int& value) {
  require(value >= 0, 67, "arithmetic", "negative integer square root");
  if (value < 2) return value;
  cpp_int x = cpp_int(1) << ((bit_length(value) + 1) / 2);
  for (;;) {
    const cpp_int y = (x + value / x) >> 1;
    if (y >= x) return x;
    x = y;
  }
}

bool exact_square(const cpp_int& value, cpp_int* root) {
  if (value < 0) return false;
  const cpp_int y = integer_sqrt(value);
  if (y * y != value) return false;
  if (root != nullptr) *root = y;
  return true;
}

u64 low_u64(const cpp_int& value) {
  const cpp_int mask = (cpp_int(1) << 64) - 1;
  return canonical_mod(value, cpp_int(1) << 64).convert_to<u64>() &
         mask.convert_to<u64>();
}

struct Pair {
  cpp_int p;
  cpp_int q;
};

Pair pair_product(const Pair& a, const Pair& b, const cpp_int& eta,
                  const cpp_int& n, OperationCounts* counts) {
  if (counts != nullptr) counts->pair_muls = checked_add(counts->pair_muls, 1);
  const cpp_int pp = mod_product(a.p, b.p, n, counts);
  const cpp_int qq = mod_product(a.q, b.q, n, counts);
  const cpp_int eqq = mod_product(eta, qq, n, counts);
  const cpp_int pq = mod_product(a.p, b.q, n, counts);
  const cpp_int qp = mod_product(a.q, b.p, n, counts);
  return {canonical_mod(pp + eqq, n), canonical_mod(pq + qp, n)};
}

Pair pair_power(const cpp_int& t, const cpp_int& eta, cpp_int exponent,
                const cpp_int& n, OperationCounts* counts) {
  require(exponent >= 0, 67, "arithmetic", "negative pair exponent");
  Pair accumulator{1, 0};
  Pair base{canonical_mod(t, n), 1};
  while (exponent > 0) {
    if ((exponent & 1) != 0)
      accumulator = pair_product(accumulator, base, eta, n, counts);
    exponent >>= 1;
    if (exponent > 0) base = pair_product(base, base, eta, n, counts);
  }
  return accumulator;
}

u64 power_product_count(cpp_int exponent) {
  require(exponent >= 0, 67, "arithmetic", "negative power count");
  if (exponent == 0) return 0;
  u64 count = 0;
  while (exponent > 0) {
    if ((exponent & 1) != 0) ++count;
    exponent >>= 1;
    if (exponent > 0) ++count;
  }
  return count;
}

std::vector<Pair> pair_chain(const cpp_int& t, const cpp_int& eta,
                             const cpp_int& n, int maximum,
                             OperationCounts* counts) {
  std::vector<Pair> powers(static_cast<std::size_t>(maximum + 1));
  powers[0] = {1, 0};
  if (maximum >= 1) powers[1] = {canonical_mod(t, n), 1};
  const Pair generator{canonical_mod(t, n), 1};
  for (int e = 2; e <= maximum; ++e)
    powers[static_cast<std::size_t>(e)] = pair_product(
        powers[static_cast<std::size_t>(e - 1)], generator, eta, n, counts);
  return powers;
}

struct Matrix {
  std::array<cpp_int, 4> x;
};

Matrix matrix_product(const Matrix& a, const Matrix& b, const cpp_int& n,
                      OperationCounts* counts) {
  if (counts != nullptr)
    counts->matrix_muls = checked_add(counts->matrix_muls, 1);
  Matrix result;
  for (int row = 0; row < 2; ++row) {
    for (int column = 0; column < 2; ++column) {
      cpp_int sum = 0;
      for (int inner = 0; inner < 2; ++inner)
        sum += mod_product(a.x[2 * row + inner], b.x[2 * inner + column],
                           n, counts);
      result.x[2 * row + column] = canonical_mod(sum, n);
    }
  }
  return result;
}

Matrix matrix_power(Matrix base, cpp_int exponent, const cpp_int& n,
                    OperationCounts* counts) {
  Matrix accumulator{{1, 0, 0, 1}};
  while (exponent > 0) {
    if ((exponent & 1) != 0)
      accumulator = matrix_product(accumulator, base, n, counts);
    exponent >>= 1;
    if (exponent > 0) base = matrix_product(base, base, n, counts);
  }
  return accumulator;
}

cpp_int mod_power(cpp_int base, cpp_int exponent, const cpp_int& n,
                  OperationCounts* counts) {
  cpp_int accumulator = 1;
  base = canonical_mod(base, n);
  while (exponent > 0) {
    if ((exponent & 1) != 0)
      accumulator = mod_product(accumulator, base, n, counts);
    exponent >>= 1;
    if (exponent > 0) base = mod_product(base, base, n, counts);
  }
  return accumulator;
}

void literal_matrix_check(const cpp_int& n, const cpp_int& exponent,
                          const cpp_int& t, const cpp_int& eta,
                          const cpp_int& v, const cpp_int& f,
                          OperationCounts* counts) {
  const cpp_int inv2 = inverse_owned(2, n, counts);
  const cpp_int inv4 = mod_product(inv2, inv2, n, counts);
  const cpp_int v2 = canonical_mod(v * v, n);
  Matrix c{{mod_product(canonical_mod(t - v, n), inv2, n, counts), 1,
            mod_product(canonical_mod(eta - v2, n), inv4, n, counts),
            mod_product(canonical_mod(t + v, n), inv2, n, counts)}};
  const Matrix powered = matrix_power(c, exponent, n, counts);
  const cpp_int scale = mod_power(inv2, exponent, n, counts);
  const cpp_int right = mod_product(scale, f, n, counts);
  require(powered.x[0] == right, 67, "arithmetic", "literal matrix equality");
}

struct ManifestRow {
  std::string artifact;
  u64 bytes = 0;
  std::string hash;
};

std::vector<ManifestRow> parse_manifest(const std::string& bytes,
                                        const std::string& context,
                                        const std::vector<std::string>& names) {
  const auto lines = split_lines(bytes, context);
  require(lines.size() == names.size() + 1 &&
          lines[0] == "artifact\tbytes\tsha256", 65, "input_schema",
          context + ": header/count");
  std::vector<ManifestRow> rows;
  for (std::size_t i = 0; i < names.size(); ++i) {
    const auto fields = split_tabs(lines[i + 1]);
    require(fields.size() == 3 && fields[0] == names[i] &&
            lowercase_hash(fields[2]), 65, "input_schema",
            context + ": manifest row");
    if (i != 0)
      require(names[i - 1] < names[i], 65, "input_schema",
              context + ": manifest order");
    rows.push_back({fields[0], parse_u64(fields[1], context), fields[2]});
  }
  return rows;
}

const ManifestRow& manifest_find(const std::vector<ManifestRow>& rows,
                                 const std::string& name) {
  const auto found = std::find_if(rows.begin(), rows.end(),
      [&](const ManifestRow& row) { return row.artifact == name; });
  require(found != rows.end(), 65, "input_schema", "missing manifest row");
  return *found;
}

struct Promise {
  std::string phase;
  std::string public_name;
  u64 public_bytes = 0;
  std::string public_hash;
  std::string private_name;
  u64 private_bytes = 0;
  std::string private_hash;
  std::string tape_name;
  u64 tape_bytes = 0;
  std::string tape_hash;
  std::string provenance_hash;
  std::string validator_hash;
  std::string containment_hash;
};

Promise parse_promise(const std::string& bytes, const std::string& phase) {
  JsonCursor json(bytes, "promise");
  Promise promise;
  json.begin_object();
  json.key("version"); require(json.string_value() == VERSION, 65, "input_schema", "promise version");
  json.key("phase"); promise.phase = json.string_value();
  require(promise.phase == phase, 65, "input_schema", "promise phase");
  json.key("public_fixture_name"); promise.public_name = json.string_value();
  json.key("public_fixture_bytes"); promise.public_bytes = json.uint_value();
  json.key("public_fixture_sha256"); promise.public_hash = json.string_value();
  json.key("private_fixture_name"); promise.private_name = json.string_value();
  json.key("private_fixture_bytes"); promise.private_bytes = json.uint_value();
  json.key("private_fixture_sha256"); promise.private_hash = json.string_value();
  json.key("tape_name"); promise.tape_name = json.string_value();
  json.key("tape_bytes"); promise.tape_bytes = json.uint_value();
  json.key("tape_sha256"); promise.tape_hash = json.string_value();
  json.key("tape_provenance_sha256"); promise.provenance_hash = json.string_value();
  json.key("row_count"); require(json.uint_value() == ROWS_PER_PHASE, 65, "input_schema", "promise row count");
  json.key("promise_pass"); require(json.bool_value(), 65, "input_schema", "promise pass");
  json.key("validator_binary_sha256"); promise.validator_hash = json.string_value();
  json.key("containment_manifest_sha256"); promise.containment_hash = json.string_value();
  json.end_object(); json.finish();
  require(lowercase_hash(promise.public_hash) && lowercase_hash(promise.private_hash) &&
          lowercase_hash(promise.tape_hash) && lowercase_hash(promise.provenance_hash) &&
          lowercase_hash(promise.validator_hash) && lowercase_hash(promise.containment_hash),
          65, "input_schema", "promise hash");
  require(promise.public_name == std::string(VERSION) + "." + phase + ".public.tsv" &&
          promise.private_name == std::string(VERSION) + "." + phase + ".private.tsv" &&
          promise.tape_name == std::string(VERSION) + "." + phase + ".tape.bin" &&
          promise.tape_bytes == TAPE_BYTES, 65, "input_schema", "promise basename/size");
  return promise;
}

struct Containment {
  std::string fixture_binary_hash;
  std::string public_binary_hash;
  std::string runner_binary_hash;
  u64 runner_uid = 0;
  u64 public_uid = 0;
  u64 label_uid = 0;
  std::string deployment_hash;
};

Containment parse_containment(const std::string& bytes) {
  JsonCursor json(bytes, "containment");
  Containment result;
  json.begin_object();
  json.key("version"); require(json.string_value() == VERSION, 65, "input_schema", "containment version");
  json.key("fixture_label_binary_sha256"); result.fixture_binary_hash = json.string_value();
  json.key("public_binary_sha256"); result.public_binary_hash = json.string_value();
  json.key("runner_binary_sha256"); result.runner_binary_hash = json.string_value();
  json.key("runner_uid"); result.runner_uid = json.uint_value();
  json.key("public_uid"); result.public_uid = json.uint_value();
  json.key("label_uid"); result.label_uid = json.uint_value();
  json.key("public_fixture_fd"); require(json.uint_value() == 3, 65, "input_schema", "containment fd3");
  json.key("tape_fd"); require(json.uint_value() == 4, 65, "input_schema", "containment fd4");
  json.key("promise_fd"); require(json.uint_value() == 5, 65, "input_schema", "containment fd5");
  json.key("inputs_manifest_fd"); require(json.uint_value() == 6, 65, "input_schema", "containment fd6");
  json.key("containment_manifest_fd"); require(json.uint_value() == 7, 65, "input_schema", "containment fd7");
  json.key("selection_fd"); require(json.uint_value() == 8, 65, "input_schema", "containment fd8");
  json.key("output_dir_fd"); require(json.uint_value() == 9, 65, "input_schema", "containment fd9");
  json.key("status_fd"); require(json.uint_value() == 10, 65, "input_schema", "containment fd10");
  json.key("discovery_public_manifest_fd"); require(json.uint_value() == 11, 65, "input_schema", "containment fd11");
  json.key("discovery_summary_fd"); require(json.uint_value() == 12, 65, "input_schema", "containment fd12");
  json.key("deployment_contract_sha256"); result.deployment_hash = json.string_value();
  json.end_object(); json.finish();
  require(lowercase_hash(result.fixture_binary_hash) && lowercase_hash(result.public_binary_hash) &&
          lowercase_hash(result.runner_binary_hash) && lowercase_hash(result.deployment_hash),
          65, "input_schema", "containment hash");
  require(result.runner_uid != result.public_uid && result.runner_uid != result.label_uid &&
          result.public_uid != result.label_uid &&
          result.public_uid == static_cast<u64>(::getuid()) &&
          result.public_uid == static_cast<u64>(::geteuid()),
          65, "descriptor", "public identity");
  return result;
}

u64 descriptor_size(int fd, const std::string& context) {
  struct stat st{};
  require(::fstat(fd, &st) == 0, 65, "input_io", context + ": fstat");
  require(S_ISREG(st.st_mode) && st.st_size >= 0, 65, "descriptor",
          context + ": regular input");
  return static_cast<u64>(st.st_size);
}

const std::vector<std::string>& input_manifest_names() {
  static const std::vector<std::string> names = {
    "F279-D06.containment.json",
    "F279-D06.discovery.private.tsv",
    "F279-D06.discovery.promise.json",
    "F279-D06.discovery.public.tsv",
    "F279-D06.discovery.tape.bin",
    "F279-D06.heldout.private.tsv",
    "F279-D06.heldout.promise.json",
    "F279-D06.heldout.public.tsv",
    "F279-D06.heldout.tape.bin",
    "F279-D06.heldout_seed.commitment.json",
    "F279-D06.tape.provenance.json"
  };
  return names;
}

constexpr std::array<int, 9> ANCHORS{{-4,-3,-2,-1,0,1,2,3,4}};

std::string source_id(int anchor_index, int trace_index, int eta_index) {
  return "s" + std::to_string(anchor_index) + "-t" +
         pad_decimal(static_cast<unsigned>(trace_index), 2) + "-e" +
         pad_decimal(static_cast<unsigned>(eta_index), 2);
}

std::string target_id(int anchor_index, int value_index) {
  return "d" + std::to_string(anchor_index) + "-v" +
         pad_decimal(static_cast<unsigned>(value_index), 2);
}

std::string candidate_id(int source_anchor, int trace_index, int eta_index,
                         int target_anchor, int value_index) {
  return source_id(source_anchor, trace_index, eta_index) + "-" +
         target_id(target_anchor, value_index);
}

struct SourceSpec {
  int anchor = 0;
  int trace = 0;
  int eta = 0;
  int ordinal = 0;
  std::string id;
};

struct CandidateSpec {
  int source_anchor = 0;
  int trace = 0;
  int eta = 0;
  int target_anchor = 0;
  int value = 0;
  int source_ordinal = 0;
  int ordinal = 0;
  std::string id;
};

struct Grammar {
  std::vector<SourceSpec> sources;
  std::vector<CandidateSpec> candidates;
  std::array<std::vector<int>, SOURCES> candidates_by_source;
  std::map<std::string, int> candidate_by_id;
};

Grammar make_grammar() {
  Grammar grammar;
  grammar.sources.reserve(SOURCES);
  grammar.candidates.reserve(CANDIDATES);
  for (int i = 0; i < 9; ++i) {
    for (int tt = 0; tt < 10; ++tt) {
      for (int ee = 0; ee < 10; ++ee) {
        const int source_ordinal = 100 * i + 10 * tt + ee;
        grammar.sources.push_back({i, tt, ee, source_ordinal,
                                   source_id(i, tt, ee)});
        for (int j = std::max(0, i - 1); j <= std::min(8, i + 1); ++j) {
          for (int vv = 0; vv < 10; ++vv) {
            const int ordinal = static_cast<int>(grammar.candidates.size());
            CandidateSpec candidate{i,tt,ee,j,vv,source_ordinal,ordinal,
                                    candidate_id(i,tt,ee,j,vv)};
            grammar.candidate_by_id.emplace(candidate.id, ordinal);
            grammar.candidates_by_source[static_cast<std::size_t>(source_ordinal)]
                .push_back(ordinal);
            grammar.candidates.push_back(std::move(candidate));
          }
        }
      }
    }
  }
  require(grammar.sources.size() == SOURCES &&
          grammar.candidates.size() == CANDIDATES &&
          grammar.candidate_by_id.size() == CANDIDATES,
          70, "internal", "grammar counts");
  return grammar;
}

struct SelectionEntry {
  unsigned rank = 0;
  int candidate = -1;
  u64 unexplained = 0;
  u64 scales = 0;
  u64 minimum = 0;
  u64 proper = 0;
};

std::vector<SelectionEntry> parse_selection(const std::string& bytes,
                                            const Grammar& grammar) {
  const auto lines = split_lines(bytes, "selection");
  require(lines.size() == 129 &&
          lines[0] == "rank\tcandidate_id\tbox_unexplained_rows\tscale_count\tmin_scale_count\tproper_endpoint_rows",
          65, "input_schema", "selection header/count");
  std::vector<SelectionEntry> entries;
  std::set<int> seen;
  for (unsigned rank = 1; rank <= 128; ++rank) {
    const auto fields = split_tabs(lines[rank]);
    require(fields.size() == 6 && parse_u64(fields[0], "selection rank") == rank,
            65, "input_schema", "selection record");
    const auto found = grammar.candidate_by_id.find(fields[1]);
    require(found != grammar.candidate_by_id.end() && seen.insert(found->second).second,
            65, "input_schema", "selection candidate");
    SelectionEntry entry{rank, found->second,
      parse_u64(fields[2], "selection unexplained"),
      parse_u64(fields[3], "selection scales"),
      parse_u64(fields[4], "selection minimum"),
      parse_u64(fields[5], "selection proper")};
    require(entry.unexplained <= ROWS_PER_PHASE && entry.scales <= 4 &&
            entry.minimum <= ROWS_PER_PHASE / 4 && entry.proper <= ROWS_PER_PHASE,
            65, "input_schema", "selection range");
    if (!entries.empty()) {
      const SelectionEntry& prior = entries.back();
      const auto prior_key = std::make_tuple(
          std::numeric_limits<u64>::max() - prior.unexplained,
          std::numeric_limits<u64>::max() - prior.scales,
          std::numeric_limits<u64>::max() - prior.minimum,
          std::numeric_limits<u64>::max() - prior.proper, prior.candidate);
      const auto key = std::make_tuple(
          std::numeric_limits<u64>::max() - entry.unexplained,
          std::numeric_limits<u64>::max() - entry.scales,
          std::numeric_limits<u64>::max() - entry.minimum,
          std::numeric_limits<u64>::max() - entry.proper, entry.candidate);
      require(prior_key < key, 65, "input_schema", "selection order");
    }
    entries.push_back(entry);
  }
  return entries;
}

struct FixtureRow {
  std::string id;
  cpp_int n;
  cpp_int b;
  unsigned b_pub = 0;
  bool diagnostic = false;
  int ordinal = 0;
};

std::vector<FixtureRow> parse_public_fixture(const std::string& bytes,
                                             const std::string& phase) {
  const auto lines = split_lines(bytes, "public fixture");
  require(lines.size() == ROWS_PER_PHASE + 1 &&
          lines[0] == "row_id\tN\tdiagnostic", 65, "input_schema",
          "public fixture header/count");
  const std::array<unsigned,4> discovery_sizes{{18,24,30,36}};
  const std::array<unsigned,4> heldout_sizes{{40,46,52,56}};
  const auto& sizes = phase == "discovery" ? discovery_sizes : heldout_sizes;
  const char prefix = phase == "discovery" ? 'd' : 'h';
  std::set<cpp_int> seen;
  std::vector<FixtureRow> rows;
  rows.reserve(ROWS_PER_PHASE);
  for (int ordinal = 0; ordinal < ROWS_PER_PHASE; ++ordinal) {
    const auto fields = split_tabs(lines[static_cast<std::size_t>(ordinal + 1)]);
    const std::string id = std::string(1, prefix) +
                           pad_decimal(static_cast<unsigned>(ordinal), 4);
    require(fields.size() == 3 && fields[0] == id &&
            (fields[2] == "0" || fields[2] == "1"),
            65, "input_schema", "public fixture row");
    cpp_int n = parse_cpp_uint(fields[1], "public N");
    require(n > 1 && (n & 1) != 0 && seen.insert(n).second,
            65, "input_schema", "public N conditions");
    const cpp_int b = integer_sqrt(n);
    require(b * b <= n && n < (b + 1) * (b + 1),
            67, "arithmetic", "public square root");
    const unsigned b_pub = (bit_length(n) + 1) / 2;
    require(b_pub == sizes[static_cast<std::size_t>(ordinal / 256)],
            65, "input_schema", "public scale order");
    const bool expected_diagnostic = ordinal % 256 < 4;
    require((fields[2] == "1") == expected_diagnostic,
            65, "input_schema", "diagnostic flag");
    rows.push_back({id,n,b,b_pub,expected_diagnostic,ordinal});
  }
  return rows;
}

struct AuthenticatedInputs {
  std::string phase;
  std::string containment_hash;
  std::string inputs_hash;
  std::string promise_hash;
  std::string fixture_hash;
  std::string tape_hash;
  std::string selection_hash;
  Promise promise;
  Containment containment;
  std::vector<ManifestRow> input_manifest;
  std::vector<SelectionEntry> selection;
  std::vector<FixtureRow> rows;
};

AuthenticatedInputs authenticate_inputs(const Cli& cli, const Grammar& grammar) {
  AuthenticatedInputs result;
  result.phase = phase_token(cli.mode);
  const u64 containment_bytes = descriptor_size(7, "containment");
  result.containment_hash = hash_fd(7, containment_bytes, "containment");
  require(result.containment_hash == cli.trusted_containment, 65, "input_auth",
          "containment trust anchor");
  const u64 inputs_bytes = descriptor_size(6, "inputs manifest");
  result.inputs_hash = hash_fd(6, inputs_bytes, "inputs manifest");
  require(result.inputs_hash == cli.trusted_inputs, 65, "input_auth",
          "inputs trust anchor");

  const std::string containment_text = read_fd_all(7, MAX_JSON_BYTES, "containment");
  result.containment = parse_containment(containment_text);
  const std::string manifest_text = read_fd_all(6, MAX_JSON_BYTES, "inputs manifest");
  result.input_manifest = parse_manifest(manifest_text, "inputs manifest",
                                         input_manifest_names());
  const ManifestRow& containment_row = manifest_find(result.input_manifest,
                                                       std::string(VERSION) + ".containment.json");
  require(containment_row.bytes == containment_bytes &&
          containment_row.hash == result.containment_hash,
          65, "input_auth", "containment manifest row");

  const std::string promise_name = std::string(VERSION) + "." + result.phase +
                                   ".promise.json";
  const ManifestRow& promise_row = manifest_find(result.input_manifest, promise_name);
  require(descriptor_size(5, "promise") == promise_row.bytes, 65, "input_auth",
          "promise bytes");
  result.promise_hash = hash_fd(5, promise_row.bytes, "promise");
  require(result.promise_hash == promise_row.hash, 65, "input_auth", "promise hash");
  const std::string promise_text = read_fd_all(5, 4096, "promise");
  result.promise = parse_promise(promise_text, result.phase);
  require(result.promise.containment_hash == result.containment_hash &&
          result.promise.validator_hash == result.containment.fixture_binary_hash,
          65, "input_auth", "promise trust bindings");

  const ManifestRow& public_row = manifest_find(result.input_manifest,
                                                 result.promise.public_name);
  require(public_row.bytes == result.promise.public_bytes &&
          public_row.hash == result.promise.public_hash &&
          descriptor_size(3, "public fixture") == public_row.bytes,
          65, "input_auth", "public fixture manifest");
  result.fixture_hash = hash_fd(3, public_row.bytes, "public fixture");
  require(result.fixture_hash == public_row.hash, 65, "input_auth", "public fixture hash");

  const ManifestRow& private_row = manifest_find(result.input_manifest,
                                                  result.promise.private_name);
  require(private_row.bytes == result.promise.private_bytes &&
          private_row.hash == result.promise.private_hash,
          65, "input_auth", "opaque private fixture commitment");
  const ManifestRow& tape_row = manifest_find(result.input_manifest,
                                               result.promise.tape_name);
  require(tape_row.bytes == TAPE_BYTES && tape_row.bytes == result.promise.tape_bytes &&
          tape_row.hash == result.promise.tape_hash &&
          descriptor_size(4, "tape") == TAPE_BYTES,
          65, "input_auth", "tape manifest");
  result.tape_hash = hash_fd(4, TAPE_BYTES, "tape");
  require(result.tape_hash == tape_row.hash, 65, "input_auth", "tape hash");
  const ManifestRow& provenance_row = manifest_find(
      result.input_manifest, std::string(VERSION) + ".tape.provenance.json");
  require(provenance_row.hash == result.promise.provenance_hash,
          65, "input_auth", "tape provenance commitment");

  result.rows = parse_public_fixture(
      read_fd_all(3, result.promise.public_bytes, "public fixture"), result.phase);
  if (cli.mode != Mode::Discovery) {
    const u64 selection_bytes = descriptor_size(8, "selection");
    result.selection_hash = hash_fd(8, selection_bytes, "selection");
    require(result.selection_hash == cli.trusted_selection, 65, "input_auth",
            "selection trust anchor");
    result.selection = parse_selection(read_fd_all(8, 1048576, "selection"), grammar);
  }
  return result;
}

struct PhaseSummary {
  std::string phase;
  std::string promise_hash;
  std::string inputs_hash;
  std::string containment_hash;
  std::string fixture_hash;
  std::string tape_hash;
  std::string selection_hash;
  u64 row_count = 0;
  u64 cleanup_rows = 0;
  u64 eligible_rows = 0;
  u64 source_slots = 0;
  u64 candidate_slots = 0;
  u64 raw_hits = 0;
  u64 unexplained_hits = 0;
  u64 global_checks = 0;
  u64 carry_raw = 0;
  u64 carry_global = 0;
  u64 packet_raw = 0;
  u64 packet_global = 0;
  OperationCounts operations;
  u64 output_bytes = 0;
  std::string rows_hash;
  std::string scores_hash;
  std::string certificates_hash;
  std::string controls_hash;
  std::string diagnostic_hash;
  std::string endpoint_checksum;
};

PhaseSummary parse_summary(const std::string& bytes,
                           const std::string& expected_phase) {
  JsonCursor json(bytes, "phase summary");
  PhaseSummary summary;
  json.begin_object();
  json.key("version"); require(json.string_value() == VERSION, 65, "input_schema", "summary version");
  json.key("phase"); summary.phase = json.string_value();
  require(summary.phase == expected_phase, 65, "input_schema", "summary phase");
  json.key("promise_sha256"); summary.promise_hash = json.string_value();
  json.key("inputs_manifest_sha256"); summary.inputs_hash = json.string_value();
  json.key("containment_manifest_sha256"); summary.containment_hash = json.string_value();
  json.key("public_fixture_sha256"); summary.fixture_hash = json.string_value();
  json.key("tape_sha256"); summary.tape_hash = json.string_value();
  json.key("selection_sha256"); summary.selection_hash = json.string_value();
  json.key("row_count"); summary.row_count = json.uint_value();
  json.key("cleanup_rows"); summary.cleanup_rows = json.uint_value();
  json.key("eligible_rows"); summary.eligible_rows = json.uint_value();
  json.key("source_slots"); summary.source_slots = json.uint_value();
  json.key("candidate_slots"); summary.candidate_slots = json.uint_value();
  json.key("raw_hits"); summary.raw_hits = json.uint_value();
  json.key("box_unexplained_hits"); summary.unexplained_hits = json.uint_value();
  json.key("global_order_checks"); summary.global_checks = json.uint_value();
  json.key("carry_raw_hits"); summary.carry_raw = json.uint_value();
  json.key("carry_global_order_checks"); summary.carry_global = json.uint_value();
  json.key("packet_raw_hits"); summary.packet_raw = json.uint_value();
  json.key("packet_global_order_checks"); summary.packet_global = json.uint_value();
  json.key("operation_counts"); json.begin_nested_object();
  json.key("pair_muls"); summary.operations.pair_muls = json.uint_value();
  json.key("mod_muls"); summary.operations.mod_muls = json.uint_value();
  json.key("gcds"); summary.operations.gcds = json.uint_value();
  json.key("inverses"); summary.operations.inverses = json.uint_value();
  json.key("matrix_muls"); summary.operations.matrix_muls = json.uint_value();
  json.key("sha256_contexts"); summary.operations.sha256_contexts = json.uint_value();
  json.key("sha256_updates"); summary.operations.sha256_updates = json.uint_value();
  json.key("sha256_bytes"); summary.operations.sha256_bytes = json.uint_value();
  json.key("tape_blocks"); summary.operations.tape_blocks = json.uint_value();
  json.key("endpoint_checksum_records"); summary.operations.endpoint_checksum_records = json.uint_value();
  json.key("control_checksum_records"); summary.operations.control_checksum_records = json.uint_value();
  json.key("diagnostic_scan_records"); summary.operations.diagnostic_scan_records = json.uint_value();
  json.end_nested_object();
  json.key("output_bytes"); summary.output_bytes = json.uint_value();
  json.key("rows_sha256"); summary.rows_hash = json.string_value();
  json.key("scores_sha256"); summary.scores_hash = json.string_value();
  json.key("certificates_sha256"); summary.certificates_hash = json.string_value();
  json.key("controls_sha256"); summary.controls_hash = json.string_value();
  json.key("diagnostic_sha256"); summary.diagnostic_hash = json.string_value();
  json.key("endpoint_checksum"); summary.endpoint_checksum = json.string_value();
  json.end_object(); json.finish();
  const std::array<std::string,12> hashes{{summary.promise_hash,summary.inputs_hash,
      summary.containment_hash,summary.fixture_hash,summary.tape_hash,
      summary.selection_hash,summary.rows_hash,summary.scores_hash,
      summary.certificates_hash,summary.controls_hash,summary.diagnostic_hash,
      summary.endpoint_checksum}};
  for (const std::string& hash : hashes)
    require(lowercase_hash(hash), 65, "input_schema", "summary hash");
  require(summary.row_count == ROWS_PER_PHASE &&
          summary.source_slots == static_cast<u64>(ROWS_PER_PHASE) * SOURCES &&
          summary.candidate_slots == static_cast<u64>(ROWS_PER_PHASE) * CANDIDATES &&
          summary.cleanup_rows + summary.eligible_rows == ROWS_PER_PHASE &&
          summary.unexplained_hits <= summary.raw_hits,
          65, "input_schema", "summary counts");
  require(summary.packet_raw == checked_add(summary.carry_raw, summary.raw_hits,
                                             65, "input_schema") &&
          summary.packet_global == checked_add(summary.carry_global,
                                                summary.global_checks,
                                                65, "input_schema") &&
          summary.packet_raw <= MAX_RAW_HITS_TOTAL &&
          summary.packet_global <= MAX_GLOBAL_ORDER_CHECKS_TOTAL,
          65, "input_schema", "summary packet counters");
  return summary;
}

const std::vector<std::string>& discovery_manifest_names() {
  static const std::vector<std::string> names = {
    "F279-D06.discovery.certificates.tsv",
    "F279-D06.discovery.controls.json",
    "F279-D06.discovery.diagnostic.tsv",
    "F279-D06.discovery.rows.tsv",
    "F279-D06.discovery.scores.tsv",
    "F279-D06.discovery.selection.tsv",
    "F279-D06.discovery.summary.json"
  };
  return names;
}

const std::vector<std::string>& heldout_manifest_names() {
  static const std::vector<std::string> names = {
    "F279-D06.heldout.certificates.tsv",
    "F279-D06.heldout.controls.json",
    "F279-D06.heldout.diagnostic.tsv",
    "F279-D06.heldout.rows.tsv",
    "F279-D06.heldout.scores.tsv",
    "F279-D06.heldout.summary.json"
  };
  return names;
}

struct Carry {
  u64 raw = 0;
  u64 global = 0;
  u64 output_bytes = 0;
  std::string manifest_hash;
  PhaseSummary summary;
  std::vector<ManifestRow> manifest;
};

Carry authenticate_carry(const Cli& cli, const AuthenticatedInputs& inputs) {
  Carry carry;
  if (cli.mode != Mode::Heldout && cli.mode != Mode::ReplayHeldout) return carry;
  const u64 manifest_bytes = descriptor_size(11, "discovery public manifest");
  carry.manifest_hash = hash_fd(11, manifest_bytes, "discovery public manifest");
  require(carry.manifest_hash == cli.trusted_discovery_manifest,
          65, "input_auth", "discovery manifest trust anchor");
  carry.manifest = parse_manifest(
      read_fd_all(11, MAX_JSON_BYTES, "discovery public manifest"),
      "discovery public manifest", discovery_manifest_names());
  const ManifestRow& summary_row = manifest_find(
      carry.manifest, std::string(VERSION) + ".discovery.summary.json");
  require(descriptor_size(12, "discovery summary") == summary_row.bytes,
          65, "input_auth", "discovery summary bytes");
  const std::string summary_hash = hash_fd(12, summary_row.bytes,
                                           "discovery summary");
  require(summary_hash == summary_row.hash, 65, "input_auth",
          "discovery summary hash");
  carry.summary = parse_summary(read_fd_all(12, MAX_JSON_BYTES,
                                            "discovery summary"), "discovery");
  const auto& in = inputs.input_manifest;
  require(carry.summary.promise_hash == manifest_find(
              in, std::string(VERSION) + ".discovery.promise.json").hash &&
          carry.summary.inputs_hash == inputs.inputs_hash &&
          carry.summary.containment_hash == inputs.containment_hash &&
          carry.summary.fixture_hash == manifest_find(
              in, std::string(VERSION) + ".discovery.public.tsv").hash &&
          carry.summary.tape_hash == manifest_find(
              in, std::string(VERSION) + ".discovery.tape.bin").hash &&
          carry.summary.selection_hash == inputs.selection_hash,
          65, "input_schema", "discovery summary bindings");
  require(carry.summary.carry_raw == 0 && carry.summary.carry_global == 0 &&
          carry.summary.packet_raw == carry.summary.raw_hits &&
          carry.summary.packet_global == carry.summary.global_checks,
          65, "input_schema", "discovery carry identities");
  require(manifest_find(carry.manifest, std::string(VERSION) + ".discovery.rows.tsv").hash == carry.summary.rows_hash &&
          manifest_find(carry.manifest, std::string(VERSION) + ".discovery.scores.tsv").hash == carry.summary.scores_hash &&
          manifest_find(carry.manifest, std::string(VERSION) + ".discovery.certificates.tsv").hash == carry.summary.certificates_hash &&
          manifest_find(carry.manifest, std::string(VERSION) + ".discovery.controls.json").hash == carry.summary.controls_hash &&
          manifest_find(carry.manifest, std::string(VERSION) + ".discovery.diagnostic.tsv").hash == carry.summary.diagnostic_hash &&
          manifest_find(carry.manifest, std::string(VERSION) + ".discovery.selection.tsv").hash == carry.summary.selection_hash,
          65, "input_schema", "discovery manifest summary hashes");
  u64 preceding = 0;
  for (const ManifestRow& row : carry.manifest)
    if (row.artifact != std::string(VERSION) + ".discovery.summary.json")
      preceding = checked_add(preceding, row.bytes, 65, "input_schema");
  require(preceding == carry.summary.output_bytes, 65, "input_schema",
          "discovery summary output bytes");
  carry.raw = carry.summary.packet_raw;
  carry.global = carry.summary.packet_global;
  carry.output_bytes = manifest_bytes;
  for (const ManifestRow& row : carry.manifest)
    carry.output_bytes = checked_add(carry.output_bytes, row.bytes, 65,
                                     "input_schema");
  require(carry.output_bytes <= HARD_OUTPUT_CAP, 65, "input_schema",
          "discovery output carry");
  return carry;
}

class OutputBudget {
 public:
  explicit OutputBudget(u64 initial) : total_(initial) {
    rlimit limit{};
    require(::getrlimit(RLIMIT_FSIZE, &limit) == 0, 66, "output_io",
            "RLIMIT_FSIZE");
    per_file_ = limit.rlim_cur == RLIM_INFINITY
        ? HARD_OUTPUT_CAP : static_cast<u64>(limit.rlim_cur);
  }
  void extend(u64 file_before, u64 amount) {
    const u64 file_after = checked_add(file_before, amount, 66, "output_cap");
    const u64 total_after = checked_add(total_, amount, 66, "output_cap");
    require(file_after <= per_file_ && total_after <= HARD_OUTPUT_CAP,
            66, "output_cap", "output byte cap");
    total_ = total_after;
  }
  u64 total() const { return total_; }
 private:
  u64 total_ = 0;
  u64 per_file_ = 0;
};

void require_output_absent(const std::vector<std::string>& names) {
  for (const std::string& name : names) {
    struct stat st{};
    errno = 0;
    const int result = ::fstatat(9, name.c_str(), &st, AT_SYMLINK_NOFOLLOW);
    if (result == 0) fail(66, "output_exists", "output basename exists");
    require(errno == ENOENT, 66, "output_io", "output preflight stat");
  }
}

class OutputFile {
 public:
  OutputFile(std::string name, OutputBudget* budget)
      : name_(std::move(name)), budget_(budget) {
    fd_ = ::openat(9, name_.c_str(), O_CREAT | O_EXCL | O_WRONLY | O_NOFOLLOW,
                   0600);
    if (fd_ < 0 && errno == EEXIST) fail(66, "output_exists", "exclusive output");
    require(fd_ >= 0, 66, "output_io", "open output");
  }
  OutputFile(const OutputFile&) = delete;
  OutputFile& operator=(const OutputFile&) = delete;
  ~OutputFile() { if (fd_ >= 0) ::close(fd_); }

  void append(const std::string& bytes, u64 record_cap = 0) {
    require(!bytes.empty() && bytes.back() == '\n', 66, "serialization",
            "output record LF");
    if (record_cap != 0)
      require(bytes.size() <= record_cap, 66, "serialization",
              "output record cap");
    budget_->extend(bytes_, static_cast<u64>(bytes.size()));
    std::size_t done = 0;
    while (done < bytes.size()) {
      const ssize_t wrote = ::write(fd_, bytes.data() + done, bytes.size() - done);
      if (wrote < 0 && errno == EINTR) continue;
      require(wrote > 0, 66, "output_io", "write output");
      done += static_cast<std::size_t>(wrote);
    }
    bytes_ += static_cast<u64>(bytes.size());
  }

  std::string close_and_hash(OperationCounts* counts) {
    require(fd_ >= 0 && ::fsync(fd_) == 0, 66, "output_io", "fsync output");
    require(::close(fd_) == 0, 66, "output_io", "close output");
    fd_ = -1;
    const int read_fd = ::openat(9, name_.c_str(), O_RDONLY | O_NOFOLLOW);
    require(read_fd >= 0, 66, "output_io", "reopen output");
    const std::string digest = hash_fd(read_fd, bytes_, "closed output");
    require(::close(read_fd) == 0, 66, "output_io", "close hashed output");
    if (counts != nullptr) {
      counts->sha256_contexts = checked_add(counts->sha256_contexts, 1);
      const u64 updates = (bytes_ + 1048575) / 1048576;
      counts->sha256_updates = checked_add(counts->sha256_updates, updates);
      counts->sha256_bytes = checked_add(counts->sha256_bytes, bytes_);
    }
    return digest;
  }

  u64 bytes() const { return bytes_; }
  const std::string& name() const { return name_; }

 private:
  std::string name_;
  OutputBudget* budget_ = nullptr;
  int fd_ = -1;
  u64 bytes_ = 0;
};

struct AtomBank {
  std::array<cpp_int,5> atom;
};

struct Cleanup {
  bool clean = true;
  std::string code = "-";
  cpp_int factor = 0;
  std::array<AtomBank,9> banks;
};

Cleanup clean_row(const FixtureRow& row, OperationCounts* counts) {
  Cleanup result;
  cpp_int g = gcd_owned(row.b, row.n, counts);
  if (g > 1 && g < row.n)
    return {false,"boundary_cleanup",g,{}};
  for (int j = -64; j <= 64; ++j) {
    const cpp_int value = row.b + j;
    if (value <= 0 || value >= row.n) continue;
    g = gcd_owned(value, row.n, counts);
    if (g > 1 && g < row.n)
      return {false,"offset_cleanup",g,{}};
  }
  for (int j = 0; j <= 64; ++j) {
    const cpp_int x = row.b + 1 + j;
    const cpp_int difference = x * x - row.n;
    cpp_int y;
    if (exact_square(difference, &y)) {
      const cpp_int left = x - y;
      const cpp_int right = x + y;
      require(left > 1 && right > 1 && left * right == row.n,
              67, "arithmetic", "Fermat factor verification");
      return {false,"fermat_cleanup",left,{}};
    }
  }
  for (int i = 0; i < 9; ++i) {
    const cpp_int x = row.b + ANCHORS[static_cast<std::size_t>(i)];
    require(x > 0, 67, "arithmetic", "positive anchor");
    g = gcd_owned(x, row.n, counts);
    if (g > 1 && g < row.n) return {false,"atom_cleanup",g,{}};
    if (g == row.n) return {false,"atom_saturated",g,{}};
    const cpp_int d = row.n / x;
    const cpp_int r = row.n - x * d;
    const cpp_int u = inverse_owned(x, row.n, counts);
    require(x * u >= 1 && (x * u - 1) % row.n == 0,
            67, "arithmetic", "inverse quotient exactness");
    const cpp_int k = (x * u - 1) / row.n;
    result.banks[static_cast<std::size_t>(i)].atom = {{x,d,r,u,k}};
    for (const cpp_int& atom : result.banks[static_cast<std::size_t>(i)].atom) {
      if (atom == 0) continue;
      g = gcd_owned(atom, row.n, counts);
      if (g > 1 && g < row.n) return {false,"atom_cleanup",g,{}};
      if (g == row.n) return {false,"atom_saturated",g,{}};
    }
  }
  return result;
}

cpp_int expression_value(const AtomBank& bank, int expression,
                         const cpp_int& n) {
  require(expression >= 0 && expression < 10, 70, "internal",
          "expression ordinal");
  cpp_int value = bank.atom[static_cast<std::size_t>(expression / 2)];
  if ((expression & 1) != 0) value = -value;
  return canonical_mod(value, n);
}

std::string mask_hex(const std::array<unsigned char,70>& mask) {
  require((mask[69] & 1U) == 0, 70, "internal", "mask padding");
  std::ostringstream out;
  out << std::hex << std::setfill('0');
  for (unsigned char byte : mask) out << std::setw(2) << unsigned(byte);
  const std::string result = out.str();
  require(result.size() == 140, 70, "internal", "mask width");
  return result;
}

void set_mask(std::array<unsigned char,70>* mask, int bit) {
  require(bit >= 0 && bit < 559, 70, "internal", "mask bit");
  (*mask)[static_cast<std::size_t>(bit / 8)] |=
      static_cast<unsigned char>(0x80U >> (bit % 8));
}

std::string signed_event(int e) {
  if (e == 0) return "00";
  return std::string(e < 0 ? "-" : "+") +
         pad_decimal(static_cast<unsigned>(e < 0 ? -e : e), 2);
}

std::string source_order_event(int m) {
  return "so" + pad_decimal(static_cast<unsigned>(m), 2);
}

std::string orbit_event(int e) { return "or" + signed_event(e); }
std::string target_torsion_event(int m) {
  return "tt" + pad_decimal(static_cast<unsigned>(m), 2);
}
std::string mixed_event(int e, int m) {
  return "mx" + signed_event(e) + "-" +
         pad_decimal(static_cast<unsigned>(m), 2);
}

struct PacketCounters {
  std::atomic<u64> raw;
  std::atomic<u64> global;
  std::atomic<u64> phase_raw{0};
  std::atomic<u64> phase_global{0};
  explicit PacketCounters(const Carry& carry) : raw(carry.raw), global(carry.global) {}
};

void reserve_packet_counter(std::atomic<u64>* packet,
                            std::atomic<u64>* phase, u64 limit,
                            const std::string& error) {
  u64 value = packet->load(std::memory_order_relaxed);
  for (;;) {
    require(value < limit, 68, error, "packet counter cap");
    if (packet->compare_exchange_weak(value, value + 1,
                                      std::memory_order_relaxed,
                                      std::memory_order_relaxed)) break;
  }
  phase->fetch_add(1, std::memory_order_relaxed);
}

struct SourceEvaluation {
  std::string status = "endpoint_eligible";
  std::string classification = "-";
  std::string event = "-";
  cpp_int t;
  cpp_int eta;
  cpp_int delta4;
  cpp_int g_eta;
  cpp_int g_delta;
  cpp_int p_b;
  cpp_int q_b;
  cpp_int g_p;
  cpp_int g_q;
  std::vector<Pair> small;
  mutable std::optional<std::vector<Pair>> full;
  std::array<unsigned char,70> mask{};
};

SourceEvaluation evaluate_source(const FixtureRow& row, const Cleanup& cleanup,
                                 const SourceSpec& spec,
                                 OperationCounts* counts) {
  SourceEvaluation source;
  source.t = expression_value(cleanup.banks[spec.anchor], spec.trace, row.n);
  source.eta = expression_value(cleanup.banks[spec.anchor], spec.eta, row.n);
  source.g_eta = gcd_owned(source.eta, row.n, counts);
  if (source.g_eta > 1 && source.g_eta < row.n) {
    source.status = "source_invariant_factor_eta";
    source.classification = "direct_source_invariant_eta";
    source.event = "ge";
    return source;
  }
  if (source.g_eta == row.n) {
    source.status = "source_degenerate_eta";
    return source;
  }
  source.delta4 = canonical_mod(
      mod_product(source.t, source.t, row.n, counts) - source.eta, row.n);
  source.g_delta = gcd_owned(source.delta4, row.n, counts);
  if (source.g_delta > 1 && source.g_delta < row.n) {
    source.status = "source_invariant_factor_delta";
    source.classification = "direct_source_invariant_delta";
    source.event = "gd";
    return source;
  }
  if (source.g_delta == row.n) {
    source.status = "source_degenerate_delta";
    return source;
  }
  source.small = pair_chain(source.t, source.eta, row.n, 16, counts);
  for (int m = 2; m <= 16; ++m) {
    const cpp_int g = gcd_owned(source.small[static_cast<std::size_t>(m)].q,
                                row.n, counts);
    if (g > 1 && g < row.n) {
      source.status = "source_order_factor";
      source.classification = "direct_source_order";
      source.event = source_order_event(m);
      return source;
    }
    if (g == row.n) set_mask(&source.mask, m - 2);
  }
  const Pair power_b = pair_power(source.t, source.eta, row.b, row.n, counts);
  source.p_b = power_b.p;
  source.q_b = power_b.q;
  source.g_q = gcd_owned(source.q_b, row.n, counts);
  source.g_p = gcd_owned(source.p_b, row.n, counts);
  if (source.g_q > 1 && source.g_q < row.n) {
    source.status = "powered_collision_factor";
    source.classification = "direct_powered_collision";
    source.event = "qb";
    return source;
  }
  if (source.g_p > 1 && source.g_p < row.n) {
    source.status = "half_order_factor";
    source.classification = "direct_half_order";
    source.event = "pb";
    return source;
  }
  if (source.g_q == row.n) set_mask(&source.mask, 557);
  if (source.g_p == row.n) set_mask(&source.mask, 558);
  return source;
}

const std::vector<Pair>& full_source_powers(const FixtureRow& row,
                                            SourceEvaluation* source) {
  if (!source->full.has_value())
    source->full = pair_chain(source->t, source->eta, row.n, 256, nullptr);
  return *source->full;
}

struct RawClassification {
  std::string classification = "box_unexplained_exclusive";
  std::string event = "-";
  std::array<unsigned char,70> mask{};
  std::vector<cpp_int> large_exponents;
};

std::string first_global_class(const std::array<unsigned char,70>& mask) {
  for (int bit = 0; bit <= 14; ++bit)
    if ((mask[static_cast<std::size_t>(bit/8)] & (0x80U >> (bit%8))) != 0)
      return "registered_global_source_order";
  if ((mask[69] & (0x80U >> 5)) != 0) return "registered_global_powered_collision";
  if ((mask[69] & (0x80U >> 6)) != 0) return "registered_global_half_order";
  return "";
}

RawClassification classify_raw(const FixtureRow& row, SourceEvaluation* source,
                               const cpp_int& v, PacketCounters* packet,
                               OperationCounts* counts) {
  RawClassification result;
  result.mask = source->mask;
  std::string first_global = first_global_class(result.mask);
  std::string first_proper;
  std::string first_event;
  const auto& source_powers = full_source_powers(row, source);
  counts->pair_muls = checked_add(counts->pair_muls, 240);
  counts->mod_muls = checked_add(counts->mod_muls, 1200);
  const std::vector<Pair> target_powers = pair_chain(v, source->eta, row.n, 16,
                                                     counts);
  int orbit_bit = 15;
  for (int e = -16; e <= 16; ++e) {
    if (e == 0) continue;
    const Pair& p = source_powers[static_cast<std::size_t>(e < 0 ? -e : e)];
    const cpp_int product = mod_product(v, p.q, row.n, counts);
    const cpp_int residue = canonical_mod(p.p + (e < 0 ? product : -product),
                                          row.n);
    const cpp_int g = gcd_owned(residue, row.n, counts);
    if (g > 1 && g < row.n && first_proper.empty()) {
      first_proper = "direct_registered_orbit";
      first_event = orbit_event(e);
    }
    if (g == row.n) {
      set_mask(&result.mask, orbit_bit);
      if (first_global.empty()) first_global = "registered_global_orbit";
    }
    ++orbit_bit;
  }
  for (int m = 2; m <= 16; ++m) {
    const cpp_int g = gcd_owned(target_powers[static_cast<std::size_t>(m)].q,
                                row.n, counts);
    if (g > 1 && g < row.n && first_proper.empty()) {
      first_proper = "direct_registered_target_torsion";
      first_event = target_torsion_event(m);
    }
    if (g == row.n) {
      set_mask(&result.mask, 47 + m - 2);
      if (first_global.empty()) first_global = "registered_global_target_torsion";
    }
  }
  int mixed_bit = 62;
  for (int e = -16; e <= 16; ++e) {
    for (int m = 2; m <= 16; ++m, ++mixed_bit) {
      const Pair& target = target_powers[static_cast<std::size_t>(m)];
      const int exponent = e * m;
      const Pair& source_power = source_powers[static_cast<std::size_t>(
          exponent < 0 ? -exponent : exponent)];
      const cpp_int rq = mod_product(target.p,
          exponent < 0 ? canonical_mod(-source_power.q, row.n) : source_power.q,
          row.n, counts);
      const cpp_int sp = mod_product(target.q, source_power.p, row.n, counts);
      const cpp_int determinant = canonical_mod(rq - sp, row.n);
      const cpp_int g = gcd_owned(determinant, row.n, counts);
      if (g > 1 && g < row.n && first_proper.empty()) {
        first_proper = "direct_registered_mixed_phase";
        first_event = mixed_event(e,m);
      }
      if (g == row.n) {
        set_mask(&result.mask, mixed_bit);
        bool owns_global = first_global.empty();
        if (owns_global) first_global = "registered_global_mixed_phase";
        reserve_packet_counter(&packet->global, &packet->phase_global,
                               MAX_GLOBAL_ORDER_CHECKS_TOTAL,
                               "global_order_cap");
        const cpp_int large = cpp_int(m) * (row.b - e);
        result.large_exponents.push_back(large);
        const Pair order = pair_power(source->t, source->eta, large, row.n,
                                      counts);
        const cpp_int order_gcd = gcd_owned(order.q, row.n, counts);
        require(order_gcd != 1, 67, "arithmetic",
                "mixed relation order consistency");
        if (order_gcd == row.n && owns_global)
          first_global = "registered_phase_split";
        if (order_gcd > 1 && order_gcd < row.n && first_proper.empty()) {
          first_proper = "direct_registered_mixed_phase";
          first_event = mixed_event(e,m);
        }
      }
    }
  }
  if (!first_proper.empty()) {
    result.classification = first_proper;
    result.event = first_event;
  } else if (!first_global.empty()) {
    result.classification = first_global;
  }
  return result;
}

struct PendingCertificate {
  int candidate = -1;
  std::string left;
  std::string right;
};

PendingCertificate make_certificate(const std::string& phase,
                                    const FixtureRow& row,
                                    const Cleanup& cleanup,
                                    const CandidateSpec& spec,
                                    const SourceEvaluation& source,
                                    const cpp_int& v, const cpp_int& h4,
                                    const cpp_int& g_h, const cpp_int& f,
                                    const cpp_int& g_f,
                                    const RawClassification& classification) {
  const AtomBank& sb = cleanup.banks[static_cast<std::size_t>(spec.source_anchor)];
  const AtomBank& tb = cleanup.banks[static_cast<std::size_t>(spec.target_anchor)];
  const std::string certificate_id = std::string(1, phase == "discovery" ? 'd' : 'h') +
      pad_decimal(static_cast<unsigned>(row.ordinal),4) + "-" + spec.id;
  u64 pair_muls = checked_add(15, power_product_count(row.b));
  pair_muls = checked_add(pair_muls, 15 + 240);
  for (const cpp_int& exponent : classification.large_exponents)
    pair_muls = checked_add(pair_muls, power_product_count(exponent));
  const u64 global = classification.large_exponents.size();
  const u64 mod_muls = checked_add(checked_mul(5, pair_muls, 70, "internal"),
                                   1025);
  const u64 gcds = checked_add(563, global);
  std::vector<std::string> fields{
    certificate_id,phase,row.id,"",spec.id,decimal(row.n),decimal(row.b),
    signed_decimal(ANCHORS[spec.source_anchor]),
    signed_decimal(ANCHORS[spec.target_anchor])
  };
  for (const cpp_int& x : sb.atom) fields.push_back(decimal(x));
  for (const cpp_int& x : tb.atom) fields.push_back(decimal(x));
  fields.insert(fields.end(), {decimal(source.t),decimal(source.eta),decimal(v),
      decimal(source.delta4),decimal(h4),decimal(source.g_eta),decimal(source.g_delta),
      decimal(g_h),decimal(source.p_b),decimal(source.q_b),decimal(f),decimal(source.g_p),
      decimal(source.g_q),decimal(g_f),mask_hex(classification.mask),classification.event,
      decimal(global),decimal(pair_muls),decimal(mod_muls),decimal(gcds),
      classification.classification,
      classification.classification.rfind("direct_",0) == 0
          ? classification.classification + ":" + classification.event
          : classification.classification});
  require(fields.size() == 41, 70, "internal", "certificate field count");
  const std::string left = fields[0] + "\t" + fields[1] + "\t" + fields[2] + "\t";
  std::string right;
  for (std::size_t i = 4; i < fields.size(); ++i) {
    right.push_back('\t');
    right += fields[i];
  }
  right.push_back('\n');
  return {spec.ordinal,left,right};
}

std::string endpoint_record(const std::string& phase, const FixtureRow& row,
                            const CandidateSpec& candidate,
                            const std::string& status, const std::string& f,
                            const std::string& g, const std::string& classification,
                            const std::string& event) {
  return tsv({phase,row.id,candidate.id,status,f,g,classification,event});
}

struct ControlStats {
  u64 potential = 0;
  u64 eligible = 0;
  u64 attempts = 0;
  u64 modulo_rejections = 0;
  u64 target_rejections = 0;
  u64 proper_cleanup_events = 0;
  u64 shortfalls = 0;
  u64 proper_hits = 0;
  void add(const ControlStats& other) {
    potential = checked_add(potential, other.potential);
    eligible = checked_add(eligible, other.eligible);
    attempts = checked_add(attempts, other.attempts);
    modulo_rejections = checked_add(modulo_rejections, other.modulo_rejections);
    target_rejections = checked_add(target_rejections, other.target_rejections);
    proper_cleanup_events = checked_add(proper_cleanup_events,
                                        other.proper_cleanup_events);
    shortfalls = checked_add(shortfalls, other.shortfalls);
    proper_hits = checked_add(proper_hits, other.proper_hits);
  }
};

cpp_int read_tape_block(int row, int source, int control, int attempt,
                        OperationCounts* counts) {
  const u64 block = (((static_cast<u64>(row) * SOURCES + source) * 2 + control) *
                     3 + attempt);
  const u64 offset = checked_mul(block, 32, 70, "internal");
  require(offset + 32 <= TAPE_BYTES, 70, "internal", "tape block range");
  std::array<unsigned char,32> bytes{};
  std::size_t done = 0;
  while (done < bytes.size()) {
    const ssize_t got = ::pread(4, bytes.data() + done, bytes.size() - done,
                                static_cast<off_t>(offset + done));
    if (got < 0 && errno == EINTR) continue;
    require(got > 0, 65, "input_io", "ExactTape256 pread");
    done += static_cast<std::size_t>(got);
  }
  counts->tape_blocks = checked_add(counts->tape_blocks, 1);
  cpp_int result = 0;
  for (unsigned char byte : bytes) {
    result <<= 8;
    result += byte;
  }
  return result;
}

void evaluate_controls(const std::string& phase, const FixtureRow& row,
                       const SourceSpec& spec, const SourceEvaluation& source,
                       std::string* stream, ControlStats* stats,
                       OperationCounts* counts) {
  const cpp_int modulus_square = row.n * row.n;
  const cpp_int bound = ((cpp_int(1) << 256) / modulus_square) * modulus_square;
  for (int control = 0; control < CONTROLS_PER_SOURCE; ++control) {
    stats->eligible = checked_add(stats->eligible, 1);
    bool accepted = false;
    for (int attempt = 0; attempt < MAX_ATTEMPTS; ++attempt) {
      stats->attempts = checked_add(stats->attempts, 1);
      const cpp_int r = read_tape_block(row.ordinal, spec.ordinal, control,
                                        attempt, counts);
      if (r >= bound) {
        stats->modulo_rejections = checked_add(stats->modulo_rejections, 1);
        *stream += tsv({phase,row.id,spec.id,std::to_string(control),
                       std::to_string(attempt),"modulo_reject","-","-","-",
                       "-","-","-"});
        continue;
      }
      const cpp_int u = r % modulus_square;
      const cpp_int v = u / row.n;
      const cpp_int w = u % row.n;
      const cpp_int inner = gcd_owned(v, w, counts);
      const cpp_int g_vector = gcd_owned(inner, row.n, counts);
      const cpp_int w2 = mod_product(w, w, row.n, counts);
      const cpp_int eta_w2 = mod_product(source.eta, w2, row.n, counts);
      const cpp_int v2 = mod_product(v, v, row.n, counts);
      const cpp_int target_residue = canonical_mod(v2 - eta_w2, row.n);
      const cpp_int g_target = gcd_owned(target_residue, row.n, counts);
      if (g_vector > 1 && g_vector < row.n)
        stats->proper_cleanup_events = checked_add(stats->proper_cleanup_events, 1);
      if (g_target > 1 && g_target < row.n)
        stats->proper_cleanup_events = checked_add(stats->proper_cleanup_events, 1);
      if (g_vector != 1 || g_target != 1) {
        stats->target_rejections = checked_add(stats->target_rejections, 1);
        *stream += tsv({phase,row.id,spec.id,std::to_string(control),
                       std::to_string(attempt),"target_reject",decimal(v),decimal(w),
                       decimal(g_vector),decimal(g_target),"-","-"});
        continue;
      }
      const cpp_int wp = mod_product(w, source.p_b, row.n, counts);
      const cpp_int vq = mod_product(v, source.q_b, row.n, counts);
      const cpp_int f = canonical_mod(wp - vq, row.n);
      const cpp_int g_f = gcd_owned(f, row.n, counts);
      if (g_f > 1 && g_f < row.n)
        stats->proper_hits = checked_add(stats->proper_hits, 1);
      *stream += tsv({phase,row.id,spec.id,std::to_string(control),
                     std::to_string(attempt),"accept",decimal(v),decimal(w),
                     decimal(g_vector),decimal(g_target),decimal(f),decimal(g_f)});
      accepted = true;
      break;
    }
    if (!accepted) {
      stats->shortfalls = checked_add(stats->shortfalls, 1);
      fail(68, "control_shortfall", "three ExactTape256 attempts rejected");
    }
  }
}

struct RowResult {
  int ordinal = -1;
  std::string row_record;
  std::string endpoint_stream;
  std::string control_stream;
  std::string diagnostic_records;
  std::vector<unsigned char> proper;
  std::vector<unsigned char> unexplained;
  std::vector<PendingCertificate> certificates;
  OperationCounts operations;
  ControlStats controls;
  u64 eligible_sources = 0;
  u64 eligible_candidates = 0;
  u64 raw_hits = 0;
  u64 unexplained_hits = 0;
  bool cleanup = false;
};

std::string certificate_header() {
  return "certificate_id\tphase\trow_id\tcandidate_rank\tcandidate_id\tN\tB\tsource_anchor\ttarget_anchor\tsx\tsd\tsr\tsu\tsk\ttx\ttd\ttr\ttu\ttk\tt\teta\tv\tdelta4\tH4\tg_eta\tg_delta\tg_H\tP_B\tQ_B\tF\tg_P\tg_Q\tg_F\tsaturated_mask\tfirst_direct_event\tglobal_order_checks\tpair_muls\tmod_muls\tgcds\tclassification\treason\n";
}

std::string endpoint_header() {
  return "phase\trow_id\tcandidate_id\tstatus\tF\tg_F\tclassification\tfirst_direct_event\n";
}

std::string control_header() {
  return "phase\trow_id\tsource_id\tcontrol_index\tattempt\toutcome\tV\tW\tg_vector\tg_target\tF_uniform\tg_F_uniform\n";
}

std::string rows_header() {
  return "row_id\tB\tb_pub\tstatus\tcleanup_code\tcleanup_gcd\teligible_sources\teligible_candidates\traw_hits\tbox_unexplained_hits\tcontrol_status\n";
}

std::string scores_header() {
  return "candidate_id\tbox_unexplained_rows\tscale_count\tmin_scale_count\tproper_endpoint_rows\n";
}

std::string selection_header() {
  return "rank\tcandidate_id\tbox_unexplained_rows\tscale_count\tmin_scale_count\tproper_endpoint_rows\n";
}

std::string evaluate_diagnostic(const std::string& phase,
                                const FixtureRow& row,
                                const Cleanup& cleanup,
                                PacketCounters* packet,
                                OperationCounts* counts);

RowResult evaluate_row(const std::string& phase, const FixtureRow& row,
                       const Grammar& grammar, PacketCounters* packet) {
  RowResult result;
  result.ordinal = row.ordinal;
  result.proper.assign(CANDIDATES, 0);
  result.unexplained.assign(CANDIDATES, 0);
  result.controls.potential = static_cast<u64>(SOURCES) * CONTROLS_PER_SOURCE;
  const Cleanup cleanup = clean_row(row, &result.operations);
  if (!cleanup.clean) {
    result.cleanup = true;
    for (const CandidateSpec& candidate : grammar.candidates)
      result.endpoint_stream += endpoint_record(phase,row,candidate,"row_cleanup",
                                                "-","-","-","-");
    result.row_record = tsv({row.id,decimal(row.b),std::to_string(row.b_pub),
        "cleanup",cleanup.code,decimal(cleanup.factor),"0","0","0","0",
        "not_run"});
    result.diagnostic_records = evaluate_diagnostic(phase,row,cleanup,packet,
                                                     &result.operations);
    return result;
  }

  for (const SourceSpec& source_spec : grammar.sources) {
    SourceEvaluation source = evaluate_source(row, cleanup, source_spec,
                                              &result.operations);
    const auto& indices = grammar.candidates_by_source[
        static_cast<std::size_t>(source_spec.ordinal)];
    if (source.status != "endpoint_eligible") {
      for (int index : indices) {
        const CandidateSpec& candidate = grammar.candidates[static_cast<std::size_t>(index)];
        result.endpoint_stream += endpoint_record(
            phase,row,candidate,source.status,"-","-",source.classification,
            source.event);
      }
      continue;
    }
    result.eligible_sources = checked_add(result.eligible_sources, 1);
    for (int index : indices) {
      const CandidateSpec& candidate = grammar.candidates[static_cast<std::size_t>(index)];
      const cpp_int v = expression_value(
          cleanup.banks[static_cast<std::size_t>(candidate.target_anchor)],
          candidate.value,row.n);
      const cpp_int v2 = mod_product(v,v,row.n,&result.operations);
      const cpp_int h4 = canonical_mod(v2 - source.eta,row.n);
      const cpp_int g_h = gcd_owned(h4,row.n,&result.operations);
      if (g_h > 1 && g_h < row.n) {
        result.endpoint_stream += endpoint_record(
            phase,row,candidate,"target_invariant_factor","-","-",
            "direct_target_invariant","gh");
        continue;
      }
      if (g_h == row.n) {
        result.endpoint_stream += endpoint_record(
            phase,row,candidate,"target_degenerate","-","-","-","-");
        continue;
      }
      result.eligible_candidates = checked_add(result.eligible_candidates, 1);
      const cpp_int vq = mod_product(v,source.q_b,row.n,&result.operations);
      const cpp_int f = canonical_mod(source.p_b - vq,row.n);
      const cpp_int g_f = gcd_owned(f,row.n,&result.operations);
      if (g_f == 1) {
        result.endpoint_stream += endpoint_record(phase,row,candidate,"no_hit",
                                                  decimal(f),"1","-","-");
        continue;
      }
      if (g_f == row.n) {
        result.endpoint_stream += endpoint_record(
            phase,row,candidate,"saturated_hit",decimal(f),decimal(g_f),"-","-");
        continue;
      }
      reserve_packet_counter(&packet->raw,&packet->phase_raw,MAX_RAW_HITS_TOTAL,
                             "raw_hit_cap");
      result.raw_hits = checked_add(result.raw_hits, 1);
      result.proper[static_cast<std::size_t>(index)] = 1;
      RawClassification classification = classify_raw(
          row,&source,v,packet,&result.operations);
      literal_matrix_check(row.n,row.b,source.t,source.eta,v,f,
                           &result.operations);
      if (classification.classification == "box_unexplained_exclusive") {
        result.unexplained[static_cast<std::size_t>(index)] = 1;
        result.unexplained_hits = checked_add(result.unexplained_hits, 1);
      }
      result.certificates.push_back(make_certificate(
          phase,row,cleanup,candidate,source,v,h4,g_h,f,g_f,classification));
      result.endpoint_stream += endpoint_record(
          phase,row,candidate,"raw_proper_hit",decimal(f),decimal(g_f),
          classification.classification,classification.event);
    }
    evaluate_controls(phase,row,source_spec,source,&result.control_stream,
                      &result.controls,&result.operations);
  }
  result.row_record = tsv({row.id,decimal(row.b),std::to_string(row.b_pub),
      "eligible","-","-",decimal(result.eligible_sources),
      decimal(result.eligible_candidates),decimal(result.raw_hits),
      decimal(result.unexplained_hits),"pass"});
  result.diagnostic_records = evaluate_diagnostic(phase,row,cleanup,packet,
                                                   &result.operations);
  return result;
}

std::string diagnostic_header() {
  return "phase\trow_id\tN\tB\tD0\tA0\tscan_status\tstop_base\tstop_exponent\tdirect_factor\tretained_z\tbases_screened\texponent_checks\tscan_checksum\ttarget_id\ttarget_status\tt\teta\tv\tP_B\tQ_B\tF\tg_P\tg_Q\tg_F\tclassification\tfirst_direct_event\n";
}

std::string diagnostic_scan_header() {
  return "phase\trow_id\tbase\texponent\tvalue\tgcd\toutcome\n";
}

SourceEvaluation evaluate_diagnostic_source(const FixtureRow& row,
                                            const cpp_int& z,
                                            OperationCounts* counts) {
  SourceEvaluation source;
  source.eta = 1;
  const cpp_int denominator = canonical_mod(z - 1,row.n);
  const cpp_int denominator_gcd = gcd_owned(denominator,row.n,counts);
  require(denominator_gcd == 1,67,"arithmetic","retained base denominator");
  source.t = mod_product(canonical_mod(z + 1,row.n),
                         inverse_owned(denominator,row.n,counts),row.n,counts);
  source.g_eta = gcd_owned(source.eta,row.n,counts);
  source.delta4 = canonical_mod(
      mod_product(source.t,source.t,row.n,counts) - source.eta,row.n);
  source.g_delta = gcd_owned(source.delta4,row.n,counts);
  require(source.g_eta == 1 && source.g_delta == 1,67,"arithmetic",
          "diagnostic source invariant");
  source.small = pair_chain(source.t,source.eta,row.n,16,counts);
  for (int m=2;m<=16;++m) {
    const cpp_int g = gcd_owned(source.small[static_cast<std::size_t>(m)].q,
                                row.n,counts);
    require(g == 1,67,"arithmetic","diagnostic small source order");
  }
  const Pair power = pair_power(source.t,source.eta,row.b,row.n,counts);
  source.p_b = power.p;
  source.q_b = power.q;
  source.g_q = gcd_owned(source.q_b,row.n,counts);
  source.g_p = gcd_owned(source.p_b,row.n,counts);
  if (source.g_q > 1 && source.g_q < row.n) {
    source.status = "powered_collision_factor";
    source.classification = "direct_powered_collision";
    source.event = "qb";
  } else if (source.g_p > 1 && source.g_p < row.n) {
    source.status = "half_order_factor";
    source.classification = "direct_half_order";
    source.event = "pb";
  }
  if (source.g_q == row.n) set_mask(&source.mask,557);
  if (source.g_p == row.n) set_mask(&source.mask,558);
  return source;
}

std::string diagnostic_common(const std::string& phase,
                              const FixtureRow& row, unsigned d0,
                              unsigned a0, const std::string& status,
                              const std::string& stop_base,
                              const std::string& stop_exponent,
                              const std::string& direct_factor,
                              const std::string& retained,
                              u64 bases, u64 exponents,
                              const std::string& checksum) {
  return phase + "\t" + row.id + "\t" + decimal(row.n) + "\t" +
      decimal(row.b) + "\t" + std::to_string(d0) + "\t" +
      std::to_string(a0) + "\t" + status + "\t" + stop_base + "\t" +
      stop_exponent + "\t" + direct_factor + "\t" + retained + "\t" +
      decimal(bases) + "\t" + decimal(exponents) + "\t" + checksum;
}

std::string diagnostic_no_target(const std::string& common) {
  return common + "\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-\n";
}

std::string evaluate_diagnostic(const std::string& phase,
                                const FixtureRow& row,
                                const Cleanup& cleanup,
                                PacketCounters* packet,
                                OperationCounts* counts) {
  if (!row.diagnostic) return "";
  const unsigned d0 = bit_length(row.n);
  const unsigned a0 = d0*d0+d0;
  if (!cleanup.clean) {
    const std::string common = diagnostic_common(phase,row,d0,a0,"row_cleanup",
                                                  "-","-","-","-",0,0,"-");
    const std::string record = diagnostic_no_target(common);
    require(split_tabs(record.substr(0,record.size()-1)).size() == 27,
            70,"internal","diagnostic cleanup fields");
    return record;
  }
  Sha256 scan_hash;
  const std::string header = diagnostic_scan_header();
  scan_hash.update(header);
  counts->sha256_contexts = checked_add(counts->sha256_contexts,1);
  counts->sha256_updates = checked_add(counts->sha256_updates,1);
  counts->sha256_bytes = checked_add(counts->sha256_bytes,header.size());
  u64 bases = 0;
  u64 exponents = 0;
  std::string scan_status = "diagnostic_shortfall";
  std::string stop_base = "-";
  std::string stop_exponent = "-";
  std::string direct_factor = "-";
  cpp_int retained = 0;
  for (unsigned a=2;a<=a0;++a) {
    bases = checked_add(bases,1);
    const cpp_int base = a;
    const cpp_int base_gcd = gcd_owned(base,row.n,counts);
    const std::string base_outcome = base_gcd == 1 ? "one" :
        (base_gcd == row.n ? "saturated" : "proper");
    const std::string base_record = tsv({phase,row.id,std::to_string(a),"0",
                                         std::to_string(a),decimal(base_gcd),
                                         base_outcome});
    scan_hash.update(base_record);
    counts->sha256_updates = checked_add(counts->sha256_updates,1);
    counts->sha256_bytes = checked_add(counts->sha256_bytes,base_record.size());
    counts->diagnostic_scan_records = checked_add(
        counts->diagnostic_scan_records,1);
    if (base_gcd > 1 && base_gcd < row.n) {
      scan_status = "diagnostic_factor";
      stop_base = std::to_string(a);
      stop_exponent = "0";
      direct_factor = decimal(base_gcd);
      break;
    }
    if (base_gcd == row.n) continue;
    cpp_int power = 1;
    bool rejected = false;
    for (unsigned e=1;e<=d0;++e) {
      power = mod_product(power,base,row.n,counts);
      const cpp_int value = canonical_mod(power-1,row.n);
      const cpp_int g = gcd_owned(value,row.n,counts);
      exponents = checked_add(exponents,1);
      const std::string outcome = g == 1 ? "one" :
          (g == row.n ? "saturated" : "proper");
      const std::string record = tsv({phase,row.id,std::to_string(a),
          std::to_string(e),decimal(value),decimal(g),outcome});
      scan_hash.update(record);
      counts->sha256_updates = checked_add(counts->sha256_updates,1);
      counts->sha256_bytes = checked_add(counts->sha256_bytes,record.size());
      counts->diagnostic_scan_records = checked_add(
          counts->diagnostic_scan_records,1);
      if (g > 1 && g < row.n) {
        scan_status = "diagnostic_factor";
        stop_base = std::to_string(a);
        stop_exponent = std::to_string(e);
        direct_factor = decimal(g);
        rejected = true;
        break;
      }
      if (g == row.n) {
        rejected = true;
        break;
      }
    }
    if (scan_status == "diagnostic_factor") break;
    if (!rejected) {
      scan_status = "retained";
      stop_base = std::to_string(a);
      stop_exponent = std::to_string(d0);
      retained = a;
      break;
    }
  }
  const std::string checksum = scan_hash.final_hex();
  if (scan_status != "retained") {
    const std::string common = diagnostic_common(
        phase,row,d0,a0,scan_status,stop_base,stop_exponent,direct_factor,"-",
        bases,exponents,checksum);
    const std::string record = diagnostic_no_target(common);
    require(record.size() <= MAX_RECORD_DIAGNOSTIC,66,"serialization",
            "diagnostic record cap");
    return record;
  }
  SourceEvaluation source = evaluate_diagnostic_source(row,retained,counts);
  const std::string common = diagnostic_common(
      phase,row,d0,a0,"retained",stop_base,stop_exponent,"-",decimal(retained),
      bases,exponents,checksum);
  std::string output;
  for (int anchor=0;anchor<9;++anchor) {
    for (int vv=0;vv<10;++vv) {
      const std::string id = target_id(anchor,vv);
      const cpp_int v = expression_value(cleanup.banks[static_cast<std::size_t>(anchor)],
                                         vv,row.n);
      std::vector<std::string> target{id,source.status,decimal(source.t),
          decimal(source.eta),decimal(v),decimal(source.p_b),decimal(source.q_b),
          "-",decimal(source.g_p),decimal(source.g_q),"-",source.classification,
          source.event};
      if (source.status == "endpoint_eligible") {
        const cpp_int v2 = mod_product(v,v,row.n,counts);
        const cpp_int h4 = canonical_mod(v2-source.eta,row.n);
        const cpp_int g_h = gcd_owned(h4,row.n,counts);
        if (g_h > 1 && g_h < row.n) {
          target[1] = "target_invariant_factor";
          target[11] = "direct_target_invariant";
          target[12] = "gh";
        } else if (g_h == row.n) {
          target[1] = "target_degenerate";
          target[11] = "-";
          target[12] = "-";
        } else {
          const cpp_int vq = mod_product(v,source.q_b,row.n,counts);
          const cpp_int f = canonical_mod(source.p_b-vq,row.n);
          const cpp_int g_f = gcd_owned(f,row.n,counts);
          target[7] = decimal(f);
          target[10] = decimal(g_f);
          target[11] = "-";
          target[12] = "-";
          if (g_f == 1) target[1] = "no_hit";
          else if (g_f == row.n) target[1] = "saturated_hit";
          else {
            target[1] = "raw_proper_hit";
            RawClassification classification = classify_raw(
                row,&source,v,packet,counts);
            target[11] = classification.classification;
            target[12] = classification.event;
            literal_matrix_check(row.n,row.b,source.t,source.eta,v,f,counts);
          }
        }
      }
      std::string record = common;
      for (const std::string& field : target) {
        record.push_back('\t');
        record += field;
      }
      record.push_back('\n');
      require(split_tabs(record.substr(0,record.size()-1)).size() == 27 &&
              record.size() <= MAX_RECORD_DIAGNOSTIC,
              66,"serialization","diagnostic target record");
      output += record;
    }
  }
  return output;
}

std::string read_openat_file(const std::string& name, u64 maximum,
                             const std::string& context) {
  const int fd = ::openat(9,name.c_str(),O_RDONLY|O_NOFOLLOW);
  require(fd >= 0,65,"input_io",context+": openat");
  try {
    const std::string bytes = read_fd_all(fd,maximum,context);
    require(::close(fd) == 0,65,"input_io",context+": close");
    return bytes;
  } catch (...) {
    ::close(fd);
    throw;
  }
}

class CompareFile {
 public:
  CompareFile(std::string name, const ManifestRow& expected)
      : name_(std::move(name)), expected_(expected) {
    fd_ = ::openat(9,name_.c_str(),O_RDONLY|O_NOFOLLOW);
    require(fd_ >= 0,67,"replay","open sealed artifact");
    struct stat st{};
    require(::fstat(fd_,&st) == 0 && S_ISREG(st.st_mode) && st.st_size >= 0 &&
            static_cast<u64>(st.st_size) == expected_.bytes,
            67,"replay","sealed artifact size");
    require(hash_fd(fd_,expected_.bytes,"sealed artifact") == expected_.hash,
            67,"replay","sealed artifact hash");
  }
  CompareFile(const CompareFile&) = delete;
  CompareFile& operator=(const CompareFile&) = delete;
  ~CompareFile() { if (fd_ >= 0) ::close(fd_); }
  void append(const std::string& bytes, u64 record_cap=0) {
    require(!bytes.empty() && bytes.back()=='\n',66,"serialization",
            "replay serializer LF");
    if (record_cap != 0)
      require(bytes.size() <= record_cap,66,"serialization",
              "replay record cap");
    require(offset_ <= expected_.bytes && bytes.size() <= expected_.bytes-offset_,
            67,"replay","sealed artifact excess");
    std::vector<char> actual(bytes.size());
    std::size_t done=0;
    while (done<actual.size()) {
      const ssize_t got=::pread(fd_,actual.data()+done,actual.size()-done,
                                static_cast<off_t>(offset_+done));
      if (got<0 && errno==EINTR) continue;
      require(got>0,67,"replay","sealed artifact pread");
      done+=static_cast<std::size_t>(got);
    }
    require(std::equal(actual.begin(),actual.end(),bytes.begin()),
            67,"replay","sealed artifact byte mismatch");
    offset_+=static_cast<u64>(bytes.size());
  }
  std::string close_and_hash(OperationCounts* counts) {
    require(offset_==expected_.bytes,67,"replay","sealed artifact truncation");
    require(::close(fd_)==0,67,"replay","sealed artifact close");
    fd_=-1;
    if (counts!=nullptr) {
      counts->sha256_contexts=checked_add(counts->sha256_contexts,1);
      counts->sha256_updates=checked_add(counts->sha256_updates,
                                         (expected_.bytes+1048575)/1048576);
      counts->sha256_bytes=checked_add(counts->sha256_bytes,expected_.bytes);
    }
    return expected_.hash;
  }
  u64 bytes() const { return expected_.bytes; }
 private:
  std::string name_;
  ManifestRow expected_;
  int fd_=-1;
  u64 offset_=0;
};

struct Score {
  u64 unexplained=0;
  u64 proper=0;
  std::array<u64,4> by_scale{{0,0,0,0}};
  u64 scale_count() const {
    u64 result=0;
    for (u64 value:by_scale) if (value!=0) ++result;
    return result;
  }
  u64 minimum() const {
    return *std::min_element(by_scale.begin(),by_scale.end());
  }
};

int scale_index(const std::string& phase, unsigned scale) {
  const std::array<unsigned,4> discovery{{18,24,30,36}};
  const std::array<unsigned,4> heldout{{40,46,52,56}};
  const auto& values=phase=="discovery"?discovery:heldout;
  for (int i=0;i<4;++i) if (values[static_cast<std::size_t>(i)]==scale) return i;
  fail(70,"internal","unregistered public scale");
}

void hash_record_stream(Sha256* hash, const std::string& bytes,
                        u64 expected_records, OperationCounts* counts,
                        bool endpoint) {
  std::size_t begin=0;
  u64 records=0;
  while (begin<bytes.size()) {
    const std::size_t end=bytes.find('\n',begin);
    require(end!=std::string::npos,70,"internal","checksum stream LF");
    const std::string record=bytes.substr(begin,end-begin+1);
    hash->update(record);
    counts->sha256_updates=checked_add(counts->sha256_updates,1);
    counts->sha256_bytes=checked_add(counts->sha256_bytes,record.size());
    ++records;
    begin=end+1;
  }
  require(records==expected_records,70,"internal","checksum record count");
  if (endpoint)
    counts->endpoint_checksum_records=checked_add(
        counts->endpoint_checksum_records,records);
  else
    counts->control_checksum_records=checked_add(
        counts->control_checksum_records,records);
}

std::string operations_json(const OperationCounts& c) {
  return "{\"pair_muls\":"+decimal(c.pair_muls)+
      ",\"mod_muls\":"+decimal(c.mod_muls)+
      ",\"gcds\":"+decimal(c.gcds)+
      ",\"inverses\":"+decimal(c.inverses)+
      ",\"matrix_muls\":"+decimal(c.matrix_muls)+
      ",\"sha256_contexts\":"+decimal(c.sha256_contexts)+
      ",\"sha256_updates\":"+decimal(c.sha256_updates)+
      ",\"sha256_bytes\":"+decimal(c.sha256_bytes)+
      ",\"tape_blocks\":"+decimal(c.tape_blocks)+
      ",\"endpoint_checksum_records\":"+decimal(c.endpoint_checksum_records)+
      ",\"control_checksum_records\":"+decimal(c.control_checksum_records)+
      ",\"diagnostic_scan_records\":"+decimal(c.diagnostic_scan_records)+"}";
}

struct EvaluationResult {
  std::string summary_hash;
  std::string selection_hash;
  std::string endpoint_checksum;
  std::string control_checksum;
  std::string diagnostic_hash;
  u64 public_replay_count=static_cast<u64>(ROWS_PER_PHASE)*CANDIDATES;
  u64 matrix_checks=0;
};

template<class Sink>
EvaluationResult evaluate_phase_to_sinks(
    const AuthenticatedInputs& inputs, const Carry& carry, const Grammar& grammar,
    Sink& rows_file, Sink& scores_file, Sink& certificates_file,
    Sink& controls_file, Sink& diagnostic_file, Sink* selection_file,
    Sink& summary_file) {
  const std::string phase=inputs.phase;
  PacketCounters packet(carry);
  rows_file.append(rows_header(),4096);
  scores_file.append(scores_header(),4096);
  certificates_file.append(certificate_header(),4096);
  diagnostic_file.append(diagnostic_header(),4096);
  Sha256 endpoint_hash;
  Sha256 control_hash;
  OperationCounts operations;
  endpoint_hash.update(endpoint_header());
  control_hash.update(control_header());
  operations.sha256_contexts=2;
  operations.sha256_updates=2;
  operations.sha256_bytes=endpoint_header().size()+control_header().size();
  std::vector<Score> scores(CANDIDATES);
  std::vector<PendingCertificate> pending;
  ControlStats control_stats;
  u64 cleanup_rows=0;
  u64 raw_hits=0;
  u64 unexplained_hits=0;
  u64 matrix_checks=0;

  struct Slot {
    std::mutex mutex;
    std::condition_variable cv;
    std::optional<RowResult> result;
    std::exception_ptr failure;
    bool finished=false;
  };
  std::array<Slot,WORKERS> slots;
  std::atomic<bool> cancel{false};
  std::vector<std::thread> workers;
  workers.reserve(WORKERS);
  try {
    for (int worker=0;worker<WORKERS;++worker) {
      workers.emplace_back([&,worker] {
        try {
          for (int row=worker;row<ROWS_PER_PHASE;row+=WORKERS) {
            if (cancel.load(std::memory_order_relaxed)) break;
            RowResult value=evaluate_row(phase,inputs.rows[static_cast<std::size_t>(row)],
                                         grammar,&packet);
            Slot& slot=slots[static_cast<std::size_t>(worker)];
            std::unique_lock<std::mutex> lock(slot.mutex);
            slot.cv.wait(lock,[&]{return !slot.result.has_value()||
                                         cancel.load(std::memory_order_relaxed);});
            if (cancel.load(std::memory_order_relaxed)) break;
            slot.result.emplace(std::move(value));
            lock.unlock();
            slot.cv.notify_all();
          }
        } catch (...) {
          Slot& slot=slots[static_cast<std::size_t>(worker)];
          {
            std::lock_guard<std::mutex> lock(slot.mutex);
            slot.failure=std::current_exception();
          }
          cancel.store(true,std::memory_order_relaxed);
          for (Slot& item:slots) item.cv.notify_all();
        }
        Slot& slot=slots[static_cast<std::size_t>(worker)];
        {
          std::lock_guard<std::mutex> lock(slot.mutex);
          slot.finished=true;
        }
        slot.cv.notify_all();
      });
    }
  } catch (...) {
    cancel.store(true,std::memory_order_relaxed);
    for (Slot& slot:slots) slot.cv.notify_all();
    for (std::thread& worker:workers) if (worker.joinable()) worker.join();
    fail(68,"thread_resource","creation of four workers");
  }

  std::exception_ptr merge_failure;
  try {
    for (int ordinal=0;ordinal<ROWS_PER_PHASE;++ordinal) {
      Slot& slot=slots[static_cast<std::size_t>(ordinal%WORKERS)];
      std::unique_lock<std::mutex> lock(slot.mutex);
      slot.cv.wait(lock,[&]{return slot.result.has_value()||slot.failure||slot.finished;});
      if (slot.failure) std::rethrow_exception(slot.failure);
      require(slot.result.has_value() && slot.result->ordinal==ordinal,
              70,"internal","stable worker merge");
      RowResult row=std::move(*slot.result);
      slot.result.reset();
      lock.unlock();
      slot.cv.notify_all();
      rows_file.append(row.row_record,MAX_RECORD_ROW);
      if (!row.diagnostic_records.empty()) {
        std::size_t begin=0;
        while (begin<row.diagnostic_records.size()) {
          const std::size_t end=row.diagnostic_records.find('\n',begin);
          require(end!=std::string::npos,70,"internal","diagnostic merge LF");
          diagnostic_file.append(row.diagnostic_records.substr(begin,end-begin+1),
                                 MAX_RECORD_DIAGNOSTIC);
          begin=end+1;
        }
      }
      hash_record_stream(&endpoint_hash,row.endpoint_stream,CANDIDATES,
                         &row.operations,true);
      hash_record_stream(&control_hash,row.control_stream,row.controls.attempts,
                         &row.operations,false);
      const int scale=scale_index(phase,inputs.rows[static_cast<std::size_t>(ordinal)].b_pub);
      for (int candidate=0;candidate<CANDIDATES;++candidate) {
        if (row.proper[static_cast<std::size_t>(candidate)]!=0)
          scores[static_cast<std::size_t>(candidate)].proper=checked_add(
              scores[static_cast<std::size_t>(candidate)].proper,1);
        if (row.unexplained[static_cast<std::size_t>(candidate)]!=0) {
          Score& score=scores[static_cast<std::size_t>(candidate)];
          score.unexplained=checked_add(score.unexplained,1);
          score.by_scale[static_cast<std::size_t>(scale)]=checked_add(
              score.by_scale[static_cast<std::size_t>(scale)],1);
        }
      }
      cleanup_rows=checked_add(cleanup_rows,row.cleanup?1:0);
      raw_hits=checked_add(raw_hits,row.raw_hits);
      unexplained_hits=checked_add(unexplained_hits,row.unexplained_hits);
      matrix_checks=checked_add(matrix_checks,row.raw_hits);
      pending.insert(pending.end(),std::make_move_iterator(row.certificates.begin()),
                     std::make_move_iterator(row.certificates.end()));
      control_stats.add(row.controls);
      operations.add(row.operations);
    }
  } catch (...) {
    merge_failure=std::current_exception();
    cancel.store(true,std::memory_order_relaxed);
    for (Slot& slot:slots) slot.cv.notify_all();
  }
  for (std::thread& worker:workers) {
    try { if (worker.joinable()) worker.join(); }
    catch (...) { if (!merge_failure) merge_failure=std::current_exception(); }
  }
  if (merge_failure) std::rethrow_exception(merge_failure);
  require(workers.size()==WORKERS,68,"thread_resource","four worker count");
  require(packet.phase_raw.load()==raw_hits,70,"internal","raw counter ownership");
  require(control_stats.potential==static_cast<u64>(ROWS_PER_PHASE)*SOURCES*2,
          70,"internal","potential controls");

  for (int candidate=0;candidate<CANDIDATES;++candidate) {
    const Score& score=scores[static_cast<std::size_t>(candidate)];
    scores_file.append(tsv({grammar.candidates[static_cast<std::size_t>(candidate)].id,
        decimal(score.unexplained),decimal(score.scale_count()),decimal(score.minimum()),
        decimal(score.proper)}),MAX_RECORD_SCORE);
  }
  std::vector<int> ranking(CANDIDATES);
  for (int i=0;i<CANDIDATES;++i) ranking[static_cast<std::size_t>(i)]=i;
  std::stable_sort(ranking.begin(),ranking.end(),[&](int a,int b) {
    const Score& x=scores[static_cast<std::size_t>(a)];
    const Score& y=scores[static_cast<std::size_t>(b)];
    if (x.unexplained!=y.unexplained) return x.unexplained>y.unexplained;
    if (x.scale_count()!=y.scale_count()) return x.scale_count()>y.scale_count();
    if (x.minimum()!=y.minimum()) return x.minimum()>y.minimum();
    if (x.proper!=y.proper) return x.proper>y.proper;
    return a<b;
  });
  std::vector<unsigned> ranks(CANDIDATES,0);
  std::vector<SelectionEntry> selection;
  if (phase=="discovery") {
    require(selection_file!=nullptr,70,"internal","discovery selection sink");
    selection_file->append(selection_header(),4096);
    for (unsigned rank=1;rank<=128;++rank) {
      const int candidate=ranking[rank-1];
      const Score& score=scores[static_cast<std::size_t>(candidate)];
      ranks[static_cast<std::size_t>(candidate)]=rank;
      selection.push_back({rank,candidate,score.unexplained,score.scale_count(),
                           score.minimum(),score.proper});
      selection_file->append(tsv({std::to_string(rank),
          grammar.candidates[static_cast<std::size_t>(candidate)].id,
          decimal(score.unexplained),decimal(score.scale_count()),
          decimal(score.minimum()),decimal(score.proper)}),MAX_RECORD_SELECTION);
    }
  } else {
    require(selection_file==nullptr && inputs.selection.size()==128,
            70,"internal","heldout selection input");
    selection=inputs.selection;
    for (const SelectionEntry& entry:selection)
      ranks[static_cast<std::size_t>(entry.candidate)]=entry.rank;
  }
  for (const PendingCertificate& certificate:pending) {
    const unsigned rank=ranks[static_cast<std::size_t>(certificate.candidate)];
    const std::string record=certificate.left+
        (rank==0?"-":std::to_string(rank))+certificate.right;
    require(split_tabs(record.substr(0,record.size()-1)).size()==41,
            66,"serialization","certificate field count");
    certificates_file.append(record,MAX_RECORD_CERTIFICATE);
  }

  const std::string endpoint_checksum=endpoint_hash.final_hex();
  const std::string control_checksum=control_hash.final_hex();
  require(control_stats.shortfalls==0,70,"internal","successful controls");
  const std::string controls_json="{\"version\":\""+std::string(VERSION)+
      "\",\"phase\":"+json_string(phase)+
      ",\"tape_sha256\":"+json_string(inputs.tape_hash)+
      ",\"tape_bytes\":"+decimal(TAPE_BYTES)+
      ",\"potential_controls\":"+decimal(control_stats.potential)+
      ",\"eligible_controls\":"+decimal(control_stats.eligible)+
      ",\"attempts\":"+decimal(control_stats.attempts)+
      ",\"modulo_rejections\":"+decimal(control_stats.modulo_rejections)+
      ",\"target_rejections\":"+decimal(control_stats.target_rejections)+
      ",\"proper_cleanup_events\":"+decimal(control_stats.proper_cleanup_events)+
      ",\"shortfalls\":0,\"proper_hits\":"+decimal(control_stats.proper_hits)+
      ",\"control_checksum\":"+json_string(control_checksum)+"}\n";
  require(controls_json.size()<=MAX_JSON_BYTES,66,"serialization","controls JSON cap");
  controls_file.append(controls_json,MAX_JSON_BYTES);

  const std::string rows_hash=rows_file.close_and_hash(&operations);
  const std::string scores_hash=scores_file.close_and_hash(&operations);
  const std::string certificates_hash=certificates_file.close_and_hash(&operations);
  const std::string controls_hash=controls_file.close_and_hash(&operations);
  const std::string diagnostic_hash=diagnostic_file.close_and_hash(&operations);
  std::string selection_hash=inputs.selection_hash;
  u64 output_bytes=rows_file.bytes()+scores_file.bytes()+certificates_file.bytes()+
                   controls_file.bytes()+diagnostic_file.bytes();
  if (phase=="discovery") {
    selection_hash=selection_file->close_and_hash(&operations);
    output_bytes=checked_add(output_bytes,selection_file->bytes());
  }
  const u64 phase_global=packet.phase_global.load();
  require(packet.raw.load()==checked_add(carry.raw,raw_hits) &&
          packet.global.load()==checked_add(carry.global,phase_global),
          70,"internal","packet counter totals");
  const std::string summary="{\"version\":\""+std::string(VERSION)+
      "\",\"phase\":"+json_string(phase)+
      ",\"promise_sha256\":"+json_string(inputs.promise_hash)+
      ",\"inputs_manifest_sha256\":"+json_string(inputs.inputs_hash)+
      ",\"containment_manifest_sha256\":"+json_string(inputs.containment_hash)+
      ",\"public_fixture_sha256\":"+json_string(inputs.fixture_hash)+
      ",\"tape_sha256\":"+json_string(inputs.tape_hash)+
      ",\"selection_sha256\":"+json_string(selection_hash)+
      ",\"row_count\":"+decimal(ROWS_PER_PHASE)+
      ",\"cleanup_rows\":"+decimal(cleanup_rows)+
      ",\"eligible_rows\":"+decimal(ROWS_PER_PHASE-cleanup_rows)+
      ",\"source_slots\":"+decimal(static_cast<u64>(ROWS_PER_PHASE)*SOURCES)+
      ",\"candidate_slots\":"+decimal(static_cast<u64>(ROWS_PER_PHASE)*CANDIDATES)+
      ",\"raw_hits\":"+decimal(raw_hits)+
      ",\"box_unexplained_hits\":"+decimal(unexplained_hits)+
      ",\"global_order_checks\":"+decimal(phase_global)+
      ",\"carry_raw_hits\":"+decimal(carry.raw)+
      ",\"carry_global_order_checks\":"+decimal(carry.global)+
      ",\"packet_raw_hits\":"+decimal(packet.raw.load())+
      ",\"packet_global_order_checks\":"+decimal(packet.global.load())+
      ",\"operation_counts\":"+operations_json(operations)+
      ",\"output_bytes\":"+decimal(output_bytes)+
      ",\"rows_sha256\":"+json_string(rows_hash)+
      ",\"scores_sha256\":"+json_string(scores_hash)+
      ",\"certificates_sha256\":"+json_string(certificates_hash)+
      ",\"controls_sha256\":"+json_string(controls_hash)+
      ",\"diagnostic_sha256\":"+json_string(diagnostic_hash)+
      ",\"endpoint_checksum\":"+json_string(endpoint_checksum)+"}\n";
  require(summary.size()<=MAX_JSON_BYTES,66,"serialization","summary JSON cap");
  summary_file.append(summary,MAX_JSON_BYTES);
  const std::string summary_hash=summary_file.close_and_hash(nullptr);
  return {summary_hash,selection_hash,endpoint_checksum,control_checksum,
          diagnostic_hash,static_cast<u64>(ROWS_PER_PHASE)*CANDIDATES,matrix_checks};
}

std::string scientific_pass_status(Mode mode, const std::string& summary_hash) {
  return "{\"version\":\""+std::string(VERSION)+"\",\"role\":\""+
      std::string(ROLE)+"\",\"mode\":"+json_string(mode_token(mode))+
      ",\"phase\":"+json_string(phase_token(mode))+
      ",\"summary_sha256\":"+json_string(summary_hash)+
      ",\"status\":\"pass\"}\n";
}

std::string replay_pass_status(Mode mode, const AuthenticatedInputs& inputs,
                               const std::string& public_manifest_hash,
                               const EvaluationResult& result) {
  return "{\"version\":\""+std::string(VERSION)+"\",\"role\":\""+
      std::string(ROLE)+"\",\"mode\":"+json_string(mode_token(mode))+
      ",\"phase\":"+json_string(phase_token(mode))+
      ",\"inputs_manifest_sha256\":"+json_string(inputs.inputs_hash)+
      ",\"public_manifest_sha256\":"+json_string(public_manifest_hash)+
      ",\"selection_sha256\":"+json_string(result.selection_hash)+
      ",\"endpoint_checksum\":"+json_string(result.endpoint_checksum)+
      ",\"control_checksum\":"+json_string(result.control_checksum)+
      ",\"diagnostic_sha256\":"+json_string(result.diagnostic_hash)+
      ",\"public_replay_count\":"+decimal(result.public_replay_count)+
      ",\"matrix_checks\":"+decimal(result.matrix_checks)+
      ",\"failures\":[],\"status\":\"pass\"}\n";
}

std::string run_scientific(Mode mode, const Cli& cli, const Grammar& grammar) {
  AuthenticatedInputs inputs=authenticate_inputs(cli,grammar);
  Carry carry=authenticate_carry(cli,inputs);
  const std::string phase=inputs.phase;
  const std::vector<std::string> names=phase=="discovery"
      ? std::vector<std::string>{
          std::string(VERSION)+".discovery.rows.tsv",
          std::string(VERSION)+".discovery.scores.tsv",
          std::string(VERSION)+".discovery.selection.tsv",
          std::string(VERSION)+".discovery.certificates.tsv",
          std::string(VERSION)+".discovery.summary.json",
          std::string(VERSION)+".discovery.controls.json",
          std::string(VERSION)+".discovery.diagnostic.tsv"}
      : std::vector<std::string>{
          std::string(VERSION)+".heldout.rows.tsv",
          std::string(VERSION)+".heldout.scores.tsv",
          std::string(VERSION)+".heldout.certificates.tsv",
          std::string(VERSION)+".heldout.summary.json",
          std::string(VERSION)+".heldout.controls.json",
          std::string(VERSION)+".heldout.diagnostic.tsv"};
  require_output_absent(names);
  OutputBudget budget(carry.output_bytes);
  OutputFile rows(phase=="discovery"?names[0]:names[0],&budget);
  OutputFile scores(names[1],&budget);
  std::unique_ptr<OutputFile> selection;
  std::size_t certificate_index=2;
  std::size_t summary_index=3;
  std::size_t controls_index=4;
  std::size_t diagnostic_index=5;
  if (phase=="discovery") {
    selection=std::make_unique<OutputFile>(names[2],&budget);
    certificate_index=3;
    summary_index=4;
    controls_index=5;
    diagnostic_index=6;
  }
  OutputFile certificates(names[certificate_index],&budget);
  OutputFile controls(names[controls_index],&budget);
  OutputFile diagnostic(names[diagnostic_index],&budget);
  OutputFile summary(names[summary_index],&budget);
  EvaluationResult result=evaluate_phase_to_sinks(
      inputs,carry,grammar,rows,scores,certificates,controls,diagnostic,
      selection.get(),summary);
  return scientific_pass_status(mode,result.summary_hash);
}

std::string run_replay(Mode mode, const Cli& cli, const Grammar& grammar) {
  AuthenticatedInputs inputs=authenticate_inputs(cli,grammar);
  Carry carry=authenticate_carry(cli,inputs);
  const std::string phase=inputs.phase;
  const std::string manifest_name=std::string(VERSION)+"."+phase+
                                  ".public.manifest.tsv";
  const std::string manifest_text=read_openat_file(manifest_name,MAX_JSON_BYTES,
                                                   "phase public manifest");
  const std::string manifest_hash=sha256(manifest_text);
  const auto& required=phase=="discovery"?discovery_manifest_names():
                                          heldout_manifest_names();
  const std::vector<ManifestRow> manifest=parse_manifest(
      manifest_text,"phase public manifest",required);
  if (phase=="discovery") {
    const ManifestRow& selected=manifest_find(
        manifest,std::string(VERSION)+".discovery.selection.tsv");
    require(selected.hash==inputs.selection_hash &&
            selected.bytes==descriptor_size(8,"selection"),
            67,"replay","selection seal binding");
  }
  auto row_for=[&](const std::string& suffix)->const ManifestRow& {
    return manifest_find(manifest,std::string(VERSION)+"."+phase+suffix);
  };
  CompareFile rows(std::string(VERSION)+"."+phase+".rows.tsv",row_for(".rows.tsv"));
  CompareFile scores(std::string(VERSION)+"."+phase+".scores.tsv",row_for(".scores.tsv"));
  CompareFile certificates(std::string(VERSION)+"."+phase+".certificates.tsv",
                           row_for(".certificates.tsv"));
  CompareFile controls(std::string(VERSION)+"."+phase+".controls.json",
                       row_for(".controls.json"));
  CompareFile diagnostic(std::string(VERSION)+"."+phase+".diagnostic.tsv",
                         row_for(".diagnostic.tsv"));
  CompareFile summary(std::string(VERSION)+"."+phase+".summary.json",
                      row_for(".summary.json"));
  std::unique_ptr<CompareFile> selection;
  if (phase=="discovery")
    selection=std::make_unique<CompareFile>(
        std::string(VERSION)+".discovery.selection.tsv",
        row_for(".selection.tsv"));
  EvaluationResult result=evaluate_phase_to_sinks(
      inputs,carry,grammar,rows,scores,certificates,controls,diagnostic,
      selection.get(),summary);
  return replay_pass_status(mode,inputs,manifest_hash,result);
}

bool deterministic_prime_u64(u64 n) {
  if (n==2||n==3) return true;
  if (n<2||(n&1)==0) return false;
  u64 d=n-1;
  unsigned s=0;
  while ((d&1)==0) { d>>=1; ++s; }
  const std::array<u64,7> bases{{2,325,9375,28178,450775,9780504,1795265022}};
  for (u64 raw:bases) {
    const u64 a=raw%n;
    if (a==0) continue;
    cpp_int x=mod_power(a,d,n,nullptr);
    if (x==1||x==n-1) continue;
    bool pass=false;
    for (unsigned i=1;i<s;++i) {
      x=canonical_mod(x*x,n);
      if (x==n-1) { pass=true; break; }
    }
    if (!pass) return false;
  }
  return true;
}

std::string repeat_field(const std::string& value, int count) {
  std::string result;
  for (int i=0;i<count;++i) {
    if (!result.empty()) result.push_back('\t');
    result+=value;
  }
  return result;
}

struct BenchmarkVector {
  cpp_int rho0,rho1,n,b,x,d,r,u,k,t,eta,v,e,eg,f161,f162;
  Pair power,large;
  cpp_int f;
  cpp_int r_block,m,l,u_control,v_control,w_control,f_uniform;
  cpp_int inv2,inv4;
  Matrix matrix,matrix_powered;
  cpp_int normalized;
  std::array<std::string,6> records;
  std::array<std::string,4> stream_hashes;
};

BenchmarkVector make_benchmark_vector() {
  BenchmarkVector v;
  v.rho0=parse_cpp_uint("72057594036927911","benchmark rho0");
  v.rho1=parse_cpp_uint("72057594037927931","benchmark rho1");
  v.n=parse_cpp_uint("5192296858462767872764747260382141","benchmark N0");
  v.b=parse_cpp_uint("72057594037427920","benchmark B0");
  v.x=parse_cpp_uint("72057594037427920","benchmark x0");
  v.d=parse_cpp_uint("72057594037427921","benchmark d0");
  v.r=parse_cpp_uint("72057344027427821","benchmark r0");
  v.u=parse_cpp_uint("4509779229051360486714317898580055","benchmark u0");
  v.k=parse_cpp_uint("62585759201298139","benchmark k0");
  v.t=v.x; v.eta=v.d; v.v=v.r;
  v.e=parse_cpp_uint("72057594037927935","benchmark E0");
  v.eg=parse_cpp_uint("1152921504606847216","benchmark EG");
  v.f161=parse_cpp_uint("1983924214061919432247806074196061","benchmark F161");
  v.f162=parse_cpp_uint("3210056809456107725247980776292056","benchmark F162");
  require(deterministic_prime_u64(v.rho0.convert_to<u64>())&&
          deterministic_prime_u64(v.rho1.convert_to<u64>())&&v.rho0!=v.rho1&&
          bit_length(v.rho0)==56&&bit_length(v.rho1)==56&&v.rho0*v.rho1==v.n&&
          integer_sqrt(v.n)==v.b&&v.n/v.x==v.d&&v.n-v.x*v.d==v.r&&
          v.x*v.u==1+v.k*v.n&&gcd_plain(v.f162,v.f161)==1,
          69,"benchmark","literal benchmark setup");
  for (const cpp_int& atom:std::array<cpp_int,5>{{v.x,v.d,v.r,v.u,v.k}})
    require(gcd_plain(atom,v.n)==1,69,"benchmark","benchmark atom gcd");
  require(gcd_plain(v.eta,v.n)==1&&
          gcd_plain(canonical_mod(v.t*v.t-v.eta,v.n),v.n)==1&&
          gcd_plain(canonical_mod(v.v*v.v-v.eta,v.n),v.n)==1,
          69,"benchmark","benchmark invariant gcds");
  v.power=pair_power(v.t,v.eta,v.e,v.n,nullptr);
  require(v.power.p==parse_cpp_uint("546235288075814104597900157766191","P0")&&
          v.power.q==parse_cpp_uint("2050355986842150267503452025035379","Q0"),
          69,"benchmark","benchmark source power");
  v.f=canonical_mod(v.power.p-v.v*v.power.q,v.n);
  require(v.f==parse_cpp_uint("289765957888600935550152132631336","F0")&&
          gcd_plain(v.f,v.n)==1&&gcd_plain(v.power.p,v.n)==1&&
          gcd_plain(v.power.q,v.n)==1,69,"benchmark","benchmark endpoint");
  const auto source=pair_chain(v.t,v.eta,v.n,256,nullptr);
  const auto target=pair_chain(v.v,v.eta,v.n,16,nullptr);
  for (int m0=2;m0<=16;++m0)
    require(gcd_plain(source[static_cast<std::size_t>(m0)].q,v.n)==1,
            69,"benchmark","source order setup");
  for (int e0=-16;e0<=16;++e0) if (e0!=0) {
    const Pair& p=source[static_cast<std::size_t>(e0<0?-e0:e0)];
    require(gcd_plain(canonical_mod(p.p+(e0<0?v.v*p.q:-v.v*p.q),v.n),v.n)==1,
            69,"benchmark","orbit setup");
  }
  for (int m0=2;m0<=16;++m0)
    require(gcd_plain(target[static_cast<std::size_t>(m0)].q,v.n)==1,
            69,"benchmark","target torsion setup");
  for (int e0=-16;e0<=16;++e0) for (int m0=2;m0<=16;++m0) {
    const int exponent=e0*m0;
    const Pair& sp=source[static_cast<std::size_t>(exponent<0?-exponent:exponent)];
    const cpp_int sq=exponent<0?-sp.q:sp.q;
    const cpp_int determinant=canonical_mod(
        target[static_cast<std::size_t>(m0)].p*sq-
        target[static_cast<std::size_t>(m0)].q*sp.p,v.n);
    require(gcd_plain(determinant,v.n)==1,69,"benchmark","mixed setup");
  }
  v.r_block=v.n*v.n-1;
  v.m=v.n*v.n;
  v.l=((cpp_int(1)<<256)/v.m)*v.m;
  v.u_control=v.r_block%v.m;
  v.v_control=v.u_control/v.n;
  v.w_control=v.u_control%v.n;
  require(v.r_block==parse_cpp_uint("26959946666402328507693636050555806496420540967009894165513351743880","R0")&&
          ((cpp_int(1)<<256)/v.m)==4294967296ULL&&
          v.l==parse_cpp_uint("115792089234102222918792651224463791525030564515935710349301056791313463115776","L0")&&
          v.v_control==v.n-1&&v.w_control==v.n-1,
          69,"benchmark","control reduction setup");
  v.f_uniform=canonical_mod(v.w_control*v.power.p-v.v_control*v.power.q,v.n);
  require(v.f_uniform==parse_cpp_uint("1504120698766336162905551867269188","uniform F")&&
          gcd_plain(v.f_uniform,v.n)==1,69,"benchmark","uniform endpoint setup");
  v.large=pair_power(v.t,v.eta,v.eg,v.n,nullptr);
  require(v.large.p==parse_cpp_uint("3440831553615722869918064737449083","PG")&&
          v.large.q==parse_cpp_uint("462075355879171003448010482325851","QG")&&
          gcd_plain(v.large.q,v.n)==1,69,"benchmark","large order setup");
  v.inv2=inverse_owned(2,v.n,nullptr);
  v.inv4=canonical_mod(v.inv2*v.inv2,v.n);
  v.matrix={{canonical_mod((v.t-v.v)*v.inv2,v.n),1,
             canonical_mod((v.eta-v.v*v.v)*v.inv4,v.n),
             canonical_mod((v.t+v.v)*v.inv2,v.n)}};
  v.matrix_powered=matrix_power(v.matrix,v.e,v.n,nullptr);
  v.normalized=canonical_mod(mod_power(v.inv2,v.e,v.n,nullptr)*v.f,v.n);
  const std::array<cpp_int,4> matrix_expected{{
    parse_cpp_uint("2596148429231383936382498635191120","C00"),1,
    parse_cpp_uint("3894231651390995924107362428537111","C10"),
    parse_cpp_uint("2596148429231384008439842662618941","C11")}};
  const std::array<cpp_int,4> powered_expected{{
    parse_cpp_uint("4662747449486028399575507469426950","CE00"),
    parse_cpp_uint("3368742099563065922611141661159379","CE01"),
    parse_cpp_uint("242639670993409867463953164383354","CE10"),
    parse_cpp_uint("3459505105645858071340362456319990","CE11")}};
  require(v.inv2==parse_cpp_uint("2596148429231383936382373630191071","inv2")&&
          v.inv4==parse_cpp_uint("3894222643847075904573560445286606","inv4")&&
          v.matrix.x==matrix_expected&&v.matrix_powered.x==powered_expected&&
          v.normalized==powered_expected[0],69,"benchmark","matrix setup");

  const std::string U="5192296858462767872764747260382140";
  const std::string H(64,'f');
  const std::string MASK=std::string(138,'f')+"fe";
  const std::string U64="18446744073709551615";
  v.records[0]=tsv({"discovery","d1023","s8-t09-e09-d8-v09",
      "raw_proper_hit",U,U,"registered_global_powered_collision","-"});
  v.records[1]=tsv({"discovery","d1023","s8-t09-e09","1","2","accept",
      U,U,"1","1",U,U});
  v.records[2]=tsv({"discovery","d1023","12656","112",U,U,"saturated"});
  std::vector<std::string> cert{"d1023-s8-t09-e09-d8-v09","discovery","d1023","128",
      "s8-t09-e09-d8-v09","5192296858462767872764747260382141",
      "72057594037427920","-4","-4"};
  for (int i=0;i<5;++i) cert.push_back(U);
  for (int i=0;i<5;++i) cert.push_back(U);
  for (int i=0;i<14;++i) cert.push_back(U);
  cert.insert(cert.end(),{MASK,"mx-16-16","131072",U64,U64,U64,
      "direct_registered_mixed_phase","direct_registered_mixed_phase:mx-16-16"});
  v.records[3]=tsv(cert);
  v.records[4]=tsv({"d1023-s8-t09-e09-d8-v09","d1023","72057594036927911",
      "72057594037927931","four_capacity_at_most_32","72057594037927931",
      "-1","-1","1","1","1","pass"});
  std::vector<std::string> diag{"discovery","d1023",
      "5192296858462767872764747260382141","72057594037427920","112","12656",
      "retained","12656","112","-",U,"12655","1417360",H,"d8-v09",
      "raw_proper_hit"};
  for (int i=0;i<9;++i) diag.push_back(U);
  diag.insert(diag.end(),{"direct_registered_mixed_phase","mx-16-16"});
  v.records[5]=tsv(diag);
  const std::array<u64,6> lengths{{157,182,106,1250,126,590}};
  const std::array<std::string,6> record_hashes{{
    "bb011cf26654ebdf59ed90d770ea6a306e9e88edb9023c6a4c5f9508d287f9b9",
    "a87e69e0ecd6b6c4c8b1ff36ad9212dafa1f0aae50bd22a152c0df56af79e2ca",
    "c010dc158dd962b1c72bfe9fab1f863cd72b78bf53d438fb35770281c0feac54",
    "859d89a35ebe484a12542fd29b76e563da70283eed8e78499ba1c98a1aefd560",
    "0c2bc7c953e25f4c88e9545c03dcb3408f28273a5554bea7ee49005faee24711",
    "94670d6c313a08cbea3a7a6ae68ac909afc36b5a1a2bc6833d2f6c6c2737f3a0"}};
  for (std::size_t i=0;i<6;++i)
    require(v.records[i].size()==lengths[i]&&sha256(v.records[i])==record_hashes[i],
            69,"benchmark","benchmark record template");
  const std::array<std::string,4> headers{{endpoint_header(),control_header(),
                                          diagnostic_scan_header(),diagnostic_header()}};
  const std::array<int,4> record_index{{0,1,2,5}};
  const std::array<u64,4> stream_bytes{{643145,745569,434221,2416857}};
  const std::array<std::string,4> stream_expected{{
    "5a4be2abe995b7f7fb9cc35dbe3b1774445eea7fc7d014f313554c36565a52bb",
    "70cb3b4008af755192441d6ea78740adf61a8bc1d3742d416e0ae6137359cddd",
    "903196bd252c60208fedfbea3c14822955c8c1bb4bdfa798a8243d46894754e6",
    "d7e38f17f2aeddf5cb55ad248f4703705df0f7e76f4799884e435cccecf35ffe"}};
  for (int stream=0;stream<4;++stream) {
    Sha256 hash;
    hash.update(headers[static_cast<std::size_t>(stream)]);
    u64 bytes=headers[static_cast<std::size_t>(stream)].size();
    for (int i=0;i<4096;++i) {
      hash.update(v.records[static_cast<std::size_t>(record_index[stream])]);
      bytes+=v.records[static_cast<std::size_t>(record_index[stream])].size();
    }
    v.stream_hashes[static_cast<std::size_t>(stream)]=hash.final_hex();
    require(bytes==stream_bytes[static_cast<std::size_t>(stream)]&&
            v.stream_hashes[static_cast<std::size_t>(stream)]==
                stream_expected[static_cast<std::size_t>(stream)],
            69,"benchmark","benchmark streaming preimage");
  }
  return v;
}
