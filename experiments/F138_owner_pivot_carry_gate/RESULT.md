# F138 — max-digit owner pivots need not close

## Verdict

The proposed auxiliary claim is false as stated:

> Under the complete adaptive F130/F132/F133 source, old columns or different
> anchored stars must eventually cancel the max-digit owner pivots and create
> a nonzero P66 kernel.

There are two separate failures.

1. A literal full-budget integer-anchor arm can contain a row that is private
   in the **complete canonical-inverse universe**. No old column, later
   block, or different star can reuse it. A smaller prime-anchor certificate
   gives the same phenomenon.
2. Even if every displayed row is reused and the selected matrix has no
   degree-one row, the columns can still have full rank and zero kernel.

The first failure has a proof-verified 400-bit balanced semiprime certificate.
It passes the full initial F130 seed bank by an exact size bound. The second
failure has a four-column exact canonical certificate.

This is not a complete-source obstruction. A later F130 word can still return
a factor, and other columns can still create a useful P66 kernel.

## Closest prior results and material change

- P111 proves the general carry-congruence test for prime-row incidence.
- P112 proves that a row above \((N-1)/2\) is private in the complete
  canonical universe. Its finite witness is not hard for the later F130 seed
  bank, and F122 found a factor before feedback on that input.
- P120/X73 proves that one reused row need not close.
- P122/X74 proves that one anchored star cannot share unrelated fresh rows
  above the carry range.
- F135 gives an abstract expanding forest and a selected canonical depth-two
  forest.

The material change is exact alignment with the new claim. The strongest
protected row below occurs at the largest declared F133 integer anchor
\(a=E\) and its largest digit \(A=E-1\). Its residue \(2E\) is beyond the
initial seed bank. Its input has factors larger than the square of that
residue. A second certificate gives the same privacy at the prime anchor
\(3\). The small four-column certificate then closes the separate logical
gap from row reuse to kernel existence.

## Theorem 1 — the exact old/cross-star carry gate

For every unit \(c\in\{1,\ldots,N-1\}\), put

\[
P_N(c)=c\iota_N(c)=1+\kappa_N(c)N.
\]

Since both canonical endpoints are below \(N\),

\[
0\le\kappa_N(c)\le N-2.
\]

Exact-value deduplication is exactly carry deduplication: for fixed \(N\),

\[
1+\kappa N=1+\lambda N
\iff
\kappa=\lambda.
\]

Let \(\mathcal K\) be the final set of retained carries. For a prime \(r\),
the exact row degree is

\[
\boxed{
\deg(r)=
\#\{\kappa\in\mathcal K:
v_r(1+\kappa N)\equiv1\pmod2\}.}
\tag{1}
\]

If \(r\) occurs in two distinct columns with carries \(\kappa,\lambda\),
then \(r\nmid N\) and

\[
\boxed{\kappa\equiv\lambda\pmod r.}
\tag{2}
\]

Indeed, subtracting the two exact values gives

\[
(1+\kappa N)-(1+\lambda N)=N(\kappa-\lambda).
\]

Conversely, if \(r\mid1+\kappa N\) and
\(\lambda\equiv\kappa\pmod r\), then \(r\mid1+\lambda N\).
Odd valuation in the second value is still required for parity-row reuse.

Now let a star have base block \(b\), inverse \(w_b\), and unary carry

\[
bw_b=1+k_bN.
\]

Its digit-\(A\) exact value is

\[
b(w_b+NA)=1+(k_b+bA)N.
\]

Thus its carry is the affine value

\[
\boxed{\kappa(b,A)=k_b+bA.}
\tag{3}
\]

For a second star \((d,B)\), a shared prime row requires

\[
\boxed{
k_b+bA\equiv k_d+dB\pmod r.}
\tag{4}
\]

Equation (4), plus odd valuation in both columns, is the exact cross-star
gate. More blocks, rounds, or relations do not remove it. A progress theorem
must prove that the adaptive final carry set hits these hidden residue
classes. Relation count alone does not do this.

## Theorem 2A — the full-budget max-digit arm has a universe-private row

Let

\[
\begin{aligned}
p={}&1440575060366591719164812115423434185454445360021359262957569,\\
q={}&1531570574064344929935978281536186047620048484429603222323201,
\end{aligned}
\]

and put \(N=pq\). Define \(n,L,E\) as in F130, and put

\[
a=E,
\qquad
c=2E,
\qquad
A=E-1,
\qquad
r={1+(c-1)N\over c}.
\]

Their exact decimal values are

