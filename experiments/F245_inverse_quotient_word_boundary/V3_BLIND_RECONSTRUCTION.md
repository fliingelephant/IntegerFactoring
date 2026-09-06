# F245 V3 blind reconstruction

## Authentication and verdict

Before reading the statement, I computed

```text
SHA-256(V3_STATEMENT.md)
= 2120f53ec1762cd6b90236eb165d59368f9e0aad4750dcb3a5afadf3508d2c8b.
```

This equals the required digest.  This reconstruction used only the root
`PROMPT.md`, the root `AGENTS.md`, and that authenticated statement.

**Verdict: PASS, for the stated restricted-grammar boundary only.**

I can reconstruct every quantitative claim in the statement.  In
particular, the cutoff bound is exhaustive for the stated grammar and does
exclude expected numerical-quasipolynomial running time on the constructed
infinite family.  It does not prove the all-input factoring claim in the
root prompt.  The exact uncovered mechanisms are listed at the end.

## 1. Reconstructed object and exhaustive grammar

The hard inputs are distinct-odd-prime semiprimes

\[
N=pq,
\qquad
n=\lceil\log _2(N+1)\rceil,
\qquad
\Delta_N=\max_{1\le m<N^2}\tau(m).
\]

A numerical quasipolynomial is an integer-valued function bounded by
\(2^{(\log _2(n+2))^C}\) for one fixed \(C\).  Every integer is represented
explicitly.  Thus a materialized integer of \(b\) bits costs at least
\(b\) bit operations; a large exponent cannot be hidden in a succinct
circuit.

The filtration \(\mathcal F_t\) contains the full past.  Every control
choice can be \(\mathcal F_t\)-measurable, but each new random draw has the
specified conditional law given all of \(\mathcal F_t\).  The order of the
operations is part of the restriction.

### 1.1 Unit atoms

A raw \(R\) is conditionally uniform in \(\{0,\ldots,N-1\}\).  A proper
\(\gcd(R,N)\) is returned, \(R=0\) is rejected, and otherwise the accepted
\(u=R\) is conditionally uniform on the \(\varphi(N)\) canonical units.
For the least positive inverse \(v\) of \(u\), the only positive atomic
integer available from this seed is

\[
K(u)=\frac{uv-1}{N},
\qquad
\widehat K(u)=\begin{cases}K(u),&K(u)>0,\\1,&K(u)=0.\end{cases}
\]

For two stored seeds, the only collision atom is

\[
\Gamma_{ij}=\begin{cases}|K_i-K_j|,&K_i\ne K_j,\\1,&K_i=K_j.\end{cases}
\]

The inverse-quotient word \(W_{\rm iq}\) is an explicitly materialized
product of positive powers of these \(\widehat K_i\)'s and
\(\Gamma_{ij}\)'s.  Repetitions are allowed, and the empty product is one.
Neither a transform of an atom nor a new quotient digit is allowed.

### 1.2 Other integer words and tokens

The signed-power word is exactly

\[
W_{\rm sp}=\prod_{j=1}^s|N^{k_j}-\sigma_j|^{e_j},
\qquad k_j,e_j\ge1,
\quad \sigma_j\in\{+1,-1\},
\]

again with an empty product allowed and with its full expansion charged.

A common-order token \(m\), in an orientation
\((a,b)\in\{+1,-1\}^2\), is the exact order of a point in each of two cyclic
groups of respective orders \(p-a\) and \(q-b\).  Therefore

\[
m\mid p-a,
\qquad
m\mid q-b.
\]

Tokens can disclose neither local sign nor a different local order.  Any
number of them may be combined only as

\[
M=\operatorname{lcm}(m_1,\ldots,m_h),
\]

with empty lcm one.  Every powered word is exactly

\[
W=(N^2-1)^nW_{\rm sp}W_{\rm iq}M.
\]

Legal direct integer gcd arguments are only an individual bank entry, a
current signed-power or full product, \(M\), or the final exponent below.
A direct gcd can return only when it is proper.

