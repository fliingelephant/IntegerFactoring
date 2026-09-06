# F205-D01 result

## Verdict

The preregistered joint-child feature family is a null. The fixed public
transition bank is not universal.

This verdict has narrow scope. It does not show that the complete
factorizations of `K=(N-1)/2` and `E=N-floor(sqrt(N))^2` are useless. It does
not exclude a nonlinear integer decoder, a larger adaptive bank, full
class-group navigation, or another public statistic.

## Selector result

The primary training cohort contained 4,026 bank-hard inputs. The source
scored 1,768 predeclared oriented binary rules and scalar decision stumps.
The training-selected rule was:

```text
predict = NOT(largest prime factor of E is 7 mod 8)
```

Its exact metrics were:

| Cohort | Inputs | Accuracy | Balanced accuracy | Errors |
|---|---:|---:|---:|---:|
| train | 4,026 | 0.5330352707 | 0.5246868013 | 1,880 |
| holdout | 2,444 | 0.4946808511 | 0.4943292618 | 1,235 |

The holdout result is below the preregistered 0.55 null threshold. It is far
below the 0.60 correlation-lead threshold. No next-reciprocal-bit pattern in
the fixed feature family survived holdout.

Among the twenty rules ranked highest on training data, the largest observed
holdout balanced accuracy was 0.5118597986. This is descriptive only. The
preregistered decision concerns the single train-selected rule.

## Fixed public transition bank

The bank found a factor on:

- 974 of 5,000 training inputs;
- 56 of 2,500 larger holdout inputs; and
- 3,805 of 5,570 exhaustive-small inputs.

Thus the observed holdout success rate was 0.0224. The smallest exact bank
failure was

```text
N = 3551 = 53 * 67
B = 59
K = 1775 = 5^2 * 71
E = 70 = 2 * 5 * 7
M = 24850
```

The bank had one global return, certified maximum common order 2, and no
proper gcd. This single certificate refutes universality of the exact fixed
bank. It does not refute adaptive bases or other exponent families.

The frozen F202 witness `2627=37*71` was positive for the bank: base 5 and
the public exponent `phi(K)` gave factor 71. This useful finite event does not
survive as a universal rule because of the `3551` counterexample and many
larger nulls.

## Smallest preserved auxiliary counterexamples

The output preserves these exact smallest observed witnesses:

- Gap support failure: `2627=37*71`, with `K=1313=13*101`,
  `E=26=2*13`, and `d=6=2*3`. The prime 3 is absent from `2*K*E`.
- No split prime from `factor(K)` for discriminant `-4E`: `35=5*7`,
  with `K=17` and `E=10`.
- No second mixed principal norm: `527=17*31`, with `B=22`, `K=263`,
  and `E=43`.
- Ordinary common-order capacity at most 2: `15=3*5`.

Across all stored rows, including the separately repeated frozen witness,
the observed rates were:

| Event | Rate |
|---|---:|
| `d` supported on primes of `2*K*E` | 0.2597352919 |
| at least one split prime in `factor(K)` | 0.7125698110 |
| second mixed principal norm exists | 0.1265725683 |
| `gcd(p-1,q-1)<=2` | 0.6766123479 |

These frequencies are discovery evidence only. The exact individual
counterexamples refute only the corresponding universal auxiliary claims.

## Exact artifacts

- Source SHA-256:
  `9828866096689fc4025b3c0c251d961ccf261873e42590b0e9930217f614a993`.
- Log SHA-256:
  `edec0b6fa3ef8a7981bbf491b0b425a2f28a834dc2b474866cd012df0eca5e4f`.
- Result JSON SHA-256:
  `e9f2e4573631a1d40380bc329f3dcc2537689464471f4828dd6709d76515ad4d`.
- Complete rows SHA-256:
  `2dbbcea5e9f66e45f77b7ba78f4dc059d489ce74e3151a8d8cbc19642bff2abe`.

See `RUN_MANIFEST.md` for the exact remote paths, command, runtime, resource
check, and leakage controls.

