# Verdict: PASS

The supplied statement has SHA-256
`46144733d8239f5914209b06be43809d742eb151177a07dae3638f69cb811494`.
Every mathematical claim follows from the stated setup. The occurrence and
menu claims hold with exactly the stated conditions: inverse orbits are
deduplicated, the menu uses two distinct blocks with exponents only in
`{-1,1}`, there is no free global minus sign, and an identical append is a
no-op unless an algorithm separately records and charges an occurrence.

## 1. Torsion gcds

Fix a prime \(\ell\mid N\). Since \(rw\equiv1\pmod\ell\), both \(r\) and
\(w\) are nonzero modulo \(\ell\), and \(w\equiv r^{-1}\pmod\ell\). Hence

\[
\ell\mid d
\iff r\equiv r^{-1}\pmod\ell
\iff r^2\equiv1\pmod\ell.
\]

Also,

\[
d^2+4\equiv(r-r^{-1})^2+4
=r^{-2}(r^2+1)^2\pmod\ell.
\]

Because a field has no nonzero nilpotents,

\[
\ell\mid d^2+4\iff r^2\equiv-1\pmod\ell.
\]

For squarefree \(N=pq\), a gcd with \(N\) is determined by the set of
primes among \(p,q\) that divide its other argument. The two equivalences
therefore give

\[
\gcd(d,N)=\gcd(r^2-1,N),\qquad
\gcd(d^2+4,N)=\gcd(r^2+1,N).
\]

No prime divisor of the odd number \(N\) can occur in both gcds: that would
give \(r^2\equiv1\equiv-1\pmod\ell\), so \(\ell\mid2\). Thus the gcds are
coprime. Squarefreeness is essential for the second displayed equality, not
merely cosmetic. For example, for \(N=25,r=2,w=13\), one has
\(d^2+4=125\), so its gcd with \(25\) is \(25\), whereas
\(\gcd(r^2+1,25)=5\).

Now suppose \(\delta>0\). Since \(|d|<N\), \(\gcd(\delta,N)\) cannot be
\(N\). It is greater than one exactly when a prime divisor of \(N\) divides
\(r^2-1=(r-1)(r+1)\), which is exactly when one of the two sign gcds is a
proper factor. In that event \(\gcd(\delta,N)\) is \(p\) or \(q\), and
therefore

\[
\delta\geq \min(p,q).
\]

If \(\delta=0\), then \(r=w\) and \(r^2\equiv1\pmod N\). CRT gives the four
local sign choices \((1,1),(1,-1),(-1,1),(-1,-1)\). The two equal-sign
choices are the global roots \(1,N-1\); one sign gcd is \(N\) and the other
is \(1\). For either mixed choice, the two sign gcds are \(p\) and \(q\).
Finally, inversion preserves each local sign: \(w\equiv 1\) exactly where
\(r\equiv1\), and likewise for \(-1\). Thus \(r\) and \(w\) have identical
direct sign gcds.

This proves that the discriminant gcd detects precisely the distinct local
event \(r^2=-1\). Once both torsion gcds are one, these equivalences supply no
additional torsion conclusion from the magnitude of \(\delta\).

## 2. Square endpoints and inverse fibres

Take \(m\) to be the positive square root of \(rw\). Since
\(1\leq r,w\leq N-1\), the equality \(m=1\) would force \(r=w=1\), and
\(m=N-1\) would force \(r=w=N-1\). Both contradict \(r\ne w\). Hence

\[
2\leq m\leq N-2.
\]

Moreover, \(m^2=rw\equiv1\pmod N\). The bounds exclude both global roots,
so \(m\) is a mixed CRT root. Consequently \(\gcd(m-1,N)\) and
\(\gcd(m+1,N)\) are the two factors.

If \(|r-w|=1\), then \(r,w\) are coprime consecutive positive integers. If
their product were a square, unique factorization would make each of them a
square. No two positive consecutive squares exist. Thus a distance-one pair
cannot have square product.

For a fixed signed integer \(d\), every corresponding state satisfies

\[
r^2-dr-1\equiv0\pmod N.
\]

This monic quadratic has at most two roots modulo each of \(p,q\), hence at
most four modulo \(N\) by CRT. There is one possible signed value at zero and
at most \(2D\) nonzero signed values with \(|d|\leq D\). Therefore there are
at most

