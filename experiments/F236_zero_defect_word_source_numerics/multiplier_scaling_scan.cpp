#define main original_scan_main
#include "scan.cpp"
#undef main
struct Z{u64 p,q,N,B;int n;std::array<u64,3>b;std::array<int,3>u;};
int main(){constexpr int PL=1<<22,QL=1<<23;std::vector<int>spf(QL),ps;for(int i=2;i<QL;++i){if(!spf[i]){spf[i]=i;ps.push_back(i);}for(int p:ps){if(p>spf[i]||(u64)i*p>=QL)break;spf[i*p]=p;}}
 std::array<u64,3>mx{};std::array<std::map<int,u64>,3>byn;std::array<std::vector<Z>,3>rec;std::vector<Z>all;
 for(int pp:ps){if(pp>=PL)break;if(pp==2)continue;u64 p=pp;for(int n=bitlen(p*p);n<=bitlen(2*p*p-1);++n){u64 B=u64(1)<<(n/2),rr=inverse_odd_power_two(p,B);std::int64_t k0=((std::int64_t)p-(std::int64_t)rr)/(std::int64_t)B-1;for(std::int64_t kk=std::max<std::int64_t>(0,k0);kk<=k0+5;++kk){u64 q=rr+(u64)kk*B,N=p*q;if(!(p<q&&q<2*p)||q>=QL||spf[q]!=(int)q||bitlen(N)!=n||(N-1)%B)continue;Z z{p,q,N,B,n,{~u64(0),~u64(0),~u64(0)},{}};u64 U3=(u64)n*n*n;
  for(u64 u=1;u<=U3;++u){u64 ap=u*p,aq=u*q,Kp=(ap+B/2)/B,Kq=(aq+B/2)/B;std::int64_t x=(std::int64_t)ap-(std::int64_t)Kp*B,y=(std::int64_t)aq-(std::int64_t)Kq*B;__int128 num=(__int128)x*y-(__int128)u*u;if(num%(std::int64_t)B){std::cerr<<"bad\n";return 2;}auto cc=num/(std::int64_t)B;u64 c=cc<0?(u64)(-cc):(u64)cc;std::array<u64,3>caps{(u64)n,(u64)n*n,U3};for(int j=0;j<3;++j)if(u<=caps[j]&&c<z.b[j]){z.b[j]=c;z.u[j]=u;}}
  for(int j=0;j<3;++j){bool is=z.b[j]>mx[j];if(is)mx[j]=z.b[j];byn[j][n]=std::max(byn[j][n],z.b[j]);if(is)rec[j].push_back(z);}all.push_back(z);
 }}}
 auto pr=[](const Z&z){std::cout<<z.p<<" "<<z.q<<" N="<<z.N<<" n="<<z.n<<" B="<<z.B<<" best=["<<z.b[0]<<"@"<<z.u[0]<<","<<z.b[1]<<"@"<<z.u[1]<<","<<z.b[2]<<"@"<<z.u[2]<<"]\n";};for(int j=0;j<3;++j){std::cout<<"CAP n^"<<j+1<<" MAX "<<mx[j]<<" BY_N";for(auto[n,t]:byn[j])std::cout<<" "<<n<<":"<<t;std::cout<<"\nRECORDS\n";for(auto&z:rec[j])pr(z);}std::sort(all.begin(),all.end(),[](auto&a,auto&b){return a.b[2]!=b.b[2]?a.b[2]>b.b[2]:a.N>b.N;});std::cout<<"TOP10_CUBE\n";for(int i=0;i<10;++i)pr(all[i]);}
