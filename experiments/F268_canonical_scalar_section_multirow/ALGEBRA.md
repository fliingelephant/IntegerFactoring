# F268-D01 algebra — canonical scalar-section square-class circuits

## Status and exact seam

F268 is a preregistered finite search. It is not a factoring theorem.

Let `N` be odd. Let `E` be positive and even, with `gcd(E,N)=1`. For a
canonical unit `a` in `[1,N)`, define

\[
 U_E(a)=[a^E]_{N^2},\qquad Y_E(a)=[a^{E/2}]_N.
\]

Then

\[
 \boxed{Y_E(a)^2\equiv U_E(a)\pmod N}.                 \tag{1}
\]

The positive integer `U_E(a)` is below `N^2`, and its supplied root is
public. F268 gives a finite list of these rows to the complete P66 decoder.
The searched source is the fixed canonical `t=0` section `a in [1,N)`. There
is no random principal lift coordinate.

The closest promoted boundaries are P211 and P213. P211 proves that a fresh
principal lift gauge has a uniform affine carry. It explicitly leaves the
canonical section open. P213 bounds singletons, duplicates, reciprocal-output
pairs, and one fixed-past product against one fresh principal coordinate. It
explicitly leaves a fixed canonical section and a retrospectively selected
nonduplicate multirow dependency open. F268 searches exactly that remaining
interface.

P212/F245 bounds fresh uniform inverse-quotient differences, signed powers,
common-order accumulation, and feedback-free torus trials on a four-marker
family. It explicitly leaves canonical carries, biased sources, feedback,
and unrestricted relation decoders open. F268 uses no fresh inverse quotient
or torus word. It sends only canonical scalar power residues to the full
retrospective P66 decoder, after complete direct and low-support screens.

P66 and P138 are complete decoders and section theorems. They do not construct
rows. F262 searches polynomial Frobenius carries. F264 searches ordered
noncommutative matrix words. F265 uses elliptic cubic rows. F266 uses canonical
discriminants of transformed binary quadratic forms. None of those packets
searches a bank whose only P66 rows are the scalar integers `U_E(a)`.

The F26 canonical-inverse family uses endpoint products
`a*[a^-1]_N=1+Nk`. F268 tests those inverse carries as direct controls, but it
does not place them in its P66 list. Only the power residues (1) enter the
decoder.

## 1. Exact canonical-section carries

Write

\[
 U_E(a)=r_E(a)+Nh_E(a),\qquad 0\le r_E(a),h_E(a)<N.
\]

Both digits are public. F268 tests `gcd(h_E(a),N)` before it calls a later
relation strict. This is the direct canonical-digit channel that P211 leaves
open. The normalized digit `h_E(a)r_E(a)^{-1}` has the same gcd with `N`, so
it is not a separate gcd ticket.

The five frozen exponent schedules are

\[
 N-1,\quad N+1,\quad N^2-1,\quad 2(N-1),\quad2(N+1). \tag{2}
\]

They are even and coprime to `N`. None is divisible by `N`. Thus F268 does
not repackage P56's exponent-`N` lift-invariant homomorphism.

## 2. Multiplication-carry firewall

Let `a,b` be canonical units, put

\[
 c=[ab]_N,\qquad k={ab-c\over N}.
\]

The binomial theorem gives

\[
 (c+Nk)^E\equiv c^E+NEkc^{E-1}\pmod {N^2}.
\]

Since `a^Eb^E=(ab)^E`, the exact public integer

\[
 Q_E(a,b)={U_E(a)U_E(b)-U_E(c)\over N}               \tag{3}
\]

is integral and satisfies

\[
 \boxed{Q_E(a,b)\equiv Ekc^{E-1}\pmod N}.            \tag{4}
\]

Every multiplier in (4) is a unit. Therefore

\[
 \boxed{\gcd(Q_E(a,b),N)=\gcd(k,N)}.                 \tag{5}
\]

F268 verifies exact divisibility, congruence (4), and gcd equality (5) for
every registered multiplication edge. A proper gcd is a direct base-carry
factor, not a scalar-lift gain.

### Canonical inverse

If `b=[a^-1]_N`, then `ab=1+Nk` and

\[
 {U_E(a)U_E(b)-1\over N}\equiv Ek\pmod N.            \tag{6}
\]

Thus a canonical-inverse output carry has exactly the old inverse quotient's
prime support modulo `N`. This is a mandatory control.

### Canonical powers

If `c=[a^j]_N` and `k=(a^j-c)/N`, then

\[
 {U_{jE}(a)-U_E(c)\over N}\equiv Ekc^{E-1}\pmod N.   \tag{7}
\]

F268 verifies (7) whenever both displayed rows occur with the required
exponents. It never ranks (7) as a new ticket.

### Complement

Put `a^-=N-a`. For even `E`,

\[
 {U_E(a^-)-U_E(a)\over N}\equiv-Ea^{E-1}\pmod N.    \tag{8}
\]

The right side is a unit. The complete exact quotient in (8) therefore has
gcd one with `N`. Complement pairs remain useful only as possible members of
a larger exact square-class circuit.

## 3. Complete support-two test without factoring

For positive integers `u,v`, put `g=gcd(u,v)`. Since `u/g` and `v/g` are
coprime,