\[
4+2D\cdot4=4+8D
\]

oriented states. Every nonzero-distance inverse orbit has two orientations,
while each zero-distance root is a singleton, giving at most \(4+4D\)
unordered inverse pairs. These are upper bounds on the full inverse graph;
they do not assert that any transcript menu reaches one of those states.

## 3. Exhaustion, ranking, and occurrences

Exhaustive screening evaluates the same finite set of distinct inverse
orbits regardless of their order, so sorting cannot alter whether the current
round has a direct success. After a miss, the next exact menu is again a
function of the gcd-free block presentation. If an append changes neither
that presentation nor a separately authorized occurrence state, it leaves
the algorithmic state and rebuilt menu unchanged. There is no unstated
budget whose decrement could create progress.

This does not identify an orbit only by its residue. Two realizations of the
same residue can have different exact integer endpoints. A new realization
can introduce a new gcd between endpoints and thereby refine the integer
blocks, even though the modular relation value is unchanged.

## 4. Finite obstructions

### \(N=77\)

Here \(2^{-1}=39\) and \(39^{-1}=2\pmod{77}\). The four allowed signed
products from the only distinct block pair are

\[
2\cdot39\equiv1,\quad
2^{-1}39^{-1}\equiv1,\quad
2\cdot39^{-1}\equiv4,\quad
2^{-1}39\equiv58\pmod{77}.
\]

Also \(4\cdot58=232=1+3\cdot77\). After duplicate inverse orbits are
removed, the raw menu is exactly

\[
\{1\},\qquad\{4,58\}.
\]

For the nontrivial orbit, \(\delta=54\), and

\[
\gcd(54,77)=1,\qquad
\gcd(54^2+4,77)=\gcd(2920,77)=1.
\]

Thus both tickets fail. The identity has score zero, while the other orbit
has positive score. A variant that retains the identity and takes \(K=1\)
therefore selects it again. If re-appending its already-known endpoint
relation changes neither blocks nor an explicit occurrence box, the entire
state repeats exactly. This is the claimed conditional fixed point. The
specified filtered algorithm removes \(\{1\}\), so it does not have this
identity loop.

The minimality claim has a non-enumerative prime proof. Modulo \(3\), every
unit squares to \(1\). Modulo \(5\), every unit squares to \(1\) or \(-1\).
Therefore a semiprime having factor \(3\) or \(5\) cannot have both torsion
gcds equal to one. If a product of two distinct odd primes has neither
factor, it is at least \(7\cdot11=77\). At \(77\), the unit \(r=4\) is not a
global sign and satisfies

\[
\gcd(4^2-1,77)=\gcd(15,77)=1,\qquad
\gcd(4^2+1,77)=\gcd(17,77)=1.
\]

Hence \(77\) is exactly the smallest such semiprime.

### \(N=209\): failure of distance monotonicity

The identities

\[
80\cdot81=6480=1+31\cdot209,\qquad
10\cdot21=210=1+209
\]

show that both displayed pairs are inverse pairs. The first has distance one,
with direct gcd \(\gcd(1,209)=1\) and discriminant gcd
\(\gcd(5,209)=1\). The second has distance eleven and immediately gives

\[
\gcd(10+1,209)=11.
\]

Thus a strictly smaller positive distance can be worse for direct
factorization.

### \(N=143\): failure of singleton square closure

Direct multiplication gives

\[
\begin{aligned}
9\cdot16&=144=1+143,\\
61\cdot68&=4148=1+29\cdot143,\\
75\cdot82&=6150=1+43\cdot143,\\
127\cdot134&=17018=1+119\cdot143.
\end{aligned}
\]

All four are inverse pairs of distance seven. Since

\[
\gcd(7,143)=1,\qquad \gcd(7^2+4,143)=\gcd(53,143)=1,
\]

their direct and discriminant outcomes are all trivial. The first product is
\(12^2\), and

\[
\gcd(12-1,143)=11,\qquad \gcd(12+1,143)=13.
\]

The remaining products are nonsquares because

\[
64^2<4148<65^2,\qquad
78^2<6150<79^2,\qquad
130^2<17018<131^2.
\]

Equal metric and torsion outcomes therefore do not determine square closure.

