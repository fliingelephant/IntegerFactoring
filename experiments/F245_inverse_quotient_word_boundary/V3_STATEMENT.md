# F245 V3 candidate — a formal Las Vegas boundary for fresh inverse-quotient words and quadratic-torus trials

## Status and scope

This is a self-contained proof-only boundary for the restricted grammar
defined below.  It is not an all-input factoring algorithm.  It is not a
lower bound against biased or dependent integer sources, feedback from a
retained torus point, nonlinear carry words, or an unrestricted transcript
decoder.

Let

\[
N=pq,
\qquad
n=\lceil\log _2(N+1)\rceil,
\]

where `p` and `q` are distinct odd primes.  Put

\[
\Delta_N=\max_{1\le m<N^2}\tau(m).
\]

A *numerical quasipolynomial* is an integer-valued function bounded by

\[
2^{(\log_2(n+2))^C}
\tag{1}
\]

for one fixed constant `C`.  All integers used below have explicit binary
representations.  Reading, writing, multiplying, or powering by such an
integer is charged for all of its bits.  The grammar has no succinct
arithmetic-circuit representation of a longer exponent.

## 1. The restricted Las Vegas grammar

A run has a filtration `(\mathcal F_t)`.  The sigma-field `\mathcal F_t`
contains the full
public transcript, all earlier random values, every screen result, and every
control choice through step `t`.  Every fresh draw below has its stated exact
conditional law given the complete past.  A control choice can depend on the
past, subject to the stated chronology.

The only legal random sources, integer words, torus operations, gcd screens,
and factor-return rules are the following.

### 1.1 Exact unit draw and inverse-quotient bank

For one raw unit draw, sample `R` exactly uniformly from
`{0,...,N-1}` conditional on the past and compute

\[
g_R=\gcd(R,N).
\]

- If `1<g_R<N`, return `g_R` as a factor.
- If `g_R=N`, reject this raw draw.
- If `g_R=1`, accept `u=R` in `{1,...,N-1}`.

Thus an accepted `u` is exactly uniform on the canonical units conditional
on the complete past.  Let `v` be its least positive inverse modulo `N` and
store

\[
K(u)={uv-1\over N}\in\{0,\ldots,N-1\},
\qquad
\widehat K(u)=
\begin{cases}
K(u),&K(u)>0,\\
1,&K(u)=0.
\end{cases}
\tag{2}
\]

For stored values `K_i,K_j`, the bank also contains

\[
\Gamma_{ij}=
\begin{cases}
|K_i-K_j|,&K_i\ne K_j,\\
1,&K_i=K_j.
\end{cases}
\tag{3}
\]

At any later time, the run may select any stored positive values from
`{\widehat K_i}` and `{\Gamma_{ij}}`, with repetitions or positive integer
powers, and materialize their product `W_iq`.  The empty product is `1`.

### 1.2 Signed-power word and common-order lcm

The run may materialize

\[
W_{\rm sp}=\prod_{j=1}^{s}|N^{k_j}-\sigma_j|^{e_j},
\qquad
k_j,e_j\ge1,
\quad
\sigma_j\in\{+1,-1\},
\tag{4}
\]

including the empty product.  Its complete binary expansion is charged.

The grammar also grants exact common-order tokens.  A valid token `m` means
that, for one of the four sign pairs `(a,b)` in `{+1,-1}^2`, `m` is the exact
order of a point in each of the two cyclic groups of orders `p-a` and `q-b`.
Equivalently for the divisibility used here,

\[
m\mid p-a
\quad\hbox{and}\quad
m\mid q-b.
\tag{5}
\]

Tokens from different points and orientations may be accumulated as

\[
M=\operatorname{lcm}(m_1,\ldots,m_h),
\tag{6}
\]

with the empty lcm equal to `1`.  A token has no independent factor-return
rule and releases no hidden local order or sign.  Granting every valid token
only strengthens this restricted grammar.

Every powered trial uses a word of the exact form

\[
W=(N^2-1)^n W_{\rm sp}W_{\rm iq}M.
\tag{7}
\]

Before a powered trial, the run may apply `gcd(N,Z)` to `Z` equal to an
individual bank entry, any current product in (4) or (7), the lcm (6), or
the final exponent defined below.  A proper gcd is returned as a factor;
`1` and `N` do not return a factor.  No gcd of a sum, determinant, carry,
coordinate, or other integer transform is legal, except for the torus
screens explicitly defined below.

