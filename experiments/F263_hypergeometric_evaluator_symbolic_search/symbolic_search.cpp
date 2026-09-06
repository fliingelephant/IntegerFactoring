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

struct FeatureRow { std::vector<std::string> names; std::vector<cpp_int> x; };

static void push_feature(FeatureRow &r, const std::string &name, const cpp_int &x) {
    r.names.push_back(name);
    r.x.push_back(x);
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
    push_feature(out, "one", 1);
    const std::array<std::string, 6> dn{"s","m","alpha","beta","gamma","delta"};
    const std::array<cpp_int, 6> dv{cpp_int(start),cpp_int(m),cpp_int(alpha),
        cpp_int(beta),cpp_int(gamma),cpp_int(delta)};
    for (size_t i = 0; i < dv.size(); ++i) push_feature(out, dn[i], dv[i]);
    for (size_t i = 0; i < dv.size(); ++i)
        for (size_t j = i; j < dv.size(); ++j)
            push_feature(out, dn[i] + "*" + dn[j], dv[i] * dv[j]);
    auto jets = [&](char which, const std::array<cpp_int,3> &pp,
                    const std::array<cpp_int,3> &ll,
                    const std::array<cpp_int,3> &r0) {
        std::string q(1, which);
        push_feature(out, "P."+q+"0", pp[0]);
        push_feature(out, "L."+q+"0*R."+q+"0", ll[0]*r0[0]);
        push_feature(out, "P."+q+"1", pp[1]);
        push_feature(out, "L."+q+"1*R."+q+"0", ll[1]*r0[0]);
        push_feature(out, "L."+q+"0*R."+q+"1", ll[0]*r0[1]);
        push_feature(out, "P."+q+"2", pp[2]);
        push_feature(out, "L."+q+"2*R."+q+"0", ll[2]*r0[0]);
        push_feature(out, "L."+q+"1*R."+q+"1", ll[1]*r0[1]);
        push_feature(out, "L."+q+"0*R."+q+"2", ll[0]*r0[2]);
    };
    jets('u', p.u, l.u, rr.u);
    jets('v', p.v, l.v, rr.v);
    for (size_t w = 0; w < 3; ++w) {
        std::string z = std::to_string(w);
        push_feature(out, "P.f"+z+".b", p.fwd[w].b);
        push_feature(out, "L.f"+z+".a*R.f"+z+".b", l.fwd[w].a*rr.fwd[w].b);
        push_feature(out, "L.f"+z+".b*R.f"+z+".d", l.fwd[w].b*rr.fwd[w].d);
        push_feature(out, "P.r"+z+".b", p.rev[w].b);
        push_feature(out, "R.r"+z+".a*L.r"+z+".b", rr.rev[w].a*l.rev[w].b);
        push_feature(out, "R.r"+z+".b*L.r"+z+".d", rr.rev[w].b*l.rev[w].d);
    }
    push_feature(out, "P.ured", p.ured);
    push_feature(out, "P.vred", p.vred);
    push_feature(out, "L.ured*R.ured", l.ured*rr.ured);
    push_feature(out, "L.vred*R.vred", l.vred*rr.vred);
    push_feature(out, "P.jetdet01", p.u[0]*p.v[1]-p.u[1]*p.v[0]);
    push_feature(out, "P.jetdet02", p.u[0]*p.v[2]-p.u[2]*p.v[0]);
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

struct SigKey { uint64_t a, b; bool operator==(const SigKey &x) const { return a==x.a && b==x.b; } };
struct SigHash { size_t operator()(const SigKey &x) const { return size_t(mix(x.a,x.b)); } };
struct Comb { std::vector<std::pair<size_t,int>> t; };

static SigKey comb_signature(const Comb &c, const std::vector<FeatureRow> &rows) {
    uint64_t h1 = 0x243f6a8885a308d3ULL, h2 = 0x13198a2e03707344ULL;
    for (size_t r = 0; r < rows.size(); ++r) {
        uint64_t x1 = 0, x2 = 0;
        for (auto [i,s] : c.t) {
            uint64_t q1 = cpp_mod(rows[r].x[i], P1), q2 = cpp_mod(rows[r].x[i], P2);
            if (s > 0) { x1 += q1; if (x1>=P1) x1-=P1; x2 += q2; if(x2>=P2)x2-=P2; }
            else { x1 = x1>=q1 ? x1-q1 : x1+P1-q1; x2=x2>=q2?x2-q2:x2+P2-q2; }
        }
        h1 = mix(h1, x1 ^ splitmix64(r));
        h2 = mix(h2, x2 ^ splitmix64(r+0x10000));
    }
    return {h1,h2};
}

struct SymbolicReport {
    size_t columns=0, rank1=0, rank2=0, nullity1=0, nullity2=0;
    size_t sparse_relations=0, basis_relations=0, controls=0, shortcuts=0;
    size_t adjacent_recurrences=0, dyadic_recurrences=0;
    std::vector<std::string> identities;
    std::vector<std::string> recurrences;
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

struct Recurrence { int order=-1, degree=-1; std::vector<int64_t> c; };

static Recurrence guess_adjacent(int64_t a, int64_t b, int64_t len) {
    for (int ord=0;ord<=3;++ord) for(int deg=0;deg<=3;++deg) {
        size_t cols=size_t(ord+1)*size_t(deg+1);
        std::vector<std::vector<uint64_t>> mat;
        for(int64_t s=1;s<=int64_t(cols)+12;++s) {
            std::vector<uint64_t> row;
            for(int i=0;i<=ord;++i) {
                uint64_t val=cpp_mod(affine_product(a,b,s+i,len),P1), sp=1;
                for(int d=0;d<=deg;++d){row.push_back(mulmod64(val,sp,P1));sp=mulmod64(sp,uint64_t(s),P1);}
            }
            mat.push_back(std::move(row));
        }
        auto rr=rref_nullspace(mat,P1);
        if(rr.basis.empty()) continue;
        for(auto &v:rr.basis){
            auto z=rescale_small(v,P1,4096); if(z.empty()) continue;
            bool ok=true;
            for(int64_t s=50;s<70 && ok;++s){
                cpp_int sum=0; size_t k=0;
                for(int i=0;i<=ord;++i){cpp_int val=affine_product(a,b,s+i,len),sp=1;
                    for(int d=0;d<=deg;++d){sum+=cpp_int(z[k++])*sp*val;sp*=s;}}
                ok=sum==0;
            }
            if(ok) return {ord,deg,z};
        }
    }
    return {};
}

static std::string recurrence_text(const std::string &name, const Recurrence &r) {
    std::ostringstream o;
    o << name << ":order=" << r.order << ",degree=" << r.degree << ",coeff=";
    for (size_t i=0;i<r.c.size();++i) { if (i) o << ','; o << r.c[i]; }
    return o.str();
}

static size_t search_dyadic_recurrence() {
    for(int ord=0;ord<=3;++ord) for(int deg=0;deg<=3;++deg){
        size_t cols=size_t(ord+1)*size_t(deg+1);
        std::vector<std::vector<uint64_t>> mat;
        for(int64_t s:{1LL,3LL,7LL,11LL}) for(int j=0;j+ord<=15;++j){
            std::vector<uint64_t> row;
            for(int i=0;i<=ord;++i){
                int len=1<<(j+i); uint64_t val=1;
                for(int k=0;k<len;++k) val=mulmod64(val,uint64_t(4*(s+k)+2)%P1,P1);
                uint64_t jp=1;
                for(int d=0;d<=deg;++d){row.push_back(mulmod64(val,jp,P1));jp=mulmod64(jp,uint64_t(j),P1);}
            }
            mat.push_back(std::move(row));
        }
        auto rr=rref_nullspace(mat,P1);
        for(auto &v:rr.basis){
            auto z=rescale_small(v,P1,4096); if(z.empty()) continue;
            bool ok=true;
            for(int64_t s:{2LL,5LL,13LL}) for(int j=0;j+ord<=9 && ok;++j){
                cpp_int sum=0; size_t q=0;
                for(int i=0;i<=ord;++i){cpp_int val=affine_product(4,2,s,1<<(j+i)),jp=1;
                    for(int d=0;d<=deg;++d){sum+=cpp_int(z[q++])*jp*val;jp*=j;}}
                if(sum!=0) ok=false;
            }
            if(!ok) continue;
            for(int64_t s:{17LL,19LL}) for(int j=8;j+ord<=17 && ok;++j){
                uint64_t sum=0; size_t q=0;
                for(int i=0;i<=ord;++i){uint64_t val=1;int len=1<<(j+i);
                    for(int k=0;k<len;++k) val=mulmod64(val,uint64_t(4*(s+k)+2)%P2,P2);
                    uint64_t jp=1;
                    for(int d=0;d<=deg;++d){uint64_t c=z[q]>=0?uint64_t(z[q]):P2-uint64_t(-z[q]);
                        sum+=mulmod64(c,mulmod64(jp,val,P2),P2);if(sum>=P2)sum-=P2;++q;jp=mulmod64(jp,uint64_t(j),P2);}}
                if(sum!=0) ok=false;
            }
            if(ok) return 1;
        }
    }
    return 0;
}

static SymbolicReport symbolic_search() {
    std::vector<FeatureRow> train, hold;
    for(uint64_t i=0;i<128;++i) train.push_back(feature_row(i,false));
    for(uint64_t i=0;i<64;++i) hold.push_back(feature_row(i,true));
    const auto &names=train[0].names;
    for(auto &r:train) if(r.names!=names) fail("symbolic feature order drift");
    for(auto &r:hold) if(r.names!=names) fail("holdout feature order drift");
    std::vector<std::vector<uint64_t>> m1,m2;
    for(auto &r:train){std::vector<uint64_t>a,b;for(auto &x:r.x){a.push_back(cpp_mod(x,P1));b.push_back(cpp_mod(x,P2));}m1.push_back(a);m2.push_back(b);}
    auto n1=rref_nullspace(m1,P1),n2=rref_nullspace(m2,P2);
    std::set<std::string> accepted;
    std::unordered_map<SigKey,Comb,SigHash> seen;
    std::vector<Comb> all;
    for(size_t i=0;i<names.size();++i) for(int s:{1,-1}) all.push_back({{{i,s}}});
    for(size_t i=0;i<names.size();++i) for(size_t j=i+1;j<names.size();++j)
        for(int si:{1,-1}) for(int sj:{1,-1}) all.push_back({{{i,si},{j,sj}}});
    for(auto &c:all){
        SigKey k=comb_signature(c,train); auto it=seen.find(k);
        if(it==seen.end()){seen.emplace(k,c);continue;}
        std::vector<std::pair<size_t,int>> terms=c.t;
        for(auto [i,s]:it->second.t)terms.push_back({i,-s});
        auto v=normalize_relation(names.size(),terms);size_t support=0;bool small=true;
        for(auto x:v)if(x){++support;if(x<-1||x>1)small=false;}
        if(!small||support<2||support>4||!exact_relation(v,hold))continue;
        accepted.insert(relation_key(v,names));
    }
    size_t basis_count=0;
    for(auto &v:n1.basis){auto z=rescale_small(v,P1,4096);if(!z.empty()&&exact_relation(z,hold)){accepted.insert(relation_key(z,names));++basis_count;}}
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
    for(auto &k:accepted){
        bool parent=k.find("P.")!=std::string::npos;
        bool child=k.find("L.")!=std::string::npos||k.find("R.")!=std::string::npos;
        if(parent&&!child)++shortcuts;
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
    out.sparse_relations=accepted.size();out.basis_relations=basis_count;
    out.controls=controls;out.shortcuts=shortcuts;out.adjacent_recurrences=adjacent;
    out.dyadic_recurrences=search_dyadic_recurrence();
    for(auto &x:accepted)out.identities.push_back(x);
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
    Eval(const Catalog&c,const uint128_t&nn):cat(c),n(nn),status(c.names.size(),0){}
    void divisor(const std::string&name,uint128_t d,const std::string&block,uint64_t leaf){
        size_t i=cat.idx.at(name);uint8_t s=(d>1&&d<n)?1:(d==n?2:0);if(s==1||status[i]==0)status[i]=s;
        if(s==1&&first_name.empty()){first_name=name;first_divisor=s128(d);first_block=block;first_leaf=leaf;}
    }
    void value(const std::string&name,const uint128_t&v,const std::string&block,uint64_t leaf){divisor(name,gcd128(v,n),block,leaf);}
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

static void eval_block(Eval&e,const std::string&f,const Block&b,const uint128_t&n,uint64_t leaf){
    std::string d=std::to_string(b.q.start)+":"+std::to_string(b.q.len);
    for(int i=0;i<3;++i){e.value(f+".u"+std::to_string(i),b.s.u[i],d,leaf);e.value(f+".v"+std::to_string(i),b.s.v[i],d,leaf);}
    e.value(f+".jet_det01",det2(b.s.u[0],b.s.u[1],b.s.v[0],b.s.v[1],n),d,leaf);
    e.value(f+".jet_det02",det2(b.s.u[0],b.s.u[2],b.s.v[0],b.s.v[2],n),d,leaf);
    e.value(f+".jet_det12",det2(b.s.u[1],b.s.u[2],b.s.v[1],b.s.v[2],n),d,leaf);
    e.value(f+".jet_resultant",resultant2(b.s.u,b.s.v,n),d,leaf);
    for(int w=0;w<3;++w){e.value(f+".transfer_f"+std::to_string(w),b.s.fwd[w].b,d,leaf);e.value(f+".transfer_r"+std::to_string(w),b.s.rev[w].b,d,leaf);}
    e.value(f+".transfer_det01",det2(b.s.fwd[0].a,b.s.fwd[0].b,b.s.fwd[1].a,b.s.fwd[1].b,n),d,leaf);
    e.value(f+".transfer_det02",det2(b.s.fwd[0].a,b.s.fwd[0].b,b.s.fwd[2].a,b.s.fwd[2].b,n),d,leaf);
    e.value(f+".transfer_det12",det2(b.s.fwd[1].a,b.s.fwd[1].b,b.s.fwd[2].a,b.s.fwd[2].b,n),d,leaf);
    for(int i=0;i<16;++i)e.value(f+".projection"+(i<10?"0":"")+std::to_string(i),projection(b.s,n,SEED^uint64_t(i),b.q,false),d,leaf);
    for(int i=0;i<8;++i)e.value(f+".product_hash"+(i<10?"0":"")+std::to_string(i),projection(b.s,n,SEED^0x5555^uint64_t(i),b.q,true),d,leaf);
    if(!b.has_adj)return;
    for(int i=0;i<3;++i){e.value(f+".adj_du"+std::to_string(i),subm(b.adj.u[i],b.s.u[i],n),d,leaf);e.value(f+".adj_dv"+std::to_string(i),subm(b.adj.v[i],b.s.v[i],n),d,leaf);}
    e.value(f+".adj_u_det01",det2(b.s.u[0],b.s.u[1],b.adj.u[0],b.adj.u[1],n),d,leaf);
    e.value(f+".adj_u_det02",det2(b.s.u[0],b.s.u[2],b.adj.u[0],b.adj.u[2],n),d,leaf);
    e.value(f+".adj_u_det12",det2(b.s.u[1],b.s.u[2],b.adj.u[1],b.adj.u[2],n),d,leaf);
    e.value(f+".adj_v_det01",det2(b.s.v[0],b.s.v[1],b.adj.v[0],b.adj.v[1],n),d,leaf);
    e.value(f+".adj_v_det02",det2(b.s.v[0],b.s.v[2],b.adj.v[0],b.adj.v[2],n),d,leaf);
    e.value(f+".adj_v_det12",det2(b.s.v[1],b.s.v[2],b.adj.v[1],b.adj.v[2],n),d,leaf);
    e.value(f+".adj_resultant_u",resultant2(b.s.u,b.adj.u,n),d,leaf);
    e.value(f+".adj_resultant_v",resultant2(b.s.v,b.adj.v,n),d,leaf);
    auto x=state_vector(b.s),y=state_vector(b.adj);uint128_t g=n;
    for(auto z:x)g=gcd128(g,z);for(auto z:y)g=gcd128(g,z);e.divisor(f+".smith_d1",g,d,leaf);
    g=n;for(size_t i=0;i<x.size();++i)for(size_t j=i+1;j<x.size();++j)g=gcd128(g,det2(x[i],x[j],y[i],y[j],n));e.divisor(f+".smith_d2",g,d,leaf);
}

static void eval_pair(Eval&e,const std::string&f,const Block&a,const Block&b,const uint128_t&n,uint64_t leaf){
    std::string d=std::to_string(a.q.start)+","+std::to_string(b.q.start)+":"+std::to_string(a.q.len);
    for(int i=0;i<8;++i){uint128_t x=projection(a.s,n,SEED^0x7777^uint64_t(i),a.q,false),y=projection(b.s,n,SEED^0x7777^uint64_t(i),b.q,false);e.value(f+".pair_projection_diff"+(i<10?"0":"")+std::to_string(i),subm(x,y,n),d,leaf);}
    e.value(f+".pair_u_det01",det2(a.s.u[0],a.s.u[1],b.s.u[0],b.s.u[1],n),d,leaf);
    e.value(f+".pair_u_det02",det2(a.s.u[0],a.s.u[2],b.s.u[0],b.s.u[2],n),d,leaf);
    e.value(f+".pair_u_det12",det2(a.s.u[1],a.s.u[2],b.s.u[1],b.s.u[2],n),d,leaf);
    for(int w=0;w<3;++w)e.value(f+".pair_transfer_det"+std::to_string(w),det2(a.s.fwd[w].a,a.s.fwd[w].b,b.s.fwd[w].a,b.s.fwd[w].b,n),d,leaf);
    e.value(f+".pair_resultant",resultant2(a.s.u,b.s.u,n),d,leaf);
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
struct RowResult {
    Labelled in; uint64_t B=0,H=0,queries=0,leaves=0,capacity=0;
    bool odd=false,cleanup=false,central_cover=false,shifted_cover=false;
    std::string cleanup_divisor,first_name,first_divisor,first_block;uint64_t first_leaf=0;
    std::vector<uint8_t> status;
};

static RowResult analyze(const Labelled&in,const Catalog&cat){
    RowResult r;r.in=in;r.B=isqrt128(in.n);r.H=r.B/2;r.odd=r.B&1;
    uint128_t d=gcd128(in.n,r.B);if(d>1&&d<in.n){r.cleanup=true;r.cleanup_divisor=s128(d);r.status.assign(cat.names.size(),0);return r;}
    d=gcd128(in.n,r.H+1);if(d>1&&d<in.n){r.cleanup=true;r.cleanup_divisor=s128(d);r.status.assign(cat.names.size(),0);return r;}
    r.capacity=std::gcd(in.p-1,in.q-1);Eval e(cat,in.n);
    uint64_t central_k=(in.p-1)/2, shifted_c=r.B-in.p;
    for(auto [fam,name,domain,base,salt]:std::vector<std::tuple<Family,std::string,uint64_t,uint64_t,uint64_t>>{
            {Family::Central,"central",r.H,0,SEED^0x1111},{Family::Shifted,"shifted",r.H>0?r.H-1:0,1,SEED^0x2222}}){
        if(domain<8)continue;auto qs=queries(domain,in.bits,mix(low64(in.n),salt));
        std::map<uint64_t,std::vector<Block>> bylen;
        for(auto q:qs){Block b;b.q=q;uint64_t actual=base+q.start;
            b.s=scan_state(fam,in.n,r.B,actual,q.len,mix(salt,q.start));r.leaves+=q.len;++r.queries;
            if(q.start+q.len<domain){b.has_adj=true;b.adj=scan_state(fam,in.n,r.B,actual+1,q.len,mix(salt,q.start+1));r.leaves+=q.len;++r.queries;}
            if(fam==Family::Central&&q.start<=central_k&&central_k<q.start+q.len)r.central_cover=true;
            if(fam==Family::Shifted&&shifted_c>=1){uint64_t z=shifted_c-1;if(q.start<=z&&z<q.start+q.len)r.shifted_cover=true;}
            eval_block(e,name,b,in.n,r.leaves);bylen[q.len].push_back(std::move(b));
        }
        for(auto &[l,bs]:bylen)if(bs.size()>1)for(size_t i=1;i<bs.size();++i)eval_pair(e,name,bs[0],bs[i],in.n,r.leaves);
    }
    r.status=std::move(e.status);r.first_name=e.first_name;r.first_divisor=e.first_divisor;r.first_block=e.first_block;r.first_leaf=e.first_leaf;return r;
}

static uint64_t exact_bit_candidate(unsigned bits,uint64_t h){
    uint64_t mask=(uint64_t(1)<<bits)-1,top=uint64_t(1)<<(bits-1);return (h&mask)|top|1;
}

static uint64_t find_prime(unsigned bits,uint64_t seed,uint64_t cap=2000000){
    for(uint64_t a=0;a<cap;++a){uint64_t x=exact_bit_candidate(bits,splitmix64(seed^a));if(prime64(x))return x;}fail("prime generator cap");
}

static uint64_t find_safe(unsigned bits,uint64_t seed){
    for(uint64_t a=0;a<4000000;++a){uint64_t r=find_prime(bits-1,mix(seed,a),200);uint64_t p=2*r+1;if(bitlen(uint128_t(p))==bits&&prime64(p))return p;}fail("safe-prime generator cap");
}

static Labelled make_row(unsigned bits,const std::string&cohort,size_t idx,uint64_t salt){
    uint64_t tag=mix(SEED,mix(bits,mix(literal_hash(cohort),idx^salt))),p=0,q=0;
    if(cohort=="safe_safe"){p=find_safe(bits,tag);q=find_safe(bits,tag^0x123456789abcdef0ULL);if(p==q)q=find_safe(bits,tag^0xfedcba9876543210ULL);}
    else if(cohort=="consecutive"){p=find_prime(bits,tag);q=next_prime(p);if(bitlen(uint128_t(q))!=bits) return make_row(bits,cohort,idx,salt+1);}
    else {p=find_prime(bits,tag);bool accepted=false;for(uint64_t a=0;a<100000;++a){uint64_t candidate=find_prime(bits,mix(tag^0xabcdef,a));if(candidate!=p){uint64_t lo=std::min(p,candidate),hi=std::max(p,candidate);if(hi<2*lo&&(cohort!="bounded_capacity"||std::gcd(lo-1,hi-1)<=16)){p=lo;q=hi;accepted=true;break;}}}if(!accepted)fail("pair generator cap");}
    if(p>q)std::swap(p,q);if(q>=2*p)fail("balance generator error");
    return {p,q,uint128_t(p)*uint128_t(q),bits,cohort,idx};
}

static bool accepts_pair(uint64_t p,uint64_t q,const std::string&cohort){
    if(p==q)return false;if(p>q)std::swap(p,q);
    return q<2*p&&(cohort!="bounded_capacity"||std::gcd(p-1,q-1)<=16);
}

static std::vector<Labelled> cohort_rows(bool heldout){
    std::vector<unsigned> bits=heldout?std::vector<unsigned>{40,48,56,60}:std::vector<unsigned>{16,24,32};
    std::vector<Labelled> out;std::set<std::string> seen;
    for(unsigned b:bits)for(auto [name,count]:std::vector<std::pair<std::string,size_t>>{{"random",128},{"consecutive",64},{"safe_safe",b==16?16UL:32UL},{"bounded_capacity",64}})
        for(size_t i=0;i<count;++i){Labelled x=make_row(b,name,i,0);if(!seen.insert(s128(x.n)).second)fail("duplicate frozen modulus");out.push_back(x);}
    return out;
}

static std::string bithex(const std::vector<uint8_t>&s,uint8_t want){
    static const char*h="0123456789abcdef";std::string o;for(size_t i=0;i<s.size();i+=4){int z=0;for(size_t j=0;j<4&&i+j<s.size();++j)if(s[i+j]==want)z|=1<<j;o.push_back(h[z]);}return o;
}

struct CStat { uint64_t proper=0,saturated=0,hostile=0;std::set<unsigned>sizes; };

static void write_results(const fs::path&out,bool heldout,const Catalog&cat,const SymbolicReport&sym,const std::vector<RowResult>&rows,const std::set<std::string>&selection={}){
    fs::create_directories(out);std::string phase=heldout?"heldout":"discovery";
    std::ofstream t(out/("F263-D01."+phase+".rows.tsv"));
    t<<"factor_bits\tcohort\tindex\tp\tq\tN\tB\tH\tparity\tcapacity\tcleanup\tcleanup_divisor\tqueries\tleaves\tcentral_cover\tshifted_cover\tproper_bits\tsaturated_bits\tfirst_name\tfirst_divisor\tfirst_block\tfirst_leaf\n";
    std::vector<CStat> st(cat.names.size());
    for(auto&r:rows){t<<r.in.bits<<'\t'<<r.in.cohort<<'\t'<<r.in.index<<'\t'<<r.in.p<<'\t'<<r.in.q<<'\t'<<s128(r.in.n)<<'\t'<<r.B<<'\t'<<r.H<<'\t'<<(r.odd?"odd":"even")<<'\t'<<r.capacity<<'\t'<<r.cleanup<<'\t'<<r.cleanup_divisor<<'\t'<<r.queries<<'\t'<<r.leaves<<'\t'<<r.central_cover<<'\t'<<r.shifted_cover<<'\t'<<bithex(r.status,1)<<'\t'<<bithex(r.status,2)<<'\t'<<r.first_name<<'\t'<<r.first_divisor<<'\t'<<r.first_block<<'\t'<<r.first_leaf<<'\n';
        for(size_t i=0;i<r.status.size();++i){if(r.status[i]==1){++st[i].proper;st[i].sizes.insert(r.in.bits);if(r.in.cohort=="safe_safe"||r.in.cohort=="bounded_capacity")++st[i].hostile;}else if(r.status[i]==2)++st[i].saturated;}}
    std::ofstream j(out/("F263-D01."+phase+".summary.json"));j<<"{\n  \"phase\": \""<<phase<<"\",\n  \"rows\": "<<rows.size()<<",\n  \"symbolic\": {\"columns\": "<<sym.columns<<", \"rank1\": "<<sym.rank1<<", \"rank2\": "<<sym.rank2<<", \"nullity1\": "<<sym.nullity1<<", \"nullity2\": "<<sym.nullity2<<", \"relations\": "<<sym.sparse_relations<<", \"controls\": "<<sym.controls<<", \"shortcuts\": "<<sym.shortcuts<<", \"adjacent_recurrences\": "<<sym.adjacent_recurrences<<", \"dyadic_recurrences\": "<<sym.dyadic_recurrences<<", \"identities\": [";
    for(size_t i=0;i<sym.identities.size();++i){if(i)j<<',';j<<'\"'<<sym.identities[i]<<'\"';}
    j<<"], \"recurrences\": [";
    for(size_t i=0;i<sym.recurrences.size();++i){if(i)j<<',';j<<'\"'<<sym.recurrences[i]<<'\"';}
    j<<"]},\n  \"candidates\": [\n";
    for(size_t i=0;i<cat.names.size();++i){j<<"    {\"name\": \""<<cat.names[i]<<"\", \"proper\": "<<st[i].proper<<", \"saturated\": "<<st[i].saturated<<", \"hostile\": "<<st[i].hostile<<", \"sizes\": "<<st[i].sizes.size()<<", \"selected\": "<<(selection.count(cat.names[i])?"true":"false")<<"}"<<(i+1==cat.names.size()?"\n":",\n");}j<<"  ]\n}\n";
    if(!heldout){std::vector<size_t>ord(cat.names.size());std::iota(ord.begin(),ord.end(),0);std::sort(ord.begin(),ord.end(),[&](size_t a,size_t b){if(st[a].hostile!=st[b].hostile)return st[a].hostile>st[b].hostile;if(st[a].proper!=st[b].proper)return st[a].proper>st[b].proper;if(st[a].sizes.size()!=st[b].sizes.size())return st[a].sizes.size()>st[b].sizes.size();return cat.names[a]<cat.names[b];});std::ofstream s(out/"F263-D01.selection.tsv");s<<"rank\tname\thostile_hits\tproper_hits\tsizes\n";for(size_t k=0;k<std::min<size_t>(64,ord.size());++k){size_t i=ord[k];s<<k+1<<'\t'<<cat.names[i]<<'\t'<<st[i].hostile<<'\t'<<st[i].proper<<'\t'<<st[i].sizes.size()<<'\n';}}
}

static std::set<std::string> read_selection(const std::string&path,const Catalog&cat){
    std::ifstream f(path);if(!f)fail("cannot read selection");std::string line;std::getline(f,line);std::set<std::string>s;
    while(std::getline(f,line)){std::istringstream q(line);std::string rank,name;if(!std::getline(q,rank,'\t')||!std::getline(q,name,'\t'))fail("bad selection row");if(!cat.idx.count(name))fail("unknown selected syntax");s.insert(name);}if(s.size()!=64)fail("selection must contain 64 distinct candidates");return s;
}

static std::vector<RowResult> run_rows(const std::vector<Labelled>&in,const Catalog&cat,unsigned threads){
    if(threads<1||threads>8)fail("threads outside frozen range");std::vector<RowResult>out(in.size());std::atomic<size_t>next{0};std::vector<std::thread>pool;
    for(unsigned t=0;t<threads;++t)pool.emplace_back([&]{for(;;){size_t i=next.fetch_add(1);if(i>=in.size())break;out[i]=analyze(in[i],cat);}});for(auto&t:pool)t.join();return out;
}

static void self_test(){
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
    Catalog c=build_catalog();if(c.names.size()!=148)fail("candidate count drift: "+std::to_string(c.names.size()));
    {
        const uint128_t test_n=15;
        Eval e(c,test_n);
        e.divisor(c.names[0],uint128_t(15),"saturated-first",1);
        e.divisor(c.names[0],uint128_t(3),"proper-second",2);
        if(e.status[0]!=1||e.first_divisor!="3")fail("saturated-before-proper ordering");
    }
    if(accepts_pair(17,37,"bounded_capacity")||accepts_pair(17,17,"random")||
       !accepts_pair(17,19,"bounded_capacity"))fail("attempt-cap acceptance predicate");
    if(literal_hash("bounded_capacity")!=12148366553126710945ULL)fail("literal cohort hash drift");
    Labelled bounded=make_row(16,"bounded_capacity",0,0);
    if(std::gcd(bounded.p-1,bounded.q-1)>16)fail("bounded-capacity generator");
    if(s.identities.size()!=s.sparse_relations||s.recurrences.size()!=4)fail("symbolic output retention");
    std::cout<<"SELF_TEST_PASS controls="<<s.controls<<" columns="<<s.columns<<" ranks="<<s.rank1<<','<<s.rank2<<" nullities="<<s.nullity1<<','<<s.nullity2<<" identities="<<s.sparse_relations<<" shortcuts="<<s.shortcuts<<" adjacent="<<s.adjacent_recurrences<<" dyadic="<<s.dyadic_recurrences<<" candidates="<<c.names.size()<<"\n";
}

static void benchmark(){
    auto begin=std::chrono::steady_clock::now();SymbolicReport s=symbolic_search();Catalog c=build_catalog();
    uint64_t p=(uint64_t(1)<<60)-93,q=(uint64_t(1)<<60)-33;Labelled x{p,q,uint128_t(p)*q,60,"public_benchmark",0};RowResult r=analyze(x,c);
    double sec=std::chrono::duration<double>(std::chrono::steady_clock::now()-begin).count();
    std::cout<<std::fixed<<std::setprecision(6)<<"BENCHMARK_PASS seconds="<<sec<<" blocks="<<r.queries<<" leaf_touches="<<r.leaves<<" candidates="<<c.names.size()<<" symbolic_columns="<<s.columns<<" symbolic_relations="<<s.sparse_relations<<" shortcuts="<<s.shortcuts<<"\n";
}

int main(int argc,char**argv){
    try{
        if(argc==2&&std::string(argv[1])=="--self-test"){self_test();return 0;}
        if(argc==2&&std::string(argv[1])=="--benchmark"){benchmark();return 0;}
        if(argc==5&&std::string(argv[1])=="--discovery"){
            fs::path out=argv[2];unsigned th=unsigned(std::stoul(argv[3]));if(std::string(argv[4])!="full")fail("frozen mode must be full");
            SymbolicReport s=symbolic_search();Catalog c=build_catalog();auto rows=run_rows(cohort_rows(false),c,th);write_results(out,false,c,s,rows);return 0;
        }
        if(argc==6&&std::string(argv[1])=="--heldout"){
            fs::path out=argv[2];std::string selection=argv[3];unsigned th=unsigned(std::stoul(argv[4]));if(std::string(argv[5])!="full")fail("frozen mode must be full");
            SymbolicReport s=symbolic_search();Catalog c=build_catalog();auto sel=read_selection(selection,c);auto rows=run_rows(cohort_rows(true),c,th);write_results(out,true,c,s,rows,sel);return 0;
        }
        std::cerr<<"usage: symbolic_search --self-test | --benchmark | --discovery OUT THREADS full | --heldout OUT SELECTION THREADS full\n";return 64;
    }catch(const std::exception&e){std::cerr<<"F263_ERROR "<<e.what()<<'\n';return 70;}
}
