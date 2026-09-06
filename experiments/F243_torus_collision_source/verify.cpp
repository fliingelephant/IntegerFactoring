#include <algorithm>
#include <array>
#include <bit>
#include <chrono>
#include <cmath>
#include <cstdint>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <sys/resource.h>
#include <tuple>
#include <unordered_map>
#include <utility>
#include <vector>

using u64 = uint64_t;
using u128 = unsigned __int128;
using i128 = __int128;

static std::string decimal(u128 x) {
    if (!x) return "0";
    std::string s;
    while (x) {
        s.push_back(char('0' + x % 10));
        x /= 10;
    }
    std::reverse(s.begin(), s.end());
    return s;
}

struct U256 {
    std::array<u64, 4> w{};
};

static U256 square128(u128 x) {
    u64 a[2] = {u64(x), u64(x >> 64)};
    U256 z;
    for (int i = 0; i < 2; ++i) {
        u128 carry = 0;
        for (int j = 0; j < 2; ++j) {
            int k = i + j;
            u128 cur = u128(a[i]) * a[j] + z.w[k] + carry;
            z.w[k] = u64(cur);
            carry = cur >> 64;
        }
        z.w[i + 2] += u64(carry);
    }
    return z;
}

static U256 mul_small(U256 x, u64 a) {
    u128 carry = 0;
    for (int i = 0; i < 4; ++i) {
        u128 cur = u128(x.w[i]) * a + carry;
        x.w[i] = u64(cur);
        carry = cur >> 64;
    }
    if (carry) throw std::runtime_error("U256 overflow");
    return x;
}

static bool ge256(const U256 &a, const U256 &b) {
    for (int i = 3; i >= 0; --i) {
        if (a.w[i] != b.w[i]) return a.w[i] > b.w[i];
    }
    return true;
}

// Compact SHA-256, used only to implement the frozen input and RNG ordering.
struct Sha256 {
    std::array<uint32_t, 8> h = {0x6a09e667, 0xbb67ae85, 0x3c6ef372,
        0xa54ff53a, 0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19};
    std::array<uint8_t, 64> buf{};
    u64 bits = 0;
    size_t used = 0;

    static uint32_t rotr(uint32_t x, int n) { return (x >> n) | (x << (32 - n)); }

    void block(const uint8_t *p) {
        static constexpr uint32_t K[64] = {
            0x428a2f98,0x71374491,0xb5c0fbcf,0xe9b5dba5,0x3956c25b,0x59f111f1,0x923f82a4,0xab1c5ed5,
            0xd807aa98,0x12835b01,0x243185be,0x550c7dc3,0x72be5d74,0x80deb1fe,0x9bdc06a7,0xc19bf174,
            0xe49b69c1,0xefbe4786,0x0fc19dc6,0x240ca1cc,0x2de92c6f,0x4a7484aa,0x5cb0a9dc,0x76f988da,
            0x983e5152,0xa831c66d,0xb00327c8,0xbf597fc7,0xc6e00bf3,0xd5a79147,0x06ca6351,0x14292967,
            0x27b70a85,0x2e1b2138,0x4d2c6dfc,0x53380d13,0x650a7354,0x766a0abb,0x81c2c92e,0x92722c85,
            0xa2bfe8a1,0xa81a664b,0xc24b8b70,0xc76c51a3,0xd192e819,0xd6990624,0xf40e3585,0x106aa070,
            0x19a4c116,0x1e376c08,0x2748774c,0x34b0bcb5,0x391c0cb3,0x4ed8aa4a,0x5b9cca4f,0x682e6ff3,
            0x748f82ee,0x78a5636f,0x84c87814,0x8cc70208,0x90befffa,0xa4506ceb,0xbef9a3f7,0xc67178f2};
        uint32_t w[64];
        for (int i = 0; i < 16; ++i)
            w[i] = uint32_t(p[4*i]) << 24 | uint32_t(p[4*i+1]) << 16 |
                   uint32_t(p[4*i+2]) << 8 | p[4*i+3];
        for (int i = 16; i < 64; ++i) {
            uint32_t s0 = rotr(w[i-15],7) ^ rotr(w[i-15],18) ^ (w[i-15] >> 3);
            uint32_t s1 = rotr(w[i-2],17) ^ rotr(w[i-2],19) ^ (w[i-2] >> 10);
            w[i] = w[i-16] + s0 + w[i-7] + s1;
        }
        uint32_t a=h[0],b=h[1],c=h[2],d=h[3],e=h[4],f=h[5],g=h[6],x=h[7];
        for (int i = 0; i < 64; ++i) {
            uint32_t S1=rotr(e,6)^rotr(e,11)^rotr(e,25);
            uint32_t ch=(e&f)^((~e)&g);
            uint32_t t1=x+S1+ch+K[i]+w[i];
            uint32_t S0=rotr(a,2)^rotr(a,13)^rotr(a,22);
            uint32_t maj=(a&b)^(a&c)^(b&c);
            uint32_t t2=S0+maj;
            x=g; g=f; f=e; e=d+t1; d=c; c=b; b=a; a=t1+t2;
        }
        h[0]+=a;h[1]+=b;h[2]+=c;h[3]+=d;h[4]+=e;h[5]+=f;h[6]+=g;h[7]+=x;
    }

