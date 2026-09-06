# F269-D02 preregistration — adaptive Euclidean prefix search

## Status

**Status:** D02 repair candidate; not frozen. It preserves the D01 algebra,
expression grammar, cohorts, selection, and finite verdict semantics. It
changes only the evidence/resource implementation required by the failed D01
hostile pre-run audit, plus the registered maximum-work and grammar-evidence
fixtures needed to test those same semantics. The intended host currently has
no writable delegated cgroup-v2 leaf, which this contract requires before
compile. Freeze is pending an explicit enforcement decision. Production
remains forbidden until a fresh hostile static audit and measured stress
preflight both pass.

F269-D02 is incompatible with an active F265 production or validation
process. It must not compile, benchmark, generate a corpus, or run while F265
is active.

## 1. Exact question and imported grant

For a balanced distinct odd semiprime

```text
N=p*q, p<q<2*p,
```

grant a correct beta-two reciprocal prefix

```text
u=p^(-1) mod m, m=2^t.
```

At every stage

```text
1 <= t < floor((bitlength(N)-1)/4),
```

the program constructs the four public quotient corners from `(N,t,u)`.
It asks whether a bounded exact Euclidean expression selects the factor-lift
bit `a` in `p=r+a*m mod 2m` or gives a proper certified gcd. It then converts
the prediction to the reciprocal-lift bit `e` by

```text
kappa = ((u*r-1)/m) mod 2
e = a xor kappa.
```

The prefix is an explicit grant. F269 does not claim to compute it. A finite
selector is not a theorem.

## 2. Closest prior routes and exact difference

### F210-D01 / P185

F210-D01 completely factored four branch-relative quotient children on
small cohorts. Its fixed feature menu included one Euclidean quotient and
remainder between its compatible and crossed quotient children, scalar
factorization summaries, and a fixed modular action bank. Its held-out
selector and action results were null.

F269 first proves that the scaled F210 quartet is the one public rectangle

```text
K, K-r, K-c, K-r-c-m.
```

It removes every affine duplicate and the forced first quotient of every
corner pair. Its live objects are all six residual Euclidean tails,
corner-coordinate tails, depth-2/4/8 continuants, cross-tail determinants,
and short adaptive compositions. It uses no factorization summary and no
recursive child call. F210 did not test this grammar.

### F261-D02

F261 assumes the zero-defect family `2^floor(n/2) | N-1`. It searches
multipliers, two hidden nearest centers, and a hidden centered carry. Its
prefix only filters a carry bank.

F269 has no zero-defect condition, multiplier search, nearest center, or
oracle carry. After the prefix grant, every expression is a function of
`(N,t,u)` only.

### F263-D02 / F267 / P220

F263 searches short blocks, product jets, and transfer states in a
characteristic-size central-binomial or shifted recurrence. F267 proves that
all its finite non-direct hits are public `p=floor(sqrt(N))-s` query-boundary
or first-Fermat controls.

F269 has no arithmetic-progression block, binomial product, transfer jet, or
`floor(sqrt(N))-s` syntax. It screens the first Fermat trial before scoring.
Its exact divisions act only on public `O(n)`-bit quotient states.

## 3. Public-source firewall

The expression grammar is constructed before any labelled modulus exists.
It has fixed role names, typed layers, operation order, syntax order, seed,
and caps.

For one stage, the arithmetic entry point is exactly

```text
analyze_public(N, t, u)
```

It does not accept `p`, `q`, a target bit, a cohort name, or a factor-bit
label. It verifies every displayed divisibility, positivity, unit, rectangle,
difference, affine-carry, and Euclidean-shell identity before it returns.

The corpus generator uses hidden `p,q` only to make `N`, the granted prefix
`u`, the factor-lift label `a`, and the reciprocal-lift label `e`. It invokes
`analyze_public` first. It attaches both labels only after all public values
for that row are complete.

The audit labels are computed exactly as

```text
a_hidden = ((p-r)/m) mod 2
e_hidden = ((inverse_mod(p,2*m)-u)/m) mod 2
b_hidden = ((q-c)/m) mod 2.
```

After public evaluation, require `b_hidden=a_hidden xor delta` and
`e_hidden=a_hidden xor kappa`. These checks do not change any value, syntax,
validity mask, or decision. A failure aborts the process.

No hidden or oracle value enters:

- expression construction;
- syntactic canonicalization;
- an adaptive branch;
- expression validity;
- direct-gcd evaluation; or
- held-out replay.

## 4. Exact public controls

For every modulus, first test the public Fermat value

```text
A=ceil(sqrt(N)), D=A*A-N.
```

If `D` is a square and gives a proper factor, mark the complete modulus
`FIRST_FERMAT_CONTROL`. Preserve it, but exclude all its stages from selector
ranking and lead counts.

At each retained stage, verify:

1. `m=2^t`, `u` is an odd unit, and `r=u^(-1) mod m`;
2. `m | u*r-1`, `kappa=((u*r-1)/m) mod 2`, and the exact conversion
   `e=a xor kappa` for the hidden audit label;
3. `c=N*u mod m`, `m | N-r*c`, and `delta=K mod 2`;
4. all four lifted products are below `N` and all four corners are positive;
5. all corners and their own two coordinates have the unit gcds proved in
   `DRAFT_ALGEBRA.md`;
6. the translated rectangle and six exact difference identities;
7. all four `J-2K` coordinate identities, where `J` is the crossed scaled
   corner and is not P185's quantity `H=2mK`;
8. `N>8m^2`; for each formal pair, a zero registered gap gives equal corners
   and constructor status `ZERO_GAP`, while every nonzero pair has first
   quotient exactly one and first remainder equal to its registered gap; and
9. both same-coordinate ordered resultant identities, their complete
   coefficient triples, and their evaluations at every chart point in the
   literal ordered array `{-2,-1,0,1,2,3}`.

An identity failure aborts the process. It cannot become an ineligible row.

There are two disjoint control types.

`SYMBOLIC_CONTROL` contains the ordered coefficient triples of
`2*Res_Q(F_0,F_1)` and `2*Res_P(F_0,F_1)`, the six evaluations of each, and
the two sign-normalized discriminant formulas. The resultant convention is
literally `A_0*B_1-A_1*B_0`, with `F_0` first, as fixed in Algebra (12a).
The checked coefficient triples are exactly Algebra (15a). The left side is
always twice the ordered resultant; the checker does not divide by two or
change its sign. Only discriminant reporting multiplies the `delta=1`
`Q`-resultant polynomial by minus one to make it monic. Symbolic controls
verify identities and serialize coefficient/evaluation evidence. Neither a
coefficient nor an evaluation enters the integer row-control equality set.

`ROW_CONTROL` contains the actual row integers `0,1,m,r,c,S`, all lifted
coordinates, all four corners, all six gaps, all `J-2K` coordinate values,
and the first-Fermat integers when they exist. Raw corner differences,
`J-2K` coordinates, direct balanced-box scans, public `B-s` offsets, and a
Fermat step are controls. They are not expression terminals. The two control
types have disjoint enums and output columns; a value cannot move from the
symbolic set into the row set by numerical coincidence.

The exact self-test includes both reciprocal/factor-bit orientations:

```text
m=4, u=r=1: kappa=0, so e=a;
m=8, u=r=3: kappa=1, so e=a xor 1.
```

For each fixture and both `a` values, it multiplies `(u+e*m)(r+a*m)` modulo
`2m` and requires one. It also requires the hidden-label constructor and
public postprocessor to produce the same `e`. A failure aborts before any
benchmark.

The exact zero-gap/alias fixture uses `N=10541` twice. At `t=1,u=1`, require
`r=c=1,K=5270,delta=0`; tail ID 5 (`PX:OX`) must be `ZERO_GAP` on both
branches and must perform zero divisions. At `t=2,u=3`, require
`r=c=3,K=2633,delta=1`; tail ID 0 (`PC:OC`) must be `ZERO_GAP` on both
branches and must perform zero divisions. The latter row must also reproduce
the two `PC:R=OC:C` aliases stated in Algebra. The second literal `t=1`
fixture is `N=943=23*41,u=r=c=1,K=471,delta=1`. Together, the
`(N,t,u)=(10541,1,1)` and `(943,1,1)` fixtures cover both possible `t=1`
parities. They require tail ID 5 to be the unique zero-gap pair role when
`delta=0`, tail ID 0 to be the unique zero-gap pair role when `delta=1`, and
exactly thirty ordinary root attempts on that tail and branch to carry reason
`ZERO_GAP`. The test runs both candidate branches. No fixture is allowed to
replace a missing numeric value by zero.

## 5. Fixed expression language for D02

This section is frozen. The source audit remains mandatory before production.

### Exact integer semantics

All expression values are signed `boost::multiprecision::cpp_int` values.
Define

```text
abs_cpp(x)   = x if x>=0, else -x
signbit(x)   = 1 iff x<0
bitlength(0) = 0
bitlength(x) = 1+floor(log2(abs_cpp(x))) for x!=0
v2_nonzero(x)= largest v>=0 with 2^v | abs_cpp(x), for x!=0
```

The sign is not included in `bitlength`. `v2_nonzero(0)` is invalid.

For `floor_div(x,d)`, first require `d!=0` and normalize `D=abs_cpp(d)`.
The returned pair `(q,r)` is the unique pair satisfying

```text
x = q*D+r, 0<=r<D.
```

Thus `q=floor(x/D)` also for negative `x`; C++ truncating division is never
used as the definition. For example, `floor_div(-1,3)=-1` and its remainder
is two. `euclidean_rem(x,d)` returns this `r`. `centered_rem(x,d)` returns
`r-D` only when `2*r>D`; an exact half tie returns `+D/2`. Zero denominators
make all three operations invalid. `gcd_abs(x,y)` is the nonnegative gcd of
`abs_cpp(x),abs_cpp(y)`, with `gcd_abs(0,0)=0`.

Every nonconstant value must have signed bit length at most

```text
8*bitlength(N)+256.
```

Crossing the cap makes the expression invalid. It does not truncate or
reduce the value.

### Typed operand firewall

The F269 operational grammar has three disjoint operand types. The separate
verification-only `SYMBOLIC_CONTROL` type is not an operand type.

1. `CONTROL_ONLY`: raw corners, raw gaps, `R_a,C_(b_a)`, `m,r,c,K,S`,
   `J_a-2K_a`, and Fermat values. These exist only to verify algebra and
   construct an allowed residual Euclidean tail. Resultant objects have the
   separate non-scalar type `SYMBOLIC_CONTROL` and cannot enter either a tail
   or a row-value comparison.
2. `TAIL_STATE`: one normalized residual state `(B,d)` after the forced first
   corner-pair quotient, or one `(corner,own-coordinate)` state. A tail state
   is a structured pair. It is not a scalar operand.
3. `SCOREABLE`: a registered non-initial quotient/remainder, centered
   remainder, chain aggregate, or continuant extracted by advancing a
   `TAIL_STATE` at least one additional Euclidean step.

`CONTROL_ONLY` values can enter only the audited constructors
`make_pair_tail` and `make_coordinate_tail`. They cannot enter a scoreable
operation, an adaptive guard, a selector ticket, or a direct-gcd ticket.
Raw corners and gaps are therefore not scalar terminals.

The constructor marks every scalar with an exact dependency mask containing
the source corner IDs, source gap ID, step index, and extraction operation.
Reject a scalar before scoring when the literal rewrite system below gives
any of:

```text
constant; m; r; c; S; R_a; C_(b_a); one raw corner; one raw gap;
J_a-2K_a; or plus/minus any of these.
```

The filter is syntax-directed. Its affine form is the coefficient vector
`AFF(v_K,v_r,v_c,v_m,v_1)` in the public basis `(K,r,c,m,1)`. `CONST(z)` is
the special affine vector `(0,0,0,0,z)`. `ABS_AFF(v)` identifies `v` and
`-v` by choosing the sign whose first nonzero coefficient is positive.
`TAG(id,payload)` records a declared non-affine control constructor.
`OPAQUE` means that this finite rewrite system has no rule. It does not mean
that the value is new.

The literal affine control table is:

