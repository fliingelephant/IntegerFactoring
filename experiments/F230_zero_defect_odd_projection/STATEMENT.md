# F230 candidate — zero-defect quotient children give an odd-order Las Vegas progress dichotomy

## Status and boundary

This is a proof-only favorable-state theorem.  It repairs the zero-defect
branch found by the hostile F228 audit and gives an exact sparse-source
boundary outside that state.  It is not an all-input factoring algorithm.

Let

\[
N=pq,
\qquad p<q<2p,
\qquad n=\lceil\log_2(N+1)\rceil,
\qquad B=2^{\lfloor n/2\rfloor},
\]

where `p` and `q` are distinct odd primes.  For an odd integer `u` with
`1<=u<B`, write

\[
uN=Q_uB+R_u,
\qquad 0<R_u<B,
\]

and, for an integer shift `c`, put

\[
A_{u,c}=Q_u+c,
\qquad E_{u,c}=u-R_u+cB.
\]

## Theorem A — exact zero-defect classification

For the stated range `1<=u<B`,

\[
\boxed{
E_{u,c}=0
\quad\Longleftrightarrow\quad
B\mid N-1\ \hbox{ and }\ c=0.
}
\tag{1}
\]

In that branch define

\[
H={N-1\over B}.
\tag{2}
\]

Then every zero-defect quotient child has the exact form

\[
R_u=u,
\qquad Q_u=uH,
\qquad A_{u,0}=uH.
\tag{3}
\]

Thus random small multipliers do not create independent `N`-dependent
children.  They expose one public half-size integer `H` and multiply it by
known small integers.  The integer `H` has at most `ceil(n/2)` bits.  Once
`H` is completely factored, every `uH` in a numerical-QP multiplier bank is
completely factored after a numerical-QP sieve for the multipliers.

For general odd `u=v+kB`, where `0<v<B`, the exact extension is

\[
E_{u,c}=0
\quad\Longleftrightarrow\quad
B\mid N-1\ \hbox{ and }\ c=-k,
\]

and again `A_{u,c}=uH`.  The rest of the theorem uses `u<B`, so the unique
zero shift is `c=0`.

## Theorem B — exact odd local-return law

Let

\[
P=(p-1)_{\rm odd},
\qquad Q=(q-1)_{\rm odd},
\qquad D=\gcd(P,Q),
\]

and define the coprime residual odd orders

\[
s_p={P\over D},
\qquad s_q={Q\over D},
\qquad \gcd(s_p,s_q)=1,
\qquad S=\operatorname{lcm}(s_p,s_q)=s_ps_q.
\tag{4}
\]

The residual annihilator `S` is hidden.  The algorithm neither computes nor
enumerates it.  Although `SH` annihilates every projected base, `S` can be
exponential.  The favorable theorem below needs only one of its two coprime
factors to lie in the public bank.

In the zero-defect branch,

\[
\gcd(H,P)=\gcd(H,Q)=D.
\tag{5}
\]

Choose `x` uniformly from the units modulo `N` and put

\[
a=x^{2^n}\pmod N.
\tag{6}
\]

The two CRT coordinates of `a` are independent and uniform in the odd-order
subgroups of orders `P` and `Q`.  For every fixed odd `u`, the exact local
return probabilities for the factored exponent `A=uH` are

\[
\alpha_p(u)
=\Pr(a^{uH}=1\bmod p)
={\gcd(u,s_p)\over s_p},
\]

\[
\alpha_q(u)
=\Pr(a^{uH}=1\bmod q)
={\gcd(u,s_q)\over s_q}.
\tag{7}
\]

Consequently,

\[
\Pr\bigl(1<\gcd(a^{uH}-1,N)<N\bigr)
=\alpha_p+\alpha_q-2\alpha_p\alpha_q,
\tag{8}
\]

and

\[
\Pr(a^{uH}=1\bmod N)=\alpha_p\alpha_q.
\tag{9}
\]

These formulas are exact.  They include arbitrary prime powers in `P`,
`Q`, `D`, `s_p`, and `s_q`.

## Theorem C — favorable-state Las Vegas progress

Assume a complete factorization of `H` is available.  Let `U=U(n)` be a
public numerical-QP integer with `U<B`.  Maintain an odd certified common
divisor

\[
M\mid D.
\]

One multiplier-bank stage does the following.

1. Sieve the public multiplier bank and screen every `gcd(u,N)`.  A proper
   value is an immediate factor.
2. Choose `x` uniformly from `1,...,N-1`.  A nontrivial
   `gcd(x,N)` is an immediate factor.  Otherwise form `a` by (6).
3. For every odd `1<=u<=U`, compute
   `g=gcd(a^(uH)-1,N)`.