    void add(const void *data, size_t n) {
        const auto *p = static_cast<const uint8_t *>(data);
        bits += 8*n;
        while (n) {
            size_t take = std::min(n, 64-used);
            std::copy(p, p+take, buf.begin()+used);
            used += take; p += take; n -= take;
            if (used == 64) { block(buf.data()); used = 0; }
        }
    }

    std::array<uint8_t,32> finish() {
        u64 original = bits;
        uint8_t one = 0x80; add(&one,1);
        uint8_t zero = 0;
        while (used != 56) add(&zero,1);
        uint8_t len[8];
        for (int i=0;i<8;++i) len[7-i]=uint8_t(original>>(8*i));
        add(len,8);
        std::array<uint8_t,32> out{};
        for (int i=0;i<8;++i) for(int j=0;j<4;++j) out[4*i+j]=uint8_t(h[i]>>(24-8*j));
        return out;
    }
};

static std::array<uint8_t,32> sha(const std::string &s) {
    Sha256 h; h.add(s.data(),s.size()); return h.finish();
}

static std::string hex(const std::array<uint8_t,32> &x) {
    static const char *d="0123456789abcdef";
    std::string s; s.reserve(64);
    for (uint8_t b:x) { s.push_back(d[b>>4]); s.push_back(d[b&15]); }
    return s;
}

static u64 mulmod(u64 a, u64 b, u64 m) { return u64(u128(a)*b%m); }

static u64 powmod(u64 a, u64 e, u64 m) {
    u64 z=1;
    while(e){if(e&1)z=mulmod(z,a,m);a=mulmod(a,a,m);e>>=1;}
    return z;
}

static std::vector<int> sieve(int n) {
    std::vector<bool> ok(n+1,true); ok[0]=ok[1]=false;
    for(int i=2;i*i<=n;++i) if(ok[i]) for(int j=i*i;j<=n;j+=i) ok[j]=false;
    std::vector<int> p; for(int i=2;i<=n;++i) if(ok[i]) p.push_back(i); return p;
}

using Factors=std::vector<std::pair<u64,int>>;

static Factors factor(u64 x,const std::vector<int>& primes) {
    Factors f;
    for(u64 p:primes){if(p*p>x)break;if(x%p==0){int e=0;do{x/=p;++e;}while(x%p==0);f.push_back({p,e});}}
    if(x>1)f.push_back({x,1}); return f;
}

static Factors merge_factors(Factors a,const Factors& b) {
    for(auto [p,e]:b){auto it=std::find_if(a.begin(),a.end(),[&](auto z){return z.first==p;});if(it==a.end())a.push_back({p,e});else it->second+=e;}
    std::sort(a.begin(),a.end()); return a;
}

