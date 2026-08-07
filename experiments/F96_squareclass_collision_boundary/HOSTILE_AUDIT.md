# F96 hostile independent audit

## Verdict: FAIL

The general square-class theorem is correct. The principal arithmetic
witness, the distinct-value useful selector, and the finite enumeration
orders also check. The candidate nevertheless fails as written because its
source silently excludes candidates with exact relation value P = P1, while
its JSON and prose report unqualified same-square-class collision and
closure counts. Those counts and two exact prose claims are false without a
distinct-relation-value or useful qualifier.

There is also a provenance wording defect. The useful-candidate acceptance
path is independent of the supplied target 842, but the executable does
receive 842 and compares every menu residue and inverse against it for a
diagnostic field. Thus the mathematical blind selector is valid, while the
literal statement that the run does not receive or use 842 is too strong.

## Pinned input artifacts

I pinned these hashes before reading any F96 artifact:

    78217eac369f3d09dd3946639e1ba23f56e80ac5701bca6e5c983389d17c681e  OUTPUT.json
    06977d6640a6a5f2ef7bdf701fd18b216a1deee1904e0369320e8a7b0478d7e5  RECONSTRUCT_STATEMENT.md
    30db80cb70034a71796d36e3d793fe7f2470e67443590016e81a094bb01f3af6  RESULT.md
    9d2374d1ee5bc8bb6b70a22f21bb3cf0c97e6f49efffc9da287e9adebb050f5d  RUN.log
    63f1c9e449cda35731f8a67bb906bdcf96cceb0371cfcebbaae0590629a4edc0  RUN_MANIFEST.md
    69dee0fc29ee352d389b501e46820941f2c65f79375ef9378c525991d0df8e06  analyze_squareclass_boundary.py
    3fcd569f574cee030ca8406825a407df882003a9cc8bfb730b549379eedc40bb  run_with_timeout.py

I read every pinned file. I did not read a reconstruction result. I then
used an independent SageMath enumerator that did not import the discovery
source. I also replayed the pinned source to a temporary output. Every
deterministic replay field matched OUTPUT.json; only elapsed_seconds
changed.

## 1. General theorem: PASS

For every prime r, write

    x_r = v_r(P1),    y_r = v_r(P2).

Equality in the positive rational square-class group is equivalent to

    x_r congruent to y_r modulo 2

for every r. This is also equivalent to every exponent x_r + y_r in P1 P2
being even, hence to P1 P2 being an integer square.

Let D = gcd(P1,P2). Its r-adic exponent is min(x_r,y_r). When x_r and y_r
have the same parity, both

    x_r - min(x_r,y_r)
    y_r - min(x_r,y_r)

are even. Therefore P1 / D = A squared and P2 / D = B squared. At most one
of these two quotients has a positive r-adic exponent, so gcd(A,B) = 1.
Moreover min(x_r,y_r) has the common parity of x_r and y_r. Since P1 and
P2 are nonsquares, D is a nonsquare. The converse is immediate from
P1 = D A squared and P2 = D B squared.

Because each Pi is one modulo N, each Pi is a unit. Every divisor D of a Pi
and both square roots A and B are also units modulo N. Cancelling D gives

    A squared congruent to B squared modulo N.

The exact positive root is

    R = D A B,

and R squared is one modulo N. The identities

    D B (A - B) = R - P2
    D B (A + B) = R + P2

and the fact that D B is a unit give

    gcd(R - 1,N) = gcd(A - B,N)
    gcd(R + 1,N) = gcd(A + B,N).

For odd N, the prime-power divisors of N split between R - 1 and R + 1.
Thus a proper factor occurs exactly when R is neither global sign modulo N.
Multiplication by the unit D B makes this equivalent to A being neither
global sign of B.

The N = 143 counterexample is exact:

    102 times 136 = 13872 = 3 times 68 squared = 1 + 97 times 143
    125 times 135 = 16875 = 3 times 75 squared = 1 + 118 times 143
    R = 3 times 68 times 75 = 15300 congruent to -1 modulo 143.

