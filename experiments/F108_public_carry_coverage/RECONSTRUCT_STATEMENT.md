# Proof-blind reconstruction statement for F108

Do not read any other file in `experiments/F108_public_carry_coverage/`.
Do not read F106, F107, or the factor-assisted F100 output.  You may read only
this statement and the pinned public input named below.

## General claim to prove or refute

Let a frozen relation batch have endpoint pairs \((c_i,w_i)\), with the unit
column mask \(e_i\) attached to both endpoints.  Apply factor-free gcd
refinement

\[
(x,s),(y,t)\mapsto
(d,s+t),(x/d,s),(y/d,t),\qquad d=\gcd(x,y)>1,
\]

omitting values one and zero masks, until the surviving integers
\((q_j,m_j)\) are pairwise coprime.  Let \(E\) be the product of an explicit
list of public exposure integers.

For each \(q_j\), use only gcd and exact division to compute its largest
divisor \(S_E(q_j)\) supported on primes dividing \(E\).  Prove or refute the
set equality

\[
\{m_j:S_E(q_j)\text{ is nonsquare}\}
=
\{r_p:p\mid E,\ r_p\ne0\},
\]

where

\[
r_p=\sum_i(v_p(c_i)+v_p(w_i)\bmod2)e_i.
\]

Give the bit complexity in terms of the total explicit endpoint and exposure
list bit length.  Explain when it is polynomial in \(\log N\).

## Fixed public reconstruction

Read only

```text
experiments/F98_multiseed_presentation_closure_kill/PUBLIC_REPLAY_OUTPUT.json
```

whose expected SHA-256 is

```text
ee17d7e3ba088f382c0a1c3adec6d1e328ab7a4a814df8d1f6273e41d19c24ab
```

Use its public 166-record certificate at
`decoder.first_useful_certificate.witness_records`.  Reconstruct the C2T
canonical trajectories directly from the public modulus, active pairs,
orientation, exponent range, and modular inverse operation.

For a transition

\[
c_{e+1}=r c_e-a_eN,\qquad
r w_{e+1}=w_e+b_eN,
\]

record \(c_e\) when \(a_e=0\), and record \(w_{e+1}\) when \(b_e=0\).
Exclude a transition when both carries are zero.

Independently verify or refute all of the following:

1. The complete public circuit has 227 distinct nonsquare masks, rank 165,
   and nullity one.
2. The eight oriented trajectories represented by certificate records have
   1,840 raw exposure insertions after 541 two-zero transitions are excluded.
   They expose 191 distinct masks of rank 165.
3. All 54 round-one oriented trajectories have 15,935 raw exposure insertions
   after 6,008 two-zero transitions are excluded.  They expose 200 distinct
   masks of rank 165.
4. These raw exposures may use adjacent relation values outside the selected
   166 columns.  If both adjacent values must be selected circuit columns,
   there are 34 exposure insertions for the eight represented trajectories and
   82 for all trajectories; the resulting exposed row span has rank 54.
5. The all-column dependency has root 132013085 modulo \(N\), with extraction
   gcds 19727 and 10267.

The reconstruction must not factor any endpoint or relation value.  You may
use Sage only for independent binary rank checks that start from your own
factor-free public masks.

## General counterboundary

For the F99 private-row construction, let \(1\le e\le T\), let
\(N_T\equiv1\pmod {2^T}\), and put

\[
c_e=2^e<N_T,
\qquad
w_e=N_T-\frac{N_T-1}{2^e}.
\]

The exact relation is

\[
P_e=c_ew_e=1+(2^e-1)N_T.
\]

For every column \(e\), assume there is a distinct prime \(q_e\) such that

\[
v_{q_e}(P_e)=1,
\qquad
q_e\nmid P_j\quad(j\ne e).
\]

Verify from this displayed canonical-inverse formula that the first carry is
zero and

\[
2w_{e+1}-w_e=N_T.
\]

Explain why its raw carry exposures contain only powers of two, while the
private primes keep \(T\) columns independent.  State exactly why carry
frequency alone does not force a dependency or a non-global root.

## Required artifacts

Write an independent reconstruction source, timeout runner, complete log,
canonical output, manifest, and `RECONSTRUCT.md` in this directory.  Preserve
every failed attempt.  Do not edit any pre-existing file.