static void enumerate_divisors(const Factors& f,size_t i,u64 d,std::vector<u64>& out) {
    if(i==f.size()){out.push_back(d);return;}
    u64 x=1;for(int e=0;e<=f[i].second;++e){enumerate_divisors(f,i+1,d*x,out);x*=f[i].first;}
}

static u64 phi_from_factors(u64 x,const Factors& f) {
    u64 z=x;for(auto [p,e]:f)if(x%p==0)z=z/p*(p-1);return z;
}

static u64 order_mod(u64 a,u64 prime,const std::vector<int>& trial) {
    u64 h=prime-1;
    for(auto [r,e]:factor(h,trial)) while(h%r==0&&powmod(a,h/r,prime)==1)h/=r;
    return h;
}

static int legendre(u64 a,u64 p) { u64 x=powmod(a%p,(p-1)/2,p); return x==1?1:-1; }

struct Rat { u128 num=0,den=1,eq=0;u64 aux=0; };

static Rat divisor_law(u64 A,const Factors& f,u64 ell,const std::vector<int>& trial) {
    (void)A;
    std::vector<u64>d;enumerate_divisors(f,0,1,d);
    std::vector<u64> c(ell);
    for(u64 x:d)++c[x%ell];
    u128 num=0;for(u64 x:c)num+=u128(x)*(x-1);
    u64 h=1;
    for(auto [p,e]:f)h=std::lcm(h,order_mod(p%ell,ell,trial));
    return {num,u128(d.size())*d.size(),u128(d.size()),h};
}

static Rat gcd_divisor_law(u64 A,const Factors& f,u64 ell) {
    std::vector<u64>d;enumerate_divisors(f,0,1,d);
    std::vector<u128> c(ell);
    u128 eq=0;
    for(u64 x:d){u64 w=phi_from_factors(A/x,f);c[x%ell]+=w;eq+=u128(w)*w;}
    u128 coll=0;for(u128 x:c)coll+=x*x;
    if(coll<eq)throw std::runtime_error("negative collision energy");
    return {coll-eq,u128(A)*A,eq,0};
}

struct Alg {u64 x,y;};

static Alg amul(Alg a,Alg b,u64 D,u64 ell) {
    return {(mulmod(a.x,b.x,ell)+mulmod(D,mulmod(a.y,b.y,ell),ell))%ell,
            (mulmod(a.x,b.y,ell)+mulmod(a.y,b.x,ell))%ell};
}

static Alg apow(Alg a,u64 e,u64 D,u64 ell) {
    Alg z{1,0};while(e){if(e&1)z=amul(z,a,D,ell);a=amul(a,a,D,ell);e>>=1;}return z;
}

static std::pair<Rat,Rat> pell_laws(u64 N,u64 ell,u64 T,const std::vector<int>& trial) {
    u64 D=(mulmod(N%ell,N%ell,ell)+ell-1)%ell;
    u64 group=ell-legendre(D,ell),h=group;
    Alg eta{N%ell,1};
    for(auto [r,e]:factor(group,trial))while(h%r==0){Alg z=apow(eta,h/r,D,ell);if(z.x==1&&z.y==0)h/=r;else break;}
    u64 q=T/h,r=T%h;
    u128 pairnum=u128(h)*q*(q-1)+u128(2)*r*q;
    std::vector<u64> trace(ell);
    Alg z{1,0};for(u64 k=0;k<T;++k){++trace[z.x];z=amul(z,eta,D,ell);}
    u128 trnum=0;for(u64 x:trace)trnum+=u128(x)*(x-1);
    u128 den=u128(T)*T;
    return {{pairnum,den,T,h},{trnum,den,T,h}};
}

static std::pair<Rat,Rat> box_laws(u64 ell,int B) {
    std::vector<u64> slope(ell+1),orbit(ell+1);
    u64 S=0;
    for(int a=0;a<B;++a)for(int b=0;b<B;++b){
        if((a==0&&b==0)||std::gcd(a,b)!=1)continue;
        u64 t=a%ell?mulmod(b%ell,powmod(a%ell,ell-2,ell),ell):ell;
        ++slope[t];u64 o=t==ell?ell:std::min(t,(ell-t)%ell);++orbit[o];++S;
    }
    u128 det=0,tr=0;for(u64 x:slope)det+=u128(x)*(x-1);for(u64 x:orbit)tr+=u128(x)*(x-1);
    return {{det,u128(S)*S,S,0},{tr,u128(S)*S,S,0}};
}

