#define main original_scan_main
#include "scan.cpp"
#undef main
struct Z{Row r;u64 best;int bestu;std::vector<u64>cs;};
int main(){constexpr int PL=1<<22,QL=1<<23;std::vector<int>spf(QL),ps;for(int i=2;i<QL;++i){if(!spf[i]){spf[i]=i;ps.push_back(i);}for(int p:ps){if(p>spf[i]||(u64)i*p>=QL)break;spf[i*p]=p;}}
 u64 bestall=0;std::map<int,u64>byn;std::array<u64,4>small{};std::vector<Z>records,all;
 for(int pp:ps){if(pp>=PL)break;if(pp==2)continue;u64 p=pp;for(int n=bitlen(p*p);n<=bitlen(2*p*p-1);++n){u64 B=u64(1)<<(n/2),rr=inverse_odd_power_two(p,B);std::int64_t k0=((std::int64_t)p-(std::int64_t)rr)/(std::int64_t)B-1;for(std::int64_t kk=std::max<std::int64_t>(0,k0);kk<=k0+5;++kk){u64 q=rr+(u64)kk*B;if(!(p<q&&q<2*p)||q>=QL||spf[q]!=(int)q)continue;u64 N=p*q;if(bitlen(N)!=n||(N-1)%B)continue;u64 H=(N-1)/B;int e=v2(p-1);u64 P=(p-1)>>e,Q=(q-1)>>e,D=std::gcd(P,Q),sp=P/D,sq=Q/D;Z z{{p,q,N,B,H,sp,sq,n,e,D},~u64(0),0,{}};
  for(int u=1;u<=n;++u){u64 ap=(u64)u*p,aq=(u64)u*q,Kp=(ap+B/2)/B,Kq=(aq+B/2)/B;std::int64_t x=(std::int64_t)ap-(std::int64_t)Kp*B,y=(std::int64_t)aq-(std::int64_t)Kq*B,num=x*y-(std::int64_t)u*u;if(num%(std::int64_t)B){std::cerr<<"bad div\n";return 2;}std::int64_t c=num/(std::int64_t)B;u64 ac=c<0?-c:c;z.cs.push_back(ac);if(ac<z.best){z.best=ac;z.bestu=u;}}
  bool rec=false;if(z.best>bestall){bestall=z.best;rec=true;}byn[n]=std::max(byn[n],z.best);for(int a=1;a<=4;++a){u64 t=1;for(int j=0;j<a;++j)t*=n;if(z.best<=t)++small[a-1];}if(rec)records.push_back(z);all.push_back(z);
 }}}
 auto pr=[&](auto&z){auto&r=z.r;std::cout<<"p="<<r.p<<" q="<<r.q<<" N="<<r.N<<" n="<<r.n<<" B="<<r.B<<" best="<<z.best<<" u="<<z.bestu<<" cs=[";for(int i=0;i<r.n;++i){if(i)std::cout<<",";std::cout<<z.cs[i];}std::cout<<"]\n";};std::cout<<"MAX "<<bestall<<" SMALL";for(int a=0;a<4;++a)std::cout<<" n^"<<a+1<<":"<<small[a];std::cout<<"\nBY_N";for(auto[n,t]:byn)std::cout<<" "<<n<<":"<<t;std::cout<<"\nRECORDS\n";for(auto&z:records)pr(z);std::sort(all.begin(),all.end(),[](auto&a,auto&b){return a.best!=b.best?a.best>b.best:a.r.N>b.r.N;});std::cout<<"TOP10\n";for(int i=0;i<10;++i)pr(all[i]);}
