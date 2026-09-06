# F129 candidate: exact support-layer and cross-root accounting

## Status and scope

This is a proof-only decoder theorem. It gives exact accounting for a fixed
finite source of canonical-inverse exact relations. It does not prove that
the F26-Q source has a dependency, that a dependency has a non-global root,
or that a factoring algorithm succeeds on every input.

Throughout, let \(N\geq 3\) be odd. Work after every declared residue has
passed the unit and direct-sign screens. For a unit \(c\), let

\[
\iota_N(c)\in\{1,\ldots,N-1\}
\]

be its least positive inverse, and put

\[
P_N(c)=c\,\iota_N(c)=1+\kappa_N(c)N.
\]

Values equal to one are omitted.

## Intrinsic support layers

Fix the full declared word menu before exact-value deletion. A declared
presentation \(e\) has a canonical residue
\(c(e)\in\{1,\ldots,N-1\}\), the least positive representative of its
unit residue, a generator support
\(\operatorname{supp}(e)\), and the exact value \(P_N(c(e))\).

For a retained exact value \(P\), define its pre-deletion endpoint orbit by

\[
\mathcal O(P)=
\{c(e),\iota_N(c(e)):
  P_N(c(e))=P\}.
\]

The set includes the endpoints from every declared record with exact value
\(P\), not only the first record that survives exact-value deletion. Define

\[
\boxed{
\sigma(P)=
\min\bigl\{
|\operatorname{supp}(e)|:
c(e)\in\mathcal O(P)
\bigr\}.
}
\]

Thus the minimum uses every declared presentation of either endpoint residue
in the complete pre-deletion exact-value orbit. It does not depend on source
order or on the representative retained by exact-value deletion.

Assume every retained value has \(\sigma(P)\ge1\). The omitted value
\(P=1\) is the only value produced by the empty word in the declared source.

Let \(\mathcal L_s\) contain the distinct retained values with
\(\sigma(P)=s\). Empty layers are allowed.

## One aligned parity space

Let \(\mathcal R\) be the set of all rational primes that divide at least one
retained exact value in \(\bigcup_s\mathcal L_s\). Every matrix below uses
this one aligned row space. The column of \(P\) is

\[
v(P)=\bigl(v_r(P)\bmod 2\bigr)_{r\in\mathcal R}.
\]

Let \(A_s\) be the matrix of the columns in \(\mathcal L_s\), and put

\[
U_s=[A_1\;A_2\;\cdots\;A_s],
\qquad
K_s=\ker A_s,
\qquad
\widehat K_s=\ker U_s.
\]

The rational-prime row space is used only to state and prove the theorem.
P66 and P106 give the equivalent factor-free public decoder.

## Theorem 1: exact layer interaction

For \(s\geq2\), embed \(\widehat K_{s-1}\) and \(K_s\) in the old and new
coordinate blocks of \(\widehat K_s\), and define

\[
C_s=
\widehat K_s/
(\widehat K_{s-1}\oplus K_s).
\]

Then

\[
\boxed{
C_s\simeq
\operatorname{im}U_{s-1}\cap\operatorname{im}A_s.
}
\]

In particular, for every \(d\ge1\),

\[
\boxed{
\dim\widehat K_d
=
\sum_{s=1}^{d}\dim K_s
+
\sum_{s=2}^{d}\dim C_s.
}
\]

The first sum counts dependencies contained in one intrinsic support layer.
The second sum counts dependency directions that require old retained values
and the new layer together.

## Theorem 2: the corrected cross-root map

Let

\[
T_N=
\{z\in(\mathbb Z/N\mathbb Z)^\times:z^2=1\}/\{+1,-1\}.
\]

The P66 positive-root construction gives normalized-root homomorphisms on
all displayed kernels. Write

\[
H_{\leq s}=\operatorname{im}(\rho_{\leq s}:\widehat K_s\to T_N),
\qquad
H_s=\operatorname{im}(\rho_s:K_s\to T_N).
\]

There is a canonical relative cross-root map

\[
\boxed{
\bar\rho_s:
C_s\longrightarrow
T_N/(H_{\leq s-1}+H_s).
}
\]

Its image is exactly