struct Summary {u64 rows=0,zeros=0,generic=0,useful=0;std::vector<long double> scaled,auxratio;};

static void add_summary(std::map<std::string,Summary>& sums,const std::string& key,u64 ell,const Rat& r) {
    auto &s=sums[key];++s.rows;if(!r.num)++s.zeros;
    if(r.num*ell<=u128(4)*r.den)++s.generic;
    if(ge256(mul_small(square128(r.num),ell),square128(r.den)))++s.useful;
    s.scaled.push_back((long double)ell*(long double)r.num/(long double)r.den);
    if(r.aux)s.auxratio.push_back((long double)r.aux/ell);
}

static void row(std::ofstream& out,std::map<std::string,Summary>& sums,u64 p,u64 q,u64 ell,
                const std::string& source,const std::string& param,const Rat& r) {
    out<<p*q<<'\t'<<p<<'\t'<<q<<'\t'<<ell<<'\t'<<source<<'\t'<<param<<'\t'
       <<decimal(r.num)<<'\t'<<decimal(r.den)<<'\t'<<decimal(r.eq)<<'\t'<<r.aux<<'\n';
    add_summary(sums,source+":"+param,ell,r);
}

struct Xoshiro {
    u64 s[4];
    explicit Xoshiro(const std::string& seed) {
        auto h=sha(seed);
        for(int i=0;i<4;++i){s[i]=0;for(int j=0;j<8;++j)s[i]=(s[i]<<8)|h[8*i+j];}
        if(!(s[0]|s[1]|s[2]|s[3]))s[0]=1;
    }
    static u64 rotl(u64 x,int k){return(x<<k)|(x>>(64-k));}
    u64 next(){u64 z=rotl(s[1]*5,7)*9,t=s[1]<<17;s[2]^=s[0];s[3]^=s[1];s[1]^=s[2];s[0]^=s[3];s[2]^=t;s[3]=rotl(s[3],45);return z;}
    u64 below(u64 n){u64 threshold=-n%n;for(;;){u64 x=next();if(x>=threshold)return x%n;}}
};

static int jacobi(i128 aa,u64 nn) {
    if(nn%2==0||!nn)return 0;
    i128 rem=aa%i128(nn);if(rem<0)rem+=nn;u64 a=u64(rem),n=nn;int t=1;
    while(a){while(!(a&1)){a>>=1;u64 r=n&7;if(r==3||r==5)t=-t;}std::swap(a,n);if((a&3)==3&&(n&3)==3)t=-t;a%=n;}
    return n==1?t:0;
}

static i128 egcd(i128 a,i128 b,i128& x,i128& y) {
    if(!b){x=1;y=0;return a;}i128 x1,y1,g=egcd(b,a%b,x1,y1);x=y1;y=x1-(a/b)*y1;return g;
}

static u64 invmod(u64 a,u64 n) {
    i128 x,y;egcd(a,n,x,y);x%=i128(n);if(x<0)x+=n;return u64(x);
}

static u64 signed_mod(i128 x,u64 m){i128 r=x%i128(m);if(r<0)r+=m;return u64(r);}

static u64 draw_unit_discriminant(Xoshiro& rng,u64 N,int sign) {
    for(;;){u64 D=1+rng.below(N-1);if(std::gcd(D,N)==1&&jacobi(D,N)==sign)return D;}
}

static Alg draw_hilbert(Xoshiro& rng,u64 N,u64 D) {
    for(;;){
        u64 a=rng.below(N),b=rng.below(N);
        u64 a2=mulmod(a,a,N),db2=mulmod(D,mulmod(b,b,N),N);
        u64 nu=(a2+N-db2)%N;if(std::gcd(nu,N)!=1)continue;
        u64 iv=invmod(nu,N);
        return {mulmod((a2+db2)%N,iv,N),mulmod(mulmod(2,a,N),mulmod(b,iv,N),N)};
    }
}