```text
id                 exact form
M                  (0,0,0,1,0)
R                  (0,1,0,0,0)
C                  (0,0,1,0,0)
S                  (0,1,1,1,0)
R0,R1              (0,1,0,0,0), (0,1,0,1,0)
C0,C1              (0,0,1,0,0), (0,0,1,1,0)
Z00,Z10,Z01,Z11    (1,0,0,0,0), (1,0,-1,0,0),
                   (1,-1,0,0,0), (1,-1,-1,-1,0)
G00_10,G00_01      (0,0,1,0,0), (0,1,0,0,0)
G00_11             (0,1,1,1,0)
G10_01             ABS_AFF(0,1,-1,0,0)
G10_11,G01_11      (0,1,0,1,0), (0,0,1,1,0)
JLOCAL_R(a,delta)  (2*(a xor delta)-1)*R_a
JLOCAL_C(a,delta)  (2*a-1)*C_(a xor delta)
```

`JLOCAL_R` is `J_a-2K_a`. `JLOCAL_C` is `J_(1-a)-2K_a`. The table includes
both signs of every displayed form when it tests control equivalence. Every
`CONST(z)` is a constant control, for all signed integers `z`; the displayed
`0,1` are only the values also placed in the row-level control set.

The registered non-affine `ROW_CONTROL` tags are literal IDs

```text
FERMAT_A, FERMAT_D, FERMAT_MINUS, FERMAT_PLUS.
```

`FERMAT_A=ceil(sqrt(N))` and `FERMAT_D=FERMAT_A*FERMAT_A-N`; the last two
tags exist only when `FERMAT_D` is a square and have payloads
`FERMAT_A-sqrt(FERMAT_D)` and `FERMAT_A+sqrt(FERMAT_D)`. These tags are
constructor-only. Resultant coefficients, evaluations, and discriminants use
the separate `SYMBOLIC_CONTROL` enum from Section 4. They never receive a
row-control `TAG` and never enter the row-value equality firewall.

The normalizer uses only this rewrite table:

```text
constructor or op    supported exact rewrite
raw affine atom      AFF(the literal vector above)
abs                  CONST -> exact CONST;
                     AFF -> signed AFF when its sign is proved, else ABS_AFF;
                     ABS_AFF -> itself
bitlength,v2         exact CONST evaluation; v2(0) is INVALID
add                  AFF+AFF -> coefficient addition
absdiff              AFF-AFF -> abs by the abs rule
min,max              identical forms -> that form;
                     two AFF forms -> one arm only when their difference sign
                     is proved
gcd_abs              two CONST values -> exact CONST;
                     gcd(0,x) or gcd(x,0) -> abs(x);
                     identical forms -> abs(form)
product              two CONST values -> exact CONST;
                     0*x -> CONST(0), 1*x -> x;
                     (-1)*AFF(v) -> AFF(-v)
floor_div            two CONST values -> exact CONST;
                     0/d -> CONST(0) when d is proved nonzero;
                     x/(+/-1) -> x
euclidean_rem        two CONST values -> exact CONST;
                     0 mod d -> CONST(0) when d is proved nonzero;
                     x mod (+/-1) -> CONST(0)
centered_rem         two CONST values -> exact CONST;
                     the same zero and unit-denominator rules
select_parity        choose the literal arm fixed by the chamber bit
select_sign          identical arms -> that arm; otherwise choose an arm only
                     when the guard sign is proved
select_lt            identical arms -> that arm; otherwise choose an arm only
                     when the sign of g-h is proved
```

Every unlisted case returns `OPAQUE`. A sign is proved only for an exact
signed integer constant; an exact signed copy of a table entry known positive
from Algebra (5)--(10); or `r-c`, whose sign follows from the chamber order.
Zero is proved only by an exact zero vector or the `r=c` chamber. This is a
closed rule table. The source cannot add algebraic simplifications.

The normalizer enumerates exactly 24 formal chambers

```text
a in {0,1}, delta in {0,1}, kappa in {0,1},
order(r,c) in {less=0,equal=1,greater=2}.
```

The chamber index and bit are

```text
i=12*a+6*delta+3*kappa+order_code,
CHAMBER_BIT=uint32(1)<<i.
```

No formal chamber is removed as infeasible. For each syntax, bit `i` of
`CONTROL_CASE_MASK` is one exactly when its chamber normal form is a
`CONST`, a signed affine/absolute-affine match to the literal control table,
or a matching registered `TAG`. `OPAQUE` never sets a bit. Reject a syntax
globally exactly when the mask is `0x00ffffff`. If the mask is nonzero but
not full, retain the syntax and mark candidate branch `a` invalid on a row
exactly when the bit indexed by that row's `(a,delta,kappa,order(r,c))` is
set. The mask is serialized as eight lowercase hexadecimal digits. The
normalizer never uses a cohort row or label. The row-level value firewall
below still tests every retained `OPAQUE` case. The packet does not claim an
identity solver for arbitrary floor expressions.

### Scoreable roots

For each candidate factor-lift branch `a`, name the four corner roles

```text
PC = candidate-compatible, OC = opposite-compatible,
PX = candidate-crossed,    OX = opposite-crossed.
```

They mean exactly

```text
PC=Z_(a,b_a),             OC=Z_(1-a,b_(1-a)),
PX=Z_(a,1-b_a),           OX=Z_(1-a,1-b_(1-a)),
b_j=j xor delta.
```

Create exactly 14 structured tail roles:

```text
six pair tails:
  PC:OC, PC:PX, PC:OX, OC:PX, OC:OX, PX:OX
eight own-coordinate tails:
  PC:R, PC:C, OC:R, OC:C, PX:R, PX:C, OX:R, OX:C.
```

For each candidate factor-lift branch `a`, these role names map publicly to
the appropriate rectangle corners and their own `R_x,C_y` coordinates.
For a pair tail, compute the actual unsigned corner gap before ordering the
state. A zero gap creates the nonnumeric constructor status `ZERO_GAP`; no
division, quotient, remainder, trace, alias value, or scalar sentinel is
created. A nonzero pair tail starts at `(x_0,x_1)=(B,d)` after the proved
quotient one. Coordinate tails start at `(corner,own-coordinate)`. Every
numeric tail satisfies `x_0>x_1>0`. Write every further division as

```text
x_(j-1) = q_j*x_j+x_(j+1),
q_j=floor(x_(j-1)/x_j),
0<=x_(j+1)<x_j, j=1,2,... .
```

The source keeps an immutable `tail_id` and step index on every extraction.
It performs at most nine divisions and records `x_0,...,x_10` only as far as
they exist. Define the strict-depth bit

```text
STRICT_d = 1 iff the tail is numeric and x_(d+2)>0, 1<=d<=8.
```

Thus every scoreable step-`j` quotient, remainder, or centered remainder uses
`STRICT_j`, not merely the existence of `q_j`. Every depth-`d` aggregate or
continuant uses `STRICT_d`. A false bit is `DEPTH_MISSING`, not numeric zero.

The quotient word has this orientation: `q_1` is the first quotient of the
displayed starting pair, and a depth-`d` prefix is `(q_1,...,q_d)`. Define

```text
P_0=1, Q_0=0,
P_1=q_1, Q_1=1,
P_j=q_j*P_(j-1)+P_(j-2),
Q_j=q_j*Q_(j-1)+Q_(j-2), 2<=j<=d.
```

The source requires

```text
P_d/Q_d=[q_1;q_2,...,q_d],
P_d*Q_(d-1)-P_(d-1)*Q_d=(-1)^d
```

on every constructed prefix. `P_d` is the registered numerator continuant.
`Q_d` is the registered denominator continuant. For an ordered registered
tail pair `(T,T')`, the cross root is the signed integer

```text
D_d(T,T')=P_d(T)*Q_d(T')-Q_d(T)*P_d(T').
```

The literal displayed order `(T,T')` is semantic. Do not take an absolute
value. Do not sort the roles. Reversing the roles negates the root.

The ninth division is lookahead only: its quotient, remainder, continuant,
and aggregates are never scoreable and never enter a tuple. A registered
prefix of depth `d` is scoreable only when `STRICT_d=1`. Thus at least two
nonzero Euclidean state entries remain after the prefix. No scoreable prefix
is a complete continued fraction, and the terminal gcd scale is never
exposed.

Scoreable roots are:

- one quotient or one remainder at one registered step 1 through 8;
- one centered remainder at step 1 or 2;
- the quotient sum or maximum quotient of one strict prefix of depth 2, 4,
  or 8;
- one continuant numerator or denominator of one strict prefix of depth 2,
  4, or 8; and
- the fixed 2-by-2 cross-continuant determinants at depths 2, 4, and 8 for
  these eight role pairs:

```text
(PC:PX,OC:OX), (PC:OX,OC:PX),
(PC:R,OC:R),   (PC:C,OC:C),
(PX:R,OX:R),   (PX:C,OX:C),
(PC:R,PX:C),   (PC:C,PX:R).
```

Both prefixes of a cross root must satisfy the strict-prefix condition. If
either declared tail is `ZERO_GAP`, the cross-root attempt has reason
`ZERO_GAP`. Otherwise, if either `STRICT_d` bit is zero, it has reason
`DEPTH_MISSING`. Otherwise, if the two complete numeric tail serializations
have the same actual tail-alias ID, it has reason `TAIL_STATE_ALIAS`. It has a
numeric determinant only when both bits are one and the tails are not actual
aliases.
Apply the row-level public-control equality rejection to every numeric root
before it can become scoreable. Its static root syntax remains `OPAQUE` as
specified below. No missing ordinary or cross root uses a numeric sentinel.

For depth eight, the strict-prefix predicate reads `x_10` produced by the
unscored ninth lookahead division. If the ninth division terminates or
`x_10=0`, every depth-eight root for that tail is invalid. The source asserts
that no step-nine value appears in a root, tuple operand, guard, ticket, or
output other than the boolean strict-prefix mask and aggregate lookahead
counter. In particular, `q_9` is not part of the depth-eight continuant.

Every ordinary scoreable root carries a provenance set containing its
`tail_id`, every raw corner role used by that tail, its raw gap role when
applicable, and its explicit own-coordinate role when applicable. A
cross-continuant root carries the union for its two declared tails. The eight
registered cross pairs above have disjoint source sets by construction.

The tuple generator preserves provenance unions. It requires all scalar
operands of one binary or adaptive tuple to have pairwise-disjoint provenance
sets. Public bit guards have the empty set. Consequently it cannot combine
`q_j,x_(j+1),x_(j+2)` from one tail to reconstruct
`x_j=q_(j+1)*x_(j+1)+x_(j+2)`, or combine two tails through a shared raw
corner, gap, or lifted coordinate. This structural rule is checked before the
affine-equivalence filter.

### Literal IDs and canonical UTF-8 syntax

Tail role IDs are the zero-based positions in this literal array:

```text
0 PC:OC   1 PC:PX   2 PC:OX   3 OC:PX   4 OC:OX   5 PX:OX
6 PC:R    7 PC:C    8 OC:R    9 OC:C   10 PX:R   11 PX:C
12 OX:R  13 OX:C
```

Cross-pair IDs are the zero-based positions in this literal array. Pair
orientation is part of the ID.

```text
0 (PC:PX,OC:OX)  1 (PC:OX,OC:PX)
2 (PC:R,OC:R)    3 (PC:C,OC:C)
4 (PX:R,OX:R)    5 (PX:C,OX:C)
6 (PC:R,PX:C)    7 (PC:C,PX:R)
```

Ordinary root-kind enum order is:

```text
0 QUOTIENT             parameter j in [1,9)
1 REMAINDER            parameter j in [1,9)
2 CENTERED_REMAINDER   parameter j in [1,3)
3 QUOTIENT_SUM         parameter d in {2,4,8}
4 QUOTIENT_MAX         parameter d in {2,4,8}
5 CONTINUANT_P         parameter d in {2,4,8}
6 CONTINUANT_Q         parameter d in {2,4,8}
```

For each tail ID, enumerate root kinds in this order and parameters in
increasing order. Then enumerate cross-pair IDs in increasing order and
depths `2,4,8`. The root-attempt ID is literal:

```text
ordinary: 30*tail_id + offset
  QUOTIENT j:           offset=j-1          (0..7)
  REMAINDER j:          offset=8+j-1        (8..15)
  CENTERED_REMAINDER j: offset=16+j-1       (16..17)
  QUOTIENT_SUM d:       offset=18+depth_id  (18..20)
  QUOTIENT_MAX d:       offset=21+depth_id  (21..23)
  CONTINUANT_P d:       offset=24+depth_id  (24..26)
  CONTINUANT_Q d:       offset=27+depth_id  (27..29)
cross: 420+3*cross_pair_id+depth_id          (420..443)
depth_id(2)=0, depth_id(4)=1, depth_id(8)=2.
```

