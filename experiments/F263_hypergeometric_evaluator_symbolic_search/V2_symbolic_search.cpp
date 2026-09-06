#include <boost/multiprecision/cpp_int.hpp>
#include <boost/multiprecision/cpp_int/serialize.hpp>
#include <algorithm>
#include <array>
#include <atomic>
#include <chrono>
#include <cstdint>
#include <filesystem>
#include <fstream>
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
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>

using boost::multiprecision::cpp_int;
using boost::multiprecision::uint128_t;
using boost::multiprecision::uint256_t;
namespace fs = std::filesystem;

static constexpr uint64_t SEED = 0x8f3f73b5cf1c9d27ULL;
static constexpr uint64_t P1 = 1000000007ULL;
static constexpr uint64_t P2 = 1000000009ULL;

[[noreturn]] static void fail(const std::string &s) { throw std::runtime_error(s); }

static uint64_t splitmix64(uint64_t x) {
    x += 0x9e3779b97f4a7c15ULL;
    x = (x ^ (x >> 30)) * 0xbf58476d1ce4e5b9ULL;
    x = (x ^ (x >> 27)) * 0x94d049bb133111ebULL;
    return x ^ (x >> 31);
}

static uint64_t mix(uint64_t a, uint64_t b) {
    return splitmix64(a ^ splitmix64(b + 0x6a09e667f3bcc909ULL));
}

static std::string s128(const uint128_t &x) { return x.convert_to<std::string>(); }

static uint64_t literal_hash(const std::string &s) {
    uint64_t h = 1469598103934665603ULL;
    for (unsigned char c : s) { h ^= c; h *= 1099511628211ULL; }
    return h;
}

static uint32_t rotr32(uint32_t x,unsigned r){return (x>>r)|(x<<(32-r));}

static std::string sha256_bytes(const std::string&s){
    static const uint32_t k[64]={
        0x428a2f98,0x71374491,0xb5c0fbcf,0xe9b5dba5,0x3956c25b,0x59f111f1,0x923f82a4,0xab1c5ed5,
        0xd807aa98,0x12835b01,0x243185be,0x550c7dc3,0x72be5d74,0x80deb1fe,0x9bdc06a7,0xc19bf174,
        0xe49b69c1,0xefbe4786,0x0fc19dc6,0x240ca1cc,0x2de92c6f,0x4a7484aa,0x5cb0a9dc,0x76f988da,
        0x983e5152,0xa831c66d,0xb00327c8,0xbf597fc7,0xc6e00bf3,0xd5a79147,0x06ca6351,0x14292967,
        0x27b70a85,0x2e1b2138,0x4d2c6dfc,0x53380d13,0x650a7354,0x766a0abb,0x81c2c92e,0x92722c85,
        0xa2bfe8a1,0xa81a664b,0xc24b8b70,0xc76c51a3,0xd192e819,0xd6990624,0xf40e3585,0x106aa070,
        0x19a4c116,0x1e376c08,0x2748774c,0x34b0bcb5,0x391c0cb3,0x4ed8aa4a,0x5b9cca4f,0x682e6ff3,
        0x748f82ee,0x78a5636f,0x84c87814,0x8cc70208,0x90befffa,0xa4506ceb,0xbef9a3f7,0xc67178f2};
    std::vector<uint8_t>b(s.begin(),s.end());uint64_t bits=uint64_t(b.size())*8;b.push_back(0x80);
    while((b.size()%64)!=56)b.push_back(0);for(int i=7;i>=0;--i)b.push_back(uint8_t(bits>>(8*i)));
    uint32_t h[8]={0x6a09e667,0xbb67ae85,0x3c6ef372,0xa54ff53a,0x510e527f,0x9b05688c,0x1f83d9ab,0x5be0cd19};
    for(size_t off=0;off<b.size();off+=64){uint32_t w[64];
        for(int i=0;i<16;++i)w[i]=(uint32_t(b[off+4*i])<<24)|(uint32_t(b[off+4*i+1])<<16)|(uint32_t(b[off+4*i+2])<<8)|b[off+4*i+3];
        for(int i=16;i<64;++i){uint32_t s0=rotr32(w[i-15],7)^rotr32(w[i-15],18)^(w[i-15]>>3);uint32_t s1=rotr32(w[i-2],17)^rotr32(w[i-2],19)^(w[i-2]>>10);w[i]=w[i-16]+s0+w[i-7]+s1;}
        uint32_t a=h[0],c=h[2],d=h[3],e=h[4],f=h[5],g=h[6],hh=h[7],bb=h[1];
        for(int i=0;i<64;++i){uint32_t s1=rotr32(e,6)^rotr32(e,11)^rotr32(e,25),ch=(e&f)^((~e)&g);uint32_t t1=hh+s1+ch+k[i]+w[i];uint32_t s0=rotr32(a,2)^rotr32(a,13)^rotr32(a,22),maj=(a&bb)^(a&c)^(bb&c);uint32_t t2=s0+maj;hh=g;g=f;f=e;e=d+t1;d=c;c=bb;bb=a;a=t1+t2;}
        h[0]+=a;h[1]+=bb;h[2]+=c;h[3]+=d;h[4]+=e;h[5]+=f;h[6]+=g;h[7]+=hh;
    }
    std::ostringstream o;o<<std::hex<<std::setfill('0');for(uint32_t x:h)o<<std::setw(8)<<x;return o.str();
}

static std::string read_binary(const fs::path&p){
    std::ifstream f(p,std::ios::binary);if(!f)fail("cannot read "+p.string());
    std::ostringstream o;o<<f.rdbuf();return o.str();
}

static uint64_t low64(const uint128_t &x) {
    static const uint128_t mask = (uint128_t(1) << 64) - 1;
    return (x & mask).convert_to<uint64_t>();
}

static uint64_t high64(const uint128_t &x) { return (x >> 64).convert_to<uint64_t>(); }

static unsigned bitlen(const uint128_t &x) {
    if (x == 0) return 0;
    return boost::multiprecision::msb(x) + 1;
}

static uint128_t addm(const uint128_t &a, const uint128_t &b, const uint128_t &n) {
    uint128_t z = a + b;
    if (z >= n) z -= n;
    return z;
}

static uint128_t subm(const uint128_t &a, const uint128_t &b, const uint128_t &n) {
    return a >= b ? a - b : n - (b - a);
}

static uint128_t mulm(const uint128_t &a, const uint128_t &b, const uint128_t &n) {
    return uint128_t((uint256_t(a) * uint256_t(b)) % uint256_t(n));
}

static uint128_t gcd128(uint128_t a, uint128_t b) {
    while (b != 0) {
        uint128_t r = a % b;
        a = b;
        b = r;
    }
    return a;
}

static uint64_t isqrt128(const uint128_t &n) {
    const unsigned e = (bitlen(n) + 1) / 2;
    if (e >= 64) fail("isqrt input outside frozen range");
    uint64_t lo = 0, hi = uint64_t(1) << e;
    while (lo + 1 < hi) {
        uint64_t md = lo + (hi - lo) / 2;
        uint128_t sq = uint128_t(md) * uint128_t(md);
        if (sq <= n) lo = md;
        else hi = md;
    }
    return lo;
}

static uint64_t mulmod64(uint64_t a, uint64_t b, uint64_t m) {
    return uint64_t((static_cast<unsigned __int128>(a) * b) % m);
}

static uint64_t powmod64(uint64_t a, uint64_t e, uint64_t m) {
    uint64_t r = 1;
    while (e) {
        if (e & 1) r = mulmod64(r, a, m);
        a = mulmod64(a, a, m);
        e >>= 1;
    }
    return r;
}

static bool prime64(uint64_t n) {
    if (n < 2) return false;
    for (uint64_t p : {2ULL, 3ULL, 5ULL, 7ULL, 11ULL, 13ULL, 17ULL, 19ULL,
                       23ULL, 29ULL, 31ULL, 37ULL}) {
        if (n % p == 0) return n == p;
    }
    uint64_t d = n - 1, s = 0;
    while ((d & 1) == 0) { d >>= 1; ++s; }
    for (uint64_t a : {2ULL, 325ULL, 9375ULL, 28178ULL, 450775ULL,
                       9780504ULL, 1795265022ULL}) {
        if (a % n == 0) continue;
        uint64_t x = powmod64(a % n, d, n);
        if (x == 1 || x == n - 1) continue;
        bool witness = true;
        for (uint64_t r = 1; r < s; ++r) {
            x = mulmod64(x, x, n);
            if (x == n - 1) { witness = false; break; }
        }
        if (witness) return false;
    }
    return true;
}

static uint64_t next_prime(uint64_t n) {
    if (n < 2) return 2;
    n += (n & 1) ? 2 : 1;
    while (!prime64(n)) n += 2;
    return n;
}

static uint64_t modpowp(uint64_t a, uint64_t e, uint64_t p) {
    uint64_t r = 1;
    while (e) {
        if (e & 1) r = mulmod64(r, a, p);
        a = mulmod64(a, a, p);
        e >>= 1;
    }
    return r;
}

static uint64_t invp(uint64_t a, uint64_t p) {
    if (!a) fail("zero modular inverse");
    return modpowp(a, p - 2, p);
}

static uint64_t cpp_mod(const cpp_int &x, uint64_t p) {
    cpp_int r = x % p;
    if (r < 0) r += p;
    return r.convert_to<uint64_t>();
}

static cpp_int gcd_cpp(cpp_int a, cpp_int b) {
    if (a < 0) a = -a;
    if (b < 0) b = -b;
    while (b != 0) {
        cpp_int r = a % b;
        a = b;
        b = r;
    }
    return a;
}

struct ETri { cpp_int a = 1, b = 0, d = 1; };
struct EState {
    std::array<cpp_int, 3> u{cpp_int(1), cpp_int(0), cpp_int(0)};
    std::array<cpp_int, 3> v{cpp_int(1), cpp_int(0), cpp_int(0)};
    std::array<ETri, 3> fwd, rev;
    cpp_int ured = 1, vred = 1;
};

static ETri emul(const ETri &x, const ETri &y) {
    return {x.a * y.a, x.a * y.b + x.b * y.d, x.d * y.d};
}

static EState exact_state(int64_t alpha, int64_t beta, int64_t gamma,
                          int64_t delta, int64_t start, int64_t len,
                          uint64_t tag) {
    EState z;
    for (int64_t j = 0; j < len; ++j) {
        int64_t k = start + j;
        cpp_int u = cpp_int(alpha) * k + beta;
        cpp_int v = cpp_int(gamma) * k + delta;
        z.u[2] = z.u[2] * u + z.u[1];
        z.u[1] = z.u[1] * u + z.u[0];
        z.u[0] *= u;
        z.v[2] = z.v[2] * v + z.v[1];
        z.v[1] = z.v[1] * v + z.v[0];
        z.v[0] *= v;
        std::array<cpp_int, 3> w{cpp_int(1), cpp_int(k + 1),
            cpp_int(splitmix64(tag ^ uint64_t(k)) % 1000003ULL + 1)};
        for (size_t h = 0; h < 3; ++h) {
            ETri t{u, w[h], v};
            z.fwd[h] = emul(z.fwd[h], t);
            z.rev[h] = emul(t, z.rev[h]);
        }
    }
    cpp_int g = gcd_cpp(z.u[0], z.v[0]);
    if (g == 0) g = 1;
    z.ured = z.u[0] / g;
    z.vred = z.v[0] / g;
    return z;
}

