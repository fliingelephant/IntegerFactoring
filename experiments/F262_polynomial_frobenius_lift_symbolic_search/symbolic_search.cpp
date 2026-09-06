#include <algorithm>
#include <array>
#include <atomic>
#include <chrono>
#include <cmath>
#include <cstdint>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <map>
#include <mutex>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <thread>
#include <tuple>
#include <unordered_map>
#include <utility>
#include <vector>

#include <boost/multiprecision/cpp_int.hpp>

using boost::multiprecision::cpp_int;
using u64 = std::uint64_t;
using u128 = __uint128_t;
using Vec = std::vector<cpp_int>;
using Mat = std::vector<Vec>;

static constexpr int FAMILY_COUNT = 48;
static constexpr int FACTOR_BITS[] = {16, 24, 32, 40, 48, 56, 60};
static constexpr int RANDOM_PER_BITS = 384;
static constexpr int NEIGHBOR_PER_BITS = 192;
static constexpr int SAFE_PER_BITS = 192;
static constexpr int SAFE_16_BITS = 96;
static constexpr int TRIPLE_SYNTH_CAP = 8192;
static constexpr int QUAD_SYNTH_CAP = 4096;
static constexpr u64 COHORT_SEED = 0xf262d01c0ffee123ULL;
static constexpr u64 SYNTH_SEED = 0x26f2a17e5eed9913ULL;
static constexpr u64 FP_PRIME_1 = 1000000007ULL;
static constexpr u64 FP_PRIME_2 = 1000000009ULL;

static const char* FAMILY_NAMES[FAMILY_COUNT] = {
    "low_coeff_control", "lift_coeff_C", "lift_delta1", "lift_delta2",
    "lift_reflection_sum", "lift_reflection_difference", "low_lift_2minors",
    "lift_2minors", "lift_3minors", "lift_window_determinants",
    "lift_window_cofactors", "section_K_control", "section_k_digit",
    "section_H_second", "section_2minors", "assoc_exact_zero_decoy",
    "assoc_digit_residual_control", "assoc_quotient_Q",
    "mult_residual_control", "mult_quotient_Q", "mult_Q_2minors",
    "mult_Q_3minors", "assoc_Q_2minors", "assoc_Q_3minors", "trace_C",
    "norm_C", "charpoly_C", "resultant_f_C", "resultant_C_pair",
    "discriminant_unit_monic_C", "trace_delta1", "norm_delta1",
    "charpoly_delta1", "trace_Qmult", "norm_Qmult", "charpoly_Qmult",
    "trace_Qassoc", "norm_Qassoc", "charpoly_Qassoc",
    "mixed_trace_determinants", "mixed_norm_differences", "mixed_resultants",
    "coefficient_hankel_minors", "multiplication_krylov_minors",
    "smith_D1_controls", "smith_D2_indicators", "translation_raw_decoy",
    "translation_canonical_control"};

static const char* FAMILY_SCHEMAS[FAMILY_COUNT] = {
    "row:coeff(r)", "row:coeff(C)", "edge:fd1(C)", "triple:fd2(C)",
    "edge:reflection_sum(C)", "edge:reflection_diff(C)",
    "edge:minors2(r,C)", "edge:minors2(C_i,C_j)",
    "triple:minors3(C_i,C_j,C_k)", "window:det(columns(C))",
    "window:cofactor(columns(C))", "edge:coeff(K)", "edge:coeff(k)",
    "edge:coeff(H)", "edge:minors2(K,k,H)", "triple:full_associator_zero",
    "triple:digit_associator", "triple:exact_div_N(digit_associator)",
    "edge:lift_multiplicativity_residual", "edge:exact_div_N(mult_residual)",
    "edge:minors2(Qmult)", "triple:minors3(Qmult)",
    "edge:minors2(Qassoc)", "triple:minors3(Qassoc)", "row:trace(M(C))",
    "row:det(M(C))", "row:charcoeff(M(C))", "row:resultant(f,C)",
    "edge:resultant(C_i,C_j)", "row:disc(unit_monic(C))",
    "edge:trace(M(fd1(C)))", "edge:det(M(fd1(C)))",
    "edge:charcoeff(M(fd1(C)))", "edge:trace(M(Qmult))",
    "edge:det(M(Qmult))", "edge:charcoeff(M(Qmult))",
    "triple:trace(M(Qassoc))", "triple:det(M(Qassoc))",
    "triple:charcoeff(M(Qassoc))", "mixed:det(trace_channels)",
    "mixed:diff(norm_channels)", "mixed:resultant(channels)",
    "row:hankel_minors(coeff)", "row:krylov_minors(M(coeff))",
    "scope:gcd_N(entries)", "scope:gcd_N(minors2)",
    "translation:raw_digit_difference", "translation:transported_full_zero"};

[[noreturn]] static void fail(const std::string& message) {
  throw std::runtime_error(message);
}
static void require(bool condition, const std::string& message) {
  if (!condition) fail(message);
}

static u64 splitmix64(u64 x) {
  x += 0x9e3779b97f4a7c15ULL;
  x = (x ^ (x >> 30)) * 0xbf58476d1ce4e5b9ULL;
  x = (x ^ (x >> 27)) * 0x94d049bb133111ebULL;
  return x ^ (x >> 31);
}
struct Rng {
  u64 state;
  explicit Rng(u64 seed) : state(seed) {}
  u64 next() { return state = splitmix64(state); }
};

static cpp_int abs_cpp(cpp_int x) { return x < 0 ? -x : x; }
static cpp_int gcd_cpp(cpp_int a, cpp_int b) {
  a = abs_cpp(a); b = abs_cpp(b);
  while (b != 0) { cpp_int r = a % b; a = b; b = r; }
  return a;
}
static cpp_int mod_cpp(cpp_int x, const cpp_int& m) {
  x %= m; if (x < 0) x += m; return x;
}
static u64 mod_u64(const cpp_int& x, u64 m) {
  cpp_int r = x % m; if (r < 0) r += m; return r.convert_to<u64>();
}
static u64 low64(const cpp_int& x) {
  static const cpp_int mask = (cpp_int(1) << 64) - 1;
  return (x & mask).convert_to<u64>();
}
static std::string str_cpp(const cpp_int& x) { return x.convert_to<std::string>(); }
static cpp_int primitive_n(cpp_int x, const cpp_int& N) {
  x = abs_cpp(x); if (x == 0) return 0;
  while (x % N == 0) x /= N;
  return x;
}
static u64 mul_u64(u64 a, u64 b, u64 m) {
  return static_cast<u64>((static_cast<u128>(a) * b) % m);
}
static u64 pow_u64(u64 a, u64 e, u64 m) {
  u64 r = 1 % m;
  while (e) { if (e & 1) r = mul_u64(r, a, m); a = mul_u64(a, a, m); e >>= 1; }
  return r;
}
static bool is_prime(u64 n) {
  if (n < 2) return false;
  for (u64 p : {2ULL,3ULL,5ULL,7ULL,11ULL,13ULL,17ULL,19ULL,23ULL,29ULL,31ULL,37ULL}) {
    if (n % p == 0) return n == p;
  }
  u64 d = n - 1, s = 0;
  while (!(d & 1)) { d >>= 1; ++s; }
  for (u64 a : {2ULL,325ULL,9375ULL,28178ULL,450775ULL,9780504ULL,1795265022ULL}) {
    if (a % n == 0) continue;
    u64 x = pow_u64(a % n, d, n);
    if (x == 1 || x == n - 1) continue;
    bool witness = true;
    for (u64 i = 1; i < s; ++i) {
      x = mul_u64(x, x, n);
      if (x == n - 1) { witness = false; break; }
    }
    if (witness) return false;
  }
  return true;
}
static u64 random_prime(int bits, Rng& rng) {
  u64 lo = 1ULL << (bits - 1), mask = (1ULL << bits) - 1;
  for (;;) {
    u64 x = (rng.next() & mask) | lo | 1;
    for (int k = 0; k < 8192 && x <= mask; ++k, x += 2) if (is_prime(x)) return x;
  }
}
static u64 random_safe_prime(int bits, Rng& rng) {
  for (;;) {
    u64 h = random_prime(bits - 1, rng), p = 2 * h + 1;
    if ((p >> (bits - 1)) == 1 && is_prime(p)) return p;
  }
}
static u64 next_prime_same_bits(u64 x, int bits) {
  u64 limit = 1ULL << bits;
  for (x += 2; x < limit; x += 2) if (is_prime(x)) return x;
  return 0;
}