struct Candidate {u64 p,q;std::array<uint8_t,32> digest;};

static std::vector<std::pair<u64,u64>> frozen_inputs(const std::vector<int>& trial,const std::string& run,std::string& digest) {
    std::vector<u64> large,small;
    for(int p:trial){
        if(p>=4096&&p<16384)large.push_back(p);
        if(run=="r1"&&p<512&&(p&1))small.push_back(p);
        if(run=="r2"&&p>=512&&p<4096)small.push_back(p);
    }
    std::vector<Candidate> all;all.reserve(large.size()*(large.size()-1)/2);
    const std::string seed="F243-torus-collision-source-v1";
    for(size_t i=0;i<large.size();++i)for(size_t j=i+1;j<large.size();++j){
        std::string key=seed+":"+std::to_string(large[i])+":"+std::to_string(large[j]);
        all.push_back({large[i],large[j],sha(key)});
    }
    std::sort(all.begin(),all.end(),[](const Candidate&a,const Candidate&b){return a.digest<b.digest;});
    size_t start=run=="r1"?0:20000,stop=start+20000;
    std::vector<std::pair<u64,u64>> out;out.reserve(25000);
    for(size_t i=start;i<stop&&i<all.size();++i)out.push_back({all[i].p,all[i].q});
    if(run=="r1"){
        for(size_t i=0;i<small.size();++i)for(size_t j=i+1;j<small.size();++j)out.push_back({small[i],small[j]});
    }else{
        std::vector<Candidate> edges;edges.reserve(small.size()*(small.size()-1)/2);
        const std::string edge_seed="F243-torus-collision-source-v2";
        for(size_t i=0;i<small.size();++i)for(size_t j=i+1;j<small.size();++j){
            std::string key=edge_seed+":"+std::to_string(small[i])+":"+std::to_string(small[j]);
            edges.push_back({small[i],small[j],sha(key)});
        }
        std::sort(edges.begin(),edges.end(),[](const Candidate&a,const Candidate&b){return a.digest<b.digest;});
        for(size_t i=0;i<5000&&i<edges.size();++i)out.push_back({edges[i].p,edges[i].q});
    }
    std::string transcript;transcript.reserve(out.size()*16);
    for(auto [p,q]:out)transcript+=std::to_string(p)+":"+std::to_string(q)+"\n";
    digest=hex(sha(transcript));return out;
}

static std::set<u64> exterior_targets(u64 p,u64 q,const std::vector<int>& trial) {
    u64 N=p*q,A=N*N-1;std::set<u64> targets;
    for(int ep:{-1,1})for(int eq:{-1,1}){
        u64 mp=ep==1?p-1:p+1,mq=eq==1?q-1:q+1,d=std::gcd(mp,mq);
        for(u64 s:{mp/d,mq/d})for(auto [ell,e]:factor(s,trial))if(A%ell)targets.insert(ell);
    }
    return targets;
}

static void exact_input(u64 p,u64 q,const std::vector<int>& trial,std::ofstream& out,
                        std::map<std::string,Summary>& sums,
                        std::map<std::pair<u64,int>,std::pair<Rat,Rat>>& boxcache) {
    u64 N=p*q,Am=N-1,Ap=N+1,A=N*N-1;
    Factors fm=factor(Am,trial),fp=factor(Ap,trial),fa=merge_factors(fm,fp);
    auto targets=exterior_targets(p,q,trial);
    for(u64 ell:targets){
        row(out,sums,p,q,ell,"divisor","N-1",divisor_law(Am,fm,ell,trial));
        row(out,sums,p,q,ell,"divisor","N+1",divisor_law(Ap,fp,ell,trial));
        row(out,sums,p,q,ell,"divisor","N2-1",divisor_law(A,fa,ell,trial));
        row(out,sums,p,q,ell,"gcd-divisor","N2-1",gcd_divisor_law(A,fa,ell));
        for(u64 T:{8,16,32,64,128}){
            auto [pair,trace]=pell_laws(N,ell,T,trial);
            row(out,sums,p,q,ell,"pell-pair",std::to_string(T),pair);
            row(out,sums,p,q,ell,"pell-trace",std::to_string(T),trace);
        }
        for(int B:{8,16,32,64}){
            auto key=std::make_pair(ell,B);
            auto it=boxcache.find(key);
            if(it==boxcache.end())it=boxcache.emplace(key,box_laws(ell,B)).first;
            row(out,sums,p,q,ell,"box-det",std::to_string(B),it->second.first);
            row(out,sums,p,q,ell,"box-trace",std::to_string(B),it->second.second);
        }
    }
}

