# F94 — feedback lifts the public presentation, but a private fresh block prevents saturation closure

**Status:** proof-only candidate. No research computation, hostile audit,
proof-blind reconstruction, cross-family audit, human audit, or literature
audit has run. This is an exact accounting theorem for multiplicative
feedback and prime saturation. It is not a feedback source law or a
factoring algorithm.

## 1. Material difference

P91 proves that one appended relation adds an \(\ell\)-th-root coset exactly
when its exponent column closes in the old column span modulo \(\ell\).
P99 proves that bare \(N\) already supplies generators of the complete unit
group with constant probability, or directly finds a factor.

Together, these facts change the feedback question. On the P99 source event,
feedback cannot enlarge the abstract unit subgroup. It can still refine the
integer block presentation and append known relations. The present result
tracks those two changes separately. It proves that block refinement alone
does not enlarge any prime-saturation kernel, and that a relation containing
one private fresh block to exponent one cannot close for any prime.

Thus accumulating many canonical-inverse relations is useful for saturation
only when later relations reuse earlier blocks or otherwise remove every
private row. Relation count and abstract subgroup size are not valid progress
measures.

## 2. Public block presentation

Let \(N\ge2\). Let

\[
Q=(q_1,\ldots,q_s)
\]

be pairwise-coprime positive integers that are units modulo \(N\). Suppose
the algorithm knows \(m\) multiplicative relations

\[
A_i=\prod_{j=1}^s q_j^{e_{ji}}\equiv1\pmod N,
\qquad
1\le i\le m,
\]

with exponent matrix

\[
E=(e_{ji})\in\mathbb Z_{\ge0}^{s\times m}.
\]

This is only the **known relation list**. It need not be the complete
relation lattice of the residues.

Now jointly gcd-free refine the old blocks with new integer endpoints. Let

\[
B=(b_1,\ldots,b_t)
\]

be the final pairwise-coprime block list. Every old block has an exact
factorization

\[
q_j=\prod_{r\in D_j}b_r,
\tag{1}
\]

where the nonempty sets \(D_j\) are pairwise disjoint. Let \(F\) be the set
of indices of blocks that divide no old \(q_j\). These are the fresh rows.

Define

\[
\Delta:\mathbb Z^s\longrightarrow\mathbb Z^t
\]

by

\[
(\Delta x)_r=
\begin{cases}
x_j,&r\in D_j,\\
0,&r\in F.
\end{cases}
\tag{2}
\]

The old relation matrix in the refined coordinates is

\[
E'=\Delta E.
\tag{3}
\]

## 3. Refinement preserves every old saturation kernel

### Theorem 1

For every prime \(\ell\), reduction of \(\Delta\) modulo \(\ell\) is
injective. Consequently,

