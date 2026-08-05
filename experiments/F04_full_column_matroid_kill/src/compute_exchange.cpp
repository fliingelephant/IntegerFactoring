#include <flint/flint.h>
#include <flint/nmod.h>
#include <flint/nmod_mat.h>
#include <flint/nmod_poly.h>

#include <algorithm>
#include <atomic>
#include <chrono>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <mutex>
#include <numeric>
#include <stdexcept>
#include <string>
#include <thread>
#include <tuple>
#include <vector>

namespace {

constexpr std::uint64_t N = 20000000499999937ULL;
constexpr std::uint64_t P = 100000007ULL;
constexpr std::uint64_t Q = 199999991ULL;
constexpr std::uint32_t A = 2942;
constexpr std::uint32_t R = 2953;
constexpr std::uint32_t EXTRA = R - A;
constexpr char GLOBAL_MAGIC[8] = {'F','0','4','F','C','M','0','1'};
constexpr char C_MAGIC[8] = {'F','0','4','C','M','A','T','1'};

struct Options {
    std::string global_output;
    std::string c_p_output;
    std::string c_q_output;
    std::string entry_output;
    std::string minor_output;
    std::string summary_output;
    unsigned threads = 1;
};

struct LocalResult {
    std::uint64_t prime;
    std::uint64_t determinant;
    std::vector<std::uint64_t> c;
    double solve_seconds;
};

struct EntryRecord {
    std::uint32_t i;
    std::uint32_t j;
    std::uint64_t p_value;
    std::uint64_t q_value;
};

struct MinorRecord {
    std::uint32_t i1;
    std::uint32_t i2;
    std::uint32_t j1;
    std::uint32_t j2;
    std::uint64_t p_value;
    std::uint64_t q_value;
};

struct ExchangeCertificate {
    bool present = false;
    unsigned order = 0;
    std::uint32_t i1 = 0;
    std::uint32_t i2 = 0;
    std::uint32_t j1 = 0;
    std::uint32_t j2 = 0;
    int sign = 1;
    std::uint64_t quotient_p = 0;
    std::uint64_t quotient_q = 0;
    std::uint64_t formula_p = 0;
    std::uint64_t formula_q = 0;
    std::uint64_t direct_p = 0;
    std::uint64_t direct_q = 0;
    std::uint64_t global_value = 0;
    std::uint64_t gcd = 0;
};

Options parse_options(int argc, char** argv) {
    Options o;
    o.threads = std::max(1u, std::thread::hardware_concurrency());
    for (int i = 1; i < argc; ++i) {
        std::string arg = argv[i];
        auto take = [&](std::string& out) {
            if (++i >= argc) throw std::runtime_error("missing value for " + arg);
            out = argv[i];
        };
        if (arg == "--global") take(o.global_output);
        else if (arg == "--c-p") take(o.c_p_output);
        else if (arg == "--c-q") take(o.c_q_output);
        else if (arg == "--entries") take(o.entry_output);
        else if (arg == "--minors") take(o.minor_output);
        else if (arg == "--summary") take(o.summary_output);
        else if (arg == "--threads" && i + 1 < argc) o.threads = std::stoul(argv[++i]);
        else throw std::runtime_error("unknown argument: " + arg);
    }
    if (o.global_output.empty() || o.c_p_output.empty() || o.c_q_output.empty() ||
        o.entry_output.empty() || o.minor_output.empty() || o.summary_output.empty() ||
        o.threads == 0) throw std::runtime_error("incomplete options");
    return o;
}

void write_u32(std::ostream& s, std::uint32_t x) {
    for (unsigned k = 0; k < 4; ++k) s.put(static_cast<char>((x >> (8*k)) & 255));
}

void write_u64(std::ostream& s, std::uint64_t x) {
    for (unsigned k = 0; k < 8; ++k) s.put(static_cast<char>((x >> (8*k)) & 255));
}

std::uint64_t crt(std::uint64_t xp, std::uint64_t xq) {
    const std::uint64_t inv = n_invmod(P % Q, Q);
    const std::uint64_t delta = (xq + Q - xp % Q) % Q;
    const std::uint64_t t = static_cast<std::uint64_t>(
        static_cast<unsigned __int128>(delta) * inv % Q);
    return xp + P*t;
}

void form_global_row(std::uint32_t shift, std::uint64_t* row) {
    nmod_poly_t modulus, base, power;
    nmod_poly_init(modulus, N);
    nmod_poly_init(base, N);
    nmod_poly_init(power, N);
    nmod_poly_set_coeff_ui(modulus, 0, N-1);
    nmod_poly_set_coeff_ui(modulus, R, 1);
    nmod_poly_set_coeff_ui(base, 0, shift);
    nmod_poly_set_coeff_ui(base, 1, 1);
    nmod_poly_powmod_ui_binexp(power, base, N, modulus);
    for (std::uint32_t k = 0; k < R; ++k) row[k] = nmod_poly_get_coeff_ui(power, k);
    nmod_t mod;
    nmod_init(&mod, N);
    row[N % R] = nmod_sub(row[N % R], 1, mod);
    row[0] = nmod_sub(row[0], shift, mod);
    nmod_poly_clear(power);
    nmod_poly_clear(base);
    nmod_poly_clear(modulus);
}

std::vector<std::uint64_t> form_global(unsigned threads, double& seconds) {
    const auto start = std::chrono::steady_clock::now();
    std::vector<std::uint64_t> global(static_cast<std::size_t>(A)*R);
    std::atomic<std::uint32_t> next{0};
    std::vector<std::thread> workers;
    const unsigned count = std::min<unsigned>(threads, A);
    for (unsigned t = 0; t < count; ++t) {
        workers.emplace_back([&]() {
            while (true) {
                const std::uint32_t i = next.fetch_add(1);
                if (i >= A) break;
                form_global_row(i+1, global.data() + static_cast<std::size_t>(i)*R);
            }
        });
    }
    for (auto& worker : workers) worker.join();
    seconds = std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count();
    return global;
}

void write_global(const std::string& path, const std::vector<std::uint64_t>& global) {
    std::ofstream out(path, std::ios::binary | std::ios::trunc);
    out.write(GLOBAL_MAGIC, 8);
    write_u32(out, 1); write_u32(out, A); write_u32(out, R); write_u32(out, 1); write_u32(out, A);
    write_u64(out, N); write_u64(out, P); write_u64(out, Q);
    write_u64(out, static_cast<std::uint64_t>(A)*R);
    for (std::uint32_t i = 0; i < A; ++i) {
        write_u32(out, i+1);
        for (std::uint32_t j = 0; j < R; ++j)
            write_u64(out, global[static_cast<std::size_t>(i)*R+j]);
    }
    if (!out) throw std::runtime_error("failed writing global matrix");
}

LocalResult solve_local(std::uint64_t prime, const std::vector<std::uint64_t>& global) {
    const auto start = std::chrono::steady_clock::now();
    nmod_mat_t base, rhs, solution, check;
    nmod_mat_init(base, A, A, prime);
    nmod_mat_init(rhs, A, EXTRA, prime);
    nmod_mat_init(solution, A, EXTRA, prime);
    nmod_mat_init(check, A, EXTRA, prime);
    for (std::uint32_t i = 0; i < A; ++i) {
        const std::size_t off = static_cast<std::size_t>(i)*R;
        for (std::uint32_t j = 0; j < A; ++j)
            nmod_mat_entry(base, i, j) = global[off+j] % prime;
        for (std::uint32_t j = 0; j < EXTRA; ++j)
            nmod_mat_entry(rhs, i, j) = global[off+A+j] % prime;
    }
    const std::uint64_t determinant = nmod_mat_det(base);
    if (determinant == 0 || !nmod_mat_solve(solution, base, rhs))
        throw std::runtime_error("certified base was singular modulo " + std::to_string(prime));
    nmod_mat_mul(check, base, solution);
    if (!nmod_mat_equal(check, rhs))
        throw std::runtime_error("M0*C != M1 modulo " + std::to_string(prime));
    std::vector<std::uint64_t> c(static_cast<std::size_t>(A)*EXTRA);
    for (std::uint32_t i = 0; i < A; ++i)
        for (std::uint32_t j = 0; j < EXTRA; ++j)
            c[static_cast<std::size_t>(i)*EXTRA+j] = nmod_mat_entry(solution, i, j);
    nmod_mat_clear(check);
    nmod_mat_clear(solution);
    nmod_mat_clear(rhs);
    nmod_mat_clear(base);
    const double elapsed = std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count();
    return {prime, determinant, std::move(c), elapsed};
}

void write_c(const std::string& path, const LocalResult& local) {
    std::ofstream out(path, std::ios::binary | std::ios::trunc);
    out.write(C_MAGIC, 8);
    write_u32(out, 1); write_u32(out, A); write_u32(out, EXTRA); write_u64(out, local.prime);
    for (std::uint64_t x : local.c) write_u64(out, x);
    if (!out) throw std::runtime_error("failed writing C matrix");
}

std::uint64_t det2(const std::vector<std::uint64_t>& c, std::uint32_t i1,
                   std::uint32_t i2, std::uint32_t j1, std::uint32_t j2,
                   nmod_t mod) {
    const std::uint64_t a = c[static_cast<std::size_t>(i1)*EXTRA+j1];
    const std::uint64_t b = c[static_cast<std::size_t>(i1)*EXTRA+j2];
    const std::uint64_t d = c[static_cast<std::size_t>(i2)*EXTRA+j1];
    const std::uint64_t e = c[static_cast<std::size_t>(i2)*EXTRA+j2];
    return nmod_sub(nmod_mul(a,e,mod), nmod_mul(b,d,mod), mod);
}

int exchange_sign(const std::vector<std::uint32_t>& removed) {
    std::uint64_t exponent = 0;
    for (std::uint32_t i : removed) exponent += i+1; // one-based row indices in Laplace expansion
    const std::uint32_t k = removed.size();
    for (std::uint32_t column = A-k+1; column <= A; ++column) exponent += column;
    return exponent % 2 ? -1 : 1;
}

std::uint64_t signed_product(std::uint64_t determinant, std::uint64_t quotient,
                             int sign, std::uint64_t prime) {
    nmod_t mod;
    nmod_init(&mod, prime);
    std::uint64_t value = nmod_mul(determinant, quotient, mod);
    return sign == 1 || value == 0 ? value : prime-value;
}

std::uint64_t direct_exchange_det(const std::vector<std::uint64_t>& global,
                                  std::uint64_t prime,
                                  const std::vector<std::uint32_t>& removed,
                                  const std::vector<std::uint32_t>& extra) {
    std::vector<bool> is_removed(A, false);
    for (std::uint32_t i : removed) is_removed[i] = true;
    std::vector<std::uint32_t> columns;
    columns.reserve(A);
    for (std::uint32_t j = 0; j < A; ++j) if (!is_removed[j]) columns.push_back(j);
    for (std::uint32_t j : extra) columns.push_back(A+j);
    if (columns.size() != A) throw std::runtime_error("bad exchange columns");
    nmod_mat_t matrix;
    nmod_mat_init(matrix, A, A, prime);
    for (std::uint32_t i = 0; i < A; ++i) {
        const std::size_t off = static_cast<std::size_t>(i)*R;
        for (std::uint32_t j = 0; j < A; ++j)
            nmod_mat_entry(matrix,i,j) = global[off+columns[j]] % prime;
    }
    const std::uint64_t determinant = nmod_mat_det(matrix);
    nmod_mat_clear(matrix);
    return determinant;
}

} // namespace

