# F165-R02 V2 fixed-depth cost theorem: independent proof draft

Status: candidate. This draft was derived only from
`V2_BLIND_STATEMENT.md`. It does not use the finite replay as evidence for the
unbounded claim.

## Claim

Let (L=\lceil\log_2(n+1)\rceil). Assume that the explicit base transcript has
total bit length (2^{L^{O(1)}}) and at most

\[
R_0\le 2^{C L^a}
\]

records. At each layer, enumerate every nonempty subset of the selected basis
with support at most (D\le L^b). Retain at most one canonical exact record
per attempt. Then, for each fixed (H\), generation, retention, complete
factor-free refinement, and full decoding through layer (H) use

\[
2^{L^{O_H(1)}}
\]

bit operations and space.

## 1. Attempt count

Let (M_{h+1}) be the number of attempts generated from layer (h). Since
(r_h\le R_h),

\[
M_{h+1}
=\sum_{d=1}^{\min(D,r_h)}{r_h\choose d}
\le (D+1)(R_h+1)^D.
\]

This bound also covers (D=0\), (r_h=0\), and (R_h=0\). Since at most one
new record is retained per attempt,

\[
R_{h+1}\le R_h+M_{h+1}.
\]

Suppose (R_h\le 2^{L^{k_h}}), after increasing a fixed exponent or constant
if necessary. For (L\ge2),

\[
\begin{aligned}
\log_2(M_{h+1}+1)
&\le O(\log(D+2))+D\log_2(R_h+1)\\
&\le L^{O(k_h+b+1)}.
\end{aligned}
\]

Thus (R_{h+1}\le2^{L^{k_{h+1}}}) for some fixed
(k_{h+1}=O(k_h+b+1)). The constant in this exponent can depend on the layer.

## 2. Bit lengths of generated records

All decorated residues are maintained modulo (N). Reduce after every
multiplication and after every parity-block correction. Each residue and its
least positive inverse therefore has (O(n)) bits. The retained exact value
is (A=zw<N^2), so it also has (O(n)) bits. A subset description needs at
most (D\lceil\log_2(R_h+1)\rceil) bits. Other fixed record metadata is no
larger than a polynomial in these quantities and the current transcript.

Because (n\le2^L), every generated record has

\[
2^{L^{O(1)}}+L^b\log_2(R_h+1)
\]

bits. Let (S_h) denote the total bit length of the retained transcript
through layer (h). The attempt bound and the one-record-per-attempt rule give

\[
S_{h+1}\le
S_h+M_{h+1}\operatorname{poly}
\bigl(n,D,\log(R_h+1),S_h\bigr).
\]

Consequently, if (S_h\le2^{L^{s_h}}), then
(S_{h+1}\le2^{L^{s_{h+1}}}) for a fixed exponent
(s_{h+1}=O(s_h+k_h+b+1)).

This argument counts all attempts, including duplicates. Canonicalization can
use a dictionary keyed by the exact integer and decorated root. Hashing is not
needed for correctness: a balanced comparison tree gives a deterministic
alternative with polynomial overhead in the transcript length.

## 3. Factor-free refinement is polynomial in transcript length

Here is a constructive bound. Start with one labelled component for each
distinct exact value. A component is a positive base together with its sparse
vector of multiplicities in the labelled records.

Repeat these operations:

1. If a base is a perfect (e)-th power, replace it by its maximal exact root
   and multiply its multiplicity vector by (e).
2. For two bases (x,y) with (g=\gcd(x,y)>1), replace their occurrences by
   (g,x/g,y/g). Add multiplicity vectors when the same base occurs more than
   once.

These transformations preserve every labelled exact value. Let

\[
\Phi=\sum_{	ext{distinct component bases }q}\log_2 q.
\]

Initially (Phi\le S_h). A perfect-power extraction strictly decreases
(Phi). A gcd refinement changes the contribution of (x,y) from
(log_2x+log_2y) to at most

\[
\log_2g+\log_2(x/g)+\log_2(y/g)
=\log_2x+log_2y-log_2g,
\]

so it decreases (Phi) by at least one. Merging equal bases decreases it
further. Hence there are at most (S_h) refinement steps. There are at most
(R_h+S_h) live components. Even a naive scan of all component pairs at each
step uses only polynomially many gcd operations.

Maximal perfect powers can be found without factoring: test the possible
exponents up to the bit length and use exact integer-root computation. This is
polynomial in the base bit length. Integer gcd, division, multiplication, and
exact-root computation all have polynomial bit complexity. Sparse
multiplicity vectors also have polynomial total size. Thus complete
factor-free refinement uses (operatorname{poly}(S_h)) bit operations and
space.

At termination, the component bases are pairwise coprime and are not perfect
powers. For each labelled value, split every component exponent into its even
part and its parity. This gives uniquely

\[
A=s^2\prod_j q_j^{v_j},\qquad v_j\in\{0,1\}.
\]

Components whose multiplicities are even in every record contribute only to
the square parts and do not create parity rows. The remaining blocks are
pairwise coprime nonsquares.

## 4. Full decoding is polynomial in transcript length

The parity matrix has at most (R_h) columns and at most (R_h+S_h) rows.
Gaussian elimination over (mathbf F_2), including recording a complete
kernel basis and the first-occurrence column basis, is polynomial in (S_h).

There are at most (R_h) kernel-basis dependencies. For one dependency, the
product of its exact records has bit length at most (S_h). Its exact positive
square root, the product of supplied roots modulo (N), both signed gcd
tests, and the normalized residue therefore have polynomial bit complexity.
The square parts, decorated lifts, and selected columns also occupy
polynomial space. This accounts for complete decoding, not only rank
calculation.

For generation, a conservative implementation can spend polynomial time in
the current transcript per attempt. It can scan all parity rows to apply the
needed block corrections. Multiplying this polynomial by (M_{h+1}) remains
quasipolynomial under the bounds above.

## 5. Fixed-depth induction

The base assumptions give (R_0,S_0\le2^{L^{O(1)}}). Sections 1--4 show that
one layer maps quasipolynomial record count and transcript length to new
quasipolynomial bounds, with an exponent that can increase by a quantity
depending on (b) and the prior exponent. Induction for the finite sequence
(0,1,\ldots,H) proves

\[
T_H,\;\mathrm{Space}_H\le2^{L^{O_H(1)}}.
\]

Storing every attempt would still satisfy this space bound. Streaming
duplicate attempts and sequence hashes only lowers the space use.

The dependence on (H) is essential in this proof. For example, the exponent
recurrence can increase by about (b) at each layer. If (H) grows with
(n), this does not yield one fixed quasipolynomial exponent. The proof also
contains no claim that a factor certificate ever occurs. Therefore it proves
the stated fixed-depth cost theorem and no success theorem.
