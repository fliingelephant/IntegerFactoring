#include <algorithm>
#include <array>
#include <atomic>
#include <cstdint>
#include <cstring>
#include <exception>
#include <fstream>
#include <filesystem>
#include <iomanip>
#include <iostream>
#include <limits>
#include <map>
#include <mutex>
#include <set>
#include <sstream>
#include <stdexcept>
#include <string>
#include <thread>
#include <tuple>
#include <utility>
#include <vector>

#include <boost/multiprecision/cpp_int.hpp>

using boost::multiprecision::cpp_int;
using u64 = std::uint64_t;

namespace {

constexpr int kFamilyCount = 12;
constexpr int kOriginalRows = 284;
constexpr int kCaseCount = 188;
constexpr int kCleanCases = 125;
constexpr int kMaxRows = 284;
constexpr int kMaxBlocks = 65536;
constexpr u64 kMaxSteps = 1000000;
constexpr int kMaxCaseRelations = 50000;
constexpr int kMaxGlobalRelations = 1000000;
constexpr int kMaxTotalRowBits = 100000;
constexpr u64 kMaxRelationPayload = 100663296ULL;
constexpr u64 kMaxOutputBytes = 201326592ULL;
constexpr u64 kMaxOutputLineBytes = 1048576ULL;
constexpr const char* kEvidenceSha =
    "a0ef66750b51aa311be854c207331f018d4a420c04c7bb749206cf8781dc67dc";
constexpr const char* kBanksSha =
    "c908bfd6c30f73864dc1f2b83ace770b3d117f72d98e2e086c4f4f51064b2ef6";
constexpr const char* kCorpusSha =
    "8b6f8dbe4eae9aa10c042928fc19fbe20a0015487340e7478135ce6f37b5adb5";

[[noreturn]] void fail(const std::string& text) { throw std::runtime_error(text); }
void require(bool condition, const std::string& text) { if (!condition) fail(text); }

class Sha256 {
 public:
  Sha256() : state_{0x6a09e667U,0xbb67ae85U,0x3c6ef372U,0xa54ff53aU,
                    0x510e527fU,0x9b05688cU,0x1f83d9abU,0x5be0cd19U} {}
  void update(const unsigned char* data, std::size_t length) {
    total_ += length;
    while (length) {
      std::size_t take=std::min<std::size_t>(length,64-used_);
      std::memcpy(block_.data()+used_,data,take);
      used_+=take; data+=take; length-=take;
      if (used_==64) { compress(block_.data()); used_=0; }
    }
  }
  void update(const std::string& text) {
    update(reinterpret_cast<const unsigned char*>(text.data()),text.size());
  }
  std::string final_hex() {
    u64 bits=total_*8; block_[used_++]=0x80;
    if (used_>56) { while (used_<64) block_[used_++]=0; compress(block_.data()); used_=0; }
    while (used_<56) block_[used_++]=0;
    for (int i=7;i>=0;--i) block_[used_++]=static_cast<unsigned char>(bits>>(8*i));
    compress(block_.data());
    std::ostringstream out; out<<std::hex<<std::setfill('0');
    for (auto word:state_) out<<std::setw(8)<<word;
    return out.str();
  }
 private:
  std::array<std::uint32_t,8> state_{};
  std::array<unsigned char,64> block_{};
  std::size_t used_=0; u64 total_=0;
  static std::uint32_t rotr(std::uint32_t x,int n) { return (x>>n)|(x<<(32-n)); }
  void compress(const unsigned char* bytes) {
    static constexpr std::uint32_t c[64]={
      0x428a2f98U,0x71374491U,0xb5c0fbcfU,0xe9b5dba5U,0x3956c25bU,0x59f111f1U,0x923f82a4U,0xab1c5ed5U,
      0xd807aa98U,0x12835b01U,0x243185beU,0x550c7dc3U,0x72be5d74U,0x80deb1feU,0x9bdc06a7U,0xc19bf174U,
      0xe49b69c1U,0xefbe4786U,0x0fc19dc6U,0x240ca1ccU,0x2de92c6fU,0x4a7484aaU,0x5cb0a9dcU,0x76f988daU,
      0x983e5152U,0xa831c66dU,0xb00327c8U,0xbf597fc7U,0xc6e00bf3U,0xd5a79147U,0x06ca6351U,0x14292967U,
      0x27b70a85U,0x2e1b2138U,0x4d2c6dfcU,0x53380d13U,0x650a7354U,0x766a0abbU,0x81c2c92eU,0x92722c85U,
      0xa2bfe8a1U,0xa81a664bU,0xc24b8b70U,0xc76c51a3U,0xd192e819U,0xd6990624U,0xf40e3585U,0x106aa070U,
      0x19a4c116U,0x1e376c08U,0x2748774cU,0x34b0bcb5U,0x391c0cb3U,0x4ed8aa4aU,0x5b9cca4fU,0x682e6ff3U,
      0x748f82eeU,0x78a5636fU,0x84c87814U,0x8cc70208U,0x90befffaU,0xa4506cebU,0xbef9a3f7U,0xc67178f2U};
    std::uint32_t w[64];
    for (int i=0;i<16;++i) w[i]=(std::uint32_t(bytes[4*i])<<24)|(std::uint32_t(bytes[4*i+1])<<16)|
                                    (std::uint32_t(bytes[4*i+2])<<8)|bytes[4*i+3];
    for (int i=16;i<64;++i) {
      auto s0=rotr(w[i-15],7)^rotr(w[i-15],18)^(w[i-15]>>3);
      auto s1=rotr(w[i-2],17)^rotr(w[i-2],19)^(w[i-2]>>10);
      w[i]=w[i-16]+s0+w[i-7]+s1;
    }
    auto a=state_[0],b=state_[1],d0=state_[2],d=state_[3];
    auto e=state_[4],f=state_[5],g=state_[6],h=state_[7];
    for (int i=0;i<64;++i) {
      auto s1=rotr(e,6)^rotr(e,11)^rotr(e,25),ch=(e&f)^((~e)&g);
      auto t1=h+s1+ch+c[i]+w[i];
      auto s0=rotr(a,2)^rotr(a,13)^rotr(a,22),maj=(a&b)^(a&d0)^(b&d0),t2=s0+maj;
      h=g;g=f;f=e;e=d+t1;d=d0;d0=b;b=a;a=t1+t2;
    }
    state_[0]+=a;state_[1]+=b;state_[2]+=d0;state_[3]+=d;
    state_[4]+=e;state_[5]+=f;state_[6]+=g;state_[7]+=h;
  }
};

std::string read_file(const std::string& path) {
  std::ifstream in(path,std::ios::binary); require(bool(in),"open input: "+path);
  std::ostringstream out; out<<in.rdbuf(); require(in.good()||in.eof(),"read input: "+path);
  return out.str();
}
std::string sha256(const std::string& bytes) { Sha256 h; h.update(bytes); return h.final_hex(); }
cpp_int absz(cpp_int x) { return x<0?-x:x; }
cpp_int modz(cpp_int x,const cpp_int& n) { x%=n; if (x<0) x+=n; return x; }
cpp_int gcdz(cpp_int a,cpp_int b) { a=absz(a);b=absz(b);while(b!=0){cpp_int r=a%b;a=b;b=r;}return a; }
cpp_int invmod(cpp_int a,const cpp_int& n) {
  a=modz(a,n); cpp_int oldr=a,r=n,olds=1,s=0;
  while(r!=0){cpp_int q=oldr/r,nr=oldr-q*r,ns=olds-q*s;oldr=r;r=nr;olds=s;s=ns;}
  require(oldr==1,"inverse of nonunit"); return modz(olds,n);
}
int bitlen(const cpp_int& x) { return x==0?0:boost::multiprecision::msb(absz(x))+1; }
cpp_int pow_small(cpp_int base,std::uint32_t exponent) {
  cpp_int out=1; while(exponent){if(exponent&1U)out*=base;base*=base;exponent>>=1U;} return out;
}
cpp_int powmod(cpp_int base,cpp_int exponent,const cpp_int& modulus) {
  base=modz(base,modulus);cpp_int out=1%modulus;
  while(exponent>0){if((exponent&1)!=0)out=modz(out*base,modulus);base=modz(base*base,modulus);exponent>>=1;}return out;
}
bool squarez(const cpp_int& value,cpp_int* root=nullptr) {
  if(value<0)return false;if(value==0){if(root)*root=0;return true;}
  cpp_int x=cpp_int(1)<<((bitlen(value)+1)/2);
  for(;;){cpp_int y=(x+value/x)>>1;if(y>=x)break;x=y;}
  while((x+1)*(x+1)<=value)++x;while(x*x>value)--x;
  if(x*x!=value)return false;if(root)*root=x;return true;
}
cpp_int parse_positive(const std::string& text) {
  require(!text.empty()&&text.find_first_not_of("0123456789")==std::string::npos,"integer syntax");
  cpp_int x(text);require(x>0,"positive integer");return x;
}
std::vector<std::string> split_tab(const std::string& line) {
  std::istringstream in(line);std::vector<std::string> out;std::string x;
  while(std::getline(in,x,'\t'))out.push_back(x);return out;
}
std::string join(const std::vector<std::string>& values,const char* separator) {
  std::ostringstream out;for(std::size_t i=0;i<values.size();++i){if(i)out<<separator;out<<values[i];}return out.str();
}

using Bits=std::vector<u64>;
bool bit_get(const Bits& b,int i){return (b[i>>6]>>(i&63))&1ULL;}
void bit_flip(Bits& b,int i){b[i>>6]^=1ULL<<(i&63);}
void bit_xor(Bits& a,const Bits& b){require(a.size()==b.size(),"bit width");for(std::size_t i=0;i<a.size();++i)a[i]^=b[i];}
bool bit_zero(const Bits& b){for(u64 w:b)if(w)return false;return true;}
int bit_weight(const Bits& b){int n=0;for(u64 w:b)n+=__builtin_popcountll(w);return n;}
int first_bit(const Bits& b,int columns){for(int i=0;i<columns;++i)if(bit_get(b,i))return i;return -1;}

struct BitBasis {
  int columns;std::vector<Bits> pivot;
  explicit BitBasis(int n):columns(n),pivot(n){}
  Bits reduce(Bits x) const {for(int i=0;i<columns;++i)if(bit_get(x,i)&&!pivot[i].empty())bit_xor(x,pivot[i]);return x;}
  bool insert(Bits x){x=reduce(std::move(x));int p=first_bit(x,columns);if(p<0)return false;pivot[p]=std::move(x);return true;}
  int dimension()const{int n=0;for(const auto& x:pivot)n+=!x.empty();return n;}
};

struct Case { std::string shape;int factor_bits=0,index=0,cell_index=0;cpp_int N;bool clean=true; };
struct Provenance {
  int original=-1,family=-1,row=-1,exponent_tag=-1,group=-1,role=-1,orbit_i=-1,orbit_j=-1;
  cpp_int root,base,exponent,low,high;std::string syntax;
};
struct Row { int retained_id=-1;cpp_int value,root;std::vector<Provenance> provenance; };
struct Block { cpp_int value;std::vector<std::uint32_t> exponents; };
struct Decoder { std::vector<Block> blocks;std::vector<Bits> equations,kernel;u64 steps=0;int rank=0; };

struct GlobalBudget {
  explicit GlobalBudget(u64 limit):output_limit(limit) {
    require(limit>0&&limit<=kMaxOutputBytes,"output budget");
  }
  void reserve_output(u64 bytes) {
    std::lock_guard<std::mutex> lock(mutex);
    require(!cancelled.load(),"GLOBAL_BUDGET_CANCELLED");
    if(bytes>output_limit-output_bytes){cancelled.store(true);fail("OUTPUT_BYTES_CAP");}
    output_bytes+=bytes;
  }
  void reserve_relation(u64 bytes) {
    std::lock_guard<std::mutex> lock(mutex);
    require(!cancelled.load(),"GLOBAL_BUDGET_CANCELLED");
    if(relation_count>=kMaxGlobalRelations){cancelled.store(true);fail("GLOBAL_RELATION_CAP");}
    if(bytes>kMaxRelationPayload-relation_payload){cancelled.store(true);fail("RELATION_PAYLOAD_CAP");}
    if(bytes>output_limit-output_bytes){cancelled.store(true);fail("OUTPUT_BYTES_CAP");}
    ++relation_count;relation_payload+=bytes;output_bytes+=bytes;
  }
  void cancel() { std::lock_guard<std::mutex> lock(mutex);cancelled.store(true); }
  void require_active() { require(!cancelled.load(),"GLOBAL_BUDGET_CANCELLED"); }
  u64 reserved_output() {
    std::lock_guard<std::mutex> lock(mutex);return output_bytes;
  }
  int reserved_relations() {
    std::lock_guard<std::mutex> lock(mutex);return relation_count;
  }
  u64 reserved_relation_payload() {
    std::lock_guard<std::mutex> lock(mutex);return relation_payload;
  }
 private:
  std::mutex mutex;
  std::atomic<bool> cancelled{false};
  int relation_count=0;
  u64 relation_payload=0,output_bytes=0,output_limit=0;
};

std::vector<Case> parse_corpus(const std::string& bytes) {
  require(sha256(bytes)==kCorpusSha,"corpus SHA-256");std::istringstream in(bytes);std::string line;
  require(std::getline(in,line)&&line=="version\tsplit\tshape\tfactor_bits\tindex\tN","corpus header");
  std::vector<Case> out;std::set<std::tuple<std::string,int,int>> seen;
  while(std::getline(in,line)){if(line.empty())continue;auto f=split_tab(line);
    require(f.size()==6&&f[0]=="F268-D04"&&f[1]=="discovery","corpus record");
    Case c{f[2],std::stoi(f[3]),static_cast<int>(out.size()),std::stoi(f[4]),parse_positive(f[5]),true};
    require(seen.insert({c.shape,c.factor_bits,c.cell_index}).second,"duplicate corpus case");out.push_back(std::move(c));
  }
  require(out.size()==kCaseCount,"corpus case count");return out;
}

using CaseKey=std::tuple<std::string,int,int>;
std::map<CaseKey,std::array<bool,kFamilyCount>> parse_banks(const std::string& bytes,const std::vector<Case>& cases) {
  require(sha256(bytes)==kBanksSha,"banks SHA-256");std::istringstream in(bytes);std::string line;
  require(std::getline(in,line),"banks header");auto h=split_tab(line);std::map<std::string,int> col;
  for(int i=0;i<static_cast<int>(h.size());++i)col[h[i]]=i;
  for(const char* name:{"version","split","shape","factor_bits","case_index","N","family","eligible","resource_reject","rows","rank","kernel_dim","earlier_factor"})
    require(col.count(name),std::string("banks field ")+name);
  std::map<CaseKey,std::array<bool,kFamilyCount>> labels;std::map<CaseKey,std::array<bool,kFamilyCount>> observed;
  for(const auto& c:cases){labels[{c.shape,c.factor_bits,c.index}]={};observed[{c.shape,c.factor_bits,c.index}]={};}
  int rows=0;
  while(std::getline(in,line)){if(line.empty())continue;auto f=split_tab(line);require(f.size()==h.size(),"banks width");
    require(f[col["version"]]=="F268-D04"&&f[col["split"]]=="discovery","banks identity");
    CaseKey key{f[col["shape"]],std::stoi(f[col["factor_bits"]]),std::stoi(f[col["case_index"]])};
    require(labels.count(key),"banks unknown case");int family=std::stoi(f[col["family"]]);require(family>=0&&family<kFamilyCount,"banks family");
    int case_index=std::stoi(f[col["case_index"]]);require(case_index>=0&&case_index<static_cast<int>(cases.size()),"banks case index");
    require(cases[case_index].shape==f[col["shape"]]&&cases[case_index].factor_bits==std::stoi(f[col["factor_bits"]])&&
            cases[case_index].N==parse_positive(f[col["N"]]),"banks corpus join");
    require(!observed[key][family],"duplicate bank");observed[key][family]=true;
    require(f[col["eligible"]]=="1"&&f[col["resource_reject"]]=="0","bank eligibility");
    int expected=family==10?20:24;require(std::stoi(f[col["rows"]])==expected,"bank row count");
    require(std::stoi(f[col["rank"]])==expected&&std::stoi(f[col["kernel_dim"]])==0,"bank full-rank baseline");
    require(f[col["earlier_factor"]]=="0"||f[col["earlier_factor"]]=="1","earlier-factor label");
    labels[key][family]=f[col["earlier_factor"]]=="1";++rows;
  }
  require(rows==kCaseCount*kFamilyCount,"bank count");
  for(const auto& [key,flags]:observed)for(bool flag:flags)require(flag,"missing bank");return labels;
}

using OriginalBanks=std::map<CaseKey,std::array<std::vector<Row>,kFamilyCount>>;
OriginalBanks parse_evidence(const std::string& bytes,const std::vector<Case>& cases) {
  require(sha256(bytes)==kEvidenceSha,"evidence SHA-256");std::istringstream in(bytes);std::string line;
  require(std::getline(in,line)&&line=="record\tsplit\tshape\tfactor_bits\tcase_index\tfamily\tobject\tvalue1\tvalue2\tvalue3\tvalue4\tvalue5\tvalue6\tmeta1\tmeta2\tmeta3\tsparse\tsyntax_or_templates\tclass","evidence header");
  OriginalBanks banks;for(const auto& c:cases)banks[{c.shape,c.factor_bits,c.index}]={};
  while(std::getline(in,line)){if(line.empty())continue;auto f=split_tab(line);require(f.size()==19,"evidence width");if(f[0]!="ROW")continue;
    require(f[1]=="discovery","evidence split");CaseKey key{f[2],std::stoi(f[3]),std::stoi(f[4])};require(banks.count(key),"evidence case");
    int family=std::stoi(f[5]),object=std::stoi(f[6]);require(family>=0&&family<kFamilyCount,"evidence family");
    auto& rows=banks[key][family];require(object==static_cast<int>(rows.size()),"evidence row order");
    Row row;row.value=parse_positive(f[7]);row.root=parse_positive(f[8]);
    Provenance p; p.family=family;p.row=object;p.base=parse_positive(f[9]);p.exponent=parse_positive(f[10]);
    p.low=parse_positive(f[11]);p.high=cpp_int(f[12]);require(p.high>=0,"negative high digit");p.exponent_tag=std::stoi(f[13]);
    p.group=std::stoi(f[14]);p.role=std::stoi(f[15]);std::size_t comma=f[16].find(',');require(comma!=std::string::npos,"orbit syntax");
    p.orbit_i=std::stoi(f[16].substr(0,comma));p.orbit_j=std::stoi(f[16].substr(comma+1));p.syntax=f[17];p.root=row.root;
    require(f[18]=="-","row class");row.provenance.push_back(std::move(p));rows.push_back(std::move(row));
  }
  for(const auto& c:cases){const auto& family_rows=banks.at({c.shape,c.factor_bits,c.index});int total=0;
    for(int family=0;family<kFamilyCount;++family){int expected=family==10?20:24;require(static_cast<int>(family_rows[family].size())==expected,"evidence family rows");
      for(const auto& row:family_rows[family]){const auto& p=row.provenance[0];require(row.value<c.N*c.N,"canonical row range");
        require(powmod(p.base,p.exponent,c.N*c.N)==row.value,"row exact power");require(modz(row.value,c.N)==p.low&&(row.value-p.low)/c.N==p.high,"row digits");
        require(modz(row.root*row.root,c.N)==p.low,"row supplied root");}total+=expected;}
    require(total==kOriginalRows,"case row count");}
  return banks;
}

Decoder decode_rows(const std::vector<Row>& rows,u64* case_steps=nullptr) {
  require(static_cast<int>(rows.size())<=kMaxRows,"row cap");int bits=0;for(const auto& row:rows)bits+=bitlen(row.value);require(bits<=kMaxTotalRowBits,"TOTAL_ROW_BITS_CAP");
  Decoder d;int count=rows.size();for(int i=0;i<count;++i)if(rows[i].value!=1){Block b{rows[i].value,std::vector<std::uint32_t>(count)};b.exponents[i]=1;d.blocks.push_back(std::move(b));}
  bool changed=true;while(changed){changed=false;
    for(std::size_t i=0;i<d.blocks.size()&&!changed;++i)for(std::size_t j=i+1;j<d.blocks.size();++j){cpp_int g=gcdz(d.blocks[i].value,d.blocks[j].value);if(g==1)continue;
      Block left=d.blocks[i],right=d.blocks[j];cpp_int lc=left.value/g,rc=right.value/g;std::vector<std::uint32_t> shared(count);
      for(int k=0;k<count;++k){u64 sum=u64(left.exponents[k])+right.exponents[k];require(sum<=std::numeric_limits<std::uint32_t>::max(),"block exponent overflow");shared[k]=sum;}
      d.blocks.erase(d.blocks.begin()+j);d.blocks.erase(d.blocks.begin()+i);
      if(lc>1)d.blocks.push_back({lc,std::move(left.exponents)});if(rc>1)d.blocks.push_back({rc,std::move(right.exponents)});d.blocks.push_back({g,std::move(shared)});
      ++d.steps;
      if(case_steps){++*case_steps;require(*case_steps<=kMaxSteps,"CASE_GCD_FREE_STEPS_CAP");}
      else require(d.steps<=kMaxSteps,"GCD_FREE_STEPS_CAP");
      require(static_cast<int>(d.blocks.size())<=kMaxBlocks,"BLOCK_CAP");changed=true;break;}}
  }
  std::sort(d.blocks.begin(),d.blocks.end(),[](const Block&a,const Block&b){return a.value<b.value;});
  for(std::size_t i=0;i<d.blocks.size();++i)for(std::size_t j=i+1;j<d.blocks.size();++j)require(gcdz(d.blocks[i].value,d.blocks[j].value)==1,"non-coprime blocks");
  for(int column=0;column<count;++column){cpp_int product=1;for(const auto& b:d.blocks)if(b.exponents[column])product*=pow_small(b.value,b.exponents[column]);require(product==rows[column].value,"row reconstruction");}
  int words=(count+63)/64;for(const auto& b:d.blocks){if(squarez(b.value))continue;Bits eq(words);for(int i=0;i<count;++i)if(b.exponents[i]&1U)bit_flip(eq,i);if(!bit_zero(eq))d.equations.push_back(std::move(eq));}
  std::vector<int> pivots;for(int column=0;column<count;++column){int selected=-1;for(int r=d.rank;r<static_cast<int>(d.equations.size());++r)if(bit_get(d.equations[r],column)){selected=r;break;}if(selected<0)continue;
    std::swap(d.equations[d.rank],d.equations[selected]);for(int r=0;r<static_cast<int>(d.equations.size());++r)if(r!=d.rank&&bit_get(d.equations[r],column))bit_xor(d.equations[r],d.equations[d.rank]);pivots.push_back(column);++d.rank;}
  std::vector<char> pivot(count);for(int p:pivots)pivot[p]=1;for(int free=0;free<count;++free)if(!pivot[free]){Bits v(words);bit_flip(v,free);for(int r=0;r<d.rank;++r)if(bit_get(d.equations[r],free))bit_flip(v,pivots[r]);d.kernel.push_back(std::move(v));}
  for(const auto& v:d.kernel)for(const auto& eq:d.equations){unsigned parity=0;for(int w=0;w<words;++w)parity^=__builtin_parityll(v[w]&eq[w]);require(parity==0,"kernel verification");}
  require(d.rank+static_cast<int>(d.kernel.size())==count,"rank-nullity");return d;
}

