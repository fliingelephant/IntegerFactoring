# F279-D06 additive accounting algebra

## Status, ancestry, and merge rule

F279-D06 is an unfrozen theory/interface amendment. It authorizes no
runner, fixture, tape, source freeze, compile, preprocessing, self-test,
benchmark, scientific execution, private-label access, remote access,
ledger change, staging, or commit.

Its authenticated immediate inputs are:

```text
D05_DRAFT_ALGEBRA.md
5e27479a5298b2ed6758bc81ba6f1aabaca107b97a624887aa7d420eef114763

D05_DRAFT_PREREGISTRATION.md
2d76c815fe752d1bc7f50caac788ab8943a8ec2a46377e7773677590a416cdb5

D05_HOSTILE_THEORY_AUDIT.md
b22d63037d47c670c9535135d34847c7895afc432b181e8190ec3386f416a64a
```

Read this file and `D06_DRAFT_PREREGISTRATION.md` additively with the exact
D01--D05 bytes. D06 supersedes only the undefined primitive accounting in
the four certificate fields

```text
global_order_checks,pair_muls,mod_muls,gcds
```

and the formerly nonliteral benchmark vector. All endpoint signs, source
and candidate states, finite relation-box semantics, ExactTape256 law,
packet caps, manifests, public/private firewall, replay chronology,
probability scope, and D05 status interface remain unchanged. Every future
artifact prefix and JSON version is `F279-D06`.

The incomplete, unaudited `f279_public.cpp` is not an input to D06. D06
does not authenticate, amend, freeze, or authorize use of those bytes.

## 1. Logical primitives, not implementation accidents

Evidence counters describe one canonical logical evaluator. They do not
count C++ expressions, allocator calls, machine instructions, Euclidean
loop iterations, cache hits, or wall-clock events. An implementation may
cache equal values or fuse arithmetic, but it charges the same logical
primitives as the reference evaluator below. It may not make evidence bytes
depend on an optimization, thread schedule, or cache layout.

All operands are first reduced to their inherited canonical residue when
the inherited algorithm says `mod N`. The logical charges are:

```text
gcd2(a,b)
    one gcd

inverse(a,N)
    one inverse and zero gcds; its internal extended-Euclid iterations are
    not separate gcds

mod_product(a,b,N)
    one mod_mul for forming a*b and reducing modulo N

pair_product((R,S),(X,Y),eta,N)
    one pair_mul and five mod_muls, in this order:
    R*X, S*Y, eta*(S*Y mod N), R*Y, S*X

matrix_product(A,B,N)
    one matrix_mul and eight mod_muls in row-major output and inner-index
    order
```

Additions, subtractions, comparisons, signs, shifts, exact integer
division, integer products that are not reduced modulo `N`, canonical
formatting, and mask updates have no `mod_muls` charge. A modular square is
one `mod_product`. A product chain has one charge for each binary product;
thus `eta*W*W mod N` has two charges.

The three-argument control expression is not one primitive:

```text
gcd(V,W,N) = gcd2(gcd2(V,W),N).
```

It therefore charges exactly two gcds. Every other displayed inherited gcd
charges one gcd. Factor multiplication checks and exact-square tests charge
no gcd unless the inherited chronology explicitly displays a gcd.

## 2. Canonical powers and bounded caches

For a positive exponent `e`, canonical pair power starts with accumulator
`(1,0)`, base `(t,1)`, and processes the binary expansion from least to
most significant bit:

```text
while e>0:
    if e is odd: accumulator=pair_product(accumulator,base)
    e=floor(e/2)
    if e>0: base=pair_product(base,base)
```

There is no unused square after the last bit. Define

```text
pow_pair_muls(0)=0
pow_pair_muls(e)=popcount(e)+floor(log2(e))  for e>0.
```

Matrix power uses the identical control flow with `matrix_product`.
Negative inherited powers compute the positive power of the absolute
exponent and then negate the second pair coordinate. Negation has no
primitive charge.

Canonical scalar modular power uses the same loop with `mod_product` in
place of pair product. Define

```text
pow_mod_muls(0)=0
pow_mod_muls(e)=popcount(e)+floor(log2(e))  for e>0.
```

For each endpoint-eligible named source, the canonical source cache starts
with powers zero and one and obtains powers `2,...,16` by fifteen successive
multiplications by `(t,1)`. It separately computes `(P_B,Q_B)` with the
binary algorithm. Numerically equal named sources each own these charges.

For a raw proper candidate, the canonical lazy relation cache:

1. computes target powers `2,...,16` by fifteen successive pair products;
2. extends that candidate's view of the named source cache from power 16
   through power 256 by 240 successive pair products; and
3. uses those cached pairs for all 32 orbit, 15 target-torsion, and 495
   mixed determinants.

No lazy cache is charged for `no_hit`, `saturated_hit`, a target-ineligible
slot, or a source-ineligible slot. Every saturated mixed relation owns one
separate canonical binary power at exponent `m*(B-e)`. Equal exponents are
not merged because each registered relation owns one packet-cap event.

## 3. Exact isolated-certificate counters