static void monte_carlo(u64 p,u64 q,const std::vector<int>& trial,std::ofstream& out,
                        std::map<std::string,Summary>& sums,u64 samples) {
    u64 N=p*q;auto targets=exterior_targets(p,q,trial);if(targets.empty())return;
    int bits=std::bit_width(N);
    for(int sign:{-1,1}){
        Xoshiro rng("F243-discriminant-monte-carlo-v1:"+std::to_string(bits)+":"+std::to_string(sign)+":raw");
        std::map<u64,std::pair<u64,u64>> counts;
        for(u64 k=0;k<samples;++k){u64 a=draw_unit_discriminant(rng,N,sign),b=draw_unit_discriminant(rng,N,sign);for(u64 ell:targets){if(a==b)++counts[ell].second;else if(a%ell==b%ell)++counts[ell].first;}}
        for(u64 ell:targets){auto [hit,eq]=counts[ell];row(out,sums,p,q,ell,"mc-raw-D",std::to_string(sign),{hit,samples,eq,0});}
    }
    std::vector<std::pair<std::string,i128>> fixed={{"-1",-1},{"2",2},{"3",3},{"5",5},{"N-1",i128(N)-1},{"N+1",i128(N)+1}};
    for(auto [tag,raw]:fixed){
        u64 D=signed_mod(raw,N);if(std::gcd(D,N)!=1)continue;
        Xoshiro rng("F243-discriminant-monte-carlo-v1:"+std::to_string(bits)+":"+std::to_string(jacobi(D,N))+":hilbert:"+tag);
        struct C {u64 h0=0,e0=0,h1=0,e1=0,uni=0,det=0,zdet=0;};std::map<u64,C> counts;
        for(u64 k=0;k<samples;++k){
            Alg a=draw_hilbert(rng,N,D),b=draw_hilbert(rng,N,D);i128 det=i128(a.x)*b.y-i128(a.y)*b.x;
            for(u64 ell:targets){auto &c=counts[ell];bool z0=a.x==b.x,z1=a.y==b.y;
                if(z0)++c.e0;else if(a.x%ell==b.x%ell)++c.h0;
                if(z1)++c.e1;else if(a.y%ell==b.y%ell)++c.h1;
                if((!z0&&a.x%ell==b.x%ell)||(!z1&&a.y%ell==b.y%ell))++c.uni;
                if(!det)++c.zdet;else if(signed_mod(det,ell)==0)++c.det;
            }
        }
        for(u64 ell:targets){auto c=counts[ell];
            row(out,sums,p,q,ell,"mc-hilbert-x0",tag,{c.h0,samples,c.e0,0});
            row(out,sums,p,q,ell,"mc-hilbert-x1",tag,{c.h1,samples,c.e1,0});
            row(out,sums,p,q,ell,"mc-hilbert-union",tag,{c.uni,samples,0,0});
            row(out,sums,p,q,ell,"mc-hilbert-det",tag,{c.det,samples,c.zdet,0});
        }
    }
}

static long double quantile(std::vector<long double> v,long double q) {
    if(v.empty())return 0;size_t k=size_t(q*(v.size()-1));std::nth_element(v.begin(),v.begin()+k,v.end());return v[k];
}