enum class DepClass { Descriptor, ShortScan, RecursiveMerge, OracleBlock, FullScan };

static const char *dep_name(DepClass c) {
    switch (c) {
        case DepClass::Descriptor: return "descriptor";
        case DepClass::ShortScan: return "short_scan";
        case DepClass::RecursiveMerge: return "recursive_merge";
        case DepClass::OracleBlock: return "oracle_block";
        case DepClass::FullScan: return "full_scan";
    }
    fail("unknown dependency class");
}

struct DepMeta {
    DepClass cls = DepClass::Descriptor;
    bool parent_target = false;
    uint64_t exact_source_nodes = 0;
    std::vector<std::string> dag;
};

struct FeatureRow {
    std::vector<std::string> names;
    std::vector<cpp_int> x;
    std::vector<DepMeta> dep;
};

static DepMeta descriptor_meta() {
    return {DepClass::Descriptor, false, 1, {"public_descriptor"}};
}

static DepMeta parent_meta(uint64_t nodes) {
    return {DepClass::OracleBlock, true, nodes, {"parent_block", "source_leaves"}};
}

static DepMeta merge_meta(uint64_t nodes) {
    return {DepClass::RecursiveMerge, false, nodes,
            {"left_block", "right_block", "source_leaves"}};
}

static DepMeta full_meta(uint64_t nodes, bool target) {
    return {DepClass::FullScan, target, nodes, {"full_block", "source_leaves"}};
}

static void push_feature(FeatureRow &r, const std::string &name, const cpp_int &x,
                         const DepMeta &dep) {
    r.names.push_back(name);
    r.x.push_back(x);
    r.dep.push_back(dep);
}

static FeatureRow feature_row(uint64_t id, bool holdout) {
    uint64_t h = splitmix64(SEED ^ id ^ (holdout ? 0xb7e151628aed2a6bULL : 0));
    int64_t alpha = 1 + int64_t(h % 5); h = splitmix64(h);
    int64_t beta = 2 + int64_t(h % 11); h = splitmix64(h);
    int64_t gamma = 1 + int64_t(h % 5); h = splitmix64(h);
    int64_t delta = 2 + int64_t(h % 11); h = splitmix64(h);
    int64_t start = 1 + int64_t(h % 7); h = splitmix64(h);
    int64_t m = 2 + int64_t(h % 6);
    EState l = exact_state(alpha, beta, gamma, delta, start, m, id);
    EState rr = exact_state(alpha, beta, gamma, delta, start + m, m, id);
    EState p = exact_state(alpha, beta, gamma, delta, start, 2 * m, id);
    FeatureRow out;
    push_feature(out, "one", 1, descriptor_meta());
    const std::array<std::string, 6> dn{"s","m","alpha","beta","gamma","delta"};
    const std::array<cpp_int, 6> dv{cpp_int(start),cpp_int(m),cpp_int(alpha),
        cpp_int(beta),cpp_int(gamma),cpp_int(delta)};
    for (size_t i = 0; i < dv.size(); ++i)
        push_feature(out, dn[i], dv[i], descriptor_meta());
    for (size_t i = 0; i < dv.size(); ++i)
        for (size_t j = i; j < dv.size(); ++j)
            push_feature(out, dn[i] + "*" + dn[j], dv[i] * dv[j], descriptor_meta());
    auto jets = [&](char which, const std::array<cpp_int,3> &pp,
                    const std::array<cpp_int,3> &ll,
                    const std::array<cpp_int,3> &r0) {
        std::string q(1, which);
        push_feature(out, "P."+q+"0", pp[0], parent_meta(uint64_t(2*m)));
        push_feature(out, "L."+q+"0*R."+q+"0", ll[0]*r0[0], merge_meta(uint64_t(2*m)));
        push_feature(out, "P."+q+"1", pp[1], parent_meta(uint64_t(2*m)));
        push_feature(out, "L."+q+"1*R."+q+"0", ll[1]*r0[0], merge_meta(uint64_t(2*m)));
        push_feature(out, "L."+q+"0*R."+q+"1", ll[0]*r0[1], merge_meta(uint64_t(2*m)));
        push_feature(out, "P."+q+"2", pp[2], parent_meta(uint64_t(2*m)));
        push_feature(out, "L."+q+"2*R."+q+"0", ll[2]*r0[0], merge_meta(uint64_t(2*m)));
        push_feature(out, "L."+q+"1*R."+q+"1", ll[1]*r0[1], merge_meta(uint64_t(2*m)));
        push_feature(out, "L."+q+"0*R."+q+"2", ll[0]*r0[2], merge_meta(uint64_t(2*m)));
    };
    jets('u', p.u, l.u, rr.u);
    jets('v', p.v, l.v, rr.v);
    for (size_t w = 0; w < 3; ++w) {
        std::string z = std::to_string(w);
        push_feature(out, "P.f"+z+".b", p.fwd[w].b, parent_meta(uint64_t(2*m)));
        push_feature(out, "L.f"+z+".a*R.f"+z+".b", l.fwd[w].a*rr.fwd[w].b,
                     merge_meta(uint64_t(2*m)));
        push_feature(out, "L.f"+z+".b*R.f"+z+".d", l.fwd[w].b*rr.fwd[w].d,
                     merge_meta(uint64_t(2*m)));
        push_feature(out, "P.r"+z+".b", p.rev[w].b, parent_meta(uint64_t(2*m)));
        push_feature(out, "R.r"+z+".a*L.r"+z+".b", rr.rev[w].a*l.rev[w].b,
                     merge_meta(uint64_t(2*m)));
        push_feature(out, "R.r"+z+".b*L.r"+z+".d", rr.rev[w].b*l.rev[w].d,
                     merge_meta(uint64_t(2*m)));
    }
    push_feature(out, "P.ured", p.ured, full_meta(uint64_t(2*m), true));
    push_feature(out, "P.vred", p.vred, full_meta(uint64_t(2*m), true));
    push_feature(out, "L.ured*R.ured", l.ured*rr.ured, full_meta(uint64_t(2*m), false));
    push_feature(out, "L.vred*R.vred", l.vred*rr.vred, full_meta(uint64_t(2*m), false));
    push_feature(out, "P.jetdet01", p.u[0]*p.v[1]-p.u[1]*p.v[0],
                 parent_meta(uint64_t(2*m)));
    push_feature(out, "P.jetdet02", p.u[0]*p.v[2]-p.u[2]*p.v[0],
                 parent_meta(uint64_t(2*m)));
    return out;
}

struct RrefResult { size_t rank = 0; std::vector<size_t> pivots; std::vector<std::vector<uint64_t>> basis; };

static RrefResult rref_nullspace(std::vector<std::vector<uint64_t>> a, uint64_t p) {
    if (a.empty()) return {};
    size_t rows = a.size(), cols = a[0].size(), r = 0;
    std::vector<size_t> piv;
    for (size_t c = 0; c < cols && r < rows; ++c) {
        size_t q = r;
        while (q < rows && a[q][c] == 0) ++q;
        if (q == rows) continue;
        std::swap(a[q], a[r]);
        uint64_t iv = invp(a[r][c], p);
        for (size_t j = c; j < cols; ++j) a[r][j] = mulmod64(a[r][j], iv, p);
        for (size_t i = 0; i < rows; ++i) if (i != r && a[i][c]) {
            uint64_t f = a[i][c];
            for (size_t j = c; j < cols; ++j) {
                uint64_t z = mulmod64(f, a[r][j], p);
                a[i][j] = a[i][j] >= z ? a[i][j] - z : a[i][j] + p - z;
            }
        }
        piv.push_back(c);
        ++r;
    }
    std::vector<bool> isp(cols, false);
    for (size_t c : piv) isp[c] = true;
    std::vector<std::vector<uint64_t>> basis;
    for (size_t f = 0; f < cols; ++f) if (!isp[f]) {
        std::vector<uint64_t> v(cols, 0); v[f] = 1;
        for (size_t i = 0; i < piv.size(); ++i) if (a[i][f]) v[piv[i]] = p - a[i][f];
        basis.push_back(std::move(v));
    }
    return {r, piv, basis};
}

static std::vector<int64_t> primitive(std::vector<int64_t> v) {
    int64_t g = 0;
    for (int64_t x : v) g = std::gcd(g, x < 0 ? -x : x);
    if (g > 1) for (auto &x : v) x /= g;
    for (int64_t x : v) if (x) {
        if (x < 0) for (auto &y : v) y = -y;
        break;
    }
    return v;
}

static std::string coefficient_key(const std::vector<int64_t> &v) {
    std::ostringstream o;
    for (size_t i=0;i<v.size();++i) { if(i)o<<',';o<<v[i]; }
    return o.str();
}

static std::vector<int64_t> rescale_small(const std::vector<uint64_t> &v,
                                           uint64_t p, int64_t cap) {
    size_t first = 0;
    while (first < v.size() && !v[first]) ++first;
    if (first == v.size()) return {};
    uint64_t iv = invp(v[first], p);
    for (int64_t t = 1; t <= cap; ++t) for (int sign : {1,-1}) {
        uint64_t target = sign > 0 ? uint64_t(t) : p - uint64_t(t);
        uint64_t scale = mulmod64(target, iv, p);
        std::vector<int64_t> z(v.size());
        bool ok = true;
        for (size_t i = 0; i < v.size(); ++i) {
            uint64_t q = mulmod64(v[i], scale, p);
            int64_t x;
            if (q <= uint64_t(cap)) x = int64_t(q);
            else if (p-q <= uint64_t(cap)) x = -int64_t(p-q);
            else { ok = false; break; }
            z[i] = x;
        }
        if (ok) return primitive(std::move(z));
    }
    return {};
}

static std::vector<int64_t> normalize_relation(size_t cols,
        const std::vector<std::pair<size_t,int>> &terms) {
    std::vector<int64_t> z(cols, 0);
    for (auto [i,c] : terms) z[i] += c;
    return primitive(std::move(z));
}

static std::string relation_key(const std::vector<int64_t> &v,
                                const std::vector<std::string> &names) {
    std::ostringstream o;
    bool first = true;
    for (size_t i = 0; i < v.size(); ++i) if (v[i]) {
        if (!first) o << ';';
        first = false;
        o << v[i] << '*' << names[i];
    }
    return o.str();
}

static bool exact_relation(const std::vector<int64_t> &v,
                           const std::vector<FeatureRow> &rows) {
    for (const auto &r : rows) {
        cpp_int s = 0;
        for (size_t i = 0; i < v.size(); ++i) if (v[i]) s += cpp_int(v[i]) * r.x[i];
        if (s != 0) return false;
    }
    return true;
}

struct Comb { std::vector<std::pair<size_t,int>> t; };