\[
\boxed{
\operatorname{im}\bar\rho_s
=
H_{\leq s}/(H_{\leq s-1}+H_s).
}
\]

In general, the assignment \([z]\mapsto\rho_{\le s}(z)\) need not be
well-defined as a map from \(C_s\) directly to \(T_N\). The direct
formulation is valid on the decoder-failure path

\[
H_{\leq s-1}=0
\quad\text{and}\quad
H_s=0.
\]

On that path, \(\bar\rho_s:C_s\to T_N\) is canonical. If the cumulative
normalized-root decoder first becomes useful at layer \(s\), and the pure
layer is not useful, then \(\bar\rho_s\neq0\).

Equivalently, the full retained decoder has nonzero normalized-root image if
and only if some support layer has either

1. a nonzero pure image \(H_s\), or
2. a nonzero relative cross image \(\operatorname{im}\bar\rho_s\).

This is a localization theorem. It does not force either event.

## Theorem 3: shared-row and carry necessities

Let \(S_s\subseteq\mathcal R\) be the rational-prime parity rows that occur
in both \(U_{s-1}\) and \(A_s\). Then

\[
\boxed{\dim C_s\leq |S_s|.}
\]

If every column of \(A_s\) has an odd-valuation rational-prime row that
occurs in no old column and in no other column of \(A_s\), then

\[
\boxed{C_s=0.}
\]

For two canonical values

\[
P=1+\kappa N,
\qquad
P'=1+\kappa'N,
\]

a rational prime row \(r\) can be shared only if

\[
\boxed{
\kappa\equiv\kappa'\equiv-N^{-1}\pmod r.
}
\]

Thus a nonzero layer cross quotient requires at least one old/new carry
collision modulo a shared odd-valuation prime. This condition is necessary
only. A carry congruence or a shared row does not by itself produce an image
intersection, a dependency, or a non-global root.

## Proposition 4: support-two exact-congruence obstruction

Fix an odd \(N\) and an integer \(m\geq1\). Choose pairwise-distinct rational
primes

\[
a_1,\ldots,a_m,b_1,\ldots,b_m
\equiv1\pmod N.
\]

Treat the \(a_i,b_i\) as formal generators. Put the support-one exact values
\(a_i,b_i\) in layer one and the support-two exact values \(a_ib_i\) in
layer two. All values are \(1\bmod N\), all values are distinct, and

\[
K_1=K_2=0,
\qquad
\dim C_2=m.
\]

The cross kernel is generated by the triples

\[
\{a_i,b_i,a_ib_i\},
\]

but every such dependency has positive root

\[
a_ib_i\equiv1\pmod N.
\]

Hence the complete normalized-root image is zero although the cross quotient
can be arbitrarily large.

This construction is not canonical-inverse for two independent reasons.
First, each prime \(a_i\) and \(b_i\) is greater than \(N\), so it cannot be
a nontrivial product of two canonical endpoints below \(N\). Second,
\(a_ib_i>N^2\), while every canonical product
\(c\iota_N(c)\) is strictly less than \(N^2\). The proposition therefore
refutes deductions from parity, retention, and support alone. It is not an
F26-Q counterexample.

## Canonical scope supplied by P111

P111 gives an infinite trial-hard semiprime family with
\(\Theta(n/\log n)\) selected, distinct canonical exact values produced by
declared support-two seed-pair words. Their selected parity matrix contains
an identity private-row submatrix. Consequently, for the selected submatrix
alone, every partition into ordered layers has zero pure kernels and zero
cross quotients.

P111 does not prove that these values have intrinsic minimum support exactly
two. It does not protect the private rows against omitted F26-Q columns. It
does not exclude a different earlier representation with a successful direct
screen. It therefore gives neither a complete-source null nor a failure of
the F26-Q normalized-root decoder.

## Exact consequence for F26-Q

Quasipolynomial enumeration and permanent retention make every intrinsic
polylog-support layer available to the decoder. They do not force progress.
A positive F26-Q theorem must prove two separate arithmetic statements:

1. some layer defeats private rows and creates a pure dependency or a
   nonzero cross quotient; and
2. the resulting pure or relative normalized-root image is nonzero.

The second statement cannot be replaced by a rank or nullity bound.
