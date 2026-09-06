#define main original_scan_main
#include "scan.cpp"
#undef main
struct Z{u64 p,q,N,B;int n;std::array<u64,4>first,hits;};
int main(){constexpr int PL=1<<22,QL=1<<23;std::vector<int>spf(QL),ps;for(int i=2;i<QL;++i){if(!spf[i]){spf[i]=i;ps.push_back(i);}for(int p:ps){if(p>spf[i]||(u64)i*p>=QL)break;spf[i*p]=p;}}
 std::array<u64,4>hitcount{},maxfirst{};std::array<std::map<int,u64>,4>byn;std::array<std::vector<Z>,4>all;
 for(int pp:ps){if(pp>=PL)break;if(pp==2)continue;u64 p=pp;for(int n=bitlen(p*p);n<=bitlen(2*p*p-1);++n){u64 B=u64(1)<<(n/2),rr=inverse_odd_power_two(p,B);std::int64_t k0=((std::int64_t)p-(std::int64_t)rr)/(std::int64_t)B-1;for(std::int64_t kk=std::max<std::int64_t>(0,k0);kk<=k0+5;++kk){u64 q=rr+(u64)kk*B,N=p*q;if(!(p<q&&q<2*p)||q>=QL||spf[q]!=(int)q||bitlen(N)!=n||(N-1)%B)continue;Z z{p,q,N,B,n,{0,0,0,0},{0,0,0,0}};u64 U=(u64)n*n*n;std::array<u64,4>C{1,(u64)n,(u64)n*n,(u64)n*n*n};
  for(u64 u=1;u<=U;++u){u64 ap=u*p,aq=u*q,Kp=(ap+B/2)/B,Kq=(aq+B/2)/B;std::int64_t x=(std::int64_t)ap-(std::int64_t)Kp*B,y=(std::int64_t)aq-(std::int64_t)Kq*B;__int128 num=(__int128)x*y-(__int128)u*u,cc=num/(std::int64_t)B;u64 c=cc<0?(u64)(-cc):(u64)cc;for(int j=0;j<4;++j)if(c<=C[j]){++z.hits[j];if(!z.first[j])z.first[j]=u;}}
  for(int j=0;j<4;++j){if(z.first[j]){++hitcount[j];maxfirst[j]=std::max(maxfirst[j],z.first[j]);byn[j][n]=std::max(byn[j][n],z.first[j]);}all[j].push_back(z);}
 }}}
 auto pr=[](const Z&z,int j){std::cout<<z.p<<" "<<z.q<<" N="<<z.N<<" n="<<z.n<<" B="<<z.B<<" first="<<z.first[j]<<" hits="<<z.hits[j]<<"\n";};for(int j=0;j<4;++j){std::cout<<"THRESH "<<j<<" HITCOUNT "<<hitcount[j]<<" MAXFIRST "<<maxfirst[j]<<" BY_N";for(auto[n,u]:byn[j])std::cout<<" "<<n<<":"<<u;std::cout<<"\nLATEST\n";std::sort(all[j].begin(),all[j].end(),[j](auto&a,auto&b){return a.first[j]!=b.first[j]?a.first[j]>b.first[j]:a.N>b.N;});for(int i=0;i<10;++i)pr(all[j][i],j);}
}
