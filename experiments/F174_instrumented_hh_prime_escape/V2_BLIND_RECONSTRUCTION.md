# F174 V2 blind reconstruction

## Source lock and verdict

This reconstruction used only **V2_STATEMENT.md**. Its SHA-256 was verified
before it was read:

~~~text
faca4273e53eb04347c07bde9b0fd2fe429f7b681201bec205916cb49d97cecb
~~~

The Harvey--Hittmeir transcript facts in Section 2 and the F172 assertion
that every ordinary common order is at most six are treated as premises.
All other claims below are reconstructed from elementary arithmetic in the
hidden prime-power components.

**Verdict: PASS.** Subject to those two declared premises, the trichotomy,
the repeated-prime-power scope, the exact cutoff constants, every
factor-first branch, and the deterministic QP cost all follow. Here and
below \(C\) is a positive integer, as is implicit in the scan
\(e=1,\ldots,C\) and in the notation
\(C=2^{(\log n)^{O(1)}}\).

## 1. Precise reconstructed claim

There is an absolute threshold \(N_0\) with the following property. Let
\(N\ge N_0\) be any odd composite integer, put

\[
n=\lceil\log_2(N+1)\rceil,
\]

and let \(D,C\) be positive integers satisfying

\[
n\le D<N-1,
\qquad
D,C=2^{(\log n)^{O(1)}}.
\]

The constants in the \(O(1)\) exponents are uniform. They do not depend on
\(N\). There is a deterministic procedure of
\(2^{(\log n)^{O(1)}}\) bit cost that returns exactly one of these public
outputs:

1. a verified divisor \(d\) with \(1<d<N\);
2. a residue \(h\bmod N\), an integer \(L>D\), and the complete
   factorization of \(L\), such that

   \[
   \gcd(L,N)=1,
   \qquad
   \operatorname{ord}_{p^a}(h)=L
   \]

   for every maximal prime power \(p^a\parallel N\); or
3. a residue \(g\bmod N\), a completely factored integer \(M\le D\), and
   a prime integer \(\beta\) satisfying the hard-block properties proved
   in Section 9.

The factorization \(N=\prod_jp_j^{a_j}\) is used only in the proof. The
procedure does not know it. Inputs below \(N_0\) are handled by one fixed
finite table or by direct trial division. Thus finitely many small cases
do not change the uniform claim.

This is a source-and-decoder theorem. Outcomes 2 and 3 are not claimed to
factor \(N\).

## 2. Prime-power facts used by every screen

Write

\[
N=\prod_{j=1}^sR_j,
\qquad R_j=p_j^{a_j},
\]

where the \(p_j\) are distinct odd primes. Two elementary facts make all
gcd screens valid without a squarefreeness assumption.

First, for any integer \(z\):

* \(\gcd(z,N)=N\) means \(z\equiv0\pmod {R_j}\) for every \(j\);
* \(\gcd(z,N)=1\) means \(z\not\equiv0\pmod {p_j}\) for every \(j\); and
* every other gcd is a verified proper factor of \(N\), including a gcd
  that cuts strictly inside one \(p_j^{a_j}\).

Thus a no-factor gcd result of one is stronger than mere noncongruence
modulo \(R_j\). It gives noncongruence even modulo the underlying prime.

Second, for odd \(p\), the group
\((\mathbb Z/p^a\mathbb Z)^\times\) is cyclic. If \(g\) has order \(M\) in
that group and \(H=\langle g\rangle\), then

\[
H=\{x:x^M=1\}.
\tag{2.1}
\]

Indeed, \(M\) divides the group order. A cyclic group has exactly \(M\)
solutions to \(x^M=1\), and \(H\) already supplies \(M\) such solutions.
This equality is valid for every exponent \(a\ge1\).

## 3. Factor-first exact-order certification

Let \(x\) be a unit modulo \(N\). Suppose its exact global order is the
known, completely factored integer \(m\). For every prime \(q\mid m\),
compute

\[
d_q=\gcd(x^{m/q}-1,N).
\tag{3.1}
\]

Since \(m\) is the exact global order, \(d_q\ne N\). If \(d_q\) is neither
one nor \(N\), it is a proper factor. On a no-factor branch every
\(d_q=1\).

