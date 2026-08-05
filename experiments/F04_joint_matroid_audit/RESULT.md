# F04 joint-matroid hostile audit

**Audit family:** `F04_joint_matroid_audit`  
**Audited family:** `F04_joint_matroid_kill`

## Verdict

The candidate result is **correct as explicitly scoped**.  Its P14 and P11
arithmetic, global-matrix provenance, ranks, prefix determinants, CRT values,
and stated linear-algebra lemma all survive fresh reconstruction.

Its scope cannot be widened to the complete column matroid or to all maximal
Pluecker supports.  On the same P11 matrix, the two local column matroids are
in fact different.  A fixed 2942-column minor has residues

\[
15564403\pmod {100000007},\qquad 0\pmod {199999991},
\]

and its CRT lift has gcd `199999991` with `N`.

This is not a contradiction in the candidate text: its Scope section already
disclaims complete column-matroid equality.  It is a sharp boundary on what
the advertised “counterexample” kills.

## Correct theorem boundary

Write an `A`-by-`r` local matrix as

\[
M_\ell=[B_\ell\mid T_\ell],\qquad B_\ell=M_\ell[:,0:A].
\]

If `det(B_l) != 0`, then:

- all `A` rows are independent, so the complete row matroid on those rows is
  the free matroid;
- every row-prefix rank is its number of rows;
- every full-row column-prefix rank is `min(t,A)`;
- the lexicographically first column basis is `0,...,A-1`.

These conclusions are exactly the candidate lemma and are valid.  They do not
determine any other column basis.

For the P11 tail, set `C_l = B_l^(-1) T_l`.  Replacing prefix column `i` by
tail column `A+u` gives

\[
\det M_\ell[(B\setminus\{i\})\cup\{A+u\}]
=(-1)^{A-1-i}\det(B_\ell)C_{\ell,i,u}.
\]

Replacing prefix columns `i<j` by tail columns `A+u<A+v` gives

\[
\det M_\ell[(B\setminus\{i,j\})\cup\{A+u,A+v\}]
=(-1)^{i+j+1}\det(B_\ell)
\det C_\ell[\{i,j\},\{u,v\}].
\]

Thus a common invertible prefix only proves that one basis is common.  Equality
of the remaining normalized minor zero patterns is additional information.

## Fresh P14 verification

For

\[
N=79403=271\cdot293,\qquad (A,r)=(266,269),
\]

the fresh joint construction reproduced global-matrix SHA-256

```text
170e8b80ca1c4e6a5f335c376a4a8ebd3c95c782f2b9d74da1d4ab9cd3f997d7
```

and the exact local data:

| characteristic | full rank | prefix determinant | raw local zeros |
| ---: | ---: | ---: | ---: |
| 271 | 23 | 0 | 65191 |
| 293 | 266 | 30 | 1 |

The same reconstructed global matrix has 65192 nonunit entries.  CRT gives
prefix determinant `71815 mod 79403`, with gcd `271`.  The exact ranks and the
P14 separator are therefore confirmed.  The candidate's Lucas/Vandermonde
explanation is consistent with these values; this audit does not need that
explanation to certify the ranks.

## Fresh P11 verification

For

\[
N=20000000499999937=100000007\cdot199999991,
\qquad (A,r)=(2942,2953),
\]

the fresh build formed each row once over `Z/NZ` and assigned the same
coefficient vector to both local matrices before either local solve.  A
separate certificate then reconstructed all `8,687,726` global entries from
the retained local matrices by CRT and reproduced every candidate row hash and
the aggregate SHA-256

```text
85c4bcda5ff5d0f23117721a503fedb77e3a84b9d708a3ceb0f7bed1673c6f53
```

The exact prefix data also agree:

| characteristic | full rank | prefix determinant | raw local zeros |
| ---: | ---: | ---: | ---: |
| 100000007 | 2942 | 56136614 | 0 |
| 199999991 | 2942 | 132391112 | 0 |

Every raw global entry is a unit.  The prefix CRT residue is
`16315256998204520`, with gcd 1.  Hence both row matroids really are the same
free matroid, and every named one-axis profile in the candidate really agrees.