### 1.3 Discriminant, Hilbert--90 sample, and chronology

A raw \(D\) is conditionally uniform modulo \(N\).  Its gcd screen has the
same proper-return and zero-rejection rules as the unit draw.  An accepted
\(D\) is a unit and has Jacobi sign

\[
J=\left(\frac D N\right)\in\{+1,-1\}.
\]

The machine can retain this \(D\).  Before every fresh coefficient pair it
must fix

\[
E=(N-J)W.
\]

This measurability requirement is essential: \(E\) is fixed before the
point that it powers.

Next, \(A,B\) are conditionally independent uniform residues modulo \(N\).
The coefficient screen is

\[
c=\gcd(N,A,B).
\]

A proper value is returned and \(c=N\) rejects the pair.  If \(c=1\), put

\[
\nu=A^2-DB^2\pmod N
\]

and apply its gcd screen.  A proper gcd is returned, gcd \(N\) rejects, and
only gcd one enters the clean branch.  There the inverse of \(\nu\) exists
and

\[
U=\frac{A+Bw}{A-Bw}=x_0+x_1w,
\qquad w^2=D,
\]

with

\[
x_0=(A^2+DB^2)\nu^{-1},
\qquad
x_1=2AB\nu^{-1}\pmod N.
\]

All later torus arithmetic uses only

\[
(x_0,x_1)(y_0,y_1)
=(x_0y_0+Dx_1y_1,\ x_0y_1+x_1y_0)\pmod N.
\]

Thus no inverse is taken before its norm is certified as a unit.

### 1.4 Powered and two-primary screens

For \(Y=(y_0,y_1)\), the only point screens are

\[
G_+(Y)=\gcd(N,y_0-1,y_1),
\qquad
G_-(Y)=\gcd(N,y_0+1,y_1).
\]

The trial first computes \(V=U^E\) and applies only \(G_+(V)\).  A proper
value is returned, value one makes the trial null, and value \(N\) means
\(V=1\) at both hidden primes.  Only in the last case, write

\[
E=2^ve_0,
\qquad e_0\text{ odd},
\qquad v\ge1,
\]

and screen both signs on

\[
Y_j=U^{e_0 2^j},
\qquad 0\le j\le v.
\]

No coordinate, carry, determinant, power, or other transform of this point
can become a later integer word.  A valid common-order token is the only
allowed order summary.  Later choices remain adaptive, but every later
draw and exponent obeys the same law and chronology.

These lists are exhaustive by definition.  The machine can return only a
verified proper gcd from a raw-unit screen, a raw-discriminant screen, the
coefficient/norm screens, a legal direct-word screen, or the displayed
torus screens.  Rejections and null trials may be followed by more work,
and raw rejected draws count toward the running time.

## 2. Inverse-quotient atom and collision bounds

Fix an exact value \(K=k\).  Every seed giving it yields a positive factor
pair

\[
uv=1+Nk<N^2.
\]

For a fixed right-hand side, the number of possible \(u\)'s is at most its
divisor count.  Consequently

\[
\#\{u:K(u)=k\}\le\tau(1+Nk)\le\Delta_N
\]

and conditional uniformity of an accepted unit gives

\[
\Pr(K=k)\le\frac{\Delta_N}{\varphi(N)}.
\]

Every value of \(\widehat K\), except possibly one, has one preimage among
the exact \(K\)-values.  The value one can have the two preimages \(K=0\)
and \(K=1\).  Hence

\[
\Pr(\widehat K=t)\le\frac{2\Delta_N}{\varphi(N)}.
\]

For a prime \(\ell<N\), one residue class contains at most
\(\lceil N/\ell\rceil\) possible values of \(\widehat K\).  Therefore

\[
\Pr(\widehat K\equiv r\pmod\ell)
\le
\beta_{N,\ell}
:=\frac{2\lceil N/\ell\rceil\Delta_N}{\varphi(N)}.
\]