Put \(m_j=\operatorname{ord}_{R_j}(x)\). Since \(m_j\mid m\), the relation
\(m_j\mid m/q\) would imply \(x^{m/q}=1\pmod {R_j}\), hence
\(p_j\mid d_q\). Therefore, when \(d_q=1\),

\[
v_q(m_j)=v_q(m)
\qquad(1\le j\le s).
\]

Doing this for every prime divisor \(q\) gives

\[
\operatorname{ord}_{R_j}(x)=m
\qquad(1\le j\le s).
\tag{3.2}
\]

The same power screens prove that the order is coprime to \(N\). If some
hidden prime \(p_j\) divided \(m\), take \(q=p_j\). By (3.2),
\(x^{m/p_j}\) has exact order \(p_j\) modulo \(R_j\). Its reduction modulo
\(p_j\) has order dividing both \(p_j\) and \(p_j-1\), so that reduction is
one. Hence

\[
p_j\mid x^{m/p_j}-1.
\]

This makes \(d_{p_j}\) a nontrivial gcd. It cannot equal \(N\), because
\(m\) is the exact global order. This contradicts the no-factor branch.
Thus

\[
\gcd(m,N)=1.
\tag{3.3}
\]

This is why the factor-first qualifier is essential. A bare exact global
order need not be a common local order. The complete family of
prime-divisor gcd screens supplies both the common-order conclusion and
the coprimality conclusion. It exposes any obstructing prime power as a
factor.

### 3.1. Stripping a factored multiple

There is a related procedure that starts with a completely factored
multiple \(E\) of all local orders. For each prime \(q\mid E\), repeatedly
compute

\[
\gcd(x^{E/q}-1,N).
\]

If the gcd is \(N\), replace \(E\) by \(E/q\). If it is proper, return that
factor. If it is one, retain the current \(q\)-power and move to the next
prime.

The invariant that every local order divides the current \(E\) is
preserved whenever \(q\) is stripped. At the first retained \(q\)-power,
gcd one says that no local order divides \(E/q\). Thus every local order
has the full current \(q\)-adic valuation. At termination, the remaining
integer \(m\) is the exact order in every \(R_j\). The preceding
\(q=p_j\) argument also shows that a no-factor result has
\(\gcd(m,N)=1\).

### 3.2. Public primary-component merge

Suppose public residues \(x,y\) have certified common local orders \(u,v\),
with both factorizations known. Let \(W=\operatorname{lcm}(u,v)\). For
each \(q^b\parallel W\), choose a source whose order has \(q\)-adic
valuation \(b\), and raise that source to its order divided by \(q^b\).
The result has exact order \(q^b\) in every \(R_j\). The product of these
public, pairwise coprime-order primary components has exact order \(W\) in
every \(R_j\). This reconstructs the lcm merge in the transcript. Its
factorization follows directly from those of \(u\) and \(v\).

## 4. The transcript invariant and the line-13 prefix

The early Harvey--Hittmeir return cannot occur under the chosen
parameters. From the definition of \(n\),

\[
N+1\le2^n\le2^D,
\]

so \(2^D<N\) is false.

Start with the trivial state \(g=1,M=1\). Whenever the transcript finds an
exact order through \(D\), apply the screens in Section 3. A screen either
returns a factor or certifies that order in every \(R_j\). The public
primary-component merge then preserves a common exact order and its
complete factorization. Consequently, on every no-factor loop entry,

\[
g^M=1\pmod N,
\qquad
\operatorname{ord}_{R_j}(g)=M\quad(1\le j\le s),
\qquad
\gcd(M,N)=1.
\tag{4.1}
\]

Because the transcript returns immediately after a merge makes \(M>D\),
one also has \(M\le D\) immediately before line 13 or the loop-end scan.

Suppose line 13 is reached at \(\beta\). The external transcript premise
gives

\[
\beta^M\ne1\pmod N,
\qquad
\operatorname{ord}_N(\beta)>D.
\tag{4.2}
\]

Every earlier scanned integer \(a<\beta\) either already satisfied the
then-current \(a^M=1\), or had an exact order found and merged into the
later state. Hence the state at the escape satisfies

\[
a^M=1\pmod N
\qquad(1\le a<\beta).
\tag{4.3}
\]

In particular every such \(a\) is a unit. By (2.1),

