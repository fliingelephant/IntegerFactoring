#include <flint/flint.h>
#include <flint/nmod.h>
#include <flint/nmod_poly.h>

#include <cstdint>
#include <fstream>
#include <iostream>
#include <map>
#include <stdexcept>
#include <string>
#include <vector>

namespace {

constexpr std::uint64_t N = 20000000499999937ULL;
constexpr std::uint64_t PRIME_P = 100000007ULL;
constexpr std::uint64_t PRIME_Q = 199999991ULL;
constexpr std::uint32_t R = 2953;
constexpr char MAGIC[8] = {'F', '0', '4', 'G', 'L', 'O', 'B', '1'};
constexpr std::uint32_t SAMPLES[] = {1, 2, 1471, 2942};

std::uint32_t read_u32(std::istream& stream) {
    std::uint32_t value = 0;
    for (unsigned i = 0; i < 4; ++i) {
        const int byte = stream.get();
        if (byte == EOF) throw std::runtime_error("unexpected EOF");
        value |= static_cast<std::uint32_t>(byte) << (8 * i);
    }
    return value;
}

std::uint64_t read_u64(std::istream& stream) {
    std::uint64_t value = 0;
    for (unsigned i = 0; i < 8; ++i) {
        const int byte = stream.get();
        if (byte == EOF) throw std::runtime_error("unexpected EOF");
        value |= static_cast<std::uint64_t>(byte) << (8 * i);
    }
    return value;
}

std::vector<std::uint64_t> direct_global(std::uint32_t shift) {
    nmod_poly_t modulus;
    nmod_poly_t base;
    nmod_poly_t power;
    nmod_poly_init(modulus, N);
    nmod_poly_init(base, N);
    nmod_poly_init(power, N);
    nmod_poly_set_coeff_ui(modulus, 0, N - 1);
    nmod_poly_set_coeff_ui(modulus, R, 1);
    nmod_poly_set_coeff_ui(base, 0, shift);
    nmod_poly_set_coeff_ui(base, 1, 1);
    nmod_poly_powmod_ui_binexp(power, base, N, modulus);
    std::vector<std::uint64_t> result(R);
    for (std::uint32_t k = 0; k < R; ++k) {
        result[k] = nmod_poly_get_coeff_ui(power, k);
    }
    nmod_t mod;
    nmod_init(&mod, N);
    result[N % R] = nmod_sub(result[N % R], 1, mod);
    result[0] = nmod_sub(result[0], shift, mod);
    nmod_poly_clear(power);
    nmod_poly_clear(base);
    nmod_poly_clear(modulus);
    return result;
}

bool flint_chain_is_normal(const std::vector<std::uint64_t>& global, std::uint64_t prime) {
    nmod_poly_t a;
    nmod_poly_t b;
    nmod_poly_t remainder;
    nmod_poly_init(a, prime);
    nmod_poly_init(b, prime);
    nmod_poly_init(remainder, prime);
    nmod_poly_set_coeff_ui(a, 0, prime - 1);
    nmod_poly_set_coeff_ui(a, R, 1);
    for (std::uint32_t k = 0; k < R; ++k) {
        nmod_poly_set_coeff_ui(b, k, global[k] % prime);
    }
    int expected = static_cast<int>(R) - 2;
    bool pass = nmod_poly_degree(b) == static_cast<int>(R) - 1;
    while (pass && nmod_poly_degree(b) > 0) {
        nmod_poly_rem(remainder, a, b);
        if (nmod_poly_degree(remainder) != expected) {
            pass = false;
            break;
        }
        --expected;
        nmod_poly_swap(a, b);
        nmod_poly_swap(b, remainder);
    }
    pass = pass && nmod_poly_degree(b) == 0 && expected == -1;
    nmod_poly_clear(remainder);
    nmod_poly_clear(b);
    nmod_poly_clear(a);
    return pass;
}

}  // namespace

int main(int argc, char** argv) {
    try {
        if (argc != 5 || std::string(argv[1]) != "--input" || std::string(argv[3]) != "--output") {
            throw std::runtime_error("usage: spot_audit --input FILE --output FILE");
        }
        std::ifstream input(argv[2], std::ios::binary);
        char magic[8];
        input.read(magic, 8);
        if (!input || !std::equal(std::begin(magic), std::end(magic), std::begin(MAGIC))) {
            throw std::runtime_error("bad magic");
        }
        const std::uint32_t version = read_u32(input);
        const std::uint32_t r = read_u32(input);
        const std::uint32_t first = read_u32(input);
        const std::uint32_t last = read_u32(input);
        const std::uint64_t n = read_u64(input);
        const std::uint64_t p = read_u64(input);
        const std::uint64_t q = read_u64(input);
        const std::uint64_t coefficient_count = read_u64(input);
        if (version != 1 || r != R || first != 1 || last != 2942 || n != N || p != PRIME_P ||
            q != PRIME_Q || coefficient_count != static_cast<std::uint64_t>(last - first + 1) * R) {
            throw std::runtime_error("header mismatch");
        }
        std::map<std::uint32_t, std::vector<std::uint64_t>> selected;
        for (std::uint32_t index = 0; index <= last - first; ++index) {
            const std::uint32_t shift = read_u32(input);
            bool wanted = false;
            for (std::uint32_t sample : SAMPLES) wanted = wanted || shift == sample;
            if (wanted) selected[shift].resize(R);
            for (std::uint32_t k = 0; k < R; ++k) {
                const std::uint64_t value = read_u64(input);
                if (wanted) selected[shift][k] = value;
            }
        }
        std::uint64_t coefficients_compared = 0;
        std::uint64_t chains_checked = 0;
        for (std::uint32_t shift : SAMPLES) {
            if (!selected.contains(shift)) throw std::runtime_error("missing sample shift");
            const std::vector<std::uint64_t> direct = direct_global(shift);
            if (direct != selected[shift]) {
                throw std::runtime_error("direct composite-modulus power disagrees at shift " +
                                         std::to_string(shift));
            }
            coefficients_compared += R;
            if (!flint_chain_is_normal(selected[shift], PRIME_P) ||
                !flint_chain_is_normal(selected[shift], PRIME_Q)) {
                throw std::runtime_error("independent FLINT Euclidean chain failed at shift " +
                                         std::to_string(shift));
            }
            chains_checked += 2;
        }
        std::ofstream output(argv[4], std::ios::trunc);
        output << "{\n"
               << "  \"status\": \"pass\",\n"
               << "  \"sample_shifts\": [1, 2, 1471, 2942],\n"
               << "  \"direct_composite_modulus_coefficients_compared\": "
               << coefficients_compared << ",\n"
               << "  \"independent_flint_chains_checked\": " << chains_checked << "\n"
               << "}\n";
        std::cout << "spot audit passed\n";
        return 0;
    } catch (const std::exception& error) {
        std::cerr << "spot_audit: " << error.what() << '\n';
        return 1;
    }
}