For distinct odd primes \(p,q\),

\[
\frac{\varphi(N)}N
=\left(1-\frac1p\right)\left(1-\frac1q\right)
\ge\frac{8}{15}>\frac12,
\]

and \(\lceil N/\ell\rceil<2N/\ell\).  Thus

\[
\beta_{N,\ell}<\frac{8\Delta_N}{\ell}.
\]

This proves the first incidence inequality.  For a pair \(i<j\), condition
on the complete history through seed \(i\), hence also on \(K_i\).  The
later accepted seed still has the exact uniform-unit law.  If
\(\ell\mid\Gamma_{ij}\), then \(K_j\equiv K_i\pmod\ell\) and
\(K_j\ne K_i\).  Dropping the inequality and applying the same exact-value
count (which is even a factor two sharper before the \(K=0\) replacement)
gives

\[
\Pr(\ell\mid\Gamma_{ij}\mid\mathcal F_i)
\le\beta_{N,\ell}.
\]

The inequalities therefore hold history by history.  With at most \(B\)
accepted seeds, there are at most

\[
H_B=B+{B\choose2}
\]

positive seed or collision atoms.  A union bound gives

\[
\Pr(\text{some available atom is divisible by }\ell)
\le H_B\beta_{N,\ell}.
\]

Adaptive selection, powers, repetitions, and stopping cannot invalidate
this event-level bound: a selected product is divisible by \(\ell\) only
if one of its already-counted positive atoms is divisible by \(\ell\).

## 3. Reconstruction of the four-marker family

Choose four distinct large marker primes
\(\lambda_+,\lambda_-,\rho_+,\rho_-\) in comparable intervals and choose a
primitive residue at each.  All markers are coprime to 24.

Use CRT modulo

\[
24\lambda_+\lambda_-\rho_+\rho_-
\]

to impose

\[
p\equiv13\pmod{24},
\qquad
p\equiv+1\pmod{\lambda_+},
\qquad
p\equiv-1\pmod{\lambda_-},
\]

and a primitive nonzero residue modulo each rho-marker.  The CRT class is
reduced.  Linnik's theorem supplies a prime \(p\) in it, with \(p\)
polynomially bounded in this first modulus.  In particular,

\[
\operatorname{ord}_{\rho_b}(p)=\rho_b-1.
\]

Now write the exact factorization

\[
p^2-1=2^3 3^e\prod_{s\ge5}s^{e_s}.
\]

The exponent of two is exactly three because \(p\equiv13\pmod{24}\).
For the second CRT class impose

\[
q\equiv3\pmod8,
\qquad
q\equiv2\pmod{3^{\max(e,2)}},
\qquad
q\equiv+1\pmod{\rho_+},
\qquad
q\equiv-1\pmod{\rho_-}.
\]

For every prime-power factor \(s^{e_s}\) of \(p^2-1\), \(s\ge5\), choose
a unit lift whose reduction is neither \(+1\) nor \(-1\).  At each
lambda-marker choose such a lift with primitive reduction.  This is
possible because a primitive element of a marker field of order greater
than three is not a sign.  The rho-markers do not divide \(p^2-1\), since
\(p\) has order \(\rho_b-1>2\) modulo them.  Hence all second-stage moduli
are compatible and coprime, and the resulting CRT class is reduced.
Linnik supplies a prime \(q\) in it.  We obtain

\[
\lambda_a\mid p-a,
\qquad
\rho_b\mid q-b,
\]

and

\[
\operatorname{ord}_{\lambda_a}(q)=\lambda_a-1,
\qquad
\operatorname{ord}_{\rho_b}(p)=\rho_b-1.
\]

The primes are distinct: modulo either lambda-marker, \(p\) is a sign while
\(q\) is primitive of order greater than two.

The exact small-prime valuations are

\[
\begin{array}{c|cc|cc}
 &v_2(p-1)&v_2(p+1)&v_3(p-1)&v_3(p+1)\\ \hline
p&2&1&e&0
\end{array}
\]

