#define main original_scan_main
#include "scan.cpp"
#undef main

struct TRow { Row r; u64 c,t; };
int main(){
 constexpr int PL=1<<22,QL=1<<23;std::vector<int>spf(QL),ps;
 for(int i=2;i<QL;++i){if(!spf[i]){spf[i]=i;ps.push_back(i);}for(int p:ps){if(p>spf[i]||(u64)i*p>=QL)break;spf[i*p]=p;}}
 u64 best=0,bestD1=0,bestSafe=0;std::map<int,u64>byn;std::vector<TRow>records,all;
 for(int pp:ps){if(pp>=PL)break;if(pp==2)continue;u64 p=pp;
  for(int n=bitlen(p*p);n<=bitlen(2*p*p-1);++n){u64 B=u64(1)<<(n/2),rr=inverse_odd_power_two(p,B);std::int64_t k0=((std::int64_t)p-(std::int64_t)rr)/(std::int64_t)B-1;
   for(std::int64_t kk=std::max<std::int64_t>(0,k0);kk<=k0+5;++kk){u64 q=rr+(u64)kk*B;if(!(p<q&&q<2*p)||q>=QL||spf[q]!=(int)q)continue;u64 N=p*q;if(bitlen(N)!=n||(N-1)%B)continue;u64 H=(N-1)/B;int e=v2(p-1);u64 P=(p-1)>>e,Q=(q-1)>>e,D=std::gcd(P,Q),sp=P/D,sq=Q/D;
    int K=q<2*B?1:2;u64 Z=(u64)K*B,x=p<Z?Z-p:p-Z,y=q<Z?Z-q:q-Z;bool same=(p<Z)==(q<Z);u64 c=(same?x*y-1:x*y+1)/B,t=std::min({c,sp,sq});Row r{p,q,N,B,H,sp,sq,n,e,D};TRow z{r,c,t};bool rec=false;if(t>best){best=t;rec=true;}byn[n]=std::max(byn[n],t);if(e==1&&D==1)bestD1=std::max(bestD1,t);if(spf[sp]==(int)sp&&spf[sq]==(int)sq)bestSafe=std::max(bestSafe,t);if(rec)records.push_back(z);all.push_back(z);
   }
  }
 }
 auto pr=[&](const TRow&z){auto&r=z.r;std::cout<<"p="<<r.p<<" q="<<r.q<<" N="<<r.N<<" n="<<r.n<<" B="<<r.B<<" e="<<r.e<<" D="<<r.D<<" sp="<<r.sp<<" sq="<<r.sq<<" c="<<z.c<<" T="<<z.t<<"\n";};
 std::cout<<"MAX "<<best<<" MAX_e1_D1 "<<bestD1<<" MAX_SAFE "<<bestSafe<<"\nBY_N";for(auto[n,t]:byn)std::cout<<" "<<n<<":"<<t;std::cout<<"\nRECORDS\n";for(auto&z:records)pr(z);std::sort(all.begin(),all.end(),[](auto&a,auto&b){return a.t!=b.t?a.t>b.t:a.r.N>b.r.N;});std::cout<<"TOP10\n";for(int i=0;i<10;++i)pr(all[i]);
}