\[
\boxed{
\ker(E'\bmod\ell)=\ker(E\bmod\ell).
}
\tag{4}

In particular, gcd-free block refinement by itself creates no new
\(\ell\)-saturation dependency.

### Proof

Each \(D_j\) is nonempty, and the sets are disjoint. If \(\Delta x=0\),
choose any \(r\in D_j\). Equation (2) gives \(x_j=0\). This holds for every
\(j\), over \(\mathbb Z\) and over every \(\mathbb F_\ell\). Thus
\(\Delta\) is injective.

For \(c\in\mathbb F_\ell^m\),

\[
E'c=0
\iff
\Delta(Ec)=0
\iff
Ec=0.
\]

This proves (4). \(\square\)

The refined blocks can still be algorithmically valuable. They add named
integer factors that can be powered, mixed with old blocks, or reused in
later feedback. The theorem says only that row refinement alone adds no root
dependency to the current known relation list.

## 4. Exact rank accounting for one appended relation

Append one known relation in the refined blocks,

\[
A_*=\prod_{r=1}^t b_r^{u_r}\equiv1\pmod N,
\qquad
u\in\mathbb Z_{\ge0}^t.
\]

For a prime \(\ell\), write

\[
V_\ell=\ker(E'\bmod\ell)
\]

and define the public saturation deficiency

\[
\kappa_\ell(E')
=m-\operatorname{rank}_{\mathbb F_\ell}(E')
=\dim_{\mathbb F_\ell}V_\ell.
\tag{5}
\]

### Theorem 2

Exactly one of the following occurs.

1. If

   \[
   u\notin\operatorname{colspan}_{\mathbb F_\ell}(E'),
   \]

   then

   \[
   \ker[E'\mid u]=(V_\ell\times\{0\}),
   \qquad
   \kappa_\ell([E'\mid u])=\kappa_\ell(E').
   \tag{6}
   \]

2. If

   \[
   u\in\operatorname{colspan}_{\mathbb F_\ell}(E'),
   \]

   choose \(c\in\mathbb F_\ell^m\) with \(E'c+u=0\). Then

   \[
   \ker[E'\mid u]
   =(V_\ell\times\{0\})\oplus\langle(c,1)\rangle,
   \qquad
   \kappa_\ell([E'\mid u])=\kappa_\ell(E')+1.
   \tag{7}
   \]

Thus a new relation makes prime-saturation progress exactly when it does
not increase column rank modulo \(\ell\).

### Proof

A vector \((x,a)\) lies in the new kernel exactly when

\[
E'x+au=0.
\]

If \(a\ne0\), this equation puts \(u\) in the old column span. Hence a
nonclosing column forces \(a=0\), which gives (6). Its addition increases
both the number of columns and the rank by one, so \(\kappa_\ell\) does not
change.

In the closing case, subtract \(a(c,1)\). The last coordinate becomes zero,
and the remaining vector lies in \(V_\ell\times\{0\}\). The sum is direct
because \((c,1)\) has last coordinate one. The new column does not increase
rank, so (7) follows. \(\square\)

P91 supplies the matching decoder consequence. In the closing case, the new
kernel direction creates one canonical \(\ell\)-th-root coset. After the
complete old decoder fails, at most \(\ell\) public gcd tests are complete
for this coset when \(\ell\) is numerically polynomial in \(\log N\).

## 5. Private-fresh-row obstruction

### Theorem 3

Every vector in

\[
\operatorname{colspan}_{\mathbb F_\ell}(E')
\]

is zero on every fresh row \(r\in F\). Therefore, if

\[
u_r\not\equiv0\pmod\ell
\qquad
\text{for some }r\in F,
\tag{8}
\]

the appended relation is nonclosing and adds no new \(\ell\)-saturation
dependency.

In particular, if one fresh block occurs in the relation to exponent one,
then the relation adds no new saturation dependency for **any** prime
\(\ell\).

### Proof

By (2), every fresh row of \(E'=\Delta E\) is zero. Its entire column span
is therefore zero on that row. Condition (8) excludes \(u\) from the span,
so Theorem 2 applies. The integer one is nonzero modulo every prime. \(\square\)

For canonical-inverse feedback, the selected endpoint is a known product of
current blocks and its least positive inverse \(w\) gives

\[
gw=1+kN.
\]

If gcd-free refinement leaves a new cofactor of \(w\) that occurs to
exponent one and has not appeared before, the new relation cannot close any
prime-saturation kernel on that step. The block can still be useful through
direct gcds, powers, mixed words, or later reuse.

## 6. Many relations do not amortize without reuse

### Corollary 4 — private-row independence

Let \(u_1,\ldots,u_M\) be appended relation columns. Fix a prime \(\ell\).
Suppose that for each \(i\) there is a row \(r_i\) such that

\[
(u_i)_{r_i}\ne0,
\qquad
(u_j)_{r_i}=0\quad(j<i),
\tag{9}
\]

and the rows \(r_i\) are distinct. Then the columns are linearly independent
over \(\mathbb F_\ell\). They create no relation dependency modulo \(\ell\).

If every feedback relation brings its own private fresh block to exponent
one, (9) holds simultaneously for every prime \(\ell\). No number of such
relations creates any prime-saturation root.

### Proof

In a linear combination, inspect the private row of the last column with a
nonzero coefficient. Earlier columns vanish there, while that last column
does not. The combination cannot be zero. \(\square\)

The corollary gives an exact answer to “amortize many lucky relations.” Many
columns help only after their block incidences overlap enough to create a
modular column dependency. Independent fresh cofactors form a triangular
matrix, not a saturation source.

## 7. Consequence of retaining a P99 generator batch

Suppose the retained raw units \(a_1,\ldots,a_d\) generate

\[
G_N=(\mathbb Z/N\mathbb Z)^\times.
\]

If every \(a_i\) is represented as an integer product of the current unit
blocks \(B\), then

\[
G_N=\langle a_1,\ldots,a_d\rangle
\le\langle B\rangle
\le G_N.
\]

Hence

\[
\boxed{\langle B\rangle=G_N.}
\tag{10}

Every later no-factor gcd-free refinement still represents all retained
\(a_i\), so (10) remains true. Abstract subgroup expansion is impossible on
this source event. Feedback changes the public presentation instead:

- it exposes new atomic integer blocks;
- it adds known relation columns;
- it can create a closing saturation dependency; or
- it can make a short direct or mixed word available.

The true relation of a new block to the original full-group generators
exists, but it is not supplied by abstract generation. The public matrix
\(E\) contains only relations that the algorithm actually knows.

## 8. Algorithmic consequence and exact gap

For feedback saturation, the exact polynomial-time bookkeeping is clear.
After each gcd-free refinement, duplicate the old exponent rows, append the
new relation column, and update its rank modulo every scanned small prime.
Only a closing column can enlarge a prime-saturation kernel. P91 then gives
the complete short root-coset scan.

This invalidates two proposed progress measures:

1. On a retained P99 source event, abstract subgroup growth is already
   saturated at \(G_N\).
2. A large count of feedback relations gives no saturation gain when each
   relation has a private fresh block.

It also limits an ephemeral-probe rule. If a split is retained but its
relation column and fresh cofactors are discarded, the state can lose the
first half of a future closing dependency. Such deletion can still be a
chosen bounded-memory heuristic, but subgroup growth does not prove it
lossless.

The remaining positive target is precise. One needs an inverse-polynomial
all-input law that does at least one of the following:

- exposes a named block with a successful direct, power, or mixed-word
  decoder;
- reuses earlier blocks so that a new relation closes modulo a public small
  prime and its root coset leaves the old synchronized image; or
- supplies a different non-power factor localizer on the full-group
  presentation.

The theorem proves no such law. It gives no factoring algorithm and no
computational lower bound.