static std::vector<uint64_t> comb_signature(const Comb &c,
                                             const std::vector<FeatureRow> &rows) {
    std::vector<uint64_t> out;
    out.reserve(2 * rows.size());
    for (const auto &r : rows) {
        uint64_t x1 = 0, x2 = 0;
        for (auto [i,s] : c.t) {
            uint64_t q1 = cpp_mod(r.x[i], P1), q2 = cpp_mod(r.x[i], P2);
            if (s > 0) { x1 += q1; if (x1>=P1) x1-=P1; x2 += q2; if(x2>=P2)x2-=P2; }
            else { x1 = x1>=q1 ? x1-q1 : x1+P1-q1; x2=x2>=q2?x2-q2:x2+P2-q2; }
        }
        out.push_back(x1);
        out.push_back(x2);
    }
    return out;
}

struct ShortcutDecision {
    bool accepted = false;
    std::string target;
    uint64_t expanded_nodes = 0;
    std::string reason;
};

static bool operational_class(DepClass c) {
    return c == DepClass::Descriptor || c == DepClass::ShortScan;
}

static ShortcutDecision classify_shortcut(const std::vector<int64_t> &v,
                                           const FeatureRow &schema) {
    ShortcutDecision out;
    size_t targets = 0;
    for (size_t i = 0; i < v.size(); ++i) if (v[i] && schema.dep[i].parent_target) {
        ++targets;
        out.target = schema.names[i];
        if (v[i] != 1 && v[i] != -1) {
            out.reason = "parent_coefficient_not_unit";
            return out;
        }
    }
    if (targets != 1) {
        out.reason = "parent_target_count=" + std::to_string(targets);
        return out;
    }
    for (size_t i = 0; i < v.size(); ++i) if (v[i] && schema.names[i] != out.target) {
        const auto &d = schema.dep[i];
        if (d.dag.empty()) {
            out.reason = "missing_dependency_dag";
            return out;
        }
        if (!operational_class(d.cls)) {
            out.reason = std::string("nonoperational_") + dep_name(d.cls);
            return out;
        }
        if (std::numeric_limits<uint64_t>::max() - out.expanded_nodes < d.exact_source_nodes) {
            out.reason = "dependency_cost_overflow";
            return out;
        }
        out.expanded_nodes += d.exact_source_nodes;
    }
    out.accepted = true;
    out.reason = "unit_target_operational_dag";
    return out;
}

struct SymbolicReport {
    size_t columns=0, rank1=0, rank2=0, nullity1=0, nullity2=0;
    size_t signed_halves=0, signature_classes=0, exact_rows=0;
    size_t sparse_relations=0, basis_relations1=0, basis_relations2=0;
    size_t controls=0, shortcuts=0;
    size_t adjacent_recurrences=0, dyadic_recurrences=0;
    std::vector<std::string> identities;
    std::vector<std::string> dependency_audit;
    std::vector<std::string> recurrences;
    std::set<std::string> operational_targets;
};

static std::string expected_key(const std::vector<std::string> &names,
                                const std::vector<std::pair<std::string,int>> &terms) {
    std::unordered_map<std::string,size_t> idx;
    for (size_t i=0;i<names.size();++i) idx[names[i]]=i;
    std::vector<std::pair<size_t,int>> z;
    for (auto &q:terms) z.push_back({idx.at(q.first),q.second});
    return relation_key(normalize_relation(names.size(),z),names);
}

static cpp_int affine_product(int64_t a, int64_t b, int64_t s, int64_t len) {
    cpp_int r=1;
    for(int64_t j=0;j<len;++j) r*=cpp_int(a)*(s+j)+b;
    return r;
}

static uint64_t affine_product_mod(int64_t a,int64_t b,int64_t s,int64_t len,
                                   uint64_t prime){
    uint64_t r=1;for(int64_t j=0;j<len;++j){cpp_int z=cpp_int(a)*(s+j)+b;r=mulmod64(r,cpp_mod(z,prime),prime);}return r;
}

struct Recurrence {
    int order=-1, degree=-1;
    std::vector<int64_t> c;
    int64_t height=0;
    DepClass dependency=DepClass::OracleBlock;
    bool unit_target=false;
    size_t auth_p1=0, auth_p2=0, auth_exact=0;
};

static bool recurrence_mod(const std::vector<int64_t> &z, int ord, int deg,
                           int64_t a, int64_t b, int64_t len, int64_t start,
                           uint64_t prime) {
    uint64_t sum=0; size_t k=0;
    for(int i=0;i<=ord;++i){
        uint64_t val=affine_product_mod(a,b,start+i,len,prime),sp=1;
        for(int d=0;d<=deg;++d){
            uint64_t c=z[k]>=0?uint64_t(z[k]):prime-uint64_t(-z[k]);
            sum += mulmod64(c,mulmod64(sp,val,prime),prime);
            if(sum>=prime)sum-=prime;
            ++k;sp=mulmod64(sp,uint64_t(start),prime);
        }
    }
    return sum==0;
}

static bool recurrence_exact(const std::vector<int64_t> &z, int ord, int deg,
                             int64_t a, int64_t b, int64_t len, int64_t start) {
    cpp_int sum=0; size_t k=0;
    for(int i=0;i<=ord;++i){
        cpp_int val=affine_product(a,b,start+i,len),sp=1;
        for(int d=0;d<=deg;++d){sum+=cpp_int(z[k++])*sp*val;sp*=start;}
    }
    return sum==0;
}

static Recurrence guess_adjacent(int64_t a, int64_t b, int64_t len) {
    for (int ord=0;ord<=3;++ord) for(int deg=0;deg<=3;++deg) {
        size_t cols=size_t(ord+1)*size_t(deg+1);
        std::vector<std::vector<uint64_t>> m1,m2;
        for(int64_t s=1;s<=int64_t(cols)+12;++s) {
            std::vector<uint64_t> r1,r2;
            for(int i=0;i<=ord;++i) {
                uint64_t v1=affine_product_mod(a,b,s+i,len,P1);
                uint64_t v2=affine_product_mod(a,b,s+i,len,P2);
                uint64_t sp1=1,sp2=1;
                for(int d=0;d<=deg;++d){
                    r1.push_back(mulmod64(v1,sp1,P1));r2.push_back(mulmod64(v2,sp2,P2));
                    sp1=mulmod64(sp1,uint64_t(s),P1);sp2=mulmod64(sp2,uint64_t(s),P2);
                }
            }
            m1.push_back(std::move(r1));m2.push_back(std::move(r2));
        }
        auto n1=rref_nullspace(m1,P1),n2=rref_nullspace(m2,P2);
        std::map<std::string,std::vector<int64_t>> candidates;
        for(auto &v:n1.basis){auto z=rescale_small(v,P1,4096);if(!z.empty())candidates[coefficient_key(z)]=z;}
        for(auto &v:n2.basis){auto z=rescale_small(v,P2,4096);if(!z.empty())candidates[coefficient_key(z)]=z;}
        for(auto &[key,z]:candidates){
            size_t ap1=0,ap2=0,ae=0;bool ok=true;
            for(int64_t s=1;s<=int64_t(cols)+12;++s){ap1+=recurrence_mod(z,ord,deg,a,b,len,s,P1);ap2+=recurrence_mod(z,ord,deg,a,b,len,s,P2);}
            if(ap1!=m1.size()||ap2!=m2.size())ok=false;
            for(int64_t s=50;s<70&&ok;++s){ok=recurrence_exact(z,ord,deg,a,b,len,s);ae+=ok;}
            if(!ok)continue;
            int64_t height=0;for(int64_t x:z)height=std::max(height,x<0?-x:x);
            bool unit=false;
            size_t base=size_t(ord)*size_t(deg+1);
            if(z[base]==1||z[base]==-1){unit=true;for(int d=1;d<=deg;++d)if(z[base+d])unit=false;}
            return {ord,deg,z,height,DepClass::FullScan,unit,ap1,ap2,ae};
        }
    }
    return {};
}

static std::string recurrence_text(const std::string &name, const Recurrence &r) {
    std::ostringstream o;
    o << name << ":order=" << r.order << ",degree=" << r.degree
      << ",height=" << r.height << ",dependency=" << dep_name(r.dependency)
      << ",unit_target=" << r.unit_target << ",auth=" << r.auth_p1 << '/'
      << r.auth_p2 << '/' << r.auth_exact << ",coeff=";
    for (size_t i=0;i<r.c.size();++i) { if (i) o << ','; o << r.c[i]; }
    return o.str();
}

static std::vector<Recurrence> search_dyadic_recurrence() {
    std::vector<Recurrence> accepted;
    const std::array<std::pair<int64_t,int64_t>,2> affines{{{4,2},{1,1}}};
    for(int ord=0;ord<=3;++ord) for(int deg=0;deg<=3;++deg){
        size_t cols=size_t(ord+1)*size_t(deg+1);
        std::vector<std::vector<uint64_t>> m1,m2;
        for(auto [a,b]:affines)for(int64_t s:{1LL,3LL,7LL,11LL})for(int j=0;j+ord<=15;++j){
            std::vector<uint64_t> r1,r2;
            for(int i=0;i<=ord;++i){
                int len=1<<(j+i);
                uint64_t v1=affine_product_mod(a,b,s,len,P1);
                uint64_t v2=affine_product_mod(a,b,s,len,P2);
                uint64_t jp1=1,jp2=1;
                for(int d=0;d<=deg;++d){
                    r1.push_back(mulmod64(v1,jp1,P1));r2.push_back(mulmod64(v2,jp2,P2));
                    jp1=mulmod64(jp1,uint64_t(j),P1);jp2=mulmod64(jp2,uint64_t(j),P2);
                }
            }
            m1.push_back(std::move(r1));m2.push_back(std::move(r2));
        }
        auto n1=rref_nullspace(m1,P1),n2=rref_nullspace(m2,P2);
        std::map<std::string,std::vector<int64_t>> candidates;
        for(auto &v:n1.basis){auto z=rescale_small(v,P1,4096);if(!z.empty())candidates[coefficient_key(z)]=z;}
        for(auto &v:n2.basis){auto z=rescale_small(v,P2,4096);if(!z.empty())candidates[coefficient_key(z)]=z;}
        for(auto &[key,z]:candidates){
            size_t ap1=0,ap2=0,ae=0;bool ok=true;
            for(size_t row=0;row<m1.size();++row){
                uint64_t s1=0,s2=0;
                for(size_t c=0;c<z.size();++c){
                    uint64_t c1=z[c]>=0?uint64_t(z[c]):P1-uint64_t(-z[c]);
                    uint64_t c2=z[c]>=0?uint64_t(z[c]):P2-uint64_t(-z[c]);
                    s1+=mulmod64(c1,m1[row][c],P1);if(s1>=P1)s1-=P1;
                    s2+=mulmod64(c2,m2[row][c],P2);if(s2>=P2)s2-=P2;
                }
                ap1+=s1==0;ap2+=s2==0;
            }
            if(ap1!=m1.size()||ap2!=m2.size())continue;
            for(auto [a,b]:affines)for(int64_t s:{2LL,5LL,13LL})for(int j=0;j+ord<=9&&ok;++j){
                cpp_int sum=0;size_t q=0;
                for(int i=0;i<=ord;++i){cpp_int val=affine_product(a,b,s,1<<(j+i)),jp=1;
                    for(int d=0;d<=deg;++d){sum+=cpp_int(z[q++])*jp*val;jp*=j;}}
                ok=sum==0;ae+=ok;
            }
            if(!ok)continue;
            int64_t height=0;for(int64_t x:z)height=std::max(height,x<0?-x:x);
            size_t base=size_t(ord)*size_t(deg+1);bool unit=z[base]==1||z[base]==-1;
            for(int d=1;d<=deg&&unit;++d)if(z[base+d])unit=false;
            accepted.push_back({ord,deg,z,height,unit?DepClass::ShortScan:DepClass::OracleBlock,
                                unit,ap1,ap2,ae});
        }
    }
    return accepted;
}