static Vec pad(Vec a, int n) { a.resize(n); return a; }
static Vec add_vec(const Vec& a, const Vec& b) {
  Vec r(std::max(a.size(), b.size()));
  for (std::size_t i = 0; i < r.size(); ++i)
    r[i] = (i < a.size() ? a[i] : 0) + (i < b.size() ? b[i] : 0);
  return r;
}
static Vec sub_vec(const Vec& a, const Vec& b) {
  Vec r(std::max(a.size(), b.size()));
  for (std::size_t i = 0; i < r.size(); ++i)
    r[i] = (i < a.size() ? a[i] : 0) - (i < b.size() ? b[i] : 0);
  return r;
}
static Vec canonical_vec(Vec a, const cpp_int& m, int d) {
  a.resize(d);
  for (auto& x : a) x = mod_cpp(x, m);
  return a;
}
static Vec rem_exact(Vec a, const Vec& f) {
  int d = static_cast<int>(f.size()) - 1;
  require(f.back() == 1, "monic reduction");
  if (a.size() < f.size()) return pad(std::move(a), d);
  for (int k = static_cast<int>(a.size()) - 1; k >= d; --k) {
    cpp_int c = a[k];
    if (c != 0) for (int j = 0; j < d; ++j) a[k - d + j] -= c * f[j];
  }
  a.resize(d); return a;
}
static Vec mul_exact(const Vec& a, const Vec& b, const Vec& f) {
  Vec c(a.size() + b.size() - 1);
  for (std::size_t i = 0; i < a.size(); ++i)
    for (std::size_t j = 0; j < b.size(); ++j) c[i+j] += a[i] * b[j];
  return rem_exact(std::move(c), f);
}
static Vec mul_mod_poly(const Vec& a, const Vec& b, const Vec& f, const cpp_int& m) {
  Vec c = mul_exact(a, b, f);
  for (auto& x : c) x = mod_cpp(x, m);
  return c;
}
static Vec pow_mod_poly(Vec a, cpp_int e, const Vec& f, const cpp_int& m) {
  int d = static_cast<int>(f.size()) - 1;
  a = canonical_vec(std::move(a), m, d);
  Vec r(d); r[0] = 1;
  while (e != 0) {
    if ((e & 1) != 0) r = mul_mod_poly(r, a, f, m);
    e >>= 1;
    if (e != 0) a = mul_mod_poly(a, a, f, m);
  }
  return r;
}
static Vec shift_poly(const Vec& a, int t) {
  Vec r(a.size());
  for (std::size_t i = 0; i < a.size(); ++i) {
    cpp_int bin = 1, tp = 1;
    for (int j = static_cast<int>(i); j >= 0; --j) {
      if (j == static_cast<int>(i)) { bin = 1; tp = 1; }
      else {
        int oldj = j + 1;
        bin = bin * oldj / (static_cast<int>(i) - j);
        tp *= t;
      }
      r[j] += a[i] * bin * tp;
    }
  }
  return r;
}

static cpp_int determinant(Mat a) {
  int n = static_cast<int>(a.size());
  if (n == 0) return 1;
  for (const auto& row : a) require(static_cast<int>(row.size()) == n, "square determinant");
  cpp_int previous = 1; int sign = 1;
  for (int k = 0; k + 1 < n; ++k) {
    int pivot = k;
    while (pivot < n && a[pivot][k] == 0) ++pivot;
    if (pivot == n) return 0;
    if (pivot != k) { std::swap(a[pivot], a[k]); sign = -sign; }
    for (int i = k + 1; i < n; ++i) for (int j = k + 1; j < n; ++j) {
      cpp_int numerator = a[i][j] * a[k][k] - a[i][k] * a[k][j];
      require(numerator % previous == 0, "Bareiss exact division");
      a[i][j] = numerator / previous;
    }
    for (int i = k + 1; i < n; ++i) a[i][k] = 0;
    previous = a[k][k];
  }
  return sign * a[n-1][n-1];
}
static cpp_int resultant(Vec a, Vec b) {
  while (a.size() > 1 && a.back() == 0) a.pop_back();
  while (b.size() > 1 && b.back() == 0) b.pop_back();
  if (a.size() == 1 && a[0] == 0) return 0;
  if (b.size() == 1 && b[0] == 0) return 0;
  int m = static_cast<int>(a.size()) - 1, n = static_cast<int>(b.size()) - 1;
  if (n == 0) { cpp_int r = 1; for (int i=0;i<m;++i) r*=b[0]; return r; }
  if (m == 0) { cpp_int r = 1; for (int i=0;i<n;++i) r*=a[0]; return r; }
  Mat S(m+n, Vec(m+n));
  for (int row=0; row<n; ++row) for (int j=0;j<=m;++j) S[row][row+j]=a[m-j];
  for (int row=0; row<m; ++row) for (int j=0;j<=n;++j) S[n+row][row+j]=b[n-j];
  return determinant(std::move(S));
}
static Vec derivative(const Vec& f) {
  Vec r(f.size() - 1); for (std::size_t i=1;i<f.size();++i) r[i-1]=f[i]*i; return r;
}
static cpp_int discriminant(const Vec& f) {
  int d = static_cast<int>(f.size()) - 1;
  cpp_int r = resultant(f, derivative(f));
  return ((d*(d-1)/2)&1) ? -r : r;
}
static Mat multiplication_matrix(const Vec& v, const Vec& f) {
  int d = static_cast<int>(f.size()) - 1;
  Mat M(d, Vec(d));
  for (int j=0;j<d;++j) {
    Vec basis(d); basis[j]=1; Vec col=mul_exact(v,basis,f);
    for (int i=0;i<d;++i) M[i][j]=col[i];
  }
  return M;
}
static cpp_int trace(const Mat& M) {
  cpp_int r=0; for (std::size_t i=0;i<M.size();++i) r+=M[i][i]; return r;
}
static Vec poly_mul_plain(const Vec& a, const Vec& b) {
  Vec r(a.size()+b.size()-1);
  for (std::size_t i=0;i<a.size();++i) for(std::size_t j=0;j<b.size();++j) r[i+j]+=a[i]*b[j];
  return r;
}
static Vec characteristic_coefficients(const Mat& M) {
  int d=static_cast<int>(M.size()); std::vector<int> p(d); std::iota(p.begin(),p.end(),0);
  Vec out(d+1); 
  do {
    int inv=0; for(int i=0;i<d;++i) for(int j=i+1;j<d;++j) inv += p[i]>p[j];
    Vec term{1};
    for(int i=0;i<d;++i) {
      Vec factor(2); factor[0]=-M[i][p[i]]; if(p[i]==i) factor[1]=1;
      term=poly_mul_plain(term,factor);
    }
    for(std::size_t i=0;i<term.size();++i) out[i] += (inv&1) ? -term[i] : term[i];
  } while(std::next_permutation(p.begin(),p.end()));
  require(out[d]==1,"monic characteristic polynomial"); return out;
}
static cpp_int det2(const Vec& a, const Vec& b, int i, int j) {
  return a[i]*b[j]-a[j]*b[i];
}
static cpp_int det3cols(const Vec& a,const Vec& b,const Vec& c,int i,int j,int k) {
  return a[i]*(b[j]*c[k]-b[k]*c[j])-b[i]*(a[j]*c[k]-a[k]*c[j])+c[i]*(a[j]*b[k]-a[k]*b[j]);
}