int matrix_rank(std::vector<Bits> equations,int columns) {
  int rank=0;for(int c=0;c<columns;++c){int selected=-1;for(int r=rank;r<static_cast<int>(equations.size());++r)if(bit_get(equations[r],c)){selected=r;break;}if(selected<0)continue;
    std::swap(equations[rank],equations[selected]);for(int r=0;r<static_cast<int>(equations.size());++r)if(r!=rank&&bit_get(equations[r],c))bit_xor(equations[r],equations[rank]);++rank;}return rank;
}

bool is_kernel_vector(const Bits& vector,const Decoder& decoder) {
  for(const auto& equation:decoder.equations){unsigned parity=0;
    for(std::size_t word=0;word<vector.size();++word)parity^=__builtin_parityll(vector[word]&equation[word]);
    if(parity)return false;
  }
  return true;
}

bool same_square_class(const cpp_int& a,const cpp_int& b,cpp_int* root=nullptr) {
  cpp_int g=gcdz(a,b),s,t;if(!squarez(a/g,&s)||!squarez(b/g,&t))return false;cpp_int r=g*s*t;require(r*r==a*b,"pair root");if(root)*root=r;return true;
}

std::string provenance_text(const Provenance& p) {
  std::ostringstream out;
  out<<p.original<<':'<<p.family<<':'<<p.row<<':'<<p.root<<':'<<p.base<<':'
     <<p.exponent<<':'<<p.low<<':'<<p.high<<':'<<p.exponent_tag<<':'<<p.group
     <<':'<<p.role<<':'<<p.orbit_i<<','<<p.orbit_j<<':'<<p.syntax;
  return out.str();
}