Independent enumeration confirms that this is the first global-sign pair
in the declared increasing distinct-odd-semiprime and relation order.

## 2. Fatal collision-count defect

The theorem does not require P1 and P2 to be distinct. In particular,
P = P1 has the same nonzero square class as P1, and P1 times P1 is an exact
square. Such a repeat closes the parity column, although its induced root is
the global root P1 congruent to one and is not useful.

The discovery source instead begins collision_with_first with

    if candidate P equals first_product:
        return no collision

and only then performs the square-product test. This is a legitimate search
for a new distinct relation value, but the resulting fields and prose do
not state that restriction.

The exact independent counts are:

| Search set | All same-class residues | Distinct-value same-class residues | Useful residues |
|---|---:|---:|---:|
| 12 raw monomials below N | 4 | 0 | 0 |
| bound n canonical menu | 4 | 0 | 0 |
| bound n squared canonical menu | 5 | 1 | 1 |
| complete subgroup H | 6 | 2 | 2 |

The four omitted residues are

    3, 43, 129, 1849.

Their canonical inverse products all equal P1 = 5547. The complete subgroup
has those four plus

    1263, 1684,

whose product with their respective canonical inverses equals the distinct
value P2 and gives a useful root.

Consequently:

- OUTPUT.json reports zero same-square-class collisions for the raw and
  bound-n menus, but the literal counts are four.
- OUTPUT.json reports one such collision for the n-squared menu, but the
  literal count is five. The first literal collision occurs before
  exponent pair (99,1).
- OUTPUT.json reports two complete-subgroup collisions, but the literal
  count is six.
- RESULT.md says exactly two residues in H have the same nonzero square
  class as P1. The exact number is six.
- RESULT.md gives 2/1334 = 1/667 as the exact probability of a closing
  presentation. The unqualified same-class closure probability is
  6/1334 = 3/667. The useful or new-distinct-value probability is 1/667.
- RESULT.md says the bound-n menu finds no closure. It finds four exact
  repeats of P1; it finds no distinct-value or useful closure.
- RUN_MANIFEST.md similarly says no raw monomial creates a same-class
  closure and that the subgroup has two closing residues. Both need the
  same qualifier.

RESULT.md does acknowledge elsewhere that four raw candidates reproduce
P1. That acknowledgement makes the useful intended distinction clear, but
it does not repair the unqualified exact counts or labels.

The correct repair is not to change the search. It is to define the search
as one for a distinct exact relation value and to qualify every associated
count, first-collision field, closure statement, and density. Alternatively,
the artifacts must count all same-class repeats and separately report the
distinct and useful subsets.

## 3. Fixed arithmetic and subgroup claims: PASS

Independent exact arithmetic gives

    N = 2773 = 47 times 59
    ord_N(3) = 667
    ord_N(43) = 1334
    43^667 congruent to -1 modulo N.

The relation 3 times 43 squared is one modulo N, so

    3 = 43^(-2)

inside the unit group. Hence H generated by 3 and 43 is the cyclic group
generated by 43 and has size 1334.

For the F95 endpoint,

    842 times 43^(-1) mod N = 471
    471 squared mod N = 1
    471 is neither 1 nor -1 mod N.

A cyclic group has at most one nonidentity involution, and the involution
in H is 43^667 = -1. Thus 471 is not in H, so neither 842 nor its inverse
2526 is in H. The nonmembership certificate is valid.

The alternative presentation is also exact:

    3^99 times 43 mod N = 1263
    inverse_N(1263) = 1684
    1263 times 1684 = 2126892 = 3 times 842 squared
    gcd(108618 - 1,2773) = 47
    gcd(108618 + 1,2773) = 59.

The shortest positive words under the declared BFS order are (99,1) for
1263 and (0,197) for 1684. The shortest signed words are (98,-1) and
(-98,1), respectively.

