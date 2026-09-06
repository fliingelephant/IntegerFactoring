# Proof of the F280 V2 additive repair

## Authenticated imported proof

V2 imports the immutable V1 file `PROOF.md` with SHA-256

```text
6a7871d91a5bd44eb08778633b04f7f0239ded8ca95392481bd6059491c006df
```

in full. Every V1 proof remains unchanged except the terminal
polynomial-\(N\) comparison in V1 Proof Section 4. Apply the exact proof
replacement below after authenticating and reading the V1 proof.

## Exact proof replacement

Replace the final three sentences of V1 Proof Section 4, beginning

```text
If \(D=N^\delta\), substitution into (6) gives
```

and ending

```text
These are only the costs of the named constructions.
```

by the following argument.

Let

\[
 D=N^\delta
\]

for one fixed \(0<\delta<1\). Then

\[
 {D\over N-1}={N^\delta\over N-1}\longrightarrow0.
\]

Hence \(1\le D<N-1\) for all sufficiently large admissible integer inputs.
This is precisely the Harvey--Hittmeir Theorem 1.1 input-domain condition.
Substitution into the source cost (6) gives

\[
 T_{\rm HH}(N,D)=N^{\delta/2+o(1)}.
\]

Under the same standard fast-integer-arithmetic convention as V1,
substitution into the explicit scan cost (3) gives

\[
 O(D\mathsf M(n)\log n)=N^{\delta+o(1)}.
\]

These are only upper-bound costs of the named admissible constructions.
No claim is made for \(\delta\ge1\), where \(D=N^\delta\) violates the
Harvey--Hittmeir input condition.

## No regression in the imported proof

The V1 arguments for the local gcd postprocessor, Nir's bounded-height
composition, the Harvey--Hittmeir composition, the numerical-QP threshold,
synchronized lcm capacity, baseline primary-multiplicity saturation, the
counterexample, and every lane or search boundary are imported byte-for-byte
by hash. V2 changes none of their hypotheses or conclusions.