\[
a\bmod R_j\in H_j:=\langle g\bmod R_j\rangle
\qquad(1\le a<\beta,\ 1\le j\le s).
\tag{4.4}
\]

Equation (4.2) says \(\beta\) is outside at least one \(H_j\), but it need
not yet be outside all of them.

Finally, \(\beta\) must be prime. If \(\beta=uv\) with
\(1<u,v<\beta\), then (4.3) gives

\[
\beta^M=(uv)^M=u^Mv^M=1\pmod N,
\]

contradicting (4.2). Thus the line-13 escape is a prime integer selected by
the deterministic source order.

## 5. Exact reconstruction of the smooth-prefix cutoff

Define

\[
L_D=\lceil\log_2(2D)\rceil,
\qquad
J_D=\lceil\log_2(L_D+1)\rceil,
\]

\[
H_D=8L_DJ_D,
\qquad
X_D=2^{H_D},
\qquad
Y_D=H_D^2.
\tag{5.1}
\]

For the present parameter range, \(D\ge n\ge4\), so \(L_D\ge3\) and
\(J_D\ge2\). The following exact inequalities explain the constant eight.
Since \(L_D<2^{J_D}\) and \(\log_2J_D\le J_D-1\),

\[
\log_2H_D
=3+\log_2L_D+\log_2J_D
\le4J_D.
\tag{5.2}
\]

Therefore

\[
Y_D^{L_D}=2^{2L_D\log_2H_D}
\le2^{8L_DJ_D}=X_D.
\tag{5.3}
\]

We also need \(L_D\) distinct primes at most \(Y_D\). The elementary
explicit bound for the \(r\)-th prime \(q_r\),

\[
q_r\le2r^2\qquad(r\ge1),
\tag{5.4}
\]

is more than sufficient:

\[
q_{L_D}\le2L_D^2\le H_D^2=Y_D.
\]

This weak prime bound is a standard consequence of Chebyshev's elementary
lower bound for \(\pi(x)\), with the finitely many small indices checked
directly. The statement's absolute small-input convention can also absorb
those finite checks.

Let \(q_1,\ldots,q_{L_D}\) be the first \(L_D\) primes. Their
\(2^{L_D}\) squarefree subset products are distinct, are \(Y_D\)-smooth,
and, by (5.3), are at most \(X_D\). Moreover,

\[
2^{L_D}\ge2D>M.
\tag{5.5}
\]

Assume now that \(\beta-1\ge Y_D\). Each \(q_i<\beta\), so (4.4) puts
every \(q_i\), and hence every subset product, in every \(H_j\).

Fix \(j\). If \(p_j>X_D\), all \(2^{L_D}\) subset products are distinct
after reduction modulo \(p_j\), and therefore after reduction modulo
\(R_j\). This puts more than \(M=|H_j|\) distinct elements in \(H_j\), a
contradiction. Consequently

\[
p_j\le X_D\qquad(1\le j\le s).
\tag{5.6}
\]

By (4.1), \(M\) is coprime to \(p_j\). Since \(M\) is the order of \(g\)
modulo \(p_j^{a_j}\), it divides \(p_j^{a_j-1}(p_j-1)\). Coprimality
therefore gives

\[
M\mid p_j-1.
\tag{5.7}
\]

Thus every \(p_j\) occurs among the integers

\[
kM+1\le X_D,\qquad k\ge1.
\]

Scanning these integers and taking their gcds with \(N\) encounters
\(p_j\) and returns the proper factor \(p_j\). This also works when
\(N=p_j^{a_j}\), because then \(a_j\ge2\) and \(p_j<N\).

It follows contrapositively that a no-factor line-13 escape has the exact
bound

\[
2\le\beta\le Y_D=H_D^2.
\tag{5.8}
\]

Indeed, \(\beta>Y_D\) is the same integer condition as
\(\beta-1\ge Y_D\). Finally,

\[
L_D=O(\log D),
\qquad
J_D=O(\log\log D),
\]

so

\[
Y_D=O((\log D\log\log D)^2).
\tag{5.9}
\]

Because \(D=2^{(\log n)^{O(1)}}\), (5.8) gives

\[
\beta=(\log n)^{O(1)}.
\tag{5.10}
\]