std::string row_provenance(const Row& row) {
  std::vector<std::string> out;
  for(const auto& p:row.provenance)out.push_back(provenance_text(p));
  return join(out,";");
}

struct RelationRecord {
  int case_index=-1,sequence=-1;
  std::string kind,support,family_class,provenance,root_class;
  std::string serialized;
  cpp_int exact_root,supplied_root,normalized,gcd_minus,gcd_plus;
  Bits bits;
};

struct PeelRecord { int round=-1,row=-1;std::vector<int> blocks;std::string provenance; };

struct CaseResult {
  int case_index=-1,cell_index=-1,factor_bits=0;
  std::string shape,cohort;
  cpp_int N;
  int original_rows=0,dedup_rows=0,peeled_rows=0,core_rows=0;
  int original_rank=0,original_nullity=0,dedup_rank=0,dedup_nullity=0;
  int core_rank=0,core_nullity=0,family_rank_sum=0,cross_gain=0;
  int separate_private=0,union_private=0,original_union_private=0;
  int private_loss=0,original_private_loss=0,peel_rounds=0;
  u64 refine_steps=0,core_refine_steps=0,singleton_tests=0,pair_tests=0;
  int duplicate_relations=0,singleton_relations=0,pair_relations=0,residual_relations=0;
  int useful_relations=0,pure_relations=0,cross_relations=0,pure_core_relations=0,cross_core_relations=0;
  std::array<int,kFamilyCount> family_ranks{};
  std::vector<Row> rows;
  std::vector<Block> blocks;
  std::vector<int> block_initial_degree,block_core_degree;
  std::vector<PeelRecord> peeling;
  std::vector<RelationRecord> relations;
};