\[
 \boxed{uv\text{ is a square}\iff u/g\text{ and }v/g
 \text{ are both squares}.}                          \tag{9}
\]

If `u/g=s^2` and `v/g=t^2`, the exact positive root is

\[
 \sqrt{uv}=gst.                                      \tag{10}
\]

This tests every support-two rational square-class relation. It includes
equal rows, exact square multiples, reciprocal-looking pairs, complement
pairs, and relations that do not fit a named template. F268 tests (9) for
all retained pairs before the residual decoder. It also tests every singleton
integer square.

For a square relation with selected-row vector `c`, define

\[
 R(c)=\sqrt{\prod_iU_i^{c_i}},\qquad
 X(c)=\prod_iY_i^{c_i}\pmod N,
\]

and

\[
 \rho(c)=R(c)X(c)^{-1}\pmod N.                       \tag{11}
\]

Both signed gcds are tested. A non-global root is already a certified factor.
A global root is a low-support decoy.

## 4. Quotient by the complete low-support subspace

Let `G_<=2` be the set of enumerated weight-at-most-two dependencies whose
root comparison has been verified to be `GLOBAL_PLUS` or `GLOBAL_MINUS`.
Let `K` be the exact binary square-dependency kernel computed by P66. Let

\[
 L_{\mathrm{global},\le2}=\operatorname{span}(G_{\le2}). \tag{12}
\]

The source first enumerates every weight-at-most-two dependency by the
singleton test and (9). It counts and serializes every useful relation before
forming (12). A useful singleton or pair is an exact terminal factor
certificate. It is never discarded and never inserted into the decoy
subspace. Only relations whose two signed comparisons prove a global sign
enter `G_<=2`. The source does not infer this set from named patterns.

P66 makes `rho` a homomorphism from `K` to the square roots of one modulo
`N`. On the branch where no singleton or support-two comparison factored
`N`, every generator of `L_<=2` maps to `+1` or `-1`. Hence the complete
subspace maps into the global-sign subgroup.

On the branch with no useful low-support certificate,
`L_global,<=2=L_<=2`, the complete low-support squareclass subspace. Use
binary elimination to extend its basis to a basis of `K`. The new vectors
`q_1,...,q_d` form a basis of `K/L_<=2`. If every `rho(q_j)` is global, then
every `rho(c)` is global. Conversely, if any relation has a non-global root,
at least one quotient-basis vector has a non-global root. Therefore testing
the quotient basis is complete on that branch. Every nonzero quotient
representative has support at least three.

If any useful singleton or pair exists, F268 records the certificate and
ends the residual branch for that bank. It still authenticates the P66
kernel. It does not quotient a useful vector or relabel it as residual.

This is an exact quotient, not a score or cleanup heuristic. Deleting only
duplicates or only square multiples would be incomplete and is forbidden.

## 5. Factor-free P66 basis

F268 repeatedly splits explicit integer blocks by gcd and exact division
until the final blocks are pairwise coprime. It retains every row exponent
vector and verifies exact reconstruction. A final block that is not an exact
square contributes one parity equation. No block is assumed prime and every
such block has status `UNKNOWN_OPAQUE_NOT_NEEDED`.

Binary elimination produces the complete kernel `K`. Every low-support and
quotient-basis vector is checked against the parity matrix. Every emitted
relation certificate recomputes its exact product, exact positive root,
supplied root, normalized root, and both signed gcds.

## 6. Registered direct-screen chronology

The target chronology is immutable. First use the stage-1 source gcds to
construct the complete public bank and its syntax metadata. Complete direct
stages 2 through 4 without changing that bank. Next classify every singleton and
pair squareclass. Then either retain every useful low-support factor
certificate as a terminal disposition, or quotient only the verified
global-sign decoy span. Only the no-useful branch can emit retrospective P66
residuals, and each such residual has support at least three.

The global stages are:

1. every attempted or retained base, affine expression, inverse, and circuit
   result gcd;
2. every row high digit, `U_E(a)+/-1`, `Y_E(a)+/-1`, and complete
   two-primary chain endpoint;
3. all retained-pair base differences/sums, row differences/sums, supplied
   root differences/sums, and high-digit differences/sums;
4. every exact multiplication, inverse, power, and complement quotient in
   (3), (6), (7), and (8), including its base-carry equality;
5. every singleton exact-square root comparison;
6. every support-two square-class comparison from (9);
7. construction and authentication of the complete P66 kernel and the exact
   verified-global low-support decoy subspace; and
8. every quotient-basis root comparison.

Each stage has `tests,unit,full,proper` counters with
`tests=unit+full+proper`. A later stage cannot run for one row before an
earlier stage has completed for all rows. An assertion or exact-divisibility
failure aborts the full process. A relation is strict only if stages 1--6
have no proper gcd and the stage-8 quotient vector has a non-global root.

## 7. Exact scope

Finite discovery can reveal a reproducible scalar circuit or kill a frozen
grammar. It cannot prove an inverse-quasipolynomial all-input event law.
Even a held-out strict hit leaves the all-input source theorem, arbitrary
composite dispatch, uniform unbounded bit complexity, and Las Vegas expected
runtime proof open.