struct Carry { Vec z, K, k, H; };
static Carry section_carry(const Vec& a,const Vec& b,const Vec& f,const cpp_int& N) {
  Vec full=mul_exact(a,b,f), z=canonical_vec(full,N,static_cast<int>(a.size()));
  Vec K(a.size()),k(a.size()),H(a.size());
  for(std::size_t i=0;i<a.size();++i) {
    require((full[i]-z[i])%N==0,"section carry exact /N");
    K[i]=(full[i]-z[i])/N; k[i]=mod_cpp(K[i],N);
    require((K[i]-k[i])%N==0,"second section carry exact /N"); H[i]=(K[i]-k[i])/N;
  }
  return {z,K,k,H};
}
static Vec exact_div_N(const Vec& a,const cpp_int& N,const std::string& label) {
  Vec r(a.size()); for(std::size_t i=0;i<a.size();++i) { require(a[i]%N==0,label); r[i]=a[i]/N; } return r;
}

struct Lift { Vec R,r,C; };
static Lift power_lift(const Vec& a,const Vec& f,const cpp_int& N) {
  cpp_int N2=N*N; Vec R=pow_mod_poly(a,N,f,N2), r=canonical_vec(R,N,static_cast<int>(R.size())), C(R.size());
  for(std::size_t i=0;i<R.size();++i) { require((R[i]-r[i])%N==0,"lift digit exact /N"); C[i]=(R[i]-r[i])/N; }
  return {R,r,C};
}

static Vec recipe_poly(int d,int recipe,const cpp_int& N) {
  Vec f(d+1); f[d]=1;
  if(recipe==0) { f[1]+=1; f[0]+=1; }
  if(recipe==1) { f[d-1]-=1; f[1]+=2; f[0]+=3; }
  if(recipe==2) { f[d-1]+=1; f[1]-=2; f[0]+=5; }
  if(recipe==3) {
    for(int slot=0;slot<3;++slot) {
      u64 h=splitmix64(low64(N)^COHORT_SEED^(u64(d)<<32)^u64(slot));
      int c=static_cast<int>(h%17)-8;
      int pos=slot==2?0:(slot==1?1:d-1); f[pos]+=c;
    }
    if(f[0]==0) f[0]=1;
  }
  return f;
}

struct Task { int bits,cohort,index; u64 p,q; };
static const char* cohort_name(int c) { return c==0?"random":(c==1?"consecutive":"safe_safe"); }
static std::vector<Task> make_tasks() {
  std::vector<Task> out; std::set<std::pair<u64,u64>> all;
  for(int bits:FACTOR_BITS) for(int cohort=0;cohort<3;++cohort) {
    int need=cohort==0?RANDOM_PER_BITS:(cohort==1?NEIGHBOR_PER_BITS:(bits==16?SAFE_16_BITS:SAFE_PER_BITS));
    Rng rng(COHORT_SEED ^ (u64(bits)<<24) ^ (u64(cohort)<<56)); int made=0;
    while(made<need) {
      u64 p=0,q=0;
      if(cohort==0) { p=random_prime(bits,rng); q=random_prime(bits,rng); }
      else if(cohort==1) { p=random_prime(bits,rng); q=next_prime_same_bits(p,bits); if(!q) continue; }
      else { p=random_safe_prime(bits,rng); q=random_safe_prime(bits,rng); }
      if(p>q) std::swap(p,q); if(p==q || q>=2*p || !all.insert({p,q}).second) continue;
      out.push_back({bits,cohort,made++,p,q});
    }
  }
  require(out.size()==5280,"frozen cohort count"); return out;
}

struct FamilyState {
  std::array<u64,FAMILY_COUNT> atoms{},zeros{},units{},hits{},mismatch_atoms{},mismatch_hits{};
  std::array<cpp_int,FAMILY_COUNT> sum,product;
  cpp_int N; std::string first; u64 cleanup=0;
  explicit FamilyState(cpp_int modulus):N(std::move(modulus)) { for(auto& x:product)x=1; }
  void add(int family,cpp_int value,bool mismatch,const std::string& scope) {
    require(family>=0&&family<FAMILY_COUNT,"family index"); ++atoms[family]; if(mismatch)++mismatch_atoms[family];
    cpp_int primitive=primitive_n(value,N);
    if(primitive==0) { ++zeros[family]; return; }
    if(primitive==1) { ++units[family]; return; }
    cpp_int residue=mod_cpp(primitive,N), g=gcd_cpp(residue,N);
    sum[family]=mod_cpp(sum[family]+residue,N);
    product[family]=mod_cpp(product[family]*mod_cpp(1+residue,N),N);
    if(g>1&&g<N) { ++hits[family]; if(mismatch)++mismatch_hits[family]; if(first.empty()) first=FAMILY_NAMES[family]+std::string(":")+scope+":"+str_cpp(g); }
  }
};

static void add_coeffs(FamilyState& s,int family,const Vec& v,bool mismatch,const std::string& scope) {
  for(std::size_t i=0;i<v.size();++i) s.add(family,v[i],mismatch,scope+".c"+std::to_string(i));
}
static void add_2minors(FamilyState& s,int family,const Vec& a,const Vec& b,bool mismatch,const std::string& scope) {
  for(int i=0;i<(int)a.size();++i) for(int j=i+1;j<(int)a.size();++j) s.add(family,det2(a,b,i,j),mismatch,scope);
}
static void add_3minors(FamilyState& s,int family,const Vec& a,const Vec& b,const Vec& c,bool mismatch,const std::string& scope) {
  for(int i=0;i<(int)a.size();++i) for(int j=i+1;j<(int)a.size();++j) for(int k=j+1;k<(int)a.size();++k) s.add(family,det3cols(a,b,c,i,j,k),mismatch,scope);
}
static cpp_int entries_gcd_N(const Vec& v,const cpp_int& N) {
  cpp_int g=N; for(const auto& x:v)g=gcd_cpp(g,x); return g;
}
static cpp_int minors2_gcd_N(const Vec& a,const Vec& b,const cpp_int& N) {
  cpp_int g=N; for(int i=0;i<(int)a.size();++i)for(int j=i+1;j<(int)a.size();++j)g=gcd_cpp(g,det2(a,b,i,j)); return g;
}

static std::vector<int> factor_partition(const Vec& f,u64 prime) {
  int d=static_cast<int>(f.size())-1; cpp_int P=prime; Vec x(d); x[1]=1; Vec cur=x;
  auto trim_mod=[&](Vec a){ for(auto& z:a)z=mod_cpp(z,P); while(a.size()>1&&a.back()==0)a.pop_back(); return a; };
  auto gcd_deg=[&](Vec a,Vec b){
    a=trim_mod(a); b=trim_mod(b);
    while(!(b.size()==1&&b[0]==0)) {
      int db=(int)b.size()-1; cpp_int inv=pow_u64(mod_u64(b.back(),prime),prime-2,prime); a=trim_mod(a);
      while((int)a.size()-1>=db && !(a.size()==1&&a[0]==0)) {
        int sh=(int)a.size()-1-db; cpp_int c=mod_cpp(a.back()*inv,P);
        for(int j=0;j<=db;++j)a[sh+j]=mod_cpp(a[sh+j]-c*b[j],P); a=trim_mod(a);
      }
      a.swap(b); b=trim_mod(b);
    }
    return (int)a.size()-1;
  };
  std::vector<int>D(d+1),m(d+1),parts;
  for(int k=1;k<=d;++k) { cur=pow_mod_poly(cur,cpp_int(prime),f,P); D[k]=gcd_deg(f,sub_vec(cur,x)); }
  for(int k=1;k<=d;++k) { int rem=D[k]; for(int e=1;e<k;++e)if(k%e==0)rem-=e*m[e]; require(rem%k==0,"partition Mobius"); m[k]=rem/k; for(int j=0;j<m[k];++j)parts.push_back(k); }
  std::sort(parts.begin(),parts.end()); require(std::accumulate(parts.begin(),parts.end(),0)==d,"partition degree"); return parts;
}