std::string support_text(const std::vector<const Row*>& rows) {
  std::vector<std::string> ids;
  for(const Row* row:rows)ids.push_back(std::to_string(row->retained_id));
  return join(ids,",");
}

std::string relation_provenance(const std::vector<const Row*>& rows) {
  std::vector<std::string> out;
  for(const Row* row:rows)out.push_back(std::to_string(row->retained_id)+"{"+row_provenance(*row)+"}");
  return join(out,"|");
}

RelationRecord make_relation(int case_index,const std::string& kind,
                             const std::vector<const Row*>& rows,const cpp_int& N,
                             Bits bits={}) {
  require(!rows.empty(),"empty relation");cpp_int product=1,supplied=1;
  std::set<int> families;
  for(const Row* row:rows){product*=row->value;supplied=modz(supplied*row->root,N);
    for(const auto& p:row->provenance)families.insert(p.family);}
  cpp_int exact;require(squarez(product,&exact),"relation is not exact square");
  require(gcdz(supplied,N)==1,"relation supplied root nonunit");
  RelationRecord out;out.case_index=case_index;out.kind=kind;out.support=support_text(rows);
  out.family_class=families.size()==1?"PURE_FAMILY":"CROSS_FAMILY";
  out.provenance=relation_provenance(rows);out.exact_root=exact;out.supplied_root=supplied;
  out.normalized=modz(exact*invmod(supplied,N),N);out.gcd_minus=gcdz(exact-supplied,N);
  out.gcd_plus=gcdz(exact+supplied,N);out.bits=std::move(bits);
  cpp_int reduced=modz(exact,N);
  if(reduced==supplied)out.root_class="GLOBAL_PLUS";
  else if(reduced==modz(-supplied,N))out.root_class="GLOBAL_MINUS";
  else out.root_class="USEFUL";
  if(out.root_class=="USEFUL")
    require((out.gcd_minus>1&&out.gcd_minus<N)||(out.gcd_plus>1&&out.gcd_plus<N),"useful relation lacks factor");
  else require((out.gcd_minus==N&&out.gcd_plus==1)||(out.gcd_minus==1&&out.gcd_plus==N),"global relation gcd class");
  return out;
}

RelationRecord make_duplicate_relation(int case_index,const Row& retained,
                                       const Provenance& left,const Provenance& right,
                                       const cpp_int& N) {
  Row a=retained,b=retained;a.provenance={left};b.provenance={right};a.root=left.root;b.root=right;
  a.retained_id=retained.retained_id;b.retained_id=retained.retained_id;
  RelationRecord out=make_relation(case_index,"EXACT_DUPLICATE",{&a,&b},N);
  out.support=std::to_string(retained.retained_id)+"@"+std::to_string(left.original)+","+
              std::to_string(retained.retained_id)+"@"+std::to_string(right.original);
  return out;
}

void account_relation(CaseResult& result,RelationRecord relation,bool core_relation,
                      GlobalBudget& budget) {
  require(static_cast<int>(result.relations.size())<kMaxCaseRelations,"CASE_RELATION_CAP");
  relation.sequence=result.relations.size();
  std::ostringstream line;
  line<<result.case_index<<'\t'<<result.N<<'\t'<<result.cohort<<'\t'<<result.shape<<'\t'<<result.factor_bits<<'\t'<<relation.sequence<<'\t'
      <<relation.kind<<'\t'<<relation.support<<'\t'<<relation.family_class<<'\t'<<relation.provenance<<'\t'<<relation.exact_root<<'\t'
      <<relation.supplied_root<<'\t'<<relation.normalized<<'\t'<<relation.gcd_minus<<'\t'<<relation.gcd_plus<<'\t'<<relation.root_class<<'\n';
  relation.serialized=line.str();
  require(relation.serialized.size()<=kMaxOutputLineBytes,"RELATION_LINE_BYTES_CAP");
  budget.reserve_relation(relation.serialized.size());
  if(relation.kind=="EXACT_DUPLICATE")++result.duplicate_relations;
  else if(relation.kind=="SINGLETON")++result.singleton_relations;
  else if(relation.kind=="SUPPORT_TWO")++result.pair_relations;
  else if(relation.kind=="RESIDUAL")++result.residual_relations;
  else fail("unknown relation kind");
  result.useful_relations+=relation.root_class=="USEFUL";
  result.pure_relations+=relation.family_class=="PURE_FAMILY";
  result.cross_relations+=relation.family_class=="CROSS_FAMILY";
  result.pure_core_relations+=core_relation&&relation.family_class=="PURE_FAMILY";
  result.cross_core_relations+=core_relation&&relation.family_class=="CROSS_FAMILY";
  result.relations.push_back(std::move(relation));
}