## 5. Representation-level feedback at \(N=209\)

The starting equalities are exact:

\[
31\cdot27=837=1+4\cdot209,\qquad
3\cdot70=210=1+209.
\]

Because \(27=3^3\) and \(3,31,70\) are pairwise coprime, complete gcd-free
refinement gives exactly the old block types \(\{3,31,70\}\).

Put \(a=3\) in \((\mathbb Z/209\mathbb Z)^\times\). The two relations give

\[
70=a^{-1},\qquad31=a^{-3}.
\]

For the three distinct block pairs, all allowed exponent choices reduce to
the following powers:

\[
\begin{array}{c|c}
\text{block pair}&\text{powers obtained}\strut\\ \hline
(3,31)&a^{-2},a^2,a^{-4},a^4\\
(3,70)&1,a^2,a^{-2},1\\
(31,70)&a^{-4},a^{-2},a^2,a^4.
\end{array}
\]

Thus, after inverse-orbit deduplication, there can be only the identity and
the \(a^{\pm2}\), \(a^{\pm4}\) orbits. Their canonical values are

\[
a^2=9,\qquad a^{-2}=93,\qquad
a^4=81,\qquad a^{-4}=80,
\]

as witnessed by \(9\cdot93=837=1+4\cdot209\) and
\(80\cdot81=6480=1+31\cdot209\). Therefore the exact menu, apart from the
filtered identity, is precisely

\[
\{9,93\},\qquad\{80,81\}.
\]

For \(\{80,81\}\), the direct and discriminant gcds are respectively
\(\gcd(1,209)=1\) and \(\gcd(5,209)=1\). For \(\{9,93\}\), they are

\[
\gcd(84,209)=1,\qquad \gcd(84^2+4,209)=\gcd(7060,209)=1.
\]

Neither endpoint product is a square:
\(80^2<6480<81^2\) and \(28^2<837<29^2\). Hence both nontrivial orbits
survive all stated immediate screens. Their positive inverse distances are
\(1\) and \(84\), so \(\{80,81\}\) is uniquely lowest.

Appending that orbit supplies the exact relation

\[
80\cdot81=1+31\cdot209.
\]

Joint integer refinement uses

\[
80=2^4\cdot5,\qquad81=3^4,\qquad
70=2\cdot5\cdot7,\qquad27=3^3.
\]

Together with the existing \(31\), the resulting pairwise-coprime block
types are exactly \(\{2,3,5,7,31\}\). Since \(2\) and \(5\) are distinct
blocks, the next exact two-block menu contains their allowed positive product
\(2\cdot5=10\), and \(\gcd(10+1,209)=11\).

It remains to check that this is a genuine subgroup enlargement, including
arbitrary old-block integer exponents. Before feedback, every such monomial
has residue

\[
3^x31^y70^z\equiv3^{x-3y-z}\pmod{209}
\]

for integers \(x,y,z\). Conversely the block \(3\) is present, so the old
generated subgroup is exactly \(H_0=\langle3\rangle\).

Modulo \(11\), the element \(3\) has order five:

\[
\langle3\rangle=\{1,3,9,5,4\}\pmod{11}.
\]

It does not contain \(-1\equiv10\pmod{11}\). Therefore \(10\notin H_0\)
modulo \(209\), and no choice of arbitrary integer exponents on the old
blocks produces \(10\). This conclusion uses the stipulated absence of an
independent global minus sign. Indeed, that restriction is substantive:
\(3^{20}\equiv199\equiv-10\pmod{209}\), so a free minus sign would defeat
this particular exclusion.

The appended endpoint residues themselves do not enlarge the subgroup,
because

\[
81=3^4,\qquad80=81^{-1}=3^{-4}\pmod{209}.
\]

The refined block subgroup contains the old generators and also contains
\(10=2\cdot5\notin H_0\). It is therefore a strict enlargement caused only
by exposing separate integer factors through gcd refinement, exactly as
claimed.

The finite examples disprove universal distance monotonicity and square
closure, while this last example proves that canonical-endpoint feedback can
still change the block-generated subgroup. Nothing in these arguments gives
an all-input hitting law or says that a transcript-derived polynomial menu
must contain a useful low-distance state. The stated scope is therefore
correct.
