# F161 candidate — factor-first relative-order growth for released blocks

## Status and scope

This is a proof-only decoder and progress candidate. It extends the F159 V2
post-refinement test from one exponent to a bounded relative-order scan. The
closest certified-order result is P144/F158.

The new result is conditional on a public released unit `d`. It gives an exact
outcome:

\[
\boxed{
\text{factor}
\quad\lor\quad
\text{old diagonal subgroup}
\quad\lor\quad
\text{larger certified common cyclic subgroup}
\quad\lor\quad
\text{every local relative order exceeds the cap}.}
\]

It does not construct a useful `d`. It does not prove an all-input source law
or a factoring algorithm.

Let `N>=3` be odd. For the proof only, write its unknown prime-power CRT
decomposition as

\[
N=\prod_{j=1}^s R_j,
\qquad
R_j=p_j^{\alpha_j},
\tag{0}
\]

where the `p_j` are distinct odd primes. This notation is not input to the
algorithm. Put

\[
n=\lceil\log_2(N+1)\rceil.
\]

Let `B>=2` be a public integer with

\[
B\le 2^{C(\log_2(n+1))^k}
\tag{1}
\]

for fixed constants `C,k`.

## 1. Certified common-order input

Let `M>=1` have a supplied complete prime factorization. Assume every prime
factor of `M` is at most `B`. First compute `gcd(M,N)`. If it is proper,
return it. Under a valid common-order state `M<N`, so on the surviving
branch

\[
\gcd(M,N)=1.
\tag{1a}
\]

Let `g` be a public unit with

\[
g^M\equiv1\pmod N
\tag{2}
\]

and

\[
\gcd(g^{M/\ell}-1,N)=1
\qquad(\ell\mid M,\ \ell\text{ prime}).
\tag{3}
\]

Then

\[
\operatorname{ord}_{R_j}(g)=M
\qquad(1\le j\le s).
\tag{4}
\]

Write

\[
H_j=\langle g\bmod R_j\rangle.
\]

For a public unit `d`, define its local relative order by

\[
e_j(d)=\operatorname{ord}_{(\mathbf Z/R_j\mathbf Z)^\times/H_j}(dH_j).
\tag{5}
\]

Thus `e_j(d)` is the least positive integer `e` for which
`d^e mod R_j` belongs to `H_j`.

## 2. Exact bounded relative-order scan

For `e=1,2,...,B`, in this order, compute

\[
D_e=\gcd(d^{eM}-1,N).
\tag{6}
\]

Stop at the first `D_e` that is not one.

When a common return `D_e=N` occurs, first compute `gcd(e,N)`. If it is
proper, return it. On the surviving common-return branch,

\[
\gcd(e,N)=1.
\tag{6a}
\]

Exactly one of the following occurs.

1. **Factor.** A state, cap, or scan gcd is proper. Return it.
2. **Common return.** The first non-one value is `D_e=N`. Then

   \[
   e_j(d)=e
   \qquad(1\le j\le s).
   \tag{7}
   \]

3. **Beyond the cap.** Every `D_e` is one. Then

   \[
   e_j(d)>B
   \qquad(1\le j\le s).
   \tag{8}
   \]

In the common-return case, put `x=d^e mod N`. A factor-first
Pohlig--Hellman calculation, stated in Section 3, returns either a proper
factor of `N` or the unique aligned exponent

\[
x=d^e\equiv g^a\pmod N,
\qquad 0\le a<M.
\tag{9}
\]

If `e=1`, equation (9) proves

\[
d\in\langle g\rangle
\tag{10}
\]

in the global diagonal subgroup.

If `e>=2`, equation (9) proves that

\[
K=\langle g,d\rangle
\tag{11}
\]

is cyclic of exact order

\[
L=Me
\tag{12}
\]

globally and in every hidden prime-power component. A public deterministic
two-dimensional Smith construction then returns a certified common-order
generator `(h,L)` with

\[
K=\langle h\rangle,
\qquad
\operatorname{ord}_{R_j}(h)=L
\quad(1\le j\le s).
\tag{13}
\]

The complete prime factorization of `L` is obtained from the supplied
factorization of `M` and deterministic trial division of `e`. Every prime
factor of `L` is at most `B`.

## 3. Factor-first Pohlig--Hellman alignment

The alignment subroutine has the following exact interface.

**Input.** A certified pair `(g,M)`, the supplied prime factorization

\[
M=\prod_i\ell_i^{c_i},
\]

and a public unit `x` with

\[
x^M\equiv1\pmod N.
\tag{14}
\]

**Output.** Either a proper factor of `N`, or the unique `a mod M` for which

\[
x\equiv g^a\pmod N.
\tag{15}
\]

For each prime power `ell^c` dividing `M`, put

\[
m=M/\ell^c,
\qquad
G=g^m,
\qquad
X=x^m,
\qquad
H=G^{\ell^{c-1}}.
\]

Suppose the lower digits

\[
A_j=\sum_{t<j}b_t\ell^t
\]

are known. Compute

\[
Y_j=(XG^{-A_j})^{\ell^{c-1-j}}.
\tag{16}
\]

For `b=0,...,ell-1`, test

\[
\gcd(Y_j-H^b,N).
\tag{17}
\]

If the hidden base-`ell` digits are not all equal, one of these gcds is
proper. If they agree, exactly one test equals `N`, and it gives `b_j`.
After all digits are aligned, ordinary integer CRT gives `a mod M`.

The subroutine uses at most

\[
\sum_i c_i\ell_i
\le B\log_2 M
\tag{18}
\]

gcd tests and modular exponentiations.

## 4. Public common-generator procedures

Assume `e>=2` and equation (9) holds. Put `L=Me`. The presentation theorem
below implies