This is stronger than the transcript's literal
\(\beta\le\lceil D^{1/3}\rceil\).

## 6. Absolute-order screen

Let

\[
\Lambda_D=\operatorname{lcm}(1,2,\ldots,D),
\qquad
A_\beta=\gcd(\beta^{\Lambda_D}-1,N).
\tag{6.1}
\]

For any integer \(t\ge1\), the factorization of \(\Lambda_D\) gives

\[
t\mid\Lambda_D
\quad\Longleftrightarrow\quad
\ell^{v_\ell(t)}\le D\text{ for every prime }\ell\mid t
\quad\Longleftrightarrow\quad
\sigma(t)\le D.
\tag{6.2}
\]

There are three exhaustive gcd outcomes.

### 6.1. A proper gcd

If \(1<A_\beta<N\), return \(A_\beta\). This includes a divisor that
contains only a proper power of some \(p_j\). No squarefree assumption is
used.

### 6.2. The gcd is \(N\)

If \(A_\beta=N\), every local order

\[
t_j=\operatorname{ord}_{R_j}(\beta)
\]

divides \(\Lambda_D\). Apply the factor-first stripping procedure of
Section 3 to this known factored multiple. It either exposes a proper
factor or leaves a completely factored integer \(m\) such that

\[
\operatorname{ord}_{R_j}(\beta)=m
\quad(1\le j\le s),
\qquad
\gcd(m,N)=1.
\tag{6.3}
\]

The global order of \(\beta\) is then \(m\). The line-13 premise (4.2)
forces

\[
m>D.
\tag{6.4}
\]

Thus \((\beta,m)\) is an exact common-order state above the target.

### 6.3. The gcd is one

If \(A_\beta=1\), then, for every \(j\),
\(\beta^{\Lambda_D}\not\equiv1\pmod {p_j}\), and hence not modulo \(R_j\).
Thus \(t_j\nmid\Lambda_D\). By (6.2),

\[
\sigma(t_j)>D
\qquad(1\le j\le s).
\tag{6.5}
\]

In particular, every local absolute order is greater than \(D\), and
\(\beta\) is outside every \(H_j\). Only this gcd-one case continues to
the relative scan.

## 7. Relative-order screen

For the remainder of the proof assume \(A_\beta=1\). Define

\[
e_j=\operatorname{ord}_{(\mathbb Z/R_j\mathbb Z)^\times/H_j}
(\beta H_j).
\tag{7.1}
\]

By (2.1), for every positive integer \(e\),

\[
\beta^e\in H_j
\quad\Longleftrightarrow\quad
\beta^{eM}=1\pmod {R_j}.
\tag{7.2}
\]

Therefore \(e_j\) is exactly the least positive \(e\) for which the
right-hand congruence holds.

Compute, in increasing order for \(1\le e\le C\),

\[
G_e=\gcd(\beta^{eM}-1,N).
\tag{7.3}
\]

Again there are three exhaustive behaviors.

### 7.1. A proper gcd occurs

If any \(G_e\) is proper, return it. Partial divisibility inside a repeated
prime power is still a valid factor.

### 7.2. The first global return occurs

Suppose the first non-one value is \(G_e=N\). Every earlier no-factor value
was one, so (7.2) gives

\[
e_j=e
\qquad(1\le j\le s).
\tag{7.4}
\]

The value \(e\) cannot be one. Since \(M\le D\), one has
\(M\mid\Lambda_D\). If \(\beta^M=1\pmod {p_j}\) for any \(j\), then
\(\beta^{\Lambda_D}=1\pmod {p_j}\), contradicting \(A_\beta=1\). Hence
\(G_1=1\) and

\[
e\ge2.
\tag{7.5}
\]

Let \(t_j=\operatorname{ord}_{R_j}(\beta)\). In the cyclic local unit
group,

\[
|\langle g,\beta\rangle|/|H_j|=e_j.
\]

The subgroup generated by elements of orders \(M\) and \(t_j\) in a
cyclic group has order \(\operatorname{lcm}(M,t_j)\). Consequently,

\[
L:=Me
=\operatorname{lcm}(M,t_j)
\qquad(1\le j\le s),
\tag{7.6}
\]

and hence

\[
L=\operatorname{lcm}(M,\operatorname{ord}_N(\beta)).
\tag{7.7}
\]