```text
N = 2206342372188439231071704119788681118383639175630092611385003672288203658512531224766164082517129137765776226834467258369
r = 2206342372188439231071703663527772386250305539544495574654345939408069421197500116321867676177152627713145274674754869377
```

The registered verifier proves that \(p,q,r\) are prime, that
\(p<q<2p\), and that

\[
n=400,
\qquad
L=9,
\qquad
E=2^{81}.
\]

It also proves

\[
N\equiv1\pmod c,
\qquad
c^2+1<p<q.
\]

Every initial F130 seed satisfies \(2\le s\le E+1<c<p\). Also

\[
0<s^2-1<s^2+1<c^2+1<p.
\]

Thus all initial trial gcds and endpoint sign gcds are one.

Now use the current all-block generator \(b=2\), whose inverse is

\[
w_2={N+1\over2}.
\]

The F133 source scans every integer anchor through \(E\). At the largest
anchor \(a=E\), take its largest digit \(A=a-1\). Then

\[
H=w_2+AN=ar.
\]

The selected endpoints are

\[
ab=2E=c,
\qquad
{H\over a}=r.
\]

They are canonical and give

\[
\boxed{P_N(c)=cr=1+(c-1)N.}
\]

The residue is beyond the initial seed bank because \(c=2E>E+1\). Both
endpoint sign screens are one. The prime \(r\) occurs to valuation one.
Also,

\[
r=N-{N-1\over c}>{N-1\over2}.
\]

Therefore \(r\) is the only positive multiple of itself below \(N\). Any
canonical exact value divisible by \(r\) must use endpoint \(r\), whose
unique inverse is \(c\). Global exact-value deduplication leaves exactly one
\(r\)-column:

\[
\boxed{\deg(r)=1
\quad\text{in the complete canonical-inverse universe}.}
\]

No old relation or different star can cancel this full-budget max-digit row.
In fact, the same residue is the first-stage F130 support-one word
\(2^{82}=2E\), because exponent \(82\) is below \(E\). Its later F133
occurrence is an exact duplicate. The first copy already owns the same
permanently private row, and deduplication cannot create a second column.

The integer anchor \(a=E\) is not prime, so P121's prime-product width
theorem is not invoked. This is a guaranteed position of the full integer
anchor source in F133 Theorem 5 if execution reaches that scan.

Thus the certificate refutes a claim about **all** max-digit owner pivots in
the combined source. It does not refute a narrower claim restricted to
globally new F133 exact values. Such a claim needs “globally new” as an
explicit hypothesis and still faces the rank obstruction in Theorem 3.

## Theorem 2B — the same obstruction at a prime anchor

Let

\[
\begin{aligned}
p={}&1320008795989904748182462774062723291576584579927832140369037,\\
q={}&1483391727238122164760277073344336797129797980984686650045533,
\end{aligned}
\]

and put \(N=pq\) and \(r=(5N+1)/6\). Their exact decimal values are

```text
N = 1958090127852978830975606630525183532915462684425760907751271701246799901589218459681729024239617354885430788103473361721
r = 1631741773210815692479672192104319610762885570354800756459393084372333251324348716401440853533014462404525656752894468101
```

The registered proof-enabled Sage verifier certifies that \(p,q,r\) are
prime, that

\[
p<q<2p,
\qquad
N\equiv1\pmod6,
\qquad
6r=5N+1,
\tag{5}
\]

and that \(N\) has 400 bits.

### The complete initial F130 seed bank is null

For this input,

\[
n=400,
\qquad
L=9,
\qquad
E=2^{81}
=2417851639229258349412352.
\]

The verifier certifies

\[
(E+1)^2+1<p<q.
\tag{6}
\]

The F130 initial seeds are \(2\le s\le E+1\). Equation (6) gives
\(s<p,q\), so every trial gcd is one. For \(w_s=\iota_N(s)\),

\[
\gcd(s-w_s,N)=\gcd(s^2-1,N),
\qquad
\gcd(s+w_s,N)=\gcd(s^2+1,N).
\]

Both nonzero integers \(s^2-1,s^2+1\) are smaller than \(p\). Hence every
initial endpoint sign screen is one. The input reaches the first adaptive
F130 stage.

This argument does not claim that all later F130 word screens are null.

### The literal F133 arm

Use base block \(b=2\). Since \(N\) is odd,

\[
w_2=\iota_N(2)={N+1\over2}.
\]

Take the public prime anchor \(\ell=3\) and its maximum digit \(A=2\).
Then

