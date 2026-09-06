# Hostile audit of F176 HH two-base normal form

## Verdict

**PASS, with the two proof-writing qualifications stated below.**

The four-way operational output theorem is correct under the frozen F174
contract.  The new collision bank factors every line-13 escape at a prime
at least five.  A surviving escape at two has the stated absolute and
relative hard-order certificates.  A surviving escape at three forces

\[
M=n,
\qquad
N=2^n-1,
\]

and a composite exponent gives the displayed proper divisor.  The proof is
valid for arbitrary odd composites, including repeated prime factors and
prime powers.  The added work is polynomial, so the imported F174
quasipolynomial bound is preserved.

Two nonoperative qualifications must remain attached to this verdict.

1. The latest blind audit of F174 correctly observes that the *raw*
   line-13 prime need not be outside every local subgroup \(H_j\).  F176
   does not use that false strengthening.  Its collision proof uses only
   the valid prefix congruences.  Its hard certificates are asserted only
   after the F174 absolute and relative gcd-one branches, which do certify
   the displayed all-component conclusions.
2. The sentence that recursion depth is at most \(n\) does not alone bound
   a branching recursion tree.  The claimed QP recursion bound is still
   correct: a complete binary factor tree has at most
   \(\lfloor\log_2 N\rfloor\) prime leaves, counted with multiplicity, and
   hence fewer than \(2n\) total nodes.  A standard deterministic primality
   test supplies the leaf test.  This is a missing sentence, not a false
   output or cost claim.

F176 remains a normal-form theorem, not a factoring theorem.  Its base-two
and prime-exponent composite-Mersenne hard branches remain unresolved.

## Frozen inputs

I read the following current files in full and verified their SHA-256
hashes:

- F174 `STATEMENT.md`:
  `6f5ff26ad6e5735d60e85bb394b992b44e05698bee7c9d51d902a240205d5908`;
- F174 `PROOF.md`:
  `614dbb1b0bb538353c2c919a5fa5778c8ff885c031992229ab1877db5a29ec98`;
- F174 `BLIND_RECONSTRUCTION.md`:
  `086610b9fcedea2af55f7f36b81f7b43ddb5b86798e575eafacec31b2f4240d0`;
- F176 `STATEMENT.md`:
  `4258d94b09cd95dffa66a9cce67fe95b40a69706361a3ed855d7b2f7d3cf062b`;
- F176 `PROOF.md`:
  `abf7ebcbf9366c49357010d464a9ce628c6796fc6d34ef058055018d963c9a72`;
- F176 `SELF_AUDIT.md`:
  `21be2be518b0c61c3c2179a85ef3bcc0e54d1a25b24ee84ba24c0d75dc8ed026`;
- F176 `MANIFEST.md`:
  `f043b6357292e2226c3ddbc566eb033010909f207662c20220e200f7bc809ae9`.

The F176 statement received a one-byte rendering correction while this
audit was in progress.  The verdict is bound to the final hash above.  The
proof, self-audit, and manifest did not change during the audit.

## 1. Imported F174 contract and exit coverage

For every input outside the fixed finite range, \(D=n\) is admissible for
F174: \(n\ge64\) implies \(n<N-1\), and of course \(D\ge n\).  All F174
exits before line 13 remain unchanged.  They return either a verified
proper divisor or a factored exact common-order state of order greater than
\(n\).  If the HH loop completes, the imported arithmetic-progression scan
returns a factor.

At line 13, F176 imports only these valid facts:

\[
\beta\text{ is prime},
\qquad M\le n,
\qquad a^M=1\pmod N\quad(1\le a<\beta),
\]

and the exact common local order of the current state.  None of these facts
was invalidated by the latest F174 blind reconstruction.

The disputed F174 prose would assert
\(\beta\notin H_j\) for every \(j\) immediately at line 13.  The valid raw
conclusion is only that this holds for at least one \(j\).  No step of the
F176 collision or Mersenne arguments invokes either conclusion.  On an
eventual hard branch, F174's absolute gcd-one result gives

\[
\sigma(\operatorname{ord}_{R_j}(\beta))>n
\]

for every \(j\), and its relative gcd-one result gives the all-component
quotient-order lower bound.  Those later hard conclusions are valid.

## 2. Exact collision-bank bounds

Assume \(n\ge64\), let \(t=\lceil\sqrt n\rceil\), and put

\[
\mathcal S=\{2^u3^v:0\le u,v\le t\}.
\]

The stated inequality \(t\le n/4\) holds at \(n=64\) and thereafter.
Also

\[
\frac{\log_2 6}{4}n<n-1
\]

throughout this range.  Since an odd \(N\) with
\(n=\lceil\log_2(N+1)\rceil\) satisfies \(N>2^{n-1}\), every bank member
obeys

\[
2^u3^v\le6^t\le6^{n/4}<2^{n-1}<N.
\]

Unique factorization makes the \((t+1)^2\) bank members distinct, and

\[
(t+1)^2>n\ge M.
\]

Thus the cardinality and strict integer-size bounds are exact.  The fixed
preprocessing range covers every smaller \(n\).

## 3. Root count for arbitrary odd composites

