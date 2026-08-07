# F66 hostile audit — inverse-diagonal metric kill

**Candidate audited:**
`experiments/F66_inverse_diagonal_metric_kill/RESULT.md`

**Verified candidate SHA-256:**
`f1f8fe2829cf22314cf451e8a6c0218877f5c17d6de6d7e3e30c9689b2c30629`

**Verdict: PASS.**

The fibre theorem, harmonic normalization, useful mass, rejection lower
bound, Metropolis--Hastings lower bounds, and local-plateau theorem are
correct. The conclusions have the stated narrow scope. They rule out the
three named access methods. They do not rule out every sampler or every
factor-extraction rule.

No research computation was used. This audit used symbolic reasoning, hand
arithmetic, and hashing only.

## 1. Prior-result boundary — PASS

P49 covers screened sparse additive Fourier observables and fixed
axis-parallel rectangles for the uniform inverse graph. It explicitly does
not cover nonlinear diagonal statistics, dense processing, nonuniform
sources, or dissipative dynamics. The canonical statistic

\[
 |u-v(u)|
\]

is outside those proved classes. The candidate does not claim that P49
implies its new obstruction.

## 2. Signed fibres and CRT count — PASS

If `d=u-v`, then `v=u-d`. The two canonical conditions are exactly

\[
 1\le u\le N-1,
 \qquad
 1\le u-d\le N-1.
\]

Their intersection is

\[
 \max(1,1+d)\le u\le\min(N-1,N-1+d).
\]

On this interval, `u(u-d)=1 mod N` makes both factors units. It also makes
`u-d` the canonical inverse of `u`. Thus equation (1) is reversible and
exact.

Write `u(u-d)=1+kN`. Both canonical factors are in `[1,N-1]`. Hence

\[
 1\le u(u-d)\le(N-1)^2=1+(N-2)N.
\]

This gives exactly `0 <= k <= N-2`. Multiplication by four gives

\[
 (2u-d)^2=d^2+4+4kN.
\]

For an odd prime `r`, the substitution `z=2u-d` is bijective. The local
root count is

\[
 \#\{z:z^2=\Delta_d\pmod r\}
 =1+\left(\frac{\Delta_d}{r}\right).
\]

This formula includes every discriminant case:

- a nonresidue gives zero roots;
- a nonzero square gives two roots;
- a zero discriminant gives one repeated root.

CRT therefore gives the exact product in equation (4). The canonical
interval has length less than `N`, so it contains at most one integer from
each residue class. It can only remove CRT roots. Thus `f_d <= 4` is valid.

The interval is empty when `|d| >= N-1`. Inversion is an involution from
`F_d` to `F_{-d}`. Therefore `f_d=f_{-d}`.

## 3. Discriminant ticket — PASS

For a unit and its inverse,

\[
 (u-v)^2+4\equiv(u+v)^2\pmod N.
\]

For `r` equal to `p` or `q`, divisibility by `r` is equivalent to

\[
 u+u^{-1}=0\pmod r
 \quad\Longleftrightarrow\quad
 u^2=-1\pmod r.
\]

Let

\[
 e_r=1+\left(\frac{-1}{r}\right)\in\{0,2\}.
\]

The exact proper-ticket probability for uniform `u` in `U_N` is

\[
 \frac{e_p(q-1-e_q)+e_q(p-1-e_p)}{(p-1)(q-1)}
 =\frac{e_p}{p-1}+\frac{e_q}{q-1}
  -\frac{2e_pe_q}{(p-1)(q-1)}.
\]

The subtraction removes the cases in which both primes divide the
discriminant and the gcd is `N`. This exact formula implies equation (7).
It is `O(N^{-1/2})` on a balanced family. It can be zero when both primes
are `3 mod 4`. Thus “the same scale” in section 5 must be read as the same
upper scale, not as a uniform `Theta` claim.

## 4. Normalizer, useful mass, and TV reduction — PASS

The equation `u=v` is `u^2=1 mod N`. A product of two distinct odd primes
has exactly four such CRT roots. Two have equal signs and are `1,N-1`.
Two have mixed signs and reveal a proper factor through `gcd(u-1,N)` or
`gcd(u+1,N)`.

Grouping the weights by signed difference gives

\[
 Z_N=4+\sum_{d=1}^{N-2}\frac{f_d+f_{-d}}{1+d}.
\]

Using `f_d=f_{-d}<=4` gives

\[
 4\le Z_N\le4+8\sum_{d=1}^{N-2}\frac1{1+d}
 =8H_{N-1}-4.
\]

The two useful roots each have weight one. Their mass is exactly

\[
 \pi(M_N)=\frac2{Z_N}.
\]