This gives exactly `14*30+8*3=444` root attempts and exactly 444 distinct
root syntax nodes. A root attempt is a static syntax construction, not a
claim that a numeric root exists on a row. All 444 root syntax nodes exist
before any corpus. The chamber normal form of a root constructor is
`OPAQUE`, so its static `CONTROL_CASE_MASK` is zero. Row evaluation stores
either one exact integer or one invalid reason for every attempt and branch.
Missing roots do not remove syntax nodes, change a later operand array, or
cause a replacement attempt.

There is no special abort or fallback for `ALL_ROOTS_MISSING` or
`ALL_CROSS_ROOTS_MISSING` on a row or branch. A branch with all roots missing
has an all-zero `ROOT_VALID_MASK`; every dependent tuple propagates the
smallest child reason, and that branch bit stays clear for every expression.
If both branches are missing, selector prediction is `NA` and counts as an
error after labels attach. Static operand-array reductions still use the 444
root syntax nodes, never the number of numeric row values, so no row can cause
a modulo-zero draw or a grammar change. The same rule applies when only all
24 cross-root attempts are missing.

The fixed `ROOT_ATTEMPT_MASK` has bits 0 through 443 set. Mask bytes use
little-endian bit numbering within increasing byte order: attempt `i` is bit
`i mod 8` of byte `floor(i/8)`. Hex serialization prints byte zero first,
two lowercase digits per byte. Thus the literal 56-byte mask is 55 bytes
`ff` followed by one byte `0f`; the upper four padding bits must be zero.
For each row and branch, `ROOT_VALID_MASK` uses the same 56-byte encoding and
sets a bit exactly when that attempt has a numeric value. A parallel
444-entry `ROOT_REASON` array stores the enum below. Its packed form has 222
bytes: even attempt `2i` occupies the low nibble of byte `i`, and odd attempt
`2i+1` occupies the high nibble. Bytes print in increasing `i` order as 444
lowercase hexadecimal digits. A valid entry has reason zero. An invalid entry
has no value field.

Runtime invalid reasons and their precedence are the literal enum:

```text
0 VALID
1 ZERO_GAP
2 DEPTH_MISSING
3 CONTROL_CASE
4 TAIL_STATE_ALIAS
5 EQUAL_OPERAND_VALUE
6 ZERO_DENOMINATOR
7 V2_ZERO
8 VALUE_CAP
9 ROW_CONTROL_EQUALITY
```

When several conditions apply, keep the smallest nonzero ID. A parent first
propagates the smallest child reason; it then tests its own conditions in the
displayed order. `TAIL_STATE_ALIAS` means that two scalar operands depend on
distinct formal tail IDs whose complete actual tail serializations have the
same canonical tail-alias ID. `EQUAL_OPERAND_VALUE` means that the remaining
chosen scalar operands have the same exact signed value. A result equal to a
row control or its negative has reason `ROW_CONTROL_EQUALITY`. Static type,
provenance-overlap, duplicate-syntax, and all-chamber-control rejects happen
during grammar construction and therefore have no runtime reason record.
`CONTROL_REINTRODUCTION`, `gcd unit`, `gcd full`, and `gcd proper` are ticket
partitions, not expression invalid reasons.

For any retained expression on one row, `BRANCH_VALID_MASK` is a two-bit
integer: bit zero is candidate `a=0`, bit one is candidate `a=1`. Serialize
it as exactly two lowercase hexadecimal digits `00`,`01`,`02`, or `03`.
Selector comparison is defined only for `03`. Any other mask produces no
prediction. In TSV, every absent `prediction_a` or `prediction_e` is the
literal ASCII bytes `NA`; an empty field, `-1`, zero, and a reused target bit
are forbidden sentinels. After labels attach, an absent prediction counts as
one error. `INVALID_REASON_MASK` is a 16-bit OR mask over encountered runtime
reason IDs, serialized as four lowercase hexadecimal digits with bit `j`
corresponding to reason ID `j`.

The mask/absence self-test is literal. A synthetic tail `(13,5)` has trace

```text
x: 13,5,3,2,1,0
q: 2,1,1,2.
```

For its thirty ordinary attempt offsets, exactly
`0,1,8,9,16,17,18,21,24,27` are valid; the other twenty have
`DEPTH_MISSING`. Pairing this tail with a Fibonacci long tail makes the
depth-two cross root valid and the depth-four and depth-eight cross roots
`DEPTH_MISSING`. Replacing the short tail by a `ZERO_GAP` constructor state
makes all three cross roots `ZERO_GAP`. Injected branch pairs
of two identical long tail serializations make all three cross roots
`TAIL_STATE_ALIAS`. Independently, injected expression branch pairs
`(valid,valid)`, `(valid,missing)`, `(missing,valid)`, and
`(missing,missing)` must serialize branch masks `03`,`01`,`02`,`00`; the last
three selector predictions serialize as `NA`.

An `ALL_ROOTS_MISSING` fixture sets all 444 reason entries to
`DEPTH_MISSING`, requires an all-zero `ROOT_VALID_MASK`, evaluates every
retained DAG without changing the static operand arrays, and requires the
branch bit to stay clear throughout. An `ALL_CROSS_ROOTS_MISSING` fixture
sets attempts 420 through 443 to `DEPTH_MISSING` while leaving the ordinary
fixture roots valid; it requires the root syntax pool to remain 444 and every
cross-dependent DAG to propagate reason two. These are evaluator fixtures,
not corpus rows.

The chamber-mask fixtures are `CONST(0) -> 00ffffff`,
`OPAQUE -> 00000000`, and
`select_parity(kappa,CONST(0),OPAQUE) -> 001c71c7`. Swapping its arms gives
`00e38e38`. These exact words check the chamber index, mask-bit direction,
and eight-digit serialization. The two real zero-gap fixtures in Section 4
check that thirty reason-1 entries clear the corresponding
`ROOT_VALID_MASK` bits without clearing their fixed `ROOT_ATTEMPT_MASK` bits.

The tuple operation enums are literal arrays:

```text
UNARY[0..3) =
  0 ABS, 1 BITLENGTH, 2 V2_NONZERO

BINARY[0..9) =
  0 ADD, 1 ABSDIFF, 2 MIN, 3 MAX, 4 GCD_ABS,
  5 PRODUCT, 6 FLOOR_DIV, 7 EUCLIDEAN_REM, 8 CENTERED_REM

ADAPTIVE[0..5) =
  0 SELECT_KAPPA, 1 SELECT_DELTA, 2 SELECT_KAPPA_XOR_DELTA,
  3 SELECT_SIGN, 4 SELECT_LT
```

Only binary operation IDs `0,1,2,3,4,5` are commutative. Sort their two
operand syntax byte strings before serialization. No other operand list is
sorted. In particular, cross roots and adaptive arms remain oriented.

Canonical syntax is an ASCII-only subset of UTF-8. Decimal integers have no
sign and no leading zero, except the single byte `0`. There is no whitespace,
newline, BOM, NUL, escape, Unicode normalization, or locale-dependent text.
Recursively serialize one syntax with this grammar:

```text
ordinary root:  r(<tail_id>,<root_kind_id>,<parameter>)
cross root:     x(<cross_pair_id>,<depth>)
unary tuple:    u(<op_id>,<child>)
binary tuple:   b(<op_id>,<left>,<right>)
adaptive 0..2: a(<op_id>,<x>,<y>)
adaptive 3:    a(3,<guard>,<x>,<y>)
adaptive 4:    a(4,<g>,<h>,<x>,<y>)
```

The punctuation shown is literal. The canonical byte string recursively
expands child syntax. It does not contain a syntax ID, branch `a`, value,
validity bit, control mask, cohort field, or label. Compare canonical strings
by unsigned bytewise lexicographic order; if one is a byte prefix, the shorter
one comes first. Equal strings are duplicate syntax. A syntax DAG's
`node_count` is the number of distinct recursively referenced nodes, including
its top node. Its `typed_layer` is zero for a root and `1,2,3` for a top
unary, binary, or adaptive node.

`syntax_id` is never a construction-order ID. After all 5,564 grammar
attempts finish, collect every retained canonical syntax byte string, sort the
complete set by the unsigned byte order above, and assign consecutive
zero-based `syntax_id` values in that final order. Rejected attempts have no
`syntax_id`. During construction, operands and duplicate checks use canonical
bytes only. The separate immutable `grammar_attempt_id` is

```text
root:      root_attempt_id                         0..443
unary:    444+j,       0<=j<1024                 444..1467
binary:   1468+j,      0<=j<3072                1468..4539
adaptive: 4540+j,      0<=j<1024                4540..5563.
```

All outputs and witness orderings that name `syntax_id` use only the final
byte-sorted ID. Where an alias must choose a representative before final IDs
exist, it chooses the least canonical syntax byte string; after assignment
this is exactly the least final `syntax_id`. Construction order can never
break a tie.

### Row-level public alias and control firewall

Formal provenance is necessary but not sufficient. The exact non-Fermat
witness

```text
N=10541=83*127, n=14, t=2, m=4, u=r=c=3, K=2633, delta=1
```

has equal public tail states despite distinct formal role IDs. In both
candidate branches, `PC:R` equals `OC:C`: for `a=0` both are `(2630,3)`,
and for `a=1` both are `(2630,7)`. Their first strict quotients are therefore
equal. A formal-only rule would permit `floor_div(x,x)=1`.

To close this hole, `analyze_public` performs these steps before it evaluates
one tuple on every row and branch. At each step it preserves the invalid
reason precedence fixed above:

1. record `ZERO_GAP` tails without a numeric serialization; serialize each
   numeric `TAIL_STATE` as its complete ordered pair plus the exact bounded
   lookahead trace;
2. canonicalize equal numeric tail serializations to the smallest role ID;
3. evaluate scoreable roots, reject a root whose value is an actual public
   control or its negative, and canonicalize all remaining equal signed
   integer values to the least canonical syntax bytes, equivalently the
   smallest final syntax ID;
4. for every tuple, first reject the row when two chosen scalar operands use
   different formal tail IDs with the same actual tail-alias ID, then reject
   it when two remaining operands have equal actual signed values;
5. evaluate the surviving tuple with exact integer semantics; and
6. reject the tuple on that row when its result equals any actual public
   control value in the row's control set, or its negative.

After each generated layer, assign equal surviving tuple results the least
final syntax ID in that layer as their diagnostic value-alias ID. A later
fixed DAG keeps its originally frozen operand syntax IDs; evaluation never
redirects an operand, rebuilds a role array, or changes a syntax. It compares
the diagnostic alias IDs and exact signed values and rejects aliases under the
enum above. The equality check is exact signed `cpp_int` equality and runs
independently in both candidate branches.

The actual `ROW_CONTROL` set contains `0,1,m,r,c,S`, all four `R_x,C_y`, all
four raw corners, all six raw gaps, all `J_a-2K_a` values, and the registered
first-Fermat controls. It contains no resultant coefficient, resultant
evaluation, or discriminant. It is constructed from `(N,t,u)` only.

This firewall uses no factor, target label, cohort name, training score, or
held-out result. It therefore does not leak a label into selection.

Discovery first runs a public-only validity pass over every retained root and
tuple on every discovery row, before attaching labels. If a syntax has an
alias/equal-operand event or a control-valued result on either branch of any
discovery row, mark it `DISCOVERY_PUBLIC_COLLISION` and remove it from both
selector ranking and direct-family eligibility for the complete phase. It is
not scored on its collision-free subset. Require at least 192 surviving
selector rules and at least 64 surviving members of the fixed direct bank or
abort the run before reading discovery labels.

Heldout repeats the public-only pass after authenticating the selection bytes
and constructing heldout public inputs, but before reading their labels. It
does not remove, replace, or rerank a selected rule. Any selected syntax with
one heldout alias/equality/control event gets `heldout_total_valid=false` and
is ineligible for every positive selector or direct-ticket verdict. Invalid
rows count as errors after labels attach. Thus public validity can select a
discovery grammar, but it cannot create heldout abstention or label leakage.
Alias IDs and control-equality masks are serialized in row aggregates so an
audit can replay them.