If \(\beta\ge5\), both two and three belong to the completed HH prefix.
Hence

\[
2^M=3^M=1\pmod N,
\]

and every member of \(\mathcal S\) is an \(M\)-th root modulo \(N\).

Fix any rational prime \(p\mid N\).  The polynomial
\(X^M-1\in\mathbf F_p[X]\) is nonzero and has at most \(M\) roots.
Because the bank has more than \(M\) members, two distinct bank integers
\(x,y\) satisfy \(x\equiv y\pmod p\).  Their difference satisfies

\[
0<|x-y|<N.
\]

Consequently

\[
1<\gcd(|x-y|,N)<N.
\]

This remains proper when \(N=p^a\), because divisibility by \(p\) makes
the gcd nontrivial while the strict size bound prevents divisibility by all
of \(N\).  The same argument handles any repeated prime-power component.
The exhaustive pair scan therefore factors every \(\beta\ge5\) escape.
Since F174 already proves primality of \(\beta\), every no-factor escape is
two or three.

## 4. Base-two hard branch

At the first HH loop integer, the state is exactly \((1,1)\).  Therefore
the local quotient by the current subgroup is the full local unit group.
If neither F174 screen factors or returns a common exact state, its two
gcd-one branches give, for every hidden prime-power component \(R_j\),

\[
\sigma(\operatorname{ord}_{R_j}(2))>n,
\qquad
\operatorname{ord}_{R_j}(2)>C.
\]

This is exactly Outcome 3.

## 5. Base three, exact state, and Mersenne form

Before an escape at three, two is the only earlier nontrivial source
integer.  Since it did not escape at line 13, its exact global order
\(m\le n\) was found.  The no-factor prime-divisor screens and lcm update
certify

\[
\operatorname{ord}_{R_j}(2)=M=m
\qquad\text{for every }j.
\]

It follows that \(N\mid2^M-1\).  If \(M<n\), then

\[
0<2^M-1\le2^{n-1}-1<N,
\]

which is impossible.  Hence \(M=n\).  Now

\[
N\mid2^n-1,
\qquad
0<2^n-1<2N,
\]

so the positive quotient is one and \(N=2^n-1\).

The imported F174 invariant is enough here even if the concrete lcm
representative after processing two is not stipulated to be literally the
integer two.  It is a power of two of exact order \(n\), so it generates
the same local subgroup \(\langle2\rangle\).  Thus the hard quotient in
Outcome 4 is correctly written modulo \(\langle2\rangle\).  The proof's
sentence “the current state is \((2,n)\)” can be read at the subgroup level;
literal equality of the representative is unnecessary.

## 6. Composite exponent and the hard certificates

If \(n\) is composite, trial division finds a prime \(\ell\mid n\).  Since
\(n/\ell\ge2\) and \(n/\ell<n\),

\[
d=2^{n/\ell}-1
\]

satisfies

\[
1<d<2^n-1=N,
\qquad
d\mid2^n-1=N.
\]

It is therefore a verified proper divisor.  A no-factor base-three branch
has prime exponent \(n\), while the input promise still makes the Mersenne
number itself composite.

On the eventual F174 hard return, the current subgroup is
\(\langle2\rangle\) and \(D=M=n\).  The absolute and relative gcd-one
branches give, for every \(R_j\),

\[
\operatorname{ord}_{R_j}(2)=n,
\]

\[
\sigma(\operatorname{ord}_{R_j}(3))>n,
\qquad
\operatorname{ord}_{(\mathbf Z/R_j\mathbf Z)^\times/\langle2\rangle}
(3\langle2\rangle)>C.
\]

These are exactly the stated Outcome 4 certificates.  They do not use the
invalid raw all-local escape wording from F174.

## 7. QP cost and complete-factor recursion

The bank has \(O(n)\) members and \(O(n^2)\) unordered pairs.  Each member
and difference has \(O(\sqrt n)\) bits.  Construction, subtraction, and
all gcd computations therefore have polynomial bit cost and space.
Trial division of the \(O(\log n)\)-bit exponent uses \(O(\sqrt n)\)
arithmetic iterations, and the displayed Mersenne divisor has at most
\(n\) bits.  These additions preserve the imported deterministic QP bound
for \(D=n\) and fixed QP \(C\).

For recursion, a returned divisor \(d\) and cofactor \(N/d\) are both
strictly between one and \(N\), including on prime-power inputs.  Every
root-to-leaf path shortens the bit length and has length at most \(n\).
More importantly, the product of all prime leaves equals the original
\(N\), so the number of leaves, counted with multiplicity, is at most
\(\lfloor\log_2N\rfloor\).  A full binary factor tree therefore has fewer
than \(2n\) nodes.  Using deterministic polynomial-time primality testing
at leaves, the polynomial number of calls times a uniform QP per-call bound
is still QP.  Repeated prime factors do not change this argument.

## Final scope

The audit certifies only the four-way normal form.  It does not eliminate
the hard base-two branch, factor prime-exponent composite Mersenne numbers,
or convert either hard certificate into a common exact order.  It therefore
does not prove deterministic or Las Vegas QP integer factoring.
