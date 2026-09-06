#include <algorithm>
#include <array>
#include <cerrno>
#include <clocale>
#include <cstdint>
#include <cstring>
#include <dirent.h>
#include <fcntl.h>
#include <iomanip>
#include <initializer_list>
#include <iostream>
#include <map>
#include <set>
#include <sstream>
#include <stdexcept>
#include <string>
#include <sys/stat.h>
#include <sys/types.h>
#include <tuple>
#include <unistd.h>
#include <utility>
#include <vector>

#include <boost/multiprecision/cpp_int.hpp>
#include <boost/multiprecision/integer.hpp>

// Independently authored F265-D18 fixture verifier.  This source deliberately
// has its own path walker, parsers, integer facade, SHA-256, FNV, GF(2), and
// fixture reconstruction.  It includes no corpus or private-label parser and
// no fixture-root placeholder.

namespace verify_d18 {

using Big = boost::multiprecision::cpp_int;

class Error final : public std::exception {
 public:
  explicit Error(std::string message) : message_(std::move(message)) {}
  const char* what() const noexcept override { return message_.c_str(); }
 private:
  std::string message_;
};

constexpr const char* VERSION = "F265-D18";

uint32_t rr(uint32_t v, int n) { return (v >> n) | (v << (32 - n)); }

std::string hash256(const std::string& input) {
  static const uint32_t C[64] = {
      0x428a2f98,0x71374491,0xb5c0fbcf,0xe9b5dba5,0x3956c25b,0x59f111f1,0x923f82a4,0xab1c5ed5,
      0xd807aa98,0x12835b01,0x243185be,0x550c7dc3,0x72be5d74,0x80deb1fe,0x9bdc06a7,0xc19bf174,
      0xe49b69c1,0xefbe4786,0x0fc19dc6,0x240ca1cc,0x2de92c6f,0x4a7484aa,0x5cb0a9dc,0x76f988da,
      0x983e5152,0xa831c66d,0xb00327c8,0xbf597fc7,0xc6e00bf3,0xd5a79147,0x06ca6351,0x14292967,
      0x27b70a85,0x2e1b2138,0x4d2c6dfc,0x53380d13,0x650a7354,0x766a0abb,0x81c2c92e,0x92722c85,
      0xa2bfe8a1,0xa81a664b,0xc24b8b70,0xc76c51a3,0xd192e819,0xd6990624,0xf40e3585,0x106aa070,
      0x19a4c116,0x1e376c08,0x2748774c,0x34b0bcb5,0x391c0cb3,0x4ed8aa4a,0x5b9cca4f,0x682e6ff3,
      0x748f82ee,0x78a5636f,0x84c87814,0x8cc70208,0x90befffa,0xa4506ceb,0xbef9a3f7,0xc67178f2};
  uint32_t H[8] = {0x6a09e667,0xbb67ae85,0x3c6ef372,0xa54ff53a,
                   0x510e527f,0x9b05688c,0x1f83d9ab,0x5be0cd19};
  std::vector<unsigned char> data(input.begin(), input.end());
  uint64_t bit_count = static_cast<uint64_t>(data.size()) * 8;
  data.push_back(0x80);
  while ((data.size() & 63U) != 56U) data.push_back(0);
  for (int shift = 56; shift >= 0; shift -= 8)
    data.push_back(static_cast<unsigned char>(bit_count >> shift));
  for (size_t offset = 0; offset < data.size(); offset += 64) {
    uint32_t m[64];
    for (int i = 0; i < 16; ++i) {
      const unsigned char* q = &data[offset + 4 * i];
      m[i] = (uint32_t(q[0]) << 24) | (uint32_t(q[1]) << 16) |
             (uint32_t(q[2]) << 8) | uint32_t(q[3]);
    }
    for (int i = 16; i < 64; ++i) {
      uint32_t a = rr(m[i-15],7) ^ rr(m[i-15],18) ^ (m[i-15] >> 3);
      uint32_t b = rr(m[i-2],17) ^ rr(m[i-2],19) ^ (m[i-2] >> 10);
      m[i] = m[i-16] + a + m[i-7] + b;
    }
    uint32_t a=H[0],b=H[1],c=H[2],d=H[3],e=H[4],f=H[5],g=H[6],h=H[7];
    for (int i=0;i<64;++i) {
      uint32_t t1=h+(rr(e,6)^rr(e,11)^rr(e,25))+((e&f)^((~e)&g))+C[i]+m[i];
      uint32_t t2=(rr(a,2)^rr(a,13)^rr(a,22))+((a&b)^(a&c)^(b&c));
      h=g;g=f;f=e;e=d+t1;d=c;c=b;b=a;a=t1+t2;
    }
    H[0]+=a;H[1]+=b;H[2]+=c;H[3]+=d;H[4]+=e;H[5]+=f;H[6]+=g;H[7]+=h;
  }
  std::ostringstream s;s<<std::hex<<std::setfill('0');
  for(uint32_t x:H)s<<std::setw(8)<<x;
  return s.str();
}

std::string fnv_hex(const std::string& bytes) {
  uint64_t value=UINT64_C(14695981039346656037);
  for(unsigned char b:bytes)value=(value^b)*UINT64_C(1099511628211);
  std::ostringstream s;s<<std::hex<<std::setw(16)<<std::setfill('0')<<value;
  return s.str();
}

std::vector<std::string> fields(const std::string& line) {
  std::vector<std::string> out;size_t begin=0;
  for(;;){size_t end=line.find('\t',begin);out.push_back(line.substr(begin,end-begin));if(end==std::string::npos)break;begin=end+1;}
  return out;
}

std::vector<std::string> lines(const std::string& file) {
  if(file.empty()||file.back()!='\n'||file.find('\r')!=std::string::npos||file.find('\0')!=std::string::npos)throw Error("TSV_BYTES");
  std::vector<std::string> out;size_t begin=0;
  while(begin<file.size()){size_t end=file.find('\n',begin);out.push_back(file.substr(begin,end-begin));begin=end+1;}
  return out;
}

bool dec(const std::string& s) {
  if(s.empty()||(s.size()>1&&s[0]=='0'))return false;
  return std::all_of(s.begin(),s.end(),[](unsigned char c){return c>='0'&&c<='9';});
}

bool hex(const std::string& s) {
  if(s.empty()||(s.size()>1&&s[0]=='0'))return false;
  return std::all_of(s.begin(),s.end(),[](unsigned char c){return (c>='0'&&c<='9')||(c>='a'&&c<='f');});
}

uint64_t udec(const std::string& s) {
  if(!dec(s))throw Error("DEC");uint64_t v=0;
  for(char c:s){if(v>(UINT64_MAX-uint64_t(c-'0'))/10)throw Error("DEC_RANGE");v=v*10+uint64_t(c-'0');}
  return v;
}

Big integer_hex(const std::string& s) {
  if(!hex(s))throw Error("HEX");Big x=0;
  for(char c:s)x=(x<<4)+(c<='9'?c-'0':c-'a'+10);
  return x;
}

std::string xhex(const Big& x) {
  if(x<0)throw Error("NEGATIVE_HEX");std::ostringstream s;s<<std::hex<<x;return s.str();
}

Big modulo(Big a,const Big& n){a%=n;if(a<0)a+=n;return a;}
Big common(Big a,Big b){if(a<0)a=-a;if(b<0)b=-b;while(b!=0){Big r=a%b;a=b;b=r;}return a;}
Big ipow(Big a,unsigned e){Big r=1;while(e){if(e&1U)r*=a;e>>=1;if(e)a*=a;}return r;}
Big modpow(Big a,unsigned e,const Big& n){a=modulo(a,n);Big r=1%n;while(e){if(e&1U)r=r*a%n;e>>=1;if(e)a=a*a%n;}return r;}
unsigned width(const Big& x){if(x<=0)throw Error("WIDTH");return static_cast<unsigned>(boost::multiprecision::msb(x))+1;}
Big square_root(const Big& n){if(n<0)throw Error("SQRT_DOMAIN");if(n<2)return n;Big x=Big(1)<<((width(n)+1)/2);for(;;){Big y=(x+n/x)>>1;if(y>=x)return x;x=y;}}

bool is_prime(uint64_t n) {
  if(n<2)return false;if((n&1)==0)return n==2;
  for(uint64_t d=3;d<=n/d;d+=2)if(n%d==0)return false;
  return true;
}

struct RootHandle {
  int descriptor=-1;
  dev_t device=0;ino_t inode=0;mode_t permissions=0;uid_t uid=0;gid_t gid=0;
};

bool abs_grammar(const std::string& path) {
  if(path.size()<2||path.size()>1024||path.front()!='/'||path.back()=='/')return false;
  size_t p=1;
  while(p<path.size()){
    size_t e=path.find('/',p);if(e==std::string::npos)e=path.size();
    std::string c=path.substr(p,e-p);if(c.empty()||c=="."||c=="..")return false;
    for(unsigned char x:c)if(!((x>='A'&&x<='Z')||(x>='a'&&x<='z')||(x>='0'&&x<='9')||x=='_'||x=='-'||x=='.'))return false;
    p=e+1;
  }
  return true;
}

RootHandle directory(const std::string& path,bool output) {
  int current=::open("/",O_RDONLY|O_DIRECTORY|O_CLOEXEC);if(current<0)throw Error("ROOT_OPEN");
  for(size_t p=1;p<path.size();){size_t e=path.find('/',p);if(e==std::string::npos)e=path.size();std::string c=path.substr(p,e-p);int next=openat(current,c.c_str(),O_RDONLY|O_DIRECTORY|O_NOFOLLOW|O_CLOEXEC);int saved=errno;close(current);errno=saved;if(next<0)throw Error("COMPONENT_OPEN");current=next;p=e+1;}
  struct stat st{};if(fstat(current,&st)||!S_ISDIR(st.st_mode)){close(current);throw Error("DIRECTORY_TYPE");}
  if(output&&(st.st_uid!=geteuid()||(st.st_mode&077)!=0)){close(current);throw Error("OUTPUT_MODE");}
  return {current,st.st_dev,st.st_ino,mode_t(st.st_mode&07777),st.st_uid,st.st_gid};
}

std::vector<std::string> listing(int root) {
  int copy=dup(root);if(copy<0)throw Error("DUP");DIR* d=fdopendir(copy);if(!d){close(copy);throw Error("DIR_STREAM");}
  std::vector<std::string> n;errno=0;
  while(auto* e=readdir(d)){std::string x=e->d_name;if(x!="."&&x!="..")n.push_back(x);}
  int saved=errno;if(closedir(d)||saved)throw Error("ENUMERATE");std::sort(n.begin(),n.end());return n;
}

bool below(int child,dev_t device,ino_t inode) {
  int here=dup(child);if(here<0)throw Error("ANCESTRY_DUP");
  for(;;){struct stat current{};if(fstat(here,&current)){close(here);throw Error("ANCESTRY_STAT");}if(current.st_dev==device&&current.st_ino==inode){close(here);return true;}int parent=openat(here,"..",O_RDONLY|O_DIRECTORY|O_NOFOLLOW|O_CLOEXEC);if(parent<0){close(here);throw Error("ANCESTRY_OPEN");}struct stat upper{};if(fstat(parent,&upper)){close(parent);close(here);throw Error("ANCESTRY_PARENT_STAT");}if(upper.st_dev==current.st_dev&&upper.st_ino==current.st_ino){close(parent);close(here);return false;}close(here);here=parent;}
}

std::string read_member(int root,const std::string& name,size_t cap) {
  int fd=openat(root,name.c_str(),O_RDONLY|O_NOFOLLOW|O_CLOEXEC);if(fd<0)throw Error("INPUT_OPEN");
  struct stat before{},after{};if(fstat(fd,&before)||!S_ISREG(before.st_mode)||before.st_nlink<1){close(fd);throw Error("INPUT_META");}
  if(before.st_size<0||static_cast<uint64_t>(before.st_size)>cap){close(fd);throw Error("INPUT_CAP");}
  std::string data;data.reserve(static_cast<size_t>(before.st_size));std::array<char,32749> b{};
  for(;;){ssize_t n=read(fd,b.data(),b.size());if(n<0){close(fd);throw Error("INPUT_READ");}if(n==0)break;data.append(b.data(),static_cast<size_t>(n));}
  if(fstat(fd,&after)||before.st_dev!=after.st_dev||before.st_ino!=after.st_ino||before.st_size!=after.st_size||mode_t(before.st_mode&07777)!=mode_t(after.st_mode&07777)||before.st_uid!=after.st_uid||before.st_gid!=after.st_gid||before.st_nlink!=after.st_nlink){close(fd);throw Error("INPUT_CHANGED");}
#if defined(__APPLE__)
  if(before.st_mtimespec.tv_sec!=after.st_mtimespec.tv_sec||before.st_mtimespec.tv_nsec!=after.st_mtimespec.tv_nsec||before.st_ctimespec.tv_sec!=after.st_ctimespec.tv_sec||before.st_ctimespec.tv_nsec!=after.st_ctimespec.tv_nsec){close(fd);throw Error("INPUT_TIME_CHANGED");}
#else
  if(before.st_mtim.tv_sec!=after.st_mtim.tv_sec||before.st_mtim.tv_nsec!=after.st_mtim.tv_nsec||before.st_ctim.tv_sec!=after.st_ctim.tv_sec||before.st_ctim.tv_nsec!=after.st_ctim.tv_nsec){close(fd);throw Error("INPUT_TIME_CHANGED");}
#endif
  if(lseek(fd,0,SEEK_SET)!=0){close(fd);throw Error("INPUT_REWIND");}
  std::string second;for(;;){ssize_t n=read(fd,b.data(),b.size());if(n<0){close(fd);throw Error("INPUT_REREAD");}if(!n)break;second.append(b.data(),static_cast<size_t>(n));}
  if(close(fd)||data!=second||hash256(data)!=hash256(second))throw Error("INPUT_REAUTH");return data;
}

void write_output(int root,const std::string& final,const std::string& bytes,size_t cap) {
  if(bytes.size()>cap)throw Error("OUTPUT_CAP");std::string temp="."+final+".tmp";
  int fd=openat(root,temp.c_str(),O_WRONLY|O_CREAT|O_EXCL|O_NOFOLLOW|O_CLOEXEC,0600);if(fd<0)throw Error("OUTPUT_CREATE");
  try{size_t at=0;while(at<bytes.size()){ssize_t n=write(fd,bytes.data()+at,bytes.size()-at);if(n<=0)throw Error("OUTPUT_WRITE");at+=size_t(n);}if(fsync(fd))throw Error("OUTPUT_FSYNC");struct stat s{};if(fstat(fd,&s)||!S_ISREG(s.st_mode)||s.st_uid!=geteuid()||s.st_nlink!=1||(s.st_mode&0777)!=0600)throw Error("OUTPUT_META");if(close(fd)){fd=-1;throw Error("OUTPUT_CLOSE");}fd=-1;if(renameat(root,temp.c_str(),root,final.c_str()))throw Error("OUTPUT_RENAME");if(fsync(root))throw Error("OUTPUT_DIR_FSYNC");}catch(...){if(fd>=0)close(fd);unlinkat(root,temp.c_str(),0);throw;}
}

const std::array<std::string,37> fixture_names{{
 "CURVE_U32","CURVE_POWER32","RBELOW128","FACTOR129","RNG_SEMANTIC","SOURCE_BRANCH","SOURCE_CHRONO320","SOURCE_AFFINE_STOP3","SOURCE_ROW_STOP2","DECODER_SUPPORT3","DECODER_SUPPORT64","DECODER_EMPTY","DECODER_S0","DECODER_S1","DENSE_GF2","EVENT130","PACKET_EVENT60373","RATE_GCD","RATE_SAT","RATE_DIV","RATE_TREE","RATE_RECON","RATE_TERMINAL","RATE_COMPARE","RATE_IO","RATE_NODE","RATE_TOUCH","RATE_LEAF","RATE_EXP","RATE_PARITY","RATE_GF2","RATE_EXACT_PRODUCT","RATE_MOD_PRODUCT","RATE_ISQRT","RATE_INVERSE","RATE_SIGNED","RATE_BASIS_RECORD"}};

const std::array<std::string,40> counter_names{{
 "CURVE_PROPOSALS","RANDOM_BELOW_CALLS","RANDOM_BELOW_ITERATIONS","RNG_DRAWS","ADMITTED_ROWS","AFFINE_ADDITIONS","AFFINE_SAFETY_GCDS","DISCRIMINANT_GCDS","ROW_ROOT_GCDS","ROW_RECORDS","PRODUCT_MULTIPLICATIONS","PEEL_EXACT_DIVISIONS","PEEL_BASE_REMAINDERS","PEEL_MODULAR_MULTIPLICATIONS","PEEL_GCDS","PEEL_RESIDUAL_DIVISIONS","PEEL_SQUARE_TESTS","F271_SCALAR_GCDS","F271_SATURATION_POWERS","F271_REFINEMENT_DIVISIONS","F271_RECURSION_NODES","F271_TOUCHES","F271_LEAF_ASSIGNMENTS","F271_TREE_NODE_UPDATES","F271_EXPONENT_COORD_UPDATES","F271_RECONSTRUCTION_INCIDENCES","F271_TERMINAL_BLOCKS","F271_REPLACEMENT_COMPARISONS","F271_FINAL_COMPARISONS","F271_BLOCK_COMPARISONS","F271_PARITY_CELLS","F271_GF2_WORD_OPERATIONS","SELECTED_EXACT_PRODUCTS","SELECTED_MODULAR_PRODUCTS","INTEGER_SQUARE_ROOTS","MODULAR_INVERSIONS","SIGNED_RELATION_GCDS","BASIS_RECORDS","FACTOR_EVENT_LINES","IO_BYTES"}};

struct Compact {
  std::string fixture,opcode;
  uint64_t group=0,item=0,cycles=0;
  std::array<std::string,16> arg{};
};

struct FixtureTables {
  std::map<std::string,std::vector<Compact>> compact;
  std::map<std::string,std::array<uint64_t,40>> counters;
  std::map<std::string,std::string> semantic_bytes;
  struct Digest {std::string operand,fnv,trace,semantic;};
  std::map<std::string,Digest> digests;
  uint64_t logical=0,result_records=0,result_bytes=0,payload_bytes=0;
  std::string theory;
};

size_t f_rank(const std::string& f){auto i=std::find(fixture_names.begin(),fixture_names.end(),f);if(i==fixture_names.end())throw Error("FIXTURE");return size_t(i-fixture_names.begin());}
size_t c_rank(const std::string& c){auto i=std::find(counter_names.begin(),counter_names.end(),c);if(i==counter_names.end())throw Error("COUNTER");return size_t(i-counter_names.begin());}

void parse_operands(const std::string& bytes,FixtureTables& t) {
  auto row=lines(bytes);if(row.empty())throw Error("OPERAND_EMPTY");auto head=fields(row[0]);if(head.size()!=22||head[0]!="version"||head[1]!="fixture"||head[5]!="opcode")throw Error("OPERAND_HEADER");
  std::tuple<size_t,uint64_t,uint64_t> prior{0,0,0};bool first=true;
  for(size_t n=1;n<row.size();++n){auto x=fields(row[n]);if(x.size()!=22||x[0]!=VERSION)throw Error("OPERAND_ROW");size_t rank=f_rank(x[1]);uint64_t group=udec(x[2]),item=udec(x[3]),cycles=udec(x[4]);if(!cycles)throw Error("CYCLES");auto key=std::make_tuple(rank,group,item);if(!first&&key<=prior)throw Error("OPERAND_ORDER");first=false;prior=key;Compact c;c.fixture=x[1];c.group=group;c.item=item;c.cycles=cycles;c.opcode=x[5];for(int i=0;i<16;++i)c.arg[i]=x[6+i];t.compact[c.fixture].push_back(std::move(c));}
}

void parse_counters(const std::string& bytes,FixtureTables& t) {
  auto row=lines(bytes);if(row.size()!=1+37*40||row[0]!="version\tfixture\tcounter\tvalue")throw Error("COUNTER_SHAPE");size_t n=1;
  for(const auto& f:fixture_names)for(size_t c=0;c<counter_names.size();++c,++n){auto x=fields(row[n]);if(x.size()!=4||x[0]!=VERSION||x[1]!=f||x[2]!=counter_names[c])throw Error("COUNTER_ORDER");t.counters[f][c]=udec(x[3]);}
}

void parse_semantics(const std::string& bytes,FixtureTables& t) {
  auto row=lines(bytes);if(row.empty()||fields(row[0]).size()!=12)throw Error("SEMANTIC_HEADER");std::map<std::string,uint64_t> ordinal;
  for(size_t i=1;i<row.size();++i){auto x=fields(row[i]);if(x.size()!=12||x[0]!=VERSION||f_rank(x[1])>=37||udec(x[2])!=ordinal[x[1]]++)throw Error("SEMANTIC_ROW");t.semantic_bytes[x[1]]+=row[i]+"\n";}
  for(const auto& f:fixture_names){auto r=lines(t.semantic_bytes.at(f));bool pass=false;for(const auto& line:r){auto x=fields(line);if(x[3]=="STATUS"&&x[4]=="FIXTURE"&&x[5]=="0"&&x[6]=="PASS")pass=true;}if(!pass)throw Error("FIXTURE_PASS");}
}

void parse_digests(const std::string& bytes,FixtureTables& t) {
  auto row=lines(bytes);if(row.empty()||row[0]!="version\tfixture\toperand_sha256\tresult_fnv1a64\tresult_sha256\tsemantic_sha256")throw Error("DIGEST_HEADER");
  size_t previous=0;bool first=true;for(size_t i=1;i<row.size();++i){auto x=fields(row[i]);if(x.size()!=6||x[0]!=VERSION)throw Error("DIGEST_ROW");size_t rank=f_rank(x[1]);if(!first&&rank<=previous)throw Error("DIGEST_ORDER");first=false;previous=rank;t.digests[x[1]]={x[2],x[3],x[4],x[5]};}
}

std::vector<const Compact*> expanded(const std::string& fixture,const FixtureTables& t) {
  auto found=t.compact.find(fixture);if(found==t.compact.end())return {};
  std::map<uint64_t,std::vector<const Compact*>> groups;for(const auto& r:found->second)groups[r.group].push_back(&r);
  std::vector<const Compact*> out;for(auto& [group,v]:groups){(void)group;std::sort(v.begin(),v.end(),[](auto a,auto b){return a->item<b->item;});for(size_t i=0;i<v.size();++i)if(v[i]->item!=i||v[i]->cycles!=v[0]->cycles)throw Error("GROUP_RULE");for(uint64_t c=0;c<v[0]->cycles;++c)out.insert(out.end(),v.begin(),v.end());}return out;
}

std::string operand_preimage(const std::string& fixture,const FixtureTables& t) {
  auto e=expanded(fixture,t);std::string out;
  for(size_t i=0;i<e.size();++i){out+=fixture+"\t"+std::to_string(i)+"\t"+e[i]->opcode;for(const auto& a:e[i]->arg)out+='\t'+a;out+='\n';}
  return out;
}

std::string theory_root() {
  static const char* row[] = {
   "D09_DRAFT_ALGEBRA.md\t93ee6021b969a3624cf499df5e18ea9c262e2a095a6b0634644cc1d69ee8030d\n",
   "D09_DRAFT_PREREGISTRATION.md\t3b499578678a0f71c75f52608e53f2fba7f390fb5a09a95bc20c61d09fe1c0a4\n",
   "D10_DRAFT_ALGEBRA.md\taab2397c601b645f71da0bc79a8f58ed9ef79ea984fa7f7458ab2a49582a17a7\n",
   "D10_DRAFT_PREREGISTRATION.md\tbe7e2a05a1eac6659000cdfe71469697d76b867b42cb60c1c244b06ec63afb6e\n",
   "D11_DRAFT_ALGEBRA.md\ta177438e425a20550342e7efa94ec1f70d30f40fe204640f983435dc36554f27\n",
   "D11_DRAFT_PREREGISTRATION.md\t9b477799e006a9b2bb49eebcf062917f1a3c91a9852ce8fbe825fcea1a1df23e\n",
   "D11_HOSTILE_THEORY_AUDIT.md\t777ccd163959a7ec4e14bdcd3c9d12fc1d58732207f12520806e1ad2a2705246\n",
   "D12_DRAFT_ALGEBRA.md\teae660da5a5c5344b83ccd99301cfb4f2db89d5c259cf73194f85892e2d7dcb0\n",
   "D12_DRAFT_PREREGISTRATION.md\t65682542478a2c2270f3657d2c741ea253445ad3cf160758449a0ce21e806ecd\n",
   "D13_DRAFT_ALGEBRA.md\t915ec124f6be79a1530af3df628f8c65eaa5bde845f073f67f5077e66258ea9c\n",
   "D13_DRAFT_PREREGISTRATION.md\t42667461ac3a21820f3ea1d5de545d17ff03c719a38cd405dbdb0e91ff083c17\n",
   "D14_DRAFT_ALGEBRA.md\t42690a13d5a0fade1dd644bf29d299d9bab3b5cdd6a68d08354f1e9a5c6fb4f6\n",
   "D14_DRAFT_PREREGISTRATION.md\t4b02e30cfe2986fbc04dbf8c4faf22743c18acb1a64d2a07b30eefe2c6338b9b\n",
   "D14_HOSTILE_THEORY_AUDIT.md\tb7067c104eaf96dfa81d7bd08dcc9326e7616016fb66202c078bf1c2ea5ef03e\n",
   "D15_DRAFT_ALGEBRA.md\t563293afda1cf4d183b4d70ec30da60d0339086a52d9395df8b4d70d1e7ceeb6\n",
   "D15_DRAFT_PREREGISTRATION.md\t9c3b7cc4d855e906d8c9f35bcf7846631d28d728138df07f0e812cf59c12798d\n",
   "D16_DRAFT_ALGEBRA.md\t10d0e74462aac944a32dbc68404aa30c730d1f5b919f1fb4dd9e5a76ae92f5b2\n",
   "D16_DRAFT_PREREGISTRATION.md\t8a27d1d3af5b6f46d5f90e2f3545928cde55932c8012c6829b7c67207bd556a2\n",
   "D17_DRAFT_ALGEBRA.md\te784dfb9d151e816ef43644e480e705c7414d4af34114250da7d399c319d46d3\n",
   "D17_DRAFT_PREREGISTRATION.md\tacd92da342f2f88667a6b3cbfc3be1c13e9f8fdeabf4789020f3472319ed62d3\n",
   "D17_HOSTILE_THEORY_AUDIT.md\tfc068523f2d45f1a853aac1db860fc64ccb66f6ffbf8f8f8b372a2ed3937f638\n",
   "D18_DRAFT_ALGEBRA.md\t6a163bb4a642760f41a5d0fab0b5bbea40e936eef2dff93921b65fe7c7ce815d\n",
   "D18_DRAFT_PREREGISTRATION.md\t944b0ffce0036f2970cb56e097735622b1aaf97f186a40673d812d244f3709f6\n"};
  std::string preimage;for(const char* x:row)preimage+=x;return hash256(preimage);
}

std::string affine_status(const Compact& o,Big* x3,Big* y3,Big* factor) {
  Big N=integer_hex(o.arg[0]),A=integer_hex(o.arg[1]);(void)integer_hex(o.arg[2]);
  Big x1=integer_hex(o.arg[3]),y1=integer_hex(o.arg[4]),x2=integer_hex(o.arg[5]),y2=integer_hex(o.arg[6]);
  *factor=1;if(x1==x2&&modulo(y1+y2,N)==0)return "GLOBAL_INFINITY";
  if(x1==x2&&y1!=y2){Big d=common(y1-y2,N);if(d>1&&d<N){*factor=d;return "FACTOR_X_SIGN_MINUS";}d=common(y1+y2,N);if(d>1&&d<N){*factor=d;return "FACTOR_X_SIGN_PLUS";}return "UNRESOLVED_EQUAL_X";}
  Big num,den;if(x1==x2&&y1==y2){num=3*x1*x1+A;den=2*y1;}else{num=y2-y1;den=x2-x1;}
  den=modulo(den,N);Big d=common(den,N);if(d>1&&d<N){*factor=d;return "FACTOR_DENOMINATOR";}if(d==N)return "UNRESOLVED_DENOMINATOR";
  Big old=N,r=den,s0=0,s1=1;while(r){Big q=old/r;Big z=old-q*r;old=r;r=z;z=s0-q*s1;s0=s1;s1=z;}Big slope=modulo(num*s0,N);*x3=modulo(slope*slope-x1-x2,N);*y3=modulo(slope*(x1-*x3)-y1,N);return "OK";
}

std::string reconstruct_trace(const std::string& fixture,const FixtureTables& t,
                              const Big& A64,const Big& R64) {
  auto op=expanded(fixture,t);std::string result;
  if(fixture=="SOURCE_AFFINE_STOP3"){
    for(size_t i=0;i<op.size();++i){Big x=0,y=0,g=1;std::string s=affine_status(*op[i],&x,&y,&g);result+=fixture+"\tAFFINE\t"+std::to_string(i)+"\t"+s+"\t-\t-\t"+(g==1?"1":xhex(g))+"\n";}
  } else if(fixture=="SOURCE_ROW_STOP2"){
    for(size_t i=0;i<op.size();++i){Big N=integer_hex(op[i]->arg[0]),v=integer_hex(op[i]->arg[1]),g=common(v,N);std::string s=g==1?"UNIT":(g==N?"FULL_ROW_ROOT":"FACTOR_ROW_ROOT");result+=fixture+"\tROW\t"+std::to_string(i)+"\t"+s+"\t"+xhex(g)+"\n";}
  } else if(fixture=="RATE_NODE"||fixture=="RATE_TOUCH"){
    for(const auto* x:op)result+=fixture+"\t"+x->arg[0]+"\t1\t1\n";
  } else if(fixture=="RATE_LEAF"){
    for(size_t i=0;i<op.size();++i)result+=fixture+"\t"+xhex(i)+"\t"+op[i]->arg[0]+"\t"+op[i]->arg[1]+"\n";
  } else if(fixture=="RATE_EXP"){
    for(size_t i=0;i<op.size();++i){uint64_t z=udec(std::to_string(integer_hex(op[i]->arg[0]).convert_to<uint64_t>()*integer_hex(op[i]->arg[1]).convert_to<uint64_t>()+integer_hex(op[i]->arg[2]).convert_to<uint64_t>()*integer_hex(op[i]->arg[3]).convert_to<uint64_t>()));result+=fixture+"\t"+xhex(i)+"\t"+xhex(z)+"\n";}
  } else if(fixture=="RATE_PARITY"){
    for(size_t i=0;i<4096;++i)result+=fixture+"\t"+xhex(i)+"\t6666666666666666\n";
  } else if(fixture=="RATE_GF2")result="RATE_GF2\t232205\t3f\tffffffffffffffff\t123456789abcdef\n";
  else if(fixture=="RATE_EXACT_PRODUCT")for(size_t i=0;i<1024;++i)result+=fixture+"\t"+xhex(i)+"\t"+xhex(A64)+"\n";
  else if(fixture=="RATE_MOD_PRODUCT")for(size_t i=0;i<4096;++i)result+=fixture+"\t"+xhex(i)+"\t4\n";
  else if(fixture=="RATE_ISQRT")for(size_t i=0;i<256;++i)result+=fixture+"\t"+xhex(i)+"\t"+xhex(R64)+"\n";
  else if(fixture=="RATE_INVERSE")for(size_t i=0;i<262144;++i)result+=fixture+"\t"+xhex(i)+"\t4\n";
  else if(fixture=="RATE_SIGNED")for(size_t i=0;i<131072;++i)result+=fixture+"\t"+xhex(i)+"\t3\t5\n";
  else if(fixture=="RATE_BASIS_RECORD"){
    const std::string line="F265-D18\tfixture\t60\trandom\t0\tQ\t0\tffffffffffffffff\t0000000000000000\t0000000000000000\t0000000000000000\t0000000000000000\t1\t4\t4\t3\t5\tSTRUCTURAL_Q_NON_GLOBAL\n";
    for(size_t i=0;i<65536;++i)result+=line;
  }
  // SOURCE_CHRONO320 is independently reconstructed directly from its
  // registered formulas, not by invoking any public production body.
  else if(fixture=="SOURCE_CHRONO320"){
    Big N=(Big(1)<<107)-1;
    for(uint64_t curve=0;curve<2;++curve){
      for(uint64_t slot=0;slot<32;++slot){bool accept=slot==31;Big A,B,x,y,d;if(curve==0){A=accept?1:N-3;x=accept?N-1:1;y=accept?N-1:0;B=accept?3:2;}else{Big s=accept?1:N-1;x=s*s%N;y=s*s%N*s%N;A=(s+1)%N;B=modulo(y*y-x*x*x-A*x,N);}d=common(4*A*A*A+27*B*B,N);result+=fixture+"\tPROPOSAL\t"+xhex(curve)+"\t"+xhex(slot)+"\t"+(accept?"ACCEPT":"REJECT_FULL_DISCRIMINANT")+"\t"+xhex(A)+"\t"+xhex(B)+"\t"+xhex(x)+"\t"+xhex(y)+"\t"+xhex(d)+"\n";}
      for(uint64_t scalar=1;scalar<=160;++scalar){Big u,v,A,B;if(curve==0){A=1;B=3;u=scalar==1?N-1:6;v=scalar==1?N-1:15;}else{A=2;B=N-2;if(scalar==1){u=1;v=1;}else{Big slope=5*((N+1)/2)%N;u=modulo(slope*slope-2,N);v=modulo(slope*(1-u)-1,N);}}if(scalar!=1)result+=fixture+"\tAFFINE\t"+xhex(curve)+"\t"+xhex(scalar-1)+"\tOK\t"+xhex(u)+"\t"+xhex(v)+"\t1\n";result+=fixture+"\tROW\t"+xhex(curve)+"\t"+xhex(scalar)+"\tUNIT\t1\n";Big a=u*u*u+A*u+B,carry=(a-v*v)/N;result+=fixture+"\tRENDER\t"+xhex(curve*160+scalar-1)+"\t"+xhex(u)+"\t"+xhex(v)+"\t"+xhex(a)+"\t"+(carry<0?"-"+xhex(-carry):xhex(carry))+"\n";}
    }
    std::vector<Big> peel;Big product=1;for(uint64_t i=0;i<320;++i){Big w=(Big(1)<<180)+2*i+1;peel.push_back(w*w);product*=peel.back();}
    for(uint64_t i=0;i<320;++i){Big a=peel[i],g=common(a,modpow((product/a)%a,width(a),a)),b=a/g,r=square_root(b);bool square=r*r==b;result+=fixture+"\tPEEL\t"+xhex(i)+"\t"+xhex(g)+"\t"+xhex(b)+"\t"+(square?"1":"0")+"\t"+(square?"1":"0")+"\n";}
  }
  return result;
}

void verify_support64(const FixtureTables& t,Big& A64,Big& R64) {
  auto op=expanded("DECODER_SUPPORT64",t);std::array<uint64_t,128> primes{};std::array<unsigned,64> e{};std::array<Big,64> rows{};std::array<bool,128> gotp{};std::array<bool,64> gote{},gotr{};
  for(const Compact* x:op){if(x->opcode=="SUPPORT64_PRIME"){size_t family=integer_hex(x->arg[0]).convert_to<size_t>(),i=integer_hex(x->arg[1]).convert_to<size_t>();uint64_t q=integer_hex(x->arg[2]).convert_to<uint64_t>();if(family>1||i>=64||gotp[family*64+i])throw Error("SUPPORT_PRIME_INDEX");gotp[family*64+i]=true;primes[family*64+i]=q;}else if(x->opcode=="SUPPORT64_EXPONENT"){size_t i=integer_hex(x->arg[0]).convert_to<size_t>();if(i>=64||gote[i])throw Error("SUPPORT_EXP_INDEX");gote[i]=true;e[i]=integer_hex(x->arg[1]).convert_to<unsigned>();}else if(x->opcode=="DECODER_ROW"){size_t i=integer_hex(x->arg[0]).convert_to<size_t>();if(i>=64||gotr[i])throw Error("SUPPORT_ROW_INDEX");gotr[i]=true;rows[i]=integer_hex(x->arg[2]);if(integer_hex(x->arg[3])!=(i?1:4))throw Error("SUPPORT_ROOT");}}
  uint64_t last=0,count=0;for(uint64_t n=2;count<128;++n)if(n%15==1&&is_prime(n)){if(primes[count]!=n)throw Error("SUPPORT_PRIME_COMPLETE");last=n;++count;}if(!last)throw Error("SUPPORT_PRIMES");
  A64=1;R64=1;for(size_t i=0;i<64;++i){Big base=Big(primes[i])*primes[(i+1)%64],r=primes[64+i],expected=base*ipow(r,2*e[i]);if(rows[i]!=expected||width(expected)>361||width(expected*r*r)<=361)throw Error("SUPPORT_MAXIMAL");A64*=rows[i];R64*=Big(primes[i])*ipow(r,e[i]);if(rows[i]%15!=1)throw Error("SUPPORT_CONGRUENCE");}if(A64!=R64*R64||R64%15!=1)throw Error("SUPPORT_SQUARE");
}

void verify_dense(const FixtureTables& t) {
  auto op=expanded("DENSE_GF2",t);if(op.size()!=1875)throw Error("DENSE_COUNT");std::array<uint64_t,64> pivot{};std::array<bool,64> has{};unsigned rank=0;
  uint64_t words=0;for(const Compact* x:op){uint64_t v=integer_hex(x->arg[1]).convert_to<uint64_t>();for(unsigned b=0;b<64;++b){++words;if((v>>b)&1U){if(has[b]){v^=pivot[b];++words;}else{has[b]=true;pivot[b]=v;++words;++rank;break;}}}}
  if(rank!=63)throw Error("DENSE_RANK");uint64_t kernel=UINT64_MAX;for(const Compact* x:op){uint64_t row=integer_hex(x->arg[1]).convert_to<uint64_t>();if((__builtin_popcountll(row&kernel)&1)!=0)throw Error("DENSE_KERNEL");}++words;++words;if(words!=232205)throw Error("DENSE_UNPADDED_WORDS");
}

using AuditMask=std::array<uint64_t,5>;
struct AuditPart{Big base;uint16_t old_power=0,new_power=0;};
struct AuditBlock{Big base=1;std::vector<uint16_t> power;bool square=false;};

bool audit_bit(const AuditMask& x,size_t i){return ((x[i/64]>>(i%64))&1U)!=0;}
void audit_toggle(AuditMask& x,size_t i){x[i/64]^=UINT64_C(1)<<(i%64);}
void audit_xor(AuditMask& a,const AuditMask& b){for(size_t i=0;i<5;++i)a[i]^=b[i];}
bool audit_empty(const AuditMask& x){for(uint64_t w:x)if(w)return false;return true;}

Big audit_inverse(Big a,const Big& n){Big r0=n,r1=modulo(a,n),t0=0,t1=1;while(r1!=0){Big q=r0/r1,nr=r0-q*r1,nt=t0-q*t1;r0=r1;r1=nr;t0=t1;t1=nt;}if(r0!=1)throw Error("AUDIT_INVERSE");return modulo(t0,n);}

class DecoderCounterAudit {
 public:
  DecoderCounterAudit(std::array<uint64_t,40>& count,const Big& modulus,
                      std::vector<Big> rows,std::vector<Big> roots)
      : count_(count),modulus_(modulus),rows_(std::move(rows)),roots_(std::move(roots)),m_(rows_.size()) {
    if(m_!=roots_.size()||m_>64)throw Error("AUDIT_DECODER_WIDTH");products_.fill(1);
  }
  void verify(){for(size_t i=0;i<m_;++i)insert(i,rows_[i]);auto blocks=finish();std::vector<AuditMask> equation;for(const auto& b:blocks)if(!b.square){AuditMask x{};for(size_t i=0;i<m_;++i){inc("F271_PARITY_CELLS");if(b.power[i]&1U)audit_toggle(x,i);}if(!audit_empty(x))equation.push_back(x);}std::map<std::vector<uint64_t>,std::vector<size_t>> groups;size_t words=(equation.size()+63)/64;for(size_t i=0;i<m_;++i){std::vector<uint64_t> s(words);for(size_t j=0;j<equation.size();++j)if(audit_bit(equation[j],i))s[j/64]|=UINT64_C(1)<<(j%64);groups[s].push_back(i);}std::vector<AuditMask> low;for(const auto& group:groups){bool zero=true;for(uint64_t w:group.first)zero=zero&&w==0;if(zero){for(size_t i:group.second){AuditMask x{};audit_toggle(x,i);low.push_back(x);}}else if(group.second.size()>1)for(size_t j=1;j<group.second.size();++j){AuditMask x{};audit_toggle(x,group.second[0]);audit_toggle(x,group.second[j]);low.push_back(x);}}low=canonical(std::move(low));auto full=kernel(equation);std::vector<AuditMask> high;for(auto x:full){for(const auto& y:low)eliminate(x,y);for(const auto& y:high)eliminate(x,y);if(!audit_empty(x))high.push_back(x);}high=canonical(std::move(high));classify(low);classify(high);}
 private:
  std::array<uint64_t,40>& count_;Big modulus_;std::vector<Big> rows_,roots_;size_t m_;std::array<AuditBlock,2048> leaf_{};std::array<Big,4096> products_{};
  void inc(const std::string& name,uint64_t n=1){size_t i=c_rank(name);if(UINT64_MAX-count_[i]<n)throw Error("AUDIT_COUNTER_OVERFLOW");count_[i]+=n;}
  Big saturated(const Big& a,const Big& b){inc("F271_SATURATION_POWERS");inc("F271_SCALAR_GCDS");return common(a,modpow(b,width(a),a));}
  std::vector<AuditPart> refine(const Big& a,const Big& b,const Big* known){inc("F271_RECURSION_NODES");Big d;if(known)d=*known;else{inc("F271_SCALAR_GCDS");d=common(a,b);}if(d<=1)throw Error("AUDIT_SUPPORT");inc("F271_REFINEMENT_DIVISIONS",3);Big x=a/d,y=b/d,A=1,B=1;if(x>1)A=saturated(d,x);if(y>1)B=saturated(d,y);Big C=d/(A*B);std::vector<AuditPart> out;if(A>1){auto child=refine(x,A,nullptr);for(auto z:child)out.push_back({z.base,uint16_t(z.old_power+z.new_power),z.new_power});}if(B>1){auto child=refine(y,B,nullptr);for(auto z:child)out.push_back({z.base,z.new_power,uint16_t(z.old_power+z.new_power)});}if(C>1)out.push_back({C,1,1});return out;}
  std::vector<AuditPart> overlap(const Big& a,const Big& b,const Big& d){inc("F271_TOUCHES");Big x=saturated(a,b),y=saturated(b,a);inc("F271_REFINEMENT_DIVISIONS",2);auto out=refine(x,y,&d);if(a/x>1)out.push_back({a/x,1,0});if(b/y>1)out.push_back({b/y,0,1});return out;}
  size_t free_leaf()const{for(size_t i=0;i<leaf_.size();++i)if(leaf_[i].base==1)return i;throw Error("AUDIT_LEAF_CAP");}
  void replace(size_t slot,AuditBlock b){inc("F271_LEAF_ASSIGNMENTS");leaf_[slot]=std::move(b);size_t node=2048+slot;products_[node]=leaf_[slot].base;while(node>1){node>>=1;products_[node]=products_[2*node]*products_[2*node+1];inc("F271_TREE_NODE_UPDATES");}}
  void merge(std::vector<AuditPart>& a,bool final){if(a.size()<2)return;std::vector<AuditPart> work(a.size());for(size_t width_=1;width_<a.size();width_*=2)for(size_t begin=0;begin<a.size();begin+=2*width_){size_t middle=std::min(begin+width_,a.size()),end=std::min(begin+2*width_,a.size()),i=begin,j=middle,k=begin;while(i<middle&&j<end){inc(final?"F271_FINAL_COMPARISONS":"F271_REPLACEMENT_COMPARISONS");inc("F271_BLOCK_COMPARISONS");work[k++]=a[j].base<a[i].base?a[j++]:a[i++];}while(i<middle)work[k++]=a[i++];while(j<end)work[k++]=a[j++];for(k=begin;k<end;++k)a[k]=work[k];}}
  void insert(size_t row,const Big& input){Big pending=input;while(pending>1){inc("F271_SCALAR_GCDS");Big d=common(pending,products_[1]);if(d==1){std::vector<uint16_t> e(m_);e[row]=1;replace(free_leaf(),{pending,std::move(e),false});return;}size_t node=1;Big carried=d;for(unsigned level=0;level<11;++level){inc("F271_SCALAR_GCDS");Big left=common(pending,products_[2*node]);if(left>1){node*=2;carried=left;}else node=2*node+1;}size_t slot=node-2048;if(leaf_[slot].base<=1)throw Error("AUDIT_DESCENT");AuditBlock old=leaf_[slot];auto parts=overlap(old.base,pending,carried);std::vector<AuditPart> keep;Big residual=1;for(const auto& z:parts)if(z.old_power)keep.push_back(z);else residual*=ipow(z.base,z.new_power);merge(keep,false);if(keep.empty())throw Error("AUDIT_REPLACEMENT");bool first=true;for(const auto& z:keep){std::vector<uint16_t> e(m_);for(size_t i=0;i<m_;++i){uint32_t value=uint32_t(z.old_power)*old.power[i]+(i==row?z.new_power:0);inc("F271_EXPONENT_COORD_UPDATES");if(value>360)throw Error("AUDIT_EXPONENT");e[i]=uint16_t(value);}size_t target=first?slot:free_leaf();first=false;replace(target,{z.base,std::move(e),false});}pending=residual;}}
  std::vector<AuditBlock> finish(){std::vector<AuditPart> order;for(size_t i=0;i<leaf_.size();++i)if(leaf_[i].base>1)order.push_back({leaf_[i].base,uint16_t(i),0});merge(order,true);std::vector<AuditBlock> out;for(const auto& x:order)out.push_back(leaf_[x.old_power]);for(size_t row=0;row<m_;++row){Big rebuilt=1;for(const auto& b:out)if(b.power[row]){inc("F271_RECONSTRUCTION_INCIDENCES");rebuilt*=ipow(b.base,b.power[row]);}if(rebuilt!=rows_[row])throw Error("AUDIT_REBUILD");}Big product=1;for(const auto& b:out)product*=b.base;for(auto& b:out){inc("F271_TERMINAL_BLOCKS");inc("F271_SCALAR_GCDS");if(common(b.base,product/b.base)!=1)throw Error("AUDIT_TERMINAL");Big r=square_root(b.base);b.square=r*r==b.base;}return out;}
  void eliminate(AuditMask& x,const AuditMask& basis)const{size_t pivot=0;while(pivot<m_&&!audit_bit(basis,pivot))++pivot;if(pivot<m_&&audit_bit(x,pivot))audit_xor(x,basis);}
  std::vector<AuditMask> canonical(std::vector<AuditMask> input){std::array<int,320> where;where.fill(-1);std::vector<AuditMask> out;uint64_t words=(m_+63)/64;for(auto x:input){for(size_t c=0;c<m_;++c){inc("F271_GF2_WORD_OPERATIONS");if(audit_bit(x,c)&&where[c]>=0){audit_xor(x,out[size_t(where[c])]);inc("F271_GF2_WORD_OPERATIONS",words);}}if(audit_empty(x))continue;size_t pivot=0;while(pivot<m_&&!audit_bit(x,pivot))++pivot;for(auto& prior:out)if(audit_bit(prior,pivot)){audit_xor(prior,x);inc("F271_GF2_WORD_OPERATIONS",words);}where[pivot]=int(out.size());out.push_back(x);}std::sort(out.begin(),out.end(),[&](const auto& a,const auto& b){size_t x=0,y=0;while(x<m_&&!audit_bit(a,x))++x;while(y<m_&&!audit_bit(b,y))++y;return x<y;});return out;}
  std::vector<AuditMask> kernel(const std::vector<AuditMask>& equation){std::array<AuditMask,320> pivot{};std::array<bool,320> used{};uint64_t words=(m_+63)/64;for(auto x:equation)for(size_t c=0;c<m_;++c){inc("F271_GF2_WORD_OPERATIONS");if(!audit_bit(x,c))continue;if(used[c]){audit_xor(x,pivot[c]);inc("F271_GF2_WORD_OPERATIONS",words);}else{used[c]=true;pivot[c]=x;inc("F271_GF2_WORD_OPERATIONS",words);break;}}for(size_t c=m_;c-->0;)if(used[c])for(size_t d=0;d<c;++d)if(used[d]&&audit_bit(pivot[d],c)){audit_xor(pivot[d],pivot[c]);inc("F271_GF2_WORD_OPERATIONS",words);}std::vector<AuditMask> out;for(size_t free=0;free<m_;++free)if(!used[free]){AuditMask x{};audit_toggle(x,free);for(size_t c=0;c<m_;++c)if(used[c]&&audit_bit(pivot[c],free))audit_toggle(x,c);out.push_back(x);}return out;}
  void classify(const std::vector<AuditMask>& basis){for(const auto& mask:basis){Big exact=1,x=1;for(size_t i=0;i<m_;++i)if(audit_bit(mask,i)){inc("SELECTED_EXACT_PRODUCTS");inc("SELECTED_MODULAR_PRODUCTS");exact*=rows_[i];x=x*roots_[i]%modulus_;}inc("INTEGER_SQUARE_ROOTS");Big R=square_root(exact);if(R*R!=exact)throw Error("AUDIT_BASIS_SQUARE");inc("MODULAR_INVERSIONS");Big rho=R%modulus_*audit_inverse(x,modulus_)%modulus_;if(rho*rho%modulus_!=1)throw Error("AUDIT_ROOT");inc("SIGNED_RELATION_GCDS",2);Big gm=common(rho-1,modulus_),gp=common(rho+1,modulus_);if(rho!=1&&rho!=modulus_-1){if(!((gm>1&&gm<modulus_)||(gp>1&&gp<modulus_)))throw Error("AUDIT_FACTOR");inc("FACTOR_EVENT_LINES");}inc("BASIS_RECORDS");}}
};

void verify_decoder_counters(const std::string& fixture,const FixtureTables& t){std::array<uint64_t,40> expected{};if(fixture=="DECODER_EMPTY"){expected[c_rank("PRODUCT_MULTIPLICATIONS")]=1;for(const char* name:{"PEEL_EXACT_DIVISIONS","PEEL_BASE_REMAINDERS","PEEL_GCDS","PEEL_RESIDUAL_DIVISIONS","PEEL_SQUARE_TESTS"})expected[c_rank(name)]=2;expected[c_rank("PEEL_MODULAR_MULTIPLICATIONS")]=10;}else{std::vector<Big> row,root;Big N=0;for(const Compact* x:expanded(fixture,t))if(x->opcode=="DECODER_ROW"){Big n=integer_hex(x->arg[1]);if(N!=0&&N!=n)throw Error("AUDIT_DECODER_MODULUS");N=n;row.push_back(integer_hex(x->arg[2]));root.push_back(integer_hex(x->arg[3]));}if(row.empty())throw Error("AUDIT_DECODER_ROWS");DecoderCounterAudit(expected,N,std::move(row),std::move(root)).verify();}if(expected!=t.counters.at(fixture))throw Error("DECODER_COUNTER_TUPLE_"+fixture);}

void verify_packet(FixtureTables& t) {
  uint64_t logical=0;for(const auto& f:fixture_names){std::string op=operand_preimage(f,t);logical+=expanded(f,t).size();if(auto d=t.digests.find(f);d!=t.digests.end()&&hash256(op)!=d->second.operand)throw Error("OPERAND_DIGEST");if(hash256(t.semantic_bytes.at(f))!=(d==t.digests.end()?hash256(t.semantic_bytes.at(f)):d->second.semantic))throw Error("SEMANTIC_DIGEST");}
  if(logical!=t.logical||logical>8388608)throw Error("LOGICAL_TOTAL");
  Big A64,R64;verify_support64(t,A64,R64);verify_dense(t);
  for(const char* fixture:{"DECODER_SUPPORT3","DECODER_SUPPORT64","DECODER_EMPTY","DECODER_S0","DECODER_S1"})verify_decoder_counters(fixture,t);
  Big N=(Big(1)<<107)-1,s=4;for(int i=0;i<105;++i)s=modulo(s*s-2,N);if(s!=0)throw Error("LUCAS_LEHMER");
  auto io=expanded("RATE_IO",t);if(io.size()!=1||io[0]->opcode!="IO_BYTES"||integer_hex(io[0]->arg[0])!=67108864||integer_hex(io[0]->arg[1])>255)throw Error("RATE_IO_OPERAND");std::string io_chunk(1<<20,char(integer_hex(io[0]->arg[1]).convert_to<unsigned>()));std::string io_bytes;io_bytes.reserve(67108864);for(int i=0;i<64;++i)io_bytes+=io_chunk;std::string io_hash=hash256(io_bytes);bool io_sem=false;for(const auto& l:lines(t.semantic_bytes.at("RATE_IO"))){auto x=fields(l);if(x[3]=="AGGREGATE"&&x[4]=="STREAM_SHA256"&&x[5]==io_hash)io_sem=true;}if(!io_sem)throw Error("RATE_IO_SHA");
  for(const auto& [name,d]:t.digests){std::string result=reconstruct_trace(name,t,A64,R64);if(hash256(result)!=d.trace||fnv_hex(result)!=d.fnv)throw Error("TRACE_DIGEST_"+name);t.result_records+=std::count(result.begin(),result.end(),'\n');t.result_bytes+=result.size();}
  if(t.result_records>4194304||t.result_bytes>134217728)throw Error("RESULT_CAP");
  // Reconstruct each complete 40-counter tuple.  Unlisted counters remain
  // zero; decoder tuples were reconstructed independently above.
  auto fixed=[&](const std::string& fixture,std::initializer_list<std::pair<const char*,uint64_t>> nonzero){std::array<uint64_t,40> expected{};for(const auto& x:nonzero)expected[c_rank(x.first)]=x.second;if(expected!=t.counters.at(fixture))throw Error("COUNTER_TUPLE_"+fixture);};
  fixed("CURVE_U32",{{"CURVE_PROPOSALS",32},{"DISCRIMINANT_GCDS",32}});
  fixed("CURVE_POWER32",{{"CURVE_PROPOSALS",32},{"DISCRIMINANT_GCDS",32}});
  fixed("RBELOW128",{{"RANDOM_BELOW_CALLS",2},{"RANDOM_BELOW_ITERATIONS",256},{"RNG_DRAWS",256}});
  fixed("FACTOR129",{{"FACTOR_EVENT_LINES",129}});
  fixed("RNG_SEMANTIC",{{"RANDOM_BELOW_CALLS",3},{"RANDOM_BELOW_ITERATIONS",131},{"RNG_DRAWS",132}});
  fixed("SOURCE_BRANCH",{{"AFFINE_ADDITIONS",4},{"AFFINE_SAFETY_GCDS",3},{"ROW_ROOT_GCDS",3},{"FACTOR_EVENT_LINES",3}});
  fixed("SOURCE_CHRONO320",{{"CURVE_PROPOSALS",64},{"RANDOM_BELOW_CALLS",128},{"RANDOM_BELOW_ITERATIONS",128},{"RNG_DRAWS",256},{"ADMITTED_ROWS",320},{"AFFINE_ADDITIONS",318},{"AFFINE_SAFETY_GCDS",318},{"DISCRIMINANT_GCDS",64},{"ROW_ROOT_GCDS",320},{"ROW_RECORDS",320},{"PRODUCT_MULTIPLICATIONS",319},{"PEEL_EXACT_DIVISIONS",320},{"PEEL_BASE_REMAINDERS",320},{"PEEL_MODULAR_MULTIPLICATIONS",4480},{"PEEL_GCDS",320},{"PEEL_RESIDUAL_DIVISIONS",320},{"PEEL_SQUARE_TESTS",320}});
  fixed("SOURCE_AFFINE_STOP3",{{"AFFINE_ADDITIONS",3},{"AFFINE_SAFETY_GCDS",2},{"FACTOR_EVENT_LINES",2}});
  fixed("SOURCE_ROW_STOP2",{{"ROW_ROOT_GCDS",2}});
  fixed("DENSE_GF2",{{"F271_GF2_WORD_OPERATIONS",524288}});
  fixed("EVENT130",{{"FACTOR_EVENT_LINES",129}});
  fixed("PACKET_EVENT60373",{{"FACTOR_EVENT_LINES",60372}});
  fixed("RATE_GCD",{{"F271_SCALAR_GCDS",262144}});
  fixed("RATE_SAT",{{"F271_SCALAR_GCDS",262144},{"F271_SATURATION_POWERS",262144}});
  fixed("RATE_DIV",{{"F271_REFINEMENT_DIVISIONS",262144}});
  fixed("RATE_TREE",{{"F271_LEAF_ASSIGNMENTS",65536},{"F271_TREE_NODE_UPDATES",720896}});
  fixed("RATE_RECON",{{"F271_RECONSTRUCTION_INCIDENCES",262144}});
  fixed("RATE_TERMINAL",{{"F271_SCALAR_GCDS",1875},{"F271_TERMINAL_BLOCKS",1875}});
  fixed("RATE_COMPARE",{{"F271_BLOCK_COMPARISONS",262144}});
  fixed("RATE_IO",{{"IO_BYTES",67108864}});
  fixed("RATE_NODE",{{"F271_REFINEMENT_DIVISIONS",196608},{"F271_RECURSION_NODES",65536}});
  fixed("RATE_TOUCH",{{"F271_SCALAR_GCDS",131072},{"F271_SATURATION_POWERS",131072},{"F271_REFINEMENT_DIVISIONS",327680},{"F271_RECURSION_NODES",65536},{"F271_TOUCHES",65536}});
  fixed("RATE_LEAF",{{"F271_LEAF_ASSIGNMENTS",262144}});
  fixed("RATE_EXP",{{"F271_EXPONENT_COORD_UPDATES",262144}});
  fixed("RATE_PARITY",{{"F271_PARITY_CELLS",262144}});
  fixed("RATE_GF2",{{"F271_GF2_WORD_OPERATIONS",524288}});
  fixed("RATE_EXACT_PRODUCT",{{"SELECTED_EXACT_PRODUCTS",65536}});
  fixed("RATE_MOD_PRODUCT",{{"SELECTED_MODULAR_PRODUCTS",262144}});
  fixed("RATE_ISQRT",{{"INTEGER_SQUARE_ROOTS",256}});
  fixed("RATE_INVERSE",{{"MODULAR_INVERSIONS",262144}});
  fixed("RATE_SIGNED",{{"SIGNED_RELATION_GCDS",262144}});
  fixed("RATE_BASIS_RECORD",{{"BASIS_RECORDS",65536}});
}

int program(int argc,char**argv) {
  if(!std::setlocale(LC_ALL,"C"))throw Error("LOCALE");umask(077);
  if(argc!=7)throw Error("CLI_COUNT");std::map<std::string,std::string> option;
  for(int i=1;i<argc;i+=2){std::string k=argv[i];if(k!="--mode"&&k!="--fixture-root"&&k!="--output-root")throw Error("CLI_OPTION");if(!option.emplace(k,argv[i+1]).second)throw Error("CLI_REPEAT");}
  if(option["--mode"]!="verify"||!abs_grammar(option["--fixture-root"])||!abs_grammar(option["--output-root"]))throw Error("CLI_VALUE");
  RootHandle input=directory(option["--fixture-root"],false),output=directory(option["--output-root"],true);if(below(input.descriptor,output.device,output.inode)||below(output.descriptor,input.device,input.inode))throw Error("ROOT_ALIAS");if(!listing(output.descriptor).empty())throw Error("OUTPUT_NOT_EMPTY");
  const std::vector<std::string> expected{"F265-D18.PAYLOAD.sha256","F265-D18.decoder_operands.tsv","F265-D18.expected_counters.tsv","F265-D18.expected_digests.tsv","F265-D18.expected_semantics.tsv","F265-D18.materializer_attestation.tsv","F265-D18.rate_operands.tsv","F265-D18.source_operands.tsv"};if(listing(input.descriptor)!=expected)throw Error("INPUT_MEMBERSHIP");
  const std::array<std::string,7> order{{"F265-D18.source_operands.tsv","F265-D18.decoder_operands.tsv","F265-D18.rate_operands.tsv","F265-D18.expected_counters.tsv","F265-D18.expected_semantics.tsv","F265-D18.expected_digests.tsv","F265-D18.materializer_attestation.tsv"}};
  const std::array<size_t,7> caps{{1048576,4194304,4194304,1048576,1048576,1048576,65536}};std::map<std::string,std::string> file;
  for(size_t i=0;i<order.size();++i)file[order[i]]=read_member(input.descriptor,order[i],caps[i]);std::string manifest=read_member(input.descriptor,"F265-D18.PAYLOAD.sha256",65536),expected_manifest;for(const auto& n:order)expected_manifest+=hash256(file[n])+"  "+n+"\n";if(manifest!=expected_manifest)throw Error("PAYLOAD_MANIFEST");
  FixtureTables table;parse_operands(file[order[0]],table);parse_operands(file[order[1]],table);parse_operands(file[order[2]],table);parse_counters(file[order[3]],table);parse_semantics(file[order[4]],table);parse_digests(file[order[5]],table);
  auto att=lines(file[order[6]]);if(att.size()!=2||fields(att[0]).size()!=7)throw Error("ATTESTATION");auto a=fields(att[1]);if(a.size()!=7||a[0]!=VERSION||a[1]!=theory_root()||a[6]!="PASS")throw Error("ATTESTATION_VALUES");table.theory=a[1];table.logical=udec(a[2]);uint64_t claimed_records=udec(a[3]),claimed_result_bytes=udec(a[4]);table.payload_bytes=udec(a[5]);uint64_t actual_payload=0;for(size_t i=0;i<6;++i)actual_payload+=file[order[i]].size();if(actual_payload!=table.payload_bytes)throw Error("PAYLOAD_BYTES");
  verify_packet(table);if(table.result_records!=claimed_records||table.result_bytes!=claimed_result_bytes)throw Error("RESULT_TOTALS");
  if(listing(input.descriptor)!=expected)throw Error("INPUT_CHANGED");
  std::string root_hash=hash256(manifest);std::string result="version\tpayload_root\ttheory_root\tfiles\tlogical_operands\tresult_records\tresult_bytes\tstatus\n"+std::string(VERSION)+"\t"+root_hash+"\t"+table.theory+"\t7\t"+std::to_string(table.logical)+"\t"+std::to_string(table.result_records)+"\t"+std::to_string(table.result_bytes)+"\tPASS\n";
  write_output(output.descriptor,"F265-D18.verifier_attestation.tsv",result,65536);std::string verified=hash256(result)+"  F265-D18.verifier_attestation.tsv\n"+hash256(manifest)+"  F265-D18.PAYLOAD.sha256\n";write_output(output.descriptor,"F265-D18.VERIFIED.sha256",verified,65536);
  if(listing(output.descriptor)!=std::vector<std::string>({"F265-D18.VERIFIED.sha256","F265-D18.verifier_attestation.tsv"}))throw Error("OUTPUT_MEMBERSHIP");
  struct stat ie{},oe{};if(fstat(input.descriptor,&ie)||fstat(output.descriptor,&oe)||ie.st_dev!=input.device||ie.st_ino!=input.inode||oe.st_dev!=output.device||oe.st_ino!=output.inode)throw Error("ROOT_CHANGED");if(close(input.descriptor)||close(output.descriptor))throw Error("ROOT_CLOSE");return 0;
}

} // namespace verify_d18

int main(int argc,char**argv){try{return verify_d18::program(argc,argv);}catch(const std::exception& e){std::cerr<<"F265-D18 fixture verification failed: "<<e.what()<<'\n';return 1;}}
