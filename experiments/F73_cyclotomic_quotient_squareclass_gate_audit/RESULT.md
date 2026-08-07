# Hostile audit of F73 — PASS

## Verdict

**PASS.** No blocking defect remains in the local-order premise, quotient
promotion, subgroup expansion, rational square-class gate, complete
\(2\)-saturation, factor extraction, witness, or stated scope.

I used only
`experiments/F73_cyclotomic_quotient_squareclass_gate/RESULT.md` as the
mathematical source. Before reading it, I verified its SHA-256 as

```text
480fa3fbe324dfcc9947ce32724904618e05933d05eb5282c9d4ce344bb8d1f5
```

which is the expected digest.

## 1. Setup and local order

The assumptions force \(c>3\): the only excluded odd prime is \(c=3\), for
which \(N=13\) is not composite. For a prime \(c>3\), the condition
\(3\nmid N\) excludes \(c\equiv1\pmod 3\), so
\(c\equiv2\pmod3\). Hence \(b=(c+1)/3\) is an integer.

The identity

\[
c^3-1=(c-1)(c^2+c+1)=(c-1)N
\]

gives \(c^3\equiv1\pmod{p^e}\) for every prime power \(p^e\mid N\).
Also

\[
\gcd(c-1,N)=\gcd(c-1,3)=1,
\]

where the last equality uses \(3\nmid N\). Thus \(c\not\equiv1\pmod p\),
and a fortiori \(c\not\equiv1\pmod{p^e}\). Its order modulo every such
prime power is therefore exactly \(3\). Since
\(1<c<c^2<N\), the three displayed integers are the distinct canonical
representatives of \(H_0=\langle c\rangle\). Finally,
\([A_0]=[c^3]=[c]\), and this class is nonzero because \(c\) is prime.

## 2. Quotient, inverse, and promoted relation

The quotient in \(A_0=1+(c-1)N\) is exactly \(g=c-1\). It is a unit modulo
\(N\) by the gcd calculation above. Since \(c\equiv2\pmod3\),

\[
w=\frac{c^2-1}{3}=\frac{(c-1)(c+1)}3=gb
\]

is an integer. It satisfies \(0<w<N\), and direct expansion gives

\[
gw=\frac{(c-1)(c^2-1)}3
   =1+\frac{c-2}{3}N.
\]

Thus \(w\) is the canonical inverse of \(g\) modulo \(N\), and (2) is
exact, not merely a congruence.

## 3. Strict subgroup growth survives gcd refinement

The inequalities \(1<g=c-1<c\) show that \(g\) is none of the canonical
representatives \(1,c,c^2\), so \(g\notin H_0\).

Complete gcd refinement preserves every original endpoint as a product of
refined blocks, with multiplicity when required. Consequently the refined
state still generates \(c\), hence all of \(H_0\), and it generates \(g\)
from the blocks refining the endpoint \(g\). Therefore its generated
subgroup contains \(H_0\) and also an element outside \(H_0\); the inclusion
is strict. This reasoning does not use the square class of \(b\), so the
claimed separation of the subgroup and closure gates is valid.

## 4. Exact square-class and closure gate

Because \(A_1=g^2b\), its exact class in
\(\mathbf Q_{>0}^{\times}/(\mathbf Q_{>0}^{\times})^2\) is \([b]\).
Moreover \(\gcd(c,b)=1\). If \([b]=[c]\), then \(bc\) would be a rational
square. A positive integer which is a rational square is an integer square,
but \(v_c(bc)=1\), a contradiction. Hence \([b]\ne[c]\).

If \(b\) is a square, \([b]=0\), while \([c]\ne0\); the kernel of the
two-column parity map is exactly \(\langle(0,1)\rangle\). If \(b\) is not a
square, then \([b]\) and \([c]\) are distinct nonzero vectors. Two distinct
nonzero vectors over \(\mathbf F_2\) are independent, so the kernel is zero.
This proves the stated if-and-only-if gate, including the word
"immediately": among the two displayed relations, the only new dependency
in the closing branch is the singleton \(A_1\).

### Complete \(2\)-saturation adds no missed gate

Let \(\Gamma=\langle A_0,A_1\rangle\subset\mathbf Q_{>0}^{\times}\).
The two values are multiplicatively independent because \(c\nmid A_1\) and
\(A_1>1\). If \(b\) is nonsquare, the injective square-class map just proved
implies that \(x^2\in\Gamma\) forces the two exponents of \(A_0,A_1\) to be
even, and hence \(x\in\Gamma\). Induction gives the same conclusion for
every \(2^k\)-th root. Thus \(\Gamma\) is already completely
\(2\)-saturated in the nonclosing branch.

If \(b=s^2\), then \(A_1=R^2\), with \(R=s(c-1)\), so the first saturation
step adjoins exactly the root detected by the singleton parity dependency.
There is no further hidden \(2\)-division. Indeed, \(s\) is even; writing
\(s=2t\) gives

\[
R=4t(6t^2-1),\qquad \gcd(t,6t^2-1)=1.
\]

If \(R\) were a square, then \(6t^2-1\) would be a square, which is
impossible because it is \(2\pmod3\). Thus \([R]\ne0\). Also
\(\gcd(c,R)=1\), so \([R]\ne[c]\) by the same \(c\)-adic argument as
above. The classes of \(A_0\) and \(R\) are therefore independent, and
\(\langle A_0,R\rangle\) is \(2\)-saturated. Complete saturation adds
nothing beyond the parity decision: it adds no element in the nonsquare
branch and only the already displayed root \(R\) in the square branch.

## 5. Exact factor extraction

Assume \(b=s^2\). Then \(c=3s^2-1\), and oddness of \(c\) forces \(s\) to
be even. Substitution verifies

\[
N=9s^4-3s^2+1
 =(3s^2-3s+1)(3s^2+3s+1)=AB.
\]

For coprimality, a common divisor of \(A,B\) divides \(6s\), while
\(A\equiv1\pmod s\), \(A\equiv1\pmod3\), and \(A\) is odd. Hence
\(\gcd(A,B)=1\). Direct expansion also gives

\[
R-1=(s-1)B,\qquad R+1=(s+1)A.
\]

The identities

\[
A=3s(s-1)+1,\qquad B=3s(s+1)+1
\]

give \(\gcd(s-1,A)=\gcd(s+1,B)=1\). Since \(s\ge2\), both \(A\) and
\(B\) are proper nontrivial factors. Therefore

\[
\gcd(R-1,N)=B,\qquad \gcd(R+1,N)=A
\]

exactly as claimed. This also proves that the root is non-global.

For the witness \(c=11\), all hypotheses hold and
\(b=4\), \(N=133=7\cdot19\), and \(R=20\). Indeed,
\(\gcd(19,133)=19\) and \(\gcd(21,133)=7\).

## 6. Scope audit

The proof establishes only the local statement for the seed relation and its
first quotient-fed relation. The strict subgroup statement does not imply a
dependency; the dependency and factor extraction require the square branch.
Nothing in the proof supplies a density or infinitude result, a general
quotient sampler, an all-input success theorem, a novelty claim, or an
unrestricted factoring algorithm. The source explicitly disclaims all of
these extensions. No scope overreach remains.