For each primary stage row, serialize both 56-byte `ROOT_VALID_MASK` values,
the SHA-256 of each branch's 222-byte packed `ROOT_REASON` array, and each
branch's ten-bin reason histogram. The packed arrays are transient and can be
replayed from the public row; they are not expanded into TSV hex. Every
selected expression record has its two-byte `BRANCH_VALID_MASK` field and
four-digit `INVALID_REASON_MASK`. Aggregates preserve exact reason counts for
every rule. Mask padding, reason-array digests, and partition sums are fatal
schema assertions. This keeps the complete public-control/alias row below its
registered 1,024-byte maximum.

### Frozen bounded typed tuple generator

There is no Cartesian enumeration. The source defines literal fixed-size
role arrays and uses this exact tuple source:

```text
SEED = 0xF269ADAE0C1D5EED
ROOT_CAP      = 444
UNARY_TUPLES   = 1024
BINARY_TUPLES  = 3072
ADAPTIVE_TUPLES= 1024
FINAL_CAP      = 5564 including scoreable roots
```

The root bound is exact: 14 tail roles times 30 possible strict-prefix
extractions, plus eight cross-tail pairs times three depths. Invalid or
duplicate roots reduce this count; they never cause replacement.

The layer IDs and literal serial ranges are

```text
layer 1 UNARY:   j in [0,1024)
layer 2 BINARY:  j in [0,3072)
layer 3 ADAPTIVE:j in [0,1024).
```

For each such `(layer,j)`, define

```text
SplitMix64(x):
  z=x+0x9E3779B97F4A7C15
  z=(z xor (z>>30))*0xBF58476D1CE4E5B9
  z=(z xor (z>>27))*0x94D049BB133111EB
  return z xor (z>>31)
w_0=SplitMix64(SEED xor (layer<<56) xor j)
w_(k+1)=SplitMix64(w_k+k), k=0,1,2,... .
```

Unsigned arithmetic is modulo `2^64`. `w_0` chooses the operation by
reduction modulo that layer's literal operation-array length. Subsequent
words choose typed operand role IDs. Consume the words in this exact order:

```text
unary:       w_0 op, w_1 child
binary:      w_0 op, w_1 left, w_2 right
adaptive 0-2:w_0 op, w_1 x, w_2 y
adaptive 3:  w_0 op, w_1 guard, w_2 x, w_3 y
adaptive 4:  w_0 op, w_1 g, w_2 h, w_3 x, w_4 y.
```

Unary tuples draw from retained roots.
Binary tuples draw from retained roots and unary tuples. Adaptive tuples draw
from every earlier retained layer. Reduction is modulo the current canonical
role-array size. Each role array is sorted by canonical syntax bytes before
the first serial in its layer and is then immutable for that layer. An empty
array aborts the grammar self-test. A tuple is constructed once, type-checked
once, canonicalized once, and either retained or rejected. There is no retry
for a rejected tuple. Commutative operand roles are sorted. Duplicate
canonical syntax is skipped. This makes construction work exactly 5,120
attempted tuples, independent of the number of roots.

The typed semantics corresponding to the enum arrays are:

```text
unary(scoreable): abs, bitlength, v2_nonzero
binary(scoreable,scoreable): add, absdiff, min, max, gcd_abs,
                             product, floor_div, euclidean_rem,
                             centered_rem
adaptive public guard plus scoreable arms:
  select_parity(kappa,x,y)
  select_parity(delta,x,y)
  select_parity(kappa xor delta,x,y)
  select_sign(g,x,y) where g is scoreable
  select_lt(g,h,x,y) where g,h are scoreable
```

`select_parity` chooses `x` on zero and `y` on one. `select_sign` chooses
`x` for a negative guard and `y` otherwise. `select_lt` chooses `x` for
`g<h` and `y` otherwise. `add(x,y)=x+y`,
`absdiff(x,y)=abs_cpp(x-y)`, and `min/max` use the ordinary signed integer
order. `product(x,y)=x*y`. Product and every other result use the common
value-bit cap. Guards do not become output values. A control-only value other
than the three displayed public bits cannot be a guard.

Run the exact affine-equivalence filter after every tuple. No square root
occurs in the grammar; square root is used only by the public first-Fermat
control. No row-value, label, child-factor, or oracle fingerprint affects
tuple construction or deduplication.

The preflight must time grammar construction separately from evaluation. It
must report the 444 retained root attempts, 5,120 attempted tuples, retained
tuples, type rejects, provenance rejects, duplicate rejects,
all-chamber-control rejects, final syntax count, construction wall time, and
grammar bytes. The displayed disjoint partition identities are assertions.
The production projection includes this measured construction cost without
dividing it by the worker count.

Each scalar expression gives two oriented selector rules:

```text
ARGMIN: choose a with smaller E_a; ties choose 0
ARGMAX: choose a with larger E_a; ties choose 1
```

The orientations are separate rule records and separate ranking entries.
With at most 5,564 retained expressions, discovery therefore has at most
`2*5564=11128` selector-rule aggregates. It never serializes one row per
expression while silently combining the two orientations.

These rules predict the factor-lift branch `a`. The program reports both `a`
and `e=a xor kappa`. Accuracy is checked independently against both hidden
labels and must agree under this conversion. Any mismatch aborts.

For discovery, a syntax surviving the public collision pass receives a
prediction on a row only when both candidate evaluations and its selected
comparison are valid. Any other invalidity is always counted as one prediction
error; it is never dropped or treated as abstention. Discovery rank fields
include `invalid_rows` before accuracy.

For heldout, every selected rule must be valid on both candidates for every
retained heldout row. One invalid row sets `total_valid=false`, counts as one
error, and makes both `FINITE_EXACT_SELECTOR_CANDIDATE` and
`CORRELATION_LEAD` false. This applies equally to alias, equal operands,
control equality, missing depth, zero denominator, value cap, and control-case
invalidity. A selected direct family with `total_valid=false` also cannot be a
direct-ticket lead, although all its attempted-ticket partitions are still
reported.

For every eligible expression, form the prospective public tickets

```text
E_0, E_1, E_0-E_1, E_0+E_1
```

Ticket IDs `0,1,2,3` are in that displayed order. Ticket zero requires branch
mask bit zero, ticket one requires bit one, and tickets two and three require
mask `03`. A missing required branch puts the attempt in `invalid value` with
the smallest required-branch reason; it does not substitute zero or skip the
attempt.

First apply the same exact branch-paired affine rewrite and control-equivalence
filter to each ticket. A ticket reducing to a control-only value is recorded
as `CONTROL_REINTRODUCTION` and is never gcd-tested or ranked. Test every
surviving ticket by `gcd(abs(ticket),N)`. A proper gcd is checked by exact
division and stored as a direct certificate. `0`, `1`, and `N` are not proper
hits. A direct hit solves its displayed input but is not called a next-bit
prediction.

The direct-ticket population is reduced before any corpus or label exists.
Require at least 1,024 retained scoreable syntaxes after grammar construction.
Put

```text
DIRECT_SEED=0xF269D1AEC7C0FFEE
syntax_hash=64-bit FNV-1a of the canonical UTF-8 syntax bytes
direct_key=(SplitMix64(DIRECT_SEED xor syntax_hash),canonical_syntax).
```

FNV-1a starts at offset basis `14695981039346656037`. For each unsigned
syntax byte `b`, in byte order, update

```text
h=(h xor b)*1099511628211 mod 2^64.
```

The final `h` is `syntax_hash`. Compare the second component of `direct_key`
by the unsigned byte order defined above.

Select the first exactly 1,024 syntaxes by `direct_key`. Only these form the
discovery direct-ticket bank. This reduces its exact maximum from
239,296,512 to

```text
1024 syntaxes * 10752 rows * 4 tickets = 44,040,192 tickets.
```

The choice is factor-free, label-free, and value-free. It cannot change after
the corpus opens. Heldout tests only the 64 direct families authenticated in
the selection packet, for exactly at most

```text
64 * 30720 * 4 = 7,864,320 tickets.
```

Every attempted ticket contributes to exact counters: syntactic control,
row-control equality, invalid value, gcd unit, gcd full, or gcd proper. The
partition sum must equal the attempt count. Rank direct families from these
complete aggregates. Certificate retention never changes a counter or rank.

## 6. No child-factor lane in D02

F269-D02 does not factor `K_a`, `J_a`, or any quotient corner. It invokes no
recursive factoring routine.

At late stages these children have fixed-ratio size. P183 can account for
such side calls only inside an independently correct all-input recursive
dispatcher. F269 does not have that dispatcher. Complete child-factor
features would therefore be oracle diagnostics, not operational features.

D02 omits them completely. The earlier provisional estimate of about
200,000 child factorizations is withdrawn. The exact D02 child-factor count
is zero.

A later version may add an `ORACLE_DIAGNOSTIC` stream only after a separate
resource audit. Such a stream cannot affect syntax, canonicalization,
selection, held-out lead status, or any claimed algorithm unless a correct
all-input dispatcher and its P183 recurrence are supplied first.

## 7. Deterministic cohorts

The source seed is

```text
CORPUS_SEED = 0xF269C0A07E5EED01.
```

Use the literal `SplitMix64` function in Section 5. For a candidate word,
map to an odd interval `[L,U]` by

```text
odd_count = floor((U-first_odd(L))/2)+1
x = first_odd(L)+2*(word mod odd_count).
```

Every candidate stream is indexed by the exact tuple

```text
(phase, factor_bits, shape, row_serial, pair_attempt,
 role, candidate_attempt).
```

Encode the seven nonnegative fields as 64-bit words and fold them from left
to right with `h=SplitMix64(h xor SplitMix64(field))`, starting at
`CORPUS_SEED`. The result is the candidate word. The phase IDs are discovery
zero, heldout one, consecutive control two. Shape IDs are random zero,
close-hard one, edge two, safe-safe three. Role IDs are p zero, q one,
safe-pool two, safe-pair three. No mutable PRNG state exists.

For ordinary rows, `row_serial` is the requested row, `pair_attempt` is the
current pair retry, and `candidate_attempt` advances within the p or q prime
request. For a safe pool, `row_serial` is the requested pool index,
`pair_attempt=0`, and `candidate_attempt` advances until that pool entry is
filled; duplicates advance it. For safe pairing, `row_serial` is the primary
row serial, `pair_attempt` is the pair retry, and candidate attempts zero and
one produce the two pool indices modulo pool size. These conventions consume
every field exactly once.

Cells are generated in phase order, ascending factor bits, shape ID order,
then ascending row serial. All factors have the declared exact bit length.
Every primary row also requires

```text
p<q<2*p,
bitlength(p*q)=2*factor_bits,
and not FIRST_FERMAT_CONTROL.
```

The public first-Fermat exclusion is part of the primary cohort definition.
It does not use a target label. Every excluded row increments an exact cell
counter. No modulus repeats across either primary split. A duplicate advances
the same row's pair-attempt stream.

Discovery cells are:

```text
factor bits: 16,20,24,28,32,36,40
per size and shape: 32
```

Held-out cells are:

```text
factor bits: 44,48,52,56,60
per size and shape: 64
```

The exact shape constructors are:

1. `random`: request `p,q` independently from the complete exact-bit odd
   interval.
2. `close_hard`: request `p` from the complete exact-bit interval, then `q`
   from `[p+2,floor(33*p/32)]` intersected with that interval.
3. `edge`: request `p` from
   `[2^(f-1),floor((2^f-1)*32/63)]`, then `q` from
   `[ceil(63*p/32),min(2^f-1,2*p-1)]`.
4. `safe_safe`: first construct a cell pool of
   `2*cell_count+32` distinct exact-bit safe primes `z=2s+1`, where `s` is
   prime. Candidate `s` uses the complete exact-`(f-1)`-bit odd interval and
   must give exact-`f`-bit `z`. Here `cell_tag` is the fold of
   `(phase,f,shape)` by the corpus field-fold rule above. Rank the completed
   pool by `(SplitMix64(cell_tag xor z),z)`. Pair indices from the safe-pair
   stream, require distinct values, then order them as `p<q`.

Primality uses trial division by the first twelve primes followed by the
deterministic 64-bit Miller--Rabin bases

```text
2,325,9375,28178,450775,9780504,1795265022.
```

One ordinary prime request tests at most `65,536` candidate words. One row
tests at most `256` pair attempts. One safe-prime pool tests at most
`4,000,000` exact `(s,2s+1)` candidates, and safe pairing tests at most
`200,000` index pairs per cell. Every cap is inclusive of rejected primes,
wrong products, first-Fermat controls, and duplicates at its applicable
level. Cap exhaustion aborts the complete run with the exact cell and
counter. It never shrinks, replaces, or refills a cell from another shape.

