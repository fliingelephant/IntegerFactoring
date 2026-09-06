#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <map>
#include <tuple>
#include <vector>

using u64=std::uint64_t;
using u128=__uint128_t;

struct R { u64 p,q,N,B,H,c; int n,K; bool same; };
static int bits(u64 x){return 64-__builtin_clzll(x);}
static u64 inv2(u64 a,u64 m){u64 x=a;for(int i=0;i<6;++i)x*=2-a*x;return x&(m-1);}

int main(){
 constexpr int PL=1<<22,QL=1<<23;
 std::vector<int> spf(QL),ps;
 for(int i=2;i<QL;++i){
  if(!spf[i]){spf[i]=i;ps.push_back(i);}
  for(int p:ps){if(p>spf[i]||(u64)i*p>=QL)break;spf[i*p]=p;}
 }
 std::map<int,std::pair<u64,u64>> byn; // max c, max bit length
 std::array<u64,4> small{};u64 total=0;
 std::vector<R> records,all; long double best=-1;
 for(int pp:ps){
  if(pp>=PL)break;if(pp==2)continue;u64 p=pp;
  for(int n=bits(p*p);n<=bits(2*p*p-1);++n){
   u64 B=u64(1)<<(n/2),r=inv2(p,B);
   std::int64_t k0=((std::int64_t)p-(std::int64_t)r)/(std::int64_t)B-1;
   for(std::int64_t k=std::max<std::int64_t>(0,k0);k<=k0+5;++k){
    u64 q=r+(u64)k*B;if(!(p<q&&q<2*p)||q>=QL||spf[q]!=(int)q)continue;
    u64 N=p*q;if(bits(N)!=n||(N-1)%B)continue;u64 H=(N-1)/B;
    int K=q<2*B?1:2;u64 T=(u64)K*B;
    u64 x=p<T?T-p:p-T,y=q<T?T-q:q-T;bool same=(p<T)==(q<T);
    if(!(0<x&&x<B&&0<y&&y<B)){std::cerr<<"bad range\n";return 2;}
    u64 num=same?x*y-1:x*y+1;if(num%B){std::cerr<<"bad division\n";return 3;}
    u64 c=num/B;if(c>=B){std::cerr<<"bad carry\n";return 4;}
    u64 lhs=(u64)K*(p+q),rhs=(u64)K*K*B+H+(same?-(std::int64_t)c:(std::int64_t)c);
    if(lhs!=rhs){std::cerr<<"bad trace\n";return 5;}
    ++total;for(int a=1;a<=4;++a){u64 z=1;for(int j=0;j<a;++j)z*=n;if(c<=z)++small[a-1];}
    byn[n].first=std::max(byn[n].first,c);byn[n].second=std::max<u64>(byn[n].second,c?bits(c):0);
    long double ratio=(long double)c/B;
    if(ratio>best){best=ratio;records.push_back({p,q,N,B,H,c,n,K,same});}
    all.push_back({p,q,N,B,H,c,n,K,same});
   }
  }
 }
 std::cout<<"TOTAL "<<total<<" SMALL";for(int a=0;a<4;++a)std::cout<<" n^"<<a+1<<":"<<small[a];std::cout<<"\nBY_N";
 for(auto [n,z]:byn)std::cout<<" "<<n<<":"<<z.first<<"/"<<z.second;std::cout<<"\nRECORDS\n";
 for(auto&r:records)std::cout<<r.p<<" "<<r.q<<" N="<<r.N<<" n="<<r.n<<" B="<<r.B<<" H="<<r.H<<" K="<<r.K<<" same="<<r.same<<" c="<<r.c<<" ratio="<<(double)((long double)r.c/r.B)<<"\n";
 std::sort(all.begin(),all.end(),[](const R&a,const R&b){u128 x=(u128)a.c*b.B,y=(u128)b.c*a.B;return x!=y?x>y:a.N>b.N;});
 std::cout<<"TOP10\n";for(int i=0;i<10;++i){auto&r=all[i];std::cout<<r.p<<" "<<r.q<<" N="<<r.N<<" n="<<r.n<<" B="<<r.B<<" H="<<r.H<<" K="<<r.K<<" same="<<r.same<<" c="<<r.c<<" ratio="<<(double)((long double)r.c/r.B)<<"\n";}
}