static SymbolicReport symbolic_search() {
    std::vector<FeatureRow> train, hold;
    for(uint64_t i=0;i<128;++i) train.push_back(feature_row(i,false));
    for(uint64_t i=0;i<64;++i) hold.push_back(feature_row(i,true));
    const auto &names=train[0].names;
    const auto &deps=train[0].dep;
    for(auto &r:train) if(r.names!=names||r.dep.size()!=deps.size()) fail("symbolic feature order drift");
    for(auto &r:hold) if(r.names!=names||r.dep.size()!=deps.size()) fail("holdout feature order drift");
    std::vector<std::vector<uint64_t>> m1,m2;
    for(auto &r:train){std::vector<uint64_t>a,b;for(auto &x:r.x){a.push_back(cpp_mod(x,P1));b.push_back(cpp_mod(x,P2));}m1.push_back(a);m2.push_back(b);}
    auto n1=rref_nullspace(m1,P1),n2=rref_nullspace(m2,P2);
    std::vector<FeatureRow> exact_rows=train;exact_rows.insert(exact_rows.end(),hold.begin(),hold.end());
    std::set<std::string> sparse,basis1,basis2;
    std::map<std::vector<uint64_t>,std::vector<Comb>> groups;
    std::vector<Comb> all;
    all.push_back(Comb{});
    for(size_t i=0;i<names.size();++i) for(int s:{1,-1}) all.push_back({{{i,s}}});
    for(size_t i=0;i<names.size();++i) for(size_t j=i+1;j<names.size();++j)
        for(int si:{1,-1}) for(int sj:{1,-1}) all.push_back({{{i,si},{j,sj}}});
    for(auto &c:all)groups[comb_signature(c,train)].push_back(c);
    for(auto &[sig,cls]:groups)for(size_t a=0;a<cls.size();++a)for(size_t b=a+1;b<cls.size();++b){
        std::vector<std::pair<size_t,int>> terms=cls[a].t;
        for(auto [i,s]:cls[b].t)terms.push_back({i,-s});
        auto v=normalize_relation(names.size(),terms);size_t support=0;bool small=true;
        for(auto x:v)if(x){++support;if(x<-1||x>1)small=false;}
        if(!small||support<2||support>4||!exact_relation(v,exact_rows))continue;
        sparse.insert(relation_key(v,names));
    }
    for(auto &v:n1.basis){auto z=rescale_small(v,P1,4096);if(!z.empty()&&exact_relation(z,exact_rows))basis1.insert(relation_key(z,names));}
    for(auto &v:n2.basis){auto z=rescale_small(v,P2,4096);if(!z.empty()&&exact_relation(z,exact_rows))basis2.insert(relation_key(z,names));}
    std::set<std::string> accepted=sparse;accepted.insert(basis1.begin(),basis1.end());accepted.insert(basis2.begin(),basis2.end());
    std::set<std::string> expected;
    for(char q:{'u','v'}){
        std::string z(1,q);
        expected.insert(expected_key(names,{{"P."+z+"0",1},{"L."+z+"0*R."+z+"0",-1}}));
        expected.insert(expected_key(names,{{"P."+z+"1",1},{"L."+z+"1*R."+z+"0",-1},{"L."+z+"0*R."+z+"1",-1}}));
        expected.insert(expected_key(names,{{"P."+z+"2",1},{"L."+z+"2*R."+z+"0",-1},{"L."+z+"1*R."+z+"1",-1},{"L."+z+"0*R."+z+"2",-1}}));
    }
    for(int w=0;w<3;++w){std::string z=std::to_string(w);
        expected.insert(expected_key(names,{{"P.f"+z+".b",1},{"L.f"+z+".a*R.f"+z+".b",-1},{"L.f"+z+".b*R.f"+z+".d",-1}}));
        expected.insert(expected_key(names,{{"P.r"+z+".b",1},{"R.r"+z+".a*L.r"+z+".b",-1},{"R.r"+z+".b*L.r"+z+".d",-1}}));
    }
    size_t controls=0,shortcuts=0;
    for(auto &e:expected) if(accepted.count(e)) ++controls;
    std::vector<std::string> dep_audit;std::set<std::string> operational_targets;
    std::unordered_map<std::string,size_t> name_index;for(size_t i=0;i<names.size();++i)name_index[names[i]]=i;
    for(auto &key:accepted){
        std::vector<int64_t> v(names.size(),0);std::istringstream in(key);std::string term;
        while(std::getline(in,term,';')){size_t star=term.find('*');int64_t c=std::stoll(term.substr(0,star));v[name_index.at(term.substr(star+1))]=c;}
        ShortcutDecision d=classify_shortcut(v,train[0]);if(d.accepted){++shortcuts;operational_targets.insert(d.target);}
        dep_audit.push_back(key+"|target="+d.target+"|accepted="+(d.accepted?"1":"0")+
                            "|nodes="+std::to_string(d.expanded_nodes)+"|reason="+d.reason);
    }
    size_t adjacent=0;
    std::vector<std::string> recurrence_lines;
    size_t recurrence_id=0;
    for(auto t:std::vector<std::tuple<int64_t,int64_t,int64_t>>{{4,2,5},{1,1,7},{1,1009,8},{1,989,8}}){
        Recurrence r=guess_adjacent(std::get<0>(t),std::get<1>(t),std::get<2>(t));
        if(r.order==1&&r.degree==1){++adjacent;recurrence_lines.push_back(recurrence_text("adjacent"+std::to_string(recurrence_id),r));}
        ++recurrence_id;
    }
    SymbolicReport out;
    out.columns=names.size();out.rank1=n1.rank;out.rank2=n2.rank;
    out.nullity1=n1.basis.size();out.nullity2=n2.basis.size();
    out.signed_halves=all.size();out.signature_classes=groups.size();out.exact_rows=exact_rows.size();
    out.sparse_relations=sparse.size();out.basis_relations1=basis1.size();out.basis_relations2=basis2.size();
    out.controls=controls;out.shortcuts=shortcuts;out.adjacent_recurrences=adjacent;
    auto dyadic=search_dyadic_recurrence();out.dyadic_recurrences=dyadic.size();
    for(size_t i=0;i<dyadic.size();++i){recurrence_lines.push_back(recurrence_text("dyadic"+std::to_string(i),dyadic[i]));if(dyadic[i].unit_target){operational_targets.insert("P.u0");operational_targets.insert("P.v0");}}
    for(auto &x:accepted)out.identities.push_back(x);
    out.dependency_audit=std::move(dep_audit);out.operational_targets=std::move(operational_targets);
    out.recurrences=std::move(recurrence_lines);
    return out;
}

struct MTri { uint128_t a=1,b=0,d=1; };
struct MState {
    std::array<uint128_t,3> u{uint128_t(1),uint128_t(0),uint128_t(0)};
    std::array<uint128_t,3> v{uint128_t(1),uint128_t(0),uint128_t(0)};
    std::array<MTri,3> fwd,rev;
};

static MTri mmul(const MTri &x,const MTri &y,const uint128_t &n){
    return {mulm(x.a,y.a,n),addm(mulm(x.a,y.b,n),mulm(x.b,y.d,n),n),mulm(x.d,y.d,n)};
}

enum class Family { Central, Shifted };
struct Query { uint64_t len,start; };
struct Block { Query q; MState s; bool has_adj=false; MState adj; };
struct Witness {
    Family family=Family::Central;
    std::array<Query,2> support{};
    size_t count=0;
};

static Witness one_witness(Family f, Query a) {
    Witness w;w.family=f;w.support[0]=a;w.count=1;return w;
}

static Witness two_witness(Family f, Query a, Query b) {
    Witness w;w.family=f;w.support[0]=a;w.support[1]=b;w.count=2;return w;
}

static uint128_t mod_signed(int64_t x,const uint128_t &n){
    if(x>=0)return uint128_t(uint64_t(x))%n;
    uint128_t q=uint128_t(uint64_t(-x))%n;return q==0?uint128_t(0):n-q;
}

static MState scan_state(Family fam,const uint128_t &n,uint64_t B,uint64_t start,uint64_t len,uint64_t syntax){
    MState z;
    for(uint64_t j=0;j<len;++j){
        uint64_t k=start+j;
        uint128_t u,v;
        if(fam==Family::Central){u=uint128_t(4)*k+2;v=k+1;}
        else {uint64_t c=k;u=uint128_t(c)%n;v=c>=B?uint128_t(c-B)%n:n-(uint128_t(B-c)%n);}
        u%=n;v%=n;
        z.u[2]=addm(mulm(z.u[2],u,n),z.u[1],n);
        z.u[1]=addm(mulm(z.u[1],u,n),z.u[0],n);z.u[0]=mulm(z.u[0],u,n);
        z.v[2]=addm(mulm(z.v[2],v,n),z.v[1],n);
        z.v[1]=addm(mulm(z.v[1],v,n),z.v[0],n);z.v[0]=mulm(z.v[0],v,n);
        std::array<uint128_t,3>w{uint128_t(1),uint128_t(k+1)%n,
            uint128_t(splitmix64(syntax^k)%std::numeric_limits<uint64_t>::max())%n};
        for(size_t h=0;h<3;++h){MTri t{u,w[h],v};z.fwd[h]=mmul(z.fwd[h],t,n);z.rev[h]=mmul(t,z.rev[h],n);}
    }
    return z;
}

static uint128_t det2(uint128_t a,uint128_t b,uint128_t c,uint128_t d,const uint128_t &n){return subm(mulm(a,d,n),mulm(b,c,n),n);}

static uint128_t resultant2(const std::array<uint128_t,3>&f,const std::array<uint128_t,3>&g,const uint128_t&n){
    std::array<std::array<uint128_t,4>,4> a{{
        {{f[2],f[1],f[0],0}},{{0,f[2],f[1],f[0]}},
        {{g[2],g[1],g[0],0}},{{0,g[2],g[1],g[0]}}}};
    std::array<int,4> p{0,1,2,3};uint128_t ans=0;
    do{uint128_t term=1;int inv=0;for(int i=0;i<4;++i){term=mulm(term,a[i][p[i]],n);for(int j=i+1;j<4;++j)if(p[i]>p[j])++inv;}
        ans=(inv&1)?subm(ans,term,n):addm(ans,term,n);
    }while(std::next_permutation(p.begin(),p.end()));
    return ans;
}

struct Catalog {
    std::vector<std::string> names; std::unordered_map<std::string,size_t> idx;
    void add(const std::string &s){if(idx.count(s))fail("duplicate candidate "+s);idx[s]=names.size();names.push_back(s);}
};