and

\[
v_2(q-1)=1,
\quad v_2(q+1)=2,
\quad v_3(q-1)=0,
\quad v_3(q+1)=1.
\]

For every \(s\ge5\) dividing \(p^2-1\), the chosen residue gives
\(q^2\not\equiv1\pmod s\).  It follows that

\[
\gcd(p^2-1,q^2-1)=2^3\cdot3=24
\]

and, with the signs separated,

\[
\gcd(p-1,q-1)=2,
\quad
\gcd(p-1,q+1)=12,
\quad
\gcd(p+1,q-1)=2,
\quad
\gcd(p+1,q+1)=2.
\]

Quantitatively, if the marker scale is \(X\), the first Linnik modulus is
polynomial in \(X\), so \(p\) is polynomial in \(X\).  The second modulus
is at most a fixed constant times

\[
(p^2-1)\rho_+\rho_-,
\]

so \(q\), and hence \(N=pq\), is also polynomial in \(X\).  Conversely,
the congruence \(p\equiv1\pmod{\lambda_+}\) forces
\(p>\lambda_+\), and \(q\equiv1\pmod{\rho_+}\) forces
\(q>\rho_+\).  After decreasing one absolute positive constant if needed,
all four comparable markers therefore satisfy

\[
\lambda_+,\lambda_-,\rho_+,\rho_->2^{c_0n}
\]

for all sufficiently large choices.  Taking successively increasing marker
scales gives an infinite family of distinct semiprimes.

## 4. Signed-word and common-order avoidance

Consider \(\lambda_a\).  Modulo this marker,

\[
N=pq\equiv aq.
\]

If \(\lambda_a\mid N^k-\sigma\), then
\(q^k\in\{+1,-1\}\).  Because \(q\) is primitive modulo
\(\lambda_a\), this forces

\[
k\ge\frac{\lambda_a-1}{2}.
\]

The identical argument at \(\rho_b\), using
\(N\equiv bp\) and primitive \(p\), gives
\(k\ge(\rho_b-1)/2\).  A factor \(|N^k-\sigma|\) then has at least
\(k\log_2N-O(1)\) bits.  Since every marker is
\(2^{\Omega(n)}\), that length exceeds every fixed numerical
quasipolynomial for sufficiently large family members.  A product of
positive factors is at least each factor.  Therefore every explicitly
materialized signed-power word of numerical-quasipolynomial length is
coprime to all four markers.

Also \(N^2\equiv q^2\pmod{\lambda_a}\) and
\(N^2\equiv p^2\pmod{\rho_b}\).  A primitive element modulo a marker
larger than three does not have square one.  Hence
\((N^2-1)^n\) is coprime to every marker.

For the orientation \((a,b)\), its Jacobi sign is \(J=ab\).  At the two
matching markers,

\[
N-ab\equiv a(q-b)\pmod{\lambda_a},
\qquad
N-ab\equiv b(p-a)\pmod{\rho_b}.
\]

Primitive \(q\) is not the sign \(b\), and primitive \(p\) is not the sign
\(a\).  Thus neither matching marker divides \(N-J\).

Finally, a token from orientation \((a,b)\) divides the corresponding entry
among \(2,12,2,2\).  Every token therefore divides 12, even when tokens
come from different orientations, and hence

\[
M\mid12.
\]

This also shows that a token cannot itself expose either large hidden prime
or any marker.

## 5. Exact local Hilbert--90 law

For an accepted \(D\), define

\[
a=\left(\frac Dp\right),
\qquad
b=\left(\frac Dq\right),
\qquad
J=ab.
\]

At a local prime \(r\in\{p,q\}\), let
\(\epsilon=(D/r)\).  In
\(\mathbb F_r[w]/(w^2-D)\), the norm-one group is cyclic and has order

\[
m_r=r-\epsilon.
\]

