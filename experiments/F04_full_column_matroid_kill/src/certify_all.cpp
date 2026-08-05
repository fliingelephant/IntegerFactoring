#include <flint/nmod.h>
#include <flint/nmod_mat.h>

#include <algorithm>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <numeric>
#include <sstream>
#include <stdexcept>
#include <string>
#include <vector>

namespace {
constexpr std::uint64_t N=20000000499999937ULL, P=100000007ULL, Q=199999991ULL;
constexpr std::uint32_t A=2942, R=2953, EXTRA=11;

std::uint32_t read_u32(std::istream& s) {
    std::uint32_t x=0; for (unsigned k=0;k<4;++k) { int b=s.get(); if(b==EOF) throw std::runtime_error("EOF"); x|=std::uint32_t(b)<<(8*k); } return x;
}
std::uint64_t read_u64(std::istream& s) {
    std::uint64_t x=0; for (unsigned k=0;k<8;++k) { int b=s.get(); if(b==EOF) throw std::runtime_error("EOF"); x|=std::uint64_t(b)<<(8*k); } return x;
}

std::vector<std::uint64_t> load_global(const std::string& path) {
    std::ifstream in(path,std::ios::binary); char magic[8]; in.read(magic,8);
    if (!in || std::string(magic,8)!="F04FCM01") throw std::runtime_error("bad global magic");
    if (read_u32(in)!=1 || read_u32(in)!=A || read_u32(in)!=R || read_u32(in)!=1 || read_u32(in)!=A ||
        read_u64(in)!=N || read_u64(in)!=P || read_u64(in)!=Q || read_u64(in)!=std::uint64_t(A)*R)
        throw std::runtime_error("bad global header");
    std::vector<std::uint64_t> g(std::size_t(A)*R);
    for (std::uint32_t i=0;i<A;++i) {
        if (read_u32(in)!=i+1) throw std::runtime_error("bad shift");
        for (std::uint32_t j=0;j<R;++j) g[std::size_t(i)*R+j]=read_u64(in);
    }
    if (in.peek()!=EOF) throw std::runtime_error("trailing global bytes");
    return g;
}

std::vector<std::uint64_t> load_c(const std::string& path,std::uint64_t prime) {
    std::ifstream in(path,std::ios::binary); char magic[8]; in.read(magic,8);
    if(!in || std::string(magic,8)!="F04CMAT1" || read_u32(in)!=1 || read_u32(in)!=A ||
       read_u32(in)!=EXTRA || read_u64(in)!=prime) throw std::runtime_error("bad C header");
    std::vector<std::uint64_t> c(std::size_t(A)*EXTRA);
    for(auto& x:c) x=read_u64(in);
    if(in.peek()!=EOF) throw std::runtime_error("trailing C bytes");
    return c;
}

struct Record { std::uint32_t i1,i2,j1,j2; std::uint64_t vp,vq; int zp,zq; };
std::vector<Record> load_records(const std::string& path) {
    std::ifstream in(path); std::string line; std::getline(in,line); std::vector<Record> out;
    while(std::getline(in,line)) {
        std::replace(line.begin(),line.end(),',',' '); std::istringstream row(line); Record r{};
        row>>r.i1>>r.i2>>r.j1>>r.j2>>r.vp>>r.vq>>r.zp>>r.zq;
        if(!row) throw std::runtime_error("bad CSV record");
        if(r.zp!=r.zq) out.push_back(r);
    }
    return out;
}

std::uint64_t det2(const std::vector<std::uint64_t>& c,const Record& r,std::uint64_t prime) {
    nmod_t mod; nmod_init(&mod,prime);
    auto at=[&](std::uint32_t i,std::uint32_t j){return c[std::size_t(i)*EXTRA+j];};
    return nmod_sub(nmod_mul(at(r.i1,r.j1),at(r.i2,r.j2),mod),
                    nmod_mul(at(r.i1,r.j2),at(r.i2,r.j1),mod),mod);
}

int sign(const Record& r) {
    const std::uint64_t exponent=(r.i1+1)+(r.i2+1)+(A-1)+A;
    return exponent%2 ? -1:1;
}

std::uint64_t signed_product(std::uint64_t delta,std::uint64_t quotient,int s,std::uint64_t prime) {
    nmod_t mod; nmod_init(&mod,prime); auto x=nmod_mul(delta,quotient,mod);
    return s==1 || x==0 ? x:prime-x;
}

std::uint64_t direct_det(const std::vector<std::uint64_t>& g,std::uint64_t prime,const Record& r) {
    std::vector<std::uint32_t> cols; cols.reserve(A);
    for(std::uint32_t j=0;j<A;++j) if(j!=r.i1 && j!=r.i2) cols.push_back(j);
    cols.push_back(A+r.j1); cols.push_back(A+r.j2);
    nmod_mat_t m; nmod_mat_init(m,A,A,prime);
    for(std::uint32_t i=0;i<A;++i) for(std::uint32_t j=0;j<A;++j)
        nmod_mat_entry(m,i,j)=g[std::size_t(i)*R+cols[j]]%prime;
    auto d=nmod_mat_det(m); nmod_mat_clear(m); return d;
}

std::uint64_t crt(std::uint64_t xp,std::uint64_t xq) {
    auto inv=n_invmod(P%Q,Q); auto t=std::uint64_t((static_cast<unsigned __int128>((xq+Q-xp%Q)%Q)*inv)%Q);
    return xp+P*t;
}
}

