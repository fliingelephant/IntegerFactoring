# F82 hostile whole-proof and provenance audit

## Verdict: PASS

I audited
`experiments/F82_canonical_phase_only_feedback_search/RESULT.md` at the
pinned SHA-256

```text
85f9b310a0e1a10af3cdae8c081b1f374e3be3bddf2437c2d40c39b16ec45990
```

The hash matches. I also read the complete D01 helper, D02 source, D02
runner, manifest, log, output, and registry entry. I ran no search, replay,
or new research computation. The arithmetic checks below are direct
certificate inspection.

The retained \(N=2047\) certificate is correct. It proves a literal
canonical-integer feedback refinement whose new block has equal local
orders, whose pure direct-sign powers all fail, and whose displayed mixed
word factors.

Two limits are essential:

1. The computation is authenticated finite discovery evidence only. It does
   not independently prove its counts, first-witness status, frequency,
   minimality, or any asymptotic law.
2. The algorithmic “must branch or run both” sentence is valid only as a
   state-relative warning that a direct-sign power bank on the new block
   cannot replace the displayed mixed-word channel. It is not a literal
   lower bound on arbitrary factoring algorithms. The candidate later
   excludes that stronger reading and notes that trial division already
   exposes \(2\).

Under the candidate's stated mechanism-level scope, no claim fails.

## 1. Modulus and primality

The factorization is exact:

\[
23\cdot89=2047.
\]

Both factors are prime. For \(23\), it is enough to test \(2,3\). For
\(89\), the primes through \(\sqrt{89}<10\) are \(2,3,5,7\), and none
divides it.

The use of these factors is proof-side only. Every displayed execution step
after the witness is specified uses public integer arithmetic modulo
\(2047\).

## 2. Old canonical relations

The first endpoint relation is

\[
11\cdot1861=20{,}471=1+10\cdot2047.
\]

The second is

\[
312\cdot269=83{,}928=1+41\cdot2047.
\]

Also,

\[
11^4=14{,}641=7\cdot2047+312.
\]

Since \(312\cdot269\equiv1\pmod{2047}\), the residue \(269\) is the
canonical inverse of \(11^4\). The relation with \(11\) similarly makes
\(1861\) its canonical inverse. All four endpoints lie strictly between
\(1\) and \(N\).

## 3. Primality, pairwise coprimality, and perfect powers

The integers \(11\) and \(269\) are prime. For \(269\), trial divisors
through \(\sqrt{269}<17\) are \(2,3,5,7,11,13\), and none divides it.

For \(1861\), one must test primes through
\(\sqrt{1861}<44\). Its remainders at

\[
2,3,5,7,11,13,17,19,23,29,31,37,41,43
\]

are all nonzero. More explicitly, the nontrivial nearby products are

\[
\begin{aligned}
7\cdot265&=1855,&11\cdot169&=1859,&13\cdot143&=1859,\\
17\cdot109&=1853,&19\cdot98&=1862,&23\cdot81&=1863,\\
29\cdot64&=1856,&31\cdot60&=1860,&37\cdot50&=1850,\\
41\cdot45&=1845,&43^2&=1849.
\end{aligned}
\]

Thus \(1861\) is prime.

The remaining endpoint factors as

\[
312=2^3\cdot3\cdot13.
\]

The three prime exponents \(3,1,1\) have gcd one, so \(312\) is not a
nontrivial integer perfect power. The other three endpoints are prime and
therefore are not nontrivial perfect powers.

The three prime endpoints are distinct. None divides \(312\):

\[
312\bmod11=4,\qquad312\bmod269=43,
\]

and \(1861>312\). Also,

\[
1861\bmod269=247\neq0.
\]

Hence \(11,1861,312,269\) are pairwise coprime. Complete gcd-free
refinement has no cross-endpoint gcd with which to split any one of them,
so it retains the four whole blocks. Exact perfect-power preprocessing also
leaves the list unchanged.

## 4. Old subgroup and local orders

The endpoint residues are

\[
11,\quad11^{-1},\quad11^4,\quad11^{-4}.
\]

They all lie in \(\langle11\rangle\), and \(11\) itself is a block.
Therefore the old block-generated subgroup is exactly

\[
H_0=\langle11\rangle.
\]

Modulo \(23\), direct squaring gives

\[
11^2\equiv6,\qquad
11^4\equiv13,\qquad
11^5\equiv5,
\]

so

\[
11^{10}\equiv2,\qquad11^{11}\equiv-1.
\]

Modulo \(89\),

\[
11^2\equiv32,\qquad
11^4\equiv45,\qquad
11^5\equiv50,
\]

