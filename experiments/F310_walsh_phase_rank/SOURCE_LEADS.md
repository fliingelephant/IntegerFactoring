# Source leads for Boolean Walsh aggregation over `Z/2^k`

These sources are leads, not dependencies of the finite rank experiment.
No paper located here supplies the requested inverse-graph coefficient.

## Local boundary

`experiment:F293_carry_convolution` and
`experiments/F293_carry_convolution/RESULT.md` identify the same half-window
correlation as a coefficient of a cyclic square with `2^(k-2)` signs. The
coefficient retains phase. Replacing the square by an autocorrelation loses
the window placement.

## Primary cryptographic leads

1. Liu Yan, Hu Bin, and Xu Liping, "Efficient algorithm for computing Walsh
   spectrum and differential probability," *Journal on Communications* 36(5),
   2015, DOI `10.11959/j.issn.1000-436x.2015112`.
   <https://www.joconline.com.cn/rc-pub/front/front-article/download/59693231/lowqualitypdf/T%E5%87%BD%E6%95%B0Walsh%E8%B0%B1%E5%80%BC%E4%B8%8E%E5%B7%AE%E5%88%86%E8%BD%AC%E7%A7%BB%E6%A6%82%E7%8E%87%E5%BF%AB%E9%80%9F%E7%AE%97%E6%B3%95.pdf>

   For a `w`-narrow T-function, the paper writes a requested Walsh coefficient
   as a product of bit-transition matrices. Its stated arithmetic cost is
   `O(2^(2.3723639 w) n)`. This is polynomial when a presentation has bounded
   or logarithmic narrowness. The paper explicitly says that multiplication
   has input-length-dependent, difficult narrowness and that the method then
   gives no useful reduction. It does not analyze modular inversion.

2. Chang Yaqin and Jin Chenhui, "Fast Computation of Walsh Spectrum of Affine
   Function over the Ring Z/2n," *Journal of Shanghai Jiaotong University*
   45(3), 2011, 321-326.
   <https://xuebao.sjtu.edu.cn/CN/abstract/abstract39582.shtml>

   The official abstract claims a carry-based linear-time algorithm for affine
   and multi-output affine maps over the residue ring `Z/2^n`. The present map
   is fractional-linear, so this result covers only possible affine substeps.

3. A. Mahmoodi Rishakani, S. M. Dehnavi, M. R. Mirzaee Shamsabad,
   Hamidreza Maimani, and Einollah Pasha, "Statistical Properties of
   Multiplication mod 2^n."
   <https://iacr.steepath.eu/2015/201-StatisticalPropertiesofMultiplicationmod2n.pdf>

   The paper derives joint distributions for selected component bits of a
   two-input multiplication-like T-function when both inputs are uniform.
   The Walsh target here conditions on the single hyperbola `u*v=N`.
   Averaging all multiplication fibers does not preserve that correlation.

## Explicit exclusions

Finite-field inverse Walsh spectra concern `GF(2^k)`, not the ring
`Z/2^k`. Ordinary Kloosterman and Artin-Schreier-Witt sums use additive
characters. The top-bit square wave is not an additive character of
`Z/2^k`: carries can flip the top bit while both factors of the proposed
character remain positive. No applicable Artin-Schreier-Witt complexity
theorem was located.

For odd `u=1+2x`, write `N/u=1+2F_N(x)`. Then

    F_N(x)=((N-1)/2-x)/(1+2x) mod 2^(k-1).

The target is one vectorial Walsh coefficient of this T-function. The
concrete source-side question is whether `F_N` has a uniformly logarithmic
narrow presentation or another bounded transition state. None of the sources
above proves one.