These rules give exactly 896 discovery and 1,280 held-out primary moduli or
abort. Because every retained product has `2f` bits, the registered stage
schedule gives exactly

```text
discovery: 10,752 stage rows;
heldout:   30,720 stage rows;
total:     41,472 stage rows.
```

Consecutive-prime inputs are a separate control stream because F267 proves
that the relevant shifted-boundary cohort is dominated by public Fermat
behavior. For each `8<=f<=22`, enumerate odd `p` upward from `2^(f-1)+1`,
retain prime `p`, take the next prime `q`, and write the pair when both are
exact `f` bits and balanced. Retain pairs in ascending `p` order and stop at
the first of 64 retained pairs or
`p>min(2^f-1,2^(f-1)+2^20)`. Thus this stream contains at most
`15*64=960` control pairs. Record a shortfall and do not refill it.
Classify the first-Fermat event but do not exclude it. This control stream
never enters grammar construction, ranking, selection, or verdicts.

Factor-bit ranges make primary discovery and heldout disjoint. The program
emits exact generation counters, cell hashes, class counts, first-Fermat
exclusions, duplicate counts, and stage counts before scoring.

## 8. Discovery selection and held-out firewall

Discovery evaluates every eligible expression and both orientations. Set
`orientation_id=0` for `ARGMIN` and `orientation_id=1` for `ARGMAX`. Rank
rules by this total order:

1. invalid discovery rows, ascending;
2. minimum balanced accuracy across the four shapes, descending;
3. number of exact size/shape cells, descending;
4. total balanced accuracy by exact cross-products, descending;
5. total errors, ascending;
6. typed layer, then node count, each ascending;
7. canonical UTF-8 syntax bytes, ascending; and
8. orientation ID, ascending.

For item 2, pool all seven discovery factor sizes within each shape, compute
the shape balanced accuracy from the pooled exact counts, then take the
minimum over four shapes. For item 3, an exact cell is one of the 28
factor-size/shape cells with zero invalid rows and zero prediction errors.
For item 4, pool all 28 cells and compute balanced accuracy from the pooled
exact counts. Item 5 counts invalid predictions as errors. Duplicate syntax
bytes were removed, and the orientation IDs differ, so the last two items
break every remaining tie.

All accuracy arithmetic is rational. For one cell, let `n0,n1` be the total
retained row counts with labels zero and one, including invalid rows. Let
`c0,c1` count correct valid predictions. Require `n0>0` and `n1>0`; otherwise
the complete run aborts because the frozen cohort failed to contain both
classes. Define

```text
balanced_accuracy = (c0*n1+c1*n0)/(2*n0*n1).
```

Compare two accuracies only by exact integer cross-products. Do not convert
to floating point for selection or gates. Invalid rows contribute to `n0` or
`n1` and not to `c0,c1`.

The mandatory public baseline bank predicts the factor-lift bit `a` from:

```text
factor-label constants:       a=0, a=1;
reciprocal constants mapped:  a=kappa, a=1 xor kappa;
product-parity orientations:  a=delta, a=1 xor delta;
mixed orientations:           a=kappa xor delta,
                              a=1 xor kappa xor delta;
both orientations of bit_N(t), bit_N(t+1), bit_u(t-1), parity(t);
the complete mapped F210 one-step bank below.
```

For a nonnegative integer `x`, define `bit_x(j)=(x>>j)&1` for zero-based
little-endian bit index `j>=0`; a position above `bitlength(x)-1` is zero.
No negative value appears in these public bit baselines.

For candidate factor branch `a`, map the F210 reciprocal branch index by

```text
j_a = a xor kappa.
```

Let

```text
FK_a=K_(j_a)=Z_(a,b_a)/2,
FJ_a=H_(j_a)=Z_(a,1-b_a),
FX_a=R_a, FY_a=C_(b_a).
```

Here `H_(j_a)` names F210-D01's crossed quotient only inside this baseline
definition; F269 uses `J_a` elsewhere. The division by two is exact. The
complete operational mapped F210 baseline scalar list is

```text
FK_a, FJ_a, bitlength(FK_a), bitlength(FJ_a),
FK_a+FJ_a, min(FK_a,FJ_a), max(FK_a,FJ_a),
FK_a*FJ_a, gcd(FK_a,FJ_a),
larger(FK_a,FJ_a) div smaller(FK_a,FJ_a),
larger(FK_a,FJ_a) mod smaller(FK_a,FJ_a),
abs(FX_a-FY_a), FX_a+FY_a.
```

For each of these thirteen scalars, include `ARGMIN` and `ARGMAX` with the
same tie rules as selectors. These 26 rules are the complete factor-free
F210 baseline bank registered here. F210's child-factorization and modular
action features are excluded by Section 6, not silently approximated. The
baseline scalars remain control-only even when one equals a raw coordinate or
gap.

Together with the sixteen bit rules above, this is exactly 42 baseline
records. Their IDs and definition-file bytes are frozen here. The file
`F269-D02.baselines.tsv` is ASCII with LF line endings, no BOM, no quoting,
no trailing spaces, and one final LF. Its exact complete content is the text
inside this block, excluding the fences:

```text
baseline_id	baseline_key	class	feature_id	orientation_id	prediction_a
0	CONST_0	BIT	CONST_0	NA	0
1	CONST_1	BIT	CONST_1	NA	1
2	KAPPA	BIT	KAPPA	NA	kappa
3	NOT_KAPPA	BIT	KAPPA	NA	1_xor_kappa
4	DELTA	BIT	DELTA	NA	delta
5	NOT_DELTA	BIT	DELTA	NA	1_xor_delta
6	KAPPA_XOR_DELTA	BIT	KAPPA_XOR_DELTA	NA	kappa_xor_delta
7	NOT_KAPPA_XOR_DELTA	BIT	KAPPA_XOR_DELTA	NA	1_xor_kappa_xor_delta
8	BIT_N_T	BIT	BIT_N_T	NA	bit_N(t)
9	NOT_BIT_N_T	BIT	BIT_N_T	NA	1_xor_bit_N(t)
10	BIT_N_T1	BIT	BIT_N_T1	NA	bit_N(t+1)
11	NOT_BIT_N_T1	BIT	BIT_N_T1	NA	1_xor_bit_N(t+1)
12	BIT_U_TM1	BIT	BIT_U_TM1	NA	bit_u(t-1)
13	NOT_BIT_U_TM1	BIT	BIT_U_TM1	NA	1_xor_bit_u(t-1)
14	PARITY_T	BIT	PARITY_T	NA	t_mod_2
15	NOT_PARITY_T	BIT	PARITY_T	NA	1_xor_t_mod_2
16	F210_FK_ARGMIN	F210	FK	0	ARGMIN
17	F210_FK_ARGMAX	F210	FK	1	ARGMAX
18	F210_FJ_ARGMIN	F210	FJ	0	ARGMIN
19	F210_FJ_ARGMAX	F210	FJ	1	ARGMAX
20	F210_BITLEN_FK_ARGMIN	F210	BITLEN_FK	0	ARGMIN
21	F210_BITLEN_FK_ARGMAX	F210	BITLEN_FK	1	ARGMAX
22	F210_BITLEN_FJ_ARGMIN	F210	BITLEN_FJ	0	ARGMIN
23	F210_BITLEN_FJ_ARGMAX	F210	BITLEN_FJ	1	ARGMAX
24	F210_SUM_FK_FJ_ARGMIN	F210	SUM_FK_FJ	0	ARGMIN
25	F210_SUM_FK_FJ_ARGMAX	F210	SUM_FK_FJ	1	ARGMAX
26	F210_MIN_FK_FJ_ARGMIN	F210	MIN_FK_FJ	0	ARGMIN
27	F210_MIN_FK_FJ_ARGMAX	F210	MIN_FK_FJ	1	ARGMAX
28	F210_MAX_FK_FJ_ARGMIN	F210	MAX_FK_FJ	0	ARGMIN
29	F210_MAX_FK_FJ_ARGMAX	F210	MAX_FK_FJ	1	ARGMAX
30	F210_PRODUCT_FK_FJ_ARGMIN	F210	PRODUCT_FK_FJ	0	ARGMIN
31	F210_PRODUCT_FK_FJ_ARGMAX	F210	PRODUCT_FK_FJ	1	ARGMAX
32	F210_GCD_FK_FJ_ARGMIN	F210	GCD_FK_FJ	0	ARGMIN
33	F210_GCD_FK_FJ_ARGMAX	F210	GCD_FK_FJ	1	ARGMAX
34	F210_DIV_LARGE_SMALL_ARGMIN	F210	DIV_LARGE_SMALL	0	ARGMIN
35	F210_DIV_LARGE_SMALL_ARGMAX	F210	DIV_LARGE_SMALL	1	ARGMAX
36	F210_REM_LARGE_SMALL_ARGMIN	F210	REM_LARGE_SMALL	0	ARGMIN
37	F210_REM_LARGE_SMALL_ARGMAX	F210	REM_LARGE_SMALL	1	ARGMAX
38	F210_ABSDIFF_FX_FY_ARGMIN	F210	ABSDIFF_FX_FY	0	ARGMIN
39	F210_ABSDIFF_FX_FY_ARGMAX	F210	ABSDIFF_FX_FY	1	ARGMAX
40	F210_SUM_FX_FY_ARGMIN	F210	SUM_FX_FY	0	ARGMIN
41	F210_SUM_FX_FY_ARGMAX	F210	SUM_FX_FY	1	ARGMAX
```

This file has exactly one header, 42 data records, 2,014 bytes, and SHA-256
`ee5af083ba43236b92a4c52996e4134f7f40f10cb7db9997212c821482f097b4`.
The source embeds these bytes as one literal and verifies this digest against
the frozen manifest before corpus generation. Baseline aggregate rows are
separate. Their exact
TSV header is

```text
baseline_id	phase	factor_bits	shape_id	rows	n0	n1	valid_rows	invalid_rows	c0	c1	errors	balanced_accuracy_num	balanced_accuracy_den
```

They are sorted by `(baseline_id,phase,factor_bits,shape_id)`. The `phase`
field is the one byte `0` for discovery and `1` for heldout. Shape IDs are
the decimal bytes `0`,`1`,`2`,`3` in the cohort order from Section 7. All
integers use decimal without leading zeros. A baseline always predicts, so
`valid_rows=rows` and
`invalid_rows=0`; these equalities are checked. Fractions are reduced with a
positive denominator. This schema is written to
`F269-D02.baseline_aggregates.tsv`; baseline records never share the selector
syntax-ID namespace.

Every baseline has type `BASELINE_ONLY`. It cannot enter the tuple grammar,
selection population, adaptive guards, or direct tickets.

The `a=kappa` pair is exactly the reciprocal constant pair converted back to
factor-branch labels. It prevents a `kappa=1` cohort from making label
convention look like prediction. Report every baseline in both `a` and
`e=a xor kappa` coordinates. The two accuracy tables must agree after the
exact conversion.

Select the first 192 selector rules. Serialize complete partitions for all
1,024 direct-bank expression families. Exclude the families marked
`DISCOVERY_PUBLIC_COLLISION` from selection as required in Section 5, then
rank every eligible survivor by this exact total-order key:

```text
1 hit_moduli,          descending
2 hit_factor_sizes,    descending
3 hit_shapes,          descending
4 proper_ticket_count, descending
5 invalid_ticket_count,ascending
6 typed_layer,         ascending
7 node_count,          ascending
8 canonical UTF-8 syntax bytes, ascending.
```

`hit_moduli` is the number of distinct discovery integers `N` for which at
least one retained stage and ticket ID gives a certified proper gcd.
`hit_factor_sizes` is the number of the seven registered discovery factor
sizes containing such a modulus. `hit_shapes` is the number of the four
registered shapes containing such a modulus. `proper_ticket_count` counts
all attempted `(N,t,ticket_id)` entries in the `gcd proper` partition; it
does not deduplicate equal factors. `invalid_ticket_count` is the sum of the
`syntactic control`, `row-control equality`, and `invalid value` partitions.
`typed_layer` and `node_count` have the canonical syntax definitions in
Section 5. Duplicate syntax bytes were already removed, so item 8 breaks
every remaining tie. No implementation order or map iteration order can
break a tie.

