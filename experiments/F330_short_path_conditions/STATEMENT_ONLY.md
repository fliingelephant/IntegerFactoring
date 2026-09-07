# Exact count and path-coordinate statements

**Family:** route:F31

This is a proof-free reconstruction input. The declared dependency is P246,
whose precise involution and path guarantee are restated below. No short-path,
probability, small-lift-size, novelty, or expected quasipolynomial claim is
part of this statement. No experimental outputs are dependencies.

## Definitions and declared dependency

Let N>1 be odd, h=(N-1)/2, and rep select [-h,h] modulo N. Let a be a
unit modulo N. For 0<=t<=h define

    Q(t) = #{1<=y<=t : 1<=a*y mod N<=h}.

If Jacobi(a,N)=1, P246 gives an involution F on

    D = {0,...,h} union {-y:1<=y<=h, rep(a*y)>0}.

It swaps 0 and 1 and fixes every nonzero nonunit. For a remaining unit x,
put w=rep(x^(-1)); use the first applicable branch:

    x>0 and w>0:          F(x)=w;
    rep(a*x)<0 and w<0:  F(x)=rep(a^(-1)*w);
    otherwise:           F(x)=-x.

A fixed nonunit gives gcd(x,N); a unit fixed in the first branch gives
the proper divisor gcd(x-1,N); a unit fixed in the scaled-inverse branch
gives a square root x^(-1) of a.

Put L=Q(h), d=L+h+1. P246 states that d is odd. Increasing rank is

    R(-y)=L-Q(y),  R(x)=L+x for x>=0.

Its inverse selects the least positive y with Q(y)>=L-i when i<L,
and returns -y; when i>=L it returns i-L. Exact Euclidean floor sums
compute size, rank, and selection in polynomial bit time.

Two auxiliary rank involutions with sole fixed rank L are:

    reflection: A(i)=(2L-i) mod d;
    adjacent: delete L, pair compressed indices j with j XOR 1, restore L.

By P246, starting at coordinate 0 and alternating F then the chosen auxiliary
reaches an F-fixed endpoint in at most d<=N F evaluations. Test the F-fixed
condition before an auxiliary move. Its nonterminal open path never repeats
a coordinate. This finite path bound is the only traversal bound declared.

## Claim 1: count reciprocity at a signed remainder

This claim requires only odd N, unit a, and 1<=t<=h; it does not require
Jacobi(a,N)=1 or that t be a unit. Let b=a^(-1) modulo N and

    C_t(u,v) = #{k in [u,v]:1<=b*k mod N<=t-1}.

An empty interval contributes zero. Let r=rep(a*t), which is nonzero.
Then

    r>0:   2Q(t)=t+1+C_t(1,r-1)-C_t(h+1,h+r);
    r=-s<0: 2Q(t)=t-1+C_t(h+1-s,h)-C_t(N-s+1,N-1).

In particular, |2Q(t)-t|<=|r|. At r=1, Q(t)=ceil(t/2); at r=-1,
Q(t)=floor(t/2). Evaluating the displayed right side requires at most
2|r|-1 inverse-image membership tests after b is computed, or
O((1+|r|)*poly(log N)) bit work. This is not a polylogarithmic improvement
over the existing floor-sum evaluator unless the remainder is suitably small.

## Claim 2: reflection has exact affine defects

Assume Jacobi(a,N)=1. For an accepted positive y set E(y)=2Q(y)-y.
Write B=R^(-1) A R for the coordinate reflection auxiliary. Then

    B(-y)=(y+E(y))/2;
    B(z)=-2z+E(y), if 1<=z<=L and y=min{u:Q(u)>=z};
    B(z)=d-z, if L<z<=h;
    B(0)=0.

In the second line Q(y)=z. These formulas concern the actual auxiliary;
they imply no general smallness of E or rapid termination of its iterates.

## Claim 3: constant matrices for a=-1

Assume N>1 and N=1 mod 4, and set a=N-1. Then L=0, d=(N+1)/2,
D={0,...,h}, and every nonspecial unit x has

    F(x)=abs(rep(x^(-1))).

All F-fixed and special 0/1 guards remain in force. Under reflection, the
first moving stage sends 0 to h, and every later nonterminal nonspecial
unit stage satisfies

    x'=d-abs(rep(x^(-1))).

