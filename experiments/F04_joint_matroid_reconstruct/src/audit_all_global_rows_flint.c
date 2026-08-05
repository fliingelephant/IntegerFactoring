/* Recompute every global row over Z/NZ with an engine independent of Sage. */

#include <flint/flint.h>
#include <flint/nmod_poly.h>
#include <inttypes.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/stat.h>
#include <time.h>


int main(int argc, char **argv)
{
    if (argc != 5) {
        fprintf(stderr, "usage: %s MATRIX N r A\n", argv[0]);
        return 2;
    }
    const char *path = argv[1];
    uint64_t N = strtoull(argv[2], NULL, 10);
    size_t r = strtoull(argv[3], NULL, 10);
    size_t A = strtoull(argv[4], NULL, 10);
    struct stat status;
    if (stat(path, &status) != 0
        || (size_t)status.st_size != A * r * sizeof(uint64_t)) {
        fprintf(stderr, "global matrix size mismatch\n");
        return 2;
    }
    FILE *file = fopen(path, "rb");
    uint64_t *global = flint_malloc(A * r * sizeof(uint64_t));
    if (fread(global, sizeof(uint64_t), A * r, file) != A * r) {
        fprintf(stderr, "global matrix read failed\n");
        return 2;
    }
    fclose(file);

    nmod_poly_t base, modulus, power;
    nmod_poly_init(base, (ulong)N);
    nmod_poly_init(modulus, (ulong)N);
    nmod_poly_init(power, (ulong)N);
    nmod_poly_set_coeff_ui(modulus, 0, (ulong)(N - 1));
    nmod_poly_set_coeff_ui(modulus, (slong)r, 1);
    size_t x_power_column = N % r;
    uint64_t mismatches = 0;
    struct timespec started, now;
    clock_gettime(CLOCK_MONOTONIC, &started);
    for (size_t row = 0; row < A; ++row) {
        uint64_t a = row + 1;
        nmod_poly_zero(base);
        nmod_poly_set_coeff_ui(base, 0, (ulong)a);
        nmod_poly_set_coeff_ui(base, 1, 1);
        nmod_poly_powmod_ui_binexp(power, base, (ulong)N, modulus);
        for (size_t column = 0; column < r; ++column) {
            uint64_t coefficient = nmod_poly_get_coeff_ui(power, (slong)column);
            if (column == x_power_column)
                coefficient = coefficient == 0 ? N - 1 : coefficient - 1;
            if (column == 0)
                coefficient = coefficient >= a
                    ? coefficient - a : coefficient + N - a;
            mismatches += coefficient != global[row * r + column];
        }
        if (row == 0 || (row + 1) % 100 == 0 || row + 1 == A) {
            clock_gettime(CLOCK_MONOTONIC, &now);
            double elapsed = (double)(now.tv_sec - started.tv_sec)
                + 1e-9 * (double)(now.tv_nsec - started.tv_nsec);
            printf("rows_complete=%zu mismatches=%" PRIu64 " elapsed=%.6f\n",
                row + 1, mismatches, elapsed);
            fflush(stdout);
        }
    }
    clock_gettime(CLOCK_MONOTONIC, &now);
    double elapsed = (double)(now.tv_sec - started.tv_sec)
        + 1e-9 * (double)(now.tv_nsec - started.tv_nsec);

    const char *run_dir = getenv("F04_RECONSTRUCT_RUN_DIR");
    char output_path[4096];
    snprintf(output_path, sizeof(output_path), "%s/all_global_rows_audit.json", run_dir);
    FILE *output = fopen(output_path, "w");
    fprintf(output,
        "{\n"
        "  \"schema\": 1,\n"
        "  \"N\": %" PRIu64 ",\n"
        "  \"r\": %zu,\n"
        "  \"A\": %zu,\n"
        "  \"entries_compared\": %zu,\n"
        "  \"mismatches\": %" PRIu64 ",\n"
        "  \"all_match\": %s,\n"
        "  \"elapsed_seconds\": %.9f,\n"
        "  \"factor_inputs\": []\n"
        "}\n",
        N, r, A, A * r, mismatches, mismatches == 0 ? "true" : "false", elapsed
    );
    fclose(output);
    nmod_poly_clear(base);
    nmod_poly_clear(modulus);
    nmod_poly_clear(power);
    flint_free(global);
    flint_cleanup_master();
    return mismatches != 0;
}
