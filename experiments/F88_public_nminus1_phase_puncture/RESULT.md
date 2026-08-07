# F88 — the public exponent N−1 can isolate a small phase component

**Status:** proof-only candidate. No research computation was run. This is a
conditional deterministic decoder for a pure phase feedback state, not an
all-input phase source or factoring algorithm.

## 1. Material difference

F86 contracts a pure phase extension under a smoothness bound on the full old
graph order. The present result removes that global smoothness requirement.

Every synchronized graph subgroup has order dividing the public integer
\(N-1\). Dividing \(N-1\) by powers of one small public prime preserves one
phase component while killing all other order components. The remaining
image can be enumerated whenever one exact primary-gap parameter is
polynomially bounded.

## 2. Public annihilator

Let

\[
N=pq
\]

for distinct odd primes. Let \(H\) be a diagonal graph subgroup, of order
\(h\), and let \(K\ge H\) be a strict pure phase extension:

\[
K_p=H_p,
\qquad
K_q=H_q,
\qquad
c=[K:H]>1.
\]

As in F86, \(K/H\) is cyclic and \(c\mid h\).

### Lemma 1

The old order divides the public exponent:

\[
\boxed{h\mid N-1.}
\tag{1}
\]

### Proof

The two graph projections are isomorphisms, so

\[
h=|H_p|=|H_q|.
\]

Therefore \(h\mid p-1\) and \(h\mid q-1\). Modulo \(h\), both hidden
primes are one, and hence

\[
N-1=pq-1\equiv0\pmod h.
\]

This proves (1). \(\square\)

Thus \(N-1\) kills both the old graph and its phase quotient. The useful
operation is to remove one controlled prime power from this annihilator.

## 3. Exact primary puncture

Choose a prime \(\ell\mid c\), and write

\[
e=v_\ell(N-1),
\qquad
H_\ell=v_\ell(h),
\qquad
C_\ell=v_\ell(c).
\tag{2}
\]

Then

\[
1\le C_\ell\le H_\ell\le e.
\]

Define

\[
j=e-C_\ell+1,
\qquad
E=\frac{N-1}{\ell^j}.
\tag{3}
\]

### Theorem 2

The powered subgroup \(K^E\) is a pure \(\ell\)-phase group with

\[
\boxed{
c_E=\ell,
\qquad
h_E=\ell^{H_\ell-C_\ell+1},
\qquad
|K^E|=\ell^{H_\ell-C_\ell+2}.
}
\tag{4}
\]

It contains exactly

\[
\boxed{2\ell-2}
\tag{5}
\]

positive separators, with density

\[
\boxed{
\frac{2(\ell-1)}{\ell^{H_\ell-C_\ell+2}}.
}
\tag{6}
\]

### Proof

Equation (3) gives

\[
v_\ell(E)=C_\ell-1.
\]

For every prime \(r\ne\ell\), the exponent \(E\) retains the full
\(r\)-valuation of \(N-1\), which is at least \(v_r(h)\) and
\(v_r(c)\). Thus it kills all non-\(\ell\) components of both the old graph
and the phase quotient.

On the \(\ell\)-components,

\[
h_E=\frac{h}{\gcd(h,E)}
=\ell^{H_\ell-C_\ell+1},
\qquad
c_E=\frac{c}{\gcd(c,E)}=\ell.
\]

The pure-phase power formula from F86 gives \(|K^E|=h_Ec_E\), the
separator count \(2c_E-2\), and the displayed density. \(\square\)

The strongest case is

\[
C_\ell=H_\ell.
\]

Then the phase quotient contains the full \(\ell\)-primary part of the old
graph, and

\[
\boxed{|K^E|=\ell^2.}
\tag{7}
\]

No condition is imposed on any other prime-power part of \(h\).

## 4. Public deterministic scan

Fix public polynomial bounds \(L\) and \(S\). Enumerate every prime
\(\ell\le L\) for which \(\ell\mid N-1\). Compute the public valuation
\(e=v_\ell(N-1)\). For every

\[
1\le j\le e,
\]

set

\[
E=(N-1)/\ell^j.
\]

For this exponent:

1. power every public generator of \(K\) by \(E\) modulo \(N\);
2. enumerate the powered subgroup by breadth-first multiplication;
3. stop after more than \(S\) distinct residues;
4. gcd-test every visited residue minus one.

### Corollary 3

The scan deterministically factors \(N\) if there is a prime \(\ell\mid c\)
such that

\[
\boxed{
\ell\le L
\qquad\text{and}\qquad
\ell^{H_\ell-C_\ell+2}\le S.
}
\tag{8}
\]

In particular, it succeeds with \(S=L^2\) whenever some
\(\ell\le L\) satisfies \(C_\ell=H_\ell\).

### Proof

For the prime and exponent in Theorem 2, condition (8) keeps the complete
powered subgroup within the cap. Its nonzero separator count forces one of
the public gcd tests to return a proper factor. Every other exponent is
bounded by the same cap.

There are at most \(L\) candidate primes and at most
\(\log_2(N-1)\) punctures for each. Every exponent has \(O(\log N)\) bits.
For \(L,S\), the public generator count, and their encodings polynomial in
\(\log N\), the full scan has deterministic polynomial bit complexity and
storage. It uses no hidden order, valuation, factor, branch decision, or
cancellation word. \(\square\)

## 5. The F82 phase witness uses E=186

For

\[
N=2047,
\qquad
H=\langle11\rangle,
\qquad
K=\langle11,2\rangle,
\]

one has

\[
h=22,
\qquad
c=11.
\]

Take \(\ell=11\). Then

\[
N-1=2046=2\cdot3\cdot11\cdot31,
\qquad
e=H_{11}=C_{11}=1.
\]

The public puncture is

\[
\boxed{E=(N-1)/11=186.}
\]

It gives

\[
h_E=11,
\qquad
c_E=11,
\qquad
|K^E|=121,
\]

with 20 positive separators. This is the same small factor-bearing phase
image obtained in F86, with a shorter exponent and without assuming that
the other primary components of \(h\) are bounded.

## 6. Scope and remaining source question

The public annihilator removes global smoothness from the pure phase theorem,
but it does not remove every promise. The phase quotient must contain a
publicly scanned small prime, and the valuation gap

\[
H_\ell-C_\ell
\]

must be small enough that the surviving subgroup fits the polynomial cap.
The theorem does not prove either condition for feedback-generated states.

It also assumes that a strict pure phase extension has already been created.
General order/phase mixtures require separate analysis. No all-input feedback
law, inverse-polynomial source probability, arbitrary-composite reduction,
complete factoring algorithm, lower bound, or literature novelty is proved.
