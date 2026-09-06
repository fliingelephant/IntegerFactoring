#define main original_scan_main
#include "scan.cpp"
#undef main

// This file intentionally reuses the frozen sieve and arithmetic routines
// from scan.cpp, but has a separate preregistered output contract.
int main(){
 constexpr int PL=1<<22,QL=1<<23;
 std::vector<int> spf(QL),ps;
 for(int i=2;i<QL;++i){if(!spf[i]){spf[i]=i;ps.push_back(i);}for(int p:ps){if(p>spf[i]||(u64)i*p>=QL)break;spf[i*p]=p;}}
 u64 maxord=0,maxres=0;std::vector<Row> records,worst;u64 total=0;
 for(int pp:ps){if(pp>=PL)break;if(pp==2)continue;u64 p=pp;
  for(int n=bitlen(p*p);n<=bitlen(2*p*p-1);++n){u64 B=u64(1)<<(n/2),rr=inverse_odd_power_two(p,B);std::int64_t k0=((std::int64_t)p-(std::int64_t)rr)/(std::int64_t)B-1;
   for(std::int64_t kk=std::max<std::int64_t>(0,k0);kk<=k0+5;++kk){u64 q=rr+(u64)kk*B;if(!(p<q&&q<2*p)||q>=QL||spf[q]!=(int)q)continue;u64 N=p*q;if(bitlen(N)!=n||(N-1)%B)continue;u64 H=(N-1)/B;
    int e=v2(p-1);u64 P=(p-1)>>e,Q=(q-1)>>e,D=std::gcd(P,Q),sp=P/D,sq=Q/D;int K=q<2*B?1:2;u64 T=(u64)K*B,x=p<T?T-p:p-T,y=q<T?T-q:q-T;bool same=(p<T)==(q<T);u64 c=((same?x*y-1:x*y+1)/B);
    u64 A=(u64)K*(N+1)-(u64)K*K*B-H;
    auto check=[&](u64 s){if(s==1)return true;u64 lhs=A%s,rhs=c%s;if(same&&rhs)rhs=s-rhs;return lhs==rhs;};if(!check(sp)||!check(sq)){std::cerr<<"bad congruence\n";return 2;}
    u64 cp=remove_supported_primes(sp,A),cq=remove_supported_primes(sq,A);u64 op=multiplicative_order(A%cp,cp,spf),oq=multiplicative_order(A%cq,cq,spf),mo=std::min(op,oq);
    auto wr=[&](u64 s){if(s==1)return u64(1);u64 w=1%s;for(int j=1;j<=n;++j)w=(u128)w*((powmod(A,j,s)+s-1)%s)%s;return s/std::gcd(s,w);};u64 mr=std::min(wr(sp),wr(sq));
    Row row{p,q,N,B,H,sp,sq,n,e,D,op,oq,0,0,{mr,0,0,0,0}};++total;bool rec=false;if(mo>maxord){maxord=mo;rec=true;}if(mr>maxres){maxres=mr;rec=true;}if(rec)records.push_back(row);worst.push_back(row);
   }
  }
 }
 std::cout<<"TOTAL "<<total<<" MAX_MIN_ORDER "<<maxord<<" MAX_MIN_RESIDUAL "<<maxres<<"\nRECORDS "<<records.size()<<"\n";for(auto&r:records)print_row(r,spf);
 std::sort(worst.begin(),worst.end(),[](const Row&a,const Row&b){return a.residual[0]!=b.residual[0]?a.residual[0]>b.residual[0]:a.N>b.N;});std::cout<<"WORST\n";for(int i=0;i<10;++i)print_row(worst[i],spf);
}