int main(int argc,char**argv) {
    try{
        if(hex(sha("abc"))!="ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad")
            throw std::runtime_error("SHA-256 self-test");
        if(invmod(3,11)!=4||jacobi(5,11)!=1||jacobi(2,11)!=-1||
           !ge256(mul_small(square128(1),100),square128(10))||
           ge256(mul_small(square128(1),99),square128(10)))
            throw std::runtime_error("exact arithmetic self-test");
        size_t limit=0;u64 mc_samples=200000;std::string run="r2",prefix="F243_R2";
        for(int i=1;i<argc;++i){std::string a=argv[i];if(a=="--limit"&&i+1<argc)limit=std::stoull(argv[++i]);else if(a=="--mc"&&i+1<argc)mc_samples=std::stoull(argv[++i]);else if(a=="--prefix"&&i+1<argc)prefix=argv[++i];else if(a=="--run"&&i+1<argc)run=argv[++i];else throw std::runtime_error("bad argument");}
        if(run!="r1"&&run!="r2")throw std::runtime_error("run must be r1 or r2");
        auto started=std::chrono::steady_clock::now();auto trial=sieve(16384);std::string input_digest;auto inputs=frozen_inputs(trial,run,input_digest);
        if(limit&&limit<inputs.size())inputs.resize(limit);
        std::ofstream out(prefix+".tsv");out<<"N\tp\tq\tell\tsource\tparam\tnumerator\tdenominator\tequality_numerator\taux\n";
        std::map<std::string,Summary>sums;std::map<std::pair<u64,int>,std::pair<Rat,Rat>>boxcache;
        for(size_t i=0;i<inputs.size();++i){auto[p,q]=inputs[i];exact_input(p,q,trial,out,sums,boxcache);if((i+1)%1000==0)std::cerr<<"exact "<<i+1<<"/"<<inputs.size()<<"\n";}
        if(!limit){
            std::map<int,std::pair<u64,u64>> reps;
            for(auto[p,q]:inputs){int b=std::bit_width(p*q);if(b>=25&&b<=28&&!reps.count(b))reps[b]={p,q};}
            for(auto [b,pq]:reps){std::cerr<<"mc bits "<<b<<" N "<<pq.first*pq.second<<"\n";monte_carlo(pq.first,pq.second,trial,out,sums,mc_samples);}
        }
        out.close();auto elapsed=std::chrono::duration<long double>(std::chrono::steady_clock::now()-started).count();struct rusage ru{};getrusage(RUSAGE_SELF,&ru);
        std::ofstream report(prefix+"_REPORT.md");
        report<<"# F243-"<<(run=="r1"?"R1":"R2")<<" numerical report\n\n- Inputs: "<<inputs.size()<<"\n- Frozen full-input digest: `"<<input_digest<<"`\n- Wall seconds: "<<std::fixed<<std::setprecision(3)<<elapsed<<"\n- Peak RSS KiB: "<<ru.ru_maxrss<<"\n- Monte Carlo pairs per row: "<<(limit?0:mc_samples)<<"\n\n";
        report<<"| source | rows | zero | <=4/ell | >=1/sqrt(ell) | ell*kappa min | q25 | median | q75 | max | aux/ell median |\n|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|\n";
        for(auto &[key,s]:sums){auto mm=std::minmax_element(s.scaled.begin(),s.scaled.end());report<<"| "<<key<<" | "<<s.rows<<" | "<<s.zeros<<" | "<<s.generic<<" | "<<s.useful<<" | "<<double(*mm.first)<<" | "<<double(quantile(s.scaled,.25))<<" | "<<double(quantile(s.scaled,.5))<<" | "<<double(quantile(s.scaled,.75))<<" | "<<double(*mm.second)<<" | "<<double(quantile(s.auxratio,.5))<<" |\n";}
        report<<"\nFinite measurements are guidance only. They do not prove an asymptotic bound.\n";
        std::cout<<"PASS F243-"<<(run=="r1"?"R1":"R2")<<" inputs="<<inputs.size()<<" seconds="<<double(elapsed)<<" rss_kib="<<ru.ru_maxrss<<" digest="<<input_digest<<"\n";
    }catch(const std::exception&e){std::cerr<<"FAIL "<<e.what()<<"\n";return 1;}
}