For \(\epsilon=-1\), this is the norm-one subgroup of
\(\mathbb F_{r^2}^{\times}\), of order \(r+1\).  For \(\epsilon=+1\), the
algebra splits as \(\mathbb F_r\times\mathbb F_r\), and its norm-one group
has order \(r-1\).

The map

\[
z=A+Bw\longmapsto z/\bar z
\]

from the elements of nonzero norm onto this norm-one group is surjective
and has constant fibers: its kernel is the embedded
\(\mathbb F_r^\times\), of size \(r-1\).  A uniform local coefficient pair,
conditioned on nonzero norm, therefore maps to a uniform element of the
entire local group, including both signs.

CRT makes the coefficient pairs at \(p\) and \(q\) independent.  The clean
condition is the intersection of one nonzero-norm event on each side, so
conditioning preserves that product structure.  Thus the two clean local
points are independent uniforms in the cyclic groups of orders

\[
m_p=p-a,
\qquad
m_q=q-b.
\]

Since \(E\) was fixed before this point, a uniform element in a cyclic group
of order \(m\) satisfies \(U^E=1\) with exact probability

\[
\frac{\gcd(E,m)}m.
\]

This proves both local return formulas.  A proper initial \(G_+\) screen
means \(U^E=1\) on exactly one side.  The later chain is entered only after
\(U^E=1\) on both sides.  Hence every clean-branch factor return is contained
in the union of the two local return events.

For later use, the number of local zero-norm coefficient pairs is

\[
\#\{(A,B):A^2-DB^2=0\}
=\begin{cases}1,&(D/r)=-1,\\2r-1,&(D/r)=+1.\end{cases}
\]

It is always at most \(2r\).  Any proper coefficient-screen result has
\(A=B=0\) at one local prime and thus has zero norm there; any proper norm
screen has zero norm at one local prime by definition.  Therefore, for one
raw coefficient pair, the combined probability of a factor through either
screen is at most

\[
\frac2p+\frac2q.
\]

This derivation also covers split discriminants; no nonsquare assumption is
hidden in the sampling claim.

## 6. Exact Miller-chain probability

Suppose the global return occurred.  Write \(E=2^ve_0\), with \(e_0\) odd,
and define

\[
h_p=\min(v_2(m_p),v),
\qquad
h_q=\min(v_2(m_q),v).
\]

Conditional on \(U^E=1\) in a local cyclic group, \(U\) is uniform in the
kernel of the \(E\)-power map.  Its two-primary component is consequently
uniform in a cyclic group of order \(2^{h_r}\).  If \(T_r\) is the exponent
of its exact two-primary order, then

\[
\Pr(T_r=0)=2^{-h_r},
\qquad
\Pr(T_r=t)=2^{t-1-h_r}\quad(1\le t\le h_r).
\]

The odd exponent \(e_0\) kills the odd-order component and preserves the
exact order of the two-primary component.  The chain screens a proper
factor exactly when \(T_p\ne T_q\): if the exponents differ, immediately
before the larger-order side reaches one it is \(-1\), while the other side
is already \(+1\); if they agree, both sides are simultaneously neither a
sign, then \(-1\), then \(+1\).

Put

\[
a_2=\min(h_p,h_q),
\qquad
b_2=\max(h_p,h_q).
\]

The conditional failure probability is

\[
\begin{aligned}
\Pr(T_p=T_q)
&=2^{-a_2-b_2}
  \left(1+\sum_{t=1}^{a_2}4^{t-1}\right)\\
&=\frac{4^{a_2}+2}{3\,2^{a_2+b_2}}.
\end{aligned}
\]

Thus the exact conditional success probability is

\[
\mu_{a_2,b_2}
=1-\frac{4^{a_2}+2}{3\,2^{a_2+b_2}}
\ge\frac12.
\]

Both local group orders are even and \(E\) is even because \(N-J\) is
even, so \(a_2\ge1\).  The formula includes identity and minus-one samples;
no deletion or renormalization of those points occurs.