int main(int argc,char** argv) {
    try {
        if(argc!=13) throw std::runtime_error("expected six named path options");
        std::string global,cp_path,cq_path,records_path,out_path,summary_path;
        for(int i=1;i<argc;i+=2) {
            std::string key=argv[i],value=argv[i+1];
            if(key=="--global") global=value; else if(key=="--c-p") cp_path=value;
            else if(key=="--c-q") cq_path=value; else if(key=="--records") records_path=value;
            else if(key=="--output") out_path=value; else if(key=="--summary") summary_path=value;
            else throw std::runtime_error("unknown option "+key);
        }
        auto g=load_global(global);
        auto cp=load_c(cp_path,P);
        auto cq=load_c(cq_path,Q);
        auto records=load_records(records_path);
        if(records.empty()) throw std::runtime_error("no mismatches to certify");
        constexpr std::uint64_t delta_p=56136614,delta_q=132391112;
        std::ofstream out(out_path); out<<"base_row_1,base_row_2,extra_column_1,extra_column_2,sign,quotient_p,quotient_q,formula_p,formula_q,direct_p,direct_q,global_value,gcd_N\n";
        for(const auto& r:records) {
            auto qp=det2(cp,r,P),qq=det2(cq,r,Q); if(qp!=r.vp || qq!=r.vq) throw std::runtime_error("C minor mismatch");
            int s=sign(r); auto fp=signed_product(delta_p,qp,s,P),fq=signed_product(delta_q,qq,s,Q);
            auto dp=direct_det(g,P,r),dq=direct_det(g,Q,r); if(fp!=dp || fq!=dq) throw std::runtime_error("direct identity mismatch");
            auto value=crt(dp,dq), factor=std::gcd(value,N); if(factor==1 || factor==N) throw std::runtime_error("trivial gcd");
            out<<r.i1<<','<<r.i2<<','<<r.j1<<','<<r.j2<<','<<s<<','<<qp<<','<<qq<<','<<fp<<','<<fq<<','<<dp<<','<<dq<<','<<value<<','<<factor<<'\n';
        }
        std::ofstream summary(summary_path); summary<<"{\n  \"status\": \"pass\",\n  \"mismatches_certified\": "<<records.size()<<",\n  \"direct_local_exchange_determinants\": "<<2*records.size()<<"\n}\n";
        std::cout<<"certified all "<<records.size()<<" mismatches\n";
        return 0;
    } catch(const std::exception& e) { std::cerr<<"certify_all: "<<e.what()<<'\n'; return 1; }
}
