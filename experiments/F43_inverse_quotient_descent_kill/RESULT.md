# F43 inverse-quotient descent mandatory kill — finite scan resumed

**Status:** incomplete candidate. The preregistered finite scan now completes,
but the all-input success-probability analysis is still open. The exact
one-step law, a near-square-root worst-case depth bound, and a slow-chain
family are unbounded mathematical results. No polynomial-time factoring result
or unbounded success probability is claimed.

For \(N\ge2\) and a unit \(u\in\{1,\ldots,N-1\}\), let \(v\) be the least
positive inverse of \(u\bmod N\), and define

\[
D_N(u)=\frac{uv-1}{N}.
\]

The first exact runner attempt failed at Sage import because the sandbox denied
its cache write. An identical escalated attempt reached the JSON write but failed
because a carry sequence retained Sage `Integer` objects. Both failures and the
invalid partial JSON are preserved and fully disposed in `RUN_MANIFEST.md`.

After the user resumed the research, attempt 3 added the two requested state
tickets and repaired only the JSON integer boundary. The same declared scan of
all distinct odd semiprimes \(15\le N\le511\) then completed successfully.
Its finite summary is:

- largest observed descent depth: 13, at \(N=481\) from start 480;
- smallest direct state/carry success: \(14/192\), at \(N=221\);
- smallest extended-ticket success: \(130/220\), at \(N=253\);
- every tested \(n^2\)-offset menu contained an extended-ticket success.

These values are discovery evidence only. They do not prove polylogarithmic
depth, inverse-polynomial success, or an all-input factoring algorithm. They
motivated the symbolic analysis and separately registered scaling scan below.

The preregistered F43-D02 scaling scan then sampled 50,000 uniform units on six
balanced semiprimes with smaller factor from 257 through 262,147. The extended
hit rate fell from 0.19346 to 0.00030. On the largest input, only 15 of 50,000
sampled trajectories hit an extended ticket, and none of the 1,369 public
\(n^2\)-offset starts hit one. All trajectories ended before the step cap; the
largest sampled depth was 46.

This kills the finite optimism from F43-D01. It is still not an asymptotic
obstruction. A promoted method failure requires a theorem that bounds the
polynomial-depth hit probability on an infinite balanced family, or a structural
reduction showing that the full nonzero quotient transcript has no stronger
decoder. Conversely, a retry survives only if it proves a joint transcript use
whose success does not reduce to the union of the named rare tickets.

A preregistered third run also kills the simplest symbolic depth shortcut. The
conjecture

\[
2D_N(D_N(u))\le u
\]

for consecutive unit states already fails at \(N=11,u=7\), whose trajectory
starts \(7\to5\to4\). It also fails on the balanced distinct semiprime
\(N=35\), where \(19\to13\to10\). In the declared exhaustive and seeded scan, 593,870 of
3,887,362 eligible pairs violated the inequality. The largest recorded
two-step ratio was close to one rather than one half. This finite result does
not disprove a weaker amortized or potential-based polynomial depth theorem;
it only removes uniform two-step contraction as its proof.

## Exact structure of one step

Let \(2\le u<N\) and \(\gcd(u,N)=1\). Let \(r_u\) be the least positive
inverse of \(N\bmod u\). Then

\[
\boxed{D_N(u)=u-r_u.}
\tag{1}
\]

Indeed, write \(Nr_u-1=tu\). Since \(1\le r_u<u<N\), one has
\(1\le t<N\). The integer \(v=N-t\) lies in \(\{1,\ldots,N-1\}\) and
satisfies

\[
uv=N(u-r_u)+1.
\]

Thus \(v\) is the least positive inverse of \(u\bmod N\), and (1) follows.
In particular,

\[
D_N(u)=u-r
\quad\Longleftrightarrow\quad
u\mid Nr-1,qquad 1\le r<u.
\tag{2}
\]

There is also an exact reverse description. For \(1\le k<N\),

\[
D_N^{-1}(k)=\{u:k<u<N,\ u\mid Nk+1\}.
\tag{3}
\]

If \(v=(Nk+1)/u\), these conditions automatically imply \(k<v<N\) and
\(\gcd(u,N)=\gcd(v,N)=1\). Equivalently, the preimages are the two factors in
factorizations

\[
Nk+1=uv,
\qquad
k<u<N,
\qquad
k<v<N.
\tag{4}
\]

The complementary factor \(v\) is a second preimage, so non-square preimages
come in inverse pairs. Formula (3) is structural, not an efficient reverse
sampler: enumerating those preimages requires finding suitable divisors of the
known integer \(Nk+1\).

## A near-square-root depth bound, but not a polynomial-bit bound

Consider one trajectory until it reaches \(1\) or a proper nonunit. Write

\[
r_i=u_i-u_{i+1}\ge1.
\]

The states \(u_i\) are strictly decreasing, and (2) shows that every state with
the same decrement \(r\) is a distinct divisor of \(Nr-1\). Let

\[
\Delta_N=\max_{1\le m<N^2}\tau(m),
\]

where \(\tau\) is the divisor-counting function. For every integer
\(1\le B<N\), the number \(L\) of transitions satisfies

\[
\boxed{L\le \frac{N}{B}+B\Delta_N+1.}
\tag{5}
\]

The first term bounds steps with \(r_i>B\) by their total decrease. The second
bounds, for every \(1\le r\le B\), the number of states dividing \(Nr-1\).
The standard maximal-divisor bound

\[
\Delta_N=\exp\!\left(O\!\left(\frac{\log N}{\log\log N}\right)\right)
=N^{o(1)}
\]

and a balanced choice of \(B\) give

\[
L\le N^{1/2+o(1)}.
\tag{6}
\]

This improves the trivial \(L<N\) integer-state bound, but it is still
exponential in the binary input length. It does not establish a usable runtime.

Long slow chains are genuine. Put

\[
M_L=\operatorname{lcm}(2,3,\ldots,L+1),
\qquad
N_L=(M_L+1)^2.
\]

Then \(N_L\equiv1\pmod u\) for every \(2\le u\le L+1\), so (1) gives the
exact trajectory

\[
L+1\longrightarrow L\longrightarrow\cdots\longrightarrow2
\longrightarrow1.
\tag{7}
\]

The usual Chebyshev bounds for
\(\log\operatorname{lcm}(1,\ldots,L+1)\) make the input bit length
\(\Theta(L)\). These moduli are easy perfect squares; (7) is only a sharp
warning against a universal \(o(\log N)\) depth claim, not a hard factoring
family.

## Remaining algorithmic question

The public trajectory produces exact factorizations

\[
u_i v_i=N u_{i+1}+1
\]

of many integers congruent to \(1\bmod N\). The finite gcd tickets were sparse
on the larger F43-D02 inputs, but no infinite-family hit bound is proved. That
does not show that the whole collection is useless. The surviving question is
whether polynomially many
such factorizations admit a global decoder, such as a parity, lattice, or
continued-fraction relation, whose success is not the union of rare coordinate
events. Without such a decoder or a stronger hit theorem, F26 is not a
factoring algorithm.
