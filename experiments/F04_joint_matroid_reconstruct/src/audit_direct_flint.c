/* Independent direct-minor and sampled global-row audit from the saved matrix. */

#include <flint/flint.h>
#include <flint/nmod_mat.h>
#include <flint/nmod_poly.h>
#include <inttypes.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/stat.h>


static uint64_t *read_global(const char *path, size_t entries)
{
    struct stat status;
    if (stat(path, &status) != 0 || (size_t)status.st_size != entries * sizeof(uint64_t))
        return NULL;
    FILE *file = fopen(path, "rb");
    uint64_t *global = flint_malloc(entries * sizeof(uint64_t));
    if (fread(global, sizeof(uint64_t), entries, file) != entries)
        return NULL;
    fclose(file);
    return global;
}


static int audit_row(
    const uint64_t *global,
    size_t columns,
    uint64_t N,
    size_t row_index,
    size_t r)
{
    uint64_t a = row_index + 1;
    nmod_poly_t base, modulus, power;
    nmod_poly_init(base, (ulong)N);
    nmod_poly_init(modulus, (ulong)N);
    nmod_poly_init(power, (ulong)N);
    nmod_poly_set_coeff_ui(base, 0, (ulong)a);
    nmod_poly_set_coeff_ui(base, 1, 1);
    nmod_poly_set_coeff_ui(modulus, 0, (ulong)(N - 1));
    nmod_poly_set_coeff_ui(modulus, (slong)r, 1);
    nmod_poly_powmod_ui_binexp(power, base, (ulong)N, modulus);

    int matches = 1;
    size_t x_power_column = (size_t)(N % r);
    for (size_t j = 0; j < r; ++j) {
        uint64_t coefficient = nmod_poly_get_coeff_ui(power, (slong)j);
        if (j == x_power_column)
            coefficient = coefficient == 0 ? N - 1 : coefficient - 1;
        if (j == 0)
            coefficient = coefficient >= a ? coefficient - a : coefficient + N - a;
        if (coefficient != global[row_index * columns + j])
            matches = 0;
    }
    nmod_poly_clear(base);
    nmod_poly_clear(modulus);
    nmod_poly_clear(power);
    return matches;
}


static uint64_t direct_determinant(
    const uint64_t *global,
    size_t rows,
    size_t columns,
    uint64_t prime,
    int exchanged)
{
    nmod_mat_t selected;
    nmod_mat_init(selected, (slong)rows, (slong)rows, (ulong)prime);
    for (size_t i = 0; i < rows; ++i) {
        size_t output_column = 0;
        for (size_t j = 0; j < rows; ++j)
            if (!exchanged || (j != 423 && j != 2336))
                nmod_mat_entry(selected, (slong)i, (slong)output_column++)
                    = (ulong)(global[i * columns + j] % prime);
        if (exchanged) {
            nmod_mat_entry(selected, (slong)i, (slong)output_column++)
                = (ulong)(global[i * columns + 2944] % prime);
            nmod_mat_entry(selected, (slong)i, (slong)output_column++)
                = (ulong)(global[i * columns + 2948] % prime);
        }
    }
    uint64_t determinant = nmod_mat_det(selected);
    nmod_mat_clear(selected);
    return determinant;
}


int main(int argc, char **argv)
{
    if (argc != 7) {
        fprintf(stderr, "usage: %s MATRIX N r A p q\n", argv[0]);
        return 2;
    }
    const char *path = argv[1];
    uint64_t N = strtoull(argv[2], NULL, 10);
    size_t r = strtoull(argv[3], NULL, 10);
    size_t A = strtoull(argv[4], NULL, 10);
    uint64_t p = strtoull(argv[5], NULL, 10);
    uint64_t q = strtoull(argv[6], NULL, 10);
    uint64_t *global = read_global(path, A * r);
    if (global == NULL) {
        fprintf(stderr, "global matrix read failed\n");
        return 2;
    }

    size_t sampled_rows[3] = {0, A / 2, A - 1};
    int row_matches[3];
    for (size_t index = 0; index < 3; ++index)
        row_matches[index] = audit_row(global, r, N, sampled_rows[index], r);

    flint_set_num_threads(8);
    uint64_t p_base = direct_determinant(global, A, r, p, 0);
    uint64_t q_base = direct_determinant(global, A, r, q, 0);
    uint64_t p_exchange = direct_determinant(global, A, r, p, 1);
    uint64_t q_exchange = direct_determinant(global, A, r, q, 1);

    const char *run_dir = getenv("F04_RECONSTRUCT_RUN_DIR");
    char output_path[4096];
    snprintf(output_path, sizeof(output_path), "%s/direct_audit.json", run_dir);
    FILE *output = fopen(output_path, "w");
    fprintf(output,
        "{\n"
        "  \"schema\": 1,\n"
        "  \"sampled_global_rows\": [\n"
        "    {\"a\": %zu, \"matches\": %s},\n"
        "    {\"a\": %zu, \"matches\": %s},\n"
        "    {\"a\": %zu, \"matches\": %s}\n"
        "  ],\n"
        "  \"direct_base_determinants\": {\"%" PRIu64 "\": %" PRIu64 ", \"%" PRIu64 "\": %" PRIu64 "},\n"
        "  \"direct_exchanged_determinants\": {\"%" PRIu64 "\": %" PRIu64 ", \"%" PRIu64 "\": %" PRIu64 "}\n"
        "}\n",
        sampled_rows[0] + 1, row_matches[0] ? "true" : "false",
        sampled_rows[1] + 1, row_matches[1] ? "true" : "false",
        sampled_rows[2] + 1, row_matches[2] ? "true" : "false",
        p, p_base, q, q_base, p, p_exchange, q, q_exchange
    );
    fclose(output);
    printf("sampled_rows_match=%d,%d,%d\n", row_matches[0], row_matches[1], row_matches[2]);
    printf("base=%" PRIu64 ",%" PRIu64 " exchange=%" PRIu64 ",%" PRIu64 "\n",
        p_base, q_base, p_exchange, q_exchange);
    flint_free(global);
    flint_cleanup_master();
    return !(row_matches[0] && row_matches[1] && row_matches[2]);
}