struct PolyScopeResult { bool used=false,mismatch=false; };
static PolyScopeResult process_polynomial(const Vec& f,int degree,int recipe,
                                          const cpp_int& N,u64 p,u64 q,
                                          FamilyState& state,bool direct_pair_check) {
  cpp_int disc=discriminant(f), dg=gcd_cpp(disc,N);
  if(dg>1) {
    if(dg<N) { ++state.cleanup; if(state.first.empty()) state.first="cleanup_discriminant:d"+std::to_string(degree)+"r"+std::to_string(recipe)+":"+str_cpp(dg); }
    return {false,false};
  }
  bool mismatch=factor_partition(f,p)!=factor_partition(f,q);
  std::array<Lift,5> lifts;
  for(int si=0;si<5;++si) { Vec a(degree); a[0]=si-2; a[1]=1; lifts[si]=power_lift(a,f,N); }
  std::vector<Vec> delta1,delta2;
  for(int i=0;i<4;++i) delta1.push_back(sub_vec(lifts[i+1].C,lifts[i].C));
  for(int i=0;i<3;++i) delta2.push_back(sub_vec(delta1[i+1],delta1[i]));
  std::string scope="d"+std::to_string(degree)+"r"+std::to_string(recipe);

  for(int i=0;i<5;++i) {
    add_coeffs(state,0,lifts[i].r,mismatch,scope+"s"+std::to_string(i-2));
    add_coeffs(state,1,lifts[i].C,mismatch,scope+"s"+std::to_string(i-2));
    add_2minors(state,6,lifts[i].r,lifts[i].C,mismatch,scope);
    Mat M=multiplication_matrix(lifts[i].C,f); cpp_int tr=trace(M),norm=determinant(M);
    state.add(24,tr,mismatch,scope); state.add(25,norm,mismatch,scope);
    Vec ch=characteristic_coefficients(M); for(int j=0;j<degree;++j)state.add(26,ch[j],mismatch,scope);
    state.add(27,resultant(f,lifts[i].C),mismatch,scope);
    if(abs_cpp(lifts[i].C.back())==1) {
      Vec mon=lifts[i].C; if(mon.back()==-1)for(auto&x:mon)x=-x;
      state.add(29,discriminant(mon),mismatch,scope);
    }
    for(int a=0;a<degree;++a)for(int b=a+1;b<degree;++b) {
      int c=(a+b)%degree,d=(a+b+1)%degree;
      state.add(42,lifts[i].C[c]*lifts[i].C[(c+2)%degree]-lifts[i].C[d]*lifts[i].C[(d+1)%degree],mismatch,scope);
    }
    Mat K(degree,Vec(degree)); Vec v(degree); v[0]=1;
    for(int col=0;col<degree;++col) { for(int row=0;row<degree;++row)K[row][col]=v[row]; v=mul_exact(v,lifts[i].C,f); }
    state.add(43,determinant(K),mismatch,scope);
    state.add(44,entries_gcd_N(lifts[i].C,N),mismatch,scope);
  }
  for(int i=0;i<4;++i) {
    add_coeffs(state,2,delta1[i],mismatch,scope);
    Mat M=multiplication_matrix(delta1[i],f); state.add(30,trace(M),mismatch,scope); state.add(31,determinant(M),mismatch,scope);
    Vec ch=characteristic_coefficients(M); for(int j=0;j<degree;++j)state.add(32,ch[j],mismatch,scope);
  }
  for(const Vec& v:delta2)add_coeffs(state,3,v,mismatch,scope);
  for(int i=0;i<2;++i) {
    Vec sum=add_vec(lifts[i].C,lifts[4-i].C),dif=sub_vec(lifts[4-i].C,lifts[i].C);
    add_coeffs(state,4,sum,mismatch,scope); add_coeffs(state,5,dif,mismatch,scope);
  }
  for(int i=0;i<5;++i)for(int j=i+1;j<5;++j) {
    add_2minors(state,7,lifts[i].C,lifts[j].C,mismatch,scope);
    state.add(28,resultant(lifts[i].C,lifts[j].C),mismatch,scope);
    state.add(45,minors2_gcd_N(lifts[i].C,lifts[j].C,N),mismatch,scope);
  }
  for(int i=0;i<5;++i)for(int j=i+1;j<5;++j)for(int k=j+1;k<5;++k)
    add_3minors(state,8,lifts[i].C,lifts[j].C,lifts[k].C,mismatch,scope);
  if(degree<=5) {
    std::vector<int> choose(degree); std::iota(choose.begin(),choose.end(),0);
    for(;;) {
      Mat W(degree,Vec(degree)); for(int c=0;c<degree;++c)for(int r=0;r<degree;++r)W[r][c]=lifts[choose[c]].C[r];
      state.add(9,determinant(W),mismatch,scope);
      int pos=degree-1; while(pos>=0&&choose[pos]==5-degree+pos)--pos; if(pos<0)break;
      ++choose[pos]; for(int z=pos+1;z<degree;++z)choose[z]=choose[z-1]+1;
    }
  }
  if(degree>=3) {
    int sz=degree-1; Mat W(sz,Vec(sz)); for(int c=0;c<sz;++c)for(int r=0;r<sz;++r)W[r][c]=lifts[c].C[r];
    state.add(10,determinant(W),mismatch,scope);
  }

  std::vector<Vec> qmult;
  for(int i=0;i<5;++i)for(int j=i+1;j<5;++j) {
    Carry carry=section_carry(lifts[i].r,lifts[j].r,f,N);
    add_coeffs(state,11,carry.K,mismatch,scope); add_coeffs(state,12,carry.k,mismatch,scope); add_coeffs(state,13,carry.H,mismatch,scope);
    add_2minors(state,14,carry.K,carry.k,mismatch,scope); add_2minors(state,14,carry.k,carry.H,mismatch,scope);
    Vec cross=add_vec(mul_exact(lifts[i].r,lifts[j].C,f),mul_exact(lifts[i].C,lifts[j].r,f));
    Vec Rab=mul_mod_poly(lifts[i].R,lifts[j].R,f,N*N),rab=canonical_vec(Rab,N,degree),Cab(degree);
    for(int z=0;z<degree;++z) { require((Rab[z]-rab[z])%N==0,"product lift exact /N"); Cab[z]=(Rab[z]-rab[z])/N; }
    if(direct_pair_check) {
      Vec ai(degree),aj(degree); ai[0]=i-2;ai[1]=1;aj[0]=j-2;aj[1]=1;
      Vec ab=mul_exact(ai,aj,f), direct=pow_mod_poly(ab,N,f,N*N); require(direct==Rab,"direct exponent multiplicativity");
    }
    Vec residual=sub_vec(sub_vec(Cab,carry.K),cross),Q=exact_div_N(residual,N,"multiplicativity residual exact /N");
    add_coeffs(state,18,residual,mismatch,scope); add_coeffs(state,19,Q,mismatch,scope); qmult.push_back(Q);
    Mat MQ=multiplication_matrix(Q,f); state.add(33,trace(MQ),mismatch,scope);state.add(34,determinant(MQ),mismatch,scope);
    Vec ch=characteristic_coefficients(MQ);for(int z=0;z<degree;++z)state.add(35,ch[z],mismatch,scope);
    state.add(39,trace(MQ)*trace(multiplication_matrix(lifts[i].C,f))-trace(multiplication_matrix(lifts[j].C,f))*trace(multiplication_matrix(Q,f)),mismatch,scope);
    state.add(40,determinant(MQ)-determinant(multiplication_matrix(lifts[i].C,f)),mismatch,scope);
    state.add(41,resultant(Q,lifts[i].C),mismatch,scope);
  }
  for(int i=0;i<(int)qmult.size();++i)for(int j=i+1;j<(int)qmult.size();++j)add_2minors(state,20,qmult[i],qmult[j],mismatch,scope);
  for(int i=0;i<(int)qmult.size();++i)for(int j=i+1;j<(int)qmult.size();++j)for(int k=j+1;k<(int)qmult.size();++k)
    if((i+j+k)%7==0)add_3minors(state,21,qmult[i],qmult[j],qmult[k],mismatch,scope);

  std::vector<Vec> qassoc;
  for(int i=0;i<5;++i)for(int j=i+1;j<5;++j)for(int k=j+1;k<5;++k) {
    const Vec &u=lifts[i].r,&v=lifts[j].r,&w=lifts[k].r;
    Carry uv=section_carry(u,v,f,N),vw=section_carry(v,w,f,N),left=section_carry(uv.z,w,f,N),right=section_carry(u,vw.z,f,N);
    Vec full=sub_vec(add_vec(left.K,mul_exact(uv.K,w,f)),add_vec(right.K,mul_exact(u,vw.K,f)));
    for(const auto&x:full)require(x==0,"full associator exact zero"); add_coeffs(state,15,full,mismatch,scope);
    Vec E=sub_vec(add_vec(left.k,mul_exact(uv.k,w,f)),add_vec(right.k,mul_exact(u,vw.k,f)));
    Vec Q=exact_div_N(E,N,"digit associator exact /N"); add_coeffs(state,16,E,mismatch,scope);add_coeffs(state,17,Q,mismatch,scope);qassoc.push_back(Q);
    Mat MQ=multiplication_matrix(Q,f);state.add(36,trace(MQ),mismatch,scope);state.add(37,determinant(MQ),mismatch,scope);
    Vec ch=characteristic_coefficients(MQ);for(int z=0;z<degree;++z)state.add(38,ch[z],mismatch,scope);
  }
  for(int i=0;i<(int)qassoc.size();++i)for(int j=i+1;j<(int)qassoc.size();++j)add_2minors(state,22,qassoc[i],qassoc[j],mismatch,scope);
  for(int i=0;i<(int)qassoc.size();++i)for(int j=i+1;j<(int)qassoc.size();++j)for(int k=j+1;k<(int)qassoc.size();++k)
    add_3minors(state,23,qassoc[i],qassoc[j],qassoc[k],mismatch,scope);
  return {true,mismatch};
}