so

\[
11^{10}\equiv8,\qquad11^{11}\equiv-1.
\]

Thus the order divides \(22\) in both fields and does not divide \(11\).
The only remaining proper divisor compatible with the eleventh power being
\(-1\) is \(2\), which would require \(11=-1\); this is false modulo both
primes. The local orders are therefore exactly \(22,22\).

For every exponent, identity occurs in both components at residues
\(0\bmod22\), and \(-1\) occurs in both at residues \(11\bmod22\). The old
subgroup has no direct sign separator.

## 5. Feedback word and canonical inverse

Using \(11^4\equiv312\), direct multiplication gives

\[
11^7\equiv1778\pmod{2047}.
\]

The claimed inverse relation is exact:

\[
1778\cdot1735
=3{,}084{,}830
=1+1507\cdot2047.
\]

Both endpoints are canonical integers in \(\{1,\ldots,N-1\}\), and their
residues are \(11^7\) and \(11^{-7}\). Appending the relation adds no new
residue to \(H_0\).

Their factorizations are

\[
1778=2\cdot7\cdot127,
\qquad
1735=5\cdot347.
\]

The numbers \(127\) and \(347\) are prime. For \(127\), primes through
\(\sqrt{127}<12\) do not divide it. For \(347\), testing
\(2,3,5,7,11,13,17\) gives nonzero remainders. Thus both displayed
factorizations have only exponent one, and neither feedback endpoint is a
nontrivial perfect power.

## 6. Immediate screens

Using \(2047=23\cdot89\), none of

\[
1777,\quad1779,\quad1734,\quad1736,\quad43
\]

is divisible by \(23\) or \(89\). Hence

\[
\gcd(1778\pm1,N)=
\gcd(1735\pm1,N)=
\gcd(1778-1735,N)=1.
\]

The related discriminant-style direct screen also fails:

\[
(1778-1735)^2+4=1853,
\]

which is divisible by neither hidden prime. Thus the exact displayed
immediate menu, and the usual extra endpoint-pair discriminant check, expose
no factor.

The candidate does not claim that every conceivable public arithmetic
screen fails.

## 7. Complete gcd-free refinement

The six endpoint factorizations are

\[
\begin{aligned}
11,\quad1861,\quad2^3\cdot3\cdot13,\quad269,\\
2\cdot7\cdot127,\quad5\cdot347.
\end{aligned}
\]

The only shared prime between an old and new endpoint is \(2\). In
particular,

\[
\gcd(312,1778)=2.
\]

Complete gcd-free refinement therefore separates the common base \(2\),
with exponent three in \(312\) and exponent one in \(1778\). It is a public
block even though the remaining cofactors can stay composite. This proves
the claimed refinement directly; it does not rely on the search program's
generic overlap filter.

## 8. Strict subgroup expansion

Suppose \(2\in H_0\). Since \(11\in H_0\) and \(H_0\) is a group, this
would imply \(22=2\cdot11\in H_0\). But

\[
22\equiv-1\pmod{23},
\qquad
22\not\equiv-1\pmod{89}.
\]

This contradicts the proved sign synchronization of every element of
\(H_0\). Hence \(2\notin H_0\), and

\[
\langle H_0,2\rangle\supsetneq H_0.
\]

The new residue information comes from splitting the canonical integer
representatives, not from the appended residues themselves.

## 9. Equal local orders and pure-power impossibility

The exact integer identity

\[
2^{11}=2048=1+2047
\]

shows that the order of \(2\) divides \(11\) modulo both hidden primes.
Since \(11\) is prime and \(2\neq1\) in either field, both local orders are
exactly \(11\).

For every \(e\geq0\), the residue \(2^e\) is \(1\) in one component exactly
when \(11\mid e\), which is simultaneously true in the other. Therefore

\[
\gcd(2^e-1,N)\in\{1,N\}.
\]

Each generated local subgroup has odd order \(11\), so it contains no
element of order two and hence no \(-1\). Thus

\[
\gcd(2^e+1,N)=1
\]

for every \(e\geq0\).

No exponent bank can succeed through the two direct sign gcds of a pure
power of this block. This is the exact “pure-power impossibility” proved
here. It is not a lower bound for other functions of the power transcript.

## 10. Mixed public word

The mixed word is

\[
x=[2\cdot11]_N=22.
\]

It satisfies

\[
x\equiv-1\pmod{23},\qquad x=22\not\equiv-1\pmod{89}.
\]

Therefore the public final step gives

\[
\gcd(x+1,N)
=\gcd(23,2047)
=23.
\]

