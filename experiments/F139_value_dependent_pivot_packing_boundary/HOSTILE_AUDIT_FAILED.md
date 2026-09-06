# F139 hostile audit — failed pending two local statement repairs

## Verdict

**FAIL as written.** The simultaneous-preservation theorem, strict row-count
bound, global-deduplication theorem, conditional quasipolynomial packing
cost, multi-pivot linear-algebra argument, abstract hyperforest, and the
selected \(N=989\) certificate all survived re-derivation. However, the
frozen statement has one undefined source condition and one malformed
operator in the boxed splice criterion. Both must be repaired before a clean
proof-blind reconstruction.

Audited frozen hashes:

- `STATEMENT.md`:
  `810e37e044778b24db0901b7a35a2b9f403d065590e6c08edc5b2ee4f8119b8b`
- `PROOF.md`:
  `56f4d677fec4ea05644b41191689880473eea4bb3b25eb8ab1f33013f5aef757`
- corrected `OUTPUT.json` and `RUN.log`:
  `4cda0f1af6adf29f73fc7e5f0d0d74f85ca4b331c02e8cbabe61b97a7c0778ba`
- pre-audit `MANIFEST.md`:
  `3b9d9662460e30d23f12e043306776b1005e873a0978417fb76597799bb08f75`

## 1. Undefined eligibility condition

The setup says:

> For an eligible integer anchor \(\ell\le B\)

but it never defines **eligible**. The existence and uniqueness of
\(A_\ell\) require at least

\[
\gcd(\ell,N)=1.
\]

The registered verifier uses the stronger and apparently intended condition

\[
\boxed{1\le\ell\le B,\qquad \gcd(\ell,Nq)=1.}
\]

That is also the natural integer-anchor extension of the earlier prime-anchor
condition \(\ell\nmid Nq\). The statement must declare the chosen condition.
Nothing else in the proof fails under the verifier's condition.

## 2. Malformed boxed splice criterion

Theorem 4 currently displays

```text
\widehat u_j+sum_{i=1}^t\widehat v_i
```

with no backslash before `sum`. Taken literally, this is not the summation
proved below it. It must be

\[
\boxed{
\sum_{j=1}^d\beta_j
\left(
\widehat u_j+\sum_{i=1}^t\widehat v_i
\right)
\in\operatorname{colspan}(\widehat W).
}
\]

The proof already contains the correct operator and proves this corrected
formula.

## 3. Simultaneous-preservation count — pass

For \(r\in\mathcal R_B(q)\), one has \(r\nmid N\). Hence

\[
w+NA\equiv0\pmod r
\]

selects one residue class modulo \(r\). Since the occupied digits lie in
\([1,B-1]\) and \(r>B\), at most one occupied digit is divisible by \(r\).
The union of these possible exceptions has size at most
\(|\mathcal R_B(q)|\). Every digit outside it has zero, hence even,
\(r\)-valuation for every large odd row at once.

Also,

\[
\prod_{r\in\mathcal R_B(q)}r\le q,
\qquad r>B,
\]

so

\[
B^{|\mathcal R_B(q)|}<q,
\qquad
|\mathcal R_B(q)|<\frac{\log q}{\log B}.
\]

The inequalities and their strictness are correct, including the empty-row
case because \(q>1\).

## 4. Global deduplication and factor-free packing — pass

If two odd prime rows are globally degree one in different old columns, a
common-good new value contains both rows oddly. Equality with an old exact
value would force that old value to be both distinct owners, a contradiction.
Different digits give different integers because

\[
V_A-V_{A'}=qN(A-A')\ne0.
\]

The word **globally** is essential and is stated correctly. Residual privacy
created only after peeling does not suffice.

The factor-free corollary is also valid. A nonsquare \(B\)-rough basis block
has at least one hidden prime larger than \(B\) to odd valuation. Pairwise
coprimality makes the chosen hidden primes different. Global degree one of
the public block row makes each such hidden prime private to the same owner.
No hidden factorization is used by the operation.

The conditional cost claim is correctly narrow. Refining an explicit
quasipolynomial transcript against the primorial through a
quasipolynomial \(B\), exact square testing, sorting one minimum block per
owner, and scanning at most \(B\) anchors all have quasipolynomial cost. The
sorted prefix has maximum owner cardinality because the product of the
\(s\) smallest owner minima is no larger than any \(s\)-owner product. The
artifact correctly gives no theorem that two owners fit below \(N/B\).

## 5. Multi-pivot splice and hyperforest — pass after the operator repair

In each private pivot row, the dependency equation forces

\[
\alpha_i=\sum_j\beta_j=s.
\]

After deletion of the pivot rows, the remaining equation is exactly the
corrected boxed membership test above. Conversely, any such membership
reconstructs a dependency by taking every owner coefficient equal to \(s\).
Old-column independence makes every new dependency use nonzero
\(\beta\).

The abstract family is full rank for every \(t\ge2,d\ge1\). Each new column
\(u_j\) has its own private row \(h_j\). These rows force all new
coefficients to zero; the old pivots then force every old coefficient to
zero. The declared peeling order is exact. Thus simultaneous reuse of all
old pivots does not imply a rank defect.

## 6. Registered \(N=989\) certificate — pass

I reran the registered command with Sage proof arithmetic enabled:

```text
gtimeout 300 sage verify.sage
```

The fresh standard output has SHA-256

```text
4cda0f1af6adf29f73fc7e5f0d0d74f85ca4b331c02e8cbabe61b97a7c0778ba
```

which exactly matches both frozen output files. Every named check is true.
In particular:

- \(989=23\cdot43\), \(5\cdot187<989\), and
  \(187\cdot238=1+45\cdot989\);
- the packed plus and minus gcd screens are both one;
- all five integer-anchor pairs are canonical and both sign screens are one;
- the digits are \(0,0,1,2,3\), with the two zero-digit presentations
  deduplicated only after both endpoint screens;
- the six retained values and all displayed factorizations are exact;
- rows \(11\) and \(17\) are degree one in the frozen selected two-column
  old ledger and occur oddly in every nonzero-digit value;
- the displayed \(9\)-by-\(6\) matrix has rank six and nullity zero;
- the registered peeling witness removes all six columns.

The certificate consistently limits itself to the selected six-column
source. It makes no complete-F26-Q, complete-canonical-universe, density, or
factoring claim.

## 7. Preserved \(N=667\) failure history — complete

The rejected certificate, original preregistration, three verifier pin
stages, two empty serialization outputs, both revision notes, final
scope-incomplete arithmetic output, failure explanation, and exploratory
search note are all present. Their pinned hashes agree with the files.

The fatal omitted operation is recorded correctly:

\[
\gcd(133+331,667)=29.
\]

Thus that run factors before the proposed no-factor branch. The artifact
does not use it as evidence for F139. References inside the preserved files
retain their original pre-rename filenames; the manifest explains the
subsequent `667` suffixes. This is faithful preserved history, not missing
evidence.

## Required repair

Define integer-anchor eligibility explicitly, and insert the missing
backslash in Theorem 4. Then refreeze the statement and proof hashes and run
a fresh hostile re-audit. I found no further mathematical defect and no
counterexample to the intended corrected result.