static Catalog build_catalog(){
    Catalog c;
    for(std::string f:{"central","shifted"}){
        for(std::string x:{"u0","u1","u2","v0","v1","v2","jet_det01","jet_det02","jet_det12","jet_resultant"})c.add(f+"."+x);
        for(std::string o:{"f","r"})for(int w=0;w<3;++w)c.add(f+".transfer_"+o+std::to_string(w));
        for(std::string x:{"transfer_det01","transfer_det02","transfer_det12"})c.add(f+"."+x);
        for(int i=0;i<16;++i)c.add(f+".projection"+(i<10?"0":"")+std::to_string(i));
        for(int i=0;i<8;++i)c.add(f+".product_hash"+(i<10?"0":"")+std::to_string(i));
        for(std::string x:{"adj_du0","adj_du1","adj_du2","adj_dv0","adj_dv1","adj_dv2",
                           "adj_u_det01","adj_u_det02","adj_u_det12","adj_v_det01","adj_v_det02","adj_v_det12",
                           "adj_resultant_u","adj_resultant_v","smith_d1","smith_d2"})c.add(f+"."+x);
        for(int i=0;i<8;++i)c.add(f+".pair_projection_diff"+(i<10?"0":"")+std::to_string(i));
        for(std::string x:{"pair_u_det01","pair_u_det02","pair_u_det12","pair_transfer_det0","pair_transfer_det1","pair_transfer_det2","pair_resultant"})c.add(f+"."+x);
    }
    return c;
}

struct Eval {
    const Catalog &cat; const uint128_t &n; std::vector<uint8_t> status;
    std::string first_name,first_divisor,first_block; uint64_t first_leaf=0;
    Witness first_witness;std::vector<std::vector<Witness>> proper_witnesses;
    Eval(const Catalog&c,const uint128_t&nn):cat(c),n(nn),status(c.names.size(),0),proper_witnesses(c.names.size()){}
    void divisor(const std::string&name,uint128_t d,const std::string&block,uint64_t leaf,
                 const Witness&w){
        size_t i=cat.idx.at(name);uint8_t s=(d>1&&d<n)?1:(d==n?2:0);if(s==1||status[i]==0)status[i]=s;
        if(s==1){proper_witnesses[i].push_back(w);if(first_name.empty()){first_name=name;first_divisor=s128(d);first_block=block;first_leaf=leaf;first_witness=w;}}
    }
    void value(const std::string&name,const uint128_t&v,const std::string&block,uint64_t leaf,
               const Witness&w){divisor(name,gcd128(v,n),block,leaf,w);}
};

static std::vector<uint128_t> state_vector(const MState&s){
    std::vector<uint128_t>x{s.u[0],s.u[1],s.u[2],s.v[0],s.v[1],s.v[2]};
    for(int w=0;w<3;++w)x.push_back(s.fwd[w].b);
    for(int w=0;w<3;++w)x.push_back(s.rev[w].b);
    return x;
}

static uint128_t projection(const MState&s,const uint128_t&n,uint64_t seed,const Query&q,bool product){
    auto x=state_vector(s);uint64_t nh=mix(low64(n),high64(n));uint128_t r=product?uint128_t(1):uint128_t(0);
    for(size_t i=0;i<x.size();++i){uint128_t w=uint128_t(splitmix64(seed^nh^mix(q.start,q.len)^i))%n;if(w==0)w=1;
        uint128_t z=mulm(w,x[i],n);if(product)r=mulm(r,addm(1,z,n),n);else r=addm(r,z,n);}
    return r;
}

static void eval_block(Eval&e,Family family,const std::string&f,const Block&b,const uint128_t&n,uint64_t leaf){
    std::string d=std::to_string(b.q.start)+":"+std::to_string(b.q.len);
    Witness base=one_witness(family,b.q);
    for(int i=0;i<3;++i){e.value(f+".u"+std::to_string(i),b.s.u[i],d,leaf,base);e.value(f+".v"+std::to_string(i),b.s.v[i],d,leaf,base);}
    e.value(f+".jet_det01",det2(b.s.u[0],b.s.u[1],b.s.v[0],b.s.v[1],n),d,leaf,base);
    e.value(f+".jet_det02",det2(b.s.u[0],b.s.u[2],b.s.v[0],b.s.v[2],n),d,leaf,base);
    e.value(f+".jet_det12",det2(b.s.u[1],b.s.u[2],b.s.v[1],b.s.v[2],n),d,leaf,base);
    e.value(f+".jet_resultant",resultant2(b.s.u,b.s.v,n),d,leaf,base);
    for(int w=0;w<3;++w){e.value(f+".transfer_f"+std::to_string(w),b.s.fwd[w].b,d,leaf,base);e.value(f+".transfer_r"+std::to_string(w),b.s.rev[w].b,d,leaf,base);}
    e.value(f+".transfer_det01",det2(b.s.fwd[0].a,b.s.fwd[0].b,b.s.fwd[1].a,b.s.fwd[1].b,n),d,leaf,base);
    e.value(f+".transfer_det02",det2(b.s.fwd[0].a,b.s.fwd[0].b,b.s.fwd[2].a,b.s.fwd[2].b,n),d,leaf,base);
    e.value(f+".transfer_det12",det2(b.s.fwd[1].a,b.s.fwd[1].b,b.s.fwd[2].a,b.s.fwd[2].b,n),d,leaf,base);
    for(int i=0;i<16;++i)e.value(f+".projection"+(i<10?"0":"")+std::to_string(i),projection(b.s,n,SEED^uint64_t(i),b.q,false),d,leaf,base);
    for(int i=0;i<8;++i)e.value(f+".product_hash"+(i<10?"0":"")+std::to_string(i),projection(b.s,n,SEED^0x5555^uint64_t(i),b.q,true),d,leaf,base);
    if(!b.has_adj)return;
    Query aq{b.q.len,b.q.start+1};Witness adjacent=two_witness(family,b.q,aq);
    for(int i=0;i<3;++i){e.value(f+".adj_du"+std::to_string(i),subm(b.adj.u[i],b.s.u[i],n),d,leaf,adjacent);e.value(f+".adj_dv"+std::to_string(i),subm(b.adj.v[i],b.s.v[i],n),d,leaf,adjacent);}
    e.value(f+".adj_u_det01",det2(b.s.u[0],b.s.u[1],b.adj.u[0],b.adj.u[1],n),d,leaf,adjacent);
    e.value(f+".adj_u_det02",det2(b.s.u[0],b.s.u[2],b.adj.u[0],b.adj.u[2],n),d,leaf,adjacent);
    e.value(f+".adj_u_det12",det2(b.s.u[1],b.s.u[2],b.adj.u[1],b.adj.u[2],n),d,leaf,adjacent);
    e.value(f+".adj_v_det01",det2(b.s.v[0],b.s.v[1],b.adj.v[0],b.adj.v[1],n),d,leaf,adjacent);
    e.value(f+".adj_v_det02",det2(b.s.v[0],b.s.v[2],b.adj.v[0],b.adj.v[2],n),d,leaf,adjacent);
    e.value(f+".adj_v_det12",det2(b.s.v[1],b.s.v[2],b.adj.v[1],b.adj.v[2],n),d,leaf,adjacent);
    e.value(f+".adj_resultant_u",resultant2(b.s.u,b.adj.u,n),d,leaf,adjacent);
    e.value(f+".adj_resultant_v",resultant2(b.s.v,b.adj.v,n),d,leaf,adjacent);
    auto x=state_vector(b.s),y=state_vector(b.adj);uint128_t g=n;
    for(auto z:x)g=gcd128(g,z);for(auto z:y)g=gcd128(g,z);e.divisor(f+".smith_d1",g,d,leaf,adjacent);
    g=n;for(size_t i=0;i<x.size();++i)for(size_t j=i+1;j<x.size();++j)g=gcd128(g,det2(x[i],x[j],y[i],y[j],n));e.divisor(f+".smith_d2",g,d,leaf,adjacent);
}

static void eval_pair(Eval&e,Family family,const std::string&f,const Block&a,const Block&b,const uint128_t&n,uint64_t leaf){
    std::string d=std::to_string(a.q.start)+","+std::to_string(b.q.start)+":"+std::to_string(a.q.len);
    Witness pair=two_witness(family,a.q,b.q);
    for(int i=0;i<8;++i){uint128_t x=projection(a.s,n,SEED^0x7777^uint64_t(i),a.q,false),y=projection(b.s,n,SEED^0x7777^uint64_t(i),b.q,false);e.value(f+".pair_projection_diff"+(i<10?"0":"")+std::to_string(i),subm(x,y,n),d,leaf,pair);}
    e.value(f+".pair_u_det01",det2(a.s.u[0],a.s.u[1],b.s.u[0],b.s.u[1],n),d,leaf,pair);
    e.value(f+".pair_u_det02",det2(a.s.u[0],a.s.u[2],b.s.u[0],b.s.u[2],n),d,leaf,pair);
    e.value(f+".pair_u_det12",det2(a.s.u[1],a.s.u[2],b.s.u[1],b.s.u[2],n),d,leaf,pair);
    for(int w=0;w<3;++w)e.value(f+".pair_transfer_det"+std::to_string(w),det2(a.s.fwd[w].a,a.s.fwd[w].b,b.s.fwd[w].a,b.s.fwd[w].b,n),d,leaf,pair);
    e.value(f+".pair_resultant",resultant2(a.s.u,b.s.u,n),d,leaf,pair);
}

static std::vector<Query> queries(uint64_t domain,unsigned n,uint64_t salt){
    std::set<uint64_t> ls;uint64_t cap=std::min<uint64_t>(domain,uint64_t(n)*n);
    for(uint64_t x=8;x<=cap&&x;x*=2){ls.insert(x);if(x>cap/2)break;}
    if(std::min<uint64_t>(domain,n)>=8)ls.insert(std::min<uint64_t>(domain,n));
    if(cap>=8)ls.insert(cap);
    std::set<std::pair<uint64_t,uint64_t>> all;
    for(uint64_t l:ls){uint64_t m=domain-l;std::set<uint64_t> ss{0,m,m/2,m/4};
        for(int j=0;j<4;++j)ss.insert(m?splitmix64(salt^l^uint64_t(j))%(m+1):0);
        for(uint64_t s:ss)all.insert({l,s});}
    std::vector<Query> out;for(auto [l,s]:all)out.push_back({l,s});
    std::sort(out.begin(),out.end(),[](auto&a,auto&b){return std::tie(a.len,a.start)<std::tie(b.len,b.start);});return out;
}

struct Labelled { uint64_t p,q; uint128_t n; unsigned bits; std::string cohort; size_t index; };
struct ControlAudit {
    uint64_t central_root_factors=0,shifted_root_factors=0;
    uint64_t tree_factors=0,tree_merges=0,tree_state_words=0;
    uint64_t oracle_calls_central=0,oracle_calls_shifted=0;
    uint64_t recompute_factors_central=0,recompute_factors_shifted=0;
    bool oracle_covers_central=false,oracle_covers_shifted=false;
};
struct RowResult {
    Labelled in; unsigned modulus_bits=0;uint64_t B=0,H=0,queries=0,leaves=0,capacity=0;
    bool odd=false,cleanup=false,central_cover=false,shifted_cover=false;
    bool first_nondirect=false;
    std::string cleanup_divisor,first_name,first_divisor,first_block;uint64_t first_leaf=0;
    std::vector<uint8_t> status,nondirect_status;ControlAudit control;
};

