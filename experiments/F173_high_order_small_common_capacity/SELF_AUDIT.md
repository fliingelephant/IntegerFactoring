# F173 candidate self-audit

## Claim audited

F173 claims an existence-level interface obstruction. It constructs an
infinite trial-hard semiprime family with all four shifted ambient orders
carrying exponential prime factors, while every relevant common order is at
most six. Supplied primitive ordinary and torus witnesses then force the
named QP decoders into their hard-capacity branches.

It does not claim that Harvey--Hittmeir returns those witnesses or that
factoring is hard on the family.

## Quantifier audit

- The constants in the Linnik bounds are absolute.
- The family is constructed before a QP cap is applied.
- For every fixed QP function, all four selected primes exceed four times
  that cap after a finite prefix because their logarithms are linear in the
  input length.
- The family is unbalanced. No balanced-prime distribution is used.

## Construction audit

The first CRT class is reduced modulo the pairwise-coprime primes
\(3,r,u\). The second class is reduced modulo the pairwise-coprime moduli
\(H,s,t\). The added conditions modulo \(s,t\) do not change the F172
residue modulo \(H\), so all four shifted-gcd identities remain valid.

The size chain is

\[
p=r^{O(1)},
\quad H,s,t=p^{O(1)},
\quad q=p^{O(1)},
\]

and \(r<p<q\). Thus \(n=\Theta(\log r)\). There is no circular use of the
eventual input length.

## Screen audit

Each local primitive order contains a selected prime greater than the QP
cap. The matching cross-shift does not contain that prime because the
corresponding shifted gcd is at most six. This single observation verifies:

- failure of the \(\Lambda_T\) absolute return;
- failure of every capped relative return;
- distinct quotient fingerprints through the cap;
- no short equality or signed equality;
- no signed \(j(N\pm1)\) return for \(j\le T\).

The factor two in a signed equality is harmless because all selected primes
are odd and greater than \(4Q\).

## Exact-order audit

The candidate does not call the exact global order unavailable by
definition. It proves the opposite conditional: if that order and its
complete factorization are supplied, one standard prime-divisor screen
factors the input. This is the required distinction between an exact order
and the Harvey--Hittmeir lower-bound output.

## Capacity audit

The updater starts from a maximal local common subgroup: order six in the
ordinary channel and order \(b_\epsilon\) in each torus channel. A primitive
witness generates the full local ambient group, so its quotient fingerprint
has exact order ambient-order divided by the common order. The first
\(T(n)+1\) table entries are distinct in both components. The conclusion is a
capacity lower bound only. No exact quotient order is inferred.

## Scope risks retained

1. The primitive witnesses use the hidden factors for their existence
   construction. They are not a factor-free source.
2. Actual modular residues and torus coordinates can contain structure not
   modeled by order and capacity data.
3. The theorem checks the standard bounded power, equality, inverse,
   \(\Lambda_T\), and \(N\pm1\) channels. It does not quantify over every
   adaptive QP exponent or word grammar.
4. Cross-discriminant operations and integer-presentation decoders remain
   open.
5. The result is not a generic-group lower bound and not a complexity lower
   bound for factoring.

These limits are stated in the candidate and are necessary.
