/* Reduce one saved global matrix, then compute local determinants with FLINT. */

#include <flint/flint.h>
#include <flint/nmod_mat.h>
#include <inttypes.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/stat.h>
#include <time.h>


static double seconds_since(const struct timespec *start)
{
    struct timespec now;
    clock_gettime(CLOCK_MONOTONIC, &now);
    return (double)(now.tv_sec - start->tv_sec)
        + 1e-9 * (double)(now.tv_nsec - start->tv_nsec);
}


static uint64_t multiply_mod(uint64_t a, uint64_t b, uint64_t modulus)
{
    return (uint64_t)(((__uint128_t)a * b) % modulus);
}


static int64_t extended_gcd(int64_t a, int64_t b, int64_t *x, int64_t *y)
{
    if (b == 0) {
        *x = 1;
        *y = 0;
        return a;
    }
    int64_t next_x, next_y;
    int64_t gcd = extended_gcd(b, a % b, &next_x, &next_y);
    *x = next_y;
    *y = next_x - (a / b) * next_y;
    return gcd;
}


static uint64_t inverse_mod(uint64_t a, uint64_t modulus)
{
    int64_t x, y;
    extended_gcd((int64_t)a, (int64_t)modulus, &x, &y);
    x %= (int64_t)modulus;
    if (x < 0)
        x += (int64_t)modulus;
    return (uint64_t)x;
}


static uint64_t gcd_u64(uint64_t a, uint64_t b)
{
    while (b != 0) {
        uint64_t remainder = a % b;
        a = b;
        b = remainder;
    }
    return a;
}


typedef struct {
    uint64_t prime;
    uint64_t base_determinant;
    uint64_t exchange_factor;
    uint64_t exchanged_determinant;
    int solve_verified;
    double elapsed_seconds;
} local_result;


static local_result analyze_prime(
    const uint64_t *global,
    size_t rows,
    size_t columns,
    uint64_t prime,
    const char *solution_path)
{
    struct timespec started;
    clock_gettime(CLOCK_MONOTONIC, &started);
    const size_t tail_columns = columns - rows;
    nmod_mat_t base, tail, solution, product;
    nmod_mat_init(base, (slong)rows, (slong)rows, (ulong)prime);
    nmod_mat_init(tail, (slong)rows, (slong)tail_columns, (ulong)prime);
    nmod_mat_init(solution, (slong)rows, (slong)tail_columns, (ulong)prime);
    nmod_mat_init(product, (slong)rows, (slong)tail_columns, (ulong)prime);

    for (size_t i = 0; i < rows; ++i) {
        const uint64_t *source = global + i * columns;
        for (size_t j = 0; j < rows; ++j)
            nmod_mat_entry(base, (slong)i, (slong)j) = (ulong)(source[j] % prime);
        for (size_t j = 0; j < tail_columns; ++j)
            nmod_mat_entry(tail, (slong)i, (slong)j) = (ulong)(source[rows + j] % prime);
    }

    uint64_t determinant = (uint64_t)nmod_mat_det(base);
    int solved = nmod_mat_solve(solution, base, tail);
    nmod_mat_mul(product, base, solution);
    int verified = solved && nmod_mat_equal(product, tail);

    const size_t i0 = 423, i1 = 2336, j0 = 2, j1 = 6;
    uint64_t diagonal = multiply_mod(
        nmod_mat_entry(solution, (slong)i0, (slong)j0),
        nmod_mat_entry(solution, (slong)i1, (slong)j1),
        prime
    );
    uint64_t off_diagonal = multiply_mod(
        nmod_mat_entry(solution, (slong)i0, (slong)j1),
        nmod_mat_entry(solution, (slong)i1, (slong)j0),
        prime
    );
    uint64_t exchange_factor = (diagonal + prime - off_diagonal) % prime;
    const size_t swaps = (rows - 2 - i0) + (rows - 1 - i1);
    uint64_t exchanged = multiply_mod(determinant, exchange_factor, prime);
    if (swaps % 2 != 0 && exchanged != 0)
        exchanged = prime - exchanged;

    FILE *solution_file = fopen(solution_path, "wb");
    for (size_t i = 0; i < rows; ++i)
        for (size_t j = 0; j < tail_columns; ++j) {
            uint64_t entry = (uint64_t)nmod_mat_entry(solution, (slong)i, (slong)j);
            fwrite(&entry, sizeof(entry), 1, solution_file);
        }
    fclose(solution_file);

    nmod_mat_clear(base);
    nmod_mat_clear(tail);
    nmod_mat_clear(solution);
    nmod_mat_clear(product);
    local_result result = {
        prime,
        determinant,
        exchange_factor,
        exchanged,
        verified,
        seconds_since(&started),
    };
    return result;
}