There is a public common-order generator even though the individual
\(t_j\) are unknown. Factor \(e\), so the complete factorization of
\(L=Me\) is known. For each \(q^b\parallel L\), define

\[
w_q=
\begin{cases}
g^{M/q^b},&v_q(M)=b,\\[3pt]
\beta^{L/q^b},&v_q(M)<b.
\end{cases}
\tag{7.8}
\]

In the first case \(w_q\) has exact order \(q^b\) in every \(R_j\). In the
second case, (7.6) forces \(v_q(t_j)=b\) and \(t_j\mid L\), so
\(\beta^{L/q^b}\) also has exact order \(q^b\) in every \(R_j\). Therefore

\[
h=\prod_{q^b\parallel L}w_q\pmod N
\tag{7.9}
\]

has exact order \(L\) in every hidden component.

Apply the factor-first prime-divisor screens to this proposed common state.
They either expose a proper factor or certify the state. In particular, a
no-factor state has \(\gcd(L,N)=1\), by Section 3. Furthermore, (4.2) and
(7.7) give

\[
L>D.
\tag{7.10}
\]

Equation (7.5) also shows strict growth \(L=Me>M\).

### 7.3. Every scanned gcd is one

If \(G_e=1\) for every \(1\le e\le C\), then (7.2) gives

\[
e_j>C
\qquad(1\le j\le s).
\tag{7.11}
\]

This is the hard-block branch.

## 8. Exhaustiveness of the three outputs

The branches are deterministic and mutually exclusive.

* A Harvey--Hittmeir factor, a loop-end arithmetic-progression factor, a
  proper smooth-prefix gcd, a proper absolute gcd, a proper stripping gcd,
  a proper relative gcd, or a proper certification gcd is Outcome A.
* A Harvey--Hittmeir merge that first raises \(M\) above \(D\), the
  \(A_\beta=N\) stripped state, or a relative first-global-return state is
  Outcome B. In every case the public order is completely factored, is
  coprime to \(N\), is exact in every \(R_j\), and exceeds \(D\).
* The only remaining route is a line-13 escape followed by \(A_\beta=1\)
  and \(G_e=1\) for all \(1\le e\le C\). This is Outcome C.

No gcd has a fourth status besides one, proper, and \(N\). The external
transcript premise says that finishing the main loop returns a prime factor
of composite \(N\). Hence no execution path is omitted.

## 9. Exact hard-block content

On Outcome C the public tuple \((g,M,\beta)\) has a completely factored
\(M\) and satisfies, for every \(j\),

\[
\operatorname{ord}_{R_j}(g)=M\le D,
\qquad
\gcd(M,N)=1,
\tag{9.1}
\]

\[
2\le\beta\le H_D^2
=O((\log D\log\log D)^2)
=(\log n)^{O(1)},
\qquad
\beta\text{ is prime},
\tag{9.2}
\]

\[
a\bmod R_j\in H_j
\quad\text{for every integer }1\le a<\beta,
\tag{9.3}
\]

and

\[
\sigma(\operatorname{ord}_{R_j}(\beta))>D,
\qquad
e_j>C.
\tag{9.4}
\]

The first \(C+1\) public fingerprints

\[
1,\beta^M,\beta^{2M},\ldots,\beta^{CM}
\tag{9.5}
\]

are distinct modulo every \(R_j\). An equality between the \(r\)-th and
\(s\)-th entries, with \(0\le r<s\le C\), would give
\(\beta^{(s-r)M}=1\pmod {R_j}\), contradicting \(e_j>C\).

More explicitly, the \(M(C+1)\) residues

\[
g^u\beta^v,
\qquad
0\le u<M,\quad0\le v\le C,
\tag{9.6}
\]