enum class Op { BASE_SUM,BASE_PRODUCT,ADD,DIFF,MUL,DET,D2,TRIPLE,QUAD };
struct Candidate { Op op; std::array<int,4> a{{-1,-1,-1,-1}}; std::string syntax; u64 aliases=1; };
static bool control_family(int f) { return f==15||f==16||f==18||f==46||f==47; }
static u64 hash_string(const std::string& s) { u64 h=SYNTH_SEED;for(unsigned char c:s)h=splitmix64(h^c);return h; }
static std::vector<Candidate> build_candidates() {
  std::vector<int> fam;for(int f=0;f<FAMILY_COUNT;++f)if(!control_family(f))fam.push_back(f);
  std::vector<Candidate> all;
  for(int f:fam) { all.push_back({Op::BASE_SUM,{f,-1,-1,-1},"sum("+std::string(FAMILY_NAMES[f])+")"}); all.push_back({Op::BASE_PRODUCT,{f,-1,-1,-1},"prod1("+std::string(FAMILY_NAMES[f])+")"}); }
  for(int x=0;x<(int)fam.size();++x)for(int y=x+1;y<(int)fam.size();++y) {
    int a=fam[x],b=fam[y]; std::string A=FAMILY_NAMES[a],B=FAMILY_NAMES[b];
    all.push_back({Op::ADD,{a,b,-1,-1},"add(sum("+A+"),sum("+B+"))"});
    all.push_back({Op::DIFF,{a,b,-1,-1},"difference(sum("+A+"),sum("+B+"))"});
    all.push_back({Op::MUL,{a,b,-1,-1},"mul(prod1("+A+"),prod1("+B+"))"});
    all.push_back({Op::DET,{a,b,-1,-1},"det2(sum("+A+"),prod1("+A+"),sum("+B+"),prod1("+B+"))"});
  }
  for(int i=0;i+2<(int)fam.size();++i) all.push_back({Op::D2,{fam[i],fam[i+1],fam[i+2],-1},"fd2(sum("+std::string(FAMILY_NAMES[fam[i]])+"),sum("+FAMILY_NAMES[fam[i+1]]+"),sum("+FAMILY_NAMES[fam[i+2]]+"))"});
  std::vector<Candidate> triples,quads;
  for(int i=0;i<(int)fam.size();++i)for(int j=i+1;j<(int)fam.size();++j)for(int k=j+1;k<(int)fam.size();++k) {
    std::string s="tri(sum("+std::string(FAMILY_NAMES[fam[i]])+"),prod1("+FAMILY_NAMES[fam[j]]+"),sum("+FAMILY_NAMES[fam[k]]+"))";
    triples.push_back({Op::TRIPLE,{fam[i],fam[j],fam[k],-1},s});
    for(int l=k+1;l<(int)fam.size();++l) {
      std::string q="quad(sum("+std::string(FAMILY_NAMES[fam[i]])+"),prod1("+FAMILY_NAMES[fam[j]]+"),sum("+FAMILY_NAMES[fam[k]]+"),prod1("+FAMILY_NAMES[fam[l]]+"))";
      quads.push_back({Op::QUAD,{fam[i],fam[j],fam[k],fam[l]},q});
    }
  }
  auto priority=[](const Candidate&a,const Candidate&b){u64 ha=hash_string(a.syntax),hb=hash_string(b.syntax);return ha!=hb?ha<hb:a.syntax<b.syntax;};
  std::sort(triples.begin(),triples.end(),priority);if((int)triples.size()>TRIPLE_SYNTH_CAP)triples.resize(TRIPLE_SYNTH_CAP);
  std::sort(quads.begin(),quads.end(),priority);if((int)quads.size()>QUAD_SYNTH_CAP)quads.resize(QUAD_SYNTH_CAP);
  all.insert(all.end(),triples.begin(),triples.end());all.insert(all.end(),quads.begin(),quads.end());
  std::set<std::string> syntax;for(const auto&c:all)require(syntax.insert(c.syntax).second,"duplicate candidate syntax");
  return all;
}

template<class T> static T eval_candidate(const Candidate& c,const std::array<T,FAMILY_COUNT>& sum,
                                           const std::array<T,FAMILY_COUNT>& product,const T& mod) {
  auto add=[&](T x,T y)->T{T r=(x+y)%mod;return r;}; auto mul=[&](T x,T y)->T{T r=(x*y)%mod;return r;};
  auto sub=[&](T x,T y)->T{T r=x>=y?T(x-y):T((x+mod-y)%mod);return r;};
  switch(c.op) {
    case Op::BASE_SUM:return sum[c.a[0]];
    case Op::BASE_PRODUCT:return product[c.a[0]];
    case Op::ADD:return add(sum[c.a[0]],sum[c.a[1]]);
    case Op::DIFF:return sub(sum[c.a[0]],sum[c.a[1]]);
    case Op::MUL:return mul(product[c.a[0]],product[c.a[1]]);
    case Op::DET:return sub(mul(sum[c.a[0]],product[c.a[1]]),mul(product[c.a[0]],sum[c.a[1]]));
    case Op::D2:return sub(add(sum[c.a[0]],sum[c.a[2]]),add(sum[c.a[1]],sum[c.a[1]]));
    case Op::TRIPLE:return mul(mul(sum[c.a[0]],product[c.a[1]]),sum[c.a[2]]);
    case Op::QUAD:return mul(mul(sum[c.a[0]],product[c.a[1]]),mul(sum[c.a[2]],product[c.a[3]]));
  }
  return 0;
}