int main(int argc, char** argv) {
    try {
        const Options options = parse_options(argc, argv);
        const auto total_start = std::chrono::steady_clock::now();
        double formation_seconds = 0;
        std::vector<std::uint64_t> global = form_global(options.threads, formation_seconds);
        for (std::uint64_t x : global) if (x >= N) throw std::runtime_error("noncanonical global entry");
        write_global(options.global_output, global);
        std::cout << "formed global matrix in " << formation_seconds << " seconds\n";

        LocalResult p = solve_local(P, global);
        LocalResult q = solve_local(Q, global);
        write_c(options.c_p_output, p);
        write_c(options.c_q_output, q);
        std::cout << "solved local systems in " << p.solve_seconds << " and " << q.solve_seconds << " seconds\n";

        std::vector<EntryRecord> entry_union;
        std::uint64_t entry_zero_p = 0, entry_zero_q = 0, entry_mismatch = 0;
        for (std::uint32_t i = 0; i < A; ++i) for (std::uint32_t j = 0; j < EXTRA; ++j) {
            const std::uint64_t vp = p.c[static_cast<std::size_t>(i)*EXTRA+j];
            const std::uint64_t vq = q.c[static_cast<std::size_t>(i)*EXTRA+j];
            entry_zero_p += vp == 0; entry_zero_q += vq == 0;
            entry_mismatch += (vp == 0) != (vq == 0);
            if (vp == 0 || vq == 0) entry_union.push_back({i,j,vp,vq});
        }
        std::ofstream entry_out(options.entry_output, std::ios::trunc);
        entry_out << "base_row,extra_column,p_value,q_value,p_zero,q_zero\n";
        for (const auto& z : entry_union)
            entry_out << z.i << ',' << z.j << ',' << z.p_value << ',' << z.q_value << ','
                      << (z.p_value==0) << ',' << (z.q_value==0) << '\n';

        const auto scan_start = std::chrono::steady_clock::now();
        const unsigned worker_count = std::min<unsigned>(options.threads, A-1);
        std::vector<std::vector<MinorRecord>> local_records(worker_count);
        std::vector<std::thread> workers;
        for (unsigned worker = 0; worker < worker_count; ++worker) {
            workers.emplace_back([&,worker]() {
                nmod_t mod_p, mod_q;
                nmod_init(&mod_p, P); nmod_init(&mod_q, Q);
                auto& records = local_records[worker];
                for (std::uint32_t i1 = worker; i1+1 < A; i1 += worker_count) {
                    for (std::uint32_t i2 = i1+1; i2 < A; ++i2) {
                        for (std::uint32_t j1 = 0; j1+1 < EXTRA; ++j1) {
                            for (std::uint32_t j2 = j1+1; j2 < EXTRA; ++j2) {
                                const std::uint64_t vp = det2(p.c,i1,i2,j1,j2,mod_p);
                                const std::uint64_t vq = det2(q.c,i1,i2,j1,j2,mod_q);
                                if (vp == 0 || vq == 0) records.push_back({i1,i2,j1,j2,vp,vq});
                            }
                        }
                    }
                }
            });
        }
        for (auto& worker : workers) worker.join();
        std::vector<MinorRecord> minor_union;
        for (auto& records : local_records)
            minor_union.insert(minor_union.end(), records.begin(), records.end());
        std::sort(minor_union.begin(), minor_union.end(), [](const auto& x, const auto& y) {
            return std::tie(x.i1,x.i2,x.j1,x.j2) < std::tie(y.i1,y.i2,y.j1,y.j2);
        });
        const double scan_seconds = std::chrono::duration<double>(std::chrono::steady_clock::now()-scan_start).count();
        std::uint64_t minor_zero_p = 0, minor_zero_q = 0, minor_mismatch = 0;
        std::ofstream minor_out(options.minor_output, std::ios::trunc);
        minor_out << "base_row_1,base_row_2,extra_column_1,extra_column_2,p_value,q_value,p_zero,q_zero\n";
        for (const auto& z : minor_union) {
            minor_zero_p += z.p_value == 0; minor_zero_q += z.q_value == 0;
            minor_mismatch += (z.p_value == 0) != (z.q_value == 0);
            minor_out << z.i1 << ',' << z.i2 << ',' << z.j1 << ',' << z.j2 << ','
                      << z.p_value << ',' << z.q_value << ',' << (z.p_value==0) << ','
                      << (z.q_value==0) << '\n';
        }

        ExchangeCertificate cert;
        std::vector<std::uint32_t> removed, extras;
        if (entry_mismatch) {
            const auto it = std::find_if(entry_union.begin(), entry_union.end(), [](const auto& z) {
                return (z.p_value==0)!=(z.q_value==0);
            });
            cert.present=true; cert.order=1; cert.i1=it->i; cert.j1=it->j;
            cert.quotient_p=it->p_value; cert.quotient_q=it->q_value;
            removed={it->i}; extras={it->j};
        } else if (minor_mismatch) {
            const auto it = std::find_if(minor_union.begin(), minor_union.end(), [](const auto& z) {
                return (z.p_value==0)!=(z.q_value==0);
            });
            cert.present=true; cert.order=2; cert.i1=it->i1; cert.i2=it->i2;
            cert.j1=it->j1; cert.j2=it->j2; cert.quotient_p=it->p_value;
            cert.quotient_q=it->q_value; removed={it->i1,it->i2}; extras={it->j1,it->j2};
        }
        if (cert.present) {
            cert.sign=exchange_sign(removed);
            cert.formula_p=signed_product(p.determinant,cert.quotient_p,cert.sign,P);
            cert.formula_q=signed_product(q.determinant,cert.quotient_q,cert.sign,Q);
            cert.direct_p=direct_exchange_det(global,P,removed,extras);
            cert.direct_q=direct_exchange_det(global,Q,removed,extras);
            if (cert.formula_p!=cert.direct_p || cert.formula_q!=cert.direct_q)
                throw std::runtime_error("determinant quotient identity failed direct verification");
            cert.global_value=crt(cert.direct_p,cert.direct_q);
            cert.gcd=std::gcd(cert.global_value,N);
            if (cert.gcd==1 || cert.gcd==N)
                throw std::runtime_error("local mismatch did not yield a nontrivial global gcd");
        }

        const std::uint64_t total_entries=static_cast<std::uint64_t>(A)*EXTRA;
        const std::uint64_t row_pairs=static_cast<std::uint64_t>(A)*(A-1)/2;
        const std::uint64_t col_pairs=static_cast<std::uint64_t>(EXTRA)*(EXTRA-1)/2;
        const std::uint64_t total_minors=row_pairs*col_pairs;
        const std::uint64_t delta_global=crt(p.determinant,q.determinant);
        const double total_seconds=std::chrono::duration<double>(std::chrono::steady_clock::now()-total_start).count();
        std::ofstream summary(options.summary_output,std::ios::trunc);
        summary << "{\n"
                << "  \"status\": \"pass\",\n"
                << "  \"global_rows_formed_directly_modulo_N\": true,\n"
                << "  \"A\": " << A << ",\n  \"r\": " << R << ",\n"
                << "  \"threads\": " << worker_count << ",\n"
                << "  \"formation_seconds\": " << formation_seconds << ",\n"
                << "  \"p_solve_seconds\": " << p.solve_seconds << ",\n"
                << "  \"q_solve_seconds\": " << q.solve_seconds << ",\n"
                << "  \"scan_2x2_seconds\": " << scan_seconds << ",\n"
                << "  \"total_seconds\": " << total_seconds << ",\n"
                << "  \"delta_p\": " << p.determinant << ",\n"
                << "  \"delta_q\": " << q.determinant << ",\n"
                << "  \"delta_global\": " << delta_global << ",\n"
                << "  \"delta_global_gcd_N\": " << std::gcd(delta_global,N) << ",\n"
                << "  \"entry_statuses\": " << total_entries << ",\n"
                << "  \"entry_zero_p\": " << entry_zero_p << ",\n"
                << "  \"entry_zero_q\": " << entry_zero_q << ",\n"
                << "  \"entry_zero_mismatches\": " << entry_mismatch << ",\n"
                << "  \"two_by_two_statuses\": " << total_minors << ",\n"
                << "  \"two_by_two_zero_p\": " << minor_zero_p << ",\n"
                << "  \"two_by_two_zero_q\": " << minor_zero_q << ",\n"
                << "  \"two_by_two_zero_mismatches\": " << minor_mismatch << ",\n"
                << "  \"certificate_present\": " << (cert.present?"true":"false") << ",\n"
                << "  \"certificate_order\": " << cert.order << ",\n"
                << "  \"certificate_i1\": " << cert.i1 << ",\n"
                << "  \"certificate_i2\": " << cert.i2 << ",\n"
                << "  \"certificate_j1\": " << cert.j1 << ",\n"
                << "  \"certificate_j2\": " << cert.j2 << ",\n"
                << "  \"certificate_sign\": " << cert.sign << ",\n"
                << "  \"certificate_quotient_p\": " << cert.quotient_p << ",\n"
                << "  \"certificate_quotient_q\": " << cert.quotient_q << ",\n"
                << "  \"certificate_formula_p\": " << cert.formula_p << ",\n"
                << "  \"certificate_formula_q\": " << cert.formula_q << ",\n"
                << "  \"certificate_direct_p\": " << cert.direct_p << ",\n"
                << "  \"certificate_direct_q\": " << cert.direct_q << ",\n"
                << "  \"certificate_global_value\": " << cert.global_value << ",\n"
                << "  \"certificate_gcd_N\": " << cert.gcd << "\n}\n";
        if (!summary || !entry_out || !minor_out) throw std::runtime_error("failed writing outputs");
        std::cout << "scanned " << total_entries << " entries and " << total_minors
                  << " two-by-two minors; mismatches=" << entry_mismatch+minor_mismatch << "\n";
        return 0;
    } catch (const std::exception& e) {
        std::cerr << "compute_exchange: " << e.what() << '\n';
        return 1;
    }
}