are distinct in every \(R_j\). If two were equal, cancellation would put
\(\beta^{v-v'}\) in \(H_j\). Raising to \(M\) would contradict (7.11)
unless \(v=v'\), after which the exact order of \(g\) forces \(u=u'\).
Thus the public factor-first table certifies

\[
|\langle g,\beta\rangle_{R_j}|
=M e_j
\ge M(C+1)
\qquad(1\le j\le s).
\tag{9.7}
\]

It does not certify that the unknown integers \(e_j\) are equal, and it
does not provide their exact values.

## 10. Deterministic QP cost

All costs below are bit costs in the input length \(n\).

1. **Harvey--Hittmeir source.** The permitted premise gives

   \[
   O\!\left(
   \frac{D^{1/2}\log D}{(\log\log D)^{1/2}}\log N
   \right),
   \]

   which is QP for QP \(D\).

2. **The smooth-prefix scan.** By (5.1),

   \[
   \log_2X_D=H_D
   =O(\log D\log\log D)
   =(\log n)^{O(1)}.
   \]

   Hence the numerical number \(X_D\), not only its encoding length, is
   QP. There are at most \(X_D\) candidate gcds \(kM+1\le X_D\), and each
   gcd has polynomial bit cost in \(n+H_D\). Their total is QP.

3. **The absolute screen.** The factorization

   \[
   \Lambda_D=\prod_{q\le D}q^{\lfloor\log_qD\rfloor}
   \]

   is obtained by a sieve through \(D\). The elementary bound

   \[
   \log_2\Lambda_D\le D\log_2D
   \]

   suffices. Constructing its factored representation, computing one
   modular power with this exponent, and performing at most
   \(O(D\log D)\) stripping attempts all have deterministic QP bit cost.

4. **The relative scan.** It uses \(C\) modular powers and gcds. The
   exponents have bit length \(O(\log C+\log D)\), so the total is QP.
   Factoring the returned index \(e\le C\), even by deterministic trial
   division or a sieve, is also QP.

5. **Certificates and public words.** The common-order merges use at most
   one primary component per prime divisor of the factored order. Modular
   residues use \(O(n)\) bits, and their exponents and factorizations have
   QP length. A straight-line provenance word therefore has QP encoding
   length. If the full hard-block table (9.6) is materialized, it has at
   most \(D(C+1)\) entries and hence QP size.

Composing finitely many deterministic QP stages remains deterministic QP.
All hidden constants are fixed independently of \(N\), which establishes
the uniform cost quantifier.

## 11. Consequence for the F172 family

Now use the second and only other external premise: on the F172 family,
every ordinary common order is at most six. Choose a valid \(D>6\).
Outcome B would exhibit one public residue having the same exact local
order \(L>D>6\) in every hidden component, contradicting that premise.
Therefore, on this family, the deterministic source obeys

\[
\boxed{
\text{proper factor}
\quad\lor\quad
\text{algorithm-selected polylog-small prime hard block}.}
\tag{11.1}
\]

The prime is algorithm-selected because it is the first source integer
whose order search reaches line 13. It is not a witness supplied with the
input.

Moreover, in the hard branch the local orders of \(\beta\) cannot all be
equal. If they were all one integer \(t\), then \(\beta\) itself would have
ordinary common order \(t\), while (9.4) would give \(t>D>6\). Thus a
hidden order mismatch exists. None of the public gcd results identifies
which components disagree, so the procedure does not locate that mismatch
in QP time.

## 12. Scope audit and exact nonclaims

The reconstructed proof establishes universal statements over **all**
maximal odd prime powers \(p_j^{a_j}\parallel N\). It never silently
replaces them by primes or assumes \(N\) squarefree. Intermediate
\(p_j\)-adic gcds are factors, while no-factor gcd-one and gcd-\(N\)
results supply exactly the strong endpoint information used above.

The proof gives no implication beyond its displayed branches. In
particular, it does not show that the hard branch is empty. The conditions

\[
\sigma(\operatorname{ord}_{R_j}(\beta))>D
\quad\text{and}\quad e_j>C
\]

hold component by component but do not align the hidden primary orders or
make the \(e_j\) equal. Therefore they do not yield a useful exact common
order. The finite equality bank certifies only the first \(C+1\) distinct
fingerprints. The small retained integer presentation of \(\beta\)
supplies no factor-correlated inverse identity. No step transfers the
order to a Jacobi-minus-one torus, reaches a separate dual-CRT threshold,
or turns the trichotomy into deterministic or Las Vegas QP factoring.

Accordingly, the exact surviving problem is the one stated: detect and use
a hidden local-order mismatch, certify a common hard order without already
knowing it, or exploit the retained presentation of the selected
polylog-small prime to force a useful exact relation.