The four certificate counters are the cost of an isolated canonical public
classification replay of that one certificate. They are not a partition of
the phase summary. In particular, their source cost is deliberately repeated
in certificates that share a source. This makes a certificate independently
reconstructible while the phase summary charges shared named-source work
only once.

Let `k` be the number of saturated mixed relations in this certificate.
List their registered exponents in inherited `(e,m)` chronology as

```text
L_j=m_j*(B-e_j),  j=1,...,k.
```

Every certificate is a raw proper endpoint, so its complete-box cost is:

```text
global_order_checks = k

pair_muls
    = 15                         source powers 2,...,16
    + pow_pair_muls(B)           source power B
    + 15                         target powers 2,...,16
    + 240                        source powers 17,...,256
    + sum_j pow_pair_muls(L_j)   large mixed-order checks

mod_muls
    = 5*pair_muls
    + 1      t^2 in the source discriminant
    + 1      v^2 in the target invariant
    + 1      v*Q_B in the endpoint
    + 32     one v*Q_e in every orbit screen
    + 990    two products in every one of 495 mixed determinants

gcds
    = 19     g_eta, g_delta, fifteen source-order gcds, g_Q, g_P
    + 2      g_H and g_F
    + 542    32 orbit, 15 target-torsion, and 495 mixed gcds
    + k      one gcd for each large mixed-order check.
```

Equivalently, every certificate must satisfy

```text
mod_muls = 5*pair_muls+1025
gcds = 563+global_order_checks.
```

The certificate fields exclude row cleanup, atom construction, uniform
controls, diagnostic scans, checksum hashing, serialization, label work,
and every literal matrix replay. Those operations have no ownership by an
individual ranked certificate.

The complete registered box still runs after the first proper relation.
Thus direct and global certificate classes use the same formulas. All
saturations remain in the mask, and every saturated mixed relation still
owns its large check.

## 4. Phase ownership and replay

The D03 summary `operation_counts` is the sum of primary-phase logical
owners in this exact hierarchy:

```text
phase
  row cleanup owner
  named source owner, once for each of 900 source IDs on an eligible row
  ranked candidate owner, once for each candidate action actually reached
  ExactTape256 control-attempt owner
  diagnostic scan owner
  retained diagnostic-source owner
  diagnostic-target owner
  canonical serializer/SHA owner
```

A named source owns its invariant, small-power, `B`-power, `g_Q`, and `g_P`
work once. A ranked candidate owns `g_H`, its endpoint when reached, and its
lazy complete box only for a raw proper endpoint. A control reuses the
source pair without reallocating source work. It owns two gcds for
`gcd(V,W,N)`, one target-invariant gcd, and, only on acceptance, its two-
product endpoint and endpoint gcd. Rejected attempts own only operations
already reached.

A diagnostic scan owns one gcd for each displayed base record, one modular
multiplication and one gcd for each positive-exponent record, and no ranked
candidate charge. A retained diagnostic source is shared once across its 90
targets. Each diagnostic target then follows the same target and lazy-box
rules as a ranked target. Its large mixed checks increment the same D05
packet counter, but diagnostic endpoints do not increment the D05 raw-ranked-
hit counter and do not create ranked certificates.

Every primary raw ranked certificate and every primary raw diagnostic
target runs the inherited literal matrix equality before serialization. It
owns one `inverse(2,N)`, forms `inv4=inv2^2 mod N`, constructs the three
nonconstant matrix entries using the already owned `v^2`, matrix-powers at
`B`, scalar-powers `inv2` at `B`, and multiplies that scale by `F`. If
`h=pow_pair_muls(B)`, this check adds exactly

```text
inverses    1
matrix_muls h
mod_muls    5+8*h+pow_mod_muls(B).
```

The five nonmatrix products are `inv2*inv2`, the three matrix-entry scale
products, and the final scale-times-`F` product. The earlier candidate owns
the reused `v^2`. These matrix charges enter the phase summary but remain
excluded from the four isolated-certificate fields in Section 3.

Endpoint and control checksum streams own only their D03 SHA and
serialization counts. Public replay repeats every literal matrix check,
reconstructs the primary logical counts, and compares the sealed summary;
it does not add the replay invocation's physical work to those reconstructed
counts.

Operational deduplication never changes ownership. Four-worker execution
charges by the immutable `(phase,row,source,candidate/control,diagnostic)`
keys and merges in inherited order.

## 5. Caps and aborted work

The D05 raw-hit gate occurs after `g_F` and before any lazy-box primitive.
The D05 global-order gate occurs before exponent construction and before
any pair or gcd charge for that check. A permitted global check increments
both the packet event counter and its owner's certificate or diagnostic
count exactly once.

A source terminal event creates no candidate endpoint and no certificate.
A target terminal event creates no endpoint and no certificate. A failed
cap check, control shortfall, arithmetic abort, resource abort, replay
abort, or output abort produces no successful summary or certificate whose
counters could be evidence. Partial files from that failed root retain no
accounting authority. There is therefore no serialization rule for a
partially computed or aborted certificate.

These rules make equal logical executions serialize equal counters while
leaving both D05 packet caps independently reconstructible.
