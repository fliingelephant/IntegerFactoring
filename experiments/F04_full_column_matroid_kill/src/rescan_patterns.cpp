#include <flint/nmod.h>
#include <algorithm>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <stdexcept>
#include <string>
#include <thread>
#include <tuple>
#include <vector>

namespace {
constexpr std::uint64_t P=100000007ULL,Q=199999991ULL;
constexpr std::uint32_t A=2942,E=11;
std::uint32_t u32(std::istream& s){std::uint32_t x=0;for(int k=0;k<4;++k){int b=s.get();if(b==EOF)throw std::runtime_error("EOF");x|=std::uint32_t(b)<<(8*k);}return x;}
std::uint64_t u64(std::istream& s){std::uint64_t x=0;for(int k=0;k<8;++k){int b=s.get();if(b==EOF)throw std::runtime_error("EOF");x|=std::uint64_t(b)<<(8*k);}return x;}
std::vector<std::uint64_t> load(const std::string& path,std::uint64_t prime){
 std::ifstream in(path,std::ios::binary);char magic[8];in.read(magic,8);if(!in||std::string(magic,8)!="F04CMAT1"||u32(in)!=1||u32(in)!=A||u32(in)!=E||u64(in)!=prime)throw std::runtime_error("header");
 std::vector<std::uint64_t> c(std::size_t(A)*E);for(auto&x:c)x=u64(in);if(in.peek()!=EOF)throw std::runtime_error("trailing");return c;
}
struct Z{std::uint32_t i1,i2,j1,j2;std::uint64_t p,q;};
std::uint64_t minor(const std::vector<std::uint64_t>&c,std::uint32_t i1,std::uint32_t i2,std::uint32_t j1,std::uint32_t j2,nmod_t m){
 auto at=[&](std::uint32_t i,std::uint32_t j){return c[std::size_t(i)*E+j];};return nmod_sub(nmod_mul(at(i1,j1),at(i2,j2),m),nmod_mul(at(i1,j2),at(i2,j1),m),m);
}
}
int main(int argc,char**argv){
 try{
  if(argc!=9)throw std::runtime_error("usage");std::string pp,qq,out,summary;
  for(int i=1;i<argc;i+=2){std::string k=argv[i],v=argv[i+1];if(k=="--c-p")pp=v;else if(k=="--c-q")qq=v;else if(k=="--output")out=v;else if(k=="--summary")summary=v;else throw std::runtime_error("option");}
  auto cp=load(pp,P),cq=load(qq,Q);constexpr unsigned T=10;std::vector<std::vector<Z>> local(T);std::vector<std::thread> threads;
  for(unsigned t=0;t<T;++t)threads.emplace_back([&,t](){nmod_t mp,mq;nmod_init(&mp,P);nmod_init(&mq,Q);unsigned pair=0;
   for(std::uint32_t j1=0;j1+1<E;++j1)for(std::uint32_t j2=j1+1;j2<E;++j2,++pair)if(pair%T==t)
    for(std::uint32_t i2=1;i2<A;++i2)for(std::uint32_t i1=0;i1<i2;++i1){auto p=minor(cp,i1,i2,j1,j2,mp),q=minor(cq,i1,i2,j1,j2,mq);if(p==0||q==0)local[t].push_back({i1,i2,j1,j2,p,q});}
  });
  for(auto&t:threads)t.join();std::vector<Z> z;for(auto&v:local)z.insert(z.end(),v.begin(),v.end());std::sort(z.begin(),z.end(),[](auto&a,auto&b){return std::tie(a.i1,a.i2,a.j1,a.j2)<std::tie(b.i1,b.i2,b.j1,b.j2);});
  std::ofstream f(out);f<<"base_row_1,base_row_2,extra_column_1,extra_column_2,p_value,q_value,p_zero,q_zero\n";std::uint64_t zp=0,zq=0;
  for(auto&r:z){zp+=r.p==0;zq+=r.q==0;f<<r.i1<<','<<r.i2<<','<<r.j1<<','<<r.j2<<','<<r.p<<','<<r.q<<','<<(r.p==0)<<','<<(r.q==0)<<'\n';}
  std::ofstream s(summary);s<<"{\n  \"status\": \"pass\",\n  \"loop_order\": \"extra-column pairs, upper row, lower row\",\n  \"statuses\": 237941605,\n  \"zero_p\": "<<zp<<",\n  \"zero_q\": "<<zq<<",\n  \"union_records\": "<<z.size()<<"\n}\n";
  std::cout<<"independent rescan records="<<z.size()<<'\n';return 0;
 }catch(const std::exception&e){std::cerr<<"rescan_patterns: "<<e.what()<<'\n';return 1;}
}

