#define main original_scan_main
#include "scan.cpp"
#undef main
static u64 invmod(u64 a,u64 m){std::int64_t t=0,nt=1;std::int64_t r=m,nr=a;while(nr){auto q=r/nr;auto z=t-q*nt;t=nt;nt=z;z=r-q*nr;r=nr;nr=z;}if(t<0)t+=m;return t;}
struct Z{u64 p,q,N,B,a;int n;std::array<u64,3>b;std::array<int,3>d;};
int main(){constexpr int PL=1<<22,QL=1<<23;std::vector<int>spf(QL),ps;for(int i=2;i<QL;++i){if(!spf[i]){spf[i]=i;ps.push_back(i);}for(int p:ps){if(p>spf[i]||(u64)i*p>=QL)break;spf[i*p]=p;}}
 std::array<u64,3>mx{};std::array<std::map<int,u64>,3>byn;std::array<std::vector<Z>,3>rec;std::vector<Z>all;
 for(int pp:ps){if(pp>=PL)break;if(pp==2)continue;u64 p=pp;for(int n=bitlen(p*p);n<=bitlen(2*p*p-1);++n){u64 B=u64(1)<<(n/2),rr=inverse_odd_power_two(p,B);std::int64_t k0=((std::int64_t)p-(std::int64_t)rr)/(std::int64_t)B-1;for(std::int64_t kk=std::max<std::int64_t>(0,k0);kk<=k0+5;++kk){u64 q=rr+(u64)kk*B,N=p*q;if(!(p<q&&q<2*p)||q>=QL||spf[q]!=(int)q||bitlen(N)!=n||(N-1)%B)continue;u64 a=(u128)p*invmod(B%q,q)%q;Z z{p,q,N,B,a,n,{~u64(0),~u64(0),~u64(0)},{}};u64 U=(u64)n*n*n;std::array<u64,3>C{(u64)n,(u64)n*n,U};for(u64 d=1;d<=U;++d){u64 v=(u128)d*a%q,r=std::min(v,q-v);for(int j=0;j<3;++j)if(d<=C[j]&&r<z.b[j]){z.b[j]=r;z.d[j]=d;}}
  for(int j=0;j<3;++j){bool is=z.b[j]>mx[j];if(is)mx[j]=z.b[j];byn[j][n]=std::max(byn[j][n],z.b[j]);if(is)rec[j].push_back(z);}all.push_back(z);
 }}}
 auto pr=[](auto&z){std::cout<<z.p<<" "<<z.q<<" N="<<z.N<<" n="<<z.n<<" B="<<z.B<<" a="<<z.a<<" best=["<<z.b[0]<<"@"<<z.d[0]<<","<<z.b[1]<<"@"<<z.d[1]<<","<<z.b[2]<<"@"<<z.d[2]<<"]\n";};for(int j=0;j<3;++j){std::cout<<"CAP n^"<<j+1<<" MAX "<<mx[j]<<" BY_N";for(auto[n,t]:byn[j])std::cout<<" "<<n<<":"<<t;std::cout<<"\nRECORDS\n";for(auto&z:rec[j])pr(z);}std::sort(all.begin(),all.end(),[](auto&a,auto&b){return a.b[2]!=b.b[2]?a.b[2]>b.b[2]:a.N>b.N;});std::cout<<"TOP10\n";for(int i=0;i<10;++i)pr(all[i]);}