## Explicit column-matroid separator

The tail has only 11 columns.  Both exact systems `B_l C_l = T_l` were solved
and checked by full matrix multiplication.

- All `2942*11 = 32,362` one-tail exchanges are bases in both fields: neither
  normalized matrix has a zero entry.
- All `binomial(11,2)*binomial(2942,2) = 237,941,605` two-tail exchanges per
  field were scanned exactly by grouping the 2942 normalized row pairs by
  projective direction.
- Exactly two zero-support mismatches occur.  Both are nonzero modulo
  `100000007` and zero modulo `199999991`.

The first mismatch replaces prefix columns `{423,2336}` with global columns
`{2944,2948}`.  The selected columns are ordered as all surviving prefix
columns followed by the two tail columns.  Here

\[
(-1)^{423+2336+1}=+1,
\]

the normalized `2`-by-`2` determinants are `67899852` and `0`, and the
exchange-minor formula gives `15564403` and `0`.  Direct dense determinant
computations on the two selected 2942-column submatrices independently give
the same residues.

CRT gives

\[
D\equiv2473353088699106\pmod N,
\qquad \gcd(D,N)=199999991.
\]

Therefore this column set is a basis modulo `100000007` but not modulo
`199999991`.  The complete column matroids and maximal Pluecker supports are
different.  Moreover, the globally fixed family of all two-tail exchanges
from the canonical prefix basis exposes a factor on this P11 input.  Because
the prefix determinant is a unit modulo `N`, the normalization can in
principle be performed directly over `Z/NZ`; factor knowledge is not required
to define this family or take the final gcd.

## What P11 does and does not kill

| Invariant or family | P11 conclusion |
| --- | --- |
| Complete row matroid on the 2942 fixed shifts | Killed: both are free |
| All row-prefix ranks | Killed: both equal `s` |
| All full-row column-prefix ranks | Killed: both equal `min(t,2942)` |
| Lexicographically first column basis | Killed: both are `0,...,2941` |
| Canonical first-2942-column minor | Killed: both local residues are nonzero and its global residue is a unit |
| Raw-entry gcd scan | Killed: all entries are units |
| Complete column matroid / maximal Pluecker support | Not killed: explicitly different |
| All one-tail exchanges from the prefix basis | Killed on P11: all are bases in both fields |
| All two-tail exchanges from the prefix basis | Not killed: exactly two support mismatches; one yields factor `199999991` |
| Maximal exchanges using 3 through 11 tail columns | Not scanned here |
| Two-dimensional prefix-rectangle ranks | Not scanned here |
| Nonstandard shifts/moduli or nonlinear joint invariants | Not addressed |
| Uniform separation theorem for a richer minor family | Still open; success on P11 is not a universal theorem |

## Provenance and timeout audit

The candidate numerical artifacts are reproducible, and every recorded source
hash checked out.  Its timeout evidence is weaker than its manifest claims:
the manifest names shell `timeout` commands and says they exited 0, but the
seven retained logs contain no machine-readable start/finish envelopes and
there is no retained per-run status directory.  Consequently the retained
candidate artifacts do not independently prove that those wrappers ran or
exited as stated.

Every fresh run used a runner that records the exact command, hard limit,
start/end timestamps, wall duration, timeout flag, exit code, disposition,
and log hash.  Three failed attempts are retained and excluded from all
claims:

- A02 timed out after 900 seconds while coupling both tail solves in one run.
- A03 saved both full matrices, then exited 1 while serializing a Sage integer
  to JSON.
- A04 exited 1 on the same integer-serialization boundary during recovery.

A05 is the authoritative validation of A03's saved matrices: it CRT-rebuilt
and re-hashed every global entry, recomputed both prefix determinants, and
fixed both matrix artifact hashes before A06/A07 loaded them.  No claim relies
on A02 or A04.  The original A03 matrix objects are retained unmodified and
uncompressed; together they occupy `829,542,004` bytes.  Exact sizes and
SHA-256 values are in `RUN_MANIFEST.md` and A05.

The complete artifact audit is `output/A09_artifact_audit.json` with
`audit_passed=true`.