static std::pair<uint64_t,uint64_t> oracle_path_cost(uint64_t domain,uint64_t target) {
    if(domain==0||target>=domain)return {0,0};
    uint64_t calls=0,recomputed=0,start=0,len=domain;
    while(len>1){
        uint64_t left=len/2,right=len-left;++calls;
        if(target<start+left){len=left;}
        else{start+=left;len=right;}
        recomputed+=len;
    }
    return {calls,recomputed};
}

static bool contains(Query q,uint64_t target) {
    return q.start<=target&&target-q.start<q.len;
}

static bool direct_witness(const Witness&w,uint64_t central_index,uint64_t shifted_index) {
    uint64_t target=w.family==Family::Central?central_index:shifted_index;
    for(size_t i=0;i<w.count;++i)if(contains(w.support[i],target))return true;
    return false;
}

static RowResult analyze(const Labelled&in,const Catalog&cat){
    RowResult r;r.in=in;r.modulus_bits=bitlen(in.n);r.B=isqrt128(in.n);r.H=r.B/2;r.odd=r.B&1;
    r.control.central_root_factors=r.H;r.control.shifted_root_factors=r.H? r.H-1:0;
    r.control.tree_factors=r.H;r.control.tree_merges=r.H? r.H-1:0;
    r.control.tree_state_words=r.H?2*r.H-1:0;
    r.capacity=std::gcd(in.p-1,in.q-1);
    uint64_t central_k=(in.p-1)/2,shifted_c=r.B-in.p,shifted_index=shifted_c?shifted_c-1:0;
    auto cp=oracle_path_cost(r.H,central_k);r.control.oracle_calls_central=cp.first;
    r.control.recompute_factors_central=cp.second;r.control.oracle_covers_central=central_k<r.H;
    auto sp=oracle_path_cost(r.H?r.H-1:0,shifted_index);r.control.oracle_calls_shifted=sp.first;
    r.control.recompute_factors_shifted=sp.second;r.control.oracle_covers_shifted=shifted_c>=1&&shifted_index<r.H-1;
    uint128_t d=gcd128(in.n,r.B);if(d>1&&d<in.n){r.cleanup=true;r.cleanup_divisor=s128(d);r.status.assign(cat.names.size(),0);r.nondirect_status.assign(cat.names.size(),0);return r;}
    d=gcd128(in.n,r.H+1);if(d>1&&d<in.n){r.cleanup=true;r.cleanup_divisor=s128(d);r.status.assign(cat.names.size(),0);r.nondirect_status.assign(cat.names.size(),0);return r;}
    Eval e(cat,in.n);std::vector<Query> central_bank,shifted_bank;
    for(auto [fam,name,domain,base,salt]:std::vector<std::tuple<Family,std::string,uint64_t,uint64_t,uint64_t>>{
            {Family::Central,"central",r.H,0,SEED^0x1111},{Family::Shifted,"shifted",r.H>0?r.H-1:0,1,SEED^0x2222}}){
        if(domain<8)continue;auto qs=queries(domain,r.modulus_bits,mix(low64(in.n),salt));
        if(fam==Family::Central)central_bank=qs;else shifted_bank=qs;
        std::map<uint64_t,std::vector<Block>> bylen;
        for(auto q:qs){Block b;b.q=q;uint64_t actual=base+q.start;
            b.s=scan_state(fam,in.n,r.B,actual,q.len,mix(salt,q.start));r.leaves+=q.len;++r.queries;
            if(q.start+q.len<domain){b.has_adj=true;b.adj=scan_state(fam,in.n,r.B,actual+1,q.len,mix(salt,q.start+1));r.leaves+=q.len;++r.queries;}
            eval_block(e,fam,name,b,in.n,r.leaves);bylen[q.len].push_back(std::move(b));
        }
        for(auto &[l,bs]:bylen)if(bs.size()>1)for(size_t i=1;i<bs.size();++i)eval_pair(e,fam,name,bs[0],bs[i],in.n,r.leaves);
    }
    for(Query q:central_bank)r.central_cover|=contains(q,central_k);
    if(shifted_c>=1)for(Query q:shifted_bank)r.shifted_cover|=contains(q,shifted_index);
    r.status=std::move(e.status);r.nondirect_status.assign(cat.names.size(),0);
    for(size_t i=0;i<e.proper_witnesses.size();++i)for(const Witness&w:e.proper_witnesses[i])
        if(!direct_witness(w,central_k,shifted_index)){r.nondirect_status[i]=1;break;}
    r.first_name=e.first_name;r.first_divisor=e.first_divisor;r.first_block=e.first_block;r.first_leaf=e.first_leaf;
    if(!e.first_name.empty())r.first_nondirect=!direct_witness(e.first_witness,central_k,shifted_index);
    return r;
}

static uint64_t exact_bit_candidate(unsigned bits,uint64_t h){
    uint64_t mask=(uint64_t(1)<<bits)-1,top=uint64_t(1)<<(bits-1);return (h&mask)|top|1;
}

static bool find_prime_bounded(unsigned bits,uint64_t seed,uint64_t cap,uint64_t&out){
    for(uint64_t a=0;a<cap;++a){uint64_t x=exact_bit_candidate(bits,splitmix64(seed^a));if(prime64(x)){out=x;return true;}}
    return false;
}

static bool find_safe_bounded(unsigned bits,uint64_t seed,uint64_t cap,uint64_t&out){
    for(uint64_t a=0;a<cap;++a){
        uint64_t r=exact_bit_candidate(bits-1,splitmix64(seed^a));
        if(!prime64(r))continue;uint64_t p=2*r+1;
        if(bitlen(uint128_t(p))==bits&&prime64(p)){out=p;return true;}
    }
    return false;
}

static bool next_prime_bounded(uint64_t p,uint64_t cap,uint64_t&out){
    uint64_t x=p+2;
    for(uint64_t a=0;a<cap;++a,x+=2)if(prime64(x)){out=x;return true;}
    return false;
}

static bool accepts_pair(uint64_t p,uint64_t q,const std::string&cohort){
    if(p==q)return false;if(p>q)std::swap(p,q);
    if(q>=2*p)return false;
    if(cohort=="bounded_capacity"&&std::gcd(p-1,q-1)>16)return false;
    if(cohort=="safe_safe"){
        if(std::gcd(p-1,q-1)!=2||!prime64((p-1)/2)||!prime64((q-1)/2))return false;
    }
    return true;
}

static bool try_make_row(unsigned bits,const std::string&cohort,size_t idx,
                         uint64_t attempt,Labelled&out){
    uint64_t tag=mix(SEED,mix(bits,mix(literal_hash(cohort),mix(idx,attempt)))),p=0,q=0;
    constexpr uint64_t PRIME_CAP=4096,SAFE_CAP=65536,NEXT_CAP=4096;
    if(cohort=="safe_safe"){
        if(!find_safe_bounded(bits,tag,SAFE_CAP,p)||
           !find_safe_bounded(bits,tag^0x123456789abcdef0ULL,SAFE_CAP,q))return false;
    }else if(cohort=="consecutive"){
        if(!find_prime_bounded(bits,tag,PRIME_CAP,p)||!next_prime_bounded(p,NEXT_CAP,q))return false;
        if(bitlen(uint128_t(q))!=bits)return false;
    }else{
        if(!find_prime_bounded(bits,tag,PRIME_CAP,p)||
           !find_prime_bounded(bits,tag^0xabcdef1234567890ULL,PRIME_CAP,q))return false;
    }
    if(p>q)std::swap(p,q);
    if(bitlen(uint128_t(p))!=bits||bitlen(uint128_t(q))!=bits||
       !accepts_pair(p,q,cohort))return false;
    out={p,q,uint128_t(p)*uint128_t(q),bits,cohort,idx};return true;
}

static Labelled make_unique_row(unsigned bits,const std::string&cohort,size_t idx,
                                std::set<std::string>&seen){
    constexpr uint64_t ROW_ATTEMPT_CAP=64;
    for(uint64_t attempt=0;attempt<ROW_ATTEMPT_CAP;++attempt){
        Labelled x;if(!try_make_row(bits,cohort,idx,attempt,x))continue;
        if(seen.insert(s128(x.n)).second)return x;
    }
    fail("row generator cap or global duplicate exhaustion: "+cohort+":"+
         std::to_string(bits)+":"+std::to_string(idx));
}

static size_t expected_cohort_rows(bool heldout){return heldout?1152:848;}

static std::vector<Labelled> cohort_rows(bool heldout){
    std::vector<unsigned> bits=heldout?std::vector<unsigned>{40,48,56,60}:std::vector<unsigned>{16,24,32};
    std::vector<Labelled> out;std::set<std::string> seen;
    for(unsigned b:bits)for(auto [name,count]:std::vector<std::pair<std::string,size_t>>{{"random",128},{"consecutive",64},{"safe_safe",b==16?16UL:32UL},{"bounded_capacity",64}})
        for(size_t i=0;i<count;++i)out.push_back(make_unique_row(b,name,i,seen));
    size_t expected=expected_cohort_rows(heldout);if(out.size()!=expected||seen.size()!=expected)fail("cohort row count or uniqueness drift");
    return out;
}

static std::string bithex(const std::vector<uint8_t>&s,uint8_t want){
    static const char*h="0123456789abcdef";std::string o;for(size_t i=0;i<s.size();i+=4){int z=0;for(size_t j=0;j<4&&i+j<s.size();++j)if(s[i+j]==want)z|=1<<j;o.push_back(h[z]);}return o;
}

struct CStat {
    uint64_t proper=0,saturated=0,hostile=0,nondirect=0;
    std::set<unsigned>sizes,nondirect_sizes;
    bool high=false,nondirect_hostile=false;
};

struct SelectionRow {uint64_t rank=0;std::string name;uint64_t hostile=0,proper=0,sizes=0;};
struct SelectionPacket {std::vector<SelectionRow> rows;std::set<std::string> names;std::string digest;};
static constexpr uint64_t OUTPUT_CAP=1073741824ULL;

static uint64_t directory_bytes(const fs::path&out){
    uint64_t total=0;if(!fs::exists(out))return 0;
    for(auto &e:fs::recursive_directory_iterator(out))if(e.is_regular_file()){
        uint64_t z=e.file_size();if(OUTPUT_CAP-total<z)return OUTPUT_CAP+1;total+=z;
    }
    return total;
}

static void write_bounded(const fs::path&out,const fs::path&path,const std::string&bytes){
    if(fs::exists(path))fail("refuse to overwrite output "+path.string());
    uint64_t used=directory_bytes(out);if(used>OUTPUT_CAP||bytes.size()>OUTPUT_CAP-used)fail("applied output budget exceeded");
    std::ofstream f(path,std::ios::binary);if(!f)fail("cannot create output "+path.string());
    f.write(bytes.data(),std::streamsize(bytes.size()));f.close();if(!f||fs::file_size(path)!=bytes.size())fail("short output write");
}

static uint64_t parse_canonical_u64(const std::string&s,const std::string&field){
    if(s.empty()||(s.size()>1&&s[0]=='0'))fail("noncanonical "+field);
    uint64_t x=0;for(char c:s){if(c<'0'||c>'9')fail("nonnumeric "+field);uint64_t d=uint64_t(c-'0');if(x>(std::numeric_limits<uint64_t>::max()-d)/10)fail("overflow "+field);x=10*x+d;}
    if(std::to_string(x)!=s)fail("noncanonical "+field);return x;
}

