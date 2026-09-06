#include <algorithm>
#include <array>
#include <cerrno>
#include <clocale>
#include <cstdint>
#include <cstring>
#include <dirent.h>
#include <fcntl.h>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <map>
#include <set>
#include <sstream>
#include <stdexcept>
#include <string>
#include <sys/stat.h>
#include <sys/types.h>
#include <time.h>
#include <tuple>
#include <unistd.h>
#include <utility>
#include <vector>

#include <boost/multiprecision/cpp_int.hpp>

// F265-D18 private-classification source draft.  This compilation unit has no
// curve source, peel, decoder, basis construction, diagnostic search, finite-
// decision selection, or fixture-injection body.  Its two deliberately invalid
// constants are the source-freeze gate required by D12--D18.

namespace f265_d18_private {

using boost::multiprecision::cpp_int;

static constexpr const char kFixturePayloadRoot[] =
    @F265_D18_FIXTURE_PAYLOAD_ROOT@;
static constexpr const char kFixtureVerificationRoot[] =
    @F265_D18_FIXTURE_VERIFICATION_ROOT@;

constexpr char kVersion[] = "F265-D18";
constexpr char kDiscoveryPublicHash[] =
    "8b6f8dbe4eae9aa10c042928fc19fbe20a0015487340e7478135ce6f37b5adb5";
constexpr char kHeldoutPublicHash[] =
    "b4a4c976013dd62c58376b948c51a1c5c380265a46fbf932a5e0972fb6c389d5";
constexpr char kDiscoveryPrivateHash[] =
    "0433b7e295528de85f717f8e357efd68533eef935a7881850265e13554f3f4a6";
constexpr char kHeldoutPrivateHash[] =
    "a962125dd3b7c5189d84d406ab229d9776317ece23aac9c2ea551de07b8380b2";

struct Failure : std::runtime_error { using std::runtime_error::runtime_error; };

class Sha256 {
 public:
  Sha256(){state_={0x6a09e667U,0xbb67ae85U,0x3c6ef372U,0xa54ff53aU,0x510e527fU,0x9b05688cU,0x1f83d9abU,0x5be0cd19U};}
  void add(const void* data,size_t n){const auto* p=static_cast<const unsigned char*>(data);total_+=n;while(n){size_t take=std::min(n,64-used_);std::memcpy(block_.data()+used_,p,take);used_+=take;p+=take;n-=take;if(used_==64){compress(block_.data());used_=0;}}}
  void add(const std::string& s){add(s.data(),s.size());}
  std::string finish(){uint64_t bits=total_*8;block_[used_++]=0x80;if(used_>56){std::fill(block_.begin()+static_cast<ptrdiff_t>(used_),block_.end(),0);compress(block_.data());used_=0;}std::fill(block_.begin()+static_cast<ptrdiff_t>(used_),block_.begin()+56,0);for(int i=0;i<8;++i)block_[63-i]=static_cast<unsigned char>(bits>>(8*i));compress(block_.data());std::ostringstream out;out<<std::hex<<std::setfill('0');for(uint32_t x:state_)out<<std::setw(8)<<x;return out.str();}
 private:
  static uint32_t ror(uint32_t x,unsigned n){return (x>>n)|(x<<(32-n));}
  void compress(const unsigned char* p){static constexpr uint32_t k[64]={0x428a2f98U,0x71374491U,0xb5c0fbcfU,0xe9b5dba5U,0x3956c25bU,0x59f111f1U,0x923f82a4U,0xab1c5ed5U,0xd807aa98U,0x12835b01U,0x243185beU,0x550c7dc3U,0x72be5d74U,0x80deb1feU,0x9bdc06a7U,0xc19bf174U,0xe49b69c1U,0xefbe4786U,0x0fc19dc6U,0x240ca1ccU,0x2de92c6fU,0x4a7484aaU,0x5cb0a9dcU,0x76f988daU,0x983e5152U,0xa831c66dU,0xb00327c8U,0xbf597fc7U,0xc6e00bf3U,0xd5a79147U,0x06ca6351U,0x14292967U,0x27b70a85U,0x2e1b2138U,0x4d2c6dfcU,0x53380d13U,0x650a7354U,0x766a0abbU,0x81c2c92eU,0x92722c85U,0xa2bfe8a1U,0xa81a664bU,0xc24b8b70U,0xc76c51a3U,0xd192e819U,0xd6990624U,0xf40e3585U,0x106aa070U,0x19a4c116U,0x1e376c08U,0x2748774cU,0x34b0bcb5U,0x391c0cb3U,0x4ed8aa4aU,0x5b9cca4fU,0x682e6ff3U,0x748f82eeU,0x78a5636fU,0x84c87814U,0x8cc70208U,0x90befffaU,0xa4506cebU,0xbef9a3f7U,0xc67178f2U};uint32_t w[64];for(int i=0;i<16;++i)w[i]=(uint32_t(p[4*i])<<24)|(uint32_t(p[4*i+1])<<16)|(uint32_t(p[4*i+2])<<8)|p[4*i+3];for(int i=16;i<64;++i)w[i]=w[i-16]+(ror(w[i-15],7)^ror(w[i-15],18)^(w[i-15]>>3))+w[i-7]+(ror(w[i-2],17)^ror(w[i-2],19)^(w[i-2]>>10));uint32_t a=state_[0],b=state_[1],c=state_[2],d=state_[3],e=state_[4],f=state_[5],g=state_[6],h=state_[7];for(int i=0;i<64;++i){uint32_t t=h+(ror(e,6)^ror(e,11)^ror(e,25))+((e&f)^((~e)&g))+k[i]+w[i],u=(ror(a,2)^ror(a,13)^ror(a,22))+((a&b)^(a&c)^(b&c));h=g;g=f;f=e;e=d+t;d=c;c=b;b=a;a=t+u;}state_[0]+=a;state_[1]+=b;state_[2]+=c;state_[3]+=d;state_[4]+=e;state_[5]+=f;state_[6]+=g;state_[7]+=h;}
  std::array<uint32_t,8> state_{};std::array<unsigned char,64> block_{};uint64_t total_=0;size_t used_=0;
};

std::string sha256(const std::string& s){Sha256 h;h.add(s);return h.finish();}
bool decimal(const std::string& s){return !s.empty()&&!(s.size()>1&&s[0]=='0')&&std::all_of(s.begin(),s.end(),[](unsigned char c){return c>='0'&&c<='9';});}
bool hexadecimal(const std::string& s){return !s.empty()&&!(s.size()>1&&s[0]=='0')&&std::all_of(s.begin(),s.end(),[](unsigned char c){return (c>='0'&&c<='9')||(c>='a'&&c<='f');});}
bool digest(const std::string& s){return s.size()==64&&std::all_of(s.begin(),s.end(),[](unsigned char c){return (c>='0'&&c<='9')||(c>='a'&&c<='f');});}
uint64_t udec(const std::string& s){if(!decimal(s))throw Failure("DECIMAL");uint64_t x=0;for(char c:s){if(x>(UINT64_MAX-uint64_t(c-'0'))/10)throw Failure("DECIMAL_RANGE");x=x*10+uint64_t(c-'0');}return x;}
cpp_int zdec(const std::string& s){if(!decimal(s))throw Failure("BIG_DECIMAL");cpp_int x=0;for(char c:s)x=x*10+(c-'0');return x;}
cpp_int zhex(const std::string& s){if(!hexadecimal(s))throw Failure("BIG_HEX");cpp_int x=0;for(char c:s)x=(x<<4)+(c<='9'?c-'0':c-'a'+10);return x;}
std::vector<std::string> fields(const std::string& line){std::vector<std::string> out;size_t at=0;for(;;){size_t e=line.find('\t',at);out.push_back(line.substr(at,e-at));if(e==std::string::npos)return out;at=e+1;}}
std::vector<std::string> lines(const std::string& bytes){if(bytes.empty()||bytes.back()!='\n'||bytes.find('\r')!=std::string::npos||bytes.find('\0')!=std::string::npos)throw Failure("TEXT_BYTES");std::vector<std::string> out;size_t at=0;while(at<bytes.size()){size_t e=bytes.find('\n',at);out.push_back(bytes.substr(at,e-at));at=e+1;}return out;}

struct FileMark {dev_t dev{};ino_t ino{};off_t size{};mode_t mode{};uid_t uid{};gid_t gid{};nlink_t links{};timespec mt{},ct{};std::string sha;};
struct RootMark {dev_t dev{};ino_t ino{};mode_t mode{};uid_t uid{};gid_t gid{};};
timespec mt(const struct stat& s){
#if defined(__APPLE__)
  return s.st_mtimespec;
#else
  return s.st_mtim;
#endif
}
timespec ct(const struct stat& s){
#if defined(__APPLE__)
  return s.st_ctimespec;
#else
  return s.st_ctim;
#endif
}
bool same_time(const timespec&a,const timespec&b){return a.tv_sec==b.tv_sec&&a.tv_nsec==b.tv_nsec;}
FileMark mark(const struct stat&s,const std::string&h){return{s.st_dev,s.st_ino,s.st_size,mode_t(s.st_mode&07777),s.st_uid,s.st_gid,s.st_nlink,mt(s),ct(s),h};}
bool same(const FileMark&a,const FileMark&b){return a.dev==b.dev&&a.ino==b.ino&&a.size==b.size&&a.mode==b.mode&&a.uid==b.uid&&a.gid==b.gid&&a.links==b.links&&same_time(a.mt,b.mt)&&same_time(a.ct,b.ct)&&a.sha==b.sha;}
bool abs_path(const std::string& path){if(path.size()<2||path.size()>1024||path.front()!='/'||path.back()=='/')return false;for(size_t at=1;at<path.size();){size_t e=path.find('/',at);if(e==std::string::npos)e=path.size();std::string part=path.substr(at,e-at);if(part.empty()||part=="."||part=="..")return false;for(unsigned char c:part)if(!((c>='A'&&c<='Z')||(c>='a'&&c<='z')||(c>='0'&&c<='9')||c=='_'||c=='-'||c=='.'))return false;at=e+1;}return true;}
int open_dir(const std::string& path){int fd=open("/",O_RDONLY|O_DIRECTORY|O_CLOEXEC);if(fd<0)throw Failure("OPEN_SLASH");for(size_t at=1;at<path.size();){size_t e=path.find('/',at);if(e==std::string::npos)e=path.size();std::string part=path.substr(at,e-at);int next=openat(fd,part.c_str(),O_RDONLY|O_DIRECTORY|O_NOFOLLOW|O_CLOEXEC);int saved=errno;close(fd);errno=saved;if(next<0)throw Failure("OPEN_COMPONENT");fd=next;at=e+1;}return fd;}
std::vector<std::string> members(int fd){int copy=dup(fd);if(copy<0)throw Failure("DUP_DIR");DIR*d=fdopendir(copy);if(!d){close(copy);throw Failure("FDOPENDIR");}std::vector<std::string> out;errno=0;while(dirent*e=readdir(d)){std::string n=e->d_name;if(n!="."&&n!="..")out.push_back(n);}int saved=errno;if(closedir(d)||saved)throw Failure("READDIR");std::sort(out.begin(),out.end());return out;}
bool ancestor(int child,dev_t dev,ino_t ino){int here=dup(child);if(here<0)throw Failure("ANCESTOR_DUP");for(;;){struct stat s{};if(fstat(here,&s)){close(here);throw Failure("ANCESTOR_STAT");}if(s.st_dev==dev&&s.st_ino==ino){close(here);return true;}int parent=openat(here,"..",O_RDONLY|O_DIRECTORY|O_NOFOLLOW|O_CLOEXEC);if(parent<0){close(here);throw Failure("ANCESTOR_PARENT");}struct stat p{};if(fstat(parent,&p)){close(parent);close(here);throw Failure("ANCESTOR_PARENT_STAT");}if(p.st_dev==s.st_dev&&p.st_ino==s.st_ino){close(parent);close(here);return false;}close(here);here=parent;}}

struct InputFile {
  int fd=-1;std::string name,bytes;FileMark identity;
  InputFile()=default;
  InputFile(int parent,const std::string& n,size_t cap):name(n){fd=openat(parent,n.c_str(),O_RDONLY|O_NOFOLLOW|O_CLOEXEC);if(fd<0)throw Failure("INPUT_OPEN");struct stat a{},b{};if(fstat(fd,&a)||!S_ISREG(a.st_mode)||a.st_size<0||uint64_t(a.st_size)>cap)throw Failure("INPUT_META");std::array<char,65536> buffer{};for(;;){ssize_t got=read(fd,buffer.data(),buffer.size());if(got<0)throw Failure("INPUT_READ");if(!got)break;bytes.append(buffer.data(),size_t(got));}std::string h=sha256(bytes);if(fstat(fd,&b))throw Failure("INPUT_POST_STAT");FileMark x=mark(a,h),y=mark(b,h);if(!same(x,y)||lseek(fd,0,SEEK_SET)!=0)throw Failure("INPUT_RACE");identity=x;}
  InputFile(InputFile&&x)noexcept:fd(x.fd),name(std::move(x.name)),bytes(std::move(x.bytes)),identity(x.identity){x.fd=-1;}
  InputFile&operator=(InputFile&&x)noexcept{if(this!=&x){if(fd>=0)close(fd);fd=x.fd;x.fd=-1;name=std::move(x.name);bytes=std::move(x.bytes);identity=x.identity;}return *this;}
  InputFile(const InputFile&)=delete;InputFile&operator=(const InputFile&)=delete;~InputFile(){if(fd>=0)close(fd);}
  void recheck(){if(lseek(fd,0,SEEK_SET)!=0)throw Failure("RECHECK_SEEK");std::string now;std::array<char,65536> buffer{};for(;;){ssize_t got=read(fd,buffer.data(),buffer.size());if(got<0)throw Failure("RECHECK_READ");if(!got)break;now.append(buffer.data(),size_t(got));}struct stat s{};if(fstat(fd,&s)||now!=bytes||!same(identity,mark(s,sha256(now))))throw Failure("INPUT_CHANGED");}
};

struct InputRoot {
  int fd=-1;RootMark identity;std::vector<std::string> membership;std::map<std::string,InputFile> file;
  InputRoot(const std::string& path,const std::vector<std::pair<std::string,size_t>>& expected){fd=open_dir(path);struct stat s{};if(fstat(fd,&s)||!S_ISDIR(s.st_mode))throw Failure("INPUT_ROOT");identity={s.st_dev,s.st_ino,mode_t(s.st_mode&07777),s.st_uid,s.st_gid};membership=members(fd);std::vector<std::string>want;for(const auto&x:expected)want.push_back(x.first);std::sort(want.begin(),want.end());if(want!=membership)throw Failure("INPUT_MEMBERSHIP");for(const auto&x:expected)file.emplace(x.first,InputFile(fd,x.first,x.second));}
  InputRoot(const InputRoot&)=delete;~InputRoot(){if(fd>=0)close(fd);}
  void recheck(){struct stat s{};if(fstat(fd,&s)||s.st_dev!=identity.dev||s.st_ino!=identity.ino||mode_t(s.st_mode&07777)!=identity.mode||s.st_uid!=identity.uid||s.st_gid!=identity.gid||members(fd)!=membership)throw Failure("ROOT_CHANGED");for(auto&x:file)x.second.recheck();}
};

struct DirectFile {
  int parent=-1;RootMark parent_identity;InputFile file;
  DirectFile(const std::string& path,size_t cap){size_t slash=path.rfind('/');std::string directory=slash==0?"/":path.substr(0,slash),base=path.substr(slash+1);parent=directory=="/"?open("/",O_RDONLY|O_DIRECTORY|O_CLOEXEC):open_dir(directory);if(parent<0)throw Failure("DIRECT_PARENT");struct stat s{};if(fstat(parent,&s))throw Failure("DIRECT_PARENT_STAT");parent_identity={s.st_dev,s.st_ino,mode_t(s.st_mode&07777),s.st_uid,s.st_gid};file=InputFile(parent,base,cap);}
  DirectFile(const DirectFile&)=delete;~DirectFile(){if(parent>=0)close(parent);}
  void recheck(){file.recheck();struct stat s{};if(fstat(parent,&s)||s.st_dev!=parent_identity.dev||s.st_ino!=parent_identity.ino||mode_t(s.st_mode&07777)!=parent_identity.mode||s.st_uid!=parent_identity.uid||s.st_gid!=parent_identity.gid)throw Failure("DIRECT_PARENT_CHANGED");}
};

struct OutputRoot {
  int fd=-1;RootMark identity;std::set<std::pair<dev_t,ino_t>> forbidden;std::vector<std::string> final;
  explicit OutputRoot(const std::string& path){fd=open_dir(path);struct stat s{};if(fstat(fd,&s)||!S_ISDIR(s.st_mode)||s.st_uid!=geteuid()||(s.st_mode&077)!=0||!members(fd).empty())throw Failure("OUTPUT_ROOT");identity={s.st_dev,s.st_ino,mode_t(s.st_mode&07777),s.st_uid,s.st_gid};}
  OutputRoot(const OutputRoot&)=delete;~OutputRoot(){if(fd>=0)close(fd);}
  void forbid(const InputFile& f){forbidden.insert({f.identity.dev,f.identity.ino});}
  void write(const std::string& name,const std::string& bytes,size_t cap){if(bytes.size()>cap)throw Failure("OUTPUT_CAP");std::string temp="."+name+".tmp";int out=openat(fd,temp.c_str(),O_WRONLY|O_CREAT|O_EXCL|O_NOFOLLOW|O_CLOEXEC,0600);if(out<0)throw Failure("OUTPUT_CREATE");try{struct stat s{};if(fstat(out,&s)||!S_ISREG(s.st_mode)||s.st_nlink!=1||s.st_uid!=geteuid()||(s.st_mode&0777)!=0600||forbidden.count({s.st_dev,s.st_ino}))throw Failure("OUTPUT_META");size_t at=0;while(at<bytes.size()){ssize_t n=::write(out,bytes.data()+at,bytes.size()-at);if(n<=0)throw Failure("OUTPUT_WRITE");at+=size_t(n);}if(fsync(out)||close(out)){out=-1;throw Failure("OUTPUT_FLUSH");}out=-1;int verify=openat(fd,temp.c_str(),O_RDONLY|O_NOFOLLOW|O_CLOEXEC);if(verify<0)throw Failure("OUTPUT_VERIFY_OPEN");std::string copy;std::array<char,65536>b{};for(;;){ssize_t n=read(verify,b.data(),b.size());if(n<0){close(verify);throw Failure("OUTPUT_VERIFY_READ");}if(!n)break;copy.append(b.data(),size_t(n));}if(close(verify)||copy!=bytes)throw Failure("OUTPUT_VERIFY");struct stat absent{};if(fstatat(fd,name.c_str(),&absent,AT_SYMLINK_NOFOLLOW)==0||errno!=ENOENT||renameat(fd,temp.c_str(),fd,name.c_str())||fsync(fd))throw Failure("OUTPUT_RENAME");final.push_back(name);}catch(...){if(out>=0)close(out);unlinkat(fd,temp.c_str(),0);throw;}}
  void finish(){struct stat s{};if(fstat(fd,&s)||s.st_dev!=identity.dev||s.st_ino!=identity.ino||mode_t(s.st_mode&07777)!=identity.mode||s.st_uid!=identity.uid||s.st_gid!=identity.gid)throw Failure("OUTPUT_CHANGED");std::sort(final.begin(),final.end());if(members(fd)!=final)throw Failure("OUTPUT_MEMBERSHIP");}
};

void separate(OutputRoot& output,const std::vector<InputRoot*>& roots,const std::vector<DirectFile*>& files){for(size_t i=0;i<roots.size();++i){InputRoot*r=roots[i];if(ancestor(output.fd,r->identity.dev,r->identity.ino)||ancestor(r->fd,output.identity.dev,output.identity.ino))throw Failure("ROOT_ALIAS");for(size_t j=0;j<i;++j)if(ancestor(r->fd,roots[j]->identity.dev,roots[j]->identity.ino)||ancestor(roots[j]->fd,r->identity.dev,r->identity.ino))throw Failure("INPUT_ROOT_ALIAS");for(auto&x:r->file)output.forbid(x.second);}for(DirectFile*f:files){output.forbid(f->file);if(ancestor(output.fd,f->parent_identity.dev,f->parent_identity.ino)||ancestor(f->parent,output.identity.dev,output.identity.ino))throw Failure("DIRECT_OUTPUT_ALIAS");}}

struct Cli {std::map<std::string,std::string> value;};
Cli parse_cli(int argc,char**argv){if(argc!=21)throw Failure("CLI_COUNT");Cli c;for(int i=1;i<argc;i+=2){std::string key=argv[i];if(key.rfind("--",0)!=0||!c.value.emplace(key,argv[i+1]).second)throw Failure("CLI_OPTION");}const std::set<std::string> need{"--mode","--discovery-public","--heldout-public","--discovery-private","--heldout-private","--discovery-evaluation-root","--heldout-evaluation-root","--sealed-root","--diagnostics-root","--output-root"};if(c.value.size()!=need.size()||c.value.at("--mode")!="classify")throw Failure("CLI_MODE");for(const auto&x:need)if(!c.value.count(x))throw Failure("CLI_REQUIRED");for(const auto&[key,value]:c.value)if(key!="--mode"&&!abs_path(value))throw Failure("CLI_PATH");return c;}

const std::vector<std::pair<std::string,size_t>> kDiscoveryEvaluation{{"F265-D18.discovery.meta.tsv",1048576},{"F265-D18.discovery.banks.tsv",128*1024*1024},{"F265-D18.discovery.rows.tsv",128*1024*1024},{"F265-D18.discovery.basis.tsv",128*1024*1024},{"F265-D18.discovery.events.tsv",15455488},{"F265-D18.discovery.event_witnesses.tsv",8388608},{"F265-D18.discovery.counters.tsv",8388608},{"F265-D18.discovery.CORE.sha256",65536}};
const std::vector<std::pair<std::string,size_t>> kHeldoutEvaluation{{"F265-D18.heldout.meta.tsv",1048576},{"F265-D18.heldout.banks.tsv",128*1024*1024},{"F265-D18.heldout.rows.tsv",128*1024*1024},{"F265-D18.heldout.basis.tsv",128*1024*1024},{"F265-D18.heldout.events.tsv",15455488},{"F265-D18.heldout.event_witnesses.tsv",8388608},{"F265-D18.heldout.counters.tsv",8388608},{"F265-D18.heldout.CORE.sha256",65536}};
const std::vector<std::pair<std::string,size_t>> kSeal{{"F265-D18.decision.tsv",1048576},{"F265-D18.SEALED.sha256",65536}};
const std::vector<std::pair<std::string,size_t>> kDiagnostics{{"F265-D18.diagnostic_summary.tsv",1048576},{"F265-D18.diagnostic_details.tsv",7667712},{"F265-D18.DIAGNOSTICS.sha256",65536}};

void manifest(const InputRoot& root,const std::string& name,const std::vector<std::string>& ordered){std::string expected;for(const auto&n:ordered)expected+=root.file.at(n).identity.sha+"  "+n+"\n";if(root.file.at(name).bytes!=expected)throw Failure("MANIFEST");}

struct PublicRow {std::string split,shape,bits,index,N;uint64_t split_rank=0,shape_rank=0,bit_rank=0;};
std::string key(const std::string&s,const std::string&b,const std::string&shape,const std::string&i){return s+"\t"+b+"\t"+shape+"\t"+i;}

std::vector<PublicRow> public_rows(const DirectFile& file,const std::string& split){const char* expected=split=="discovery"?kDiscoveryPublicHash:kHeldoutPublicHash;if(file.file.identity.sha!=expected)throw Failure("PUBLIC_HASH");auto r=lines(file.file.bytes);size_t expected_count=split=="discovery"?188:296;if(r.size()!=expected_count+1||r[0]!="version\tsplit\tshape\tfactor_bits\tindex\tN")throw Failure("PUBLIC_HEADER");const std::vector<uint64_t> menu=split=="discovery"?std::vector<uint64_t>{12,16,20,24,32}:std::vector<uint64_t>{40,48,56,60};std::set<std::string> keys,moduli;std::vector<PublicRow> out;for(size_t i=1;i<r.size();++i){auto f=fields(r[i]);if(f.size()!=6||f[0]!="F268-D04"||f[1]!=split||!decimal(f[3])||!decimal(f[4])||!decimal(f[5])||!keys.insert(key(f[1],f[3],f[2],f[4])).second||!moduli.insert(f[5]).second)throw Failure("PUBLIC_ROW");uint64_t shape=f[2]=="random"?0:f[2]=="neighbor"?1:f[2]=="safe-safe"?2:f[2]=="marker-control"?3:99;if(shape==99)throw Failure("PUBLIC_SHAPE");uint64_t bits=udec(f[3]);auto at=std::find(menu.begin(),menu.end(),bits);if(shape!=3&&at==menu.end())throw Failure("PUBLIC_BITS");out.push_back({f[1],f[2],f[3],f[4],f[5],split=="discovery"?0U:1U,shape,shape==3?UINT64_MAX:uint64_t(at-menu.begin()+(split=="discovery"?0:5))});}return out;}

struct EvaluationBinding {std::string root,prior_core,prior_replay,event_suffix,event_hash;uint64_t cumulative_events=0,local_events=0;std::map<std::string,std::string>N;};
EvaluationBinding evaluation(InputRoot& root,const std::string& split,const std::string& public_hash,const EvaluationBinding* prior){std::string p="F265-D18."+split+".";manifest(root,p+"CORE.sha256",{p+"meta.tsv",p+"banks.tsv",p+"rows.tsv",p+"basis.tsv",p+"events.tsv",p+"event_witnesses.tsv",p+"counters.tsv"});auto meta=lines(root.file.at(p+"meta.tsv").bytes);if(meta.size()!=2||meta[0]!="version\tsplit\tpublic_sha256\tfixture_payload_root\tfixture_verification_root\tprior_evaluation_root\tprior_replay_root\tbank_count\trow_count\tbasis_count\tevent_count\tpacket_event_sha256\tstatus")throw Failure("EVALUATION_META");auto m=fields(meta[1]);if(m.size()!=13||m[0]!=kVersion||m[1]!=split||m[2]!=public_hash||m[3]!=kFixturePayloadRoot||m[4]!=kFixtureVerificationRoot||m[12]!="PASS"||!digest(m[11]))throw Failure("EVALUATION_META_ROW");if(split=="discovery"){if(prior||m[5]!="-"||m[6]!="-")throw Failure("DISCOVERY_PRIOR");}else if(!prior||m[5]!=prior->root||!digest(m[6]))throw Failure("HELDOUT_PRIOR");EvaluationBinding out;out.root=root.file.at(p+"CORE.sha256").identity.sha;out.prior_core=m[5];out.prior_replay=m[6];out.cumulative_events=udec(m[10]);out.event_hash=m[11];auto banks=lines(root.file.at(p+"banks.tsv").bytes);if(banks.empty()||banks[0]!="version\tsplit\tfactor_bits\tshape\tindex\tN\tA_0\tB_0\tA_1\tB_1\tstatus\tK\trow_count\tpeel_committed\tbasis_committed\tsurvivor_count\tkernel_dimension\tsingleton_count\tsupport_two_count\tL_dimension\tQ_dimension\tquotient_defined\tall_Q_images_global\tdecoder_strict_structural_hit\tlow_hit\tobserved_factor\tevent_count\tevent_sha256\trow_stream_sha256\tpeel_sha256\tbasis_sha256\tdecoder_reservation\tdecoder_call_count\tbank_nonce")throw Failure("EVALUATION_BANK_HEADER");uint64_t bank_events=0;for(size_t i=1;i<banks.size();++i){auto f=fields(banks[i]);if(f.size()!=34||f[0]!=kVersion||f[1]!=split||!decimal(f[2])||!decimal(f[4])||!decimal(f[5])||!decimal(f[26])||!out.N.emplace(key(f[1],f[2],f[3],f[4]),f[5]).second)throw Failure("EVALUATION_BANK");bank_events+=udec(f[26]);}auto ev=lines(root.file.at(p+"events.tsv").bytes);if(ev.empty()||ev[0]!="version\tsplit\tfactor_bits\tshape\tindex\tbank_event_ordinal\tphase\tclass\tside\tcurve\trow_1\trow_2\tmask_present\tmask_0\tmask_1\tmask_2\tmask_3\tmask_4\tg_hex\tbank_nonce")throw Failure("EVENT_HEADER");std::string local;for(size_t i=1;i<ev.size();++i){auto f=fields(ev[i]);if(f.size()!=20||f[0]!=kVersion||f[1]!=split||!out.N.count(key(f[1],f[2],f[3],f[4])))throw Failure("EVENT_ROW");for(size_t j=5;j<20;++j){if(j!=5)local+='\t';local+=f[j];}local+='\n';}out.local_events=ev.size()-1;if(out.local_events!=bank_events)throw Failure("EVENT_BANK_COUNT");out.event_suffix=prior?prior->event_suffix+local:local;if(std::count(out.event_suffix.begin(),out.event_suffix.end(),'\n')!=out.cumulative_events||sha256(out.event_suffix)!=out.event_hash)throw Failure("EVENT_CUMULATIVE_DIGEST");return out;}

struct SealBinding {std::string root,diagnostic_expected;};
SealBinding sealed_root(InputRoot& sealed,const std::string& discovery_public,const std::string& heldout_public,const EvaluationBinding& d,const EvaluationBinding& h){auto r=lines(sealed.file.at("F265-D18.decision.tsv").bytes);if(r.size()!=2||r[0]!="version\tdiscovery_public_sha256\theldout_public_sha256\tdiscovery_core\tdiscovery_replay\theldout_core\theldout_replay\tdecision\theldout_events\theldout_eligible\theldout_decoder_strict_hits\thit_factor_bit_cells\tall_null_clauses\tstatus")throw Failure("SEAL_HEADER");auto f=fields(r[1]);static const std::set<std::string> label{"FINITE_STRUCTURAL_POSITIVE_SIGNAL","FINITE_OTHER_FACTOR_SIGNAL","FINITE_NULL_SIGNAL","FINITE_MIXED_OR_INCONCLUSIVE"};if(f.size()!=14||f[0]!=kVersion||f[1]!=discovery_public||f[2]!=heldout_public||f[3]!=d.root||f[4]!=h.prior_replay||f[5]!=h.root||!digest(f[6])||!label.count(f[7])||f[13]!="PASS")throw Failure("SEAL_ROW");std::string expected=sealed.file.at("F265-D18.decision.tsv").identity.sha+"  F265-D18.decision.tsv\n"+f[3]+"  F265-D18.discovery.CORE.sha256\n"+f[5]+"  F265-D18.heldout.CORE.sha256\n"+f[4]+"  F265-D18.discovery.REPLAY.sha256\n"+f[6]+"  F265-D18.heldout.REPLAY.sha256\n";if(sealed.file.at("F265-D18.SEALED.sha256").bytes!=expected)throw Failure("SEAL_MANIFEST");return{sealed.file.at("F265-D18.SEALED.sha256").identity.sha,""};}

std::string diagnostic_root(InputRoot& diagnostic,const SealBinding& sealed){auto summary=lines(diagnostic.file.at("F265-D18.diagnostic_summary.tsv").bytes);if(summary.size()!=2||summary[0]!="version\tsealed_root\tstatus\tcompleted_tasks\tpair_tasks\tanchored_tasks\tgcd_calls\tcoordinate_multiplications\tpredicate_evaluations\tchord_remainders\tstream_sha256\tnext_task_key\tomitted_details")throw Failure("DIAGNOSTIC_HEADER");auto f=fields(summary[1]);if(f.size()!=13||f[0]!=kVersion||f[1]!=sealed.root||(f[2]!="COMPLETE"&&f[2]!="TIMEOUT")||!digest(f[10]))throw Failure("DIAGNOSTIC_ROW");auto detail=lines(diagnostic.file.at("F265-D18.diagnostic_details.tsv").bytes);if(detail.empty()||detail[0]!="version\ttask_kind\tsplit\tfactor_bits_rank\tshape\tindex\tbasis_ordinal\tcurve\tpair_row_1\tpair_row_2\tthird_row\tpayload")throw Failure("DIAGNOSTIC_DETAIL");std::string expected=diagnostic.file.at("F265-D18.diagnostic_summary.tsv").identity.sha+"  F265-D18.diagnostic_summary.tsv\n"+diagnostic.file.at("F265-D18.diagnostic_details.tsv").identity.sha+"  F265-D18.diagnostic_details.tsv\n"+sealed.root+"  F265-D18.SEALED.sha256\n";if(diagnostic.file.at("F265-D18.DIAGNOSTICS.sha256").bytes!=expected)throw Failure("DIAGNOSTIC_MANIFEST");return diagnostic.file.at("F265-D18.DIAGNOSTICS.sha256").identity.sha;}

struct PrivateLabel {std::string N;cpp_int p,q;};
std::map<std::string,PrivateLabel> private_rows(const DirectFile& file,const std::string& split,const std::vector<PublicRow>& pub){const char* expected=split=="discovery"?kDiscoveryPrivateHash:kHeldoutPrivateHash;if(file.file.identity.sha!=expected)throw Failure("PRIVATE_HASH");auto r=lines(file.file.bytes);if(r.size()!=pub.size()+1||r[0]!="version\tsplit\tshape\tfactor_bits\tindex\tN\tp\tq\tlambda_plus\tlambda_minus\trho_plus\trho_minus")throw Failure("PRIVATE_HEADER");std::map<std::string,const PublicRow*> public_map;for(const auto&x:pub)public_map.emplace(key(x.split,x.bits,x.shape,x.index),&x);std::map<std::string,PrivateLabel> out;for(size_t i=1;i<r.size();++i){auto f=fields(r[i]);if(f.size()!=12||f[0]!="F268-D04"||f[1]!=split)throw Failure("PRIVATE_ROW");for(size_t j=3;j<12;++j)if(j!=2&&!decimal(f[j]))throw Failure("PRIVATE_DECIMAL");std::string k=key(f[1],f[3],f[2],f[4]);auto p=public_map.find(k);if(p==public_map.end()||p->second->N!=f[5])throw Failure("PRIVATE_JOIN");cpp_int a=zdec(f[6]),b=zdec(f[7]),N=zdec(f[5]);if(!(1<a&&a<b&&a*b==N))throw Failure("PRIVATE_FACTORS");if(!out.emplace(k,PrivateLabel{f[5],a,b}).second)throw Failure("PRIVATE_DUPLICATE");}if(out.size()!=public_map.size())throw Failure("PRIVATE_COVERAGE");return out;}

int classify(const Cli& c){DirectFile discovery_public(c.value.at("--discovery-public"),8388608),heldout_public(c.value.at("--heldout-public"),8388608);auto dp=public_rows(discovery_public,"discovery"),hp=public_rows(heldout_public,"heldout");InputRoot de(c.value.at("--discovery-evaluation-root"),kDiscoveryEvaluation),he(c.value.at("--heldout-evaluation-root"),kHeldoutEvaluation),seal(c.value.at("--sealed-root"),kSeal),diag(c.value.at("--diagnostics-root"),kDiagnostics);EvaluationBinding d=evaluation(de,"discovery",discovery_public.file.identity.sha,nullptr),h=evaluation(he,"heldout",heldout_public.file.identity.sha,&d);SealBinding sb=sealed_root(seal,discovery_public.file.identity.sha,heldout_public.file.identity.sha,d,h);std::string diagnostic_hash=diagnostic_root(diag,sb);DirectFile discovery_private(c.value.at("--discovery-private"),8388608),heldout_private(c.value.at("--heldout-private"),8388608);auto dl=private_rows(discovery_private,"discovery",dp),hl=private_rows(heldout_private,"heldout",hp);OutputRoot output(c.value.at("--output-root"));separate(output,{&de,&he,&seal,&diag},{&discovery_public,&heldout_public,&discovery_private,&heldout_private});std::string checks="version\tsplit\tfactor_bits\tshape\tindex\tevent_ordinal\tg_hex\tmatches_private_factor\n";uint64_t checked=0;for(const auto& item:std::array<std::tuple<InputRoot*,std::string,std::map<std::string,PrivateLabel>*>,2>{{{&de,"discovery",&dl},{&he,"heldout",&hl}}}){InputRoot* root=std::get<0>(item);const std::string& split=std::get<1>(item);auto* labels=std::get<2>(item);std::string name="F265-D18."+split+".events.tsv";auto ev=lines(root->file.at(name).bytes);std::string previous;uint64_t ordinal=0;for(size_t i=1;i<ev.size();++i){auto f=fields(ev[i]);if(f.size()!=20)throw Failure("CLASSIFY_EVENT");std::string k=key(f[1],f[2],f[3],f[4]);if(k!=previous){previous=k;ordinal=0;}if(udec(f[5])!=ordinal++)throw Failure("CLASSIFY_EVENT_ORDER");auto label=labels->find(k);if(label==labels->end())throw Failure("CLASSIFY_EVENT_JOIN");cpp_int g=zhex(f[18]);if(g!=label->second.p&&g!=label->second.q)throw Failure("CLASSIFY_FACTOR_MISMATCH");checks+=std::string(kVersion)+"\t"+split+"\t"+f[2]+"\t"+f[3]+"\t"+f[4]+"\t"+f[5]+"\t"+f[18]+"\t1\n";++checked;}}if(checked!=d.local_events+h.local_events)throw Failure("CLASSIFY_EVENT_COUNT");std::string classification="version\tsealed_root\tdiagnostics_root\tdiscovery_private_sha256\theldout_private_sha256\tjoined_rows\tchecked_events\tstatus\n"+std::string(kVersion)+"\t"+sb.root+"\t"+diagnostic_hash+"\t"+discovery_private.file.identity.sha+"\t"+heldout_private.file.identity.sha+"\t"+std::to_string(dl.size()+hl.size())+"\t"+std::to_string(checked)+"\tPASS\n";std::string private_manifest=sha256(classification)+"  F265-D18.private_classification.tsv\n"+sha256(checks)+"  F265-D18.factor_checks.tsv\n"+seal.file.at("F265-D18.SEALED.sha256").identity.sha+"  F265-D18.SEALED.sha256\n"+diag.file.at("F265-D18.DIAGNOSTICS.sha256").identity.sha+"  F265-D18.DIAGNOSTICS.sha256\n";uint64_t total=classification.size()+checks.size()+private_manifest.size();if(total>226088448)throw Failure("PRIVATE_TOTAL_CAP");discovery_public.recheck();heldout_public.recheck();de.recheck();he.recheck();seal.recheck();diag.recheck();discovery_private.recheck();heldout_private.recheck();output.write("F265-D18.private_classification.tsv",classification,1048576);output.write("F265-D18.factor_checks.tsv",checks,15455488);output.write("F265-D18.PRIVATE.sha256",private_manifest,65536);output.finish();return 0;}

}  // namespace f265_d18_private

int main(int argc,char**argv){try{if(!std::setlocale(LC_ALL,"C"))throw f265_d18_private::Failure("LOCALE");umask(077);return f265_d18_private::classify(f265_d18_private::parse_cli(argc,argv));}catch(const std::exception&e){std::cerr<<"F265-D18 private failure: "<<e.what()<<'\n';return 1;}}