The two lower bounds in equation (9) follow from the upper bound on `Z_N`
and `H_m<=1+log(m)`. Since `log N` and the bit length `n` differ by a
constant factor, this mass is `Omega(1/n)`.

If a sampler law is `mu` and

\[
 d_{TV}(\mu,\pi)\le\frac1{8H_{N-1}-4},
\]

then

\[
 \mu(M_N)\ge\pi(M_N)-d_{TV}(\mu,\pi)
 \ge\frac1{8H_{N-1}-4}.
\]

Independent reruns therefore need `O(log N)=O(n)` samples for constant
factoring probability. The target-signal PASS is justified.

## 5. Rejection cost, phi bound, and side gcds — PASS

For a uniform unit proposal, acceptance probability is exactly `Z_N/m`,
where `m=phi(N)`. The proposal count is geometric, so

\[
 \mathbb E T_{rej}=\frac{m}{Z_N}.
\]

If `p<q`, then either `p=3,q>=5`, or both prime factors are larger. Hence

\[
 \frac{\varphi(N)}N
 =\left(1-\frac1p\right)\left(1-\frac1q\right)
 \ge\frac23\frac45=\frac8{15}.
\]

Combining this with the normalizer bound proves
`Omega(N/log N)` proposals. A proposal uniform on all `N` residues has
weighted acceptance probability `Z_N/N`, so it cannot improve the sampler
completion cost.

The side events do not turn this into a polynomial-time factoring route on
balanced inputs:

- There are exactly `p+q-2` nonzero nonunits. A raw residue proposal finds
  one with probability `(p+q-2)/N`.
- The exact discriminant-ticket probability is given in section 3.
- The direct screens `gcd(u-1,N)` and `gcd(u+1,N)` have union probability

  \[
   \frac{2p+2q-10}{(p-1)(q-1)}.
  \]

- The screen `gcd(u-v,N)` has proper-ticket probability

  \[
   \frac{2p+2q-12}{(p-1)(q-1)},
  \]

  because `u-v=0 mod r` is `u^2=1 mod r` and has two local roots.
- A screen on the weight denominator also stays sparse. The event
  `r | 1+|u-v|` implies `u-u^{-1}=1` or `-1 mod r`. These are two
  quadratics, so there are at most four local residues.

Each probability is `O(N^{-1/2})` on a fixed balanced family. A polynomial
number of trials in `n` keeps their union probability
`2^{-Omega(n)}`. These events can reduce an augmented algorithm's expected
time to a factor to a square-root scale on some families. They do not
invalidate the stated `Omega(N/log N)` sampler-completion bound. The
candidate does not claim an `Omega(N/log N)` lower bound for every possible
side-screen factoring algorithm.

## 6. Metropolis--Hastings bounds — PASS

Detailed balance follows from

\[
 \pi(x)P(x,y)=\frac{\min(w(x),w(y))}{Z_Nm}.
\]

At `x=1`, every distinct proposal `y` is accepted with probability `w(y)`.
The exact leave probability is therefore

\[
 \ell=\frac1m\sum_{y\ne1}w(y)=\frac{Z_N-1}{m}.
\]

For `t <= m/(4(Z_N-1))`, staying at `1` for all `t` transitions has
probability

\[
 (1-\ell)^t\ge1-t\ell\ge\frac34.
\]

Since `pi(1)=1/Z_N<=1/4`, the event `{1}` gives TV distance at least
`1/2`. The bounds `m=Omega(N)` and `Z_N=O(log N)` prove the claimed
worst-start mixing lower bound.

For a uniform start, the chain can enter `M_N` only if the start or one of
the first `t` proposals is in `M_N`. Thus

\[
 \Pr(X_t\in M_N)
 \le\Pr(\text{some entrance by time }t)
 \le\frac{2(t+1)}m.
\]

If `t+1<=m/(2Z_N)`, subtraction from the exact target mass `2/Z_N` gives
equation (19). This lasts for `Omega(N/log N)` steps.

There is a harmless endpoint precision issue if “within” is defined with a
non-strict `<=` at exactly the displayed target tolerance. One can replace
the condition by

\[
 t+1\le\frac{m}{4Z_N}.
\]

Then the same argument gives TV distance at least `3/(2Z_N)`, which is
strictly larger than `1/(8H_{N-1}-4)`. This changes no asymptotic claim.

All fresh MH proposals are uniform units. Therefore the side-gcd bounds in
section 5 also apply to them. Such tickets remain negligible for a
polynomial number of steps. They do not change the kernel's mixing time.

## 7. The two explicit plateaus — PASS

For `N=55`, hand multiplication gives

\[
 6\cdot46=5\cdot55+1,
 \quad 7\cdot8=55+1,
 \quad 9\cdot49=8\cdot55+1.
\]