Once the transcript is specified, the execution needs no hidden factor or
local order: compute the two canonical relations, perform gcd-free
refinement, form the word \(2\cdot11\), and take the final gcd.

## 11. Exact mechanism-level consequence

This witness proves that a direct-sign power bank on the new block is not a
complete replacement for mixed old/new words in the canonical feedback
state model. The new block has equal local orders, every direct-sign pure
power fails, and the displayed mixed word succeeds.

It does not prove that every complete factoring algorithm must literally
detect this branch or run these two named routines. A unified mixed-word
method, further refinement, square-class decoding, trial division, or an
unrelated factoring operation is outside that inference. The candidate
acknowledges this practical scope by noting that \(2\) is already visible
through trial division of \(312\) and is an ordinary public base.

Accordingly, the certificate realizes a phase-only feedback mechanism. It
does not prove that feedback is necessary for this integer, give a rule for
selecting \(11^7\) or \(2\cdot11\) on general inputs, or yield an all-input
factoring algorithm.

## 12. D02 provenance hashes

The five hashes stated in the candidate match the retained files exactly:

| Artifact | SHA-256 |
| --- | --- |
| Imported D01 source `scripts/F82_D01_search.py` | `9dadc2e68a364a2722fe972948dd4d6bf8af3ed3877e6f95b86588c4316b8bd4` |
| D02 source `scripts/F82_D02_nonpower_search.py` | `aeb5d3fe951b8574ee018ee603faef523a29a78ba329f9c73c0447254db3aaf3` |
| D02 runner `run_F82_D02.sh` | `f6e100b29748887e44c828f32973af4787ca8cc3d916777da0af0419b95c67fc` |
| D02 log `logs/F82-D02.log` | `53800a402b47fd95392075882044d79a92edad06210a00e39dc6fd202d5a9983` |
| D02 output `output/F82-D02.json` | `53800a402b47fd95392075882044d79a92edad06210a00e39dc6fd202d5a9983` |

The identical log and output hashes are expected. The source writes sorted,
indented JSON with one final newline to the output and prints the same JSON
to stdout; the runner pipes that stdout through `tee` to the log.

The runner:

- refuses to overwrite an existing log or output;
- uses the declared `/opt/homebrew/bin/timeout 120s`;
- uses the declared Python runtime;
- enables `set -euo pipefail`, so timeout or source failure propagates
  through the `tee` pipeline; and
- invokes the D02 source that imports the pinned D01 helpers from the same
  scripts directory.

The D02 manifest records the same source, runner, timeout, log, output, and
hashes. The F82-D02 row in `REGISTRY.md` records the run as finite discovery
evidence pending independent audit.

## 13. What the D02 source and output support

The D02 source implements the declared finite enumeration using the hidden
factors and local orders as discovery labels. It:

- enumerates distinct odd primes through the declared bound and bases through
  \(64\);
- retains equal-old-order states;
- constructs the two old canonical inverse pairs;
- requires four distinct, positive, pairwise-coprime old endpoints;
- excludes all six declared endpoints if they are nontrivial perfect powers;
- applies the stated direct sign and endpoint-difference screens;
- searches proper old/new integer gcd overlaps;
- requires a unit overlap outside the old power list with equal local
  orders; and
- exhausts the finite mixed exponent box for the first direct-sign hit.

Its perfect-power set is exact over the scan range. Every nontrivial perfect
power below the largest modulus has a base at most its square root, and the
source enumerates every power of each such base.

The output and log agree byte for byte. They contain the stated witness,
quotients, endpoint list, new block, equal order \(11\), and mixed
certificate \(2\cdot11=22\) with factor \(23\).

The source is a discovery program, not an independent certificate verifier.
In particular, it uses \(p,q\), computes local orders, and stops at its first
accepted record. Its generic overlap test is not a separately audited
implementation of complete gcd-free refinement; the retained block \(2\)
is instead certified directly in Section 7 above.

No fresh replay has authenticated the aggregate counts or re-enumerated the
claim that this is the first witness in the declared order. The candidate
does not use either fact in its theorem. The registered computation supports
discovery of the record and exact artifact provenance only.

## 14. Final scope

The exact certificate is independent of search exhaustiveness. D01's
\(N=703\) record is used only as historical motivation for adding the
perfect-power filter; no D01 theorem is imported.

F82 proves no frequency, minimality, asymptotic family, inverse-polynomial
selection law, complexity lower bound, or general factoring algorithm. It
also does not show that feedback is needed on this fixed input. Within those
limits, the arithmetic, group theory, refinement claim, provenance, and
phase-only conclusion all pass.