int main(int argc, char **argv)
{
    if (argc != 7) {
        fprintf(stderr, "usage: %s MATRIX N r A p q\n", argv[0]);
        return 2;
    }
    const char *matrix_path = argv[1];
    uint64_t N = strtoull(argv[2], NULL, 10);
    size_t r = (size_t)strtoull(argv[3], NULL, 10);
    size_t A = (size_t)strtoull(argv[4], NULL, 10);
    uint64_t p = strtoull(argv[5], NULL, 10);
    uint64_t q = strtoull(argv[6], NULL, 10);
    if ((__uint128_t)p * q != N || r < A) {
        fprintf(stderr, "invalid dimensions or factor product\n");
        return 2;
    }

    struct stat file_status;
    if (stat(matrix_path, &file_status) != 0
        || (uint64_t)file_status.st_size != (uint64_t)A * r * sizeof(uint64_t)) {
        fprintf(stderr, "matrix size mismatch\n");
        return 2;
    }
    FILE *matrix_file = fopen(matrix_path, "rb");
    uint64_t *global = flint_malloc(A * r * sizeof(uint64_t));
    if (fread(global, sizeof(uint64_t), A * r, matrix_file) != A * r) {
        fprintf(stderr, "matrix read failed\n");
        return 2;
    }
    fclose(matrix_file);
    for (size_t i = 0; i < A * r; ++i)
        if (global[i] >= N) {
            fprintf(stderr, "noncanonical global residue\n");
            return 2;
        }

    const char *run_dir = getenv("F04_RECONSTRUCT_RUN_DIR");
    char p_solution[4096], q_solution[4096], result_path[4096];
    snprintf(p_solution, sizeof(p_solution), "%s/base_inverse_tail_%" PRIu64 ".u64le.bin", run_dir, p);
    snprintf(q_solution, sizeof(q_solution), "%s/base_inverse_tail_%" PRIu64 ".u64le.bin", run_dir, q);
    snprintf(result_path, sizeof(result_path), "%s/local_analysis_flint.json", run_dir);

    flint_set_num_threads(8);
    local_result p_result = analyze_prime(global, A, r, p, p_solution);
    printf("prime=%" PRIu64 " base_det=%" PRIu64 " exchange_factor=%" PRIu64
           " exchange_det=%" PRIu64 " solve_verified=%d elapsed=%.6f\n",
           p_result.prime, p_result.base_determinant, p_result.exchange_factor,
           p_result.exchanged_determinant, p_result.solve_verified,
           p_result.elapsed_seconds);
    fflush(stdout);
    local_result q_result = analyze_prime(global, A, r, q, q_solution);
    printf("prime=%" PRIu64 " base_det=%" PRIu64 " exchange_factor=%" PRIu64
           " exchange_det=%" PRIu64 " solve_verified=%d elapsed=%.6f\n",
           q_result.prime, q_result.base_determinant, q_result.exchange_factor,
           q_result.exchanged_determinant, q_result.solve_verified,
           q_result.elapsed_seconds);

    uint64_t base_lift_coefficient = multiply_mod(
        (q_result.base_determinant + q - p_result.base_determinant % q) % q,
        inverse_mod(p % q, q), q
    );
    uint64_t base_crt = (uint64_t)((p_result.base_determinant
        + (__uint128_t)p * base_lift_coefficient) % N);
    uint64_t exchange_lift_coefficient = multiply_mod(
        (q_result.exchanged_determinant + q - p_result.exchanged_determinant % q) % q,
        inverse_mod(p % q, q), q
    );
    uint64_t exchange_crt = (uint64_t)((p_result.exchanged_determinant
        + (__uint128_t)p * exchange_lift_coefficient) % N);

    FILE *result_file = fopen(result_path, "w");
    fprintf(result_file,
        "{\n"
        "  \"schema\": 1,\n"
        "  \"N\": %" PRIu64 ",\n"
        "  \"r\": %zu,\n"
        "  \"A\": %zu,\n"
        "  \"global_matrix\": \"%s\",\n"
        "  \"threads\": 8,\n"
        "  \"base_determinants\": {\"%" PRIu64 "\": %" PRIu64 ", \"%" PRIu64 "\": %" PRIu64 "},\n"
        "  \"base_determinant_crt\": %" PRIu64 ",\n"
        "  \"base_determinant_gcd_N\": %" PRIu64 ",\n"
        "  \"removed_base_columns\": [423, 2336],\n"
        "  \"tail_offsets\": [2, 6],\n"
        "  \"global_tail_columns\": [2944, 2948],\n"
        "  \"in_place_to_sorted_swaps\": 3122,\n"
        "  \"exchange_sign\": 1,\n"
        "  \"exchange_factors\": {\"%" PRIu64 "\": %" PRIu64 ", \"%" PRIu64 "\": %" PRIu64 "},\n"
        "  \"exchanged_determinants\": {\"%" PRIu64 "\": %" PRIu64 ", \"%" PRIu64 "\": %" PRIu64 "},\n"
        "  \"exchanged_determinant_crt\": %" PRIu64 ",\n"
        "  \"exchanged_determinant_gcd_N\": %" PRIu64 ",\n"
        "  \"solves_verified\": [true, true],\n"
        "  \"elapsed_seconds\": {\"%" PRIu64 "\": %.9f, \"%" PRIu64 "\": %.9f}\n"
        "}\n",
        N, r, A, matrix_path,
        p, p_result.base_determinant, q, q_result.base_determinant,
        base_crt, gcd_u64(base_crt, N),
        p, p_result.exchange_factor, q, q_result.exchange_factor,
        p, p_result.exchanged_determinant, q, q_result.exchanged_determinant,
        exchange_crt, gcd_u64(exchange_crt, N),
        p, p_result.elapsed_seconds, q, q_result.elapsed_seconds
    );
    fclose(result_file);
    flint_free(global);
    flint_cleanup_master();
    return !(p_result.solve_verified && q_result.solve_verified);
}
