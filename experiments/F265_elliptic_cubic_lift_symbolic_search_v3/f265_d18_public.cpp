#include <algorithm>
#include <array>
#include <atomic>
#include <cerrno>
#include <chrono>
#include <clocale>
#include <cstdint>
#include <cstring>
#include <dirent.h>
#include <exception>
#include <fcntl.h>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <limits>
#include <map>
#include <memory>
#include <numeric>
#include <set>
#include <sstream>
#include <stdexcept>
#include <string>
#include <sys/stat.h>
#include <sys/types.h>
#include <time.h>
#include <thread>
#include <tuple>
#include <unistd.h>
#include <utility>
#include <vector>

#include <boost/multiprecision/cpp_int.hpp>
#include <boost/multiprecision/integer.hpp>

// F265-D18 public source draft.  The two deliberately invalid constants are
// the source-freeze gate required by D12--D18.  They must be replaced in one
// reviewed edit after fixture materialization and independent verification.
// No mode in this file is authorized to execute before the separate source,
// containment, runner, and release gates pass.

namespace f265_d18_public {

using boost::multiprecision::cpp_int;

static constexpr const char kFixturePayloadRoot[] =
    @F265_D18_FIXTURE_PAYLOAD_ROOT@;
static constexpr const char kFixtureVerificationRoot[] =
    @F265_D18_FIXTURE_VERIFICATION_ROOT@;

constexpr char kVersion[] = "F265-D18";
constexpr char kDiscoveryHash[] =
    "8b6f8dbe4eae9aa10c042928fc19fbe20a0015487340e7478135ce6f37b5adb5";
constexpr char kHeldoutHash[] =
    "b4a4c976013dd62c58376b948c51a1c5c380265a46fbf932a5e0972fb6c389d5";
constexpr char kEmptyHash[] =
    "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855";
constexpr uint64_t kMasterSeed = UINT64_C(0x0F265D09C0DEC0DE);
constexpr uint64_t kPacketGcdCap = UINT64_C(8388608);
constexpr uint64_t kDecoderGrant = UINT64_C(91111);
constexpr uint64_t kPacketEventCap = UINT64_C(60372);
constexpr size_t kTreeLeaves = 2048;

struct Fatal : std::runtime_error { using std::runtime_error::runtime_error; };
struct Resource : std::runtime_error { using std::runtime_error::runtime_error; };

class Sha256 {
 public:
  Sha256() { reset(); }
  void reset() {
    state_={0x6a09e667U,0xbb67ae85U,0x3c6ef372U,0xa54ff53aU,
            0x510e527fU,0x9b05688cU,0x1f83d9abU,0x5be0cd19U};
    total_=0;used_=0;buffer_.fill(0);
  }
  void add(const void* data,size_t n) {
    const auto* p=static_cast<const unsigned char*>(data);total_+=n;
    while(n){size_t take=std::min(n,64-used_);std::memcpy(buffer_.data()+used_,p,take);used_+=take;p+=take;n-=take;if(used_==64){round(buffer_.data());used_=0;}}
  }
  void add(const std::string& s){add(s.data(),s.size());}
  std::string final() {
    uint64_t bits=total_*8;buffer_[used_++]=0x80;
    if(used_>56){std::fill(buffer_.begin()+static_cast<ptrdiff_t>(used_),buffer_.end(),0);round(buffer_.data());used_=0;}
    std::fill(buffer_.begin()+static_cast<ptrdiff_t>(used_),buffer_.begin()+56,0);
    for(int i=0;i<8;++i)buffer_[63-i]=static_cast<unsigned char>(bits>>(8*i));round(buffer_.data());
    std::ostringstream out;out<<std::hex<<std::setfill('0');for(uint32_t x:state_)out<<std::setw(8)<<x;return out.str();
  }
 private:
  static uint32_t rotate(uint32_t x,unsigned n){return (x>>n)|(x<<(32-n));}
  void round(const unsigned char* p) {
    static constexpr uint32_t k[64]={
      0x428a2f98U,0x71374491U,0xb5c0fbcfU,0xe9b5dba5U,0x3956c25bU,0x59f111f1U,0x923f82a4U,0xab1c5ed5U,
      0xd807aa98U,0x12835b01U,0x243185beU,0x550c7dc3U,0x72be5d74U,0x80deb1feU,0x9bdc06a7U,0xc19bf174U,
      0xe49b69c1U,0xefbe4786U,0x0fc19dc6U,0x240ca1ccU,0x2de92c6fU,0x4a7484aaU,0x5cb0a9dcU,0x76f988daU,
      0x983e5152U,0xa831c66dU,0xb00327c8U,0xbf597fc7U,0xc6e00bf3U,0xd5a79147U,0x06ca6351U,0x14292967U,
      0x27b70a85U,0x2e1b2138U,0x4d2c6dfcU,0x53380d13U,0x650a7354U,0x766a0abbU,0x81c2c92eU,0x92722c85U,
      0xa2bfe8a1U,0xa81a664bU,0xc24b8b70U,0xc76c51a3U,0xd192e819U,0xd6990624U,0xf40e3585U,0x106aa070U,
      0x19a4c116U,0x1e376c08U,0x2748774cU,0x34b0bcb5U,0x391c0cb3U,0x4ed8aa4aU,0x5b9cca4fU,0x682e6ff3U,
      0x748f82eeU,0x78a5636fU,0x84c87814U,0x8cc70208U,0x90befffaU,0xa4506cebU,0xbef9a3f7U,0xc67178f2U};
    uint32_t w[64];for(int i=0;i<16;++i)w[i]=(uint32_t(p[4*i])<<24)|(uint32_t(p[4*i+1])<<16)|(uint32_t(p[4*i+2])<<8)|p[4*i+3];
    for(int i=16;i<64;++i)w[i]=w[i-16]+(rotate(w[i-15],7)^rotate(w[i-15],18)^(w[i-15]>>3))+w[i-7]+(rotate(w[i-2],17)^rotate(w[i-2],19)^(w[i-2]>>10));
    uint32_t a=state_[0],b=state_[1],c=state_[2],d=state_[3],e=state_[4],f=state_[5],g=state_[6],h=state_[7];
    for(int i=0;i<64;++i){uint32_t t=h+(rotate(e,6)^rotate(e,11)^rotate(e,25))+((e&f)^((~e)&g))+k[i]+w[i];uint32_t u=(rotate(a,2)^rotate(a,13)^rotate(a,22))+((a&b)^(a&c)^(b&c));h=g;g=f;f=e;e=d+t;d=c;c=b;b=a;a=t+u;}
    state_[0]+=a;state_[1]+=b;state_[2]+=c;state_[3]+=d;state_[4]+=e;state_[5]+=f;state_[6]+=g;state_[7]+=h;
  }
  std::array<uint32_t,8> state_{};std::array<unsigned char,64> buffer_{};uint64_t total_=0;size_t used_=0;
};

std::string sha256(const std::string& s){Sha256 h;h.add(s);return h.final();}
uint64_t fnv1a(const std::string& s){uint64_t h=UINT64_C(14695981039346656037);for(unsigned char c:s)h=(h^c)*UINT64_C(1099511628211);return h;}

cpp_int absz(cpp_int x){return x<0?-x:x;}
cpp_int modz(cpp_int x,const cpp_int& n){x%=n;if(x<0)x+=n;return x;}
cpp_int gcdz(cpp_int a,cpp_int b){a=absz(a);b=absz(b);while(b!=0){cpp_int r=a%b;a=b;b=r;}return a;}
unsigned bitlen(const cpp_int& x){if(x<=0)throw Fatal("BITLEN_DOMAIN");return static_cast<unsigned>(boost::multiprecision::msb(x))+1;}
cpp_int powz(cpp_int a,unsigned e){cpp_int r=1;while(e){if(e&1U)r*=a;e>>=1;if(e)a*=a;}return r;}
cpp_int powmod(cpp_int a,cpp_int e,const cpp_int& n){a=modz(a,n);cpp_int r=1%n;while(e){if((e&1)!=0)r=r*a%n;e>>=1;if(e)a=a*a%n;}return r;}
cpp_int invmod(cpp_int a,const cpp_int& n){a=modz(a,n);cpp_int b=n,x=1,y=0;while(b){cpp_int q=a/b,r=a-q*b;a=b;b=r;r=x-q*y;x=y;y=r;}if(a!=1)throw Fatal("NONUNIT_INVERSE");return modz(x,n);}
cpp_int isqrtz(const cpp_int& n){if(n<0)throw Fatal("ISQRT_DOMAIN");if(n<2)return n;cpp_int x=cpp_int(1)<<((bitlen(n)+1)/2);for(;;){cpp_int y=(x+n/x)>>1;if(y>=x){while((x+1)*(x+1)<=n)++x;while(x*x>n)--x;return x;}x=y;}}
bool squarez(const cpp_int& n,cpp_int* root=nullptr){if(n<0)return false;cpp_int r=isqrtz(n);if(r*r!=n)return false;if(root)*root=r;return true;}

std::string hexz(const cpp_int& x){if(x<0)return "-"+hexz(-x);std::ostringstream out;out<<std::hex<<x;return out.str();}
std::string maskz(uint64_t x){std::ostringstream out;out<<std::hex<<std::setw(16)<<std::setfill('0')<<x;return out.str();}
std::string seconds9(const cpp_int& ns){if(ns<0)throw Fatal("NEGATIVE_TIME");cpp_int q=ns/1000000000,r=ns%1000000000;std::ostringstream out;out<<q<<'.'<<std::setw(9)<<std::setfill('0')<<r;return out.str();}

struct Rational {
  cpp_int n=0,d=1;
  Rational()=default;Rational(cpp_int x):n(std::move(x)),d(1){}Rational(cpp_int x,cpp_int y):n(std::move(x)),d(std::move(y)){normalize();}
  void normalize(){if(d<=0||n<0)throw Fatal("RATIONAL_DOMAIN");cpp_int g=gcdz(n,d);if(g){n/=g;d/=g;}}
};
Rational operator+(const Rational&a,const Rational&b){return {a.n*b.d+b.n*a.d,a.d*b.d};}
Rational operator*(const Rational&a,const cpp_int&b){return {a.n*b,a.d};}
Rational operator*(const Rational&a,uint64_t b){return a*cpp_int(b);}
Rational operator*(const Rational&a,const Rational&b){return {a.n*b.n,a.d*b.d};}
cpp_int ceilq(const Rational& x){return (x.n+x.d-1)/x.d;}

uint64_t tick_ns(const timespec& start,const timespec& end){cpp_int sec=cpp_int(end.tv_sec)-start.tv_sec,nano=cpp_int(end.tv_nsec)-start.tv_nsec;cpp_int ns=sec*1000000000+nano;if(ns<0||ns>std::numeric_limits<uint64_t>::max())throw Fatal("CLOCK_RANGE");return ns.convert_to<uint64_t>();}
timespec monotonic(){timespec t{};if(clock_gettime(CLOCK_MONOTONIC,&t))throw Fatal("CLOCK");return t;}

bool dec_token(const std::string& s){return !s.empty()&&!(s.size()>1&&s[0]=='0')&&std::all_of(s.begin(),s.end(),[](unsigned char c){return c>='0'&&c<='9';});}
bool hex_token(const std::string& s){return !s.empty()&&!(s.size()>1&&s[0]=='0')&&std::all_of(s.begin(),s.end(),[](unsigned char c){return (c>='0'&&c<='9')||(c>='a'&&c<='f');});}
bool sha_token(const std::string& s){return s.size()==64&&std::all_of(s.begin(),s.end(),[](unsigned char c){return (c>='0'&&c<='9')||(c>='a'&&c<='f');});}
uint64_t parse_dec(const std::string& s){if(!dec_token(s))throw Fatal("DEC");uint64_t r=0;for(char c:s){if(r>(UINT64_MAX-uint64_t(c-'0'))/10)throw Fatal("DEC_RANGE");r=r*10+uint64_t(c-'0');}return r;}
cpp_int parse_hex(const std::string& s){if(!hex_token(s))throw Fatal("HEX");cpp_int x=0;for(char c:s)x=(x<<4)+(c<='9'?c-'0':c-'a'+10);return x;}

std::vector<std::string> split_fields(const std::string& line){std::vector<std::string> f;size_t p=0;for(;;){size_t e=line.find('\t',p);f.push_back(line.substr(p,e-p));if(e==std::string::npos)return f;p=e+1;}}
std::vector<std::string> split_lines(const std::string& bytes){if(bytes.empty()||bytes.back()!='\n'||bytes.find('\r')!=std::string::npos||bytes.find('\0')!=std::string::npos)throw Fatal("TEXT_BYTES");std::vector<std::string> out;size_t p=0;while(p<bytes.size()){size_t e=bytes.find('\n',p);out.push_back(bytes.substr(p,e-p));p=e+1;}return out;}

struct FileIdentity {dev_t dev{};ino_t ino{};off_t size{};mode_t mode{};uid_t uid{};gid_t gid{};nlink_t links{};timespec mt{},ct{};std::string sha;};
struct RootIdentity {dev_t dev{};ino_t ino{};mode_t mode{};uid_t uid{};gid_t gid{};};

timespec mtime_of(const struct stat& s){
#if defined(__APPLE__)
  return s.st_mtimespec;
#else
  return s.st_mtim;
#endif
}
timespec ctime_of(const struct stat& s){
#if defined(__APPLE__)
  return s.st_ctimespec;
#else
  return s.st_ctim;
#endif
}
FileIdentity file_tuple(const struct stat& s,const std::string& hash){return {s.st_dev,s.st_ino,s.st_size,mode_t(s.st_mode&07777),s.st_uid,s.st_gid,s.st_nlink,mtime_of(s),ctime_of(s),hash};}
bool same_time(const timespec&a,const timespec&b){return a.tv_sec==b.tv_sec&&a.tv_nsec==b.tv_nsec;}
bool same_file(const FileIdentity&a,const FileIdentity&b){return a.dev==b.dev&&a.ino==b.ino&&a.size==b.size&&a.mode==b.mode&&a.uid==b.uid&&a.gid==b.gid&&a.links==b.links&&same_time(a.mt,b.mt)&&same_time(a.ct,b.ct)&&a.sha==b.sha;}

bool absolute_grammar(const std::string& path){if(path.size()<2||path.size()>1024||path[0]!='/'||path.back()=='/')return false;size_t p=1;while(p<path.size()){size_t e=path.find('/',p);if(e==std::string::npos)e=path.size();std::string c=path.substr(p,e-p);if(c.empty()||c=="."||c=="..")return false;for(unsigned char x:c)if(!((x>='A'&&x<='Z')||(x>='a'&&x<='z')||(x>='0'&&x<='9')||x=='_'||x=='-'||x=='.'))return false;p=e+1;}return true;}

int walk_directory(const std::string& path){int fd=open("/",O_RDONLY|O_DIRECTORY|O_CLOEXEC);if(fd<0)throw Fatal("OPEN_SLASH");for(size_t p=1;p<path.size();){size_t e=path.find('/',p);if(e==std::string::npos)e=path.size();std::string c=path.substr(p,e-p);int next=openat(fd,c.c_str(),O_RDONLY|O_DIRECTORY|O_NOFOLLOW|O_CLOEXEC);int saved=errno;close(fd);errno=saved;if(next<0)throw Fatal("OPEN_COMPONENT");fd=next;p=e+1;}return fd;}

std::vector<std::string> enumerate(int fd){int copy=dup(fd);if(copy<0)throw Fatal("DUP_DIR");DIR* d=fdopendir(copy);if(!d){close(copy);throw Fatal("FDOPENDIR");}std::vector<std::string> out;errno=0;while(dirent* e=readdir(d)){std::string x=e->d_name;if(x!="."&&x!="..")out.push_back(x);}int saved=errno;if(closedir(d)||saved)throw Fatal("READDIR");std::sort(out.begin(),out.end());return out;}

bool contains_root(int child,dev_t dev,ino_t ino){int here=dup(child);if(here<0)throw Fatal("ANCESTRY_DUP");for(;;){struct stat s{};if(fstat(here,&s)){close(here);throw Fatal("ANCESTRY_STAT");}if(s.st_dev==dev&&s.st_ino==ino){close(here);return true;}int parent=openat(here,"..",O_RDONLY|O_DIRECTORY|O_NOFOLLOW|O_CLOEXEC);if(parent<0){close(here);throw Fatal("ANCESTRY_PARENT");}struct stat p{};if(fstat(parent,&p)){close(here);close(parent);throw Fatal("ANCESTRY_PARENT_STAT");}if(p.st_dev==s.st_dev&&p.st_ino==s.st_ino){close(here);close(parent);return false;}close(here);here=parent;}}

struct InputFile {
  int fd=-1;FileIdentity identity;std::string bytes;std::string basename;
  InputFile()=default;
  InputFile(int parent,const std::string& name,size_t cap):basename(name){fd=openat(parent,name.c_str(),O_RDONLY|O_NOFOLLOW|O_CLOEXEC);if(fd<0)throw Fatal("INPUT_OPEN");struct stat s0{},s1{};if(fstat(fd,&s0)||!S_ISREG(s0.st_mode)||s0.st_size<0||static_cast<uint64_t>(s0.st_size)>cap)throw Fatal("INPUT_META");std::array<char,65536>b{};for(;;){ssize_t n=read(fd,b.data(),b.size());if(n<0)throw Fatal("INPUT_READ");if(n==0)break;bytes.append(b.data(),size_t(n));}std::string h=sha256(bytes);if(fstat(fd,&s1))throw Fatal("INPUT_POST_STAT");FileIdentity before=file_tuple(s0,h),after=file_tuple(s1,h);if(!same_file(before,after))throw Fatal("INPUT_RACE");identity=before;if(lseek(fd,0,SEEK_SET)!=0)throw Fatal("INPUT_REWIND");}
  InputFile(InputFile&&x)noexcept:fd(x.fd),identity(x.identity),bytes(std::move(x.bytes)),basename(std::move(x.basename)){x.fd=-1;}
  InputFile& operator=(InputFile&&x)noexcept{if(this!=&x){if(fd>=0)close(fd);fd=x.fd;x.fd=-1;identity=x.identity;bytes=std::move(x.bytes);basename=std::move(x.basename);}return *this;}
  InputFile(const InputFile&)=delete;InputFile&operator=(const InputFile&)=delete;
  ~InputFile(){if(fd>=0)close(fd);}
  void reauthenticate(){if(lseek(fd,0,SEEK_SET)!=0)throw Fatal("REAUTH_REWIND");std::string now;std::array<char,65536>b{};for(;;){ssize_t n=read(fd,b.data(),b.size());if(n<0)throw Fatal("REAUTH_READ");if(!n)break;now.append(b.data(),size_t(n));}struct stat s{};if(fstat(fd,&s))throw Fatal("REAUTH_STAT");FileIdentity current=file_tuple(s,sha256(now));if(now!=bytes||!same_file(identity,current))throw Fatal("INPUT_MUTATION");}
};

struct InputRoot {
  int fd=-1;RootIdentity identity;std::vector<std::string> membership;std::map<std::string,InputFile> file;
  InputRoot(const std::string& path,const std::vector<std::pair<std::string,size_t>>& expected){fd=walk_directory(path);struct stat s{};if(fstat(fd,&s)||!S_ISDIR(s.st_mode))throw Fatal("INPUT_ROOT");identity={s.st_dev,s.st_ino,mode_t(s.st_mode&07777),s.st_uid,s.st_gid};membership=enumerate(fd);std::vector<std::string> names;for(const auto& x:expected)names.push_back(x.first);std::sort(names.begin(),names.end());if(membership!=names)throw Fatal("INPUT_MEMBERSHIP");for(const auto& x:expected)file.emplace(x.first,InputFile(fd,x.first,x.second));}
  InputRoot(InputRoot&&)=delete;InputRoot(const InputRoot&)=delete;~InputRoot(){if(fd>=0)close(fd);}
  void reauthenticate(){struct stat s{};if(fstat(fd,&s)||s.st_dev!=identity.dev||s.st_ino!=identity.ino||mode_t(s.st_mode&07777)!=identity.mode||s.st_uid!=identity.uid||s.st_gid!=identity.gid||enumerate(fd)!=membership)throw Fatal("ROOT_MUTATION");for(auto& x:file)x.second.reauthenticate();}
};

struct DirectFile {
  int parent=-1;InputFile file;RootIdentity parent_id;
  explicit DirectFile(const std::string& path,size_t cap){size_t slash=path.rfind('/');std::string parent_path=slash==0?"/":path.substr(0,slash),base=path.substr(slash+1);if(parent_path=="/")parent=open("/",O_RDONLY|O_DIRECTORY|O_CLOEXEC);else parent=walk_directory(parent_path);if(parent<0)throw Fatal("FILE_PARENT");struct stat p{};if(fstat(parent,&p))throw Fatal("FILE_PARENT_STAT");parent_id={p.st_dev,p.st_ino,mode_t(p.st_mode&07777),p.st_uid,p.st_gid};file=InputFile(parent,base,cap);}
  DirectFile(DirectFile&&)=delete;DirectFile(const DirectFile&)=delete;~DirectFile(){if(parent>=0)close(parent);}
  void reauthenticate(){file.reauthenticate();struct stat p{};if(fstat(parent,&p)||p.st_dev!=parent_id.dev||p.st_ino!=parent_id.ino)throw Fatal("FILE_PARENT_CHANGED");}
};

struct OutputRoot {
  int fd=-1;RootIdentity identity;std::set<std::pair<dev_t,ino_t>> input_ids;std::vector<std::string> final_names;
  explicit OutputRoot(const std::string& path){fd=walk_directory(path);struct stat s{};if(fstat(fd,&s)||!S_ISDIR(s.st_mode)||s.st_uid!=geteuid()||(s.st_mode&077)!=0||!enumerate(fd).empty())throw Fatal("OUTPUT_ROOT");identity={s.st_dev,s.st_ino,mode_t(s.st_mode&07777),s.st_uid,s.st_gid};}
  OutputRoot(const OutputRoot&)=delete;~OutputRoot(){if(fd>=0)close(fd);}
  void forbid(const InputFile& f){input_ids.emplace(f.identity.dev,f.identity.ino);}
  void write_file(const std::string& name,const std::string& bytes,size_t cap){if(bytes.size()>cap)throw Fatal("OUTPUT_FILE_CAP");std::string temp="."+name+".tmp";int out=openat(fd,temp.c_str(),O_WRONLY|O_CREAT|O_EXCL|O_NOFOLLOW|O_CLOEXEC,0600);if(out<0)throw Fatal("OUTPUT_CREATE");try{struct stat s{};if(fstat(out,&s)||!S_ISREG(s.st_mode)||s.st_nlink!=1||s.st_uid!=geteuid()||(s.st_mode&0777)!=0600||input_ids.count({s.st_dev,s.st_ino}))throw Fatal("OUTPUT_META");size_t at=0;while(at<bytes.size()){ssize_t n=write(out,bytes.data()+at,bytes.size()-at);if(n<=0)throw Fatal("OUTPUT_WRITE");at+=size_t(n);}if(fsync(out))throw Fatal("OUTPUT_FSYNC");if(close(out)){out=-1;throw Fatal("OUTPUT_CLOSE");}out=-1;int verify=openat(fd,temp.c_str(),O_RDONLY|O_NOFOLLOW|O_CLOEXEC);if(verify<0)throw Fatal("OUTPUT_VERIFY_OPEN");std::string got;std::array<char,65536>b{};for(;;){ssize_t n=read(verify,b.data(),b.size());if(n<0){close(verify);throw Fatal("OUTPUT_VERIFY_READ");}if(!n)break;got.append(b.data(),size_t(n));}if(close(verify)||got!=bytes)throw Fatal("OUTPUT_VERIFY_BYTES");struct stat absent{};if(fstatat(fd,name.c_str(),&absent,AT_SYMLINK_NOFOLLOW)==0||errno!=ENOENT)throw Fatal("OUTPUT_FINAL_EXISTS");if(renameat(fd,temp.c_str(),fd,name.c_str())||fsync(fd))throw Fatal("OUTPUT_RENAME");final_names.push_back(name);}catch(...){if(out>=0)close(out);unlinkat(fd,temp.c_str(),0);throw;}}
  void finish(){struct stat s{};if(fstat(fd,&s)||s.st_dev!=identity.dev||s.st_ino!=identity.ino||mode_t(s.st_mode&07777)!=identity.mode||s.st_uid!=identity.uid||s.st_gid!=identity.gid)throw Fatal("OUTPUT_ROOT_CHANGED");std::sort(final_names.begin(),final_names.end());if(enumerate(fd)!=final_names)throw Fatal("OUTPUT_FINAL_MEMBERSHIP");}
};

void roots_distinct(OutputRoot& out,const std::vector<InputRoot*>& roots,const std::vector<DirectFile*>& files){for(size_t i=0;i<roots.size();++i){InputRoot* r=roots[i];if(contains_root(out.fd,r->identity.dev,r->identity.ino)||contains_root(r->fd,out.identity.dev,out.identity.ino))throw Fatal("ROOT_ALIAS");for(size_t j=0;j<i;++j)if(contains_root(r->fd,roots[j]->identity.dev,roots[j]->identity.ino)||contains_root(roots[j]->fd,r->identity.dev,r->identity.ino))throw Fatal("INPUT_ROOT_ALIAS");for(auto& x:r->file)out.forbid(x.second);}for(DirectFile* f:files){out.forbid(f->file);if(contains_root(out.fd,f->parent_id.dev,f->parent_id.ino)||contains_root(f->parent,out.identity.dev,out.identity.ino))throw Fatal("FILE_OUTPUT_ALIAS");}}

struct Cli {
  std::string mode,split;unsigned workers=0;std::map<std::string,std::string> option;
};

Cli parse_cli(int argc,char**argv){if(argc<3||(argc&1)==0)throw Fatal("CLI_PAIRS");Cli c;for(int i=1;i<argc;i+=2){std::string key=argv[i];if(key.empty()||key.rfind("--",0)!=0||!c.option.emplace(key,argv[i+1]).second)throw Fatal("CLI_OPTION");}auto m=c.option.find("--mode");if(m==c.option.end())throw Fatal("CLI_MODE");c.mode=m->second;auto s=c.option.find("--split");if(s!=c.option.end())c.split=s->second;auto w=c.option.find("--workers");if(w!=c.option.end()){if(w->second.size()!=1||w->second[0]<'1'||w->second[0]>'8')throw Fatal("WORKERS");c.workers=unsigned(w->second[0]-'0');}
  std::set<std::string> need{"--mode"};
  if(c.mode=="preflight")need.insert({"--fixture-root","--fixture-verification-root","--discovery-public","--heldout-public","--output-root","--workers"});
  else if(c.mode=="evaluate"){if(c.split!="discovery"&&c.split!="heldout")throw Fatal("SPLIT");need.insert({"--split","--fixture-root","--fixture-verification-root","--public-corpus","--output-root","--workers"});if(c.split=="heldout")need.insert({"--prior-evaluation-root","--prior-replay-root"});}
  else if(c.mode=="replay"){if(c.split!="discovery"&&c.split!="heldout")throw Fatal("SPLIT");need.insert({"--split","--fixture-root","--fixture-verification-root","--public-corpus","--evaluation-root","--output-root","--workers"});if(c.split=="heldout")need.insert({"--prior-evaluation-root","--prior-replay-root"});}
  else if(c.mode=="seal-public")need.insert({"--discovery-public","--heldout-public","--discovery-evaluation-root","--discovery-replay-root","--heldout-evaluation-root","--heldout-replay-root","--output-root"});
  else if(c.mode=="diagnostics")need.insert({"--discovery-public","--heldout-public","--discovery-evaluation-root","--heldout-evaluation-root","--sealed-root","--output-root"});
  else throw Fatal("MODE");if(c.option.size()!=need.size())throw Fatal("CLI_SET");for(const auto& x:need)if(!c.option.count(x))throw Fatal("CLI_REQUIRED");for(const auto& [key,value]:c.option)if(key!="--mode"&&key!="--split"&&key!="--workers"&&!absolute_grammar(value))throw Fatal("ABS");return c;}

enum CounterId : size_t {
  CURVE_PROPOSALS,RANDOM_BELOW_CALLS,RANDOM_BELOW_ITERATIONS,RNG_DRAWS,
  ADMITTED_ROWS,AFFINE_ADDITIONS,AFFINE_SAFETY_GCDS,DISCRIMINANT_GCDS,
  ROW_ROOT_GCDS,PRODUCT_MULTIPLICATIONS,PEEL_EXACT_DIVISIONS,
  PEEL_BASE_REMAINDERS,PEEL_MODULAR_MULTIPLICATIONS,PEEL_GCDS,
  PEEL_RESIDUAL_DIVISIONS,PEEL_SQUARE_TESTS,F271_SCALAR_GCDS,
  F271_SATURATION_POWERS,F271_REFINEMENT_DIVISIONS,F271_RECURSION_NODES,
  F271_TOUCHES,F271_LEAF_ASSIGNMENTS,F271_TREE_NODE_UPDATES,
  F271_EXPONENT_COORD_UPDATES,F271_RECONSTRUCTION_INCIDENCES,
  F271_TERMINAL_BLOCKS,F271_REPLACEMENT_COMPARISONS,F271_FINAL_COMPARISONS,
  F271_BLOCK_COMPARISONS,F271_PARITY_CELLS,F271_GF2_WORD_OPERATIONS,
  SELECTED_EXACT_PRODUCTS,SELECTED_MODULAR_PRODUCTS,INTEGER_SQUARE_ROOTS,
  MODULAR_INVERSIONS,SIGNED_RELATION_GCDS,BASIS_RECORDS,FACTOR_EVENT_LINES,
  COUNTER_COUNT
};

const std::array<const char*,COUNTER_COUNT> kCounterName{{
 "CURVE_PROPOSALS","RANDOM_BELOW_CALLS","RANDOM_BELOW_ITERATIONS","RNG_DRAWS",
 "ADMITTED_ROWS","AFFINE_ADDITIONS","AFFINE_SAFETY_GCDS","DISCRIMINANT_GCDS",
 "ROW_ROOT_GCDS","PRODUCT_MULTIPLICATIONS","PEEL_EXACT_DIVISIONS",
 "PEEL_BASE_REMAINDERS","PEEL_MODULAR_MULTIPLICATIONS","PEEL_GCDS",
 "PEEL_RESIDUAL_DIVISIONS","PEEL_SQUARE_TESTS","F271_SCALAR_GCDS",
 "F271_SATURATION_POWERS","F271_REFINEMENT_DIVISIONS","F271_RECURSION_NODES",
 "F271_TOUCHES","F271_LEAF_ASSIGNMENTS","F271_TREE_NODE_UPDATES",
 "F271_EXPONENT_COORD_UPDATES","F271_RECONSTRUCTION_INCIDENCES",
 "F271_TERMINAL_BLOCKS","F271_REPLACEMENT_COMPARISONS","F271_FINAL_COMPARISONS",
 "F271_BLOCK_COMPARISONS","F271_PARITY_CELLS","F271_GF2_WORD_OPERATIONS",
 "SELECTED_EXACT_PRODUCTS","SELECTED_MODULAR_PRODUCTS","INTEGER_SQUARE_ROOTS",
 "MODULAR_INVERSIONS","SIGNED_RELATION_GCDS","BASIS_RECORDS","FACTOR_EVENT_LINES"}};

const std::array<uint64_t,COUNTER_COUNT> kPacketCap{{
 29952,59904,7667712,15335424,122112,121176,242352,29952,122112,121644,
 122112,122112,1953792,122112,122112,122112,8388608,4893354,13981013,
 4194304,699050,4923306,54156366,313174656,10812672,877500,29360124,
 9652500,39012624,56160000,245366784,1916928,1916928,29952,29952,59904,
 29952,60372}};

const std::array<uint64_t,COUNTER_COUNT> kBankCap{{
 64,128,16384,32768,320,318,636,64,320,319,320,320,5120,320,320,320,
 91111,26631,76302,23040,3591,26695,293645,1704384,120000,1875,159786,
 20625,180411,120000,524288,4096,4096,64,64,128,64,129}};

struct Counters {
  std::array<uint64_t,COUNTER_COUNT> v{};
  void add(CounterId id,uint64_t n=1,uint64_t cap=UINT64_MAX){if(n>cap||v[id]>cap-n)throw Resource(std::string("COUNTER_")+kCounterName[id]);v[id]+=n;}
  void add_packet(CounterId id,uint64_t n=1){if(n>kPacketCap[id]||v[id]>kPacketCap[id]-n)throw Fatal(std::string("PACKET_COUNTER_")+kCounterName[id]);v[id]+=n;}
};

uint64_t mix64(uint64_t x){x+=UINT64_C(0x9e3779b97f4a7c15);x=(x^(x>>30))*UINT64_C(0xbf58476d1ce4e5b9);x=(x^(x>>27))*UINT64_C(0x94d049bb133111eb);return x^(x>>31);}
uint64_t seed_key(std::initializer_list<uint64_t> x){uint64_t h=kMasterSeed;for(uint64_t y:x)h=mix64(h^mix64(y));return h;}
struct Rng {uint64_t state;Counters* count;uint64_t next(){count->add(RNG_DRAWS,1,kBankCap[RNG_DRAWS]);state=mix64(state);return state;}};

cpp_int random_below(Rng& r,const cpp_int& n){if(n<=1)return 0;r.count->add(RANDOM_BELOW_CALLS,1,kBankCap[RANDOM_BELOW_CALLS]);unsigned bits=bitlen(n-1);for(unsigned attempt=0;attempt<128;++attempt){r.count->add(RANDOM_BELOW_ITERATIONS,1,kBankCap[RANDOM_BELOW_ITERATIONS]);cpp_int x=r.next();if(bits>64)x|=cpp_int(r.next())<<64;if(bits<128)x&=(cpp_int(1)<<bits)-1;if(x<n)return x;}throw Resource("RESOURCE_REJECT_RANDOM_BELOW_CAP");}

struct Case {std::string split,shape,n_text;uint64_t split_code=0,factor_bits=0,shape_code=0,index=0;cpp_int N;};

std::vector<Case> parse_corpus(const DirectFile& input,const std::string& expected_split){
  const std::string expected_hash=expected_split=="discovery"?kDiscoveryHash:kHeldoutHash;if(input.file.identity.sha!=expected_hash)throw Fatal("PUBLIC_HASH");auto row=split_lines(input.file.bytes);if(row.empty()||row[0]!="version\tsplit\tshape\tfactor_bits\tindex\tN")throw Fatal("PUBLIC_HEADER");size_t wanted=expected_split=="discovery"?188:296;if(row.size()!=wanted+1)throw Fatal("PUBLIC_COUNT");std::set<std::string> n_seen,key_seen;std::vector<Case> out;uint64_t markers=0;
  const std::vector<uint64_t> menu=expected_split=="discovery"?std::vector<uint64_t>{12,16,20,24,32}:std::vector<uint64_t>{40,48,56,60};
  for(size_t i=1;i<row.size();++i){auto x=split_fields(row[i]);if(x.size()!=6||x[0]!="F268-D04"||x[1]!=expected_split||!dec_token(x[3])||!dec_token(x[4])||!dec_token(x[5]))throw Fatal("PUBLIC_ROW");uint64_t bits=parse_dec(x[3]),index=parse_dec(x[4]);cpp_int N=0;for(char c:x[5])N=N*10+(c-'0');if(N<3||(N&1)==0||!n_seen.insert(x[5]).second||!key_seen.insert(x[1]+"\t"+x[3]+"\t"+x[2]+"\t"+x[4]).second)throw Fatal("PUBLIC_KEY");if(x[2]=="marker-control"){++markers;continue;}uint64_t shape=x[2]=="random"?0:x[2]=="neighbor"?1:x[2]=="safe-safe"?2:99;if(shape==99||std::find(menu.begin(),menu.end(),bits)==menu.end())throw Fatal("PUBLIC_COHORT");out.push_back({x[1],x[2],x[5],expected_split=="discovery"?0U:1U,bits,shape,index,N});}
  if(markers!=8||out.size()!=(expected_split=="discovery"?180:288))throw Fatal("PUBLIC_FILTER");std::stable_sort(out.begin(),out.end(),[&](const Case&a,const Case&b){size_t ar=std::find(menu.begin(),menu.end(),a.factor_bits)-menu.begin(),br=std::find(menu.begin(),menu.end(),b.factor_bits)-menu.begin();return std::tie(ar,a.shape_code,a.index)<std::tie(br,b.shape_code,b.index);});return out;
}

using Mask=std::array<uint64_t,5>;
struct Event {
  uint64_t ordinal=0,phase=0,klass=0,side=0,curve=65535,row1=65535,row2=65535,mask_present=0,nonce=0;Mask mask{};cpp_int g=1;
  std::string suffix() const {std::ostringstream o;o<<ordinal<<'\t'<<phase<<'\t'<<klass<<'\t'<<side<<'\t'<<curve<<'\t'<<row1<<'\t'<<row2<<'\t'<<mask_present;for(uint64_t w:mask)o<<'\t'<<maskz(w);o<<'\t'<<hexz(g)<<'\t'<<nonce<<'\n';return o.str();}
};

struct Row {
  uint64_t original=0,curve=0,scalar=0;cpp_int u=0,v=0,a=0,carry=0,g=0,b=0;bool peel_square=false,survivor=false;
};
struct Curve {cpp_int A=0,B=0,x=0,y=0,delta=0;bool accepted=false;};
struct BasisRecord {char kind='L';uint64_t ordinal=0;Mask mask{};cpp_int R=0,X=0,rho=0,gm=0,gp=0;std::string root_class;};
struct Bank {
  Case key;std::array<Curve,2> curve;std::vector<Row> rows;std::vector<Event> events;std::vector<BasisRecord> basis;Counters count;
  uint64_t status=3,K=0,survivors=0,kernel=0,singletons=0,pairs=0,Ldim=0,Qdim=0,reservation=0,decoder_calls=0,nonce=0;
  bool peel_committed=false,basis_committed=false,quotient=false,all_q_global=false,strict_hit=false,low_hit=false,source_direct=false,source_skip=false,resource=false;
  std::string row_hash=kEmptyHash,peel_hash=kEmptyHash,basis_hash=kEmptyHash,event_hash=kEmptyHash;
};

void journal(Bank& bank,uint64_t phase,uint64_t klass,uint64_t side,uint64_t curve,uint64_t row1,uint64_t row2,const Mask& mask,const cpp_int& g){if(!(g>1&&g<bank.key.N&&bank.key.N%g==0))return;if(bank.events.size()>=129)throw Fatal("INVARIANT_EVENT_CAP");Event e;e.ordinal=bank.events.size();e.phase=phase;e.klass=klass;e.side=side;e.curve=curve;e.row1=row1;e.row2=row2;e.mask_present=klass>=4;e.mask=mask;e.g=g;e.nonce=bank.nonce;std::string line=e.suffix();if(line.size()>192)throw Fatal("EVENT_LINE_CAP");bank.events.push_back(std::move(e));bank.count.add(FACTOR_EVENT_LINES,1,kBankCap[FACTOR_EVENT_LINES]);}

struct Point {cpp_int x=0,y=0;bool infinity=false;};
enum class AddKind {OK,INFINITY,FACTOR_MINUS,FACTOR_PLUS,FACTOR_DENOM,FULL_EQUAL_X,FULL_DENOM};
struct AddResult {AddKind kind=AddKind::OK;Point p;cpp_int factor=1;uint64_t side=0;};

AddResult add_points(Bank& bank,uint64_t curve_id,const Point& p,const Point& q,uint64_t row1,uint64_t row2){bank.count.add(AFFINE_ADDITIONS,1,kBankCap[AFFINE_ADDITIONS]);const cpp_int& N=bank.key.N;const cpp_int& A=bank.curve[curve_id].A;if(p.x==q.x&&modz(p.y+q.y,N)==0)return {AddKind::INFINITY,{0,0,true},1,0};if(p.x==q.x&&p.y!=q.y){bank.count.add(AFFINE_SAFETY_GCDS,1,kBankCap[AFFINE_SAFETY_GCDS]);cpp_int g=gcdz(p.y-q.y,N);if(g>1&&g<N){journal(bank,1,1,1,curve_id,std::min(row1,row2),std::max(row1,row2),{},g);return {AddKind::FACTOR_MINUS,{},g,1};}bank.count.add(AFFINE_SAFETY_GCDS,1,kBankCap[AFFINE_SAFETY_GCDS]);g=gcdz(p.y+q.y,N);if(g>1&&g<N){journal(bank,1,1,2,curve_id,std::min(row1,row2),std::max(row1,row2),{},g);return {AddKind::FACTOR_PLUS,{},g,2};}return {AddKind::FULL_EQUAL_X,{},N,0};}
  bool doubling=p.x==q.x&&p.y==q.y;cpp_int numerator=doubling?3*p.x*p.x+A:q.y-p.y,denominator=modz(doubling?2*p.y:q.x-p.x,N);bank.count.add(AFFINE_SAFETY_GCDS,1,kBankCap[AFFINE_SAFETY_GCDS]);cpp_int g=gcdz(denominator,N);if(g>1&&g<N){journal(bank,1,2,0,curve_id,std::min(row1,row2),std::max(row1,row2),{},g);return {AddKind::FACTOR_DENOM,{},g,0};}if(g==N){if(doubling&&p.y==0)return {AddKind::INFINITY,{0,0,true},1,0};return {AddKind::FULL_DENOM,{},N,0};}cpp_int slope=modz(numerator*invmod(denominator,N),N),x=modz(slope*slope-p.x-q.x,N),y=modz(slope*(p.x-x)-p.y,N);return {AddKind::OK,{x,y,false},1,0};}

bool choose_curve(Bank& bank,uint64_t id){uint64_t domain=id==0?100:108;Rng rng{seed_key({UINT64_C(0xEC265D09),bank.key.split_code,bank.key.factor_bits,bank.key.shape_code,bank.key.index,domain,id}),&bank.count};for(uint64_t slot=0;slot<32;++slot){bank.count.add(CURVE_PROPOSALS,1,kBankCap[CURVE_PROPOSALS]);cpp_int A,x,y;if(id==0){A=1+random_below(rng,bank.key.N-1);x=random_below(rng,bank.key.N);y=random_below(rng,bank.key.N);}else{cpp_int s=1+random_below(rng,bank.key.N-1);x=s*s%bank.key.N;y=x*s%bank.key.N;A=(s+1)%bank.key.N;}cpp_int B=modz(y*y-x*x*x-A*x,bank.key.N),delta=4*A*A*A+27*B*B;bank.count.add(DISCRIMINANT_GCDS,1,kBankCap[DISCRIMINANT_GCDS]);cpp_int d=gcdz(delta,bank.key.N);if(d>1&&d<bank.key.N){journal(bank,0,0,0,id,65535,65535,{},d);bank.source_direct=true;return false;}if(d==bank.key.N||B==0)continue;if(id==1&&bank.curve[0].accepted&&A==bank.curve[0].A&&B==bank.curve[0].B&&x==bank.curve[0].x&&y==bank.curve[0].y)continue;bank.curve[id]={A,B,x,y,delta,true};return true;}bank.resource=true;return false;}

bool append_row(Bank& bank,uint64_t curve,uint64_t scalar,const Point& p){bank.count.add(ROW_ROOT_GCDS,1,kBankCap[ROW_ROOT_GCDS]);cpp_int g=gcdz(p.y,bank.key.N);uint64_t original=bank.rows.size();if(g>1&&g<bank.key.N){journal(bank,2,3,0,curve,original,65535,{},g);bank.source_direct=true;return false;}if(g==bank.key.N){bank.source_skip=true;return false;}cpp_int a=p.x*p.x*p.x+bank.curve[curve].A*p.x+bank.curve[curve].B;if(a<=0||bitlen(a)>361){bank.resource=true;return false;}cpp_int diff=a-p.y*p.y;if(diff%bank.key.N!=0)throw Fatal("ROW_CONGRUENCE");bank.rows.push_back({original,curve,scalar,p.x,p.y,a,diff/bank.key.N});bank.count.add(ADMITTED_ROWS,1,kBankCap[ADMITTED_ROWS]);return true;}

bool generate_curve(Bank& bank,uint64_t id){if(!choose_curve(bank,id))return false;Point base{bank.curve[id].x,bank.curve[id].y,false},current=base;for(uint64_t scalar=1;scalar<=bank.K;++scalar){if(!append_row(bank,id,scalar,current))return false;if(scalar!=bank.K){uint64_t base_row=id*bank.K,current_row=base_row+scalar-1;AddResult r=add_points(bank,id,current,base,current_row,base_row);if(r.kind!=AddKind::OK){if(r.kind==AddKind::FACTOR_MINUS||r.kind==AddKind::FACTOR_PLUS||r.kind==AddKind::FACTOR_DENOM)bank.source_direct=true;else bank.source_skip=true;return false;}current=r.p;}}return true;}

void seal_row_stream(Bank& bank){Sha256 h;for(const Row&r:bank.rows)h.add(std::to_string(r.original)+"\t"+std::to_string(r.curve)+"\t"+std::to_string(r.scalar)+"\t"+hexz(r.u)+"\t"+hexz(r.v)+"\t"+hexz(r.a)+"\t"+hexz(r.carry)+"\n");bank.row_hash=h.final();}

void peel(Bank& bank){cpp_int product=1;for(size_t i=0;i<bank.rows.size();++i){if(i)bank.count.add(PRODUCT_MULTIPLICATIONS,1,kBankCap[PRODUCT_MULTIPLICATIONS]);product*=bank.rows[i].a;}std::vector<Row> temporary=bank.rows;uint64_t survivors=0;Sha256 stream;for(Row& row:temporary){bank.count.add(PEEL_EXACT_DIVISIONS,1,kBankCap[PEEL_EXACT_DIVISIONS]);cpp_int complement=product/row.a;bank.count.add(PEEL_BASE_REMAINDERS,1,kBankCap[PEEL_BASE_REMAINDERS]);cpp_int base=complement%row.a;unsigned L=bitlen(row.a),bits=bitlen(cpp_int(L)),ones=__builtin_popcount(L);bank.count.add(PEEL_MODULAR_MULTIPLICATIONS,bits+ones,kBankCap[PEEL_MODULAR_MULTIPLICATIONS]);cpp_int residue=powmod(base,L,row.a);bank.count.add(PEEL_GCDS,1,kBankCap[PEEL_GCDS]);row.g=gcdz(row.a,residue);bank.count.add(PEEL_RESIDUAL_DIVISIONS,1,kBankCap[PEEL_RESIDUAL_DIVISIONS]);row.b=row.a/row.g;bank.count.add(PEEL_SQUARE_TESTS,1,kBankCap[PEEL_SQUARE_TESTS]);row.peel_square=squarez(row.b);row.survivor=row.peel_square;survivors+=row.survivor;stream.add(std::to_string(row.original)+"\t"+hexz(row.g)+"\t"+hexz(row.b)+"\t"+(row.peel_square?"1":"0")+"\t"+(row.survivor?"1":"0")+"\n");}bank.rows.swap(temporary);bank.survivors=survivors;bank.peel_hash=stream.final();bank.peel_committed=true;}

// F271 V2 production decoder.
struct LocalPiece {cpp_int q;uint16_t u=0,v=0;};
struct Block {cpp_int q=1;std::vector<uint16_t> e;bool square=false;cpp_int root=0;};

cpp_int saturated(Bank& bank,const cpp_int& u,const cpp_int& v){if(u<=1||v<=1)throw Fatal("SAT_DOMAIN");bank.count.add(F271_SATURATION_POWERS,1,kBankCap[F271_SATURATION_POWERS]);bank.count.add(F271_SCALAR_GCDS,1,kDecoderGrant);return gcdz(u,powmod(v,bitlen(u),u));}

std::vector<LocalPiece> same_support(Bank& bank,const cpp_int& x,const cpp_int& y,const cpp_int* supplied){bank.count.add(F271_RECURSION_NODES,1,23040);cpp_int d;if(supplied)d=*supplied;else{bank.count.add(F271_SCALAR_GCDS,1,kDecoderGrant);d=gcdz(x,y);}if(d<=1)throw Fatal("F271_SUPPORT_GCD");bank.count.add(F271_REFINEMENT_DIVISIONS,3,kBankCap[F271_REFINEMENT_DIVISIONS]);cpp_int x0=x/d,y0=y/d,A=1,B=1;if(x0>1)A=saturated(bank,d,x0);if(y0>1)B=saturated(bank,d,y0);cpp_int C=d/(A*B);std::vector<LocalPiece> out;if(A>1){auto child=same_support(bank,x0,A,nullptr);for(auto& z:child)out.push_back({z.q,uint16_t(z.u+z.v),z.v});}if(B>1){auto child=same_support(bank,y0,B,nullptr);for(auto& z:child)out.push_back({z.q,z.v,uint16_t(z.u+z.v)});}if(C>1)out.push_back({C,1,1});return out;}

std::vector<LocalPiece> two_base(Bank& bank,const cpp_int& x,const cpp_int& y,const cpp_int& d){bank.count.add(F271_TOUCHES,1,3591);cpp_int xs=saturated(bank,x,y),ys=saturated(bank,y,x);bank.count.add(F271_REFINEMENT_DIVISIONS,2,kBankCap[F271_REFINEMENT_DIVISIONS]);auto out=same_support(bank,xs,ys,&d);if(x/xs>1)out.push_back({x/xs,1,0});if(y/ys>1)out.push_back({y/ys,0,1});return out;}

struct Decoder {
  Bank& bank;size_t m;std::array<Block,kTreeLeaves> leaf;std::array<cpp_int,2*kTreeLeaves> tree;std::vector<Block> final_blocks;
  explicit Decoder(Bank& b,size_t rows):bank(b),m(rows){tree.fill(1);}
  void update(size_t slot){size_t node=kTreeLeaves+slot;tree[node]=leaf[slot].q;while(node>1){node>>=1;tree[node]=tree[2*node]*tree[2*node+1];bank.count.add(F271_TREE_NODE_UPDATES,1,kBankCap[F271_TREE_NODE_UPDATES]);}}
  size_t vacant(){for(size_t i=0;i<kTreeLeaves;++i)if(leaf[i].q==1)return i;throw Fatal("F271_TREE_OVERFLOW");}
  void assign(size_t slot,Block value){bank.count.add(F271_LEAF_ASSIGNMENTS,1,kBankCap[F271_LEAF_ASSIGNMENTS]);leaf[slot]=std::move(value);update(slot);}
  void stable_sort_pieces(std::vector<LocalPiece>& x,bool final){if(x.size()<2)return;std::vector<LocalPiece> scratch(x.size());for(size_t width=1;width<x.size();width*=2)for(size_t begin=0;begin<x.size();begin+=2*width){size_t middle=std::min(begin+width,x.size()),end=std::min(begin+2*width,x.size()),i=begin,j=middle,k=begin;while(i<middle&&j<end){bank.count.add(final?F271_FINAL_COMPARISONS:F271_REPLACEMENT_COMPARISONS,1,kBankCap[final?F271_FINAL_COMPARISONS:F271_REPLACEMENT_COMPARISONS]);bank.count.add(F271_BLOCK_COMPARISONS,1,kBankCap[F271_BLOCK_COMPARISONS]);scratch[k++]=(x[j].q<x[i].q)?x[j++]:x[i++];}while(i<middle)scratch[k++]=x[i++];while(j<end)scratch[k++]=x[j++];for(k=begin;k<end;++k)x[k]=scratch[k];}}
  void insert(size_t row,const cpp_int& input){cpp_int y=input;while(y>1){bank.count.add(F271_SCALAR_GCDS,1,kDecoderGrant);cpp_int g=gcdz(y,tree[1]);if(g==1){std::vector<uint16_t> e(m);e[row]=1;assign(vacant(),{y,std::move(e)});return;}size_t node=1;cpp_int carried=g;for(unsigned depth=0;depth<11;++depth){bank.count.add(F271_SCALAR_GCDS,1,kDecoderGrant);cpp_int left=gcdz(y,tree[2*node]);if(left>1){node*=2;carried=left;}else node=2*node+1;}size_t slot=node-kTreeLeaves;if(leaf[slot].q<=1)throw Fatal("F271_DESCENT");Block old=leaf[slot];auto pieces=two_base(bank,old.q,y,carried);std::vector<LocalPiece> replacement;cpp_int residual=1;for(const auto& z:pieces){if(z.u)replacement.push_back(z);else residual*=powz(z.q,z.v);}stable_sort_pieces(replacement,false);if(replacement.empty())throw Fatal("F271_EMPTY_REPLACEMENT");bool first=true;for(const auto& z:replacement){std::vector<uint16_t> e(m);for(size_t i=0;i<m;++i){uint32_t value=uint32_t(z.u)*old.e[i]+(i==row?z.v:0);bank.count.add(F271_EXPONENT_COORD_UPDATES,1,kBankCap[F271_EXPONENT_COORD_UPDATES]);if(value>360)throw Fatal("F271_EXPONENT");e[i]=uint16_t(value);}size_t target=first?slot:vacant();first=false;assign(target,{z.q,std::move(e)});}y=residual;}}
  std::vector<Block> finish(const std::vector<Row*>& input){std::vector<LocalPiece> order;for(size_t i=0;i<kTreeLeaves;++i)if(leaf[i].q>1)order.push_back({leaf[i].q,uint16_t(i),0});stable_sort_pieces(order,true);std::vector<Block> out;for(const auto& z:order)out.push_back(leaf[z.u]);if(out.size()>1875)throw Fatal("F271_BLOCK_CAP");for(size_t row=0;row<input.size();++row){cpp_int rebuilt=1;for(const Block& b:out)if(b.e[row]){bank.count.add(F271_RECONSTRUCTION_INCIDENCES,1,kBankCap[F271_RECONSTRUCTION_INCIDENCES]);rebuilt*=powz(b.q,b.e[row]);}if(rebuilt!=input[row]->a)throw Fatal("F271_RECONSTRUCTION");}cpp_int P=1;for(const auto& b:out)P*=b.q;if(!out.empty()){struct TerminalNode{cpp_int modulus;int left=-1,right=-1;size_t leaf_index=0;};std::vector<TerminalNode> nodes;std::vector<size_t> level;for(size_t i=0;i<out.size();++i){nodes.push_back({out[i].q*out[i].q,-1,-1,i});level.push_back(nodes.size()-1);}while(level.size()>1){std::vector<size_t> next;for(size_t i=0;i<level.size();i+=2){if(i+1==level.size())next.push_back(level[i]);else{size_t left=level[i],right=level[i+1];nodes.push_back({nodes[left].modulus*nodes[right].modulus,int(left),int(right),0});next.push_back(nodes.size()-1);}}level.swap(next);}std::vector<cpp_int> remainder(nodes.size());remainder[level[0]]=P;std::vector<size_t> stack{level[0]};while(!stack.empty()){size_t node=stack.back();stack.pop_back();if(nodes[node].left<0){Block& b=out[nodes[node].leaf_index];bank.count.add(F271_TERMINAL_BLOCKS,1,kBankCap[F271_TERMINAL_BLOCKS]);if(remainder[node]%b.q!=0)throw Fatal("F271_TERMINAL_DIVISION");cpp_int quotient=remainder[node]/b.q;bank.count.add(F271_SCALAR_GCDS,1,kDecoderGrant);if(gcdz(b.q,quotient)!=1)throw Fatal("F271_TERMINAL");b.square=squarez(b.q,&b.root);}else{size_t left=size_t(nodes[node].left),right=size_t(nodes[node].right);remainder[left]=remainder[node]%nodes[left].modulus;remainder[right]=remainder[node]%nodes[right].modulus;stack.push_back(right);stack.push_back(left);}}}return out;}
};

bool mask_bit(const Mask& m,size_t i){return (m[i/64]>>(i%64))&1U;}
void mask_flip(Mask& m,size_t i){m[i/64]^=UINT64_C(1)<<(i%64);}
void mask_xor(Mask& a,const Mask& b){for(size_t i=0;i<5;++i)a[i]^=b[i];}
bool mask_zero(const Mask& m){return std::all_of(m.begin(),m.end(),[](uint64_t x){return x==0;});}
size_t mask_weight(const Mask&m){size_t w=0;for(uint64_t x:m)w+=__builtin_popcountll(x);return w;}

struct Gf2 {
  Bank& bank;size_t columns;std::array<Mask,320> pivot{};std::array<bool,320> used{};
  explicit Gf2(Bank& b,size_t n):bank(b),columns(n){}
  uint64_t words()const{return (columns+63)/64;}
  Mask reduce(Mask x,bool insert){for(size_t c=0;c<columns;++c){bank.count.add(F271_GF2_WORD_OPERATIONS,1,kBankCap[F271_GF2_WORD_OPERATIONS]);if(!mask_bit(x,c))continue;if(used[c]){mask_xor(x,pivot[c]);bank.count.add(F271_GF2_WORD_OPERATIONS,words(),kBankCap[F271_GF2_WORD_OPERATIONS]);}else if(insert){used[c]=true;pivot[c]=x;bank.count.add(F271_GF2_WORD_OPERATIONS,words(),kBankCap[F271_GF2_WORD_OPERATIONS]);break;}}return x;}
  std::vector<Mask> nullspace(const std::vector<Mask>& equations){for(const Mask& x:equations)reduce(x,true);for(size_t c=columns;c-->0;)if(used[c])for(size_t d=0;d<c;++d)if(used[d]&&mask_bit(pivot[d],c)){mask_xor(pivot[d],pivot[c]);bank.count.add(F271_GF2_WORD_OPERATIONS,words(),kBankCap[F271_GF2_WORD_OPERATIONS]);}std::vector<Mask> out;for(size_t free=0;free<columns;++free)if(!used[free]){Mask v{};mask_flip(v,free);for(size_t c=0;c<columns;++c)if(used[c]&&mask_bit(pivot[c],free))mask_flip(v,c);out.push_back(v);}for(const Mask& v:out)for(const Mask& e:equations){unsigned parity=0;for(size_t i=0;i<5;++i)parity^=__builtin_parityll(v[i]&e[i]);if(parity)throw Fatal("GF2_KERNEL");}return out;}
};

std::vector<Mask> canonical_rref(Bank& bank,std::vector<Mask> rows,size_t columns){std::vector<Mask> out;std::array<int,320> pivot; pivot.fill(-1);uint64_t words=(columns+63)/64;for(Mask x:rows){for(size_t c=0;c<columns;++c){bank.count.add(F271_GF2_WORD_OPERATIONS,1,kBankCap[F271_GF2_WORD_OPERATIONS]);if(mask_bit(x,c)&&pivot[c]>=0){mask_xor(x,out[size_t(pivot[c])]);bank.count.add(F271_GF2_WORD_OPERATIONS,words,kBankCap[F271_GF2_WORD_OPERATIONS]);}}if(mask_zero(x))continue;size_t pc=0;while(pc<columns&&!mask_bit(x,pc))++pc;for(size_t r=0;r<out.size();++r)if(mask_bit(out[r],pc)){mask_xor(out[r],x);bank.count.add(F271_GF2_WORD_OPERATIONS,words,kBankCap[F271_GF2_WORD_OPERATIONS]);}pivot[pc]=int(out.size());out.push_back(x);}std::sort(out.begin(),out.end(),[&](const Mask&a,const Mask&b){size_t pa=0,pb=0;while(pa<columns&&!mask_bit(a,pa))++pa;while(pb<columns&&!mask_bit(b,pb))++pb;return pa<pb;});return out;}

void classify_basis(Bank& bank,const std::vector<Row*>& rows,const std::vector<Block>& blocks,std::vector<Mask> L,std::vector<Mask> Q){bool low_non_global=false;bank.basis.clear();auto classify=[&](char kind,uint64_t ordinal,const Mask& mask){cpp_int exact=1,selected=1,modular=1;for(const Block& b:blocks){unsigned exponent=0;for(size_t i=0;i<rows.size();++i)if(mask_bit(mask,rows[i]->original))exponent+=b.e[i];if(b.square)exact*=powz(b.root,exponent);else{if(exponent&1U)throw Fatal("ROOT_PARITY");exact*=powz(b.q,exponent/2);}}for(size_t i=0;i<rows.size();++i)if(mask_bit(mask,rows[i]->original)){bank.count.add(SELECTED_EXACT_PRODUCTS,1,kBankCap[SELECTED_EXACT_PRODUCTS]);bank.count.add(SELECTED_MODULAR_PRODUCTS,1,kBankCap[SELECTED_MODULAR_PRODUCTS]);selected*=rows[i]->a;modular=modular*rows[i]->v%bank.key.N;}bank.count.add(INTEGER_SQUARE_ROOTS,1,kBankCap[INTEGER_SQUARE_ROOTS]);cpp_int checked=isqrtz(selected);if(checked*checked!=selected||checked!=exact)throw Fatal("EXACT_ROOT");bank.count.add(MODULAR_INVERSIONS,1,kBankCap[MODULAR_INVERSIONS]);cpp_int R=exact%bank.key.N,rho=R*invmod(modular,bank.key.N)%bank.key.N;if(rho*rho%bank.key.N!=1)throw Fatal("NORMALIZED_ROOT");bank.count.add(SIGNED_RELATION_GCDS,1,kBankCap[SIGNED_RELATION_GCDS]);cpp_int gm=gcdz(rho-1,bank.key.N);bank.count.add(SIGNED_RELATION_GCDS,1,kBankCap[SIGNED_RELATION_GCDS]);cpp_int gp=gcdz(rho+1,bank.key.N);std::string klass;if(rho==1)klass="GLOBAL_PLUS";else if(rho==bank.key.N-1)klass="GLOBAL_MINUS";else{bool minus=gm>1&&gm<bank.key.N,plus=gp>1&&gp<bank.key.N;if(!minus&&!plus)throw Fatal("SIGNED_ROOT_CLASS");if(kind=='L'){klass="LOW_NON_GLOBAL";low_non_global=true;journal(bank,3,4,minus?1:2,65535,65535,65535,mask,minus?gm:gp);}else if(!low_non_global){klass="STRUCTURAL_Q_NON_GLOBAL";journal(bank,4,5,minus?1:2,65535,65535,65535,mask,minus?gm:gp);}else{klass="STRUCTURAL_ONLY_LOW_IMAGE";journal(bank,4,5,minus?1:2,65535,65535,65535,mask,minus?gm:gp);}}bank.count.add(BASIS_RECORDS,1,kBankCap[BASIS_RECORDS]);bank.basis.push_back({kind,ordinal,mask,R,modular,rho,gm,gp,klass});};for(size_t i=0;i<L.size();++i)classify('L',i,L[i]);for(size_t i=0;i<Q.size();++i)classify('Q',i,Q[i]);bank.Ldim=L.size();bank.Qdim=Q.size();bank.kernel=L.size()+Q.size();bank.quotient=!low_non_global;bank.low_hit=low_non_global;bank.all_q_global=true;for(const auto& r:bank.basis)if(r.kind=='Q'&&r.root_class!="GLOBAL_PLUS"&&r.root_class!="GLOBAL_MINUS")bank.all_q_global=false;Sha256 h;for(const auto&r:bank.basis){std::string line=std::string(1,r.kind)+"\t"+std::to_string(r.ordinal);for(uint64_t w:r.mask)line+='\t'+maskz(w);line+="\t"+hexz(r.R)+"\t"+hexz(r.X)+"\t"+hexz(r.rho)+"\t"+hexz(r.gm)+"\t"+hexz(r.gp)+"\t"+r.root_class+"\n";h.add(line);}bank.basis_hash=h.final();bank.basis_committed=true;}

void decode_bank(Bank& bank){std::vector<Row*> residual;for(Row& r:bank.rows)if(r.survivor)residual.push_back(&r);if(residual.empty()){bank.kernel=bank.singletons=bank.pairs=bank.Ldim=bank.Qdim=0;bank.quotient=bank.all_q_global=true;bank.low_hit=false;bank.basis_hash=kEmptyHash;bank.basis_committed=true;return;}if(residual.size()>64){bank.resource=true;return;}bank.reservation=kDecoderGrant;Decoder decoder(bank,residual.size());for(size_t i=0;i<residual.size();++i){if(residual[i]->a<=0||bitlen(residual[i]->a)>361||residual[i]->v<0||residual[i]->v>=bank.key.N||gcdz(residual[i]->v,bank.key.N)!=1||residual[i]->v*residual[i]->v%bank.key.N!=residual[i]->a%bank.key.N)throw Fatal("F271_INPUT");decoder.insert(i,residual[i]->a);}auto blocks=decoder.finish(residual);bank.decoder_calls=bank.count.v[F271_SCALAR_GCDS];if(bank.decoder_calls>kDecoderGrant)throw Fatal("F271_GCD_BOUND");std::vector<Mask> equations;std::map<std::vector<uint64_t>,std::vector<size_t>> signatures;for(const Block& b:blocks){if(b.square)continue;Mask eq{};for(size_t i=0;i<residual.size();++i){bank.count.add(F271_PARITY_CELLS,1,kBankCap[F271_PARITY_CELLS]);if(b.e[i]&1U)mask_flip(eq,i);}if(!mask_zero(eq))equations.push_back(eq);}size_t signature_words=(equations.size()+63)/64;for(size_t i=0;i<residual.size();++i){std::vector<uint64_t> s(signature_words);for(size_t r=0;r<equations.size();++r)if(mask_bit(equations[r],i))s[r/64]|=UINT64_C(1)<<(r%64);signatures[s].push_back(i);}std::vector<Mask> low;for(const auto& [sig,index]:signatures){bool zero=std::all_of(sig.begin(),sig.end(),[](uint64_t x){return x==0;});if(zero){bank.singletons=index.size();for(size_t i:index){Mask x{};mask_flip(x,i);low.push_back(x);}}else if(index.size()>1){size_t first=index[0];for(size_t j=1;j<index.size();++j){Mask x{};mask_flip(x,first);mask_flip(x,index[j]);low.push_back(x);}}if(index.size()>=2)bank.pairs+=index.size()*(index.size()-1)/2;}low=canonical_rref(bank,std::move(low),residual.size());Gf2 gf(bank,residual.size());auto full=gf.nullspace(equations);std::vector<Mask> complement;for(Mask x:full){for(const Mask& l:low){size_t pivot=0;while(pivot<residual.size()&&!mask_bit(l,pivot))++pivot;if(pivot<residual.size()&&mask_bit(x,pivot))mask_xor(x,l);}for(const Mask& q:complement){size_t pivot=0;while(pivot<residual.size()&&!mask_bit(q,pivot))++pivot;if(pivot<residual.size()&&mask_bit(x,pivot))mask_xor(x,q);}if(!mask_zero(x))complement.push_back(x);}complement=canonical_rref(bank,std::move(complement),residual.size());auto embed=[&](std::vector<Mask>& basis){for(Mask& m:basis){Mask original{};for(size_t i=0;i<residual.size();++i)if(mask_bit(m,i))mask_flip(original,residual[i]->original);m=original;}};embed(low);embed(complement);classify_basis(bank,residual,blocks,std::move(low),std::move(complement));}

// Public serialization, fixture preflight, and process-mode dispatch follow.

const std::vector<std::pair<std::string,size_t>> kFixtureFiles{
 {"F265-D18.source_operands.tsv",1048576},{"F265-D18.decoder_operands.tsv",4194304},
 {"F265-D18.rate_operands.tsv",4194304},{"F265-D18.expected_counters.tsv",1048576},
 {"F265-D18.expected_semantics.tsv",1048576},{"F265-D18.expected_digests.tsv",1048576},
 {"F265-D18.materializer_attestation.tsv",65536},{"F265-D18.PAYLOAD.sha256",65536}};
const std::vector<std::pair<std::string,size_t>> kVerifyFiles{
 {"F265-D18.verifier_attestation.tsv",65536},{"F265-D18.VERIFIED.sha256",65536}};

std::vector<std::pair<std::string,size_t>> evaluation_files(const std::string& split){std::string p="F265-D18."+split+".";return {{p+"meta.tsv",1048576},{p+"banks.tsv",128*1024*1024},{p+"rows.tsv",128*1024*1024},{p+"basis.tsv",128*1024*1024},{p+"events.tsv",15455488},{p+"event_witnesses.tsv",8388608},{p+"counters.tsv",8388608},{p+"CORE.sha256",65536}};}
std::vector<std::pair<std::string,size_t>> replay_files(const std::string& split){std::string p="F265-D18."+split+".";return {{p+"replay.tsv",1048576},{p+"replay_counters.tsv",1048576},{p+"REPLAY.sha256",65536}};}
const std::vector<std::pair<std::string,size_t>> kSealFiles{{"F265-D18.decision.tsv",1048576},{"F265-D18.SEALED.sha256",65536}};
const std::vector<std::pair<std::string,size_t>> kDiagnosticFiles{{"F265-D18.diagnostic_summary.tsv",1048576},{"F265-D18.diagnostic_details.tsv",7667712},{"F265-D18.DIAGNOSTICS.sha256",65536}};

void manifest_exact(const InputRoot& root,const std::string& manifest_name,const std::vector<std::string>& order){std::string expected;for(const auto& name:order){auto i=root.file.find(name);if(i==root.file.end())throw Fatal("MANIFEST_MEMBER");expected+=i->second.identity.sha+"  "+name+"\n";}if(root.file.at(manifest_name).bytes!=expected)throw Fatal("MANIFEST_BYTES");}

void authenticate_fixtures(InputRoot& payload,InputRoot& verification){std::vector<std::string> po;for(size_t i=0;i<7;++i)po.push_back(kFixtureFiles[i].first);manifest_exact(payload,"F265-D18.PAYLOAD.sha256",po);if(payload.file.at("F265-D18.PAYLOAD.sha256").identity.sha!=std::string(kFixturePayloadRoot))throw Fatal("FIXTURE_PAYLOAD_ROOT");
  std::string expected=verification.file.at("F265-D18.verifier_attestation.tsv").identity.sha+"  F265-D18.verifier_attestation.tsv\n"+payload.file.at("F265-D18.PAYLOAD.sha256").identity.sha+"  F265-D18.PAYLOAD.sha256\n";if(verification.file.at("F265-D18.VERIFIED.sha256").bytes!=expected||verification.file.at("F265-D18.VERIFIED.sha256").identity.sha!=std::string(kFixtureVerificationRoot))throw Fatal("FIXTURE_VERIFICATION_ROOT");auto att=split_lines(verification.file.at("F265-D18.verifier_attestation.tsv").bytes);if(att.size()!=2||att[0]!="version\tpayload_root\ttheory_root\tfiles\tlogical_operands\tresult_records\tresult_bytes\tstatus")throw Fatal("VERIFIER_ATTESTATION");auto a=split_fields(att[1]);if(a.size()!=8||a[0]!=kVersion||a[1]!=kFixturePayloadRoot||a[3]!="7"||a[7]!="PASS")throw Fatal("VERIFIER_PASS");}

std::string wrapper(const Bank& b){return std::string(kVersion)+"\t"+b.key.split+"\t"+std::to_string(b.key.factor_bits)+"\t"+b.key.shape+"\t"+std::to_string(b.key.index);}
std::string optional(bool present,uint64_t x){return present?std::to_string(x):"-";}
std::string optional_bool(bool present,bool x){return present?(x?"1":"0"):"-";}

struct EvaluationData {
  std::string meta,banks,rows,basis,events,witnesses,counters,manifest;
  std::vector<Bank> bank;
  Counters packet;
  uint64_t cumulative_events=0;std::string cumulative_event_hash=kEmptyHash;
  uint64_t split_rows=0,split_basis=0,split_events=0;
};

std::string bank_line(const Bank& b){std::ostringstream o;o<<wrapper(b)<<'\t'<<b.key.n_text<<'\t'<<(b.curve[0].accepted?hexz(b.curve[0].A):"-")<<'\t'<<(b.curve[0].accepted?hexz(b.curve[0].B):"-")<<'\t'<<(b.curve[1].accepted?hexz(b.curve[1].A):"-")<<'\t'<<(b.curve[1].accepted?hexz(b.curve[1].B):"-")<<'\t'<<b.status<<'\t'<<b.K<<'\t'<<b.rows.size()<<'\t'<<(b.peel_committed?1:0)<<'\t'<<(b.basis_committed?1:0)<<'\t'<<optional(b.peel_committed,b.survivors)<<'\t'<<optional(b.basis_committed,b.kernel)<<'\t'<<optional(b.basis_committed,b.singletons)<<'\t'<<optional(b.basis_committed,b.pairs)<<'\t'<<optional(b.basis_committed,b.Ldim)<<'\t'<<optional(b.basis_committed,b.Qdim)<<'\t'<<optional_bool(b.basis_committed,b.quotient)<<'\t'<<optional_bool(b.basis_committed,b.all_q_global)<<'\t'<<optional_bool(b.basis_committed,b.strict_hit)<<'\t'<<optional_bool(b.basis_committed,b.low_hit)<<'\t'<<(!b.events.empty()?1:0)<<'\t'<<b.events.size()<<'\t'<<b.event_hash<<'\t'<<b.row_hash<<'\t'<<b.peel_hash<<'\t'<<b.basis_hash<<'\t'<<b.reservation<<'\t'<<b.decoder_calls<<'\t'<<b.nonce<<'\n';return o.str();}

std::string row_line(const Bank& b,const Row& r){std::ostringstream o;o<<wrapper(b)<<'\t'<<r.original<<'\t'<<r.curve<<'\t'<<r.scalar<<'\t'<<hexz(r.u)<<'\t'<<hexz(r.v)<<'\t'<<hexz(r.a)<<'\t'<<hexz(r.carry);if(b.peel_committed)o<<'\t'<<hexz(r.g)<<'\t'<<hexz(r.b)<<'\t'<<(r.peel_square?1:0)<<'\t'<<(r.survivor?1:0);else o<<"\t-\t-\t-\t-";o<<'\n';return o.str();}
std::string basis_line(const Bank& b,const BasisRecord& r){std::ostringstream o;o<<wrapper(b)<<'\t'<<r.kind<<'\t'<<r.ordinal;for(uint64_t x:r.mask)o<<'\t'<<maskz(x);o<<'\t'<<hexz(r.R)<<'\t'<<hexz(r.X)<<'\t'<<hexz(r.rho)<<'\t'<<hexz(r.gm)<<'\t'<<hexz(r.gp)<<'\t'<<r.root_class<<'\n';return o.str();}
std::string event_line(const Bank& b,const Event& e){std::string raw=e.suffix();raw.pop_back();return wrapper(b)+"\t"+raw+"\n";}
const char* event_class(uint64_t x){static const char* n[]={"CURVE_DISCRIMINANT","FACTOR_X_SIGN","AFFINE_DENOMINATOR","ROW_ROOT","LOW_BASIS","STRUCTURAL_Q"};if(x>=6)throw Fatal("EVENT_CLASS");return n[x];}
std::string witness_line(const Bank& b,const std::string& slot,const Event& e){std::string raw=e.suffix();raw.pop_back();return wrapper(b)+"\t"+slot+"\t"+raw+"\n";}

void validate_projection(const EvaluationData& data){auto row=split_lines(data.rows),basis=split_lines(data.basis);std::map<std::string,std::vector<std::vector<std::string>>> grouped_rows,grouped_basis;for(size_t i=1;i<row.size();++i){auto f=split_fields(row[i]);if(f.size()!=16)throw Fatal("ROW_SCHEMA");grouped_rows[f[0]+"\t"+f[1]+"\t"+f[2]+"\t"+f[3]+"\t"+f[4]].push_back(std::move(f));}for(size_t i=1;i<basis.size();++i){auto f=split_fields(basis[i]);if(f.size()!=18)throw Fatal("BASIS_SCHEMA");grouped_basis[f[0]+"\t"+f[1]+"\t"+f[2]+"\t"+f[3]+"\t"+f[4]].push_back(std::move(f));}uint64_t rows_seen=0,basis_seen=0;for(const Bank& b:data.bank){std::string key=wrapper(b);auto& rr=grouped_rows[key];if(rr.size()!=b.rows.size())throw Fatal("ROW_GROUP_COUNT");Sha256 rh,ph;uint64_t survivors=0;for(size_t i=0;i<rr.size();++i){auto& f=rr[i];if(parse_dec(f[5])!=i)throw Fatal("ROW_ORDER");rh.add(f[5]+"\t"+f[6]+"\t"+f[7]+"\t"+f[8]+"\t"+f[9]+"\t"+f[10]+"\t"+f[11]+"\n");if(b.peel_committed){if(f[12]=="-"||f[13]=="-"||f[14]=="-"||f[15]=="-")throw Fatal("PEEL_ABSENT");ph.add(f[5]+"\t"+f[12]+"\t"+f[13]+"\t"+f[14]+"\t"+f[15]+"\n");survivors+=parse_dec(f[15]);}else if(f[12]!="-"||f[13]!="-"||f[14]!="-"||f[15]!="-")throw Fatal("PEEL_PRESENT");}if(rh.final()!=b.row_hash||(b.peel_committed?ph.final():std::string(kEmptyHash))!=b.peel_hash||(b.peel_committed&&survivors!=b.survivors))throw Fatal("ROW_DIGEST_PROJECTION");auto& bb=grouped_basis[key];if(!b.basis_committed&&!bb.empty())throw Fatal("BASIS_UNCOMMITTED");if(b.basis_committed&&bb.size()!=b.Ldim+b.Qdim)throw Fatal("BASIS_COUNT");Sha256 bh;for(size_t i=0;i<bb.size();++i){auto& f=bb[i];std::string suffix=f[5];for(size_t j=6;j<18;++j)suffix+='\t'+f[j];suffix+='\n';bh.add(suffix);}if((bb.empty()?std::string(kEmptyHash):bh.final())!=b.basis_hash)throw Fatal("BASIS_DIGEST_PROJECTION");rows_seen+=rr.size();basis_seen+=bb.size();}if(rows_seen!=data.split_rows||basis_seen!=data.split_basis)throw Fatal("SPLIT_COUNTS");}

struct PriorState {Counters packet;uint64_t events=0,split_events=0;std::string event_suffix;std::string event_hash=kEmptyHash;std::string root;};

PriorState prior_evaluation(InputRoot& root,const std::string& split,const PriorState* prefix_state=nullptr){std::string prefix="F265-D18."+split+".";manifest_exact(root,prefix+"CORE.sha256",{prefix+"meta.tsv",prefix+"banks.tsv",prefix+"rows.tsv",prefix+"basis.tsv",prefix+"events.tsv",prefix+"event_witnesses.tsv",prefix+"counters.tsv"});PriorState p;p.root=root.file.at(prefix+"CORE.sha256").identity.sha;auto meta=split_lines(root.file.at(prefix+"meta.tsv").bytes);if(meta.size()!=2||meta[0]!="version\tsplit\tpublic_sha256\tfixture_payload_root\tfixture_verification_root\tprior_evaluation_root\tprior_replay_root\tbank_count\trow_count\tbasis_count\tevent_count\tpacket_event_sha256\tstatus")throw Fatal("PRIOR_META");auto m=split_fields(meta[1]);if(m.size()!=13||m[0]!=kVersion||m[1]!=split||m[3]!=kFixturePayloadRoot||m[4]!=kFixtureVerificationRoot||m[12]!="PASS"||!sha_token(m[11]))throw Fatal("PRIOR_META_ROW");p.events=parse_dec(m[10]);p.event_hash=m[11];auto counters=split_lines(root.file.at(prefix+"counters.tsv").bytes);if(counters.empty()||counters[0]!="version\tsplit\tscope\tbank_ordinal\tcounter\tvalue\tcap")throw Fatal("PRIOR_COUNTER_HEADER");std::array<bool,COUNTER_COUNT> seen{};for(size_t i=1;i<counters.size();++i){auto x=split_fields(counters[i]);if(x.size()!=7||x[0]!=kVersion||x[1]!=split)throw Fatal("PRIOR_COUNTER_ROW");if(x[2]=="PACKET"){auto it=std::find(kCounterName.begin(),kCounterName.end(),x[4]);if(it==kCounterName.end()||x[3]!="-")throw Fatal("PRIOR_COUNTER_NAME");size_t n=it-kCounterName.begin();if(seen[n]||x[6]!=std::to_string(kPacketCap[n]))throw Fatal("PRIOR_COUNTER_DUP");seen[n]=true;p.packet.v[n]=parse_dec(x[5]);if(p.packet.v[n]>kPacketCap[n])throw Fatal("PRIOR_COUNTER_CAP");}}if(std::find(seen.begin(),seen.end(),false)!=seen.end())throw Fatal("PRIOR_COUNTER_MISSING");auto events=split_lines(root.file.at(prefix+"events.tsv").bytes);if(events.empty()||events[0]!="version\tsplit\tfactor_bits\tshape\tindex\tbank_event_ordinal\tphase\tclass\tside\tcurve\trow_1\trow_2\tmask_present\tmask_0\tmask_1\tmask_2\tmask_3\tmask_4\tg_hex\tbank_nonce")throw Fatal("PRIOR_EVENT_HEADER");std::string local;for(size_t i=1;i<events.size();++i){auto x=split_fields(events[i]);if(x.size()!=20||x[0]!=kVersion||x[1]!=split)throw Fatal("PRIOR_EVENT");for(size_t j=5;j<20;++j){if(j!=5)local+='\t';local+=x[j];}local+='\n';}p.split_events=events.size()-1;if(split=="discovery"){if(prefix_state)throw Fatal("DISCOVERY_PREFIX");p.event_suffix=local;}else{if(!prefix_state||prefix_state->events!=prefix_state->split_events)throw Fatal("HELDOUT_PREFIX");p.event_suffix=prefix_state->event_suffix+local;}if(std::count(p.event_suffix.begin(),p.event_suffix.end(),'\n')!=p.events||sha256(p.event_suffix)!=p.event_hash)throw Fatal("PRIOR_EVENTS");return p;}

std::string replay_root(InputRoot& root,const std::string& split,const std::string& expected_eval){std::string p="F265-D18."+split+".";auto summary=split_lines(root.file.at(p+"replay.tsv").bytes);if(summary.size()!=2)throw Fatal("REPLAY_SUMMARY");auto f=split_fields(summary[1]);if(f.size()!=14||f[0]!=kVersion||f[1]!=split||f[3]!=expected_eval||f[5]!=kFixturePayloadRoot||f[6]!=kFixtureVerificationRoot||f[11]!="1"||f[12]!="1"||f[13]!="PASS")throw Fatal("REPLAY_PASS");std::string expected=root.file.at(p+"replay.tsv").identity.sha+"  "+p+"replay.tsv\n"+root.file.at(p+"replay_counters.tsv").identity.sha+"  "+p+"replay_counters.tsv\n"+expected_eval+"  "+p+"CORE.sha256\n";if(root.file.at(p+"REPLAY.sha256").bytes!=expected)throw Fatal("REPLAY_MANIFEST");return root.file.at(p+"REPLAY.sha256").identity.sha;}

void finalize_bank(Bank& bank){if(bank.resource)bank.status=3;else if(bank.basis_committed)bank.status=0;else if(bank.source_direct)bank.status=1;else if(bank.source_skip)bank.status=2;else bank.status=3;if(bank.basis_committed){bool all_l=true,has_q=false;for(const auto&r:bank.basis){if(r.kind=='L'&&r.root_class!="GLOBAL_PLUS"&&r.root_class!="GLOBAL_MINUS")all_l=false;if(r.kind=='Q'&&r.root_class=="STRUCTURAL_Q_NON_GLOBAL")has_q=true;}bank.strict_hit=bank.status==0&&bank.quotient&&all_l&&has_q;}Sha256 eh;for(const Event&e:bank.events)eh.add(e.suffix());bank.event_hash=eh.final();if(!bank.peel_committed){bank.peel_hash=kEmptyHash;bank.survivors=0;}if(!bank.basis_committed){bank.basis.clear();bank.basis_hash=kEmptyHash;}bank.decoder_calls=bank.count.v[F271_SCALAR_GCDS];if(bank.reservation!=0&&bank.reservation!=kDecoderGrant)throw Fatal("RESERVATION_VALUE");if(bank.decoder_calls>bank.reservation)throw Fatal("RESERVATION_CALLS");}

Bank prepare_bank(const Case& c){Bank bank;bank.key=c;bank.K=std::min<uint64_t>(2*bitlen(c.N),160);bank.nonce=seed_key({c.split_code,c.factor_bits,c.shape_code,c.index})&UINT32_MAX;try{bool complete=generate_curve(bank,0)&&generate_curve(bank,1);seal_row_stream(bank);if(complete){if(bank.rows.size()!=2*bank.K)throw Fatal("SOURCE_ROW_COUNT");peel(bank);}}catch(const Resource&){bank.resource=true;seal_row_stream(bank);}return bank;}

EvaluationData build_evaluation(const std::vector<Case>& cases,const std::string& public_hash,const PriorState& prior,const std::string& prior_eval,const std::string& prior_replay,unsigned workers){EvaluationData out;out.packet=prior.packet;std::string event_preimage=prior.event_suffix;uint64_t committed_gcd=prior.packet.v[F271_SCALAR_GCDS];for(size_t chunk=0;chunk<cases.size();chunk+=8){size_t end=std::min(chunk+8,cases.size());std::vector<Bank> ready;for(size_t i=chunk;i<end;++i)ready.push_back(prepare_bank(cases[i]));size_t at=0;while(at<ready.size()){std::vector<size_t> granted;uint64_t active=0;while(at<ready.size()&&granted.size()<workers){Bank& b=ready[at];if(!b.peel_committed||b.resource){finalize_bank(b);++at;continue;}if(b.survivors==0){decode_bank(b);finalize_bank(b);++at;continue;}if(b.survivors>64){b.resource=true;finalize_bank(b);++at;continue;}if(committed_gcd+active+kDecoderGrant>kPacketGcdCap){if(!granted.empty())break;b.resource=true;finalize_bank(b);++at;continue;}b.reservation=kDecoderGrant;active+=kDecoderGrant;granted.push_back(at++);}std::vector<std::exception_ptr> failure(granted.size());std::vector<std::thread> thread;thread.reserve(granted.size());for(size_t slot=0;slot<granted.size();++slot)thread.emplace_back([&,slot](){try{decode_bank(ready[granted[slot]]);}catch(...){failure[slot]=std::current_exception();}});for(auto& worker:thread)worker.join();for(size_t slot=0;slot<granted.size();++slot){if(failure[slot])std::rethrow_exception(failure[slot]);Bank& b=ready[granted[slot]];finalize_bank(b);if(b.decoder_calls>kDecoderGrant)throw Fatal("DECODER_CALLS");committed_gcd+=b.decoder_calls;}if(granted.empty()&&at<ready.size())continue;}for(Bank& b:ready){for(size_t c=0;c<COUNTER_COUNT;++c)out.packet.add_packet(static_cast<CounterId>(c),b.count.v[c]);for(const Event&e:b.events){if(++out.cumulative_events+prior.events>kPacketEventCap)throw Fatal("PACKET_EVENT_CAP");event_preimage+=e.suffix();}out.split_rows+=b.rows.size();out.split_basis+=b.basis.size();out.split_events+=b.events.size();out.bank.push_back(std::move(b));}}
  out.cumulative_events=prior.events+out.split_events;out.cumulative_event_hash=sha256(event_preimage);
  out.banks="version\tsplit\tfactor_bits\tshape\tindex\tN\tA_0\tB_0\tA_1\tB_1\tstatus\tK\trow_count\tpeel_committed\tbasis_committed\tsurvivor_count\tkernel_dimension\tsingleton_count\tsupport_two_count\tL_dimension\tQ_dimension\tquotient_defined\tall_Q_images_global\tdecoder_strict_structural_hit\tlow_hit\tobserved_factor\tevent_count\tevent_sha256\trow_stream_sha256\tpeel_sha256\tbasis_sha256\tdecoder_reservation\tdecoder_call_count\tbank_nonce\n";
  out.rows="version\tsplit\tfactor_bits\tshape\tindex\toriginal_row\tcurve\tscalar\tu\tv\ta\tcarry\tpeel_g\tpeel_b\tpeel_b_square\tsurvivor\n";
  out.basis="version\tsplit\tfactor_bits\tshape\tindex\tbasis_kind\tordinal\tmask_0\tmask_1\tmask_2\tmask_3\tmask_4\tR_mod_N\tX\trho\tgcd_minus\tgcd_plus\troot_class\n";
  out.events="version\tsplit\tfactor_bits\tshape\tindex\tbank_event_ordinal\tphase\tclass\tside\tcurve\trow_1\trow_2\tmask_present\tmask_0\tmask_1\tmask_2\tmask_3\tmask_4\tg_hex\tbank_nonce\n";
  out.witnesses="version\tsplit\tfactor_bits\tshape\tindex\twitness_slot\tbank_event_ordinal\tphase\tclass\tside\tcurve\trow_1\trow_2\tmask_present\tmask_0\tmask_1\tmask_2\tmask_3\tmask_4\tg_hex\tbank_nonce\n";
  for(const Bank& b:out.bank){std::string bl=bank_line(b);if(bl.size()>16384)throw Fatal("BANK_ROW_CAP");out.banks+=bl;size_t temporary=bl.size();for(const Row&r:b.rows){std::string x=row_line(b,r);if(x.size()>512)throw Fatal("ROW_CAP");out.rows+=x;temporary+=x.size();}for(const BasisRecord&r:b.basis){std::string x=basis_line(b,r);if(x.size()>512)throw Fatal("BASIS_CAP");out.basis+=x;temporary+=x.size();}for(const Event&e:b.events){std::string x=event_line(b,e);if(x.size()>256)throw Fatal("EVENT_WRAPPED_CAP");out.events+=x;temporary+=x.size();}if(!b.events.empty()){out.witnesses+=witness_line(b,"OVERALL",b.events[0]);for(uint64_t klass=0;klass<6;++klass){auto i=std::find_if(b.events.begin(),b.events.end(),[&](const Event&e){return e.klass==klass;});if(i!=b.events.end())out.witnesses+=witness_line(b,event_class(klass),*i);}}if(temporary>262400)throw Resource("BANK_TEMPORARY_CAP");}
  out.counters="version\tsplit\tscope\tbank_ordinal\tcounter\tvalue\tcap\n";std::string split=cases.empty()?"":cases.front().split;for(size_t c=0;c<COUNTER_COUNT;++c)out.counters+=std::string(kVersion)+"\t"+split+"\tPACKET\t-\t"+kCounterName[c]+"\t"+std::to_string(out.packet.v[c])+"\t"+std::to_string(kPacketCap[c])+"\n";for(size_t i=0;i<out.bank.size();++i)for(size_t c=0;c<COUNTER_COUNT;++c)out.counters+=std::string(kVersion)+"\t"+split+"\tBANK\t"+std::to_string(i)+"\t"+kCounterName[c]+"\t"+std::to_string(out.bank[i].count.v[c])+"\t"+std::to_string(kBankCap[c])+"\n";
  out.meta="version\tsplit\tpublic_sha256\tfixture_payload_root\tfixture_verification_root\tprior_evaluation_root\tprior_replay_root\tbank_count\trow_count\tbasis_count\tevent_count\tpacket_event_sha256\tstatus\n"+std::string(kVersion)+"\t"+split+"\t"+public_hash+"\t"+kFixturePayloadRoot+"\t"+kFixtureVerificationRoot+"\t"+prior_eval+"\t"+prior_replay+"\t"+std::to_string(out.bank.size())+"\t"+std::to_string(out.split_rows)+"\t"+std::to_string(out.split_basis)+"\t"+std::to_string(out.cumulative_events)+"\t"+out.cumulative_event_hash+"\tPASS\n";
  validate_projection(out);std::string p="F265-D18."+split+".";out.manifest=sha256(out.meta)+"  "+p+"meta.tsv\n"+sha256(out.banks)+"  "+p+"banks.tsv\n"+sha256(out.rows)+"  "+p+"rows.tsv\n"+sha256(out.basis)+"  "+p+"basis.tsv\n"+sha256(out.events)+"  "+p+"events.tsv\n"+sha256(out.witnesses)+"  "+p+"event_witnesses.tsv\n"+sha256(out.counters)+"  "+p+"counters.tsv\n";uint64_t bytes=out.meta.size()+out.banks.size()+out.rows.size()+out.basis.size()+out.events.size()+out.witnesses.size()+out.counters.size()+out.manifest.size();if(bytes>226088448)throw Fatal("TOTAL_OUTPUT_CAP");return out;}

void write_evaluation(OutputRoot& output,const std::string& split,const EvaluationData& e){std::string p="F265-D18."+split+".";output.write_file(p+"meta.tsv",e.meta,1048576);output.write_file(p+"banks.tsv",e.banks,128*1024*1024);output.write_file(p+"rows.tsv",e.rows,128*1024*1024);output.write_file(p+"basis.tsv",e.basis,128*1024*1024);output.write_file(p+"events.tsv",e.events,15455488);output.write_file(p+"event_witnesses.tsv",e.witnesses,8388608);output.write_file(p+"counters.tsv",e.counters,8388608);output.write_file(p+"CORE.sha256",e.manifest,65536);output.finish();}

int mode_evaluate(const Cli& c){InputRoot fixture(c.option.at("--fixture-root"),kFixtureFiles),verification(c.option.at("--fixture-verification-root"),kVerifyFiles);authenticate_fixtures(fixture,verification);DirectFile corpus(c.option.at("--public-corpus"),8388608);auto cases=parse_corpus(corpus,c.split);OutputRoot output(c.option.at("--output-root"));std::vector<InputRoot*> roots{&fixture,&verification};std::vector<DirectFile*> direct{&corpus};PriorState prior;std::string prior_eval="-",prior_rep="-";std::unique_ptr<InputRoot> pe,pr;if(c.split=="heldout"){pe=std::make_unique<InputRoot>(c.option.at("--prior-evaluation-root"),evaluation_files("discovery"));prior=prior_evaluation(*pe,"discovery");prior_eval=prior.root;pr=std::make_unique<InputRoot>(c.option.at("--prior-replay-root"),replay_files("discovery"));prior_rep=replay_root(*pr,"discovery",prior.root);roots.push_back(pe.get());roots.push_back(pr.get());}roots_distinct(output,roots,direct);EvaluationData data=build_evaluation(cases,corpus.file.identity.sha,prior,prior_eval,prior_rep,c.workers);fixture.reauthenticate();verification.reauthenticate();corpus.reauthenticate();if(pe)pe->reauthenticate();if(pr)pr->reauthenticate();write_evaluation(output,c.split,data);return 0;}

int mode_replay(const Cli& c){InputRoot fixture(c.option.at("--fixture-root"),kFixtureFiles),verification(c.option.at("--fixture-verification-root"),kVerifyFiles),evaluation(c.option.at("--evaluation-root"),evaluation_files(c.split));authenticate_fixtures(fixture,verification);DirectFile corpus(c.option.at("--public-corpus"),8388608);auto cases=parse_corpus(corpus,c.split);OutputRoot output(c.option.at("--output-root"));std::vector<InputRoot*> roots{&fixture,&verification,&evaluation};std::vector<DirectFile*> direct{&corpus};PriorState prior;std::string prior_eval="-",prior_rep="-";std::unique_ptr<InputRoot> pe,pr;if(c.split=="heldout"){pe=std::make_unique<InputRoot>(c.option.at("--prior-evaluation-root"),evaluation_files("discovery"));prior=prior_evaluation(*pe,"discovery");prior_eval=prior.root;pr=std::make_unique<InputRoot>(c.option.at("--prior-replay-root"),replay_files("discovery"));prior_rep=replay_root(*pr,"discovery",prior_eval);roots.push_back(pe.get());roots.push_back(pr.get());}PriorState eval_state=prior_evaluation(evaluation,c.split,c.split=="heldout"?&prior:nullptr);roots_distinct(output,roots,direct);EvaluationData regenerated=build_evaluation(cases,corpus.file.identity.sha,prior,prior_eval,prior_rep,c.workers);std::string p="F265-D18."+c.split+".";const std::array<std::pair<std::string,const std::string*>,7> compare{{{p+"meta.tsv",&regenerated.meta},{p+"banks.tsv",&regenerated.banks},{p+"rows.tsv",&regenerated.rows},{p+"basis.tsv",&regenerated.basis},{p+"events.tsv",&regenerated.events},{p+"event_witnesses.tsv",&regenerated.witnesses},{p+"counters.tsv",&regenerated.counters}}};for(const auto& x:compare)if(evaluation.file.at(x.first).bytes!=*x.second)throw Fatal("REPLAY_BYTE_MISMATCH");if(evaluation.file.at(p+"CORE.sha256").bytes!=regenerated.manifest||eval_state.events!=regenerated.cumulative_events||eval_state.event_hash!=regenerated.cumulative_event_hash)throw Fatal("REPLAY_DIGEST_MISMATCH");std::string summary="version\tsplit\tpublic_sha256\tevaluation_root\tprior_replay_root\tfixture_payload_root\tfixture_verification_root\tbanks\trows\tbasis_records\tevents\tall_counters_match\tall_digests_match\tstatus\n"+std::string(kVersion)+"\t"+c.split+"\t"+corpus.file.identity.sha+"\t"+eval_state.root+"\t"+prior_rep+"\t"+kFixturePayloadRoot+"\t"+kFixtureVerificationRoot+"\t"+std::to_string(regenerated.bank.size())+"\t"+std::to_string(regenerated.split_rows)+"\t"+std::to_string(regenerated.split_basis)+"\t"+std::to_string(regenerated.cumulative_events)+"\t1\t1\tPASS\n";std::string counters="version\tsplit\tcounter\tvalue\tcap\n";for(size_t i=0;i<COUNTER_COUNT;++i)counters+=std::string(kVersion)+"\t"+c.split+"\t"+kCounterName[i]+"\t"+std::to_string(regenerated.packet.v[i])+"\t"+std::to_string(kPacketCap[i])+"\n";std::string manifest=sha256(summary)+"  "+p+"replay.tsv\n"+sha256(counters)+"  "+p+"replay_counters.tsv\n"+evaluation.file.at(p+"CORE.sha256").identity.sha+"  "+p+"CORE.sha256\n";if(c.split=="heldout")manifest+=pr->file.at("F265-D18.discovery.REPLAY.sha256").identity.sha+"  F265-D18.discovery.REPLAY.sha256\n";fixture.reauthenticate();verification.reauthenticate();evaluation.reauthenticate();corpus.reauthenticate();if(pe)pe->reauthenticate();if(pr)pr->reauthenticate();output.write_file(p+"replay.tsv",summary,1048576);output.write_file(p+"replay_counters.tsv",counters,1048576);output.write_file(p+"REPLAY.sha256",manifest,65536);output.finish();return 0;}

struct PublicBankView {
  Case key;uint64_t status=0,row_count=0,peel_committed=0,basis_committed=0;
  uint64_t survivor_count=0,quotient_defined=0,all_q_global=0,strict_hit=0;
  uint64_t observed_factor=0,event_count=0;std::array<cpp_int,2>A{},B{};
};

struct PublicEvaluationView {
  PriorState state;std::vector<PublicBankView> bank;uint64_t local_rows=0;
  uint64_t local_basis=0,local_events=0;
};

PublicEvaluationView authenticate_public_evaluation(InputRoot& root,const std::string& split,const std::vector<Case>& cases,const std::string& public_sha,const PriorState* prefix_state,const std::string& prior_eval,const std::string& prior_replay){PublicEvaluationView v;v.state=prior_evaluation(root,split,prefix_state);std::string p="F265-D18."+split+".";auto meta=split_lines(root.file.at(p+"meta.tsv").bytes);auto m=split_fields(meta[1]);if(m[2]!=public_sha||m[3]!=kFixturePayloadRoot||m[4]!=kFixtureVerificationRoot||m[5]!=prior_eval||m[6]!=prior_replay||parse_dec(m[7])!=cases.size())throw Fatal("EVALUATION_META_BINDING");v.local_rows=parse_dec(m[8]);v.local_basis=parse_dec(m[9]);auto banks=split_lines(root.file.at(p+"banks.tsv").bytes);const std::string bank_header="version\tsplit\tfactor_bits\tshape\tindex\tN\tA_0\tB_0\tA_1\tB_1\tstatus\tK\trow_count\tpeel_committed\tbasis_committed\tsurvivor_count\tkernel_dimension\tsingleton_count\tsupport_two_count\tL_dimension\tQ_dimension\tquotient_defined\tall_Q_images_global\tdecoder_strict_structural_hit\tlow_hit\tobserved_factor\tevent_count\tevent_sha256\trow_stream_sha256\tpeel_sha256\tbasis_sha256\tdecoder_reservation\tdecoder_call_count\tbank_nonce";if(banks.empty()||banks[0]!=bank_header||banks.size()!=cases.size()+1)throw Fatal("EVALUATION_BANK_HEADER");uint64_t rows_sum=0,basis_sum=0,event_sum=0;for(size_t i=0;i<cases.size();++i){auto f=split_fields(banks[i+1]);const Case& c=cases[i];if(f.size()!=34||f[0]!=kVersion||f[1]!=split||parse_dec(f[2])!=c.factor_bits||f[3]!=c.shape||parse_dec(f[4])!=c.index||f[5]!=c.n_text)throw Fatal("EVALUATION_BANK_KEY");PublicBankView b;b.key=c;b.status=parse_dec(f[10]);b.row_count=parse_dec(f[12]);b.peel_committed=parse_dec(f[13]);b.basis_committed=parse_dec(f[14]);if(b.status>3||b.peel_committed>1||b.basis_committed>1||b.basis_committed>b.peel_committed)throw Fatal("EVALUATION_BANK_STATE");if(parse_dec(f[11])!=std::min<uint64_t>(2*bitlen(c.N),160))throw Fatal("EVALUATION_K");for(size_t j=0;j<2;++j){size_t at=6+2*j;if((f[at]=="-")!=(f[at+1]=="-"))throw Fatal("EVALUATION_COEFFICIENT_PAIR");if(f[at]!="-"){b.A[j]=parse_hex(f[at]);b.B[j]=parse_hex(f[at+1]);}}if(!b.peel_committed){for(size_t j=15;j<=24;++j)if(f[j]!="-")throw Fatal("EVALUATION_ABSENCE_00");if(f[29]!=kEmptyHash||f[30]!=kEmptyHash)throw Fatal("EVALUATION_EMPTY_DIGEST");}else{b.survivor_count=parse_dec(f[15]);if(!b.basis_committed){for(size_t j=16;j<=24;++j)if(f[j]!="-")throw Fatal("EVALUATION_ABSENCE_10");if(!b.survivor_count||f[30]!=kEmptyHash)throw Fatal("EVALUATION_STAGE_10");}else{for(size_t j=16;j<=20;++j)parse_dec(f[j]);b.quotient_defined=parse_dec(f[21]);b.all_q_global=parse_dec(f[22]);b.strict_hit=parse_dec(f[23]);parse_dec(f[24]);if(b.survivor_count>64||b.quotient_defined>1||b.all_q_global>1||b.strict_hit>1||parse_dec(f[16])!=parse_dec(f[19])+parse_dec(f[20]))throw Fatal("EVALUATION_STAGE_11");basis_sum+=parse_dec(f[19])+parse_dec(f[20]);}}b.observed_factor=parse_dec(f[25]);b.event_count=parse_dec(f[26]);if(b.observed_factor>1||b.event_count>129||b.observed_factor!=(b.event_count!=0)||!sha_token(f[27])||!sha_token(f[28])||!sha_token(f[29])||!sha_token(f[30]))throw Fatal("EVALUATION_BANK_EVIDENCE");uint64_t reservation=parse_dec(f[31]),calls=parse_dec(f[32]);if((reservation!=0&&reservation!=kDecoderGrant)||calls>reservation||!dec_token(f[33]))throw Fatal("EVALUATION_RESERVATION");if((b.status==0&&(!b.peel_committed||!b.basis_committed))||((b.status==1||b.status==2)&&(b.peel_committed||b.basis_committed))||(b.basis_committed&&b.strict_hit&&b.status!=0))throw Fatal("EVALUATION_STATUS_STAGE");rows_sum+=b.row_count;event_sum+=b.event_count;v.bank.push_back(std::move(b));}if(rows_sum!=v.local_rows||basis_sum!=v.local_basis)throw Fatal("EVALUATION_BANK_TOTALS");auto rows=split_lines(root.file.at(p+"rows.tsv").bytes),basis=split_lines(root.file.at(p+"basis.tsv").bytes),events=split_lines(root.file.at(p+"events.tsv").bytes);if(rows.size()!=v.local_rows+1||basis.size()!=v.local_basis+1||events.size()!=event_sum+1||v.state.split_events!=event_sum)throw Fatal("EVALUATION_STREAM_TOTALS");v.local_events=event_sum;return v;}

std::string authenticate_replay_for_seal(InputRoot& root,const std::string& split,const PublicEvaluationView& evaluation,const std::string& public_sha,const std::string& prior_replay){std::string p="F265-D18."+split+".";auto summary=split_lines(root.file.at(p+"replay.tsv").bytes);if(summary.size()!=2||summary[0]!="version\tsplit\tpublic_sha256\tevaluation_root\tprior_replay_root\tfixture_payload_root\tfixture_verification_root\tbanks\trows\tbasis_records\tevents\tall_counters_match\tall_digests_match\tstatus")throw Fatal("SEAL_REPLAY_HEADER");auto f=split_fields(summary[1]);if(f.size()!=14||f[0]!=kVersion||f[1]!=split||f[2]!=public_sha||f[3]!=evaluation.state.root||f[4]!=prior_replay||f[5]!=kFixturePayloadRoot||f[6]!=kFixtureVerificationRoot||parse_dec(f[7])!=evaluation.bank.size()||parse_dec(f[8])!=evaluation.local_rows||parse_dec(f[9])!=evaluation.local_basis||parse_dec(f[10])!=evaluation.state.events||f[11]!="1"||f[12]!="1"||f[13]!="PASS")throw Fatal("SEAL_REPLAY_ROW");auto counters=split_lines(root.file.at(p+"replay_counters.tsv").bytes);if(counters.size()!=COUNTER_COUNT+1||counters[0]!="version\tsplit\tcounter\tvalue\tcap")throw Fatal("SEAL_REPLAY_COUNTERS");for(size_t i=0;i<COUNTER_COUNT;++i){auto x=split_fields(counters[i+1]);if(x.size()!=5||x[0]!=kVersion||x[1]!=split||x[2]!=kCounterName[i]||parse_dec(x[3])!=evaluation.state.packet.v[i]||x[4]!=std::to_string(kPacketCap[i]))throw Fatal("SEAL_REPLAY_COUNTER_ROW");}std::string manifest=root.file.at(p+"replay.tsv").identity.sha+"  "+p+"replay.tsv\n"+root.file.at(p+"replay_counters.tsv").identity.sha+"  "+p+"replay_counters.tsv\n"+evaluation.state.root+"  "+p+"CORE.sha256\n";if(split=="heldout")manifest+=prior_replay+"  F265-D18.discovery.REPLAY.sha256\n";if(root.file.at(p+"REPLAY.sha256").bytes!=manifest)throw Fatal("SEAL_REPLAY_MANIFEST");return root.file.at(p+"REPLAY.sha256").identity.sha;}

int mode_seal_public(const Cli& c){DirectFile discovery_public(c.option.at("--discovery-public"),8388608),heldout_public(c.option.at("--heldout-public"),8388608);auto discovery_cases=parse_corpus(discovery_public,"discovery"),heldout_cases=parse_corpus(heldout_public,"heldout");InputRoot discovery_eval(c.option.at("--discovery-evaluation-root"),evaluation_files("discovery")),discovery_replay(c.option.at("--discovery-replay-root"),replay_files("discovery")),heldout_eval(c.option.at("--heldout-evaluation-root"),evaluation_files("heldout")),heldout_replay(c.option.at("--heldout-replay-root"),replay_files("heldout"));PublicEvaluationView d=authenticate_public_evaluation(discovery_eval,"discovery",discovery_cases,discovery_public.file.identity.sha,nullptr,"-","-");std::string dr=authenticate_replay_for_seal(discovery_replay,"discovery",d,discovery_public.file.identity.sha,"-");PublicEvaluationView h=authenticate_public_evaluation(heldout_eval,"heldout",heldout_cases,heldout_public.file.identity.sha,&d.state,d.state.root,dr);std::string hr=authenticate_replay_for_seal(heldout_replay,"heldout",h,heldout_public.file.identity.sha,dr);OutputRoot output(c.option.at("--output-root"));roots_distinct(output,{&discovery_eval,&discovery_replay,&heldout_eval,&heldout_replay},{&discovery_public,&heldout_public});uint64_t eligible=0,hits=0;std::set<uint64_t> hit_bits;std::map<std::pair<uint64_t,uint64_t>,uint64_t> eligible_cells;bool all_eligible_complete=true;for(const auto& b:h.bank){if(b.status==0){++eligible;++eligible_cells[{b.key.factor_bits,b.key.shape_code}];all_eligible_complete=all_eligible_complete&&b.peel_committed&&b.basis_committed&&b.quotient_defined&&b.all_q_global;}if(b.strict_hit){++hits;hit_bits.insert(b.key.factor_bits);}}bool coverage=eligible>=260;for(uint64_t bits:{40,48,56,60})for(uint64_t shape=0;shape<3;++shape)coverage=coverage&&eligible_cells[{bits,shape}]>=22;bool all_null=h.local_events==0&&all_eligible_complete&&coverage;std::string decision;if(hits>=2&&hit_bits.size()>=2)decision="FINITE_STRUCTURAL_POSITIVE_SIGNAL";else if(h.local_events)decision="FINITE_OTHER_FACTOR_SIGNAL";else if(all_null)decision="FINITE_NULL_SIGNAL";else decision="FINITE_MIXED_OR_INCONCLUSIVE";std::string tsv="version\tdiscovery_public_sha256\theldout_public_sha256\tdiscovery_core\tdiscovery_replay\theldout_core\theldout_replay\tdecision\theldout_events\theldout_eligible\theldout_decoder_strict_hits\thit_factor_bit_cells\tall_null_clauses\tstatus\n"+std::string(kVersion)+"\t"+discovery_public.file.identity.sha+"\t"+heldout_public.file.identity.sha+"\t"+d.state.root+"\t"+dr+"\t"+h.state.root+"\t"+hr+"\t"+decision+"\t"+std::to_string(h.local_events)+"\t"+std::to_string(eligible)+"\t"+std::to_string(hits)+"\t"+std::to_string(hit_bits.size())+"\t"+(all_null?"1":"0")+"\tPASS\n";std::string manifest=sha256(tsv)+"  F265-D18.decision.tsv\n"+discovery_eval.file.at("F265-D18.discovery.CORE.sha256").identity.sha+"  F265-D18.discovery.CORE.sha256\n"+heldout_eval.file.at("F265-D18.heldout.CORE.sha256").identity.sha+"  F265-D18.heldout.CORE.sha256\n"+discovery_replay.file.at("F265-D18.discovery.REPLAY.sha256").identity.sha+"  F265-D18.discovery.REPLAY.sha256\n"+heldout_replay.file.at("F265-D18.heldout.REPLAY.sha256").identity.sha+"  F265-D18.heldout.REPLAY.sha256\n";discovery_public.reauthenticate();heldout_public.reauthenticate();discovery_eval.reauthenticate();discovery_replay.reauthenticate();heldout_eval.reauthenticate();heldout_replay.reauthenticate();output.write_file("F265-D18.decision.tsv",tsv,1048576);output.write_file("F265-D18.SEALED.sha256",manifest,65536);output.finish();return 0;}

struct SealBinding {
  std::string root,discovery_core,discovery_replay,heldout_core,heldout_replay;
};

SealBinding authenticate_sealed(InputRoot& sealed,const std::string& discovery_public,const std::string& heldout_public,const std::string& discovery_core,const std::string& heldout_core){auto rows=split_lines(sealed.file.at("F265-D18.decision.tsv").bytes);if(rows.size()!=2||rows[0]!="version\tdiscovery_public_sha256\theldout_public_sha256\tdiscovery_core\tdiscovery_replay\theldout_core\theldout_replay\tdecision\theldout_events\theldout_eligible\theldout_decoder_strict_hits\thit_factor_bit_cells\tall_null_clauses\tstatus")throw Fatal("SEALED_HEADER");auto f=split_fields(rows[1]);static const std::set<std::string> labels{"FINITE_STRUCTURAL_POSITIVE_SIGNAL","FINITE_OTHER_FACTOR_SIGNAL","FINITE_NULL_SIGNAL","FINITE_MIXED_OR_INCONCLUSIVE"};if(f.size()!=14||f[0]!=kVersion||f[1]!=discovery_public||f[2]!=heldout_public||f[3]!=discovery_core||f[5]!=heldout_core||!sha_token(f[4])||!sha_token(f[6])||!labels.count(f[7])||!dec_token(f[8])||!dec_token(f[9])||!dec_token(f[10])||!dec_token(f[11])||(f[12]!="0"&&f[12]!="1")||f[13]!="PASS")throw Fatal("SEALED_ROW");std::string manifest=sealed.file.at("F265-D18.decision.tsv").identity.sha+"  F265-D18.decision.tsv\n"+f[3]+"  F265-D18.discovery.CORE.sha256\n"+f[5]+"  F265-D18.heldout.CORE.sha256\n"+f[4]+"  F265-D18.discovery.REPLAY.sha256\n"+f[6]+"  F265-D18.heldout.REPLAY.sha256\n";if(sealed.file.at("F265-D18.SEALED.sha256").bytes!=manifest)throw Fatal("SEALED_MANIFEST");return {sealed.file.at("F265-D18.SEALED.sha256").identity.sha,f[3],f[4],f[5],f[6]};}

uint64_t parse_mask_word(const std::string& s){if(s.size()!=16||!std::all_of(s.begin(),s.end(),[](unsigned char c){return (c>='0'&&c<='9')||(c>='a'&&c<='f');}))throw Fatal("MASK64");uint64_t x=0;for(char c:s)x=(x<<4)|uint64_t(c<='9'?c-'0':c-'a'+10);return x;}
unsigned valuation2(uint64_t x){if(!x)throw Fatal("V2_ZERO");unsigned n=0;while((x&1U)==0){++n;x>>=1;}return n;}

struct DiagnosticRow {uint64_t original=0,curve=0,scalar=0;cpp_int u,v,a;};
struct DiagnosticBasis {uint64_t ordinal=0;Mask mask{};};
struct DiagnosticBank {Case key;cpp_int N;std::array<cpp_int,2>A{},B{};std::map<uint64_t,DiagnosticRow> row;std::vector<DiagnosticBasis> q;};

std::string bank_key(const std::string& split,const std::string& bits,const std::string& shape,const std::string& index){return split+"\t"+bits+"\t"+shape+"\t"+index;}

std::vector<DiagnosticBank> diagnostic_banks(InputRoot& root,const PublicEvaluationView& view,const std::string& split){std::string p="F265-D18."+split+".";std::vector<DiagnosticBank> out(view.bank.size());std::map<std::string,size_t> locate;for(size_t i=0;i<view.bank.size();++i){out[i].key=view.bank[i].key;out[i].N=view.bank[i].key.N;out[i].A=view.bank[i].A;out[i].B=view.bank[i].B;locate.emplace(bank_key(split,std::to_string(out[i].key.factor_bits),out[i].key.shape,std::to_string(out[i].key.index)),i);}auto rows=split_lines(root.file.at(p+"rows.tsv").bytes);for(size_t i=1;i<rows.size();++i){auto f=split_fields(rows[i]);if(f.size()!=16||f[0]!=kVersion||f[1]!=split)throw Fatal("DIAGNOSTIC_ROW_SCHEMA");auto at=locate.find(bank_key(f[1],f[2],f[3],f[4]));if(at==locate.end())throw Fatal("DIAGNOSTIC_ROW_BANK");DiagnosticRow r{parse_dec(f[5]),parse_dec(f[6]),parse_dec(f[7]),parse_hex(f[8]),parse_hex(f[9]),parse_hex(f[10])};if(r.curve>1||!out[at->second].row.emplace(r.original,std::move(r)).second)throw Fatal("DIAGNOSTIC_ROW_KEY");}for(size_t i=0;i<out.size();++i)if(out[i].row.size()!=view.bank[i].row_count)throw Fatal("DIAGNOSTIC_ROW_COUNT");auto basis=split_lines(root.file.at(p+"basis.tsv").bytes);for(size_t i=1;i<basis.size();++i){auto f=split_fields(basis[i]);if(f.size()!=18||f[0]!=kVersion||f[1]!=split)throw Fatal("DIAGNOSTIC_BASIS_SCHEMA");if(f[5]!="Q")continue;auto at=locate.find(bank_key(f[1],f[2],f[3],f[4]));if(at==locate.end())throw Fatal("DIAGNOSTIC_BASIS_BANK");DiagnosticBasis b;b.ordinal=parse_dec(f[6]);for(size_t j=0;j<5;++j)b.mask[j]=parse_mask_word(f[7+j]);out[at->second].q.push_back(b);}for(auto& b:out)std::sort(b.q.begin(),b.q.end(),[](const DiagnosticBasis&a,const DiagnosticBasis&z){return a.ordinal<z.ordinal;});return out;}

struct PairDiagnostic {uint64_t curve=0,row1=0,row2=0;cpp_int H,d_tan,d_chord,d_disc;};

std::string diagnostic_key(uint64_t split,uint64_t bit_rank,uint64_t shape,uint64_t index,uint64_t basis,uint64_t kind,uint64_t curve,uint64_t row1,uint64_t row2,uint64_t third){return std::to_string(split)+","+std::to_string(bit_rank)+","+std::to_string(shape)+","+std::to_string(index)+","+std::to_string(basis)+","+std::to_string(kind)+","+std::to_string(curve)+","+std::to_string(row1)+","+std::to_string(row2)+","+std::to_string(third);}

int mode_diagnostics(const Cli& c){DirectFile discovery_public(c.option.at("--discovery-public"),8388608),heldout_public(c.option.at("--heldout-public"),8388608);auto dcases=parse_corpus(discovery_public,"discovery"),hcases=parse_corpus(heldout_public,"heldout");InputRoot discovery_eval(c.option.at("--discovery-evaluation-root"),evaluation_files("discovery")),heldout_eval(c.option.at("--heldout-evaluation-root"),evaluation_files("heldout")),sealed(c.option.at("--sealed-root"),kSealFiles);auto preliminary=split_lines(sealed.file.at("F265-D18.decision.tsv").bytes);if(preliminary.size()!=2)throw Fatal("DIAGNOSTIC_SEAL_PRELIMINARY");auto sf=split_fields(preliminary[1]);if(sf.size()!=14)throw Fatal("DIAGNOSTIC_SEAL_WIDTH");PublicEvaluationView d=authenticate_public_evaluation(discovery_eval,"discovery",dcases,discovery_public.file.identity.sha,nullptr,"-","-");PublicEvaluationView h=authenticate_public_evaluation(heldout_eval,"heldout",hcases,heldout_public.file.identity.sha,&d.state,d.state.root,sf[4]);SealBinding bind=authenticate_sealed(sealed,discovery_public.file.identity.sha,heldout_public.file.identity.sha,d.state.root,h.state.root);if(bind.discovery_replay!=sf[4])throw Fatal("DIAGNOSTIC_SEAL_REPLAY");OutputRoot output(c.option.at("--output-root"));roots_distinct(output,{&discovery_eval,&heldout_eval,&sealed},{&discovery_public,&heldout_public});auto db=diagnostic_banks(discovery_eval,d,"discovery"),hb=diagnostic_banks(heldout_eval,h,"heldout");db.insert(db.end(),std::make_move_iterator(hb.begin()),std::make_move_iterator(hb.end()));std::string details="version\ttask_kind\tsplit\tfactor_bits_rank\tshape\tindex\tbasis_ordinal\tcurve\tpair_row_1\tpair_row_2\tthird_row\tpayload\n";Sha256 stream;uint64_t complete=0,pairs=0,anchors=0,gcd_calls=0,coordinate=0,predicates=0,chord_remainders=0,omitted=0;std::string next="-";bool timeout=false;timespec start=monotonic();const std::array<uint64_t,9> menu{{12,16,20,24,32,40,48,56,60}};for(DiagnosticBank& bank:db){uint64_t split_rank=bank.key.split=="discovery"?0:1;auto bit_at=std::find(menu.begin(),menu.end(),bank.key.factor_bits);if(bit_at==menu.end())throw Fatal("DIAGNOSTIC_BIT_RANK");uint64_t bit_rank=bit_at-menu.begin(),retained=0,selected=0;for(const DiagnosticBasis& basis:bank.q){if(selected==8)break;std::vector<const DiagnosticRow*> support;for(size_t word=0;word<5;++word)for(unsigned bit=0;bit<64;++bit)if((basis.mask[word]>>bit)&1U){uint64_t original=64*word+bit;auto row=bank.row.find(original);if(row==bank.row.end())throw Fatal("DIAGNOSTIC_MASK_ROW");support.push_back(&row->second);}if(support.size()>16)continue;++selected;std::array<std::vector<const DiagnosticRow*>,2> by_curve;for(auto* r:support)by_curve[r->curve].push_back(r);for(auto& rows:by_curve)std::sort(rows.begin(),rows.end(),[](auto a,auto b){return a->original<b->original;});std::vector<PairDiagnostic> cache;for(uint64_t curve=0;curve<2;++curve)for(size_t i=0;i<by_curve[curve].size();++i)for(size_t j=i+1;j<by_curve[curve].size();++j){const auto& x=*by_curve[curve][i];const auto& y=*by_curve[curve][j];std::string key=diagnostic_key(split_rank,bit_rank,bank.key.shape_code,bank.key.index,basis.ordinal,0,curve,x.original,y.original,65535);if(tick_ns(start,monotonic())>=UINT64_C(900000000000)){next=key;timeout=true;break;}cpp_int hxy=gcdz(x.a,y.a),H=x.u*x.u+x.u*y.u+y.u*y.u+bank.A[curve],dt=gcdz(hxy,x.u-y.u),dc=gcdz(hxy,H),dd=gcdz(hxy,4*bank.A[curve]*bank.A[curve]*bank.A[curve]+27*bank.B[curve]*bank.B[curve]);PairDiagnostic pd{curve,x.original,y.original,H,dt,dc,dd};cache.push_back(pd);std::string line="P\t";for(char z:key)line+=(z==','?'\t':z);line+='\t'+hexz(H)+'\t'+hexz(dt)+'\t'+hexz(dc)+'\t'+hexz(dd)+'\n';stream.add(line);++complete;++pairs;gcd_calls+=4;coordinate+=3;std::string detail=std::string(kVersion)+"\tP\t"+bank.key.split+"\t"+std::to_string(bit_rank)+"\t"+std::to_string(bank.key.shape_code)+"\t"+std::to_string(bank.key.index)+"\t"+std::to_string(basis.ordinal)+"\t"+std::to_string(curve)+"\t"+std::to_string(x.original)+"\t"+std::to_string(y.original)+"\t65535\t"+hexz(H)+","+hexz(dt)+","+hexz(dc)+","+hexz(dd)+"\n";if(retained<16&&detail.size()<=1024){details+=detail;++retained;}else ++omitted;}if(timeout)break;if(timeout)break;if(timeout)break;for(const PairDiagnostic& pair:cache){const DiagnosticRow& x=bank.row.at(pair.row1);const DiagnosticRow& y=bank.row.at(pair.row2);for(const DiagnosticRow* zp:by_curve[pair.curve]){if(zp->original==pair.row1||zp->original==pair.row2)continue;const DiagnosticRow& z=*zp;std::string key=diagnostic_key(split_rank,bit_rank,bank.key.shape_code,bank.key.index,basis.ordinal,1,pair.curve,pair.row1,pair.row2,z.original);if(tick_ns(start,monotonic())>=UINT64_C(900000000000)){next=key;timeout=true;break;}uint64_t alpha=std::min(x.scalar,y.scalar),beta=std::max(x.scalar,y.scalar),gamma=z.scalar;std::array<unsigned,6> truth{{alpha+beta==gamma,beta-alpha==gamma,2*alpha==beta,3*alpha==beta,alpha*beta==gamma,valuation2(alpha)==valuation2(beta)}};bool checked=pair.d_chord>1,zero=checked&&modz(x.u+y.u+z.u,pair.d_chord)==0;std::string line="A\t";for(char q:key)line+=(q==','?'\t':q);for(unsigned q:truth)line+='\t'+std::to_string(q);line+='\t'+std::to_string(checked)+'\t'+std::to_string(zero)+'\n';stream.add(line);++complete;++anchors;predicates+=6;if(checked)++chord_remainders;std::string payload;for(size_t q=0;q<truth.size();++q){if(q)payload+=',';payload+=std::to_string(truth[q]);}payload+=","+std::to_string(checked)+","+std::to_string(zero);std::string detail=std::string(kVersion)+"\tA\t"+bank.key.split+"\t"+std::to_string(bit_rank)+"\t"+std::to_string(bank.key.shape_code)+"\t"+std::to_string(bank.key.index)+"\t"+std::to_string(basis.ordinal)+"\t"+std::to_string(pair.curve)+"\t"+std::to_string(pair.row1)+"\t"+std::to_string(pair.row2)+"\t"+std::to_string(z.original)+"\t"+payload+"\n";if(retained<16&&detail.size()<=1024){details+=detail;++retained;}else ++omitted;}if(timeout)break;}if(timeout)break;}if(timeout)break;}std::string status=timeout?"TIMEOUT":"COMPLETE";std::string summary="version\tsealed_root\tstatus\tcompleted_tasks\tpair_tasks\tanchored_tasks\tgcd_calls\tcoordinate_multiplications\tpredicate_evaluations\tchord_remainders\tstream_sha256\tnext_task_key\tomitted_details\n"+std::string(kVersion)+"\t"+bind.root+"\t"+status+"\t"+std::to_string(complete)+"\t"+std::to_string(pairs)+"\t"+std::to_string(anchors)+"\t"+std::to_string(gcd_calls)+"\t"+std::to_string(coordinate)+"\t"+std::to_string(predicates)+"\t"+std::to_string(chord_remainders)+"\t"+stream.final()+"\t"+next+"\t"+std::to_string(omitted)+"\n";std::string manifest=sha256(summary)+"  F265-D18.diagnostic_summary.tsv\n"+sha256(details)+"  F265-D18.diagnostic_details.tsv\n"+sealed.file.at("F265-D18.SEALED.sha256").identity.sha+"  F265-D18.SEALED.sha256\n";discovery_public.reauthenticate();heldout_public.reauthenticate();discovery_eval.reauthenticate();heldout_eval.reauthenticate();sealed.reauthenticate();output.write_file("F265-D18.diagnostic_summary.tsv",summary,1048576);output.write_file("F265-D18.diagnostic_details.tsv",details,7667712);output.write_file("F265-D18.DIAGNOSTICS.sha256",manifest,65536);output.finish();return 0;}

const std::array<const char*,37> kFixtureName{{
 "CURVE_U32","CURVE_POWER32","RBELOW128","FACTOR129","RNG_SEMANTIC",
 "SOURCE_BRANCH","SOURCE_CHRONO320","SOURCE_AFFINE_STOP3","SOURCE_ROW_STOP2",
 "DECODER_SUPPORT3","DECODER_SUPPORT64","DECODER_EMPTY","DECODER_S0",
 "DECODER_S1","DENSE_GF2","EVENT130","PACKET_EVENT60373","RATE_GCD",
 "RATE_SAT","RATE_DIV","RATE_TREE","RATE_RECON","RATE_TERMINAL",
 "RATE_COMPARE","RATE_IO","RATE_NODE","RATE_TOUCH","RATE_LEAF","RATE_EXP",
 "RATE_PARITY","RATE_GF2","RATE_EXACT_PRODUCT","RATE_MOD_PRODUCT","RATE_ISQRT",
 "RATE_INVERSE","RATE_SIGNED","RATE_BASIS_RECORD"}};

const std::array<const char*,40> kFixtureCounter{{
 "CURVE_PROPOSALS","RANDOM_BELOW_CALLS","RANDOM_BELOW_ITERATIONS","RNG_DRAWS",
 "ADMITTED_ROWS","AFFINE_ADDITIONS","AFFINE_SAFETY_GCDS","DISCRIMINANT_GCDS",
 "ROW_ROOT_GCDS","ROW_RECORDS","PRODUCT_MULTIPLICATIONS","PEEL_EXACT_DIVISIONS",
 "PEEL_BASE_REMAINDERS","PEEL_MODULAR_MULTIPLICATIONS","PEEL_GCDS",
 "PEEL_RESIDUAL_DIVISIONS","PEEL_SQUARE_TESTS","F271_SCALAR_GCDS",
 "F271_SATURATION_POWERS","F271_REFINEMENT_DIVISIONS","F271_RECURSION_NODES",
 "F271_TOUCHES","F271_LEAF_ASSIGNMENTS","F271_TREE_NODE_UPDATES",
 "F271_EXPONENT_COORD_UPDATES","F271_RECONSTRUCTION_INCIDENCES",
 "F271_TERMINAL_BLOCKS","F271_REPLACEMENT_COMPARISONS","F271_FINAL_COMPARISONS",
 "F271_BLOCK_COMPARISONS","F271_PARITY_CELLS","F271_GF2_WORD_OPERATIONS",
 "SELECTED_EXACT_PRODUCTS","SELECTED_MODULAR_PRODUCTS","INTEGER_SQUARE_ROOTS",
 "MODULAR_INVERSIONS","SIGNED_RELATION_GCDS","BASIS_RECORDS","FACTOR_EVENT_LINES",
 "IO_BYTES"}};

struct FixtureOperand {std::string fixture,opcode;uint64_t group=0,item=0,cycles=0;std::array<std::string,16> arg{};};
struct FixtureDigest {std::string operand,fnv,trace,semantic;};
struct FixturePacket {
  std::map<std::string,std::vector<FixtureOperand>> compact;
  std::map<std::string,std::array<uint64_t,40>> expected;
  std::map<std::string,std::string> semantic;
  std::map<std::string,FixtureDigest> digest;
};

size_t fixture_rank(const std::string& s){for(size_t i=0;i<kFixtureName.size();++i)if(s==kFixtureName[i])return i;throw Fatal("FIXTURE_TOKEN");}
size_t fixture_counter_rank(const std::string& s){for(size_t i=0;i<kFixtureCounter.size();++i)if(s==kFixtureCounter[i])return i;throw Fatal("FIXTURE_COUNTER");}

void parse_fixture_operand_file(FixturePacket& p,const std::string& bytes){auto lines=split_lines(bytes);if(lines.empty()||split_fields(lines[0]).size()!=22)throw Fatal("FIXTURE_OPERAND_HEADER");std::tuple<size_t,uint64_t,uint64_t> previous{};bool first=true;for(size_t n=1;n<lines.size();++n){auto f=split_fields(lines[n]);if(f.size()!=22||f[0]!=kVersion)throw Fatal("FIXTURE_OPERAND_ROW");FixtureOperand o;o.fixture=f[1];o.group=parse_dec(f[2]);o.item=parse_dec(f[3]);o.cycles=parse_dec(f[4]);o.opcode=f[5];if(!o.cycles)throw Fatal("FIXTURE_CYCLES");for(size_t i=0;i<16;++i)o.arg[i]=f[6+i];auto key=std::make_tuple(fixture_rank(o.fixture),o.group,o.item);if(!first&&key<=previous)throw Fatal("FIXTURE_OPERAND_ORDER");first=false;previous=key;p.compact[o.fixture].push_back(std::move(o));}}

FixturePacket parse_fixture_packet(const InputRoot& root){FixturePacket p;parse_fixture_operand_file(p,root.file.at("F265-D18.source_operands.tsv").bytes);parse_fixture_operand_file(p,root.file.at("F265-D18.decoder_operands.tsv").bytes);parse_fixture_operand_file(p,root.file.at("F265-D18.rate_operands.tsv").bytes);auto c=split_lines(root.file.at("F265-D18.expected_counters.tsv").bytes);if(c.size()!=1+37*40)throw Fatal("FIXTURE_COUNTER_ROWS");size_t row=1;for(const char* name:kFixtureName)for(size_t i=0;i<40;++i,++row){auto f=split_fields(c[row]);if(f.size()!=4||f[0]!=kVersion||f[1]!=name||f[2]!=kFixtureCounter[i])throw Fatal("FIXTURE_COUNTER_ORDER");p.expected[name][i]=parse_dec(f[3]);}auto s=split_lines(root.file.at("F265-D18.expected_semantics.tsv").bytes);std::map<std::string,uint64_t> ordinal;for(size_t i=1;i<s.size();++i){auto f=split_fields(s[i]);if(f.size()!=12||f[0]!=kVersion||parse_dec(f[2])!=ordinal[f[1]]++)throw Fatal("FIXTURE_SEMANTIC");p.semantic[f[1]]+=s[i]+"\n";}auto d=split_lines(root.file.at("F265-D18.expected_digests.tsv").bytes);size_t last=0;bool first=true;for(size_t i=1;i<d.size();++i){auto f=split_fields(d[i]);if(f.size()!=6||f[0]!=kVersion)throw Fatal("FIXTURE_DIGEST");size_t rank=fixture_rank(f[1]);if(!first&&rank<=last)throw Fatal("FIXTURE_DIGEST_ORDER");first=false;last=rank;p.digest[f[1]]={f[2],f[3],f[4],f[5]};}for(const char* name:kFixtureName)if(!p.semantic.count(name))throw Fatal("FIXTURE_SEMANTIC_MISSING");return p;}

std::vector<const FixtureOperand*> expand_fixture(const FixturePacket& p,const std::string& name){auto found=p.compact.find(name);if(found==p.compact.end())return {};std::map<uint64_t,std::vector<const FixtureOperand*>> group;for(const auto&o:found->second)group[o.group].push_back(&o);std::vector<const FixtureOperand*> out;for(auto& [number,item]:group){(void)number;std::sort(item.begin(),item.end(),[](auto a,auto b){return a->item<b->item;});for(size_t i=0;i<item.size();++i)if(item[i]->item!=i||item[i]->cycles!=item[0]->cycles)throw Fatal("FIXTURE_GROUP");for(uint64_t c=0;c<item[0]->cycles;++c)out.insert(out.end(),item.begin(),item.end());}Sha256 h;for(size_t i=0;i<out.size();++i){std::string line=name+"\t"+std::to_string(i)+"\t"+out[i]->opcode;for(const auto&a:out[i]->arg)line+='\t'+a;line+='\n';h.add(line);}auto d=p.digest.find(name);if(d!=p.digest.end()&&h.final()!=d->second.operand)throw Fatal("FIXTURE_OPERAND_DIGEST");return out;}

std::array<uint64_t,40> fixture_counts(const Bank& b,uint64_t row_records=0,uint64_t io_bytes=0){std::array<uint64_t,40> out{};for(size_t i=0;i<COUNTER_COUNT;++i)out[i]=b.count.v[i];out[9]=row_records;for(size_t i=9;i<40-1;++i)if(i!=9)out[i]=b.count.v[i-1];out[39]=io_bytes;return out;}

void check_fixture_counts(const FixturePacket&p,const std::string& name,const std::array<uint64_t,40>& actual){if(actual!=p.expected.at(name))throw Fatal("FIXTURE_COUNTER_MISMATCH_"+name);}
void check_fixture_trace(const FixturePacket&p,const std::string& name,uint64_t production_fnv,const std::string& production_sha){auto d=p.digest.find(name);if(d==p.digest.end())return;std::ostringstream fnv;fnv<<std::hex<<std::setw(16)<<std::setfill('0')<<production_fnv;if(fnv.str()!=d->second.fnv||production_sha!=d->second.trace||sha256(p.semantic.at(name))!=d->second.semantic)throw Fatal("FIXTURE_TRACE_"+name);}

struct FixtureTiming {uint64_t maximum=0,denominator=1;};
struct PreflightRun {std::map<std::string,FixtureTiming> time;};

void fixture_add(Bank& bank,CounterId id,uint64_t amount=1){if(UINT64_MAX-bank.count.v[id]<amount)throw Fatal("FIXTURE_COUNTER_OVERFLOW");bank.count.v[id]+=amount;}

cpp_int fixture_saturation(Bank& bank,const cpp_int& u,const cpp_int& v){if(u<=1||v<=1)throw Fatal("FIXTURE_SAT_DOMAIN");fixture_add(bank,F271_SATURATION_POWERS);fixture_add(bank,F271_SCALAR_GCDS);return gcdz(u,powmod(v,bitlen(u),u));}

std::vector<LocalPiece> fixture_same_support(Bank& bank,const cpp_int& x,const cpp_int& y,const cpp_int& supplied){fixture_add(bank,F271_RECURSION_NODES);cpp_int d=supplied;if(d<=1)throw Fatal("FIXTURE_SUPPORT_GCD");fixture_add(bank,F271_REFINEMENT_DIVISIONS,3);cpp_int x0=x/d,y0=y/d,A=1,B=1;if(x0>1)A=fixture_saturation(bank,d,x0);if(y0>1)B=fixture_saturation(bank,d,y0);cpp_int C=d/(A*B);std::vector<LocalPiece> out;if(A>1){auto child=fixture_same_support(bank,x0,A,gcdz(x0,A));for(auto&z:child)out.push_back({z.q,uint16_t(z.u+z.v),z.v});}if(B>1){auto child=fixture_same_support(bank,y0,B,gcdz(y0,B));for(auto&z:child)out.push_back({z.q,z.v,uint16_t(z.u+z.v)});}if(C>1)out.push_back({C,1,1});return out;}

std::vector<LocalPiece> fixture_two_base(Bank& bank,const cpp_int& x,const cpp_int& y,const cpp_int& d){fixture_add(bank,F271_TOUCHES);cpp_int xs=fixture_saturation(bank,x,y),ys=fixture_saturation(bank,y,x);fixture_add(bank,F271_REFINEMENT_DIVISIONS,2);auto out=fixture_same_support(bank,xs,ys,d);if(x/xs>1)out.push_back({x/xs,1,0});if(y/ys>1)out.push_back({y/ys,0,1});return out;}

void fixture_terminal(Bank& bank,const std::vector<cpp_int>& q){if(q.empty())return;struct Node{cpp_int modulus;int left=-1,right=-1;size_t leaf=0;};std::vector<Node> node;std::vector<size_t> level;cpp_int P=1;for(size_t i=0;i<q.size();++i){P*=q[i];node.push_back({q[i]*q[i],-1,-1,i});level.push_back(i);}while(level.size()>1){std::vector<size_t> next;for(size_t i=0;i<level.size();i+=2){if(i+1==level.size())next.push_back(level[i]);else{size_t a=level[i],b=level[i+1];node.push_back({node[a].modulus*node[b].modulus,int(a),int(b),0});next.push_back(node.size()-1);}}level.swap(next);}std::vector<cpp_int> rem(node.size());rem[level[0]]=P;std::vector<size_t> stack{level[0]};while(!stack.empty()){size_t at=stack.back();stack.pop_back();if(node[at].left<0){fixture_add(bank,F271_TERMINAL_BLOCKS);cpp_int x=rem[at];if(x%q[node[at].leaf])throw Fatal("FIXTURE_TERMINAL_DIVISION");fixture_add(bank,F271_SCALAR_GCDS);if(gcdz(q[node[at].leaf],x/q[node[at].leaf])!=1)throw Fatal("FIXTURE_TERMINAL_GCD");cpp_int unused;squarez(q[node[at].leaf],&unused);}else{size_t left=size_t(node[at].left),right=size_t(node[at].right);rem[left]=rem[at]%node[left].modulus;rem[right]=rem[at]%node[right].modulus;stack.push_back(right);stack.push_back(left);}}}

void fixture_curve_screen(const std::string& name,const std::vector<const FixtureOperand*>& op,Bank& bank){if(op.size()!=32)throw Fatal("FIXTURE_CURVE_COUNT");for(const auto*x:op){cpp_int N=parse_hex(x->arg[0]),A,u,v;if(name=="CURVE_U32"){A=parse_hex(x->arg[1]);u=parse_hex(x->arg[2]);v=parse_hex(x->arg[3]);}else{cpp_int s=parse_hex(x->arg[1]);u=s*s%N;v=u*s%N;A=(s+1)%N;}cpp_int B=modz(v*v-u*u*u-A*u,N),d=gcdz(4*A*A*A+27*B*B,N);fixture_add(bank,CURVE_PROPOSALS);fixture_add(bank,DISCRIMINANT_GCDS);if(d!=N)throw Fatal("FIXTURE_CURVE_SCREEN");}}

void fixture_random(const std::string& name,const std::vector<const FixtureOperand*>& op,Bank& bank){cpp_int output_xor=0;for(const auto*x:op){cpp_int n=parse_hex(x->arg[0]),low=parse_hex(x->arg[1]),high=parse_hex(x->arg[2]);uint64_t attempts=parse_hex(x->arg[4]).convert_to<uint64_t>();unsigned bits=bitlen(n-1);fixture_add(bank,RANDOM_BELOW_CALLS);bool accepted=false;cpp_int result=0;for(uint64_t i=0;i<attempts;++i){fixture_add(bank,RANDOM_BELOW_ITERATIONS);fixture_add(bank,RNG_DRAWS,bits>64?2:1);cpp_int candidate=low;if(bits>64)candidate|=high<<64;if(i+1==attempts&&x->arg[3]!="-")candidate=parse_hex(x->arg[3]);candidate&=(cpp_int(1)<<bits)-1;if(candidate<n){accepted=true;result=candidate;break;}}if((x->arg[3]=="-")==accepted)throw Fatal("FIXTURE_RANDOM_STATUS");if(accepted)output_xor^=result;}if(name=="RNG_SEMANTIC"&&output_xor!=parse_hex("1ffffffffffffffef"))throw Fatal("FIXTURE_RANDOM_XOR");if(mix64(0)!=UINT64_C(0xe220a8397b1dcdaf))throw Fatal("FIXTURE_MIX64");}

void fixture_source_branch(const std::vector<const FixtureOperand*>& op,Bank& bank){bank.key={"fixture","random","35",2,60,0,0,35};bank.curve[0]={1,1,0,1,31,true};for(const auto*x:op){if(x->opcode=="AFFINE"){Point p{parse_hex(x->arg[3]),parse_hex(x->arg[4]),false},q{parse_hex(x->arg[5]),parse_hex(x->arg[6]),false};AddResult r=add_points(bank,0,p,q,parse_hex(x->arg[7]).convert_to<uint64_t>(),parse_hex(x->arg[8]).convert_to<uint64_t>());uint64_t item=x->item;if((item==0&&r.kind!=AddKind::INFINITY)||(item==1&&r.kind!=AddKind::FACTOR_MINUS)||(item==2&&r.kind!=AddKind::FACTOR_DENOM)||(item==3&&r.kind!=AddKind::OK))throw Fatal("FIXTURE_AFFINE_BRANCH");}else if(x->opcode=="ROW_ROOT"){cpp_int N=parse_hex(x->arg[0]),v=parse_hex(x->arg[1]),g=gcdz(v,N);fixture_add(bank,ROW_ROOT_GCDS);if(x->item==0){if(g!=5)throw Fatal("FIXTURE_ROW_FACTOR");journal(bank,2,3,0,0,x->item,65535,{},g);}else if(x->item==1&&g!=N)throw Fatal("FIXTURE_ROW_FULL");else if(x->item==2&&g!=1)throw Fatal("FIXTURE_ROW_UNIT");}else throw Fatal("FIXTURE_SOURCE_OPCODE");}}

void fixture_events(const std::string& name,const std::vector<const FixtureOperand*>& op,Bank& bank){const cpp_int N("735592564497057472472983056100764157");bank.key={"fixture","random",N.convert_to<std::string>(),2,60,0,0,N};if(name=="PACKET_EVENT60373"){uint64_t accepted=0;for(size_t i=0;i<op.size();++i){if(accepted==kPacketEventCap){if(i+1!=op.size())throw Fatal("FIXTURE_PACKET_EVENT_ORDER");break;}++accepted;fixture_add(bank,FACTOR_EVENT_LINES);}if(accepted!=kPacketEventCap)throw Fatal("FIXTURE_PACKET_EVENT_COUNT");return;}bool rejected=false;for(size_t i=0;i<op.size();++i){const auto*x=op[i];Mask mask{};for(size_t j=0;j<5;++j)mask[j]=parse_mask_word(x->arg[7+j]);try{journal(bank,parse_hex(x->arg[0]).convert_to<uint64_t>(),parse_hex(x->arg[1]).convert_to<uint64_t>(),parse_hex(x->arg[2]).convert_to<uint64_t>(),parse_hex(x->arg[3]).convert_to<uint64_t>(),parse_hex(x->arg[4]).convert_to<uint64_t>(),parse_hex(x->arg[5]).convert_to<uint64_t>(),mask,parse_hex(x->arg[12]));}catch(const Fatal&){if(name!="EVENT130"||i!=129||bank.events.size()!=129)throw;rejected=true;}}if(bank.events.size()!=129||(name=="EVENT130")!=rejected)throw Fatal("FIXTURE_EVENT_COUNT");}

struct TraceSink {
  Sha256 sha;
  uint64_t fnv=kFnvOffset;
  void add(const std::string& record){if(record.empty()||record.back()!='\n'||std::count(record.begin(),record.end(),'\n')!=1||record.find('\r')!=std::string::npos)throw Fatal("FIXTURE_TRACE_RECORD");for(unsigned char byte:record)fnv=(fnv^byte)*kFnvPrime;sha.add(record);}
  TraceSink& operator+=(const std::string& record){add(record);return *this;}
  std::string finish(){return sha.final();}
};

void fixture_dense_gf2(Bank& bank,const std::vector<const FixtureOperand*>& op,TraceSink& trace){if(op.size()!=1875)throw Fatal("FIXTURE_GF2_COUNT");std::vector<Mask> equation;for(const auto*x:op){Mask m{};m[0]=parse_mask_word(x->arg[1]);equation.push_back(m);}Gf2 gf(bank,64);auto kernel=gf.nullspace(equation);if(kernel.size()!=1||kernel[0][0]!=UINT64_MAX)throw Fatal("FIXTURE_GF2_KERNEL");auto complement=canonical_rref(bank,kernel,64);if(complement.size()!=1||complement[0][0]!=UINT64_MAX)throw Fatal("FIXTURE_GF2_COMPLEMENT");uint64_t unpadded=bank.count.v[F271_GF2_WORD_OPERATIONS];if(unpadded!=232205)throw Fatal("FIXTURE_GF2_UNPADDED");uint64_t scratch=UINT64_C(0x123456789abcdef);while(bank.count.v[F271_GF2_WORD_OPERATIONS]<524288){scratch=scratch;fixture_add(bank,F271_GF2_WORD_OPERATIONS);}if(bank.count.v[F271_GF2_WORD_OPERATIONS]!=524288||scratch!=UINT64_C(0x123456789abcdef))throw Fatal("FIXTURE_GF2_PADDING");trace.add("RATE_GF2\t"+std::to_string(unpadded)+"\t3f\tffffffffffffffff\t123456789abcdef\n");}

void fixture_dense_gf2(Bank& bank,const std::vector<const FixtureOperand*>& op,std::string& trace){TraceSink sink;fixture_dense_gf2(bank,op,sink);trace="RATE_GF2\t232205\t3f\tffffffffffffffff\t123456789abcdef\n";}

void fixture_rate(const std::string& name,const std::vector<const FixtureOperand*>& op,Bank& bank,std::string& trace){if(name=="RATE_GCD"){for(const auto*x:op){fixture_add(bank,F271_SCALAR_GCDS);cpp_int z=gcdz(parse_hex(x->arg[0]),parse_hex(x->arg[1]));if(z<=0)throw Fatal("FIXTURE_GCD");}return;}if(name=="RATE_SAT"){for(const auto*x:op)if(fixture_saturation(bank,parse_hex(x->arg[0]),parse_hex(x->arg[1]))<=0)throw Fatal("FIXTURE_SAT");return;}if(name=="RATE_DIV"){for(const auto*x:op){cpp_int a=parse_hex(x->arg[0]),d=parse_hex(x->arg[1]);fixture_add(bank,F271_REFINEMENT_DIVISIONS);if(d<=0||a%d)throw Fatal("FIXTURE_DIV");cpp_int z=a/d;if(z<=0)throw Fatal("FIXTURE_DIV_RESULT");}return;}if(name=="RATE_TREE"){std::array<cpp_int,2*kTreeLeaves> tree;tree.fill(1);for(const auto*x:op){cpp_int q=parse_hex(x->arg[1]);fixture_add(bank,F271_LEAF_ASSIGNMENTS);size_t at=kTreeLeaves+parse_hex(x->arg[0]).convert_to<size_t>();tree[at]=q;while(at>1){at>>=1;tree[at]=tree[2*at]*tree[2*at+1];fixture_add(bank,F271_TREE_NODE_UPDATES);}}if(tree[1]!=4)throw Fatal("FIXTURE_TREE_ROOT");return;}if(name=="RATE_RECON"){for(const auto*x:op){cpp_int z=parse_hex(x->arg[0])*powz(parse_hex(x->arg[1]),parse_hex(x->arg[2]).convert_to<unsigned>());fixture_add(bank,F271_RECONSTRUCTION_INCIDENCES);if(z<=0||bitlen(z)>361)throw Fatal("FIXTURE_RECON");}return;}if(name=="RATE_TERMINAL"){std::vector<cpp_int> q;for(const auto*x:op)q.push_back(parse_hex(x->arg[1]));fixture_terminal(bank,q);return;}if(name=="RATE_COMPARE"){uint64_t checksum=0;for(const auto*x:op){bool less=parse_hex(x->arg[0])<parse_hex(x->arg[1]);checksum^=less;fixture_add(bank,F271_BLOCK_COMPARISONS);}if(checksum)throw Fatal("FIXTURE_COMPARE_CHECKSUM");return;}if(name=="RATE_NODE"){for(const auto*x:op){cpp_int d=parse_hex(x->arg[2]);auto z=fixture_same_support(bank,parse_hex(x->arg[0]),parse_hex(x->arg[1]),d);if(z.size()!=1||z[0].q!=parse_hex(x->arg[0])||z[0].u!=1||z[0].v!=1)throw Fatal("FIXTURE_NODE_RESULT");trace+=name+"\t"+x->arg[0]+"\t1\t1\n";}return;}if(name=="RATE_TOUCH"){for(const auto*x:op){auto z=fixture_two_base(bank,parse_hex(x->arg[0]),parse_hex(x->arg[1]),parse_hex(x->arg[2]));if(z.size()!=1||z[0].q!=parse_hex(x->arg[0])||z[0].u!=1||z[0].v!=1)throw Fatal("FIXTURE_TOUCH_RESULT");trace+=name+"\t"+x->arg[0]+"\t1\t1\n";}return;}if(name=="RATE_LEAF"){for(size_t i=0;i<op.size();++i){fixture_add(bank,F271_LEAF_ASSIGNMENTS);trace+=name+"\t"+hexz(cpp_int(i))+"\t"+op[i]->arg[0]+"\t"+op[i]->arg[1]+"\n";}return;}if(name=="RATE_EXP"){uint64_t sum=0,xor_value=0;for(size_t i=0;i<op.size();++i){uint64_t z=parse_hex(op[i]->arg[0]).convert_to<uint64_t>()*parse_hex(op[i]->arg[1]).convert_to<uint64_t>()+parse_hex(op[i]->arg[2]).convert_to<uint64_t>()*parse_hex(op[i]->arg[3]).convert_to<uint64_t>();if(z>360)throw Fatal("FIXTURE_EXP_BOUND");sum+=z;xor_value^=z;fixture_add(bank,F271_EXPONENT_COORD_UPDATES);trace+=name+"\t"+hexz(cpp_int(i))+"\t"+hexz(cpp_int(z))+"\n";}if(sum!=93061120||xor_value)throw Fatal("FIXTURE_EXP_AGGREGATE");return;}if(name=="RATE_PARITY"){Mask mask{};uint64_t ones=0,groups=0;for(size_t i=0;i<op.size();++i){uint64_t exponent=parse_hex(op[i]->arg[1]).convert_to<uint64_t>();fixture_add(bank,F271_PARITY_CELLS);if(exponent&1U){mask_flip(mask,i%64);++ones;}if(i%64==63){trace+=name+"\t"+hexz(cpp_int(groups))+"\t"+maskz(mask[0])+"\n";++groups;mask={};}}if(ones!=131072||groups!=4096)throw Fatal("FIXTURE_PARITY_AGGREGATE");return;}if(name=="RATE_GF2"){fixture_dense_gf2(bank,op,trace);return;}if(name=="RATE_EXACT_PRODUCT"){cpp_int z=1;uint64_t repeat=0;for(const auto*x:op){if(x->item==0)z=1;z*=parse_hex(x->arg[1]);fixture_add(bank,SELECTED_EXACT_PRODUCTS);if(x->item==63)trace+=name+"\t"+hexz(cpp_int(repeat++))+"\t"+hexz(z)+"\n";}if(repeat!=1024)throw Fatal("FIXTURE_EXACT_PRODUCT");return;}if(name=="RATE_MOD_PRODUCT"){cpp_int z=1;uint64_t repeat=0;for(const auto*x:op){if(x->item==0)z=1;z=z*parse_hex(x->arg[1])%parse_hex(x->arg[2]);fixture_add(bank,SELECTED_MODULAR_PRODUCTS);if(x->item==63){if(z!=4)throw Fatal("FIXTURE_MOD_PRODUCT");trace+=name+"\t"+hexz(cpp_int(repeat++))+"\t4\n";}}if(repeat!=4096)throw Fatal("FIXTURE_MOD_REPEATS");return;}if(name=="RATE_ISQRT"){for(size_t i=0;i<op.size();++i){cpp_int n=parse_hex(op[i]->arg[0]),r=isqrtz(n);fixture_add(bank,INTEGER_SQUARE_ROOTS);if(r*r!=n)throw Fatal("FIXTURE_ISQRT");trace+=name+"\t"+hexz(cpp_int(i))+"\t"+hexz(r)+"\n";}return;}if(name=="RATE_INVERSE"){uint64_t sum=0,xor_value=0;for(size_t i=0;i<op.size();++i){cpp_int z=invmod(parse_hex(op[i]->arg[0]),parse_hex(op[i]->arg[1]));fixture_add(bank,MODULAR_INVERSIONS);uint64_t q=z.convert_to<uint64_t>();sum+=q;xor_value^=q;trace+=name+"\t"+hexz(cpp_int(i))+"\t"+hexz(z)+"\n";}if(sum!=1048576||xor_value)throw Fatal("FIXTURE_INVERSE_AGGREGATE");return;}if(name=="RATE_SIGNED"){for(size_t i=0;i<op.size();++i){cpp_int rho=parse_hex(op[i]->arg[0]),N=parse_hex(op[i]->arg[1]),gm=gcdz(rho-1,N),gp=gcdz(rho+1,N);fixture_add(bank,SIGNED_RELATION_GCDS,2);if(gm!=3||gp!=5)throw Fatal("FIXTURE_SIGNED");trace+=name+"\t"+hexz(cpp_int(i))+"\t3\t5\n";}return;}if(name=="RATE_BASIS_RECORD"){const std::string line="F265-D18\tfixture\t60\trandom\t0\tQ\t0\tffffffffffffffff\t0000000000000000\t0000000000000000\t0000000000000000\t0000000000000000\t1\t4\t4\t3\t5\tSTRUCTURAL_Q_NON_GLOBAL\n";for(const auto*x:op){(void)x;fixture_add(bank,BASIS_RECORDS);if(line.size()>512)throw Fatal("FIXTURE_BASIS_CAP");trace+=line;}return;}throw Fatal("FIXTURE_RATE_MODE");}

std::string source_chrono_once(Bank& bank){const cpp_int N=(cpp_int(1)<<107)-1;bank.key={"fixture","random",hexz(N),2,60,0,0,N};bank.K=160;bank.nonce=seed_key({2,60,0,0})&UINT32_MAX;std::string trace;for(uint64_t curve=0;curve<2;++curve){for(uint64_t slot=0;slot<32;++slot){bool accept=slot==31;cpp_int A,B,x,y,d;if(curve==0){A=accept?1:N-3;x=accept?N-1:1;y=accept?N-1:0;B=accept?3:2;bank.count.add(RANDOM_BELOW_CALLS,3,kBankCap[RANDOM_BELOW_CALLS]);bank.count.add(RANDOM_BELOW_ITERATIONS,3,kBankCap[RANDOM_BELOW_ITERATIONS]);bank.count.add(RNG_DRAWS,6,kBankCap[RNG_DRAWS]);}else{cpp_int s=accept?1:N-1;x=s*s%N;y=x*s%N;A=(s+1)%N;B=modz(y*y-x*x*x-A*x,N);bank.count.add(RANDOM_BELOW_CALLS,1,kBankCap[RANDOM_BELOW_CALLS]);bank.count.add(RANDOM_BELOW_ITERATIONS,1,kBankCap[RANDOM_BELOW_ITERATIONS]);bank.count.add(RNG_DRAWS,2,kBankCap[RNG_DRAWS]);}bank.count.add(CURVE_PROPOSALS,1,kBankCap[CURVE_PROPOSALS]);bank.count.add(DISCRIMINANT_GCDS,1,kBankCap[DISCRIMINANT_GCDS]);d=gcdz(4*A*A*A+27*B*B,N);trace+="SOURCE_CHRONO320\tPROPOSAL\t"+hexz(curve)+"\t"+hexz(slot)+"\t"+(accept?"ACCEPT":"REJECT_FULL_DISCRIMINANT")+"\t"+hexz(A)+"\t"+hexz(B)+"\t"+hexz(x)+"\t"+hexz(y)+"\t"+hexz(d)+"\n";if(accept)bank.curve[curve]={A,B,x,y,4*A*A*A+27*B*B,true};}
    Point base{bank.curve[curve].x,bank.curve[curve].y,false};for(uint64_t scalar=1;scalar<=160;++scalar){Point point;if(scalar==1)point=base;else{Point reset=curve==0?Point{N-1,N-1,false}:Point{1,1,false};AddResult a=add_points(bank,curve,reset,reset,curve*160,curve*160);if(a.kind!=AddKind::OK)throw Fatal("SOURCE_CHRONO_AFFINE");point=a.p;trace+="SOURCE_CHRONO320\tAFFINE\t"+hexz(curve)+"\t"+hexz(scalar-1)+"\tOK\t"+hexz(point.x)+"\t"+hexz(point.y)+"\t1\n";}if(!append_row(bank,curve,scalar,point))throw Fatal("SOURCE_CHRONO_ROW");trace+="SOURCE_CHRONO320\tROW\t"+hexz(curve)+"\t"+hexz(scalar)+"\tUNIT\t1\n";const Row&r=bank.rows.back();trace+="SOURCE_CHRONO320\tRENDER\t"+hexz(r.original)+"\t"+hexz(r.u)+"\t"+hexz(r.v)+"\t"+hexz(r.a)+"\t"+hexz(r.carry)+"\n";}}
  for(uint64_t i=0;i<320;++i){cpp_int w=(cpp_int(1)<<180)+2*i+1;bank.rows[i].a=w*w;bank.rows[i].v=w;}peel(bank);for(const Row&r:bank.rows)trace+="SOURCE_CHRONO320\tPEEL\t"+hexz(r.original)+"\t"+hexz(r.g)+"\t"+hexz(r.b)+"\t"+(r.peel_square?"1":"0")+"\t"+(r.survivor?"1":"0")+"\n";return trace;}

void run_source_terminal(const std::string& name,Bank& b,std::string& trace){b.key={"fixture","random","35",2,60,0,0,35};b.nonce=0;b.curve[0]={1,1,0,1,31,true};if(name=="SOURCE_AFFINE_STOP3"){const std::array<std::pair<Point,Point>,3> p{{{{0,1,false},{0,34,false}},{{0,1,false},{0,6,false}},{{0,1,false},{7,1,false}}}};for(size_t i=0;i<3;++i){AddResult r=add_points(b,0,p[i].first,p[i].second,i,i+1);std::string status=r.kind==AddKind::INFINITY?"GLOBAL_INFINITY":r.kind==AddKind::FACTOR_MINUS?"FACTOR_X_SIGN_MINUS":"FACTOR_DENOMINATOR";trace+=name+"\tAFFINE\t"+hexz(i)+"\t"+status+"\t-\t-\t"+hexz(r.factor)+"\n";}}else{for(size_t i=0;i<2;++i){cpp_int v=i?0:5;b.count.add(ROW_ROOT_GCDS,1,kBankCap[ROW_ROOT_GCDS]);cpp_int g=gcdz(v,b.key.N);trace+=name+"\tROW\t"+hexz(i)+"\t"+(i?"FULL_ROW_ROOT":"FACTOR_ROW_ROOT")+"\t"+hexz(g)+"\n";}}}

void run_decoder_fixture(const std::string& name,const std::vector<const FixtureOperand*>& op,Bank& bank){bank.key={"fixture","random","15",2,60,0,0,15};if(name=="DECODER_EMPTY"){bank.rows={{0,0,1,0,1,31,0},{1,0,2,0,1,61,0}};peel(bank);decode_bank(bank);return;}for(const auto* x:op)if(x->opcode=="DECODER_ROW"){uint64_t original=parse_hex(x->arg[0]).convert_to<uint64_t>();cpp_int N=parse_hex(x->arg[1]),a=parse_hex(x->arg[2]),v=parse_hex(x->arg[3]);bank.key.N=N;bank.key.n_text=N.convert_to<std::string>();bank.rows.push_back({original,0,original+1,0,v,a,0,0,0,false,true});}if(bank.rows.empty())return;bank.peel_committed=true;bank.survivors=bank.rows.size();decode_bank(bank);}

FixtureTiming execute_fixture(const FixturePacket& packet,const std::string& name,OutputRoot* output) {
  auto op=expand_fixture(packet,name);
  unsigned repetitions=(name=="RATE_TERMINAL"||name=="RATE_IO")?4:8;
  FixtureTiming timing;
  if(name=="RATE_GCD"||name=="RATE_SAT"||name=="RATE_DIV"||
     name=="RATE_COMPARE"||name=="RATE_LEAF"||name=="RATE_EXP"||
     name=="RATE_PARITY"||name=="RATE_MOD_PRODUCT"||
     name=="RATE_INVERSE"||name=="RATE_SIGNED")timing.denominator=262144;
  else if(name=="RATE_TREE")timing.denominator=720896;
  else if(name=="RATE_RECON")timing.denominator=262144;
  else if(name=="RATE_TERMINAL")timing.denominator=1875;
  else if(name=="RATE_IO")timing.denominator=67108864;
  else if(name=="RATE_NODE"||name=="RATE_TOUCH"||
          name=="RATE_EXACT_PRODUCT"||name=="RATE_BASIS_RECORD")
    timing.denominator=65536;
  else if(name=="RATE_GF2")timing.denominator=524288;
  else if(name=="RATE_ISQRT")timing.denominator=256;
  else if(name=="FACTOR129")timing.denominator=129;
  else timing.denominator=1;

  for(unsigned repetition=0;repetition<repetitions;++repetition) {
    Bank bank;
    Bank* active=&bank;
    std::unique_ptr<Bank> timed_bank;
    std::string trace;
    std::array<uint64_t,40> actual{};
    if(name=="RATE_IO") {
      if(!output||op.size()!=1||op[0]->opcode!="IO_BYTES")
        throw Fatal("RATE_IO_OPERAND");
      uint64_t bytes=parse_hex(op[0]->arg[0]).convert_to<uint64_t>();
      uint64_t fill=parse_hex(op[0]->arg[1]).convert_to<uint64_t>();
      if(bytes!=67108864||fill>255)throw Fatal("RATE_IO_VALUE");
      std::string expected_sha;
      for(const auto& line:split_lines(packet.semantic.at(name))) {
        auto f=split_fields(line);
        if(f[3]=="AGGREGATE"&&f[4]=="STREAM_SHA256")expected_sha=f[5];
      }
      if(!sha_token(expected_sha)||!enumerate(output->fd).empty())
        throw Fatal("RATE_IO_INITIAL_STATE");
      struct stat probe{};
      for(const char* n:{"F265-D18.RATE_IO.bin",
                         ".F265-D18.RATE_IO.bin.tmp"})
        if(fstatat(output->fd,n,&probe,AT_SYMLINK_NOFOLLOW)==0||errno!=ENOENT)
          throw Fatal("RATE_IO_PRESENT");
      std::string buffer(1<<20,char(fill));
      int fd=-1;
      dev_t dev=0;
      ino_t ino=0;
      try {
        timespec begin=monotonic();
        fd=openat(output->fd,".F265-D18.RATE_IO.bin.tmp",
                  O_WRONLY|O_CREAT|O_EXCL|O_NOFOLLOW|O_CLOEXEC,0600);
        if(fd<0)throw Fatal("RATE_IO_CREATE");
        struct stat first{};
        if(fstat(fd,&first)||!S_ISREG(first.st_mode)||first.st_nlink!=1||
           first.st_uid!=geteuid()||first.st_gid!=getegid()||
           (first.st_mode&0777)!=0600||first.st_dev!=output->identity.dev)
          throw Fatal("RATE_IO_META");
        dev=first.st_dev;ino=first.st_ino;
        uint64_t written=0;
        while(written<bytes) {
          size_t want=size_t(std::min<uint64_t>(buffer.size(),bytes-written));
          ssize_t n=write(fd,buffer.data(),want);
          if(n<=0||uint64_t(n)>bytes-written)throw Fatal("RATE_IO_WRITE");
          written+=uint64_t(n);
        }
        struct stat closed{};
        if(fsync(fd)||fstat(fd,&closed)||closed.st_dev!=dev||
           closed.st_ino!=ino||closed.st_size!=off_t(bytes)||
           closed.st_nlink!=1||closed.st_uid!=geteuid()||
           closed.st_gid!=getegid()||(closed.st_mode&0777)!=0600)
          throw Fatal("RATE_IO_FLUSH");
        if(close(fd)){fd=-1;throw Fatal("RATE_IO_CLOSE");}
        fd=-1;
        auto authenticate_payload=[&](const char* basename) {
          int in=openat(output->fd,basename,O_RDONLY|O_NOFOLLOW|O_CLOEXEC);
          if(in<0)throw Fatal("RATE_IO_REOPEN");
          struct stat before{},after{};
          if(fstat(in,&before)||before.st_dev!=dev||before.st_ino!=ino||
             before.st_size!=off_t(bytes)||before.st_nlink!=1||
             before.st_uid!=geteuid()||before.st_gid!=getegid()||
             (before.st_mode&0777)!=0600) {
            close(in);throw Fatal("RATE_IO_READ_META");
          }
          Sha256 h;
          uint64_t read_bytes=0;
          std::array<char,65536> chunk{};
          while(read_bytes<bytes) {
            ssize_t n=read(in,chunk.data(),
                           std::min<uint64_t>(chunk.size(),bytes-read_bytes));
            if(n<=0){close(in);throw Fatal("RATE_IO_EOF");}
            h.add(chunk.data(),size_t(n));read_bytes+=uint64_t(n);
          }
          char extra;
          ssize_t tail=read(in,&extra,1);
          if(tail!=0||fstat(in,&after)||after.st_dev!=before.st_dev||
             after.st_ino!=before.st_ino||after.st_size!=before.st_size||
             after.st_nlink!=before.st_nlink||after.st_uid!=before.st_uid||
             after.st_gid!=before.st_gid||
             mode_t(after.st_mode&07777)!=mode_t(before.st_mode&07777)||
             close(in))throw Fatal("RATE_IO_STABILITY");
          if(h.final()!=expected_sha)throw Fatal("RATE_IO_HASH");
        };
        authenticate_payload(".F265-D18.RATE_IO.bin.tmp");
        if(fstatat(output->fd,"F265-D18.RATE_IO.bin",&probe,
                   AT_SYMLINK_NOFOLLOW)==0||errno!=ENOENT)
          throw Fatal("RATE_IO_FINAL_PRESENT");
        if(renameat(output->fd,".F265-D18.RATE_IO.bin.tmp",output->fd,
                    "F265-D18.RATE_IO.bin")||fsync(output->fd))
          throw Fatal("RATE_IO_RENAME");
        if(fstatat(output->fd,".F265-D18.RATE_IO.bin.tmp",&probe,
                   AT_SYMLINK_NOFOLLOW)==0||errno!=ENOENT)
          throw Fatal("RATE_IO_TEMP_AFTER_RENAME");
        if(fstatat(output->fd,"F265-D18.RATE_IO.bin",&probe,
                   AT_SYMLINK_NOFOLLOW)||probe.st_dev!=dev||
           probe.st_ino!=ino||probe.st_size!=off_t(bytes)||
           probe.st_nlink!=1||probe.st_uid!=geteuid()||
           probe.st_gid!=getegid()||(probe.st_mode&0777)!=0600)
          throw Fatal("RATE_IO_RENAME_IDENTITY");
        authenticate_payload("F265-D18.RATE_IO.bin");
        if(unlinkat(output->fd,"F265-D18.RATE_IO.bin",0)||fsync(output->fd))
          throw Fatal("RATE_IO_UNLINK");
        for(const char* n:{"F265-D18.RATE_IO.bin",
                           ".F265-D18.RATE_IO.bin.tmp"})
          if(fstatat(output->fd,n,&probe,AT_SYMLINK_NOFOLLOW)==0||
             errno!=ENOENT)throw Fatal("RATE_IO_ABSENCE");
        if(!enumerate(output->fd).empty())throw Fatal("RATE_IO_MEMBERSHIP");
        uint64_t elapsed=tick_ns(begin,monotonic());
        timing.maximum=std::max(timing.maximum,elapsed);
        actual[39]=bytes;
      } catch(...) {
        if(fd>=0)close(fd);
        for(const char* n:{".F265-D18.RATE_IO.bin.tmp",
                           "F265-D18.RATE_IO.bin"}) {
          struct stat s{};
          if(fstatat(output->fd,n,&s,AT_SYMLINK_NOFOLLOW)==0&&
             s.st_dev==dev&&s.st_ino==ino)unlinkat(output->fd,n,0);
        }
        fsync(output->fd);
        for(const char* n:{"F265-D18.RATE_IO.bin",
                           ".F265-D18.RATE_IO.bin.tmp"})
          if(fstatat(output->fd,n,&probe,AT_SYMLINK_NOFOLLOW)==0||
             errno!=ENOENT)throw Fatal("RATE_IO_CLEANUP");
        throw;
      }
      check_fixture_counts(packet,name,actual);
      check_fixture_trace(packet,name,kFnvOffset,sha256(trace));
      continue;
    }

    Sha256 production_sha;
    uint64_t production_fnv=kFnvOffset;
    timespec begin=monotonic();
    if(name=="SOURCE_CHRONO320"){
      timed_bank=std::make_unique<Bank>();
      active=timed_bank.get();
    }
    if(name=="CURVE_U32"||name=="CURVE_POWER32")
      fixture_curve_screen(name,op,*active);
    else if(name=="RBELOW128"||name=="RNG_SEMANTIC")
      fixture_random(name,op,*active);
    else if(name=="SOURCE_BRANCH")
      fixture_source_branch(op,*active);
    else if(name=="SOURCE_CHRONO320")
      trace=source_chrono_once(*active);
    else if(name=="SOURCE_AFFINE_STOP3"||name=="SOURCE_ROW_STOP2")
      run_source_terminal(name,*active,trace);
    else if(name=="FACTOR129"||name=="EVENT130"||
            name=="PACKET_EVENT60373")
      fixture_events(name,op,*active);
    else if(name.rfind("DECODER_",0)==0)
      run_decoder_fixture(name,op,*active);
    else if(name=="DENSE_GF2")
      fixture_dense_gf2(*active,op,trace);
    else if(name.rfind("RATE_",0)==0)
      fixture_rate(name,op,*active,trace);
    else throw Fatal("FIXTURE_DISPATCH");
    for(unsigned char byte:trace)production_fnv=(production_fnv^byte)*kFnvPrime;
    production_sha.add(trace);
    std::string production_digest=production_sha.final();
    uint64_t elapsed=tick_ns(begin,monotonic());
    timing.maximum=std::max(timing.maximum,elapsed);
    actual=fixture_counts(*active,name=="SOURCE_CHRONO320"?320:0);
    check_fixture_trace(packet,name,production_fnv,production_digest);
    check_fixture_counts(packet,name,actual);
  }
  return timing;
}
int mode_preflight(const Cli& c){timespec preflight_start=monotonic();OutputRoot output(c.option.at("--output-root"));InputRoot fixture(c.option.at("--fixture-root"),kFixtureFiles),verification(c.option.at("--fixture-verification-root"),kVerifyFiles);DirectFile discovery(c.option.at("--discovery-public"),8388608),heldout(c.option.at("--heldout-public"),8388608);roots_distinct(output,{&fixture,&verification},{&discovery,&heldout});authenticate_fixtures(fixture,verification);parse_corpus(discovery,"discovery");parse_corpus(heldout,"heldout");FixturePacket packet=parse_fixture_packet(fixture);PreflightRun run;for(const char* name:kFixtureName)run.time[name]=execute_fixture(packet,name,&output);
  auto rate=[&](const std::string& name){const auto& x=run.time.at(name);if(x.denominator==0)throw Fatal("ZERO_DENOMINATOR");return Rational(x.maximum,x.denominator);};Rational source=(Rational(run.time.at("SOURCE_CHRONO320").maximum)+Rational(run.time.at("SOURCE_AFFINE_STOP3").maximum)+Rational(run.time.at("SOURCE_ROW_STOP2").maximum))*468+Rational(run.time.at("RBELOW128").maximum)*59904;Rational decoder=rate("RATE_GCD")*8388608+rate("RATE_SAT")*4893354+rate("RATE_DIV")*13981013+rate("RATE_NODE")*4194304+rate("RATE_TOUCH")*699050+rate("RATE_LEAF")*4923306+rate("RATE_TREE")*54156366+rate("RATE_EXP")*313174656+rate("RATE_RECON")*10812672+rate("RATE_TERMINAL")*877500+rate("RATE_COMPARE")*39012624+rate("RATE_PARITY")*56160000+rate("RATE_GF2")*245366784+(rate("RATE_EXACT_PRODUCT")+rate("RATE_MOD_PRODUCT"))*1916928+(rate("RATE_ISQRT")+rate("RATE_INVERSE")+rate("RATE_BASIS_RECORD"))*29952+rate("RATE_SIGNED")*59904;Rational pass=source+decoder+rate("FACTOR129")*60372+rate("RATE_IO")*226088448;Rational raw=pass*2+Rational(cpp_int(900000000000LL));Rational projected=raw*Rational(7,4);cpp_int projected_ns=ceilq(projected);if((projected.n>cpp_int(10800000000000LL)*projected.d)!=(projected_ns>cpp_int(10800000000000LL))||projected_ns>cpp_int(10800000000000LL))throw Fatal("PROJECTION_GATE");uint64_t input_bytes=0;for(auto&x:fixture.file)input_bytes+=x.second.identity.size;for(auto&x:verification.file)input_bytes+=x.second.identity.size;input_bytes+=discovery.file.identity.size+heldout.file.identity.size;fixture.reauthenticate();verification.reauthenticate();discovery.reauthenticate();heldout.reauthenticate();if(!enumerate(output.fd).empty())throw Fatal("PREFLIGHT_OUTPUT_NOT_EMPTY");timespec preflight_end=monotonic();uint64_t preflight_ns=tick_ns(preflight_start,preflight_end);if(preflight_ns>UINT64_C(1200000000000))throw Fatal("PREFLIGHT_TIME_GATE");std::string tsv="version\tfixture_payload_root\tfixture_verification_root\tfixtures\tprojected_seconds\tpreflight_seconds\tpreflight_bytes\tstatus\n"+std::string(kVersion)+"\t"+kFixturePayloadRoot+"\t"+kFixtureVerificationRoot+"\t37\t"+seconds9(projected_ns)+"\t"+seconds9(preflight_ns)+"\t"+std::to_string(input_bytes)+"\tPASS\n";std::string manifest=sha256(tsv)+"  F265-D18.preflight.tsv\n";output.write_file("F265-D18.preflight.tsv",tsv,1048576);output.write_file("F265-D18.PREFLIGHT.sha256",manifest,65536);output.finish();return 0;}

int dispatch(const Cli& c){if(c.mode=="preflight")return mode_preflight(c);if(c.mode=="evaluate")return mode_evaluate(c);if(c.mode=="replay")return mode_replay(c);if(c.mode=="seal-public")return mode_seal_public(c);if(c.mode=="diagnostics")return mode_diagnostics(c);throw Fatal("MODE_DISPATCH");}



} // namespace f265_d18_public

int main(int argc,char**argv){try{if(!std::setlocale(LC_ALL,"C"))throw f265_d18_public::Fatal("LOCALE");umask(077);return f265_d18_public::dispatch(f265_d18_public::parse_cli(argc,argv));}catch(const std::exception& e){std::cerr<<"F265-D18 public failure: "<<e.what()<<'\n';return 1;}}
