# Small-remainder reciprocity and arithmetic path traces

**Family:** route:F31

The question is whether the unusually short F328 paths belong to a public
arithmetic family with a useful probability under fresh square inputs. The
closest result is F328/SHORT_PATHS.md, which gives only the two endpoint
identities at remainder +1 or -1. This packet extends the identity to every
signed remainder and records the actual branch words of three short paths.
The identities below are candidate elementary results, not independently
reconstructed results and not a short-path probability theorem.

## Exact identity to check

Let N>1 be odd, h=(N-1)/2, gcd(a,N)=1, and 1<=t<=h. Let b be the inverse
of a modulo N, and let rep choose [-h,h]. Set

    Q(t) = #{1<=y<=t : 1<=a*y mod N<=h},
    C_t(u,v) = #{k in [u,v] : 1<=b*k mod N<=t-1}.

An empty interval has count zero. Write r=rep(a*t), which is nonzero.
The proposed exact formulas are

    r>0:  2*Q(t) = t+1 + C_t(1,r-1) - C_t(h+1,h+r),
    r=-s<0: 2*Q(t) = t-1 + C_t(h+1-s,h) - C_t(N-s+1,N-1).

In particular, |2*Q(t)-t|<=|r|. This costs at most 2*|r|-1 inverse-image
tests after b is known. It requires no factorization or Jacobi promise.
The experiment must compare with direct enumeration, not reuse the same
formula on both sides. The r=+1 and r=-1 cases must separately reproduce
ceil(t/2) and floor(t/2).

## Exact finite pilot

Use every odd N from 3 through 101, every a in [1,N-1] coprime to N, and
every t in [1,h]. Check the two identities, the discrepancy bound, and the
two unit-remainder special cases. Prime factors may be used only as offline
labels if a discrepancy occurs. Reuse a precomputed direct residue prefix
and sorted inverse-image prefixes to keep this comfortably bounded.

Reproduce these frozen public tuples using F326's unchanged implementation:

| N | a | Auxiliary | Cap | Expected F endpoint call |
| --- | --- | --- | --- | --- |
| 209407403 | 71556651 | rank_reflection | 32 | 7 |
| 209407403 | 6998896 | delete_adjacent | 32 | 31 |
| 170611297 | 49354795 | rank_reflection | 32 | 25 |

Retain every visited current coordinate, its modular inverse when it exists,
F image and branch, image rank, next coordinate, and exact Q/rank/select
counts. For each nonterminal reflection step also retain the auxiliary's
affine rule:

- Negative F image -y: next=Q(y)=(y+e)/2, e=2*Q(y)-y.
- Positive F image z<=L: next=-y, Q(y)=z, e=2*z-y, next=-2*z+e.
- Positive F image z>L: next=d-z.
- Image 0: next=0.

The solver receives only N, a, auxiliary name, and cap. Any retained F328
private roots or factors are validation labels and cannot choose its steps.
Use a plain named Python source with a 30 second external timeout and
256 MB peak-memory target. Estimate runtime below three seconds. Refresh
load and memory checks first, and wait until the root's F329 numerical work
has cleared. Preserve source, log, output JSON, and source/input hashes.
Report the pilot before any extension.

## Scope

These finite checks do not establish that the selected seeds are frequent.
They test a general algebraic identity and explain already retained paths.
Any later public filter must charge every rejected input and preserve the
hidden-root independence required by P02.

## Follow-on design: the constant a=-1 family

Do not execute before reporting the first pilot. PROOF.md, Section 3 gives
an exact specialization for N=1 mod 4:

    D={0,...,(N-1)/2}, F(x)=abs(rep(inverse(x))) away from 0,1,
    next=(N+1)/2-F(x), z=2*x-1, z_next=sigma*4/(z+1) mod N,
    sigma=-sign(rep(inverse(x))).

Retain the fixed-point check and original P246 decoder before each move.
This variant has no Q, floor-sum, rank, or selection calls after setup.
Use an independent specialized implementation and compare every step with
the frozen GaussPairing for all N=1 mod4 through 501. It suffices to compare
the complete path from zero, including its terminal factor-or-root result.
Also check the integer-lift recurrence (U,V)->(4*sigma*V,U+V), starting at
(-2,1) after the first moving stage. Check z=U/V modN only while V is a
unit. Keep only a bounded trace, not exponentially many paths.

If the pilot is correct, run all retained F328 moduli satisfying the public
condition N=1 mod4, once each, with a=N-1 and cap 8192. Also retain prefixes
at 32,128,512,2048. This is seven moduli from 20 through 92 bits, at most
57,344 modular inversions and no floor-sum loops. Expected runtime under
three seconds and memory under 64 MB without the optional integer lift; the
same external 30-second timeout and 256 MB boundary apply. Scale first on
the 20/28/36-bit inputs, and ask the route's Astra to interpret those data
before the remaining inputs.

For each path retain verified factor, valid root, or cap censor; branch-sign
counts, the longest constant-sign run, modular-inversion count, wall time,
and the first 64 sign/coordinate rows. Offline factors label whether -1 is a
square; they cannot select any step, cap, or continuation. A valid root of
-1 is not counted as a factor. This is a public nonrandom parameter family,
not a private-root P02 experiment. No general success estimate is inferred
from it.