Select the first 64 direct families under this order. A syntax can occur in
both lists. The canonical selection file therefore contains exactly 192
selector rows and 64 direct rows, with complete rank fields and syntax DAGs.

Close the file, hash its exact bytes, and pass that digest as a held-out
command argument. Heldout reads those bytes once, verifies the digest,
reconstructs every DAG, verifies the discovery corpus digest named in the
packet, and generates heldout inputs only afterward.

No unselected expression is evaluated on heldout labels or heldout direct
tickets. Heldout still runs all fixed algebra controls, so a source failure
cannot hide behind selection.

## 9. Finite verdicts

A selected rule is `FINITE_EXACT_SELECTOR_CANDIDATE` only when it has zero
errors and `total_valid=true` on every retained held-out size, shape, and
stage after first-Fermat modulus exclusions.

A selected rule is `CORRELATION_LEAD` only when all of these hold:

1. held-out balanced accuracy is at least `0.60` in every shape;
2. it is at least `0.60` separately at factor sizes 52, 56, and 60;
3. it improves the complete constant, `kappa`, `delta`,
   `kappa xor delta`, `N`-bit, `u`-bit, and F210 one-step Euclidean baseline
   bank in every shape; and
4. its worst cell does not decline from sizes 52 through 60.

For item 4, at each factor size take the minimum rational balanced accuracy
over the four shapes. Require the size-56 minimum to be at least the size-52
minimum and the size-60 minimum to be at least the size-56 minimum. All
comparisons use exact cross-products. Also require `total_valid=true`.

For item 3, pool the five heldout sizes within one shape, recompute rational
balanced accuracy from pooled `c0,c1,n0,n1`, and require the candidate to be
strictly greater than every individual baseline's pooled accuracy in each of
the four shapes. A tie is not improvement. Every baseline cell must contain
both labels under the same nonempty-class abort rule.

Otherwise it is a finite null or weak result under frozen thresholds.

A direct-ticket family is a finite lead only if it produces proper certified
gcds in at least 16 held-out moduli, across at least three sizes and three
shapes, including size 56 or 60. Each certificate must replay from public
`(N,t,u,syntax)` alone.

No finite verdict proves universality, inverse-QP density, or an all-input
factoring algorithm.

## 10. Outputs

The proposed uncompressed semantic outputs are:

```text
F269-D02.discovery.corpus.tsv
F269-D02.discovery.control_alias.tsv
F269-D02.discovery.selector_rules.tsv
F269-D02.discovery.direct_families.tsv
F269-D02.discovery.certificates.jsonl
F269-D02.selection.tsv
F269-D02.heldout.corpus.tsv
F269-D02.heldout.control_alias.tsv
F269-D02.heldout.rules.tsv
F269-D02.heldout.certificates.jsonl
F269-D02.heldout.counterexamples.tsv
F269-D02.heldout.lead_gate.tsv
F269-D02.baselines.tsv
F269-D02.baseline_aggregates.tsv
F269-D02.controls.tsv
F269-D02.manifest.tsv
```

D02 separates the D01 mixed physical files only to make resource accounting
reconstructible. Each primary stage still has the same public fields. Its
core, root-mask, and reason fields are in the phase corpus file. Tail-alias
and value-alias fields are in the phase control-alias file under the same
public key `(phase,factor_bits,shape_id,row_serial,N,t)`. Discovery selector and direct
records likewise keep their D01 schemas and order, but use two files. This
split does not change one grammar, row, aggregate, rank, selection, or verdict.

Do not emit an expression-by-row dense trace. Preserve every selected-rule
error and every direct-ticket test in exact aggregates. Certificate and
counterexample examples use this bounded policy, which never changes an
aggregate, score, rank, selection, or verdict:

- for each of the 1,024 discovery direct families, retain the four smallest
  proper certificates;
- for each of the 64 selected heldout direct families, retain the sixteen
  smallest proper certificates; and
- for each of the 192 selected selector rules and each of the twenty heldout
  size/shape cells, retain the smallest invalid-or-wrong row.

Certificate order is the exact tuple

```text
(N,t,ticket_id,syntax_id,abs(ticket),proper_factor).
```

Counterexample order is
`(N,t,syntax_id,orientation_id,reason_id,prediction_a,target_a)`. The orientation
field is mandatory because `ARGMIN` and `ARGMAX` are separate rules with the
same syntax ID. Worker heaps keep the local smallest records and merge by the
same order. Retention does not stop after a cap; later tests still update
complete aggregates.

Here `reason_id` is the decimal runtime enum ID. For ordering only, prediction
codes are `0<1<2`, where code two is absent; serialization writes that code as
the literal `NA` and never writes `2`. Target is always one byte `0` or `1`.
The file `F269-D02.heldout.counterexamples.tsv` has exactly this header:

```text
N	t	syntax_id	orientation_id	reason_id	prediction_a	prediction_e	target_a	target_e
```

Every numeric field is unsigned decimal without a leading zero except zero
itself. Invalid predictions put `NA` in both prediction fields. Valid
predictions put one bit in each and must satisfy
`prediction_e=prediction_a xor kappa`; target fields obey the analogous
identity. Rows use LF and no quoting, escaping, empty field, or trailing tab.

Each output record has a checked maximum serialized byte length. Syntax DAGs
are written once in rule or selection rows; witness rows reference syntax IDs
and never repeat a DAG. The exact uncompressed component bound is:

```text
primary corpus:                  41472 * 2048 =  84,934,656 bytes
control and alias rows:           42432 * 1024 =  43,450,368 bytes
discovery selector-rule rows:     11128 * 8192 =  91,160,576 bytes
discovery direct-family rows:      1024 * 8192 =   8,388,608 bytes
heldout selector/direct rows:        256 * 8192 =   2,097,152 bytes
selection rows:                      256 * 8192 =   2,097,152 bytes
baseline definitions:                  1 * 8192 =       8,192 bytes
baseline aggregates:                2016 * 1024 =   2,064,384 bytes
certificate witnesses:             5120 * 2048 =  10,485,760 bytes
counterexample witnesses:          3840 * 2048 =   7,864,320 bytes
lead-gate rows:                      256 * 1024 =     262,144 bytes
manifests and sidecars:                            8,388,608 bytes
stdout and stderr logs:                           16,777,216 bytes
total registered bound:                          277,979,136 bytes.
```

The 11,128 discovery selector rows are the two orientations of at most 5,564
expressions. The 1,024 discovery direct-family rows hold the complete ticket
partitions for the fixed direct bank. The 256 heldout rows are 192 selected
oriented rules plus 64 selected direct families. The 256 selection rows use
the same split. The 2,016 baseline aggregate rows are exactly 42 baselines
times the 28 discovery and 20 heldout factor-size/shape cells. The single
8,192-byte definition component contains the exact 42-record file above.
Each displayed number is the cap for the complete named semantic class,
including its headers. The two corpus files share the primary-corpus cap.
The two control-alias files and consecutive-control file share the
control-and-alias cap. The two certificate files share the certificate cap.
All other TSV header bytes, the executable, the fixed ledger files, grammar
table, preflight measurements, and schema sidecars are charged to `manifests
and sidecars`. Exceeding any individual class cap is a resource failure.
The classifier matches the exact root-relative semantic paths in the table.
A same-named file in a subdirectory is a sidecar, not a semantic alias.
Log files are direct children of the fixed `logs` directory; nested log paths
are forbidden.
Only the twelve registered root-relative production `.gz.tmp` paths and the
three fixed preflight serialization/compression paths enter `TRANSIENT`.
An arbitrary `.tmp` name remains a sidecar. Registered transients have no
semantic allowance; they remain subject to the ordinary global cap. Thus they
can never consume the 8 MiB sidecar allowance or hide semantic bytes in it.

Every complete ticket partition and rule aggregate is serialized even when
its witness heap is empty. A record-size violation is a fatal schema failure,
not permission to omit evidence. Existing evidence causes refusal. The
live aggregate packet cap is exactly `536870912` bytes (512 MiB), strictly
above the registered component sum. `RLIMIT_FSIZE` is only a per-file limit;
it is not claimed to enforce this aggregate cap.

Every packet evidence or output regular file, including the executable,
logs, sidecars, fixed ledger files, serialization temporaries, and compression
temporaries, is below one dedicated evidence directory. Evidence symlinks,
hard links, sparse files, special filesystem entries, and output paths outside that directory are
forbidden. The one bootstrap compiler output and compiler log live in a fresh
private `/tmp/f269-d02-bootstrap.XXXXXX` directory. They are not evidence.
Before any validation, the frozen executable creates the ledger and imports
both bytes through the checked writer; no later raw evidence write exists.
Compiler internal temporaries remain covered by the disk, deadline, cgroup,
and process limits. The failure trap becomes active immediately after ledger
initialization and uses the bootstrap executable until the checked executable
copy is durable. The runner requires the same 5 GiB free-space floor on
`/tmp` before it creates that private directory, then removes both bootstrap
files immediately after their checked imports.

The process-shared ledger files are exactly
`.F269-D02.ledger.state` and `.F269-D02.ledger.state.lock`. They are sidecars
and count in both the sidecar and global totals. The state is 192 bytes. The
lock contains an immutable eight-byte identity word, so neither file has a
zero-byte accounting exception. The C++ writer uses the `flock(2)` system call
on the lock file; the runner does not invoke an external `flock` program.
Ledger initialization immediately acquires and releases that exact lock, so
unsupported lock semantics fail before any bootstrap import or validation.
Under that exclusive lock, every writer scans all live
regular files, compares every semantic-class count and the global count with
the fixed-size state, records an exact pending reservation, writes and closes
the bytes, rescans, and commits the reservation. Shell command stdout and
stderr go through a pipe-owning checked-exec mode. Every ordinary output and
compression mode rejects both fixed ledger paths; only the ledger protocol
writes the state, and no mode changes the lock identity. Shell-generated text
and gzip output use the same ledger. Before every extending write the ledger
reserves the exact byte increment and refuses an increment that would make
the sum exceed

```text
ORDINARY_WRITER_CAP=535822336
FAILURE_RESERVE=1048576
AGGREGATE_CAP=ORDINARY_WRITER_CAP+FAILURE_RESERVE=536870912.
```

Before a checked child can execute, it acknowledges creation of a dedicated
process group through a close-on-exec pipe. If a mid-command ledger operation
fails, the checked executor closes both capture pipes, kills that complete
process group, and waits for its leader before the shell invokes the reserved
failure writer. No capture descriptor remains live across that handoff.

Truncation and compression replacement update the same ledger. One
compression transaction reclassifies one authenticated `.gz.tmp` file from
`TRANSIENT` to the source semantic class while it removes the uncompressed
source under the same lock. Only the exact failure path
`F269-D02.failure.tsv` can consume the last `FAILURE_RESERVE` bytes. The ERR
trap records phase, exit status, source line, elapsed time, and the exact
ledger class counters. A pending ordinary reservation is reconciled from a
fresh scan before this failure-only write. No ordinary path can create or
extend the failure file.

The finalizer first closes the log class. It then predicts the exact final
hash-list length and reserves those projected counters in the fixed-size
ledger. The list authenticates every already closed regular file, the fixed
lock identity, and the exact future frozen-state bytes. The finalizer writes and syncs
`F269-D02.final.sha256`, verifies the projected scan, then atomically replaces
the reserved ledger record with those already authenticated frozen-state
bytes. A crash before that last ledger write leaves `frozen=0`; it cannot look
like a complete packet. An ordinary exception removes the hash list and rolls
the transaction back before the failure writer runs. No evidence mutation is
permitted after the frozen-state commit. The runner read-verifies the complete
hash list. The final PASS text goes only to the inherited terminal after every
evidence descriptor closes; it cannot mutate `runner.log`.

The runner independently executes GNU
`du -sb --apparent-size -- <evidence-directory>` after every registered
preflight transaction, before and after each production phase, before and
after each compression transaction, and before final closure. Every reading
is at most `536870912`. Each ledger mutation independently sums `st_size`
over every regular file and requires exact agreement with all ledger classes.
The `du` reading can be larger because it includes directory entries but can
never exceed the cap. Compression handles one artifact at a time. The
original and temporary both count globally until the checked commit. No batch
of duplicate compressed copies is permitted.

## 11. Resource envelope, hard caps, and mandatory stress preflight