Thus the displayed distances are `(40,1,1,40)`. The middle signed
differences are `-1,+1`. Their discriminant is `5`, and `gcd(5,55)=5`.
The candidate correctly rejects this as a clean obstruction.

For `N=209`, all three identities are exact:

\[
 79\cdot127=10033=48\cdot209+1,
\]

\[
 80\cdot81=6480=31\cdot209+1,
\]

\[
 82\cdot130=10660=51\cdot209+1.
\]

They give distances `(48,1,1,48)`. None of `79,80,81,82` is divisible by
`11` or `19`. Also `gcd(5,209)=1`. At `80` and `81`, both direct neighbor
gcd screens pass because the four consecutive states are units. Strict
descent stops. A non-increasing rule cannot leave the closed set
`{80,81}`. Calling it a “two-cycle” describes this closed tie edge; a rule
may also choose to stay at one endpoint.

## 8. Minimality and the general sealed plateau — PASS

A positive distance cannot be below one. If `u` has canonical inverse
`u+1`, then

\[
 f(u)=u^2+u-1=0\pmod N.
\]

For an odd prime `r != 5`, this quadratic has a root exactly when `5` is a
quadratic residue modulo `r`. Quadratic reciprocity gives

\[
 \left(\frac5r\right)=1
 \quad\Longleftrightarrow\quad
 r=1\text{ or }-1\pmod5.
\]

The smallest two distinct odd primes in these classes are `11` and `19`.
If a factor were `5`, the discriminant gcd would already reveal it. Hence a
clean distance-one example must have `N>=11*19=209`. Equality occurs because

\[
 80^2+80-1=6479=31\cdot209.
\]

The general sealing argument is also complete. Assume `gcd(N,5)=1` and
`f(u)=0 mod N`. The residues `u-1` and `u+2` are units. Otherwise a prime
factor of `N` would see `u=1` or `u=-2`, while `f(1)=f(-2)=1`.

Put `x=u-1` and use `u^2=1-u`. The three possible congruences for
`delta_N(x)<=1` give

\[
\begin{array}{c|c|c}
\text{congruence}&\text{consequence}&\text{contradiction}\\ \hline
x^2=1&3u=1&9f(u)=-5\\
x(x+1)=1&2u=0&f(0)=-1\\
x(x-1)=1&2u=1&4f(u)=-1.
\end{array}
\]

The first row contradicts `gcd(N,5)=1`. The other rows contradict
`f(u)=0`; `2` is invertible because `N` is odd.

For `y=u+2`, the three conditions give

\[
\begin{array}{c|c|c}
\text{congruence}&\text{consequence}&\text{contradiction}\\ \hline
y^2=1&3u=-4&9f(u)=-5\\
y(y-1)=1&u=-1&f(u)=-1\\
y(y+1)=1&2u=-3&4f(u)=-1.
\end{array}
\]

Thus both outer neighbors have distance greater than one. The middle pair
has distance one and ticket discriminant `5`, which is coprime to `N`.
Every such pair is a sealed, factor-free, two-state local minimum. This
proves both the stated minimum-height minimality and the general plateau
claim. It does not prove a random-start basin lower bound, and the candidate
explicitly says so.

## 9. Bit-complexity classification and final scope — PASS

With `n=ceil(log_2 N)`, one has `N>=2^{n-1}` and `log N=Theta(n)`. Hence

\[
 \frac{N}{\log N}=2^{\Omega(n)}.
\]

The rejection proposal count and MH mixing lower bound are exponential in
the input length. On balanced inputs, every side event bounded above by
`poly(n)N^{-1/2}` is also `2^{-Omega(n)}`. The candidate's use of
“polynomial time” is therefore consistent.

No counterexample was found. No mathematical repair is required. The two
optional precision edits are:

1. Replace “the same scale” for the discriminant ticket by “the same
   `O(N^{-1/2})` upper scale.”
2. Use `t+1<=m/(4Z_N)` in the uniform-start paragraph if a strict TV
   separation at the exact non-strict tolerance is desired.

Neither edit changes the verdict or any asymptotic conclusion.

## Amendment — corrected candidate

The corrected candidate has SHA-256
`0037947187b324ff655a539bbff8dd82d68c8fe52e8c0a0edcd34fab20b8568e`.

A full comparison with the previously pinned candidate found only the two
optional precision edits listed above:

1. The discriminant ticket now has an explicit `O(N^{-1/2})` upper bound.
2. The uniform-start argument now uses `t+1<=m/(4Z_N)` and obtains
   `3/(2Z_N)>1/(8H_{N-1}-4)`.

Both edits are correct. No other change was found. **Verdict: PASS.**
