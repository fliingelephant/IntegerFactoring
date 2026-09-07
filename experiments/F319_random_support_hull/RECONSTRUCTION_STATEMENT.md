# F319 statement for independent reconstruction

Let N>=4 be an integer and let S={(x,y) in Z^2:x,y>0,xy>=N}.
For any integers p,q>=2 with pq=N, write the two neighbors of P=(p,q)
on the lower convex hull of S as L=(p-h,q+k), R=(p+H,q-K).
Thus h,H,k,K are positive integers. Set lambda_minus=K/H and
lambda_plus=k/h.

Claim A: P is uniquely exposed by every normal (lambda,1) with
lambda_minus<lambda<lambda_plus, and

    N*(lambda_plus/lambda_minus-1)^3 >= 4.

Claim B: Set n=bit_length(N), Rgrid=2^(4*n). Choose e uniformly from
{-n,...,n-1} and U uniformly from {0,...,Rgrid-1}; let
lambda=2^e*(1+U/Rgrid). A call to an exact integer SUPPORT oracle for
S at normal (lambda,1) returns a nontrivial factor point with probability
at least 1/(8*n*N^(1/3)). It is sufficient to count strictly interior
normal directions, so the oracle's tie convention need not favor P.

Declared dependencies: positivity and strict convexity of the real branch
xy=N, elementary integer-lattice geometry, and exact SUPPORT. No smoothness,
factor-balance, randomness-in-N, hull-size, or counting assumption is allowed.
Check arbitrary composites and unbalanced p,q. The claims supply no
quasipolynomial bound. They imply only a polynomial cost per call times
O(n*N^(1/3)) expected calls when an appropriate support implementation is used.

Separate implementation claim: support.py implements standard-Z^2 SUPPORT
in polynomial bit cost using Algorithm 2, Corollary 3.13, Theorem 3.14,
and Remark 1.6 of Alcantara--Blanco--Criado--Santos arXiv:2501.19193v1.
Its SEEK variation makes n+2 forward NEXTPT calls, stopping early at the
rightmost vertex, then reverses along true vertices until crossing its
integer x cutoff. Its SUPPORT binary-searches the coordinate range [1,N]
and retains every candidate before discarding a range. This implementation
claim is separate from the geometric probability claims.
