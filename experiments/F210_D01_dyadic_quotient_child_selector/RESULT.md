# F210-D01 result

## Verdict

The preregistered selector menu and public action bank are both holdout nulls
in both recursion cohorts.

The late-safe result is the relevant algorithmic outcome. Complete
factorizations of all four fixed-ratio children did not produce a stable
next-bit rule or a frequent direct transition in this fixed family. The
experiment therefore supplies no QP beta-two selector.

This verdict is narrow. It does not rule out another asymmetric integer
statistic, a larger adaptive action bank, a nonlinear joint decoder, or a
genuine one-child transition.

## Selector results

The frozen menu contained 222 oriented rules. Rows with a direct public
factor exit were excluded before rule selection.

| Cohort | Selected training rule | Train BA | Holdout rows | Holdout BA | Errors | Verdict |
|---|---|---:|---:|---:|---:|---|
| early unsafe | predict `t parity` | 0.516574 | 4,492 | 0.499720 | 2,248 | `fixed_menu_null` |
| late safe | choose by `max(K,H)` count of support primes `3 mod 8` | 0.518597 | 4,036 | 0.478791 | 2,112 | `fixed_menu_null` |

The early selected rule was only a public baseline. The late selected rule
was a genuine child-factorization comparison, but it reversed below chance
on the larger holdout inputs.

This was not an isolated selected-rule accident. Among the twenty rules
ranked highest on training data:

- early holdout balanced accuracy ranged from 0.494790 to 0.513508; and
- late holdout balanced accuracy ranged from 0.478791 to 0.503252.

The smallest early selected-rule error was

`N=17989687139=132047*136237`, at `t=2,u=3`.

The smallest late selected-rule error was the same input at `t=6,u=47`.
Each error is an exact counterexample to universality of its selected rule.

## Public action bank

| Cohort | Train success | Holdout success | Holdout failures | Holdout verdict |
|---|---:|---:|---:|---|
| early unsafe | 995/6,242 = 15.9404% | 63/4,555 = 1.3831% | 4,492 | `fixed_action_null` |
| late safe | 867/5,115 = 16.9501% | 79/4,115 = 1.9198% | 4,036 | `fixed_action_null` |

The fixed bank therefore had a strong input-size effect. Its apparent
training lead collapsed below the preregistered 5% null boundary on the
disjoint larger holdout cohort.

The smallest late-safe bank failure was

```text
N = 17989687139 = 132047 * 136237
t = 5
u = 15
K = [281088852, 281088851]
H = [562177657, 562177717]
factor(K0) = 2^2 * 3 * 11 * 37 * 67 * 859
factor(K1) = 29 * 9692719
factor(H0) = 43 * 619 * 21121
factor(H1) = 562177717
```

No action in the exact frozen bank produced a proper gcd on that row. This
refutes universality of the bank even in the recursion-safe regime.

Across all 24,762 rows, first successful certificates were 6 direct gcds,
4,436 minus-power gcds, and 999 plus-power gcds. These finite successes do
not repair the holdout null.

## Quotient geometry

`K0==K1` occurred on 4,726 rows. The smallest retained example was

```text
N = 299 = 13 * 23
t = 1
u = 1
K = [74, 74]
H = [149, 145]
```

`H0==H1` occurred on no tested row. Thus the crossed quotients frequently
break the literal K-child coalescence. Their raw asymmetry is real, but the
frozen factorization and action transcripts did not orient it on holdout.

## Data and integrity

- Runtime: 108.76 seconds, one remote process, successful exit.
- Training stage rows: 11,357.
- Holdout stage rows: 8,670.
- Exhaustive-small stage rows: 4,735.
- Total rows: 24,762.
- Gzip integrity: passed.

Artifact hashes:

- log:
  `a6cb772d20a60ed90a0e37f84ee077db1ccd7b36af782e53fe2091e1f9d35ac7`;
- result JSON:
  `7e5e62a0d9012ad8ad57ea9ed6f44d4591610e0cb9cff457ecf4f2e1197f0a16`;
- compressed rows:
  `8ad41104ae3873c24c89a2fb9303d54344a197bc6611c04722bb56b64adafabe`.

See `RUN_MANIFEST.md` for the exact frozen inputs, remote command, preflight,
pair-list hashes, byte counts, and leakage checks.

## Exact scope

The late-safe null applies only to the 222 frozen branch-equivariant rules
and the exact frozen base/exponent bank. The early null is diagnostic because
factoring four near-size children there is not known to be QP.

Nothing here contradicts the valid recurrence

`T(n) <= T(n-1)+QP(n)`.

The experiment does not test an evaluator that chooses one child before
factoring all siblings. It also does not test arbitrary integer floors,
continued fractions, adaptive exact division, nonlocal support statistics,
or other nonlinear use of the complete child factorizations.