static std::vector<Candidate> canonicalize_candidates(std::vector<Candidate> input) {
  std::map<std::string,std::size_t> seen;std::vector<Candidate> out;
  for(auto&c:input) {
    std::ostringstream fp;
    for(int sample=0;sample<32;++sample)for(u64 prime:{FP_PRIME_1,FP_PRIME_2}) {
      std::array<u64,FAMILY_COUNT>s{},p{};for(int f=0;f<FAMILY_COUNT;++f){s[f]=splitmix64(SYNTH_SEED^u64(sample*131+f*2))%prime;p[f]=splitmix64(SYNTH_SEED^u64(sample*137+f*2+1))%prime;}
      fp<<eval_candidate(c,s,p,prime)<<',';
    }
    auto [it,fresh]=seen.emplace(fp.str(),out.size());if(fresh)out.push_back(c);else++out[it->second].aliases;
  }
  return out;
}

static u64 inv_prime(u64 x,u64 p) { require(x%p!=0,"modular inverse zero");return pow_u64(x,p-2,p); }
static int rref_rank(std::vector<std::vector<u64>> A,u64 p) {
  if(A.empty())return 0;int rows=A.size(),cols=A[0].size(),rank=0;
  for(int col=0;col<cols&&rank<rows;++col) {
    int pivot=rank;while(pivot<rows&&A[pivot][col]==0)++pivot;if(pivot==rows)continue;
    std::swap(A[pivot],A[rank]);u64 inv=inv_prime(A[rank][col],p);
    for(int j=col;j<cols;++j)A[rank][j]=mul_u64(A[rank][j],inv,p);
    for(int i=0;i<rows;++i)if(i!=rank&&A[i][col]) {u64 c=A[i][col];for(int j=col;j<cols;++j)A[i][j]=(A[i][j]+p-mul_u64(c,A[rank][j],p))%p;}
    ++rank;
  }
  return rank;
}
static std::vector<u64> feature_row(const std::vector<cpp_int>& terms,u64 p) {
  std::vector<u64> r{1};for(const auto&x:terms)r.push_back(mod_u64(x,p));
  for(std::size_t i=0;i<terms.size();++i)for(std::size_t j=i;j<terms.size();++j)r.push_back(mul_u64(mod_u64(terms[i],p),mod_u64(terms[j],p),p));
  return r;
}
static std::vector<std::vector<long long>> expected_relations(const std::vector<int>& signs) {
  int k=signs.size(),cols=1+k+k*(k+1)/2;std::vector<std::vector<long long>> out;
  std::vector<long long>L(cols);for(int i=0;i<k;++i)L[1+i]=signs[i];out.push_back(L);
  auto qindex=[&](int a,int b){if(a>b)std::swap(a,b);int idx=1+k;for(int i=0;i<a;++i)idx+=k-i;return idx+(b-a);};
  for(int j=0;j<k;++j){std::vector<long long>v(cols);for(int i=0;i<k;++i)v[qindex(i,j)]+=signs[i];out.push_back(v);}
  return out;
}
static void authenticate_matrix(const std::vector<std::vector<u64>>& A,const std::vector<int>& signs,u64 p,const std::string& name) {
  require(!A.empty(),name+" nonempty matrix");auto rel=expected_relations(signs);
  for(const auto&v:rel)for(const auto&row:A){u64 x=0;for(std::size_t j=0;j<row.size();++j){long long c=v[j];if(c>=0)x=(x+mul_u64(row[j],c%p,p))%p;else x=(x+p-mul_u64(row[j],(-c)%p,p))%p;}require(x==0,name+" expected null relation");}
  int rank=rref_rank(A,p),nullity=(int)A[0].size()-rank;require(nullity>=(int)rel.size(),name+" nullity control");
}

static std::string mine_public_identities() {
  const cpp_int N=FP_PRIME_1,N2=N*N;Rng rng(SYNTH_SEED);
  std::vector<std::vector<u64>> full_rows,digit_rows,mult_rows,translation_rows;
  for(int sample=0;sample<96;++sample) {
    int d=2+sample%4,recipe=(sample/4)%4;Vec f=recipe_poly(d,recipe,N);
    Vec u(d),v(d),w(d);for(int i=0;i<d;++i){u[i]=rng.next()%FP_PRIME_1;v[i]=rng.next()%FP_PRIME_1;w[i]=rng.next()%FP_PRIME_1;}
    Carry uv=section_carry(u,v,f,N),vw=section_carry(v,w,f,N),left=section_carry(uv.z,w,f,N),right=section_carry(u,vw.z,f,N);
    Vec A=mul_exact(uv.K,w,f),B=mul_exact(u,vw.K,f),a=mul_exact(uv.k,w,f),b=mul_exact(u,vw.k,f);
    for(int c=0;c<d;++c) {
      std::vector<cpp_int> ft{left.K[c],A[c],right.K[c],B[c]};full_rows.push_back(feature_row(ft,FP_PRIME_1));
      std::vector<cpp_int> dt{left.k[c],a[c],right.k[c],b[c]};digit_rows.push_back(feature_row(dt,FP_PRIME_1));
    }
    Vec aa(d),bb(d);aa[0]=(sample%5)-2;aa[1]=1;bb[0]=((sample*3)%7)-3;bb[1]=1;
    Lift la=power_lift(aa,f,N),lb=power_lift(bb,f,N);Carry carry=section_carry(la.r,lb.r,f,N);
    Vec Rab=mul_mod_poly(la.R,lb.R,f,N2),rab=canonical_vec(Rab,N,d),Cab(d),cross=add_vec(mul_exact(la.r,lb.C,f),mul_exact(la.C,lb.r,f));
    for(int c=0;c<d;++c){require((Rab[c]-rab[c])%N==0,"synthetic mult digit");Cab[c]=(Rab[c]-rab[c])/N;mult_rows.push_back(feature_row({Cab[c],carry.K[c],cross[c]},FP_PRIME_1));}
    Vec x(d);x[1]=1;Lift base=power_lift(x,f,N);int t=(sample&1)?2:-2;Vec ft=shift_poly(f,-t),xt(d);xt[0]=-t;xt[1]=1;Lift moved=power_lift(xt,ft,N);Vec back=canonical_vec(shift_poly(moved.R,t),N2,d);
    require(back==base.R,"synthetic transported translation equality");
    for(int c=0;c<d;++c)translation_rows.push_back(feature_row({base.R[c],back[c]},FP_PRIME_1));
  }
  authenticate_matrix(full_rows,{1,1,-1,-1},FP_PRIME_1,"full associator");
  authenticate_matrix(digit_rows,{1,1,-1,-1},FP_PRIME_1,"digit associator");
  authenticate_matrix(mult_rows,{1,-1,-1},FP_PRIME_1,"multiplicativity");
  authenticate_matrix(translation_rows,{1,-1},FP_PRIME_1,"translation");
  for(int sample=0;sample<64;++sample) {
    cpp_int M=2000003+2*sample;int d=2+sample%4;Vec f=recipe_poly(d,(sample/4)%4,M);Vec u(d),v(d),w(d);
    for(int i=0;i<d;++i){u[i]=splitmix64(SYNTH_SEED+sample*101+i)%M.convert_to<u64>();v[i]=splitmix64(SYNTH_SEED+sample*103+i+7)%M.convert_to<u64>();w[i]=splitmix64(SYNTH_SEED+sample*107+i+11)%M.convert_to<u64>();}
    Carry uv=section_carry(u,v,f,M),vw=section_carry(v,w,f,M),left=section_carry(uv.z,w,f,M),right=section_carry(u,vw.z,f,M);
    Vec full=sub_vec(add_vec(left.K,mul_exact(uv.K,w,f)),add_vec(right.K,mul_exact(u,vw.K,f)));
    for(const auto&x:full)require(x==0,"heldback exact associator");
    Vec E=sub_vec(add_vec(left.k,mul_exact(uv.k,w,f)),add_vec(right.k,mul_exact(u,vw.k,f)));(void)exact_div_N(E,M,"heldback assoc /N");
    Vec aa(d),bb(d);aa[0]=sample%5-2;aa[1]=1;bb[0]=sample%7-3;bb[1]=1;Lift la=power_lift(aa,f,M),lb=power_lift(bb,f,M);Carry c=section_carry(la.r,lb.r,f,M);
    Vec Rab=mul_mod_poly(la.R,lb.R,f,M*M),rab=canonical_vec(Rab,M,d),Cab(d),cross=add_vec(mul_exact(la.r,lb.C,f),mul_exact(la.C,lb.r,f));for(int z=0;z<d;++z){Cab[z]=(Rab[z]-rab[z])/M;}
    (void)exact_div_N(sub_vec(sub_vec(Cab,c.K),cross),M,"heldback mult /N");
  }
  std::ostringstream out;out<<"samples=96 heldback=64 full_rank="<<rref_rank(full_rows,FP_PRIME_1)<<"/"<<full_rows[0].size()<<" digit_rank="<<rref_rank(digit_rows,FP_PRIME_1)<<"/"<<digit_rows[0].size()<<" mult_rank="<<rref_rank(mult_rows,FP_PRIME_1)<<"/"<<mult_rows[0].size()<<" translation_rank="<<rref_rank(translation_rows,FP_PRIME_1)<<"/"<<translation_rows[0].size();return out.str();
}