4. Return a proper `g`.  If `g=N`, use the complete factorization of `uH`
   to strip redundant prime powers.  Return any factor found during
   stripping.  Otherwise accumulate every certified common primary block.
5. A global return whose stripped block is already contained in `M` is not
   a stopping event.  Continue through the bank.

The bank does not know `D`, `s_p`, `s_q`, or `S`.  Suppose only that the
hidden state satisfies

\[
\boxed{\min(s_p,s_q)\le U.}
\tag{10}
\]

Also suppose a beta-two carry calculation has supplied `p mod 2^t`, and put

\[
J=\left\lceil{N^{1/4}\over S_0(n)}\right\rceil
\]

for a fixed positive numerical-QP function `S_0`.  Assume that the attainable
odd common capacity closes the terminal:

\[
\boxed{\operatorname{lcm}(2^t,D)\ge J.}
\tag{11}
\]

At every history for which

\[
L=\operatorname{lcm}(2^t,M)<J,
\]

one complete multiplier-bank stage returns a factor or makes `M` grow with
conditional probability at least

\[
\boxed{4/9.}
\tag{12}
\]

The probability is uniform over all earlier histories.  The algorithm does
not need to identify the missing primary or the favorable residual order.

If `(s_p,s_q)!=(1,1)`, one bank entry annihilates the complete odd subgroup
on one side and yields a direct factor with probability at least `2/3`.  If
`s_p=s_q=1`, equation (11) and preterminality force a missing odd primary
`ell^k|D`.  At `u=1`, stripping returns a factor or certifies a primary
strictly beyond `M` whenever an event of the following exact probability
occurs:

\[
\left(1-\ell^{-(v_\ell(P)-k+1)}\right)
\left(1-\ell^{-(v_\ell(Q)-k+1)}\right)
\ge(1-1/\ell)^2\ge {4\over9}.
\tag{13}
\]

With the P197 potential

\[
\Phi(L)=\max\left\{0,\left\lceil\log_2{J\over L}\right\rceil\right\},
\]

equation (12) gives conditional drift at least `4/9`.  The expected number
of stages is at most `9n/4`.  Combining the terminal residue modulo
`lcm(2^t,M)` with the known-residue factorer gives a Las Vegas numerical-QP
factorer on the favorable state, conditional on a correct recursive
dispatcher that supplies the complete factorization of the half-size
integer `H`.

The hostile F228 witness lies literally in the favorable state.  For

\[
N=2881=43\cdot67,
\qquad B=64,
\qquad H=45,
\]

one has

\[
P=21,
\qquad Q=33,
\qquad D=3,
\qquad (s_p,s_q)=(7,11).
\]

At the public bank entry `u=7`, the child is `A=315`.  For a fresh projected
unit, equation (8) gives the exact direct-factor probability

\[
1-{1\over11}={10\over11}.
\tag{14}
\]

## Corollary — certified randomized-multiplier rate

Instead of scanning the full bank, choose `u` uniformly among the

\[
O_U=\lceil U/2\rceil
\]

odd integers in `[1,U]`.  Under (10)--(11), every preterminal history has
factor-or-growth probability at least

\[
{4\over9O_U}\ge {4\over9U}.
\tag{15}
\]

If `c` is independently uniform in a set of `W` consecutive integers that
contains zero, the event using the zero-defect branch has probability at least

\[
{4\over9O_UW}.
\tag{16}
\]

The shift randomization only dilutes this branch.  Once the public test
`B|(N-1)` succeeds, setting `c=0` is canonical.

## Theorem D — sharp bounded-uniform-source boundary

After the direct screen `gcd(u,N)=1`, every factor or common-primary
certificate obtainable from `a^(uH)-1` and any sequence of exponent
punctures requires at least one local return.  Therefore its probability is
at most

\[
\alpha_p(u)+\alpha_q(u)-\alpha_p(u)\alpha_q(u).
\tag{17}
\]

For every odd `u<=U`, this is at most

\[
U\left({1\over s_p}+{1\over s_q}\right).
\tag{18}
\]

The same conditional bound holds when `u` is selected adaptively from this
range and each test uses a fresh uniform odd projection.  Thus `K` such
tests have useful-event probability at most

\[
KU\left({1\over s_p}+{1\over s_q}\right).
\tag{19}
\]

For a fixed bank of `K` multipliers applied to one fresh projection, the
same expression follows directly by a union bound; independence inside the
bank is unnecessary.  When both residual odd orders are exponential, every
numerical-QP bounded uniform-witness bank is exponentially sparse even
though `H` and every `uH` are completely factored.  This is a source-model
obstruction, not a lower bound against carry-correlated multipliers,
nonuniform integer witnesses, APR-compatible residues, or a different use
of the factorization of `H`.