static std::vector<std::string> split_tabs(const std::string&s){
    std::vector<std::string>v;size_t p=0;for(;;){size_t q=s.find('\t',p);v.push_back(s.substr(p,q==std::string::npos?q:q-p));if(q==std::string::npos)break;p=q+1;}return v;
}

static SelectionPacket parse_selection_bytes(const std::string&bytes,const std::string&expected,
                                              const Catalog&cat){
    if(expected.size()!=64||!std::all_of(expected.begin(),expected.end(),[](char c){return(c>='0'&&c<='9')||(c>='a'&&c<='f');}))fail("bad expected selection SHA-256");
    std::string observed=sha256_bytes(bytes);if(observed!=expected)fail("selection SHA-256 mismatch");
    if(bytes.empty()||bytes.back()!='\n')fail("selection missing final newline");
    std::istringstream f(bytes);std::string line;if(!std::getline(f,line)||line!="rank\tname\thostile_hits\tproper_hits\tsizes")fail("selection header mismatch");
    SelectionPacket out;out.digest=observed;uint64_t expected_rank=1;
    while(std::getline(f,line)){if(line.empty())fail("empty selection row");auto x=split_tabs(line);if(x.size()!=5)fail("selection field count");
        SelectionRow r;r.rank=parse_canonical_u64(x[0],"rank");r.name=x[1];r.hostile=parse_canonical_u64(x[2],"hostile_hits");r.proper=parse_canonical_u64(x[3],"proper_hits");r.sizes=parse_canonical_u64(x[4],"sizes");
        if(r.rank!=expected_rank++)fail("selection rank sequence");if(!cat.idx.count(r.name)||!out.names.insert(r.name).second)fail("unknown or duplicate selection syntax");
        if(r.hostile>r.proper||r.proper>848||r.sizes>3)fail("selection score range");out.rows.push_back(r);
    }
    if(out.rows.size()!=64)fail("selection must contain exactly 64 rows");
    auto better=[](const SelectionRow&a,const SelectionRow&b){if(a.hostile!=b.hostile)return a.hostile>b.hostile;if(a.proper!=b.proper)return a.proper>b.proper;if(a.sizes!=b.sizes)return a.sizes>b.sizes;return a.name<b.name;};
    for(size_t i=1;i<out.rows.size();++i)if(better(out.rows[i],out.rows[i-1]))fail("selection ranking order");
    return out;
}

static SelectionPacket read_selection(const std::string&path,const std::string&expected,
                                      const Catalog&cat){
    return parse_selection_bytes(read_binary(path),expected,cat);
}

struct LeadDecision {bool gate1=false,gate2=false,gate3=false,gate4=false;bool pass=false;};

static LeadDecision lead_decision(const CStat&s,const std::string&target,
                                  const SymbolicReport&sym){
    LeadDecision d;d.gate1=s.proper>=16;d.gate2=s.sizes.size()>=3&&s.high&&s.hostile>0;
    d.gate3=s.nondirect>0;d.gate4=!target.empty()&&sym.operational_targets.count(target);
    d.pass=d.gate1&&d.gate2&&d.gate3&&d.gate4;return d;
}

static std::string generic_target(const std::string&name){
    size_t dot=name.find('.');if(dot==std::string::npos)return {};
    std::string x=name.substr(dot+1);if(x.size()==2&&(x[0]=='u'||x[0]=='v'))return "P."+x;
    if(x.rfind("transfer_f",0)==0&&x.size()==11)return "P.f"+x.substr(10)+".b";
    if(x.rfind("transfer_r",0)==0&&x.size()==11)return "P.r"+x.substr(10)+".b";
    if(x=="jet_det01")return "P.jetdet01";if(x=="jet_det02")return "P.jetdet02";
    return {};
}

static void write_results(const fs::path&out,bool heldout,const Catalog&cat,
                          const SymbolicReport&sym,const std::vector<RowResult>&rows,
                          const SelectionPacket*selection=nullptr){
    fs::create_directories(out);std::string phase=heldout?"heldout":"discovery";
    std::set<std::string> selected;if(selection)selected=selection->names;
    std::ostringstream t;t<<"factor_bits\tmodulus_bits\tcohort\tindex\tp\tq\tN\tB\tH\tparity\tcapacity\tcleanup\tcleanup_divisor\tqueries\tleaves\tcentral_cover\tshifted_cover\tproper_bits\tsaturated_bits\tnondirect_bits\tfirst_name\tfirst_divisor\tfirst_block\tfirst_leaf\tfirst_nondirect\tcontrol_central_root_factors\tcontrol_shifted_root_factors\tcontrol_tree_factors\tcontrol_tree_merges\tcontrol_tree_state_words\tcontrol_oracle_calls_central\tcontrol_oracle_calls_shifted\tcontrol_recompute_factors_central\tcontrol_recompute_factors_shifted\tcontrol_oracle_covers_central\tcontrol_oracle_covers_shifted\n";
    std::vector<CStat> st(cat.names.size());
    for(auto&r:rows){t<<r.in.bits<<'\t'<<r.modulus_bits<<'\t'<<r.in.cohort<<'\t'<<r.in.index<<'\t'<<r.in.p<<'\t'<<r.in.q<<'\t'<<s128(r.in.n)<<'\t'<<r.B<<'\t'<<r.H<<'\t'<<(r.odd?"odd":"even")<<'\t'<<r.capacity<<'\t'<<r.cleanup<<'\t'<<r.cleanup_divisor<<'\t'<<r.queries<<'\t'<<r.leaves<<'\t'<<r.central_cover<<'\t'<<r.shifted_cover<<'\t'<<bithex(r.status,1)<<'\t'<<bithex(r.status,2)<<'\t'<<bithex(r.nondirect_status,1)<<'\t'<<r.first_name<<'\t'<<r.first_divisor<<'\t'<<r.first_block<<'\t'<<r.first_leaf<<'\t'<<r.first_nondirect<<'\t'<<r.control.central_root_factors<<'\t'<<r.control.shifted_root_factors<<'\t'<<r.control.tree_factors<<'\t'<<r.control.tree_merges<<'\t'<<r.control.tree_state_words<<'\t'<<r.control.oracle_calls_central<<'\t'<<r.control.oracle_calls_shifted<<'\t'<<r.control.recompute_factors_central<<'\t'<<r.control.recompute_factors_shifted<<'\t'<<r.control.oracle_covers_central<<'\t'<<r.control.oracle_covers_shifted<<'\n';
        bool hostile=r.in.cohort=="safe_safe"||r.in.cohort=="bounded_capacity";
        for(size_t i=0;i<r.status.size();++i){if(r.status[i]==1){++st[i].proper;st[i].sizes.insert(r.in.bits);st[i].high|=r.in.bits==56||r.in.bits==60;if(hostile)++st[i].hostile;}else if(r.status[i]==2)++st[i].saturated;if(i<r.nondirect_status.size()&&r.nondirect_status[i]){++st[i].nondirect;st[i].nondirect_sizes.insert(r.in.bits);st[i].nondirect_hostile|=hostile;}}
    }
    std::ostringstream j;j<<"{\n  \"phase\": \""<<phase<<"\",\n  \"rows\": "<<rows.size()<<",\n  \"symbolic\": {\"columns\": "<<sym.columns<<", \"rank1\": "<<sym.rank1<<", \"rank2\": "<<sym.rank2<<", \"nullity1\": "<<sym.nullity1<<", \"nullity2\": "<<sym.nullity2<<", \"signed_halves\": "<<sym.signed_halves<<", \"signature_classes\": "<<sym.signature_classes<<", \"exact_rows\": "<<sym.exact_rows<<", \"sparse_relations\": "<<sym.sparse_relations<<", \"basis_relations1\": "<<sym.basis_relations1<<", \"basis_relations2\": "<<sym.basis_relations2<<", \"controls\": "<<sym.controls<<", \"shortcuts\": "<<sym.shortcuts<<", \"adjacent_recurrences\": "<<sym.adjacent_recurrences<<", \"dyadic_recurrences\": "<<sym.dyadic_recurrences<<", \"identities\": [";
    for(size_t i=0;i<sym.identities.size();++i){if(i)j<<',';j<<'\"'<<sym.identities[i]<<'\"';}
    j<<"], \"dependency_audit\": [";for(size_t i=0;i<sym.dependency_audit.size();++i){if(i)j<<',';j<<'\"'<<sym.dependency_audit[i]<<'\"';}
    j<<"], \"recurrences\": [";for(size_t i=0;i<sym.recurrences.size();++i){if(i)j<<',';j<<'\"'<<sym.recurrences[i]<<'\"';}
    j<<"]},\n  \"nonoperational_controls\": [{\"name\":\"full_central_root_product\",\"class\":\"full_scan\"},{\"name\":\"full_shifted_denominator_product\",\"class\":\"full_scan\"},{\"name\":\"full_product_tree_preprocessing\",\"class\":\"recursive_merge\"},{\"name\":\"binary_singular_child_with_oracle\",\"class\":\"oracle_block\"},{\"name\":\"recompute_oracle_children\",\"class\":\"full_scan\"}],\n  \"candidates\": [\n";
    for(size_t i=0;i<cat.names.size();++i){j<<"    {\"name\": \""<<cat.names[i]<<"\", \"proper\": "<<st[i].proper<<", \"saturated\": "<<st[i].saturated<<", \"hostile\": "<<st[i].hostile<<", \"sizes\": "<<st[i].sizes.size()<<", \"nondirect\": "<<st[i].nondirect<<", \"selected\": "<<(selected.count(cat.names[i])?"true":"false")<<"}"<<(i+1==cat.names.size()?"\n":",\n");}j<<"  ]\n}\n";
    write_bounded(out,out/("F263-D02."+phase+".rows.tsv"),t.str());
    write_bounded(out,out/("F263-D02."+phase+".summary.json"),j.str());
    if(!heldout){
        std::vector<size_t>ord(cat.names.size());std::iota(ord.begin(),ord.end(),0);std::sort(ord.begin(),ord.end(),[&](size_t a,size_t b){if(st[a].hostile!=st[b].hostile)return st[a].hostile>st[b].hostile;if(st[a].proper!=st[b].proper)return st[a].proper>st[b].proper;if(st[a].sizes.size()!=st[b].sizes.size())return st[a].sizes.size()>st[b].sizes.size();return cat.names[a]<cat.names[b];});
        std::ostringstream s;s<<"rank\tname\thostile_hits\tproper_hits\tsizes\n";for(size_t k=0;k<64;++k){size_t i=ord[k];s<<k+1<<'\t'<<cat.names[i]<<'\t'<<st[i].hostile<<'\t'<<st[i].proper<<'\t'<<st[i].sizes.size()<<'\n';}
        write_bounded(out,out/"F263-D02.selection.tsv",s.str());
    }else{
        std::ostringstream g;g<<"rank\tname\tproper_hits\thostile_hits\tsizes\thigh_size\tnondirect_hits\tnondirect_hostile\toperational_target\tgate1\tgate2\tgate3\tgate4\tpass\n";
        for(const auto&sr:selection->rows){size_t i=cat.idx.at(sr.name);std::string target=generic_target(sr.name);LeadDecision d=lead_decision(st[i],target,sym);g<<sr.rank<<'\t'<<sr.name<<'\t'<<st[i].proper<<'\t'<<st[i].hostile<<'\t'<<st[i].sizes.size()<<'\t'<<st[i].high<<'\t'<<st[i].nondirect<<'\t'<<st[i].nondirect_hostile<<'\t'<<target<<'\t'<<d.gate1<<'\t'<<d.gate2<<'\t'<<d.gate3<<'\t'<<d.gate4<<'\t'<<d.pass<<'\n';}
        write_bounded(out,out/"F263-D02.heldout.lead_gate.tsv",g.str());
    }
}