CaseResult analyze_case(const Case& c,const std::array<std::vector<Row>,kFamilyCount>& family_rows,
                        GlobalBudget& budget) {
  CaseResult result;result.case_index=c.index;result.cell_index=c.cell_index;result.factor_bits=c.factor_bits;
  result.shape=c.shape;result.cohort=c.clean?"CLEAN":"CONTROL";result.N=c.N;result.original_rows=kOriginalRows;

  std::vector<Row> original;original.reserve(kOriginalRows);int original_id=0;
  for(int family=0;family<kFamilyCount;++family)for(const auto& input:family_rows[family]){
    Row row=input;row.provenance[0].original=original_id++;original.push_back(std::move(row));
  }
  require(original_id==kOriginalRows,"flattened row count");
  int original_bits=0;for(const auto& row:original)original_bits+=bitlen(row.value);
  require(original_bits<=kMaxTotalRowBits,"TOTAL_INPUT_ROW_BITS_CAP");

  std::map<cpp_int,int> retained;
  for(const auto& input:original){budget.require_active();auto [it,inserted]=retained.emplace(input.value,result.rows.size());
    if(inserted){Row row=input;row.retained_id=result.rows.size();result.rows.push_back(std::move(row));continue;}
    Row& row=result.rows[it->second];
    for(const auto& prior:row.provenance)
      account_relation(result,make_duplicate_relation(c.index,row,prior,input.provenance[0],c.N),false,budget);
    row.provenance.push_back(input.provenance[0]);
  }
  result.dedup_rows=result.rows.size();require(result.dedup_rows<=kOriginalRows,"dedup row count");

  u64 case_steps=0;
  {
    Decoder decoder=decode_rows(result.rows,&case_steps);result.refine_steps=decoder.steps;
    result.dedup_rank=decoder.rank;result.dedup_nullity=decoder.kernel.size();result.blocks=std::move(decoder.blocks);
  }
  int original_words=(kOriginalRows+63)/64;
  std::vector<Bits> original_equations;
  result.block_initial_degree.resize(result.blocks.size());result.block_core_degree.resize(result.blocks.size());
  std::vector<char> union_private(result.dedup_rows),separate_private(kOriginalRows);
  for(int block_id=0;block_id<static_cast<int>(result.blocks.size());++block_id){const auto& block=result.blocks[block_id];if(squarez(block.value))continue;
    Bits expanded(original_words);int union_degree=0;
    for(int row=0;row<result.dedup_rows;++row)if(block.exponents[row]&1U){++union_degree;for(const auto& p:result.rows[row].provenance)bit_flip(expanded,p.original);}
    result.block_initial_degree[block_id]=union_degree;if(!bit_zero(expanded))original_equations.push_back(std::move(expanded));
    if(union_degree==1)for(int row=0;row<result.dedup_rows;++row)if(block.exponents[row]&1U)union_private[row]=1;
    for(int family=0;family<kFamilyCount;++family){int one=-1,count=0;
      for(int row=0;row<result.dedup_rows;++row)if(block.exponents[row]&1U)for(const auto& p:result.rows[row].provenance)if(p.family==family){one=p.original;++count;}
      if(count==1)separate_private[one]=1;
    }
  }
  result.original_rank=matrix_rank(original_equations,kOriginalRows);result.original_nullity=kOriginalRows-result.original_rank;
  for(int family=0;family<kFamilyCount;++family){int columns=family==10?20:24,words=(columns+63)/64;std::vector<Bits> equations;
    for(const auto& block:result.blocks){if(squarez(block.value))continue;Bits eq(words);
      for(int row=0;row<result.dedup_rows;++row)if(block.exponents[row]&1U)for(const auto& p:result.rows[row].provenance)if(p.family==family)bit_flip(eq,p.row);
      if(!bit_zero(eq))equations.push_back(std::move(eq));}
    result.family_ranks[family]=matrix_rank(std::move(equations),columns);require(result.family_ranks[family]==columns,"family rank replay");result.family_rank_sum+=columns;
  }
  result.cross_gain=result.family_rank_sum-result.original_rank;
  require(result.cross_gain==result.original_nullity,"cross-gain identity");
  require(result.original_nullity==(kOriginalRows-result.dedup_rows)+result.dedup_nullity,"dedup nullity identity");
  for(char x:separate_private)result.separate_private+=x;require(result.separate_private==kOriginalRows,"separate private replay");
  for(int row=0;row<result.dedup_rows;++row)if(union_private[row]){++result.union_private;result.original_union_private+=result.rows[row].provenance.size();}
  result.private_loss=result.dedup_rows-result.union_private;result.original_private_loss=kOriginalRows-result.original_union_private;

  std::vector<char> active(result.dedup_rows,1);int round=0;
  for(;;){std::vector<std::vector<int>> witnesses(result.dedup_rows);
    for(int block_id=0;block_id<static_cast<int>(result.blocks.size());++block_id){const auto& block=result.blocks[block_id];if(squarez(block.value))continue;int only=-1,degree=0;
      for(int row=0;row<result.dedup_rows;++row)if(active[row]&&(block.exponents[row]&1U)){only=row;++degree;}
      if(degree==1)witnesses[only].push_back(block_id);
    }
    std::vector<int> marked;for(int row=0;row<result.dedup_rows;++row)if(active[row]&&!witnesses[row].empty())marked.push_back(row);
    if(marked.empty())break;++round;
    for(int row:marked){active[row]=0;result.peeling.push_back({round,row,witnesses[row],row_provenance(result.rows[row])});}
  }
  result.peel_rounds=round;result.peeled_rows=result.peeling.size();result.core_rows=result.dedup_rows-result.peeled_rows;
  for(int block_id=0;block_id<static_cast<int>(result.blocks.size());++block_id)if(!squarez(result.blocks[block_id].value))
    for(int row=0;row<result.dedup_rows;++row)if(active[row]&&(result.blocks[block_id].exponents[row]&1U))++result.block_core_degree[block_id];
  for(int degree:result.block_core_degree)require(degree!=1,"peeling fixed point");

  std::vector<Row> core;for(int row=0;row<result.dedup_rows;++row)if(active[row])core.push_back(result.rows[row]);
  Decoder core_decoder=decode_rows(core,&case_steps);result.core_refine_steps=core_decoder.steps;result.core_rank=core_decoder.rank;result.core_nullity=core_decoder.kernel.size();
  require(case_steps==result.refine_steps+result.core_refine_steps,"aggregate refinement accounting");
  std::vector<Bits> restricted;int core_words=(result.core_rows+63)/64;
  for(const auto& block:result.blocks){if(squarez(block.value))continue;Bits eq(core_words);int column=0;
    for(int row=0;row<result.dedup_rows;++row)if(active[row]){if(block.exponents[row]&1U)bit_flip(eq,column);++column;}if(!bit_zero(eq))restricted.push_back(std::move(eq));}
  require(matrix_rank(std::move(restricted),result.core_rows)==result.core_rank,"core rank replay");

  BitBasis low(result.core_rows);bool useful_low=false;
  for(int i=0;i<result.core_rows;++i){budget.require_active();++result.singleton_tests;cpp_int root;if(!squarez(core[i].value,&root))continue;
    Bits bits(core_words);bit_flip(bits,i);RelationRecord relation=make_relation(c.index,"SINGLETON",{&core[i]},c.N,bits);
    require(is_kernel_vector(bits,core_decoder),"singleton outside core kernel");
    if(relation.root_class=="USEFUL")useful_low=true;else low.insert(bits);account_relation(result,std::move(relation),true,budget);
  }
  for(int i=0;i<result.core_rows;++i)for(int j=i+1;j<result.core_rows;++j){budget.require_active();++result.pair_tests;cpp_int root;if(!same_square_class(core[i].value,core[j].value,&root))continue;
    Bits bits(core_words);bit_flip(bits,i);bit_flip(bits,j);RelationRecord relation=make_relation(c.index,"SUPPORT_TWO",{&core[i],&core[j]},c.N,bits);
    require(is_kernel_vector(bits,core_decoder),"support two outside core kernel");
    if(relation.root_class=="USEFUL")useful_low=true;else low.insert(bits);account_relation(result,std::move(relation),true,budget);
  }
  if(!useful_low){for(const auto& kernel:core_decoder.kernel){budget.require_active();Bits remainder=low.reduce(kernel);if(bit_zero(remainder)||!low.insert(remainder))continue;
      std::vector<const Row*> selected;for(int i=0;i<result.core_rows;++i)if(bit_get(remainder,i))selected.push_back(&core[i]);
      require(is_kernel_vector(remainder,core_decoder),"residual outside core kernel");
      account_relation(result,make_relation(c.index,"RESIDUAL",selected,c.N,remainder),true,budget);}
    require(low.dimension()==result.core_nullity,"complete P66 quotient");
  }
  return result;
}