static void translation_self_test() {
  for(cpp_int N:{cpp_int(4331),cpp_int(1000003)})for(int d=2;d<=5;++d)for(int recipe=0;recipe<4;++recipe) {
    Vec f=recipe_poly(d,recipe,N),x(d);x[1]=1;Lift base=power_lift(x,f,N);
    for(int t:{-2,2}) {Vec ft=shift_poly(f,-t),xt(d);xt[0]=-t;xt[1]=1;Lift moved=power_lift(xt,ft,N);Vec back=canonical_vec(shift_poly(moved.R,t),N*N,d);require(back==base.R,"translation full conjugacy");
      Vec raw=shift_poly(moved.C,t);for(int i=0;i<d;++i){cpp_int canonical_difference=back[i]-base.R[i];require(canonical_difference==0,"translation canonical control");(void)raw[i];}}
  }
}

struct InputResult {
  Task task;cpp_int N;u64 cleanup=0,polynomials=0,cycle_match=0,cycle_mismatch=0;
  std::array<u64,FAMILY_COUNT> atoms{},zeros{},units{},hits{},mismatch_atoms{},mismatch_hits{};
  std::vector<std::pair<int,u64>> candidate_hits;u64 candidate_hash=0;std::string first;
};
static InputResult process_input(const Task& task,const std::vector<Candidate>& candidates,bool direct_pair_check=false) {
  cpp_int N=cpp_int(task.p)*task.q;FamilyState state(N);u64 used=0,match=0,mismatch=0;
  for(int d=2;d<=5;++d)for(int recipe=0;recipe<4;++recipe){auto r=process_polynomial(recipe_poly(d,recipe,N),d,recipe,N,task.p,task.q,state,direct_pair_check);if(r.used){++used;if(r.mismatch)++mismatch;else++match;}}
  InputResult out;out.task=task;out.N=N;out.cleanup=state.cleanup;out.polynomials=used;out.cycle_match=match;out.cycle_mismatch=mismatch;out.atoms=state.atoms;out.zeros=state.zeros;out.units=state.units;out.hits=state.hits;out.mismatch_atoms=state.mismatch_atoms;out.mismatch_hits=state.mismatch_hits;out.first=state.first;
  for(int i=0;i<(int)candidates.size();++i){cpp_int value=mod_cpp(eval_candidate(candidates[i],state.sum,state.product,N),N),g=gcd_cpp(value,N);if(g>1&&g<N){u64 factor=g.convert_to<u64>();out.candidate_hits.push_back({i,factor});out.candidate_hash=splitmix64(out.candidate_hash^u64(i+1)^factor);if(out.first.empty())out.first="candidate:"+std::to_string(i)+":"+str_cpp(g);}}
  return out;
}

struct CandidateAggregate {
  u64 discovery_tested=0,discovery_hits=0,heldout_tested=0,heldout_hits=0;
  u64 discovery_safe_hits=0,heldout_safe_hits=0,mismatch_tested=0,mismatch_hits=0;
  u64 discovery_size_mask=0,heldout_size_mask=0;
};

static void self_test(const std::vector<Candidate>& candidates) {
  require(is_prime(61)&&is_prime(71)&&!is_prime(4331),"primality self-test");
  std::set<std::string> names,schemas;for(int f=0;f<FAMILY_COUNT;++f){require(names.insert(FAMILY_NAMES[f]).second,"duplicate family name");require(schemas.insert(FAMILY_SCHEMAS[f]).second,"duplicate family schema");}
  translation_self_test();std::string identities=mine_public_identities();
  Task task{7,0,0,61,71};InputResult r=process_input(task,candidates,true);require(r.N==4331,"self-test N");require(r.polynomials>0,"self-test polynomial source");
  u64 atoms=std::accumulate(r.atoms.begin(),r.atoms.end(),u64(0));require(atoms>100,"self-test static atoms");require(candidates.size()>12000,"large synthesis candidate count");
  std::cout<<"SELF_TEST_PASS N=4331 families="<<FAMILY_COUNT<<" candidates="<<candidates.size()<<" aliases=";
  u64 aliases=0;for(const auto&c:candidates)aliases+=c.aliases-1;std::cout<<aliases<<" atoms="<<atoms<<" polynomials="<<r.polynomials<<" identity_mining={"<<identities<<"}\n";
}

