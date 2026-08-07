# F82 — canonical integer feedback can create a phase-only subgroup expansion

**Status:** candidate exact witness discovered by preregistered finite search.
The certificate below is proved directly and does not depend on search
exhaustiveness. This is not an all-input selector or a factoring algorithm.

## 1. Closest prior result and material difference

P78 proves that canonical feedback can expose a block outside a
separator-free old subgroup. P86 shows that its \(N=4033\) descendant has
unequal local orders, so a pure smooth power factors. F81 gives an abstract
equal-order phase model in which every pure power fails and a mixed old/new
word is necessary.

The present witness realizes that phase branch with literal canonical
integers and gcd-free refinement. It proves that actual feedback expansion is
not always reducible to a power search on the new block.

## 2. The old synchronized state

Let

\[
N=2047=23\cdot89,
\qquad
a=11.
\]

The public canonical inverse relations are

\[
11\cdot1861=1+10N
\tag{1}
\]

and

\[
312\cdot269=1+41N.
\tag{2}
\]

Also,

\[
11^4\equiv312\pmod N,
\qquad
11^{-4}\equiv269\pmod N.
\]

The four positive endpoints

\[
11,\ 1861,\ 312,\ 269
\]

are distinct, greater than one, and pairwise coprime. Complete gcd-free
refinement therefore leaves them as four whole blocks. Every block residue
is a power of \(11\), while \(11\) itself is present. Thus the old
block-generated subgroup is exactly

\[
H_0=\langle11\rangle.
\]

Modulo \(23\),

\[
11^{10}\equiv2,
\qquad
11^{11}\equiv-1.
\]

Modulo \(89\),

\[
11^{10}\equiv8,
\qquad
11^{11}\equiv-1.
\]

Since \(11\not\equiv-1\) in either field, these calculations prove that
\(11\) has exact order \(22\) in both fields. Every old power reaches \(+1\)
at the same exponents in both fields and reaches \(-1\) at the same
exponents congruent to \(11\pmod{22}\). Hence \(H_0\) has no direct sign
separator.

None of the old endpoints is a nontrivial integer perfect power. In fact,
\(11,1861,269\) are prime and

\[
312=2^3\cdot3\cdot13.
\]

Thus exact perfect-power extraction does not change the old endpoint list.

## 3. A redundant residue creates a new integer block

Take the public canonical-residue word

\[
g=[11^7]_N=1778.
\]

Its canonical inverse is

\[
w=1735,
\qquad
1778\cdot1735=1+1507N.
\tag{3}
\]

Both \(g\) and \(w\) lie in \(H_0\). Thus (3) adds no new residue to the old
subgroup. All immediate sign and endpoint-difference screens are trivial:

\[
\gcd(1778\pm1,N)=1,
\qquad
\gcd(1735\pm1,N)=1,
\qquad
\gcd(1778-1735,N)=1.
\]

Neither feedback endpoint is an integer perfect power:

\[
1778=2\cdot7\cdot127,
\qquad
1735=5\cdot347.
\]

But their ordinary integer representations create the proper overlap

\[
\boxed{\gcd(312,1778)=2}.
\tag{4}
\]

Complete gcd-free refinement therefore exposes \(2\) as a public block.

This block is not in \(H_0\). If \(2\in H_0\), then
\(2\cdot11=22\) would also lie in \(H_0\). But

\[
22\equiv-1\pmod{23},
\qquad
22\not\equiv-1\pmod{89},
\]

contradicting the proved sign synchronization of \(H_0\). Therefore

\[
\langle H_0,2\rangle\supsetneq H_0.
\]

The feedback residues were redundant, but their canonical integer
representations changed the algorithm's available multiplicative subgroup.

## 4. The new block is phase-only

The identity

\[
2^{11}=2048=1+N
\]

shows that \(2\) has order dividing \(11\) modulo both hidden primes. Since
\(11\) is prime and \(2\not\equiv1\) in either field, its local orders are
both exactly \(11\).

Consequently, every pure power \(2^e\) has synchronized identity status.
Because the common order is odd, neither local cyclic subgroup contains
\(-1\). For every integer \(e\ge0\),

\[
\gcd(2^e-1,N)\in\{1,N\},
\qquad
\gcd(2^e+1,N)=1.
\]

No exponent bank, smooth or otherwise, can factor \(N\) through a pure power
of this new block.

The mixed public word succeeds immediately:

\[
x=[2\cdot11]_N=22,
\]

\[
x\equiv-1\pmod{23},
\qquad
x\not\equiv-1\pmod{89}.
\]

Hence the final public gcd returns

\[
\boxed{\gcd(22+1,2047)=23}.
\tag{5}
\]

Thus the complete state-relative chain is

\[
\text{old synchronized subgroup}
\longrightarrow
\text{canonical representative feedback}
\longrightarrow
\text{integer block split exposing }2
\longrightarrow
\text{mixed phase cancellation}
\longrightarrow
\text{factor}.
\]

## 5. Exact consequence and scope

The witness proves an operation-level distinction.

- At \(N=4033\), feedback exposes an order mismatch, and pure power
  contraction works.
- At \(N=2047\), feedback exposes equal local orders. Every pure power fails,
  but a mixed old/new word works.

Therefore a complete post-feedback algorithm cannot replace mixed-word
selection by a power bank. It must detect which branch it has entered or run
both operations.

The witness does not provide that detector or an all-input selector. The
successful mixed word is verified after discovery; no general public rule is
proved to find the needed phase cancellation. Also, \(2\) is visible by
trial division of the old endpoint \(312\), and it is an ordinary small
public base. Thus feedback is not necessary for this fixed integer against a
stronger endpoint-preprocessing rule or an unrestricted factoring algorithm.
The exact result is the realization of the phase mechanism inside canonical
integer feedback.

F82-D01 first found \(N=703\), but its old endpoint \(27=3^3\) made that
certificate vulnerable to perfect-power extraction. F82-D02 added the
predeclared non-perfect-power filter and found the retained \(N=2047\)
witness. No claim of frequency, minimality, an asymptotic family, or
polynomial-time factoring follows.

For F82-D02, the imported source, new source, runner, log, and output have
SHA-256 hashes
9dadc2e68a364a2722fe972948dd4d6bf8af3ed3877e6f95b86588c4316b8bd4,
aeb5d3fe951b8574ee018ee603faef523a29a78ba329f9c73c0447254db3aaf3,
f6e100b29748887e44c828f32973af4787ca8cc3d916777da0af0419b95c67fc,
53800a402b47fd95392075882044d79a92edad06210a00e39dc6fd202d5a9983,
and
53800a402b47fd95392075882044d79a92edad06210a00e39dc6fd202d5a9983.
