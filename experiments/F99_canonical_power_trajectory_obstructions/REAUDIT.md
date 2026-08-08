# F99 corrected hostile re-audit

## Verdict: **PASS**

The correction repairs the only defect found by the first hostile audit.
Sections 1–3 remain correct. The corrected Section 4 no longer implies that
F98 lacks a deduplicated, non-global certificate. It states the exact narrow
lesson proved by F99: raw relation count and raw binary nullity are not, by
themselves, progress certificates.

## 1. Pinned artifacts

I pinned the corrected candidate before reading it:

```text
d3a1af9e01f0209d8f06d53c2641bbad2056077bdca4d7966f9e6bdc98e592aa  RESULT.md
```

This is the expected corrected hash. I also pinned and read the existing
verifier, its output, and the failed audit in full:

```text
9d57ba6f0eb2321c5af06a3cc4a51befeab8ca585f6faf09f057fe4511240010  verify_fixed_witness.py
bd14181c674106bbd1ccd3a2d3afa84c66aac089ef35c508ef10b63f2320a576  VERIFY_OUTPUT.json
8e8e9ecef970f26eb73130cdd4727618ebbb78f3b536cdc2d7621064e77fed2c  AUDIT.md
```

The failed audit is unchanged and preserved. For reference, its independent
source and output also remain unchanged:

```text
ad1c270f5fb791270ef9e29d3efc7f1648257c63bf4b824a04c1e4fb3f2d99f2  audit_independent_verifier.sage
a8b34a92464374e948f92d9f9bf06ae350555d2ec2640f4e7499527c9ea4dd09  AUDIT_VERIFY_OUTPUT.json
```

The failed candidate audited in `AUDIT.md` had hash:

```text
9d3155d12d2f6a7f2b57e9c3d8bd3a4bc9764570b2418c1c05d7c585f5bbc408  old RESULT.md
```

## 2. Exact correction check: PASS

The first audit passed the orbit-collapse theorem, the fixed trial-hard
witness, and the CRT private-row family. Its only blocking finding was this
old implication in Section 4:

- F98 allegedly still needed a count of unique exact values;
- F98 allegedly still needed a kernel after duplicate directions were
  removed;
- F98 allegedly still needed a non-global root or a block split.

The first audit showed that all three items were already present in F98. It
prescribed one replacement paragraph. The corrected Section 4 contains that
replacement exactly in substance:

> This obstruction does not apply to the current F98 certificate. F98
> removes repeated exact relation values before decoding, reports that all
> 166 selected values are distinct, and exhibits a non-global root that
> factors its modulus. F99 only shows that future progress claims cannot use
> raw relation count or raw nullity alone.

This repair does not add a theorem. It removes the false objection to F98.
It also leaves the final scope sentence intact: the full F98 rule remains
open because another seed can create a new square class, a non-global root,
or a real refinement split.

The current Sections 1–3 state the same claims that the failed audit checked
and passed. I found no changed hypothesis, conclusion, witness value, or
asymptotic claim there. The old blob is not retained as a Git object, so a
byte-for-byte diff against the old hash is unavailable. The expected new
hash, the unchanged passed claims, and the exact prescribed Section 4 repair
together establish the intended correction at the mathematical level.

## 3. Orbit-collapse theorem: PASS

From

\[
N=(a^m-1)/k
\]

one gets

\[
a^r a^{m-r}=a^m=1+kN.
\]

The two strict size hypotheses put both endpoints in the canonical residue
range. Hence \(a^{m-r}\) is the least positive inverse of \(a^r\).

When \(m\) is odd and \(a\) is one square-normalized basis block, every
nonzero parity column is the same. A dependency uses \(2t\) copies. Its
positive normalized root is

\[
(a^m)^t=(1+kN)^t\equiv1\pmod N.
\]

Because \(N\) is odd, the two gcds are exactly \(N\) and \(1\). Pairing any
new duplicate with one retained copy generates the new kernel directions,
and every such pair has root \(+1\). Thus duplicate columns can increase
nullity without enlarging the normalized-root image.

The no-split statement has the needed extra hypothesis: \(a\) is already a
prime basis block. Every endpoint is then a power of the same known block.
Exact gcd refinement has no new prime support to expose.

## 4. Fixed witness: PASS

The fixed arithmetic is exact:

\[
64{,}570{,}081=(3^{17}-1)/2=1{,}871\cdot34{,}511.
\]