### 1.3 Discriminant draw and factor-free Hilbert--90 sample

For one raw discriminant draw, sample `D` exactly uniformly from
`{0,...,N-1}` conditional on the past and compute `g_D=gcd(D,N)`.
A proper value is returned as a factor, `g_D=N` is rejected, and `g_D=1`
accepts this `D`.  Put

\[
J=\left({D\over N}\right)\in\{+1,-1\}.
\tag{8}
\]

An accepted `D` may be retained for several coefficient draws.  Before each
raw coefficient draw, the run must fix, as an `\mathcal F_t`-measurable
integer,

\[
E=(N-J)W,
\tag{9}
\]

where `W` has the form (7).  In particular, `E` is fixed before the fresh
torus point that it will power.

Now sample `A,B` independently and exactly uniformly modulo `N`, conditional
on the past and on this fixed `E`.  Compute the coefficient screen

\[
c=\gcd(N,A,B).
\tag{10}
\]

A proper `c` is returned as a factor and `c=N` rejects the pair.  Otherwise
compute

\[
\nu=A^2-DB^2\pmod N,
\qquad
g_\nu=\gcd(\nu,N).
\tag{11}
\]

A proper `g_\nu` is returned as a factor and `g_\nu=N` rejects the pair.  On
`g_\nu=1`, invert `\nu` modulo `N` and form

\[
U={A+Bw\over A-Bw}
=x_0+x_1w,
\tag{12}
\]

where `w^2=D` and

\[
x_0=(A^2+DB^2)\nu^{-1},
\qquad
x_1=2AB\nu^{-1}\pmod N.
\tag{13}
\]

The inverse is therefore taken only after its norm is certified to be a
unit.  Subsequent products use only

\[
(x_0,x_1)(y_0,y_1)
=
(x_0y_0+Dx_1y_1,\ x_0y_1+x_1y_0)\pmod N.
\tag{14}
\]

The events in (10)--(11) are the *nonclean coefficient branch*.
An accepted `U` is the *clean branch*.

### 1.4 Exact clean powered trial and two-primary chain

For `Y=(y_0,y_1)`, define

\[
G_+(Y)=\gcd(N,y_0-1,y_1),
\qquad
G_-(Y)=\gcd(N,y_0+1,y_1).
\tag{15}
\]

Compute `V=U^E` by (14).  Apply `G_+(V)`.

- A proper value is returned as a factor.
- If `G_+(V)=1`, the powered trial is null.
- If `G_+(V)=N`, write `E=2^v e_0` with `e_0` odd.  Here `v>=1` because
  `N-J` is even.  For `j=0,...,v`, compute

  \[
  Y_j=U^{e_0 2^j}
  \tag{16}
  \]

  and apply both screens in (15).  Return the first verified proper value.
  If every screen is `1` or `N`, the trial is null.

The exponent `E` cannot change after `U` is drawn.  The only factor screens
applied to this `U` are (15)--(16).  A later control choice may use the past,
but every later integer word must still have the exact form (7), and every
later draw must retain its stated exact conditional law.  Thus coordinates,
powers, carries, and other transforms of this `U` are not new integer-word
sources.  A valid common-order token as in (5) is the sole allowed summary
of its order.  This is the no-current-point-feedback condition.

### 1.5 Exhaustive output rule

The run may continue after a rejection or a null trial.  It may halt with a
factor only through a proper gcd in Sections 1.1--1.4, and it verifies
`1<g<N` and `g|N` before returning.  No other arithmetic transform, gcd
argument, random source, oracle output, or factor-return path belongs to the
grammar.

A *confined Las Vegas factorer* is one fixed machine using only this grammar
which halts almost surely with a verified proper factor on every input in
its claimed class.  Its running time counts raw rejected draws and all bit
operations, not only accepted samples.

## 2. Exact inverse-quotient bounds

If `U` is uniform on the canonical units modulo `N`, every exact value of
`K(U)` has probability at most

\[
{\Delta_N\over\varphi(N)},
\tag{17}
\]

and every exact value of `\widehat K(U)` has probability at most

\[
{2\Delta_N\over\varphi(N)}.
\tag{18}
\]

