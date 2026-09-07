# Rabin input mode and attempt cost

**Family:** route:F31

This is an application of the existing P02 hidden-root reduction. It is not
a new square-root algorithm or a proved speedup for the F326 path.

The discussion after Lemma 3.3 in the cached Jeřábek paper requires a search
reduction to handle even oracle answers correlated with the reduction's
private coins. Our algorithmic goal permits an actual subroutine whose inputs
and random coins are controlled. P02 therefore applies directly; the stronger
oracle convention is not an additional requirement on this route.

For odd N with at least two distinct prime divisors, draw r uniformly from
{1,...,N-1}. Return a proper gcd with N immediately. Otherwise r is a uniform
unit, and a=r^2 mod N is uniform among unit squares. Run the F326 procedure
with N,a and public limits, without giving it r. Auxiliary matching choices
must also depend only on N,a and independent coins. Verify every returned
factor or square root. A valid root c is decoded by gcd(c-r,N).

By P02, conditioned on any valid root output, this gcd is proper with
probability 1-2^(1-s)>=1/2, where s is the number of distinct primes in N.
The statement includes repeated prime exponents. The root need not itself
be sampled uniformly, and the procedure may return failure on other calls.

Suppose, for this fixed N, that over uniform unit-square inputs the procedure
has valid-output probability delta(N) and finite expected bit cost tau(N).
Writing u for the probability that the initial nonzero r is a unit, the
whole attempt has success probability at least

    (1-u)+u*delta(N)/2 >= delta(N)/2.

Its expected cost is at most poly(bitlength(N))+tau(N). Independent retries
therefore have expected cost at most

    2*(poly(bitlength(N))+tau(N))/delta(N).

This is a sufficient average-over-random-squares contract for EACH N; it
does not require a uniform bound on every a with Jacobi(a,N)=+1. Prime
testing, even removal, exact perfect-power roots, and recursive verified
splitting supply the standard all-input wrapper if the ratio is uniformly
quasipolynomial. No such ratio is proved for the current F326 procedure.

Private-root independence is essential. The pilot must not pass r to the
path algorithm or use r to select its matching, limits, or node proposals.
The root may be retained only by the outer input generator and final decoder.
Uniformity and independence here are mathematical fair-bit requirements;
seeded numerical trials are finite reproducibility evidence.
