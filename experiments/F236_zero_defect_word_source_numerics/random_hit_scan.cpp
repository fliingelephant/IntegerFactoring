#define main original_scan_main
#include "scan.cpp"
#undef main
struct Z{u64 p,q,N,B,U;int n;std::array<u64,3>hits;};
int main(){constexpr int PL=1<<22,QL=1<<23;std::vector<int>spf(QL),ps;for(int i=2;i<QL;++i){if(!spf[i]){spf[i]=i;ps.push_back(i);}for(int p:ps){if(p>spf[i]||(u64)i*p>=QL)break;spf[i*p]=p;}}
 std::array<long double,3>mn{2,2,2};std::array<std::map<int,long double>,3>byn;std::array<std::vector<Z>,3>rec;std::vector<Z>all;
 for(int pp:ps){if(pp>=PL)break;if(pp==2)continue;u64 p=pp;for(int n=bitlen(p*p);n<=bitlen(2*p*p-1);++n){u64 B=u64(1)<<(n/2),rr=inverse_odd_power_two(p,B);std::int64_t k0=((std::int64_t)p-(std::int64_t)rr)/(std::int64_t)B-1;for(std::int64_t kk=std::max<std::int64_t>(0,k0);kk<=k0+5;++kk){u64 q=rr+(u64)kk*B,N=p*q;if(!(p<q&&q<2*p)||q>=QL||spf[q]!=(int)q||bitlen(N)!=n||(N-1)%B)continue;u64 U=(u64)n*n*n;Z z{p,q,N,B,U,n,{}};std::array<u64,3>C{(u64)n,(u64)n*n,U};for(u64 u=1;u<=U;++u){u64 ap=u*p,aq=u*q,Kp=(ap+B/2)/B,Kq=(aq+B/2)/B;std::int64_t x=(std::int64_t)ap-(std::int64_t)Kp*B,y=(std::int64_t)aq-(std::int64_t)Kq*B;__int128 cc=((__int128)x*y-(__int128)u*u)/(std::int64_t)B;u64 c=cc<0?(u64)(-cc):(u64)cc;for(int j=0;j<3;++j)if(c<=C[j])++z.hits[j];}
  for(int j=0;j<3;++j){long double f=(long double)z.hits[j]/U;bool is=f<mn[j];if(is)mn[j]=f;if(!byn[j].count(n)||f<byn[j][n])byn[j][n]=f;if(is)rec[j].push_back(z);}all.push_back(z);
 }}}
 auto pr=[](auto&z,int j){std::cout<<z.p<<" "<<z.q<<" N="<<z.N<<" n="<<z.n<<" B="<<z.B<<" hits="<<z.hits[j]<<"/"<<z.U<<" fraction="<<(double)((long double)z.hits[j]/z.U)<<"\n";};for(int j=0;j<3;++j){std::cout<<"THRESH n^"<<j+1<<" MIN "<<(double)mn[j]<<" BY_N";for(auto[n,f]:byn[j])std::cout<<" "<<n<<":"<<(double)f;std::cout<<"\nRECORDS\n";for(auto&z:rec[j])pr(z,j);}std::sort(all.begin(),all.end(),[](auto&a,auto&b){u128 x=(u128)a.hits[0]*b.U,y=(u128)b.hits[0]*a.U;return x!=y?x<y:a.N>b.N;});std::cout<<"LOW10\n";for(int i=0;i<10;++i)pr(all[i],0);}