## 7. Adaptive cutoff bound

Let

\[
L=\min(\lambda_+,\lambda_-,\rho_+,\rho_-)
\]

and stop an arbitrary confined run after \(B\ge1\) bit operations.  There
can be at most \(B\) raw draws, accepted unit seeds, coefficient trials, or
screens of any one type.  Every materialized word in this prefix has at most
\(B\) bits.

First define the bank-bad event that some positive seed or collision atom is
divisible by one of

\[
\lambda_+,\lambda_-,\rho_+,\rho_-,p,q.
\]

All six primes are at least \(L\): the four markers are so by definition,
\(p>\lambda_+\), and \(q>\rho_+\).  The history-wise atom bound and a union
bound give

\[
\Pr(\text{bank-bad})
\le6H_B\frac{8\Delta_N}{L}
=48H_B\frac{\Delta_N}{L}.
\]

On its complement, no inverse-quotient product can contain a hidden prime
or a marker.  Signed-power factors and \(N^2-1\) are always units modulo
\(N\); \(N-J\) is a unit modulo \(N\); and \(M\mid12\) is a unit modulo the
large odd semiprime.  Therefore no legal direct integer-word screen can
return a proper factor.  The marker-avoidance results also show that, for a
numerical-quasipolynomial cutoff and sufficiently large family member, the
two matching orientation markers do not divide \(E\).

Since \(\lambda_a\mid m_p\) but \(\lambda_a\nmid E\),

\[
\frac{\gcd(E,m_p)}{m_p}\le\frac1{\lambda_a}\le\frac1L.
\]

Similarly the local return probability on the \(q\)-side is at most
\(1/\rho_b\le1/L\).  The union implication from the Hilbert--90 analysis
therefore bounds every clean powered or chain factor event, conditional on
the entire past, by \(2/L\).  At most \(B\) clean trials contribute

\[
\frac{2B}{L}.
\]

For a raw unit residue, the probability of a proper gcd is

\[
\frac{p+q-2}{pq}\le\frac1p+\frac1q,
\]

and the same holds for a raw discriminant.  Section 5 bounded the combined
coefficient/norm factor probability by
\(2/p+2/q\) per coefficient pair.  With at most \(B\) draws of each kind,
all nonclean factor exits contribute at most

\[
4B\left(\frac1p+\frac1q\right).
\]

Every factor-return rule belongs to exactly one of these three classes:
bank/direct-word, raw/nonclean, or clean-point.  Common-order tokens have no
return rule.  Formally, at each clean trial one splits on the
\(\mathcal F_t\)-measurable event that the bank prefix is already bad.  Any
such path is charged once to the global bank-bad event.  On a prefix-good
path the exponent is marker-free and the fresh-point bound \(2/L\) applies
conditioned on \(\mathcal F_t\).  This avoids conditioning a fresh point on
the future part of the bank-bad event.  The raw-draw bounds likewise hold
given the full filtration.  These conditional bounds can therefore be
summed under arbitrary adaptive stopping.  Hence

\[
\Pr(\text{factor by time }B)
\le
48H_B\frac{\Delta_N}{L}
+4B\left(\frac1p+\frac1q\right)
+\frac{2B}{L}.
\]

This reconstructs the stated constant 48 and the stated exhaustive cutoff
bound without assuming independence among the adaptive control choices.

## 8. Asymptotics and the expected-time contradiction

The standard maximal-divisor estimate is

\[
\max_{m\le x}\tau(m)
=\exp\!\left(O\!\left(\frac{\log x}{\log\log x}\right)\right).
\]

With \(x=N^2\), it gives

\[
\Delta_N=2^{o(n)}.
\]

For a numerical-quasipolynomial cutoff,
\(B=2^{o(n)}\) and \(H_B=2^{o(n)}\).  Also
\(L>2^{c_0n}\) and \(p,q>L\).  Each of the three terms in the cutoff bound
is consequently \(2^{-\Omega(n)}\).