static std::vector<RowResult> run_rows(const std::vector<Labelled>&in,const Catalog&cat,unsigned threads){
    if(threads<1||threads>8)fail("threads outside frozen range");std::vector<RowResult>out(in.size());std::atomic<size_t>next{0};std::vector<std::thread>pool;
    for(unsigned t=0;t<threads;++t)pool.emplace_back([&]{for(;;){size_t i=next.fetch_add(1);if(i>=in.size())break;out[i]=analyze(in[i],cat);}});for(auto&t:pool)t.join();return out;
}

static void refuse_phase_outputs(const fs::path&out,bool heldout){
    std::string phase=heldout?"heldout":"discovery";
    std::vector<fs::path> files{out/("F263-D02."+phase+".rows.tsv"),out/("F263-D02."+phase+".summary.json")};
    files.push_back(out/(heldout?"F263-D02.heldout.lead_gate.tsv":"F263-D02.selection.tsv"));
    for(const auto&p:files)if(fs::exists(p))fail("phase output already exists: "+p.string());
}

static void self_test(){
    if(sha256_bytes("abc")!="ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad")fail("SHA-256 self-test");
    if(!prime64(19)||!prime64(23)||prime64(21))fail("primality self-test");
    {
        uint128_t n=uint128_t(11)*13;uint64_t B=isqrt128(n);
        if(B!=11||gcd128(B,n)!=11||!(B&1))fail("B=p public-screen fixture");
    }
    for(auto [p,q,parity]:std::vector<std::tuple<uint64_t,uint64_t,int>>{{19,23,0},{23,29,1}}){
        uint128_t n=uint128_t(p)*q;uint64_t B=isqrt128(n),H=B/2;if(int(B&1)!=parity)fail("parity fixture");
        if(gcd128(B,n)>1)fail("unexpected cleanup fixture");uint64_t k=(p-1)/2;uint128_t un=1,vd=1;
        for(uint64_t i=0;i<H;++i){un=mulm(un,uint128_t(4)*i+2,n);vd=mulm(vd,i+1,n);}
        if(gcd128(un,n)!=p||gcd128(vd,n)!=1||k>=H)fail("central singularity self-test");
        uint64_t s=B-p;int hits=0;for(uint64_t c=1;c<H;++c)if(gcd128(n,n+c-B)>1){if(c!=s)fail("shift singular location");++hits;}if(hits!=1)fail("shift singular count");
        if(B&1){if(gcd128(H+1,n)!=1||gcd128(B,n)!=1)fail("odd multiplier screen");}
    }
    EState l=exact_state(4,2,1,1,3,5,1),r=exact_state(4,2,1,1,8,5,1),p=exact_state(4,2,1,1,3,10,1);
    if(p.u[2]!=l.u[2]*r.u[0]+l.u[1]*r.u[1]+l.u[0]*r.u[2])fail("jet merge self-test");
    SymbolicReport s=symbolic_search();if(s.controls!=12||s.adjacent_recurrences!=4)fail("symbolic controls missing");
    if(s.exact_rows!=192||s.nullity1==0||s.nullity2==0||s.signed_halves!=9801)fail("full symbolic authentication coverage");
    if(s.dependency_audit.size()!=s.identities.size()||s.recurrences.size()!=4+s.dyadic_recurrences)fail("symbolic output retention");
    for(auto t:std::vector<std::tuple<int64_t,int64_t,int64_t>>{{4,2,5},{1,1,7},{1,1009,8},{1,989,8}}){Recurrence z=guess_adjacent(std::get<0>(t),std::get<1>(t),std::get<2>(t));if(z.order!=1||z.degree!=1||z.height>4096||!z.auth_p1||!z.auth_p2||!z.auth_exact||z.dependency!=DepClass::FullScan)fail("two-prime adjacent recurrence authentication");}
    {
        FeatureRow schema;schema.names={"P.target","descriptor"};schema.x={0,0};schema.dep={parent_meta(8),descriptor_meta()};
        if(!classify_shortcut({1,-1},schema).accepted)fail("unit-target dependency criterion");
        schema.dep[1]=merge_meta(8);if(classify_shortcut({1,-1},schema).accepted)fail("recursive merge misclassified operational");
    }
    Catalog c=build_catalog();if(c.names.size()!=148)fail("candidate count drift: "+std::to_string(c.names.size()));
    {
        const uint128_t test_n=15;
        Eval e(c,test_n);
        Witness w=one_witness(Family::Central,{4,0});
        e.divisor(c.names[0],uint128_t(15),"saturated-first",1,w);
        e.divisor(c.names[0],uint128_t(3),"proper-second",2,w);
        if(e.status[0]!=1||e.first_divisor!="3")fail("saturated-before-proper ordering");
    }
    if(accepts_pair(17,37,"bounded_capacity")||accepts_pair(17,17,"random")||
       !accepts_pair(17,19,"bounded_capacity")||!accepts_pair(47,59,"safe_safe"))fail("attempt-cap acceptance predicate");
    if(literal_hash("bounded_capacity")!=12148366553126710945ULL)fail("literal cohort hash drift");
    std::set<std::string>seen;Labelled bounded=make_unique_row(16,"bounded_capacity",0,seen);Labelled safe=make_unique_row(16,"safe_safe",0,seen);Labelled random=make_unique_row(16,"random",0,seen);
    if(std::gcd(bounded.p-1,bounded.q-1)>16||std::gcd(safe.p-1,safe.q-1)!=2||seen.size()!=3||random.p==random.q)fail("bounded globally distinct generators");
    if(expected_cohort_rows(false)!=848||expected_cohort_rows(true)!=1152)fail("cohort row-count drift");
    auto qc=queries(20000,120,17);bool has_n=false,has_n2=false;for(Query q:qc){has_n|=q.len==120;has_n2|=q.len==14400;if(q.len>14400)fail("query n^2 cap");}if(!has_n||!has_n2)fail("modulus-bit query bank");
    auto pc=oracle_path_cost(8,5);if(pc.first!=3||pc.second!=7)fail("nonoperational control cost");
    if(!direct_witness(one_witness(Family::Central,{4,3}),5,0)||direct_witness(one_witness(Family::Central,{2,0}),5,0))fail("direct-mechanism classifier");
    {
        std::vector<std::string>names=c.names;std::sort(names.begin(),names.end());std::ostringstream q;q<<"rank\tname\thostile_hits\tproper_hits\tsizes\n";for(size_t i=0;i<64;++i)q<<i+1<<'\t'<<names[i]<<"\t0\t0\t0\n";
        std::string bytes=q.str(),digest=sha256_bytes(bytes);SelectionPacket packet=parse_selection_bytes(bytes,digest,c);if(packet.rows.size()!=64||packet.digest!=digest)fail("selection exact parser");
        bool rejected=false;try{parse_selection_bytes(bytes,std::string(64,'0'),c);}catch(const std::exception&){rejected=true;}if(!rejected)fail("selection digest firewall");
    }
    {
        CStat z;z.proper=16;z.hostile=1;z.nondirect=1;z.high=true;z.sizes={40,48,60};SymbolicReport a;a.operational_targets.insert("P.u0");
        LeadDecision d=lead_decision(z,"P.u0",a);if(!d.pass){fail("lead-gate positive control");}z.nondirect=0;if(lead_decision(z,"P.u0",a).pass)fail("lead-gate nondirect control");
    }
    std::cout<<"SELF_TEST_PASS controls="<<s.controls<<" columns="<<s.columns<<" ranks="<<s.rank1<<','<<s.rank2<<" nullities="<<s.nullity1<<','<<s.nullity2<<" halves="<<s.signed_halves<<" sparse="<<s.sparse_relations<<" basis="<<s.basis_relations1<<','<<s.basis_relations2<<" shortcuts="<<s.shortcuts<<" adjacent="<<s.adjacent_recurrences<<" dyadic="<<s.dyadic_recurrences<<" candidates="<<c.names.size()<<" rows=848,1152\n";
}

static void benchmark(){
    auto begin=std::chrono::steady_clock::now();SymbolicReport s=symbolic_search();Catalog c=build_catalog();
    uint64_t p=(uint64_t(1)<<60)-93,q=(uint64_t(1)<<60)-33;Labelled x{p,q,uint128_t(p)*q,60,"public_benchmark",0};RowResult r=analyze(x,c);
    double sec=std::chrono::duration<double>(std::chrono::steady_clock::now()-begin).count();
    if(r.modulus_bits!=bitlen(x.n)||r.modulus_bits!=120)fail("benchmark modulus-bit drift");
    std::cout<<std::fixed<<std::setprecision(6)<<"BENCHMARK_PASS seconds="<<sec<<" modulus_bits="<<r.modulus_bits<<" blocks="<<r.queries<<" leaf_touches="<<r.leaves<<" candidates="<<c.names.size()<<" symbolic_columns="<<s.columns<<" symbolic_relations="<<s.sparse_relations<<" shortcuts="<<s.shortcuts<<" projected_rows=2000\n";
}

int main(int argc,char**argv){
    try{
        if(argc==2&&std::string(argv[1])=="--self-test"){self_test();return 0;}
        if(argc==2&&std::string(argv[1])=="--benchmark"){benchmark();return 0;}
        if(argc==5&&std::string(argv[1])=="--discovery"){
            fs::path out=argv[2];unsigned th=unsigned(std::stoul(argv[3]));if(std::string(argv[4])!="full")fail("frozen mode must be full");
            refuse_phase_outputs(out,false);SymbolicReport s=symbolic_search();Catalog c=build_catalog();auto rows=run_rows(cohort_rows(false),c,th);write_results(out,false,c,s,rows);return 0;
        }
        if(argc==7&&std::string(argv[1])=="--heldout"){
            fs::path out=argv[2];std::string selection=argv[3],digest=argv[4];unsigned th=unsigned(std::stoul(argv[5]));if(std::string(argv[6])!="full")fail("frozen mode must be full");
            refuse_phase_outputs(out,true);Catalog c=build_catalog();SelectionPacket sel=read_selection(selection,digest,c);SymbolicReport s=symbolic_search();auto rows=run_rows(cohort_rows(true),c,th);write_results(out,true,c,s,rows,&sel);return 0;
        }
        std::cerr<<"usage: V2_symbolic_search --self-test | --benchmark | --discovery OUT THREADS full | --heldout OUT SELECTION EXPECTED_SHA256 THREADS full\n";return 64;
    }catch(const std::exception&e){std::cerr<<"F263_ERROR "<<e.what()<<'\n';return 70;}
}