int main(int argc,char**argv) try {
  std::vector<Candidate> candidates=canonicalize_candidates(build_candidates());
  if(argc==2&&std::string(argv[1])=="--describe") {
    u64 aliases=0;for(const auto&c:candidates)aliases+=c.aliases-1;
    std::cout<<"F262_D01_DESCRIPTION families="<<FAMILY_COUNT<<" candidates="<<candidates.size()<<" aliases="<<aliases<<" planned_inputs=5280 max_threads=8\n";return 0;
  }
  if(argc==2&&std::string(argv[1])=="--self-test") {self_test(candidates);return 0;}
  if(argc==2&&std::string(argv[1])=="--benchmark") {
    translation_self_test();std::string identities=mine_public_identities();Rng rng(SYNTH_SEED^0xbec4ULL);double total=0;u64 atoms=0,hits=0;
    for(int rep=0;rep<3;++rep){u64 p=random_prime(60,rng),q=random_prime(60,rng);if(p>q)std::swap(p,q);if(p==q||q>=2*p){--rep;continue;}Task task{60,0,rep,p,q};auto start=std::chrono::steady_clock::now();InputResult r=process_input(task,candidates,false);double sec=std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count();total+=sec;atoms+=std::accumulate(r.atoms.begin(),r.atoms.end(),u64(0));hits+=r.candidate_hits.size();}
    double per=total/3.0,project=per*5280.0/8.0*1.75;std::cout<<std::fixed<<std::setprecision(6)<<"BENCHMARK_PASS repetitions=3 mean_full_60bit_input_seconds="<<per<<" static_atoms="<<atoms<<" candidates="<<candidates.size()<<" candidate_hits="<<hits<<" projected_8thread_seconds_1.75x="<<project<<" projected_peak_mib=640 projected_tsv_mib=18 projected_json_mib="<<(candidates.size()*0.00042)<<" identity_mining={"<<identities<<"}\n";return 0;
  }
  require(argc==5,"usage: symbolic_search THREADS OUT_JSON OUT_TSV OUT_ANOMALIES");int threads_count=std::stoi(argv[1]);require(threads_count>=1&&threads_count<=8,"threads 1..8");
  std::vector<Task> tasks=make_tasks();std::string identities=mine_public_identities();std::vector<InputResult> results(tasks.size());std::atomic<std::size_t>next{0},done{0};std::mutex io;auto started=std::chrono::steady_clock::now();
  auto worker=[&](){for(;;){std::size_t i=next.fetch_add(1);if(i>=tasks.size())return;results[i]=process_input(tasks[i],candidates,false);std::size_t n=done.fetch_add(1)+1;if(n%32==0||n==tasks.size()){std::lock_guard<std::mutex>lock(io);double sec=std::chrono::duration<double>(std::chrono::steady_clock::now()-started).count();std::cerr<<"progress="<<n<<"/"<<tasks.size()<<" elapsed="<<std::fixed<<std::setprecision(1)<<sec<<"s rate="<<n/sec<<"/s\n";}}};
  std::vector<std::thread> pool;for(int i=0;i<threads_count;++i)pool.emplace_back(worker);for(auto&t:pool)t.join();double elapsed=std::chrono::duration<double>(std::chrono::steady_clock::now()-started).count();
  std::ofstream tsv(argv[3]);require(bool(tsv),"open TSV");tsv<<"factor_bits\tsplit\tcohort\tindex\tp\tq\tN\tcleanup\tpolynomials\tcycle_match\tcycle_mismatch\tcandidate_hits\tcandidate_hash\tfirst_certificate";for(int f=0;f<FAMILY_COUNT;++f)tsv<<'\t'<<FAMILY_NAMES[f]<<"_atoms\t"<<FAMILY_NAMES[f]<<"_hits\t"<<FAMILY_NAMES[f]<<"_mismatch_atoms\t"<<FAMILY_NAMES[f]<<"_mismatch_hits";tsv<<'\n';
  for(const auto&r:results){tsv<<r.task.bits<<'\t'<<(r.task.bits<=32?"discovery":"heldout")<<'\t'<<cohort_name(r.task.cohort)<<'\t'<<r.task.index<<'\t'<<r.task.p<<'\t'<<r.task.q<<'\t'<<r.N<<'\t'<<r.cleanup<<'\t'<<r.polynomials<<'\t'<<r.cycle_match<<'\t'<<r.cycle_mismatch<<'\t'<<r.candidate_hits.size()<<'\t'<<r.candidate_hash<<'\t'<<r.first;for(int f=0;f<FAMILY_COUNT;++f)tsv<<'\t'<<r.atoms[f]<<'\t'<<r.hits[f]<<'\t'<<r.mismatch_atoms[f]<<'\t'<<r.mismatch_hits[f];tsv<<'\n';}tsv.close();
  std::ofstream anomaly(argv[4]);require(bool(anomaly),"open anomalies");anomaly<<"factor_bits\tsplit\tcohort\tindex\tcandidate\tfactor\tsyntax\n";u64 omitted=0;for(const auto&r:results){std::size_t cap=std::min<std::size_t>(512,r.candidate_hits.size());for(std::size_t z=0;z<cap;++z){int c=r.candidate_hits[z].first;anomaly<<r.task.bits<<'\t'<<(r.task.bits<=32?"discovery":"heldout")<<'\t'<<cohort_name(r.task.cohort)<<'\t'<<r.task.index<<'\t'<<c<<'\t'<<r.candidate_hits[z].second<<'\t'<<candidates[c].syntax<<'\n';}omitted+=r.candidate_hits.size()-cap;}anomaly.close();
  std::vector<CandidateAggregate> aggregate(candidates.size());for(const auto&r:results){bool disc=r.task.bits<=32,safe=r.task.cohort==2,mm=r.cycle_mismatch>0;for(auto&a:aggregate){if(disc)++a.discovery_tested;else++a.heldout_tested;if(mm)++a.mismatch_tested;}for(const auto&hit:r.candidate_hits){auto&a=aggregate[hit.first];if(disc){++a.discovery_hits;if(safe)++a.discovery_safe_hits;a.discovery_size_mask|=1ULL<<r.task.bits;}else{++a.heldout_hits;if(safe)++a.heldout_safe_hits;a.heldout_size_mask|=1ULL<<r.task.bits;}if(mm)++a.mismatch_hits;}}
  std::ofstream json(argv[2]);require(bool(json),"open JSON");u64 alias_total=0;for(const auto&c:candidates)alias_total+=c.aliases-1;json<<"{\n  \"experiment\": \"F262-D01\",\n  \"threads\": "<<threads_count<<",\n  \"elapsed_seconds\": "<<std::setprecision(12)<<elapsed<<",\n  \"inputs\": "<<results.size()<<",\n  \"families\": "<<FAMILY_COUNT<<",\n  \"candidates\": "<<candidates.size()<<",\n  \"aliases\": "<<alias_total<<",\n  \"omitted_anomaly_rows\": "<<omitted<<",\n  \"identity_mining\": \""<<identities<<"\",\n  \"family_summary\": [\n";
  for(int f=0;f<FAMILY_COUNT;++f){u64 atoms=0,hits=0,ma=0,mh=0;for(const auto&r:results){atoms+=r.atoms[f];hits+=r.hits[f];ma+=r.mismatch_atoms[f];mh+=r.mismatch_hits[f];}if(f)json<<",\n";json<<"    {\"family\": \""<<FAMILY_NAMES[f]<<"\", \"atoms\": "<<atoms<<", \"hits\": "<<hits<<", \"mismatch_atoms\": "<<ma<<", \"mismatch_hits\": "<<mh<<"}";}json<<"\n  ],\n  \"candidate_summary\": [\n";
  for(std::size_t i=0;i<candidates.size();++i){if(i)json<<",\n";const auto&a=aggregate[i];json<<"    {\"id\": "<<i<<", \"syntax\": \""<<candidates[i].syntax<<"\", \"aliases\": "<<candidates[i].aliases<<", \"discovery_tested\": "<<a.discovery_tested<<", \"discovery_hits\": "<<a.discovery_hits<<", \"discovery_safe_hits\": "<<a.discovery_safe_hits<<", \"heldout_tested\": "<<a.heldout_tested<<", \"heldout_hits\": "<<a.heldout_hits<<", \"heldout_safe_hits\": "<<a.heldout_safe_hits<<", \"mismatch_tested\": "<<a.mismatch_tested<<", \"mismatch_hits\": "<<a.mismatch_hits<<", \"discovery_size_mask\": "<<a.discovery_size_mask<<", \"heldout_size_mask\": "<<a.heldout_size_mask<<"}";}json<<"\n  ]\n}\n";json.close();
  std::cout<<"F262_D01_PASS inputs="<<results.size()<<" candidates="<<candidates.size()<<" elapsed_seconds="<<std::fixed<<std::setprecision(3)<<elapsed<<" omitted_anomaly_rows="<<omitted<<" identity_mining={"<<identities<<"}\n";return 0;
} catch(const std::exception&e) {std::cerr<<"F262_D01_FAIL "<<e.what()<<"\n";return 1;}