For z=2x-1 modulo N and sigma=-sign(rep(x^(-1))), this becomes

    z'=4*sigma/(z+1) modulo N,
    M_sigma=[[0,4*sigma],[1,1]].

The characteristic discriminants are 17 for sigma=1 and -15 for sigma=-1.
An integer lift z=U/V starts at (-2,1) after the first stage and updates
by (U,V)->(4*sigma*V,U+V). Its integer pair is primitive. While the current
x is a unit, the denominators needed for the next move are units. At a
current nonunit x with V still a unit, gcd(U+V,N)=gcd(x,N). After T
updates the lift height is at most 2*4^T; this bounds stored lift bits, not T.

For the adjacent auxiliary, every positive coordinate y is paired with
y+(-1)^(y+1). At a nonspecial nonterminal unit stage let

    w=rep(x^(-1)), s=sign(w), epsilon=(-1)^(abs(w)+1).

Then

    x'=epsilon+s/x modulo N,
    C_epsilon,s=[[epsilon,s],[1,0]].

When s=-1, C_epsilon,-1^3=-epsilon*I. Thus three identical such moving
branches cannot occur consecutively on the open path. Starting after the
first zero stage at x=2 with lift (U,V)=(2,1), the integer update is
(U,V)->(epsilon*U+s*V,U). It preserves primitive pairs and bounds their
height by 2^(T+1) after T updates. All these are exact identities, not
short-path bounds.

## Claim 4: the adjacent path has positive rational blocks

Keep N=1 mod 4 and a=-1. Conjugate x in [1,h] to the even ordinary residue

    u=x if x even; u=N-x if x odd.

The auxiliary becomes u->N+1-u. Away from special and terminal states,
write v for the ordinary inverse of u. A moving step is

    plus:  u->1+v, if v odd;
    minus: u->N+1-v, if v even.

After the initial zero stage u=2 and v=(N+1)/2 is odd. Before termination,
the reached moving word consists of blocks plus or plus-minus. In particular
it contains no plus-minus-minus substring. The block matrices and positive
primitive integer lifts are

    P=[[1,1],[1,0]],  (U,V)->(U+V,U);
    Q=[[0,1],[1,1]],  (U,V)->(V,U+V),
    initial (U,V)=(2,1), u=U/V modulo N.

The following public kernel groups exactly these reached blocks, possibly
returning a verified divisor before the corresponding intermediate F call:

    u=2; v=(N+1)/2;
    repeat:
        if u*u mod N == N-1: return the square root u of -1;
        g=gcd(u+1,N);
        if 1<g<N: return g;
        z=(u+1)^(-1) mod N, using its ordinary representative;
        if z even: (u,v)=(z,u+1);             # Q
        else:      (u,v)=(v+1,N+1-z);         # P

The assignments use the old u,v. At the start of every nonterminal kernel
iteration, u is even, v is odd, u*v=1 modulo N, and both are in [1,N-1].
The gcd preceding inversion is 1 whenever no output was returned. A P block
is one nonspecial F/auxiliary stage and a Q block is two; apply terminal
tests at the intermediate state when comparing with the fine path.
The potential special intermediate point N-1 would require u=h, which is
unreachable before termination on this open path. There is no suppressed
nontrivial unit fixed endpoint at a Q intermediate point.

Thus the kernel terminates by P246, returns only the stated verified
factor-or-root outcomes, uses one modular inverse per moving block, and
has at most O(N) blocks of polynomial bit cost. In integer lifts the two
output conditions are gcd(U+V,N)>1 or U^2+V^2=0 modulo N, with U,V units
before the tests. If N has a prime divisor 3 mod 4, the root outcome is
impossible. This is a fixed-input a=-1 statement; no private-random-root
probability is asserted.

## Claim 5: translation runs expose an inverse-parity query

At a reached block start, u is even and its ordinary inverse is odd.
Away from any earlier fixed/nonunit/special endpoint, consecutive Q then P
blocks send u to u+2. They are selected exactly when the ordinary inverses
of u,u+1,u+2 have parities odd,even,odd. Longer such runs have the
corresponding alternating inverse-parity condition on consecutive integers within [1,N-1].
All gcd and fixed-point guards must still be accounted for in a jump.

For any unit t modulo odd N, its ordinary inverse is even if and only if
rep((2t)^(-1))>0. Thus the parity condition is a half-interval condition
on the modular inverse curve. No algorithm to find its first mismatch,
or probability bound for a proposed jump, is included in this statement.