The implementation target is C++17. The runner chooses `W` from
`{1,2,4,8}` after inspecting host load, logical CPUs, memory, disk, and active
processes. It writes `W` before validation. The same `W` is passed to the
stress preflight and production and cannot increase. Production uses one
process with `W` worker threads, `nice 15`, and one-thread compression after
all uncompressed semantic outputs close.

The draft workload has these exact maxima:

```text
2,176 primary moduli;
41,472 primary stage rows;
at most 5,564 retained expressions from 444 root and 5,120 tuple attempts;
at most 11,128 discovery selector orientations;
44,040,192 discovery direct tickets;
7,864,320 heldout direct tickets;
51,904,512 direct tickets in total;
192 selected heldout selector rules and 64 selected direct families;
zero child factorizations;
zero characteristic-size scans.
```

These are count bounds. They are not elapsed-time bounds.

### Enforceable process limits

Before compile, the runner starts a monotonic packet clock. A runner watchdog
kills the packet cgroup at exactly 14,400 elapsed seconds. The source receives
the same absolute deadline and stops accepting new work at 14,370 seconds so
that it has up to 30 seconds to close a failure manifest. The cgroup kill is
authoritative. An incomplete packet is a resource failure, never a shortened
cohort or partial result.

The runner must create a dedicated cgroup-v2 leaf for the complete packet,
require writable `memory.peak`, and write and read back

```text
memory.max      = 3758096384
memory.swap.max = 0
```

and place every compile, preflight, production, compression, and hashing
process in that leaf. If cgroup-v2 delegation or either limit is unavailable,
the packet fails before compile. The runner also requires `cgroup.kill` to be
present and writable and reads back its file identity with GNU `stat`. The
watchdog writes `1` to that exact file unconditionally at the hard deadline.
There is no watchdog-only fallback.

Before the packet clock, immediately before compile, and before each timed
preflight, corpus, or compression child, the runner reads one unlimited-width
`ps -ww -eo pid=,ppid=,args=` snapshot into the Bash process. It applies
the Bash lowercase operator and rejects every other process whose complete
argument string contains `f265`, regardless of D-number, executable name, or
whether it is a compiler, validator, preflight, corpus generator, or
production run. No grep/awk process carries the search word, so the overlap
probe cannot match itself.

The exact external-command inventory is

```text
awk bash date df dirname du env find g++ grep gzip mkdir mktemp nice nproc ps
rm rmdir sed sha256sum sleep sort stat timeout /usr/bin/time
```

The runner checks every command before the packet clock. It requires Bash 4
or newer, `--version` for Bash and every GNU program, `awk -W version`, and the exact help entries
for every non-POSIX option used: UTC date; portable and human-readable `df`;
byte, summary, and apparent-size `du`; `find -maxdepth/-printf`; fixed, exact,
quiet `grep`; stdout/no-name `gzip`; mode `mkdir`; directory `mktemp`;
adjusted `nice`; formatted/unlimited-width/sorted `ps`; forced `rm`; quiet `sed`;
`sha256sum --check`; `stat --format`; `timeout --kill-after`; and GNU time
`--verbose`. It passes the exact C++17, optimization, macro, thread, and output
options to the compiler's no-compile version probe, and passes the exact
no-name, level-six, stdout tuple to the gzip help probe. Every shell
command on the runner's builtin list is separately required to resolve as a
Bash builtin. It separately gates the exact `/usr/bin/env` shebang interpreter.
It fixes `LC_ALL=C` and `TMPDIR=/tmp` and removes inherited `GZIP` and
`POSIXLY_CORRECT` option injection before any tool gate. No unlisted external
command occurs. `flock` is a system call inside the frozen executable, not an
external command.

Before each executable starts, the runner also sets `RLIMIT_AS` soft and hard
to `4294967296` bytes and `RLIMIT_FSIZE` soft and hard to `536870912` bytes.
The executable calls `getrlimit` and requires these exact ceilings before it
allocates a corpus object. The shell's equivalent address-space setting is
`ulimit -v 4194304` KiB. The kernel cgroup is the resident-memory enforcement;
`RLIMIT_AS` is the independent virtual-address-space enforcement.

### Exact algebra self-tests and grammar timing

Use these literal replacement pairs:

```text
P_A=720575940379279399
Q_A=1008806316530991113
N_A=726921560194875913822899294212981087

P_B=792633534417207313
Q_B=1080863910568919077
N_B=856728981658246606409659147429610101
```

The four factors must first pass the same exact deterministic 64-bit
primality procedure. Trial-divide by the first twelve primes

```text
2,3,5,7,11,13,17,19,23,29,31,37.
```

For a survivor `z`, write `z-1=2^s*d` with `d` odd. For every base in the
literal order

```text
2,325,9375,28178,450775,9780504,1795265022
```

reduce the base modulo `z`, compute `x=base^d mod z`, and accept that base
only if `x` is one or `z-1`, or one of the next `s-1` repeated squares is
`z-1`. Reject on the first failed base. This base set is deterministic for
every unsigned integer below `2^64`; no probable-prime result is accepted.
The mandatory decompositions are

```text
P_A-1=2^1*360287970189639699
Q_A-1=2^3*126100789566373889
P_B-1=2^4*49539595901075457
Q_B-1=2^2*270215977642229769.
```

Require all four results to be prime, all four values to be pairwise
distinct, every value to have exactly 60 bits, `P_i<Q_i<2*P_i`, the two
displayed products to be exact, and both products to have exactly 120 bits.
A failed condition aborts before any public stage is constructed. Thus the
stress inputs satisfy the distinct-prime balanced-semiprime premise instead
of assuming it.

For each pair, compute

```text
t_terminal=floor((bitlength(N_i)-1)/4)=29.
```

For every `1<=t<=t_terminal`, set `m=2^t` and
`u=P_i^(-1) mod m`, then call the same `analyze_public(N_i,t,u)` entry point
used by production. It must check every Section 4 public control: prefix and
rectangle divisibilities, positivity, all corner and own-coordinate unit
gcds, the six differences, every zero-gap or quotient-one shell, all four
signed `J-2K` identities, both ordered-resultant coefficient triples and all
twelve evaluations, the discriminants, and the first-Fermat control. This
gives 58 exact public-algebra stages. The `t=29` rows are boundary self-tests
only. The production cohort schedule remains the strict range `t<29` and is
unchanged. No hidden label enters a public call.

The self-test serializes the complete returned public algebra. The literal
TSV header is one line with these 87 fields in this order:

```text
fixture	N	n	t_terminal	t	m	u	r	c	K	delta	kappa	S	R0	R1	C0	C1	Z00	Z10	Z01	Z11	gZ00N	gZ00R	gZ00C	gZ10N	gZ10R	gZ10C	gZ01N	gZ01R	gZ01C	gZ11N	gZ11R	gZ11C	G00_10	G00_01	G00_11	G10_01	G10_11	G01_11	P00_10_status	P00_10_q	P00_10_rem	P00_01_status	P00_01_q	P00_01_rem	P00_11_status	P00_11_q	P00_11_rem	P10_01_status	P10_01_q	P10_01_rem	P10_11_status	P10_11_q	P10_11_rem	P01_11_status	P01_11_q	P01_11_rem	J0_R_signed	J0_C_signed	J1_R_signed	J1_C_signed	RQ_c0	RQ_c1	RQ_c2	RP_c0	RP_c1	RP_c2	RQ_at_-2	RQ_at_-1	RQ_at_0	RQ_at_1	RQ_at_2	RQ_at_3	RP_at_-2	RP_at_-1	RP_at_0	RP_at_1	RP_at_2	RP_at_3	disc_Q	disc_P	fermat_A	fermat_D	fermat_s	fermat_square	fermat_minus	fermat_plus
```

`fixture` is the one byte `A` or `B`. All integer fields are canonical signed
decimal. Corner order is `00,10,01,11`. Pair order is
`00:10,00:01,00:11,10:01,10:11,01:11`. A zero pair writes
`ZERO_GAP,NA,NA`; every other pair writes
`QUOTIENT_ONE,<larger/smaller>,<larger mod smaller>`. Resultant coefficients
are the literal triples for `2*R_Q` and `2*R_P` in ascending degree. Their
evaluations use chart points `-2,-1,0,1,2,3`. `fermat_A` is
`ceil(sqrt(N))`, `fermat_D=fermat_A^2-N`, `fermat_s=floor(sqrt(fermat_D))`,
and `fermat_square` is zero or one. The last two fields are `NA` when it is
zero and are `fermat_A-fermat_s,fermat_A+fermat_s` when it is one. Fields use
one tab, rows use one LF, and every header and data row, including the last,
ends in LF. There is no BOM, quoting, escaping, padding, CR, or trailing tab.

Here `gZxyN=gcd(Zxy,N)`, while `gZxyR` and `gZxyC` use the own lifted
coordinates `R_x` and `C_y`. For candidate `a`, put `b=a xor delta`,
`Zcompat=Z_(a,b)`, and use the Algebra (4) meanings of `J_a` and `J_(1-a)`.
The two signed fields are exactly

```text
Ja_R_signed=J_a-Zcompat
Ja_C_signed=J_(1-a)-Zcompat.
```

No absolute value is taken in these four transcript fields. These definitions
and Algebra (15a) determine every column without an implementation choice.

Hash the header plus the 29 ascending-`t` rows for one fixture. Hash the
header plus all `A` rows followed by all `B` rows for the combined transcript.
The exact checks are:

```text
header: 87 fields, 659 bytes,
  SHA-256 29d8676fa23d0e58f38db8e7ec7ee05d273a57d1ade1259d6c59e671385daa53
A transcript: 29 rows, 33735 bytes,
  SHA-256 99f17050d302872a1612b0d480799972423643a02afa1b435de55ba21a267668
B transcript: 29 rows, 33805 bytes,
  SHA-256 8b8752e2e67827184eb07ad87950eec92a3084711e03aa09742350c13940db4f
combined transcript: 58 rows, 66881 bytes,
  SHA-256 fc7bfb1d9105d6a597d91f007ca3da18c2b1095e51ae0ff5b33408b62f655fe6
```

The byte totals include the header once in each named transcript. A value,
identity, row count, byte count, or digest mismatch aborts before grammar
timing. These algebra tests are not the throughput fixture and are not
extrapolated to production. The small alias witness
`N=10541,t=2,u=3` is also replayed as a mandatory firewall self-test.

The exact failed fifth-draft fixture is a mandatory negative regression:

```text
P_bad=1152921504606846883
Q_bad=1152921504606846943
     =17*2113*308137*104161559
N_bad=1329227995784915727635697479817628669
t=10, m=1024, u=11, r=931, c=991
K=1298074214633706765269235820133502, delta=0, kappa=0
R1=1955, gcd(R1,N_bad)=17
Z10=1298074214633706765269235820132511
Z11=1298074214633706765269235820130556
gcd(Z10,N_bad)=gcd(Z11,N_bad)=17.
```

The stress-domain validator must return `OUT_OF_DOMAIN_COMPOSITE_Q` for this
pair before accepting an algebra stage. The negative self-test separately
checks the displayed factor product and exact `t=10` arithmetic so the old
unit-gcd failure cannot disappear. It must never reclassify the row as valid.
It is not a corpus row, a grammar input, a `MAX_WORK_STAGE`, a timing
repetition, a forecast term, or an evaluation hash input. Its setup time is
charged only to the packet's residual `E_0` clock like every other exact
self-test.

Grammar construction runs seven times and records raw wall times
`G_1,...,G_7`. Define

```text
G_raw=sum_(i=1)^7 G_i
G_prod=max(G_2,...,G_7).
```

The first run is excluded only from the production projection; its raw time
still enters readiness. Each run attempts all 444 roots and exactly 5,120
tuples, applies the complete static rewrite table, canonicalizes and sorts the
UTF-8 syntax bytes, assigns final byte-order syntax IDs, and serializes the
complete grammar. Its exact attempt partition is `ROOT_RETAINED=444` plus
the tuple outcomes `TUPLE_RETAINED`, `TYPE_REJECT`, `PROVENANCE_REJECT`,
`DUPLICATE_REJECT`, and `ALL_CHAMBER_CONTROL_REJECT`. These disjoint counts
must sum to 5,564. It separately requires the tuple outcomes to sum to 5,120
and the retained count to equal the final syntax count. It reports every
partition, the fixed root-attempt mask, every retained syntax's control-case
mask, construction wall time, and grammar bytes.
The `root_attempt_mask` field is the complete 112-character lowercase hex
word from Section 5, not a digest or length. The `control_case_masks` field is
the complete comma-separated array of eight-character lowercase hex words in
final `syntax_id` order, including all 444 roots. Each repetition reports its
array length and SHA-256. The runner requires the literal root mask in every
one of the seven files, recomputes each control-mask-array digest, checks its
entry count against that repetition's final syntax count, and requires the
full array bytes and digest to agree across all seven repetitions. A summary
digest without the full arrays is not sufficient evidence.
Each `G_i` starts before allocation and ends after serialized-byte hashing and
teardown; no grammar work from a repetition falls into `E_0`.