The stated complete predecessor factorizations, Lucas residues, and Lucas
gcds prove that both factors are prime. The input length is 26 and the trial
bound is 676. Both factors exceed that bound.

The stability data reproduce as

```text
g = 170
A = 11
B = 203
gcd(A*B, N-1) = 1
```

The element 3 has order 17 modulo both prime factors and modulo their
product. Every nontrivial canonical presentation on the trajectory has the
same exact value

\[
3^{17}=1+2N.
\]

The complete range \(0\le e\le676\) visits exactly 17 residues. One is 1.
The other 16 give the same nontrivial exact relation value. For all 16
nontrivial residues, both direct sign gcds equal 1. All endpoints are powers
of the already known block 3.

Therefore this complete one-seed trajectory adds records and duplicate
kernel directions, but it adds no factor-relevant root and no block split.
The result does not claim that the other F98 seeds fail on this modulus.

## 5. CRT private-row family: PASS

For \(K_e=2^e-1\), Bertrand's postulate supplies distinct primes in the
disjoint stated intervals. Each \(K_e\) is invertible modulo \(q_e^2\). The
CRT class \(a\) is reduced modulo

\[
M=2^T\prod_e q_e^2.
\]

For sufficiently large \(T\), \(7\nmid M\). Among the six lifts above \(M\),
at most one lift of each CRT class is divisible by 7. Thus the two required
reduced classes modulo \(7M\) exist and are different.

Dirichlet supplies primes in the two classes. Linnik supplies choices of
polynomial size in \(M\). Their classes force both primes to exceed \(M\),
so

\[
\log N_T=\Theta(\log M)=\Theta(T^2).
\]

For every \(1\le e\le T\), the displayed \(w_e\) is an integer in
\((0,N_T)\), so it is the canonical inverse of \(2^e\). The CRT congruences
give

\[
v_{q_e}(P_e)=1
\]

and \(q_e\nmid P_j\) for every \(j\ne e\). Each column has a private odd
valuation row. Hence the \(T\) square classes are linearly independent.

The conclusion remains narrow. This family does not claim P98 stability,
failed direct screens, or no block split. It gives only
\(T=\Theta(\sqrt{n_T})\) consecutive residues, not an \(n_T^2\)-long C2T
menu. It disproves closure from consecutiveness alone.

## 6. Fresh independent replay: PASS

I wrote a new verifier. It does not import either earlier verifier. It
recomputed:

- both primality certificates and the complete trial screen;
- all stability values;
- all 677 trajectory exponents;
- every exact canonical product and direct sign gcd;
- a new CRT/private-row instance at \(T=5\), while the first audit used
  \(T=4\);
- the full rank of the five private rows over \(\mathbb F_2\).

The final command was:

```text
/usr/bin/time -p /opt/homebrew/bin/timeout 120 /usr/local/bin/sage reaudit_independent_verifier.sage
```

It exited zero in 2.09 seconds. The source predates the output and log.

```text
5d1629f275a42d4c229fde592fcfad321fa869466c3569fb4e914d5d057c590e  reaudit_independent_verifier.sage
08ac3e2f9bd2b6f16e898db1f329aab7d2ef0d4dbcf8ed3b0139c23c49e87b6a  REAUDIT_VERIFY_OUTPUT.json
ea3609df20cf060797088d0853ef616e5108226efc25a6e80e2e1900aa91b820  REAUDIT_VERIFY_RUN.log
```

The first run of the new verifier compared a Sage factorization object to
an integer and failed before checking the candidate. I preserved that log,
changed only the verifier assertion to compare factor lists, and then froze
and ran the source above.

```text
4e5f11cce588dd47c0712da4bc041ed4e72f92a03c7a5c38c10c7295b3da8ae3  REAUDIT_VERIFY_FAILED_RUN.log
```

## Final decision

**PASS.** The corrected F99 artifact proves two exact limits on canonical
power trajectories:

1. exact repeated relations can add nullity while every new normalized root
   stays global \(+1\);
2. a polynomial-length run of consecutive canonical residues can retain a
   private parity row in every column.

It does not refute F98, the full multi-seed C2T rule, or factoring in
polynomial time. It supplies a valid obstruction and a valid progress
criterion: deduplicate exact relation values and measure the normalized-root
image, not raw relation count or raw nullity.