\[
H=w_2+2N={5N+1\over2}=3r.
\tag{7}
\]

Thus \(A=2\) is exactly the unique eligible carry digit modulo \(3\), and
the canonical anchored endpoints are

\[
c=\ell b=6,
\qquad
z={H\over\ell}=r.
\]

They give

\[
\boxed{
P_N(6)=6r=1+5N.}
\tag{8}

Both sign screens are one. The prime \(r\) occurs to valuation one in (8).

Finally, (5) gives

\[
r={5N+1\over6}>{N-1\over2}.
\tag{9}

The only positive multiple of \(r\) below \(N\) is \(r\) itself. Therefore
any canonical exact value divisible by \(r\) must use endpoint \(r\). Its
other endpoint is uniquely \(6\). After global exact-value deduplication,
equation (8) is the only column containing row \(r\):

\[
\boxed{\deg(r)=1
\quad\text{in the complete canonical-inverse universe}.}
\tag{10}

Every F130, F132, and F133 relation is a canonical exact value inside this
universe. Hence no old column, later round, new block, or different anchored
star can cancel this max-digit owner row.

This disproves universal owner-pivot cancellation. It does not show that
other columns have zero kernel.

## Theorem 3 — complete row reuse still does not imply a kernel

Take

\[
N=161=7\cdot23.
\]

The following four endpoint pairs are canonical inverse pairs, and every
displayed sign screen is one:

\[
\begin{array}{c|c|c|c}
c&w&P_N(c)&\kappa\\ \hline
10&145&1450&9\\
26&31&806&5\\
32&156&4992&31\\
87&124&10788&67.
\end{array}
\tag{11}
\]

Their exact factorizations are

\[
\begin{aligned}
1450&=2\cdot5^2\cdot29,\\
806&=2\cdot13\cdot31,\\
4992&=2^7\cdot3\cdot13,\\
10788&=2^2\cdot3\cdot29\cdot31.
\end{aligned}
\tag{12}
\]

On rows \((2,3,13,29,31)\), the complete parity matrix is

\[
M=
\begin{pmatrix}
1&1&1&0\\
0&0&1&1\\
0&1&1&0\\
1&0&0&1\\
0&1&0&1
\end{pmatrix}.
\tag{13}
\]

Its row degrees are

\[
(3,2,2,2,2).
\]

Thus it has no degree-one row. Every prime row is reused.

Nevertheless, \(M\) has rank four. To see this without computation, let a
kernel vector be \((x_1,x_2,x_3,x_4)\). Rows \(13,3,29\) give

\[
x_2=x_3=x_4=x_1.
\]

The row \(2\) then gives

\[
x_1+x_2+x_3=x_1=0.
\]

Therefore

\[
\boxed{\ker M=0.}
\tag{14}
\]

The registered verifier reconstructs all factorizations, screens, row
degrees, rank, and nullity. This is a selected canonical certificate. Other
presentations or source columns at \(N=161\) are outside its scope.

## Exact missing condition

The current proposal uses this invalid implication:

\[
\text{owner rows are reused}
\quad\Longrightarrow\quad
\text{a P66 dependency exists}.
\]

The exact replacement has two gates.

### Gate 1 — carry-class hitting

For every owner row that the proof needs to eliminate, another retained carry
must satisfy (2), and both valuations must be odd. For two anchored stars,
this is the affine condition (4). The complete adaptive source currently has
no theorem that forces these hits. Theorems 2A and 2B show that a universal
version is false.

### Gate 2 — rank closure after reuse

Even after a row is reused, F132's splice law requires the residual symmetric
difference to lie in the old column span. For a complete layer, the required
statement is a rank defect

\[
\boxed{
\operatorname{rank} M_{\mathrm{final}}
<\#\{\text{distinct retained exact carries}\}.}
\tag{15}
\]

Minimum row degree two, a nonempty 2-core, and cancellation of every named
owner row do not imply (15). Theorem 3 is an exact four-column counterexample.
The finite-round expanding forest gives another obstruction: each round can
reuse old pivots while the last round creates fresh leaf pivots.

After (15), one more independent theorem must show that the normalized-root
image is non-global. Kernel existence alone does not factor \(N\).

## Consequence for the feedback route

This result does not close feedback. It removes one proposed shortcut.

The next positive theorem cannot say only that old columns or different stars
eventually touch the owner rows. It must prove a final carry-class collision
pattern that causes an actual rank defect, and then prove a non-global root.
An equivalent negative result would control the complete adaptive carry set
and preserve enough private or independent pivots through the final round.