For every prime `ell<N`, every residue class of `\widehat K` modulo `ell` has
mass at most

\[
\boxed{
\beta_{N,\ell}
={2\lceil N/\ell\rceil\Delta_N\over\varphi(N)}
<{8\Delta_N\over\ell}.
}
\tag{19}
\]

For two fresh bank values,

\[
\Pr(\ell\mid\widehat K_i)\le\beta_{N,\ell},
\qquad
\boxed{\Pr(\ell\mid\Gamma_{ij})\le\beta_{N,\ell}.}
\tag{20}
\]

These bounds hold history-wise.  If at most `B` accepted inverse seeds occur,
then for

\[
H_B=B+{B\choose2},
\tag{21}
\]

and every prime `ell<N`,

\[
\boxed{
\Pr(\text{some available bank entry is divisible by }\ell)
\le H_B\beta_{N,\ell}.
}
\tag{22}
\]

The selection, multiplicities, stopping rule, and later word choices may be
adaptive.

## 3. The explicit four-marker family

There is an absolute constant `c_0>0` and an infinite family of distinct
odd semiprimes `N=pq` with four distinct primes

\[
\lambda_+,\lambda_-,\rho_+,\rho_->2^{c_0n}
\tag{23}
\]

such that, for `a,b` in `{+1,-1}`,

\[
\lambda_a\mid p-a,
\qquad
\rho_b\mid q-b,
\tag{24}
\]

\[
\operatorname{ord}_{\lambda_a}(q)=\lambda_a-1,
\qquad
\operatorname{ord}_{\rho_b}(p)=\rho_b-1,
\tag{25}
\]

and

\[
\gcd(p-1,q-1)=2,
\quad
\gcd(p-1,q+1)=12,
\quad
\gcd(p+1,q-1)=2,
\quad
\gcd(p+1,q+1)=2.
\tag{26}
\]

One unconditional construction is sequential.  Choose the four markers in
comparable intervals and primitive residues modulo them.  Use one reduced
CRT class and Linnik's theorem to choose a prime `p` satisfying

\[
p\equiv13\pmod {24},
\quad p\equiv+1\pmod{\lambda_+},
\quad p\equiv-1\pmod{\lambda_-},
\tag{27}
\]

with `p` primitive modulo both rho-markers.  After fixing `p`, factor

\[
p^2-1=2^3 3^e\prod_{s\ge5}s^{e_s}.
\tag{28}
\]

Use a second reduced CRT class and Linnik to choose a prime `q` satisfying

\[
q\equiv3\pmod8,
\qquad
q\equiv2\pmod {3^{\max(e,2)}},
\qquad
q\equiv\pm1\pmod{\rho_\pm},
\tag{29}
\]

and, for every `s^{e_s}` in (28) with `s>=5`, choose a unit residue modulo
`s^{e_s}` whose reduction is neither sign.  At a lambda-marker, choose a
lift whose reduction is primitive.  The rho-markers do not divide `p^2-1`,
so all second-stage moduli are coprime.  This gives (24)--(26), in fact

\[
\gcd(p^2-1,q^2-1)=24.
\tag{30}
\]

Both Linnik moduli are polynomial in the marker scale and the first chosen
prime.  Hence the marker scale and `N` have logarithms within constant
factors, which gives (23).

For every fixed numerical quasipolynomial `Q`, every sufficiently large
member of this family has the following deterministic property.  Every
nonzero signed-power word (4) of binary length at most `Q(n)` satisfies

\[
\gcd(W_{\rm sp},\lambda_+\lambda_-\rho_+\rho_-)=1.
\tag{31}
\]

The same is true of `(N^2-1)^n`.  Also, for each orientation `(a,b)`, neither
`lambda_a` nor `rho_b` divides `N-ab`.

Every valid common-order lcm in (6), even when tokens come from all four
orientations, satisfies

\[
\boxed{M\mid12.}
\tag{32}
\]

## 4. Exact torus law and exhaustive cutoff bound

For an accepted discriminant, put

\[
a=\left({D\over p}\right),
\qquad
b=\left({D\over q}\right),
\qquad
J=ab.
\tag{33}
\]

The two local norm-one groups are cyclic of orders

\[
m_p=p-a,
\qquad
m_q=q-b.
\tag{34}
\]

