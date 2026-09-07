# The adjacent a=-1 path as a positive rational itinerary

**Family:** route:F31

Status: author derivation, awaiting the packet's finite comparison. The
underlying a=-1 involution is Jeřábek Lemma 4.5 / Buresh-Oppenheim prior
art. No novelty claim or short-path bound is made.

Assume N>1, N=1 mod 4, h=(N-1)/2, and use the a=-1 delete-adjacent
path of P246. Handle its first zero stage separately. It arrives at x=2.
As always, test fixed points and nonunits before making a further move.

## Even representatives remove the four-branch alphabet

Conjugate a positive coordinate x to

    u=x if x is even; u=N-x if x is odd.

This bijects [1,h] with the positive even ordinary residues modulo N.
The adjacent auxiliary becomes u -> N+1-u. The arithmetic involution
becomes the even representative of the inverse class {u^(-1),-u^(-1)},
except for its prescribed 0 / (N-1) swap.

Let v be the ordinary inverse of u. At a nonspecial unit stage the combined
move is

    v odd:  u -> 1+v,
    v even: u -> N+1-v.

Its two projective matrices are

    M+ = [[1,1],[1,0]],  M- = [[1,-1],[1,0]].

The first unit state is u=2 and v=(N+1)/2, which is odd. A word +-- is
impossible in the subsequent nonterminal path: M-^2 M+ = diag(-1,1), so
it would send an even ordinary residue to an odd one modulo odd N.
Therefore the reached path consists of blocks + and +-, subject to the
terminal tests at the intermediate state. This is an actual restriction
from the chosen representatives, not only a relation in a matrix group.

The block matrices are

    P=M+   = [[1,1],[1,0]],
    Q=M-M+ = [[0,1],[1,1]].

For a positive primitive lift u=U/V modulo N, starting at (U,V)=(2,1),
the exact updates are

    P: (U,V) -> (U+V,U),
    Q: (U,V) -> (V,U+V).

These are positive rational-tree steps. Both preserve gcd(U,V)=1 and
strictly increase U+V. They are a concrete continued-fraction / Farey
correspondence. They do not yet specify a known real target whose ordinary
Euclidean quotients would recover the itinerary without following it.

## One modular inverse per block

At the beginning of a block maintain even u, odd v, and u*v=1 modulo N.
After the fixed-point test, gcd(u+1,N)>1 yields a proper divisor. Otherwise
let z be the ordinary inverse of u+1. The branch and new inverse pair are

    z even: Q, (u,v) -> (z,u+1),
    z odd:  P, (u,v) -> (v+1,N+1-z).

To verify this, after the plus move the current point is v+1. Its inverse
is 1-z modulo N, whose ordinary representative is N+1-z. If z is odd,
that inverse is odd, so the next block starts immediately: this is P.
If z is even, the next move is minus and returns z; its inverse is the odd
number u+1. This is Q. All displayed residues lie in [1,N-1] on the
reached nonspecial path.

The terminal tests are essential. At a block state, the only possible
unit fixed endpoint has u^2=-1 modulo N. A proper gcd(u+1,N) is the
nonunit reached at the intermediate plus point, because
gcd(v+1,N)=gcd(u+1,N). In the Q case, an intermediate unit fixed point
would require (v+1)^2=1, hence v=-2 and u=h. The corresponding intermediate
point is the special representative N-1. This would return to the original
zero start, so it cannot occur on its nonterminal simple path. Retain the
special guards when checking a standalone implementation against P246.

In integer lifts, the two output conditions are

    gcd(U+V,N)>1, while U,V are units modulo N;
    U^2+V^2=0 modulo N.

The latter is a square root of -1, not automatically a factor. No P02
hidden-root probability applies to this fixed a=-1 input. When N has a
prime divisor equal to 3 mod4, the root case is impossible, so its terminal
output is a proper factor. This still gives no expected QP path bound.

## What a rational jump must decide

The consecutive blocks Q then P have product

    P Q = [[1,2],[0,1]],

and therefore send u to u+2. Away from earlier endpoints, their branch
conditions say that the ordinary inverses of u,u+1,u+2 have parities

    odd, even, odd.

Thus a run of these parabolic blocks advances through consecutive integers.
To certify its full actual-path length, one can seek the first nonunit,
fixed endpoint, or failure of the alternating inverse-parity pattern.
This is an inverse-residue interval query. It is not obtained by an
ordinary division of the positive lift coordinates U,V.

For a unit t, its ordinary inverse is even exactly when the centered
inverse of 2t is positive: divide the even inverse by two; an odd inverse
instead requires adding N before division and lands in the negative half.
Hence the jump's parity condition is a half-interval condition on the
modular inverse curve. This identifies its arithmetic content precisely.
The existing P246 floor counts concern the linear map y -> a*y and do not
evaluate this inverse condition.

Matrix powering does evaluate a proposed Q/P block string quickly. It does
not prove that the string is the one selected by N. A randomized procedure
may deliberately propose a different word and verify a gcd or root at its
endpoint; such a proposal needs its own charged success bound and need
not certify the skipped actual path.

## Size question to discriminate

The root proposed checking whether the positive lift always has
U^2+V^2<=2N before termination, then found this hand candidate at N=61:

    (2,1) -> (3,2) -> (5,3) -> (3,8)
           -> (8,11) -> (19,8) -> (8,27).
    Choices: P,P,Q,Q,P,Q.

The norm at (8,11) is 185>122. The final norm is 793=13N and the final
even residue is 50, whose square is -1 modulo 61. The bounded comparison must
verify these branches and terminal guards before this becomes a finite
counterexample. If it passes, only this 2N size bound is refuted; the
positive rational correspondence and the inverse-parity query remain.
