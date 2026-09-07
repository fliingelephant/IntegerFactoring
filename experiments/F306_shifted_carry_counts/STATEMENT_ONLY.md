# Statement for independent reconstruction

Let k>=2, M=2^k, and let N be any positive odd integer. For each odd
u in [0,M), let v(u) be the canonical odd representative of N/u modulo M.
For integer cut coordinates c,d in [0,M], define

    x_c(u)=u+M*1_(u<c),
    y_d(u)=v(u)+M*1_(v(u)<d),
    q_cd(u)=(x_c(u)*y_d(u)-N)/M,
    B(c,d)=sum_(u odd<M) q_cd(u)*(q_cd(u)-1)/2 mod M.

The division by two in each summand is an exact integer operation. In
particular the definition does not assume that sum q_cd(u)^2 is even.
The full integer N defines the carries, including when they are negative.

Claim: for 0<=a<=b<=M and 0<=c<=d<=M, the canonical inverse-graph count

    C=number of odd u with a<=u<b and c<=v(u)<d

is the canonical residue modulo M of

    (N-M/2)^(-1) * [B(b,d)-B(a,d)-B(b,c)+B(a,c)].

The multiplier is invertible modulo M, and 0<=C<=M/2<M. The same identity
is valid for empty intervals and for endpoint M. No asymptotic evaluator
for B is supplied by the claim.

Conditional complexity consequence: suppose a uniform deterministic or
classical Las Vegas subroutine returns the correct B(c,d) modulo M at
these public cut coordinates, with expected bit cost T(n) whenever its
inputs have O(n) bits. Then each such rectangle count, including its
emptiness, is computable using four calls and polynomial additional bit
work. Here T is a nondecreasing uniform bound; randomized calls use fresh
random bits and terminate almost surely with correct residues.

One declared dependency may be used for complete factoring: P237 states
that the public dyadic inverse-graph rectangle-emptiness interface gives
complete all-input factoring with O(n^2) calls and polynomial additional
work, where n=ceil(log2(N+1)). It uses M equal to the largest power of two
at most the current odd cofactor divided by eight. Small constant inputs
may be handled directly. Using this dependency, the claimed B subroutine
gives a uniform all-input expected bound O(n^2*T(n)+poly(n)). A
quasipolynomial T therefore suffices. This is conditional; no such T has
been proved for B.

Please reconstruct the algebra, divisibility, endpoint cases, retained
precision, and conditional cost from this statement alone. Do not read
the author report or other files in this packet.
