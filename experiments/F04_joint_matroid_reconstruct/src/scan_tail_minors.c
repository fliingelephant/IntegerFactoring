/* Exhaustively compare all one- and two-tail exchanges via projective keys. */

#include <inttypes.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/stat.h>


typedef struct {
    uint64_t p_basis;
    uint64_t q_basis;
    uint64_t both_basis;
    uint64_t p_only;
    uint64_t q_only;
    uint64_t neither;
} counts;

typedef struct {
    size_t removed_first;
    size_t removed_second;
    size_t tail_first;
    size_t tail_second;
} difference;


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


static uint64_t multiply_mod(uint64_t a, uint64_t b, uint64_t modulus)
{
    return (uint64_t)(((__uint128_t)a * b) % modulus);
}


static uint64_t *read_matrix(const char *path, size_t entries)
{
    struct stat status;
    if (stat(path, &status) != 0 || (size_t)status.st_size != entries * sizeof(uint64_t))
        return NULL;
    FILE *file = fopen(path, "rb");
    uint64_t *matrix = malloc(entries * sizeof(uint64_t));
    if (fread(matrix, sizeof(uint64_t), entries, file) != entries)
        return NULL;
    fclose(file);
    return matrix;
}


static void record(counts *result, int p_basis, int q_basis)
{
    result->p_basis += p_basis;
    result->q_basis += q_basis;
    result->both_basis += p_basis && q_basis;
    result->p_only += p_basis && !q_basis;
    result->q_only += !p_basis && q_basis;
    result->neither += !p_basis && !q_basis;
}


static void projective_keys(
    const uint64_t *matrix,
    size_t rows,
    size_t columns,
    size_t first,
    size_t second,
    uint64_t prime,
    uint64_t *keys,
    unsigned char *zero)
{
    for (size_t i = 0; i < rows; ++i) {
        uint64_t u = matrix[i * columns + first];
        uint64_t v = matrix[i * columns + second];
        zero[i] = u == 0 && v == 0;
        if (u != 0)
            keys[i] = multiply_mod(v, inverse_mod(u, prime), prime);
        else
            keys[i] = prime;
    }
}


int main(int argc, char **argv)
{
    if (argc != 7) {
        fprintf(stderr, "usage: %s Wp Wq rows tail_columns p q\n", argv[0]);
        return 2;
    }
    size_t rows = strtoull(argv[3], NULL, 10);
    size_t columns = strtoull(argv[4], NULL, 10);
    uint64_t p = strtoull(argv[5], NULL, 10);
    uint64_t q = strtoull(argv[6], NULL, 10);
    size_t entries = rows * columns;
    uint64_t *wp = read_matrix(argv[1], entries);
    uint64_t *wq = read_matrix(argv[2], entries);
    if (wp == NULL || wq == NULL) {
        fprintf(stderr, "solution matrix read failed\n");
        return 2;
    }

    counts one = {0}, two = {0};
    for (size_t i = 0; i < rows; ++i)
        for (size_t j = 0; j < columns; ++j)
            record(&one, wp[i * columns + j] != 0, wq[i * columns + j] != 0);

    uint64_t *kp = malloc(rows * sizeof(uint64_t));
    uint64_t *kq = malloc(rows * sizeof(uint64_t));
    unsigned char *zp = malloc(rows);
    unsigned char *zq = malloc(rows);
    difference p_only_examples[64], q_only_examples[64];
    size_t p_only_examples_count = 0, q_only_examples_count = 0;
    for (size_t first = 0; first < columns; ++first)
        for (size_t second = first + 1; second < columns; ++second) {
            projective_keys(wp, rows, columns, first, second, p, kp, zp);
            projective_keys(wq, rows, columns, first, second, q, kq, zq);
            for (size_t i = 0; i < rows; ++i)
                for (size_t k = i + 1; k < rows; ++k) {
                    int p_basis = !(zp[i] || zp[k] || kp[i] == kp[k]);
                    int q_basis = !(zq[i] || zq[k] || kq[i] == kq[k]);
                    record(&two, p_basis, q_basis);
                    if (p_basis && !q_basis && p_only_examples_count < 64)
                        p_only_examples[p_only_examples_count++] = (difference){
                            i, k, first, second
                        };
                    if (!p_basis && q_basis && q_only_examples_count < 64)
                        q_only_examples[q_only_examples_count++] = (difference){
                            i, k, first, second
                        };
                }
        }

    const char *run_dir = getenv("F04_RECONSTRUCT_RUN_DIR");
    char output_path[4096];
    snprintf(output_path, sizeof(output_path), "%s/tail_minor_scan.json", run_dir);
    FILE *output = fopen(output_path, "w");
    fprintf(output,
        "{\n"
        "  \"schema\": 1,\n"
        "  \"rows\": %zu,\n"
        "  \"tail_columns\": %zu,\n"
        "  \"one_tail\": {\n"
        "    \"total\": %" PRIu64 ", \"p_basis\": %" PRIu64 ", \"q_basis\": %" PRIu64
        ", \"both_basis\": %" PRIu64 ", \"p_only\": %" PRIu64 ", \"q_only\": %" PRIu64
        ", \"neither\": %" PRIu64 "\n"
        "  },\n"
        "  \"two_tail\": {\n"
        "    \"total\": %" PRIu64 ", \"p_basis\": %" PRIu64 ", \"q_basis\": %" PRIu64
        ", \"both_basis\": %" PRIu64 ", \"p_only\": %" PRIu64 ", \"q_only\": %" PRIu64
        ", \"neither\": %" PRIu64 "\n"
        "  },\n"
        "  \"p_only_two_tail_examples\": [",
        rows, columns,
        one.both_basis + one.p_only + one.q_only + one.neither,
        one.p_basis, one.q_basis, one.both_basis, one.p_only, one.q_only, one.neither,
        two.both_basis + two.p_only + two.q_only + two.neither,
        two.p_basis, two.q_basis, two.both_basis, two.p_only, two.q_only, two.neither
    );
    for (size_t index = 0; index < p_only_examples_count; ++index) {
        difference item = p_only_examples[index];
        fprintf(output,
            "%s{\"removed\": [%zu, %zu], \"tail_offsets\": [%zu, %zu]}",
            index == 0 ? "" : ", ",
            item.removed_first, item.removed_second, item.tail_first, item.tail_second
        );
    }
    fprintf(output, "],\n  \"q_only_two_tail_examples\": [");
    for (size_t index = 0; index < q_only_examples_count; ++index) {
        difference item = q_only_examples[index];
        fprintf(output,
            "%s{\"removed\": [%zu, %zu], \"tail_offsets\": [%zu, %zu]}",
            index == 0 ? "" : ", ",
            item.removed_first, item.removed_second, item.tail_first, item.tail_second
        );
    }
    fprintf(output, "]\n}\n");
    fclose(output);
    printf("one_total=%" PRIu64 " one_p_only=%" PRIu64 " one_q_only=%" PRIu64 "\n",
        one.both_basis + one.p_only + one.q_only + one.neither, one.p_only, one.q_only);
    printf("two_total=%" PRIu64 " two_p_only=%" PRIu64 " two_q_only=%" PRIu64 "\n",
        two.both_basis + two.p_only + two.q_only + two.neither, two.p_only, two.q_only);
    free(wp);
    free(wq);
    free(kp);
    free(kq);
    free(zp);
    free(zq);
    return 0;
}