Suppose a fixed confined Las Vegas factorer had expected running time at
most a numerical quasipolynomial \(Q(n)\) on every family member.  Markov's
inequality would give

\[
\Pr(T\le2Q(n))\ge\frac12.
\]

Taking the integer cutoff \(B=\lceil2Q(n)\rceil\), the reconstructed bound
makes the same probability \(2^{-\Omega(n)}\), hence less than one half for
all sufficiently large family members.  This contradiction proves that no
confined Las Vegas factorer has expected numerical-quasipolynomial time on
the whole infinite family.

## 9. Carry identities outside the grammar

Let

\[
g=a_0^2-Db_0^2,
\qquad
A_0=a_0^2+Db_0^2,
\qquad
B_0=2a_0b_0,
\]

where \(g\ne0\) and \(\gcd(g,N)=1\).  Let \(v\) be the least positive
inverse of the possibly signed \(g\) modulo \(N\), and let \(X,Y\) be the
canonical residues of \(A_0v,B_0v\).  Define

\[
\widetilde d=\frac{gv-1}{N},
\qquad
q_A=\frac{A_0v-X}{N},
\qquad
q_B=\frac{B_0v-Y}{N}.
\]

Since \(X=A_0v-Nq_A\), direct expansion gives

\[
\frac{gX-A_0}{N}
=A_0\widetilde d-gq_A.
\]

Likewise,

\[
\frac{gY-B_0}{N}
=B_0\widetilde d-gq_B.
\]

Writing these two integer carries as \(k,l\), respectively, gives

\[
gX=A_0+Nk,
\qquad
gY=B_0+Nl.
\]

The exact polynomial identity

\[
A_0^2-DB_0^2
=(a_0^2-Db_0^2)^2
=g^2
\]

then yields

\[
\begin{aligned}
g^2(X^2-DY^2)
&=(A_0+Nk)^2-D(B_0+Nl)^2\\
&=g^2+2N(A_0k-DB_0l)+N^2(k^2-Dl^2).
\end{aligned}
\]

After subtracting one and dividing by \(N\),

\[
\frac{X^2-DY^2-1}{N}
=\frac{2(A_0k-DB_0l)+N(k^2-Dl^2)}{g^2}.
\]

No positivity or canonical-representative assumption on \(g\) was used.
These are exact integer identities.  By the exhaustive grammar, however,
these carries, their products or squares, and any quotient carry are not
inverse-quotient atoms.  Nothing in the atom-counting proof supplies them
with the residue-mass bounds proved in Section 2.

## 10. Exact gaps and scope boundary

There is no internal proof gap in the restricted theorem reconstructed
above.  Its gap relative to the root factoring objective is exact and
substantial:

1. It treats only an explicit infinite family of distinct odd semiprimes,
   and proves an exclusion for a confined grammar.  It does not supply a
   factoring algorithm for arbitrary integers.
2. The inverse seeds must be fresh exact uniform units.  The argument does
   not cover history-dependent biased or dependent unit sources, or an
   inverse-quotient descent that creates new quotient information.
3. Each exponent must be fixed before its fresh torus point.  The proof does
   not cover feedback from a retained or current point, including words
   formed from its coordinates or powers.
4. Only linear bank atoms, positive products, the stated signed powers, and
   common-order lcms occur.  Nonlinear carry words, canonical high digits,
   cross-coordinate determinants, norm carries, higher quotient digits,
   and their products lie outside the grammar.
5. Discriminants and coefficient pairs have the stated exact conditional
   laws.  Biased discriminants or other correlated sampling laws are not
   bounded.
6. The decoder can return only through the enumerated gcd screens.  An
   unrestricted decoder using the full relation transcript is not covered.

Accordingly, **PASS** certifies the formal V3 boundary and its quantitative
proof.  It must not be promoted into either an unrestricted lower bound or
an affirmative solution of the integer-factoring prompt.