\[
\gcd(M,a,e)=1.
\tag{18a}
\]

### 4.1 Deterministic Smith word

Let

\[
E_0=\prod_{\substack{\ell\mid e,\ \ell\text{ prime}\\ \ell\nmid M}}\ell.
\]

Use ordinary integer CRT to choose `s` with

\[
s\equiv a\pmod M,
\qquad
s\equiv1\pmod {E_0}.
\tag{19}
\]

Equation (18a) gives `gcd(s,e)=1`. Extended Euclid returns `u,v` with

\[
ue+vs=1.
\tag{20}
\]

Then

\[
h=g^u d^v\pmod N
\tag{21}
\]

has exact order `L` globally and in every hidden component. This is an
explicit two-by-two Smith-normal-form generator. Negative exponents use
public modular inverses.

Verify `h^L=1 mod N`. For every prime `ell` dividing `L`, verify

\[
C_\ell=\gcd(h^{L/\ell}-1,N)=1.
\tag{22}
\]

These equalities give the next public common-order certificate.

### 4.2 Optional Las Vegas word sampler

There is also a presentation-free public sampler. Repeatedly choose

\[
u,v\ \stackrel{\$}{\leftarrow}\ \{0,1,\ldots,L-1\},
\qquad
h=g^u d^v\pmod N.
\tag{23}
\]

Test the order screens in (22), with this priority rule.

1. If some `C_ell` is proper, return it as a factor.
2. If every `C_ell=1`, return `(h,L)`.
3. Otherwise reject `h` and sample again.

On a no-factor run, `h` is uniform in the cyclic group `K`, so one trial
succeeds with probability

\[
\frac{\varphi(L)}L.
\tag{24}
\]

Moreover,

\[
\frac L{\varphi(L)}\le\omega(L)+1\le\log_2L+1,
\tag{25}
\]

where `omega(L)` is the number of distinct prime factors of `L`. Thus the
sampler terminates almost surely and uses at most `log_2 L+1` trials in
expectation. The deterministic construction in Section 4.1 is stronger and
is the default updater.

## 5. Why alignment is necessary

Equal local relative orders do not by themselves give a global cyclic
extension. The logarithms in equation (9) must also align.

Take

\[
N=91=7\cdot13,
\qquad
g=90=-1,
\qquad
M=2,
\qquad
d=30.
\]

Then

\[
D_1=D_2=1,
\qquad
D_3=91,
\]

so both local relative orders are three. But

\[
d^3\equiv64\pmod{91},
\]

which equals `1` modulo 7 and `-1` modulo 13. Therefore

\[
\gcd(d^3-1,91)=7,
\qquad
\gcd(d^3+1,91)=13.
\tag{26}
\]

The factor-first logarithm calculation detects this mismatch.

For comparison, `d=17` on the same `(N,g,M)` has

\[
D_1=D_2=1,
\qquad
D_3=91,
\qquad
17^3\equiv-1=g\pmod{91}.
\tag{27}
\]

It gives aligned growth from common order 2 to common order 6. The element
`17` itself certifies the new order because

\[
\gcd(17^3-1,91)=1,
\qquad
\gcd(17^2-1,91)=1.
\tag{28}
\]

These examples are finite certificates only.

The other scan outcomes also occur on small exact inputs. For

\[
(N,g,M,d)=(35,-1,2,2),
\]

the scan gives `D_1=1` and `D_2=5`, so it factors. For

\[
(N,g,M,d,B)=(77,-1,2,2,2),
\]

it gives `D_1=D_2=1`; the two local relative orders are three and five,
so both exceed the cap. No asymptotic claim follows from these examples.

## 6. Quasipolynomial cost and monotone iteration

The scan has `B` modular exponentiations and gcds. All exponents have
`O(n+log B)` bits. The alignment cost is bounded by (18). Factoring
`e<=B` by trial division is quasipolynomial. The Smith generator uses
integer CRT, extended Euclid, modular exponentiation, and the public order
screens. Thus one updater call has deterministic bit complexity bounded by
a fixed quasipolynomial in `n`. The optional random sampler has the same
expected bound.

Suppose a sequence of supplied blocks gives `t` successful growth outcomes

\[
M_i=M_{i-1}e_i,
\qquad e_i\ge2.
\]

Then `M_t` divides every component group order `phi(R_j)`, and consequently

\[
2^tM_0
\le M_t
\le\gcd_{1\le j\le s}\varphi(R_j)<N.
\tag{29}
\]

Hence

\[
t<n.
\tag{30}
\]

Every successful state keeps a known `B`-smooth order factorization. A
sequence of successful updater calls therefore has deterministic
quasipolynomial total cost.

This bound counts only successful growth calls. It gives no bound on the
number of inert blocks or blocks whose local relative orders exceed `B`.

## 7. Exact boundary

F159 V2 classifies only `gcd(d^M-1,N)`. F161 scans all relative orders up
to a quasipolynomial cap, aligns the hidden logarithms without knowing the
factors, and compresses an aligned two-generator subgroup back to one
certified common-order generator.

The updater resolves three possible flaws inside that decoder step:

1. equal local relative indices are insufficient without log alignment;
2. after alignment, cyclicity follows from the exact shared presentation;
3. a common generator can be constructed publicly and deterministically.

It does not resolve the source problem. No theorem here says that F154,
F156, or another public process supplies a block with relative order at
most `B`. No theorem says repeated released blocks avoid the inert and
beyond-cap outcomes.

The decoder theorem covers every odd CRT decomposition, including prime
powers and more than two distinct primes. An even factor can be removed
before it is called. This broader decoder scope does not solve the source
problem or the recursion needed for complete factorization. Therefore F161
is not a quasipolynomial factoring algorithm.