std::string sparse_exponents(const Block& block) {
  std::ostringstream out;bool first=true;
  for(int i=0;i<static_cast<int>(block.exponents.size());++i)if(block.exponents[i]){
    if(!first)out<<',';first=false;out<<i<<':'<<block.exponents[i];
  }
  return out.str();
}

std::string block_list(const std::vector<int>& blocks) {
  std::ostringstream out;for(std::size_t i=0;i<blocks.size();++i){if(i)out<<',';out<<blocks[i];}return out.str();
}

struct Aggregate {
  int cases=0;
  u64 original=0,dedup=0,peeled=0,core=0,private_loss=0,pair_tests=0;
  u64 relations=0,useful=0,pure=0,cross=0,pure_core=0,cross_core=0;
};

struct RelationWitness {
  bool set=false;
  int case_index=-1,factor_bits=0;
  cpp_int N;
  std::string cohort,shape;
  RelationRecord relation;
};

struct CaseWitness {
  bool set=false;
  int case_index=-1,factor_bits=0;
  cpp_int N;
  std::string cohort,shape;
};

class OutputWriter {
 public:
  OutputWriter(const std::string& directory,GlobalBudget& budget):directory_(directory),budget_(budget) {
    require(!std::filesystem::exists(directory_),"output directory exists");
    std::filesystem::create_directories(directory_);
    cases_.open(directory_/ "cases.tsv",std::ios::binary);
    rows_.open(directory_/ "rows.tsv",std::ios::binary);
    blocks_.open(directory_/ "blocks.tsv",std::ios::binary);
    peeling_.open(directory_/ "peeling.tsv",std::ios::binary);
    relations_.open(directory_/ "relations.tsv",std::ios::binary);
    require(bool(cases_)&&bool(rows_)&&bool(blocks_)&&bool(peeling_)&&bool(relations_),"open streamed outputs");
    emit(cases_,"case_index\tcell_index\tN\tcohort\tshape\tfactor_bits\toriginal_rows\tdedup_rows\tpeeled_rows\tcore_rows"
                "\toriginal_rank\toriginal_nullity\tdedup_rank\tdedup_nullity\tcore_rank\tcore_nullity\tfamily_rank_sum\tcross_dimension_gain"
                "\tseparate_private_rows\tunion_private_rows\toriginal_union_private_rows\tprivate_pivot_loss\toriginal_private_pivot_loss"
                "\tpeel_rounds\trefine_steps\tcore_refine_steps\tsingleton_tests\tsupport_two_tests\tduplicate_relations\tsingleton_relations"
                "\tsupport_two_relations\tresidual_relations\tuseful_relations\tpure_relations\tcross_relations\tpure_core_relations\tcross_core_relations\tfamily_ranks\n");
    emit(rows_,"case_index\tN\tcohort\tshape\tfactor_bits\tretained_row\tU\tY\tprovenance_count\tprovenance\n");
    emit(blocks_,"case_index\tN\tcohort\tshape\tfactor_bits\tblock\tvalue\tsquare_class\texponents\tinitial_degree\tcore_degree\n");
    emit(peeling_,"case_index\tN\tcohort\tshape\tfactor_bits\tround\tretained_row\twitness_blocks\tprovenance\n");
    emit(relations_,"case_index\tN\tcohort\tshape\tfactor_bits\tsequence\tkind\tsupport\tfamily_class\tprovenance\texact_root\tsupplied_root"
                    "\tnormalized_root\tgcd_minus\tgcd_plus\troot_class\n");
  }

  void write_case(const CaseResult& r) {
    std::vector<std::string> family_ranks;
    for(int rank:r.family_ranks)family_ranks.push_back(std::to_string(rank));
    std::ostringstream line;
    line<<r.case_index<<'\t'<<r.cell_index<<'\t'<<r.N<<'\t'<<r.cohort<<'\t'<<r.shape<<'\t'<<r.factor_bits<<'\t'
        <<r.original_rows<<'\t'<<r.dedup_rows<<'\t'<<r.peeled_rows<<'\t'<<r.core_rows<<'\t'<<r.original_rank<<'\t'<<r.original_nullity<<'\t'
        <<r.dedup_rank<<'\t'<<r.dedup_nullity<<'\t'<<r.core_rank<<'\t'<<r.core_nullity<<'\t'<<r.family_rank_sum<<'\t'<<r.cross_gain<<'\t'
        <<r.separate_private<<'\t'<<r.union_private<<'\t'<<r.original_union_private<<'\t'<<r.private_loss<<'\t'<<r.original_private_loss<<'\t'
        <<r.peel_rounds<<'\t'<<r.refine_steps<<'\t'<<r.core_refine_steps<<'\t'<<r.singleton_tests<<'\t'<<r.pair_tests<<'\t'
        <<r.duplicate_relations<<'\t'<<r.singleton_relations<<'\t'<<r.pair_relations<<'\t'<<r.residual_relations<<'\t'<<r.useful_relations<<'\t'
        <<r.pure_relations<<'\t'<<r.cross_relations<<'\t'<<r.pure_core_relations<<'\t'<<r.cross_core_relations<<'\t'<<join(family_ranks,",")<<'\n';
    emit(cases_,line.str());

    for(const auto& row:r.rows){line.str("");line.clear();
      line<<r.case_index<<'\t'<<r.N<<'\t'<<r.cohort<<'\t'<<r.shape<<'\t'<<r.factor_bits<<'\t'<<row.retained_id<<'\t'
          <<row.value<<'\t'<<row.root<<'\t'<<row.provenance.size()<<'\t'<<row_provenance(row)<<'\n';
      emit(rows_,line.str());
    }
    for(int i=0;i<static_cast<int>(r.blocks.size());++i){line.str("");line.clear();
      line<<r.case_index<<'\t'<<r.N<<'\t'<<r.cohort<<'\t'<<r.shape<<'\t'<<r.factor_bits<<'\t'<<i<<'\t'
          <<r.blocks[i].value<<'\t'<<(squarez(r.blocks[i].value)?"SQUARE":"NONSQUARE")<<'\t'<<sparse_exponents(r.blocks[i])<<'\t'
          <<r.block_initial_degree[i]<<'\t'<<r.block_core_degree[i]<<'\n';
      emit(blocks_,line.str());
    }
    for(const auto& p:r.peeling){line.str("");line.clear();
      line<<r.case_index<<'\t'<<r.N<<'\t'<<r.cohort<<'\t'<<r.shape<<'\t'<<r.factor_bits<<'\t'<<p.round<<'\t'
          <<p.row<<'\t'<<block_list(p.blocks)<<'\t'<<p.provenance<<'\n';
      emit(peeling_,line.str());
    }
    for(const auto& relation:r.relations){
      require(!relation.serialized.empty(),"missing reserved relation serialization");
      emit(relations_,relation.serialized,true);
      if(relation.root_class=="USEFUL"&&relation_less(r,relation,useful_))copy_relation(r,relation,useful_);
      if(relation.family_class=="CROSS_FAMILY"&&relation_less(r,relation,cross_))copy_relation(r,relation,cross_);
    }

    std::vector<std::tuple<std::string,std::string,int,std::string>> keys={
      {"ALL","ALL",-1,"ALL"},{"COHORT",r.cohort,-1,"ALL"},{"BITS","ALL",r.factor_bits,"ALL"},{"SHAPE","ALL",-1,r.shape},
      {"COHORT_BITS_SHAPE",r.cohort,r.factor_bits,r.shape}};
    for(const auto& key:keys){auto& a=aggregate_[key];++a.cases;a.original+=r.original_rows;a.dedup+=r.dedup_rows;a.peeled+=r.peeled_rows;a.core+=r.core_rows;
      a.private_loss+=r.private_loss;a.pair_tests+=r.pair_tests;a.relations+=r.relations.size();a.useful+=r.useful_relations;
      a.pure+=r.pure_relations;a.cross+=r.cross_relations;a.pure_core+=r.pure_core_relations;a.cross_core+=r.cross_core_relations;}

    bool clean=r.cohort=="CLEAN";++case_count_;clean_cases_+=clean;control_cases_+=!clean;total_core_+=r.core_rows;
    total_useful_+=r.useful_relations;total_relations_+=r.relations.size();
    clean_nonempty_+=clean&&r.core_rows>0;clean_cross_core_+=clean&&r.core_rows>0&&r.cross_core_relations>0;
    if(clean&&r.private_loss>0)++clean_loss_cells_[{r.factor_bits,r.shape}];
    if(r.core_rows>0&&case_less(r,nonempty_))copy_case(r,nonempty_);
    if(r.private_loss>0&&case_less(r,pivot_))copy_case(r,pivot_);
  }

