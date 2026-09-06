#include <algorithm>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <map>
#include <set>
#include <sstream>
#include <stdexcept>
#include <string>
#include <tuple>
#include <utility>
#include <vector>

#include <sys/stat.h>

#include <boost/multiprecision/cpp_int.hpp>

using boost::multiprecision::cpp_int;
using u64 = std::uint64_t;
using u128 = __uint128_t;

namespace {

[[noreturn]] void fail(const std::string& message) {
  throw std::runtime_error(message);
}

void require(bool condition,const std::string& message) {
  if (!condition) fail(message);
}

std::string read_file(const std::string& path) {
  std::ifstream input(path,std::ios::binary);require(bool(input),"open: "+path);
  std::ostringstream out;out<<input.rdbuf();
  require(input.good()||input.eof(),"read: "+path);return out.str();
}

std::vector<std::string> split_tab(const std::string& line) {
  std::istringstream input(line);std::vector<std::string> out;std::string field;
  while (std::getline(input,field,'\t')) out.push_back(field);return out;
}

u64 gcd64(u64 a,u64 b) {
  while (b) {u64 r=a%b;a=b;b=r;}return a;
}

u64 mul_mod(u64 a,u64 b,u64 modulus) {
  return static_cast<u64>((static_cast<u128>(a)*b)%modulus);
}

u64 pow_mod(u64 a,u64 exponent,u64 modulus) {
  u64 out=1%modulus;
  while (exponent) {
    if (exponent&1ULL) out=mul_mod(out,a,modulus);
    a=mul_mod(a,a,modulus);exponent>>=1ULL;
  }
  return out;
}

bool is_prime(u64 n) {
  if (n<2) return false;
  for (u64 p:{2ULL,3ULL,5ULL,7ULL,11ULL,13ULL,17ULL,19ULL,23ULL,29ULL,31ULL,37ULL})
    if (n%p==0) return n==p;
  u64 d=n-1,s=0;while ((d&1ULL)==0) {d>>=1ULL;++s;}
  for (u64 a:{2ULL,325ULL,9375ULL,28178ULL,450775ULL,9780504ULL,1795265022ULL}) {
    if (a%n==0) continue;u64 x=pow_mod(a%n,d,n);
    if (x==1||x==n-1) continue;bool composite=true;
    for (u64 r=1;r<s;++r) {x=mul_mod(x,x,n);if (x==n-1) {composite=false;break;}}
    if (composite) return false;
  }
  return true;
}

int bit_length(u64 value) {
  int bits=0;while (value) {++bits;value>>=1ULL;}return bits;
}

u64 next_prime(u64 start) {
  u64 candidate=start|1ULL;
  for (int attempt=0;attempt<200000;++attempt,candidate+=2) {
    require(candidate>=start,"next-prime overflow");
    if (is_prime(candidate)) return candidate;
  }
  fail("next-prime audit cap");
}

std::vector<u64> distinct_factors(u64 value) {
  std::vector<u64> out;
  for (u64 p=2;static_cast<u128>(p)*p<=value;p+=(p==2?1:2)) {
    if (value%p) continue;out.push_back(p);do value/=p;while (value%p==0);
  }
  if (value>1) out.push_back(value);return out;
}

bool primitive(u64 value,u64 prime) {
  if (!is_prime(prime)||value%prime==0) return false;
  for (u64 divisor:distinct_factors(prime-1))
    if (pow_mod(value%prime,(prime-1)/divisor,prime)==1) return false;
  return true;
}

struct PublicRow {
  std::string split,shape;
  int bits=0,index=0;
  std::string N;
};

struct LabelRow {
  PublicRow public_row;
  u64 p=0,q=0,lp=0,lm=0,rp=0,rm=0;
};

std::vector<PublicRow> parse_public(const std::string& path) {
  std::istringstream input(read_file(path));std::string line;
  require(bool(std::getline(input,line))&&
          line=="version\tsplit\tshape\tfactor_bits\tindex\tN","public header");
  std::vector<PublicRow> out;
  std::set<std::string> moduli;
  while (std::getline(input,line)) {
    if (line.empty()) continue;auto f=split_tab(line);
    require(f.size()==6&&f[0]=="F268-D03","public row");
    require(f[1]=="discovery"||f[1]=="heldout","public split");
    require(f[2]=="random"||f[2]=="neighbor"||f[2]=="safe-safe"||
            f[2]=="marker-control","public shape");
    require(!f[5].empty()&&f[5].find_first_not_of("0123456789")==std::string::npos&&
            moduli.insert(f[5]).second,"public modulus syntax/uniqueness");
    int bits=std::stoi(f[3]),index=std::stoi(f[4]);
    require(bits>=3&&bits<=60&&index>=0,"public bits/index");
    out.push_back({f[1],f[2],bits,index,f[5]});
  }
  return out;
}

std::vector<LabelRow> parse_labels(const std::string& path) {
  std::istringstream input(read_file(path));std::string line;
  require(bool(std::getline(input,line))&&
          line=="version\tsplit\tshape\tfactor_bits\tindex\tN\tp\tq"
                "\tlambda_plus\tlambda_minus\trho_plus\trho_minus","label header");
  std::vector<LabelRow> out;
  while (std::getline(input,line)) {
    if (line.empty()) continue;auto f=split_tab(line);
    require(f.size()==12&&f[0]=="F268-D03","label row");
    out.push_back({{f[1],f[2],std::stoi(f[3]),std::stoi(f[4]),f[5]},
                   std::stoull(f[6]),std::stoull(f[7]),std::stoull(f[8]),
                   std::stoull(f[9]),std::stoull(f[10]),std::stoull(f[11])});
  }
  return out;
}

void verify_marker(const LabelRow& row) {
  require(row.p%24==13&&row.q%72==11,"marker constructor classes");
  require(row.lp>5&&row.lm>5&&row.rp>5&&row.rm>5,"marker lower bound");
  std::set<u64> distinct{row.lp,row.lm,row.rp,row.rm};
  require(distinct.size()==4,"marker distinctness");
  for (u64 marker:distinct) require(is_prime(marker),"marker primality");
  require((row.p-1)%row.lp==0&&(row.p+1)%row.lm==0&&
          (row.q-1)%row.rp==0&&(row.q+1)%row.rm==0,"marker incidence");
  require(primitive(row.q,row.lp)&&primitive(row.q,row.lm)&&
          primitive(row.p,row.rp)&&primitive(row.p,row.rm),"marker cross order");
  require(gcd64(row.p-1,row.q-1)==2&&gcd64(row.p-1,row.q+1)==12&&
          gcd64(row.p+1,row.q-1)==2&&gcd64(row.p+1,row.q+1)==2,
          "marker shifted table");
}

void write_new(const std::string& path,const std::string& bytes) {
  struct stat info{};require(::stat(path.c_str(),&info)!=0,"refuse overwrite: "+path);
  std::ofstream output(path,std::ios::binary);require(bool(output),"open output");
  output.write(bytes.data(),static_cast<std::streamsize>(bytes.size()));
  require(bool(output),"write output");output.close();require(bool(output),"close output");
}

void audit(const std::string& public_path,const std::string& label_path,
           const std::string& bank_path,const std::string& shortfall_path,
           const std::string& output_path) {
  struct stat label_info{};
  require(::stat(label_path.c_str(),&label_info)==0&&
          (label_info.st_mode&0777)==0600,"label file mode is not 0600");
  std::vector<PublicRow> public_rows=parse_public(public_path);
  std::vector<LabelRow> labels=parse_labels(label_path);
  require(!public_rows.empty()&&public_rows.size()==labels.size(),
          "public/label row count");
  const std::string split=public_rows[0].split;
  for (const PublicRow& row:public_rows)
    require(row.split==split,"mixed public split");
  std::istringstream shortfalls(read_file(shortfall_path));std::string shortfall_line;
  require(bool(std::getline(shortfalls,shortfall_line))&&
          shortfall_line=="version\tsplit\tshape\tfactor_bits\tmissing",
          "shortfall header");
  std::map<std::pair<std::string,int>,int> declared_shortfall;
  while (std::getline(shortfalls,shortfall_line)) {
    if (shortfall_line.empty()) continue;
    auto f=split_tab(shortfall_line);
    require(f.size()==5&&f[0]=="F268-D03"&&
            (f[1]=="discovery"||f[1]=="heldout")&&
            f[2]=="marker-control","shortfall row");
    int bits=std::stoi(f[3]),missing=std::stoi(f[4]);
    require(missing>=1&&missing<=2&&
            declared_shortfall.emplace(std::make_pair(f[1],bits),missing).second,
            "shortfall range/uniqueness");
  }
  std::map<int,std::pair<u64,u64>> factors;
  std::map<int,int> marker_counts;
  u64 marker_rows=0;
  for (int i=0;i<static_cast<int>(labels.size());++i) {
    const PublicRow& p=public_rows[i];const LabelRow& l=labels[i];
    require(std::tie(p.split,p.shape,p.bits,p.index,p.N)==
            std::tie(l.public_row.split,l.public_row.shape,l.public_row.bits,
                     l.public_row.index,l.public_row.N),"public/label mismatch");
    require(l.p<l.q&&static_cast<u128>(l.q)<static_cast<u128>(2)*l.p,
            "factor balance");
    require(is_prime(l.p)&&is_prime(l.q),"factor primality");
    require(bit_length(l.p)==p.bits&&bit_length(l.q)==p.bits,
            "factor exact-bit declaration");
    require(cpp_int(l.p)*l.q==cpp_int(p.N),"factor product");
    factors[i]={l.p,l.q};
    if (p.shape=="marker-control") {
      verify_marker(l);++marker_rows;++marker_counts[p.bits];
    }
    else {
      require(l.lp==0&&l.lm==0&&l.rp==0&&l.rm==0,"ordinary marker labels");
      if (p.shape=="safe-safe")
        require(is_prime((l.p-1)/2)&&is_prime((l.q-1)/2),"safe-safe labels");
      if (p.shape=="neighbor") {
        require(next_prime(l.p+2)!=l.q,"neighbor is consecutive");
        u64 minimum_skip=u64(1)<<std::max(2,p.bits/4);
        require(l.q-l.p>=minimum_skip,"neighbor skip interval");
      }
    }
  }
  const std::vector<int> marker_bits=split=="discovery"
      ?std::vector<int>{12,16,20,24}:std::vector<int>{20,24,28,32};
  for (const auto& [bits,count]:marker_counts) {
    (void)count;
    require(std::find(marker_bits.begin(),marker_bits.end(),bits)!=
                marker_bits.end(),"unexpected marker public cell");
  }
  for (int bits:marker_bits) {
    int missing=2-marker_counts[bits];
    require(missing>=0&&missing<=2,"marker cell overfull");
    auto found=declared_shortfall.find({split,bits});
    require((missing==0&&found==declared_shortfall.end())||
            (missing>0&&found!=declared_shortfall.end()&&found->second==missing),
            "marker shortfall mismatch");
  }
  for (const auto& [cell,missing]:declared_shortfall) {
    (void)missing;
    if (cell.first==split)
      require(std::find(marker_bits.begin(),marker_bits.end(),cell.second)!=
                  marker_bits.end(),"unexpected marker shortfall cell");
  }
  std::istringstream banks(read_file(bank_path));std::string line;
  require(bool(std::getline(banks,line)),"bank header absent");
  auto header=split_tab(line);
  auto column=[&](const std::string& name) {
    auto found=std::find(header.begin(),header.end(),name);
    require(found!=header.end(),"bank column absent: "+name);
    return static_cast<int>(found-header.begin());
  };
  int case_column=column("case_index"),factor_column=column("first_factor");
  u64 factor_rows=0;
  while (std::getline(banks,line)) {
    if (line.empty()) continue;auto f=split_tab(line);require(f.size()==header.size(),"bank row");
    int case_index=std::stoi(f[case_column]);
    require(factors.count(case_index),"bank case index");
    cpp_int factor(f[factor_column]);
    if (factor==0) continue;
    auto [p,q]=factors[case_index];
    require(factor==p||factor==q,"public gcd is not a labelled factor");++factor_rows;
  }
  std::ostringstream out;
  out<<"metric\tvalue\nlabel_rows\t"<<labels.size()<<"\nmarker_rows\t"<<marker_rows
     <<"\npublic_factor_bank_rows\t"<<factor_rows<<"\nverdict\tPASS\n";
  write_new(output_path,out.str());
  std::cout<<"LABEL_AUDIT_PASS rows="<<labels.size()<<" marker_rows="<<marker_rows
           <<" factor_rows="<<factor_rows<<'\n';
}

void self_test() {
  require(is_prime(1847)&&is_prime(2621)&&!is_prime(4840987),"primality self-test");
  require(primitive(3,7)&&!primitive(2,7),"primitive self-test");
  std::cout<<"LABEL_AUDIT_SELF_TEST_PASS\n";
}

}  // namespace

int main(int argc,char** argv) {
  try {
    if (argc==2&&std::string(argv[1])=="--self-test") {self_test();return 0;}
    if (argc==7&&std::string(argv[1])=="--audit") {
      audit(argv[2],argv[3],argv[4],argv[5],argv[6]);return 0;
    }
    std::cerr<<"usage: label_audit --self-test | "
               "--audit PUBLIC LABELS BANKS SHORTFALLS OUTPUT\n";
    return 64;
  } catch (const std::exception& error) {
    std::cerr<<"F268_LABEL_AUDIT_FATAL "<<error.what()<<'\n';return 70;
  }
}
