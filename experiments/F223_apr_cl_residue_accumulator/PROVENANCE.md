# F223 provenance

## Namespace

Before creation, a repository-wide search found no F223 entry and no F223
experiment directory. The durable registry was not edited.

## Source question

The beta-two branch can combine a certified low-bit residue of a hidden
factor with any aggregate `M` dividing every `r-1` for `r|N`. The question
was whether APR or Cohen-Lenstra Jacobi-sum relations can add a compatible
residue modulus, and whether Las Vegas sampling can supply inverse-QP
progress.

F223 separates the question into four interfaces:

1. local character data and exact orbit membership;
2. compatibility of the local exponents;
3. the conditional known-residue terminal; and
4. the all-input probability law needed to generate progress.

## Closest prior packets

- F215 proves that scalar abelian reciprocity products preserve the
  beta-two inversion torsor. F223 is materially different. It studies the
  non-scalar APR/CL character family and the compatible exponent which can
  reconstruct a divisor residue.
- F220 proves the aggregate common-primary-order certificate and the
  beta-two/GFHP terminal. F223 adds an APR/CL orbit modulus `S` and a
  QP-size enumeration of compatible residues.
- F221 and F222 give exponential obstructions for random AKS projections.
  F223 gives separate fixed-bank, generic-model, and primary-2 anchor
  boundaries for the Jacobi-sum direction.

## Primary literature

1. Leonard M. Adleman, Carl Pomerance, and Robert S. Rumely,
   "On distinguishing prime numbers from composite numbers," *Annals of
   Mathematics* 117 (1983), 173-206,
   [journal page](https://annals.math.princeton.edu/1983/117-1/p07).
   Section 4, especially equations (4.5)-(4.6), steps C.1-C.5, and Remark
   4.1, supplies the consolidation and failure-scope comparison.
2. Henri Cohen and Hendrik W. Lenstra Jr., "Primality testing and Jacobi
   sums," *Mathematics of Computation* 42 (1984), 297-330,
   [DOI](https://doi.org/10.1090/S0025-5718-1984-0726006-X).
   Theorem 6.3, Theorem 7.8, and algorithms 11.1 and 12.1 supply the shared
   primary exponent, character relation, orbit conclusion, and algorithmic
   failure semantics.

The local orbit theorem, AP obstruction, probability tails, primary-2
fibre counts, and beta-two CRT composition are proved directly in this
packet.

## Numerical workflow

An earlier remote scan reported the concrete witness

\[
32987\cdot32993=1088340091,
\qquad f=66.
\]

That scan was exploratory. No preregistration or frozen source/output bytes
were supplied. F223 therefore contains no claimed remote command, timing,
resource record, output hash, or replay hash.

After the witness was known, `verify_witness.py` was written locally. It
uses only Python integer arithmetic and complete trial division. Its frozen
output is `POSTHOC_OUTPUT.json`. This is a reconstruction check, not a
preregistered experiment.

## Scope exclusions

F223 is not a lower bound against:

1. an auxiliary bank selected adaptively from `N`;
2. fresh randomized auxiliary primes with a proved conditional drift law;
3. coefficient-content or ideal-gcd extraction from a failed Jacobi-sum
   identity;
4. joint processing of many failed identities;
5. nonabelian or non-character cyclotomic data;
6. another source of low carry bits or common primary orders; or
7. a full APR/CL certificate that already satisfies Theorem C.

## Durable-state discipline

This packet does not edit `PROVED.md`, `FAILED.md`, `REGISTRY.md`,
`STATEMENT.md`, `notes/Progress.md`, `notes/Inspirations.md`, or any other
durable ledger. Promotion belongs to the root agent after independent
audit.