  void finish(const std::string& mode,int workers,const std::vector<int>& selected) {
    require(total_relations_==static_cast<u64>(budget_.reserved_relations()),"global relation count reservation");
    bool repeated_loss=false;for(const auto& [cell,count]:clean_loss_cells_)repeated_loss|=count>=2;

    std::ostringstream out;
    out<<"scope\tcohort\tfactor_bits\tshape\tcases\toriginal_rows\tdedup_rows\tpeeled_rows\tcore_rows\tprivate_pivot_loss"
         "\tsupport_two_tests\trelations\tuseful_relations\tpure_relations\tcross_relations\tpure_core_relations\tcross_core_relations\n";
    for(const auto& [key,a]:aggregate_){const auto& [scope,cohort,bits,shape]=key;
      out<<scope<<'\t'<<cohort<<'\t'<<(bits<0?"ALL":std::to_string(bits))<<'\t'<<shape<<'\t'
         <<a.cases<<'\t'<<a.original<<'\t'<<a.dedup<<'\t'<<a.peeled<<'\t'<<a.core<<'\t'<<a.private_loss<<'\t'<<a.pair_tests<<'\t'
         <<a.relations<<'\t'<<a.useful<<'\t'<<a.pure<<'\t'<<a.cross<<'\t'<<a.pure_core<<'\t'<<a.cross_core<<'\n';
    }
    write_single("aggregates.tsv",out.str());

    out.str("");out.clear();
    out<<"category\tcase_index\tN\tcohort\tshape\tfactor_bits\tkind\tsupport\tfamily_class\tprovenance\texact_root\tsupplied_root"
         "\tnormalized_root\tgcd_minus\tgcd_plus\troot_class\n";
    const RelationWitness* relation_choice=useful_.set?&useful_:(cross_.set?&cross_:nullptr);
    if(relation_choice){const auto& w=*relation_choice;const auto& relation=w.relation;
      out<<(useful_.set?"USEFUL_RELATION":"CROSS_FAMILY_RELATION")<<'\t'<<w.case_index<<'\t'<<w.N<<'\t'<<w.cohort<<'\t'
         <<w.shape<<'\t'<<w.factor_bits<<'\t'<<relation.kind<<'\t'<<relation.support<<'\t'<<relation.family_class<<'\t'
         <<relation.provenance<<'\t'<<relation.exact_root<<'\t'<<relation.supplied_root<<'\t'<<relation.normalized<<'\t'
         <<relation.gcd_minus<<'\t'<<relation.gcd_plus<<'\t'<<relation.root_class<<'\n';
    }else{const CaseWitness* chosen=nonempty_.set?&nonempty_:(pivot_.set?&pivot_:nullptr);
      if(chosen)out<<(nonempty_.set?"NONEMPTY_CORE":"PIVOT_LOSS")<<'\t'<<chosen->case_index<<'\t'<<chosen->N<<'\t'
                    <<chosen->cohort<<'\t'<<chosen->shape<<'\t'<<chosen->factor_bits<<"\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-\n";
      else out<<"NONE\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-\t-\n";
    }
    write_single("witness.tsv",out.str());

    std::string status;
    if(mode=="preflight")status="PREFLIGHT_ONLY";
    else if(total_core_==0)status="POSTHOC_EMPTY_CORE_KILL";
    else if(clean_cases_==kCleanCases&&clean_cross_core_>0)status="POSTHOC_CROSS_CORE_LEAD";
    else if(clean_cases_==kCleanCases&&clean_nonempty_>0&&repeated_loss)status="POSTHOC_REPEATABLE_PIVOT_LOSS";
    else status="POSTHOC_NULL";
    out.str("");out.clear();
    out<<"key\tvalue\nanalysis_mode\t"<<mode<<"\nevidence_class\tPOSTHOC_DISCOVERY_ONLY\ncases\t"<<case_count_
       <<"\nclean_cases\t"<<clean_cases_<<"\ncontrol_cases\t"<<control_cases_<<"\noriginal_rows\t"<<u64(case_count_)*kOriginalRows
       <<"\ncore_rows\t"<<total_core_<<"\nclean_nonempty_cores\t"<<clean_nonempty_<<"\nclean_cross_core_cases\t"<<clean_cross_core_
       <<"\nrepeatable_clean_pivot_loss_cell\t"<<repeated_loss<<"\nrelations\t"<<total_relations_
       <<"\nuseful_relations\t"<<total_useful_<<"\nstatus\t"<<status
       <<"\ninterpretation\tFINITE_POSTHOC_HYPOTHESIS_GENERATION_NOT_A_THEOREM\n";
    write_single("summary.tsv",out.str());

    out.str("");out.clear();
    out<<"key\tvalue\nversion\tF270-D02\nmode\t"<<mode<<"\nworkers\t"<<workers
       <<"\nevidence_sha256\t"<<kEvidenceSha<<"\nbanks_sha256\t"<<kBanksSha<<"\ncorpus_sha256\t"<<kCorpusSha
       <<"\nglobal_relation_count\t"<<budget_.reserved_relations()
       <<"\nrelation_payload_bytes\t"<<budget_.reserved_relation_payload()<<"\nselected_case_indices\t";
    for(std::size_t i=0;i<selected.size();++i){if(i)out<<',';out<<selected[i];}
    out<<"\n";
    write_single("metadata.tsv",out.str());

    cases_.close();rows_.close();blocks_.close();peeling_.close();relations_.close();
    require(!cases_.fail()&&!rows_.fail()&&!blocks_.fail()&&!peeling_.fail()&&!relations_.fail(),"close streamed outputs");
    std::set<std::string> expected={"aggregates.tsv","blocks.tsv","cases.tsv","metadata.tsv","peeling.tsv",
                                    "relations.tsv","rows.tsv","summary.tsv","witness.tsv"};
    u64 bytes=0;std::set<std::string> observed;
    for(const auto& entry:std::filesystem::directory_iterator(directory_)){
      require(entry.is_regular_file(),"non-regular output");observed.insert(entry.path().filename().string());
      bytes+=entry.file_size();
    }
    require(observed==expected,"output file set");
    require(bytes==budget_.reserved_output(),"exact output-byte ledger");
  }

 private:
  std::filesystem::path directory_;
  GlobalBudget& budget_;
  std::ofstream cases_,rows_,blocks_,peeling_,relations_;
  std::map<std::tuple<std::string,std::string,int,std::string>,Aggregate> aggregate_;
  std::map<std::pair<int,std::string>,int> clean_loss_cells_;
  RelationWitness useful_,cross_;
  CaseWitness nonempty_,pivot_;
  int case_count_=0,clean_cases_=0,control_cases_=0,clean_nonempty_=0,clean_cross_core_=0;
  u64 total_core_=0,total_useful_=0,total_relations_=0;