Conditional on the clean branch (11), the two reductions of (12) are
independent uniform elements of these full groups.  This includes `+1` and
`-1`.  For the exponent (9), fixed before the clean point, the local return
probabilities are exactly

\[
{\gcd(E,m_p)\over m_p},
\qquad
{\gcd(E,m_q)\over m_q}.
\tag{35}
\]

Every factor returned by (15)--(16) implies at least one of these two local
return events.

For completeness, put

\[
h_p=\min(v_2(m_p),v_2(E)),
\qquad
h_q=\min(v_2(m_q),v_2(E)),
\]

and let `a_2=min(h_p,h_q)` and `b_2=max(h_p,h_q)`.  Conditional on the
global return `U^E=1` on both sides, the chain (16) returns a factor exactly
when the two local two-primary exact orders differ.  Its exact conditional
success probability is

\[
\mu_{a_2,b_2}
=1-{4^{a_2}+2\over3\,2^{a_2+b_2}}
\ge {1\over2}.
\tag{36}
\]

Here `a_2>=1` because both local group orders and `E` are even.

Let

\[
L=\min(\lambda_+,\lambda_-,\rho_+,\rho_-).
\tag{37}
\]

Stop any confined run after `B>=1` bit operations.  Then it has made at most
`B` raw draws, accepted seeds, clean trials, screens of each type, and
explicit word operations.  For every sufficiently large family member for
which `B` is numerical quasipolynomial in `n`, the probability that the
stopped run returns any factor is at most

\[
\boxed{
48H_B{\Delta_N\over L}
+4B\left({1\over p}+{1\over q}\right)
+{2B\over L}.
}
\tag{38}
\]

The first term covers every bank incidence at any of the four markers or the
two hidden factors.  It therefore also covers every legal direct word-gcd
factor.  The second term covers all raw unit, discriminant, coefficient, and
norm screens.  The last term covers every clean powered and Miller-chain
factor event.  Common-order tokens have no factor exit, and (31)--(32) make
all other legal word gcds equal to `1` on the complement of the bank event.
Thus (38) exhausts every factor-return rule in Section 1.

The standard divisor estimate gives

\[
\Delta_N=2^{o(n)}.
\tag{39}
\]

Together with (23), equation (38) is `2^{-Omega(n)}` for every numerical-QP
cutoff `B`.

Consequently, no confined Las Vegas factorer has expected numerical-
quasipolynomial running time on all members of this infinite family.  If its
expected time were at most `Q(n)`, Markov's inequality would make it return
within `2Q(n)` operations with probability at least `1/2`, while (38) makes
that probability exponentially small.

## 5. Exact Hilbert--90 carry identities outside the grammar

Let `w^2=D`, take public signed integers `a_0,b_0`, and put

\[
g=a_0^2-Db_0^2,
\qquad
A_0=a_0^2+Db_0^2,
\qquad
B_0=2a_0b_0.
\]

Assume `g` is nonzero and coprime to `N`.  Let `v` be the least positive
inverse of `g` modulo `N`, and set

\[
X=\langle A_0v\rangle_N,
\qquad
Y=\langle B_0v\rangle_N,
\]

\[
\widetilde d={gv-1\over N},
\qquad
q_A={A_0v-X\over N},
\qquad
q_B={B_0v-Y\over N}.
\]

Then

\[
\boxed{
k={gX-A_0\over N}=A_0\widetilde d-gq_A,
\qquad
l={gY-B_0\over N}=B_0\widetilde d-gq_B.
}
\tag{40}
\]

The canonical norm carry is

\[
\boxed{
{X^2-DY^2-1\over N}
={2(A_0k-DB_0l)+N(k^2-Dl^2)\over g^2}.
}
\tag{41}
\]

These identities hold for signed and noncanonical `g`.  Their products,
squares, and quotient carries are not legal bank entries in Section 1 and
do not inherit (19)--(22).

## Exact remaining gap

The theorem closes only the formal grammar above.  It does not cover a
history-dependent nonuniform unit seed, inverse-quotient descent, a word
chosen from the current torus point, canonical high digits, cross-coordinate
determinants, norm carries, higher quotient digits, biased discriminants, or
a decoder that uses the full relation transcript without first entering one
of the listed gcd screens.