## 4. Raw products and menu ordering: PASS after the qualifier

The direct-product loop exhausts all nonnegative monomials

    3^a 43^b < 2773

other than one. Since both bases exceed one, the nested stopping conditions
omit none. There are exactly twelve:

    3, 9, 27, 43, 81, 129,
    243, 387, 729, 1161, 1849, 2187.

None gives a distinct relation value in P1's square class, and none gives a
useful collision. Four give P1 itself. The strict occurrence limits
a at most 1 and b at most 2 select exactly those four repeats.

For n = 12, the bound-n menu contains 169 exponent pairs. Since

    3^a 43^b = 43^(b - 2a) modulo N,

the menu reaches the 37 distinct exponents from -24 through 12. It has no
distinct-value collision.

For bound 144, there are

    145 squared = 21025

exponent pairs and 433 distinct residues. The useful residue 1263 requires

    b - 2a = -197.

The first nonnegative solution under increasing a+b and then increasing a
is (a,b) = (99,1). All totals below 100 contribute 5050 pairs, and this is
the 100th pair at total 100. Its one-based pair ordinal is therefore 5150.

Before total 100, 297 distinct residues have appeared. Pair (0,100) adds
one, and pair (99,1) adds the next. Its one-based unique-residue ordinal is
299. Thus the ordering claims for the first distinct-value useful collision
are exact.

The full canonical relation census independently gives 634 unique values,
631 nonsquares, and three distinct-value same-class pairs. All three roots
are useful. These counts match the recorded finite census.

## 5. Target and factor provenance

No factor of 2773 enters the useful menu's acceptance path. The menu forms
residues from N, 3, and 43; takes canonical inverses; tests the exact square
P1 times P; and then computes root gcds. The supplied target relation P2 is
not consulted by that path. An independent enumeration with no target
query returns the same first useful pair (99,1).

However, the executable is invoked with target 842. Inside the menu loop it
tests whether each residue or its inverse equals that target and appends
matches to menu_target_hits. Those diagnostics do not affect ordering,
deduplication, collision acceptance, or early stopping, and the recorded
target-hit lists are empty. Therefore there is no selection leakage, but
the literal claims that the executable menu does not receive or use 842
are inaccurate. The evidence should say that selection is target-independent,
or it should use a separate runner that does not accept a target.

The complete relation census performs public gcds on nonunits and can expose
factors, but it runs after the menu and is marked certificate-only. The
bounded N at most 199 counterexample scan deliberately uses trial
factorization and is also disclosed as certificate-only. Neither affects
the N = 2773 useful-candidate selection.

## 6. Representation and complexity scope

The phrase representation-level gain inside an unchanged subgroup is exact
when scoped to the alternative endpoints. Both 1263 and 1684 lie in H, so
creating their canonical inverse relation does not require residue-subgroup
growth. Public square normalization of that relation then names the block
842, which lies outside H. This is representation gain, not prior abstract
subgroup enlargement.

The fixed two-block menu has O(n^4) pairs and uses polynomial-bit arithmetic,
so it is polynomial in n = ceil(log_2 N). The exponent bound was chosen
after a complete O(N) subgroup scan. RESULT.md and RUN_MANIFEST.md disclose
this post-selection and make no all-input success, density, or factoring
claim. Those complexity and scope statements are sound.

## 7. Artifact consistency

- The source, runner, log, JSON, and result hashes agree with the manifest.
- The runner command and 120-second timeout agree with RUN.log.
- The recorded process exited with code zero.
- RUN.log pins the exact OUTPUT.json hash.
- A replay reproduced every deterministic JSON field.
- The source correctly implements its actual distinct-P convention, but the
  field names and human claims do not expose that convention.

## Final decision

FAIL. The core theorem and the useful distinct-P2 witness survive hostile
checking, but the current candidate's unqualified collision, closure, and
density claims are exactly false. The target-independent selector also
needs provenance wording that distinguishes its acceptance path from the
target-aware diagnostic executable.
