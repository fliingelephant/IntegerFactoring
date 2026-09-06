# F139 final hostile re-audit — PASS

## Verdict

**PASS as claimed.** The final statement and proof contain only the two
terminology repairs requested by the proof-blind reconstruction. Both
repairs are correct. They do not change a theorem, quantifier, algorithm,
cost bound, certificate, or unresolved scope.

The earlier hostile conclusions remain exact:

- multi-owner packing can preserve many old private rows at once;
- two globally private owners make the common-good values genuinely new;
- the packing operation has conditional quasipolynomial cost;
- preservation alone does not force a rank defect;
- the selected \(N=989\) certificate is exact;
- no qualifying packed word, dependency, non-global root, or factoring
  theorem is forced for all inputs.

## Frozen inputs

- STATEMENT.md:
  a01cd50a749a61d70aefac9b50fca91e4a87332ef882c343fccc07009b75f27b
- PROOF.md:
  8a41448676a1df5850fe90cc144bbca23a0513a36b9ac7e974a6b5de80de1a60
- prior passing HOSTILE_REAUDIT.md:
  d5ac87c39e8f9c54b2ec458ee2219fe7aee308916aadf3dba38953cf4b7c4693
- BLIND_RECONSTRUCTION.md:
  7439660188994eedb47ef21a230dab2bb34b95d2af01b3890ac3155e2ae0f80c
- pre-audit MANIFEST.md:
  f7dd9f61a125aa6de5347502d24baa9f90c25850a363e96d498dca9ed7f1060d
- unchanged verify.sage:
  d0cb52305d9ab1f75ec02f4b67fcbc1fae520b6dc424175aac077dbb940ea376
- unchanged OUTPUT.json and RUN.log:
  4cda0f1af6adf29f73fc7e5f0d0d74f85ca4b331c02e8cbabe61b97a7c0778ba

## Exact change-scope verification

The prior passing hashes were:

- STATEMENT.md:
  90f89961e4fb9f2a16bd8027cd6ea21092c3794e2e4994254b3ac7f57e04e148
- PROOF.md:
  56f4d677fec4ea05644b41191689880473eea4bb3b25eb8ab1f33013f5aef757

I mechanically reversed only the following edits.

1. Remove the new least-positive-inverse range and definition, restoring
   \(w=\iota_N(q)\) without a local explanation.
2. Restore “multi-parent hyperforest” and “abstract hyperforest” at the two
   affected places in the statement.
3. Restore the proof section heading “Abstract hyperforest.”

The reversed statement hashes exactly to the prior passing statement hash.
The reversed proof hashes exactly to the prior passing proof hash. Therefore
no unlisted mathematical change occurred.

## 1. Least-positive inverse repair

The statement now says

\[
w=\iota_N(q)\in\{1,\ldots,N-1\}
\]

and defines \(\iota_N(q)\) as the least positive inverse of \(q\) modulo
\(N\). This closes the blind reconstruction's exact objection.

The canonical endpoint proof needs both facts:

\[
qw\equiv1\pmod N
\quad\text{and}\quad
1\le w<N.
\]

For an eligible anchor, \(0\le A_\ell<\ell\), so

\[
0<w+NA_\ell<N\ell.
\]

Thus \(z_\ell=(w+NA_\ell)/\ell\) is in
\(\{1,\ldots,N-1\}\). Together with

\[
(\ell q)z_\ell\equiv1\pmod N,
\]

this proves that \(z_\ell\) is the least positive inverse of \(\ell q\).
The new definition is sufficient and consistent with every later use.

The earlier hostile repair also remains present:

\[
1\le\ell\le B,\qquad \gcd(\ell,Nq)=1.
\]

Hence the digit exists uniquely and the endpoint construction is public.

## 2. Peelable-incidence terminology repair

The statement now calls the abstract example a “multi-parent peelable
incidence system.” The proof heading uses the same term. This is exact.

For

\[
v_i=e_{p_i},
\qquad
u_j=e_{p_1}+\cdots+e_{p_t}+e_{h_j},
\]

each row \(h_j\) is private to \(u_j\). Degree-one peeling first removes
every \(u_j\). It then makes each \(p_i\) private to \(v_i\), so every
\(v_i\) peels. The full matrix is independent and has rank \(t+d\).

The term does not claim Berge acyclicity. Indeed, the incidence graph can
have cycles when \(t,d\ge2\). The new wording states only the property that
is proved and used: complete degree-one peelability.

The statement's final potential discussion now refers to the same abstract
peelable incidence system. It no longer relies on an ambiguous meaning of
“hyperforest.”

## 3. All prior theorem objections

The two initial hostile defects remain repaired.

1. Integer-anchor eligibility is explicit.
2. The shifted residual criterion contains the correct summation:
   \[
   \sum_{j=1}^d\beta_j
   \left(
   \widehat u_j+\sum_{i=1}^t\widehat v_i
   \right)
   \in\operatorname{colspan}(\widehat W).
   \]

The rest of the statement and proof are byte-identical to the prior passing
versions after the terminology reversals. I nevertheless rechecked the
dependency points:

- one large odd row excludes at most one digit because \(r>B\);
- the union bound preserves all rows simultaneously;
- \(B^{|\mathcal R_B(q)|}<q\) gives the strict row-count bound;
- two different globally private owners prevent equality with any old
  exact value;
- different digits give different exact integers;
- pairwise-coprime nonsquare \(B\)-rough blocks supply distinct hidden odd
  primes without factoring;
- sorted owner minima maximize the feasible owner count;
- the primorial, refinement, scan, and decoder-side transcript operations
  remain quasipolynomial for the declared \(B\);
- the pivot equations and shifted residual column-span test are equivalent
  in both directions;
- full pivot reuse can still peel completely and have zero kernel.

No old-only dependency or normalized-root claim was inserted.

## 4. Certificate replay

I reran

    gtimeout 300 sage verify.sage

with Sage proof arithmetic enabled. The fresh standard-output hash is

    4cda0f1af6adf29f73fc7e5f0d0d74f85ca4b331c02e8cbabe61b97a7c0778ba

which exactly matches the frozen output.

Every registered Boolean check remains true. This includes the packed base
screens, all integer-anchor screens, canonical endpoint ranges, exact
factorizations, selected-ledger deduplication, simultaneous preservation,
rank six, nullity zero, and the complete peeling witness.

The preserved \(N=667\) failure remains separate. Its packed plus screen
still gives

\[
\gcd(133+331,667)=29.
\]

It is not positive evidence.

## Nonblocking manifest note

The frozen statement and proof no longer use “hyperforest” for the abstract
countermodel. The current MANIFEST.md outcome paragraph still uses that old
word once. This does not alter the frozen theorem or this audit verdict.
Replace it with “multi-parent peelable incidence system” when the manifest
is finalized with the new audit hashes.

## Final boundary

F139 proves a genuine multi-row source effect and an exact rank boundary.
It remains conditional on finding a qualifying multi-owner product. It does
not prove that shifted residual classes become dependent. It also does not
prove that any dependency has a non-global normalized-root image. These are
the next mathematical gates.
