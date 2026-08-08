# Amended F99 Boundary Re-audit

## Verdict

**PASS.** The amended boundary is self-contained and supports the claimed counterexample.

This re-audit used only `RECONSTRUCT_STATEMENT.md`, with SHA-256
`9100aa6c2e0e3b9ce42c00b2888d87b41c6f0a43cac2026cd31c1aa2409fd722`.
It did not use another experiment file or a prior reconstruction conclusion. The
original failed statement-reconstruction artifacts were not reopened or changed.

## Universal reconstruction

Let (1\le e\le T). Since (N_T\equiv1\pmod {2^T}), the quotient
((N_T-1)/2^e) is an integer. The boundary also gives (2^e<N_T), so

\[
0<w_e=N_T-\frac{N_T-1}{2^e}<N_T.
\]

Moreover,

\[
2^e w_e
=2^eN_T-(N_T-1)
=1+(2^e-1)N_T
=P_e.
\]

Thus (w_e) is the canonical inverse of (c_e=2^e) modulo (N_T).

For every transition (1\le e<T),

\[
2c_e-c_{e+1}=2^{e+1}-2^{e+1}=0.
\]

Hence the first carry quotient is (a_e=0). Also,

\[
\begin{aligned}
2w_{e+1}-w_e
&=2\left(N_T-\frac{N_T-1}{2^{e+1}}\right)
  -\left(N_T-\frac{N_T-1}{2^e}\right)\\
&=N_T.
\end{aligned}
\]

Hence the inverse carry quotient is (b_e=1). Each transition is therefore a
zero-first-carry transition, but never a two-zero transition.

The exposure rule records (c_e=2^e) and does not record (w_{e+1}). Therefore

\[
E=\prod_{e=1}^{T-1}2^e=2^{T(T-1)/2}.
\]

For (T=1), this is the empty product (E=1), with empty prime support. For
(T\ge2), the prime support is exactly ({2}).

## Full parity rank

Let the parity-incidence matrix have one column for each (P_e) and one row for
each prime. The boundary gives a distinct prime (q_e) with
(v_{q_e}(P_e)=1) and (q_e\nmid P_j) for (j\ne e). Modulo two, the
(q_e)-row is the (e)-th unit vector. The (T) private rows form (I_T).
The full matrix therefore has rank (T) and nullity zero. No nonempty subset of
the (P_e) columns is a parity dependency.

## Exact logical limit

The construction has (T-1) zero-first-carry transitions and public exposure
supported on at most one prime. These facts do not bound the rank of the full
parity-incidence matrix. The private rows make that matrix full rank.

Thus carry frequency alone forces neither a nonempty dependency nor a
non-global square root. A dependency would only supply a square congruence. A
useful non-global root additionally needs mixed CRT signs, equivalently roots
that are not congruent up to a global sign modulo (N_T). The carry data control
neither the missing dependency here nor those signs in a setting where a
dependency exists.

This conclusion concerns the stated relation family and inference only. It does
not rule out unrelated relations or unrelated factoring methods.

## Mechanical check

The independent verifier performed 254,261 checks over all (1\le T\le96) and
congruence multipliers (1,2,3,5,17), using (N_T=1+k2^T). It confirmed the
canonical ranges, product identity, two carry identities, exposure support, and
private-row rank for 480 families. This finite sweep is a consistency check; the
algebra above supplies the universal proof. The verifier performed no
factorization and read no other input.