  void emit(std::ofstream& stream,const std::string& text,bool reserved=false) {
    require(text.size()<=kMaxOutputLineBytes,"OUTPUT_LINE_BYTES_CAP");
    if(!reserved)budget_.reserve_output(text.size());
    stream.write(text.data(),text.size());require(bool(stream),"streamed output write");
  }
  void write_single(const std::string& name,const std::string& text) {
    require(text.size()<=kMaxOutputLineBytes,"OUTPUT_FILE_BUFFER_CAP");
    budget_.reserve_output(text.size());
    std::ofstream stream(directory_/name,std::ios::binary);require(bool(stream),"open output "+name);
    stream.write(text.data(),text.size());require(bool(stream),"write output "+name);
    stream.close();require(!stream.fail(),"close output "+name);
  }
  static bool relation_less(const CaseResult& r,const RelationRecord& relation,const RelationWitness& prior) {
    if(!prior.set)return true;
    if(r.N!=prior.N)return r.N<prior.N;
    if(r.case_index!=prior.case_index)return r.case_index<prior.case_index;
    if(relation.kind!=prior.relation.kind)return relation.kind<prior.relation.kind;
    if(relation.support!=prior.relation.support)return relation.support<prior.relation.support;
    return relation.provenance<prior.relation.provenance;
  }
  static void copy_relation(const CaseResult& r,const RelationRecord& relation,RelationWitness& target) {
    target.set=true;target.case_index=r.case_index;target.factor_bits=r.factor_bits;target.N=r.N;
    target.cohort=r.cohort;target.shape=r.shape;target.relation=relation;
    target.relation.bits.clear();target.relation.serialized.clear();
  }
  static bool case_less(const CaseResult& r,const CaseWitness& prior) {
    return !prior.set||r.N<prior.N||(r.N==prior.N&&r.case_index<prior.case_index);
  }
  static void copy_case(const CaseResult& r,CaseWitness& target) {
    target.set=true;target.case_index=r.case_index;target.factor_bits=r.factor_bits;target.N=r.N;
    target.cohort=r.cohort;target.shape=r.shape;
  }
};

void self_test() {
  require(sha256("abc")=="ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad","SHA-256 KAT");
  Row a;a.retained_id=0;a.value=2;a.root=550;Provenance pa;pa.original=0;pa.family=0;pa.row=0;pa.root=550;pa.syntax="a";a.provenance={pa};
  Row b;b.retained_id=1;b.value=8;b.root=403;Provenance pb;pb.original=1;pb.family=1;pb.row=0;pb.root=403;pb.syntax="b";b.provenance={pb};
  Decoder da=decode_rows({a}),db=decode_rows({b}),du=decode_rows({a,b});
  require(da.rank==1&&db.rank==1&&du.rank==1&&du.kernel.size()==1,"697 union witness rank");
  RelationRecord witness=make_relation(0,"SUPPORT_TWO",{&a,&b},cpp_int(697));
  require(witness.exact_root==4&&witness.supplied_root==4&&witness.root_class=="GLOBAL_PLUS","697 union witness roots");
  Row duplicate=a;duplicate.value=4;duplicate.root=2;duplicate.provenance[0].root=2;
  Provenance mismatch=duplicate.provenance[0];mismatch.original=2;mismatch.family=1;mismatch.root=7;
  RelationRecord useful=make_duplicate_relation(0,duplicate,duplicate.provenance[0],mismatch,cpp_int(15));
  require(useful.root_class=="USEFUL"&&useful.gcd_minus==5&&useful.gcd_plus==3,"duplicate mismatch factor");
  std::vector<Row> circuit;
  for(int i=0;i<4;++i){Row row;row.retained_id=i;row.value=std::array<int,4>{6,10,15,7}[i];circuit.push_back(row);}
  Decoder dc=decode_rows(circuit);require(dc.rank==3&&dc.kernel.size()==1&&bit_weight(dc.kernel[0])==3,"peeling circuit decoder");
  Decoder core=decode_rows({circuit[0],circuit[1],circuit[2]});require(core.rank==2&&core.kernel.size()==1,"peeling fixed core");
  std::cout<<"SELF_TEST_OK\n";
}

}  // namespace

int main(int argc,char** argv) {
  try {
    if(argc==2&&std::string(argv[1])=="--self-test"){self_test();return 0;}
    std::map<std::string,std::string> args;
    for(int i=1;i<argc;i+=2){require(i+1<argc,"missing CLI value");std::string key=argv[i];require(key.rfind("--",0)==0,"CLI key");require(args.emplace(key,argv[i+1]).second,"duplicate CLI key");}
    for(const char* key:{"--mode","--evidence","--banks","--corpus","--out-dir","--workers","--output-budget"})require(args.count(key),std::string("missing ")+key);
    require(args.size()==7,"unknown CLI key");std::string mode=args["--mode"];require(mode=="preflight"||mode=="target","mode");
    int workers=std::stoi(args["--workers"]);require(workers>=1&&workers<=8,"workers");
    cpp_int requested_budget=parse_positive(args["--output-budget"]);require(requested_budget<=kMaxOutputBytes,"output budget cap");
    u64 output_budget=requested_budget.convert_to<u64>();
    std::string corpus_bytes=read_file(args["--corpus"]),bank_bytes=read_file(args["--banks"]),evidence_bytes=read_file(args["--evidence"]);
    std::vector<Case> cases=parse_corpus(corpus_bytes);auto labels=parse_banks(bank_bytes,cases);OriginalBanks banks=parse_evidence(evidence_bytes,cases);
    int clean=0;for(auto& c:cases){const auto& flags=labels.at({c.shape,c.factor_bits,c.index});c.clean=true;for(bool earlier:flags)c.clean&=!earlier;clean+=c.clean;}
    require(clean==kCleanCases,"clean-case count");
    std::vector<int> selected;
    if(mode=="target"){for(int i=0;i<static_cast<int>(cases.size());++i)selected.push_back(i);}
    else {
      const std::array<std::string,4> shapes={"marker-control","neighbor","random","safe-safe"};
      for(bool want_clean:{true,false})for(const auto& shape:shapes){int best=-1;
        for(const auto& c:cases)if(c.clean==want_clean&&c.shape==shape&&(best<0||c.factor_bits>cases[best].factor_bits||
            (c.factor_bits==cases[best].factor_bits&&c.index<best)))best=c.index;
        if(best>=0&&std::find(selected.begin(),selected.end(),best)==selected.end())selected.push_back(best);
      }
      std::vector<int> order(cases.size());for(int i=0;i<static_cast<int>(cases.size());++i)order[i]=i;
      std::sort(order.begin(),order.end(),[&](int a,int b){if(cases[a].factor_bits!=cases[b].factor_bits)return cases[a].factor_bits>cases[b].factor_bits;return a<b;});
      for(int id:order)if(selected.size()<8&&std::find(selected.begin(),selected.end(),id)==selected.end())selected.push_back(id);
      require(selected.size()==8,"preflight selection");std::sort(selected.begin(),selected.end());
    }
    GlobalBudget budget(output_budget);OutputWriter writer(args["--out-dir"],budget);
    for(std::size_t begin=0;begin<selected.size();begin+=std::size_t(workers)){
      std::size_t count=std::min<std::size_t>(std::size_t(workers),selected.size()-begin);
      std::vector<CaseResult> results(count);std::atomic<std::size_t> next{0};std::exception_ptr error;std::mutex error_mutex;
      auto worker=[&](){try{for(;;){std::size_t slot=next.fetch_add(1);if(slot>=count)break;const Case& c=cases[selected[begin+slot]];
            results[slot]=analyze_case(c,banks.at({c.shape,c.factor_bits,c.index}),budget);}}
        catch(...){budget.cancel();std::lock_guard<std::mutex> lock(error_mutex);if(!error)error=std::current_exception();next.store(count);}};
      std::vector<std::thread> pool;for(int i=0;i<std::min<int>(workers,static_cast<int>(count));++i)pool.emplace_back(worker);
      for(auto& thread:pool)thread.join();if(error)std::rethrow_exception(error);
      for(const auto& result:results)writer.write_case(result);
    }
    writer.finish(mode,workers,selected);
    std::cout<<"F270_OK mode="<<mode<<" cases="<<selected.size()<<" output_bytes="<<budget.reserved_output()
             <<" relations="<<budget.reserved_relations()<<" out="<<args["--out-dir"]<<'\n';return 0;
  }catch(const std::exception& error){std::cerr<<"F270_ERROR\t"<<error.what()<<'\n';return 1;}
}
