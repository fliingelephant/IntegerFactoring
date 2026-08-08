# Blind reconstruction manifest

## Verdict

`PASS_WITH_CORRECTIONS`

## Frozen inputs and artifacts

The SHA-256 values below were computed after the proof, rejected routes, and
report were complete.

| File | SHA-256 |
|:--|:--|
| `RECONSTRUCT_STATEMENT.md` | `e5607787405ff4c8f70df4d6f2ce835180278f0bde47df815875eff85207174a` |
| `RECONSTRUCT_PROOF.md` | `ab367ec8a2853b365e881b88bd4dc1dc2adf1e0ba6d226755934651b5433a56f` |
| `RECONSTRUCT_FAILED_ROUTES.md` | `f6648a860dfefe69940e1f1b7d209c2efbbf3dfe7b989ea1473ceb39f653f8b2` |
| `RECONSTRUCT_REPORT.md` | `4f6008ca54c4bf4efa4b8a2fa849b85c78eeaf467047898eaee701820a41b952` |

The ordinary SHA-256 of this manifest is reported after creation. It is not
embedded here because embedding it would change the file being hashed.

## Deterministic verification record

- The required statement hash matched before reconstruction began.
- A parser checked all 20 Lucas-certificate rows in `RECONSTRUCT_PROOF.md`.
- For each row it checked the complete factorization of `m-1`, dependency
  order of the certified prime factors, `a^(m-1) mod m = 1`, every listed
  modular residue, and every gcd equal to one.
- Exact integer checks verified the product `p*ell`, the value of `r`, the
  bit length, `n^2`, `r mod 30`, and both sign gcds.
- No randomized or probable-prime step was used.

## Blindness and write scope

Before these artifacts were frozen, the only pre-existing file read in
`experiments/F120_complete_carry_closure_theory` was
`RECONSTRUCT_STATEMENT.md`. No candidate proof, audit file, or durable ledger
was read or edited. Only the four new `RECONSTRUCT_` artifacts requested by
the reconstruction task were written.