### Deterministic maximum-work evaluation fixture

The throughput fixture does not sample valid corpus rows. It calls the frozen
production arithmetic, canonicalization, aggregate, ticket, and witness-heap
paths with a deliberately overfilled `MAX_WORK_STAGE`.

Let `B=8*120+256=1216`. Construct consecutive Fibonacci numbers `F_k,F_(k-1)`
where `F_k` is the largest Fibonacci number with bit length at most `B`.
Use `F_0=0,F_1=1,F_(j+1)=F_j+F_(j-1)`; the largest-index tie is therefore
unambiguous. For every branch `a in {0,1}` and node slot `0<=i<5564`, define
the literal signed fixture value

```text
MAG(a,i)=2^(B-1)+2*(2*i+a)+1
V(a,i)=MAG(a,i) if (a+i) mod 2=0, else -MAG(a,i)
j(a,i)=(i+7*a) mod 14
G(a,i)=F_(k-2*j(a,i))
H(a,i)=F_(k-2*j(a,i)-1).
```

All 11,128 magnitudes are distinct positive `B`-bit integers. The slot IDs
are the grammar-attempt ranges `0..443`, `444..1467`, `1468..4539`, and
`4540..5563`, so every root, unary, binary, and adaptive maximum slot has one
literal value on each branch. At every `(a,i)` slot, in this exact order, the
fixture invokes the production value-cap check on `V`, signed comparison of
`V` and `G`, `add(V,G)`, `product(V,H)`, `gcd_abs(V,G)`,
`floor_div(V,G)`, `euclidean_rem(V,G)`, and `centered_rem(V,G)`. It consumes
every status and result into the fixture hash. Oversized results take the
ordinary `VALUE_CAP` path. There is no data-dependent skip. At the ends of
the four displayed slot ranges, each branch array is canonicalized by the
production `(signed_value,grammar_attempt_id)` ordering and its full digest
enters the fixture hash.

One `MAX_WORK_STAGE` performs exactly:

```text
14 tails * 9 Euclidean divisions;
2 branch arrays * 5,564 full-width value/cap checks;
2 branch arrays canonicalized at the root, unary, binary, and adaptive cuts;
5,564 node slots * 2 branches with the literal primitive map above;
11,128 oriented selector comparison and aggregate updates;
1,024 families * 4 tickets with production gcd, partition, certificate,
  and maximum-pressure bounded-heap updates;
the maximum per-worker aggregate and witness buffers.
```

“Maximum” uses the literal production types, not reduced counter arrays.
Before timed stage work, every worker constructs one real `DiscoveryWorker`
at the 5,564-syntax maximum and one real `HeldoutWorker`. The round also keeps
one real maximum `DiscoveryAggregates` and one real maximum
`HeldoutAggregates` live while all worker states are live. This allocates all
11,128 by 28 `CellStats`, all discovery baseline cells, all 192 by 20 heldout
rule cells and counterexample slots, all heldout baseline cells, the 1,024
real `DirectAggregate` objects with four-entry certificate heaps, and the 64
real heldout direct aggregates with sixteen-entry heaps. Every worker and both
merged tables fill each discovery direct hit-modulus set to 896 distinct
strings and each heldout set to 1,280. The fixture strings exceed the maximum
decimal modulus width, so small-string storage cannot understate production.
All registered factor-size and shape sets are filled. Before timed work, every
four-entry and sixteen-entry heap is filled with 1,216-bit witness integers;
both merged heap types are also filled. Timed selector
and baseline updates call the production `update_cell`. Timed direct tickets
increment the real attempt/proper partitions and insert the real
`StressWitness` into both production heap types. The fixture hash consumes
the real cells, partitions, set sizes, and heap records. A substitute
`vector<u64>`, six-counter array, or separately defined stress aggregate is
forbidden.

Its fourteen tail inputs, in tail-ID order, are
`(F_(k-2*s),F_(k-2*s-1))` for `0<=s<14`; every one has more than nine
nonzero Euclidean divisions.

Number rounds `rho=0,1,2,3`, simultaneous workers `w=0,...,W-1`, and each
worker's sequential local stages `ell=0,...,7`. Define

```text
stage_serial=((rho*W+w)*8)+(7-ell)
t_fixture=stage_serial+1
v(stage_serial,family,ticket)=
  1+4*(1024*stage_serial+family)+ticket,
0<=family<1024, 0<=ticket<4.
```

The map `(stage_serial,family,ticket)->v` is injective by quotient and
remainder on the mixed radix `1024*4`. Distinct `(rho,w,ell)` have distinct
`stage_serial`. The decreasing `(7-ell)` order makes later stages within each
fresh worker-round heap have smaller witness keys, so every four-entry and
sixteen-entry bounded heap both fills and executes replacement paths. For the
ticket with this literal `v`, use

```text
N_star=726921560194875913822899294212981087,
ticket_v=720575940379279399*(v*1008806316530991113+1).
```

Because `gcd(P_A,Q_A)=1`, every fixture ticket has certified proper gcd
`P_A` with `N_star`. Its synthetic certificate key uses
`(N_star,t_fixture,ticket,family,abs(ticket_v),P_A)` in the corresponding
fields; fixture-only `family` occupies the syntax-ID field. These records are
never production evidence. All 4,096 ticket values in one stage and all
tickets across all timed stages are distinct.

Calling every expensive binary primitive at every node slot intentionally
does more primitive work than any one production expression node. All fixture
input values obey the production bit cap; an oversized operation result takes
the normal invalid-value path. The fixture asserts the exact call counts and
hashes all final counters so an optimizer cannot remove the work.

Run four rounds. Each round constructs fresh maximum-size worker aggregates
and heaps. In each round, each of the `W` simultaneous workers executes eight
`MAX_WORK_STAGE` instances in ascending `ell` order. Record raw round wall
times `R_1,...,R_4`; each starts before worker allocation and ends after
join, counter hashing, and teardown. Define

```text
R_raw=R_1+R_2+R_3+R_4
R_prod=max(R_2,R_3,R_4).
```

Round one is excluded only from the production projection. Define the
engineering launch forecast

```text
T_eval_forecast=ceil(41472/(8*W))*R_prod*4/3.
```

This forecast is a resource-readiness heuristic. It is not an empirical upper
bound on production time. The 14,400-second cgroup kill is the fail-safe time
bound.

### Cap-derived generator work bound

There is no sampled shadow-corpus extrapolation. The literal cohort caps give
this finite generator-work bound:

```text
ordinary rows = 7*3*32 + 5*3*64 = 1,632
ordinary pair attempts <= 1,632*256 = 417,792
ordinary prime-candidate words
  <= 1,632*256*2*65,536 = 54,760,833,024

safe-prime cells = 7+5 = 12
safe (s,2s+1) candidates <= 12*4,000,000 = 48,000,000
safe primality tests <= 96,000,000
safe index-pair attempts <= 12*200,000 = 2,400,000

consecutive-control odd candidates
  <= sum_(f=8)^22 2^(f-2) = 2,097,088.
```

The consecutive control generator scans each exact-bit odd interval once and
uses adjacent primes from that one scan. It does not restart a next-prime scan
for every `p`. These bounds count attempts through cap exhaustion. They do not
predict how early a valid cell completes and do not imply a wall-time bound.
Every generator loop checks the absolute packet deadline. Cap or deadline
exhaustion aborts the packet and preserves its exact counters.

### Serialization, compression, and launch forecast

Construct one maximum-size serialization image containing every Section 10
component at its registered bound: 41,472 primary corpus rows, 42,432 control
and alias rows, 11,128 discovery selector rows, 1,024 discovery direct rows,
256 heldout rows, 256 selection rows, all 2,016 baseline aggregates, the
exact 42-row baseline definition, all witness and lead-gate slots, and
deterministic manifest, sidecar, and log padding. Fill every variable-width
field to its registered byte limit and require the image length to be exactly
`277979136` bytes. Serialize and hash it seven times, recording raw wall
times `S_1,...,S_7`. The repetitions reuse one declared transient path: after
each close, hash, ledger check, and `du` gate, truncate that path through the
checked writer before the next repetition. At most one serialization image is
live. Each `S_i` starts before file creation and ends after that repetition's
truncate, ledger check, and final `du` gate. Define

```text
S_raw=sum_(i=1)^7 S_i
S_prod=max(S_2,...,S_7).
```

Compress and hash one deterministic 64 MiB SplitMix byte stream seven times
with the exact one-thread production compressor, recording raw wall times
`Z_1,...,Z_7`. These repetitions likewise reuse one checked transient and
keep at most one compressed copy live. Each `Z_i` includes stream creation,
compression, close, hash, both aggregate checks, and transient truncation.
Define

```text
Z_raw=sum_(i=1)^7 Z_i
Z_prod=max(Z_2,...,Z_7)
T_zip_forecast=ceil(277979136/67108864)*Z_prod*5/4.
```

At the gate, let `E_gate` be total monotonic packet elapsed time since the
clock started. Define `E_0=E_gate-(G_raw+R_raw+S_raw+Z_raw)` and require it to
be nonnegative. Thus `E_0` contains compile, exact self-tests, resource setup,
and every other preflight/orchestration interval while excluding exactly the
named 25 raw repetitions. Define

```text
T_preflight_raw=G_raw+R_raw+S_raw+Z_raw
T_production_forecast=G_prod+T_eval_forecast+S_prod+T_zip_forecast.
```

Require the engineering readiness gate

```text
E_0+T_preflight_raw+T_production_forecast <= 10800 seconds.
```

Thus the gate charges every raw preflight repetition in addition to a fresh
production grammar construction, projected production evaluation, production
serialization, and projected production compression. The remaining 3,600
seconds are an unforecast reserve for corpus generation, merges, and failure
closure. This gate is not called a production-time upper bound. All timing
inputs and outputs use integer nanoseconds. Every rational product uses
upward integer division. No term except `T_eval_forecast` is divided by `W`.

### Aggregate memory and disk gates

The exact `W`-worker maximum-work round allocates the shared immutable
grammar, all `W` worker states, maximum per-worker buffers and heaps, aggregate
tables, and the maximum serialization buffer. During it, record:

```text
cgroup memory.peak;
process VmHWM from /proc/self/status;
Maximum resident set size from /usr/bin/time -v.
```

GNU time does not report `VmPeak`; the packet makes no such claim. Let `M` be
the maximum of the three resident-memory measurements after converting each
to bytes. Require

```text
ceil(5*M/4) <= 3758096384.
```

Require the two process-RSS measurements to agree within 64 MiB. Report
`VmPeak` from `/proc/self/status` only as a diagnostic. The read-back
`RLIMIT_AS`, not GNU time, enforces the 4 GiB address-space ceiling.

Require the registered output bound `277979136` bytes, the per-file
`RLIMIT_FSIZE` value `536870912` bytes, the independent checked-writer and
`du` aggregate cap `536870912` bytes, and at least 5 GiB free disk before
production. The preflight exercises the aggregate writer through the maximum
serialization and one live compression temporary, then requires both byte
ledgers and every `du` gate to pass. It emits every raw repetition, fixture
call count, generator cap calculation, formula input, memory reading, byte
ledger, `du` reading, and integer forecast. A failure stops before production
corpus generation.

The benchmark and source must not run while F265 is active.

## 12. Implementation, freeze, and launch gates

The sixth hostile theory pass is a completed prerequisite. Before any dynamic
cohort step:

1. the complete draft must be revised only in a new immutable version after
   any failed audit;
2. algebra, preregistration, source, runner, and manifest must be frozen by
   SHA-256;
3. a fresh hostile pre-run audit must authenticate those exact bytes;
4. the host load, memory, disk, and active processes must pass resource and
   overlap gates;
5. compile and exact self-tests must pass within the packet deadline; and
6. the measured maximum-work stress preflight must pass the readiness gate.

F269 cannot launch while F265 or another incompatible production run is
active.
