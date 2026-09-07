# F303 universal unit products and power sums

**Scoped result:** for M=2^k and requested precision P, the product of the
canonical odd integers below M modulo2^P, and their fixed-degree positive
and inverse power sums to that precision, have a deterministic algorithm
polynomial in k,P and the degree. No inverse graph is enumerated.

This is an elementary construction from Faulhaber and Newton identities,
not an external novelty claim. All divisions and operand lengths below
are part of the algorithm.

## Product without an M-length loop

For M>=4, put J=M/4. The odd units are exactly

    {1+4j:0<=j<J} union {3+4j:0<=j<J}.

Let e_l be the elementary symmetric polynomial of degree l in0,...,J-1,
and p_l=sum_{j=0}^{J-1}j^l. Compute only l<=h, with h=floor((P-1)/2).
The recurrences are

    p_0=J,
    p_l=(J^(l+1)-sum_{v=0}^{l-1}binom(l+1,v)*p_v)/(l+1),
    e_0=1,
    e_l=(1/l)*sum_{v=1}^l(-1)^(v-1)*e_(l-v)*p_v.

The divisions are exact integer divisions. If l>J, the elementary
symmetric coefficient is zero; alternatively handle J<h directly.
For a=1,3, the exact product expansion gives

    product_{j<J}(a+4j)
      =a^J*sum_{l=0}^{J}e_l*4^l*a^(-l).

Modulo2^P, terms with2l>=P vanish because e_l is integral and a is odd.
Thus each product is obtained from h+1 terms and one modular exponentiation
a^J. The two products give

    P_M=product_{u odd<M}u mod2^P.                      (1)

The exponent J has only O(k) bits. It is not expanded into J multiplications.
The full integer P_M, which would have exponentially many bits in k, is
never constructed.

## Positive and inverse power sums

Write U_s=sum_{u odd<M}u^s. For s>=0, ordinary binomial expansion on the
two progressions computes U_s exactly from p_0,...,p_s.

For j>=1, use the convergent2-adic binomial series

    (a+4v)^(-j)
      =a^(-j)*sum_{l>=0}(-1)^l*binom(j+l-1,l)*(4v/a)^l.

To precision2^P only l<=floor((P-1)/2) is needed. Summing over v gives

    U_(-j)=sum_{a in{1,3}} sum_{l=0}^h
      (-1)^l*binom(j+l-1,l)*4^l*a^(-j-l)*p_l mod2^P.   (2)

These inverse powers are2-adic values of rational numbers with odd
denominators. They are not being approximated in the real metric.

## Bit costs

There are O(P^2) integer operations for the p_l,e_l recurrences. Bounds
p_l<=J^(l+1) and e_l<=J^(2l) show that their exact operands have
O(P*k+P*log(P+1)) bits. The modular exponentiations use polynomially many
P-bit operations. Computing(2) through degree d adds polynomially many
operations in d,P,k; its binomial coefficients have polynomial bit length.

Thus the result is polynomial in the requested degree, not merely in the
binary encoding length of an arbitrarily enormous degree. In particular,
degrees polynomial in k remain within polynomial bit cost. M=2 and the
other fixed small cases are direct computations.

The guard precision needed when these sums are divided by jM is described
in REPORT.md. No division by an even number is treated as a modular inverse.

## Implementation evidence and comparison status

`moment_precision.py` implements(1),(2) directly. Small cases compare them
with explicit products and inverse power sums. Larger cases use only the
polynomial-size formulas:

| k | Working bits | Symmetric truncation degree | Largest exact intermediate bits | Preparation/evaluation seconds |
|---:|---:|---:|---:|---:|
|32|98|48|2630|about0.001|
|64|194|96|11310|about0.023|
|128|386|192|47008|about0.80|

The large cases enumerate zero units. They are evaluations of the proved
finite formulas, not independent brute-force validations at those sizes.

A focused primary search found related higher-Wilson congruence work using
Newton identities and quotient power sums: [Kellner, arXiv:2509.05235](https://arxiv.org/abs/2509.05235).
Only its abstract was checked; no theorem from it is used here and a full
comparison with that paper has not been completed. The later SOURCE_LEADS.md
identifies Andreica2013's published non-enumerative power-sum/Newton
algorithm for this odd product. The elementary product construction and
the mixed-moment identities in this packet carry no novelty claim.
