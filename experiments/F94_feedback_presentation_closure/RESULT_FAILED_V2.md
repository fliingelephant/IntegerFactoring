# F94 — feedback saturation has two exact gates, and private fresh rows do not amortize

**Status:** corrected proof-only candidate after the first hostile audit
failed. No fresh hostile audit, proof-blind reconstruction, research
computation, cross-family audit, human audit, or literature audit has run on
this version. The failed version and its audit are preserved. This is an
exact accounting theorem for multiplicative feedback and prime saturation.
It is not a feedback source law or a factoring algorithm.

## 1. Material difference

P73 gives the binary private-row accounting for feedback square classes.
P91 proves that one appended relation adds an \(\ell\)-th-root coset exactly
when its exponent column closes in the old column span modulo \(\ell\).
P99 proves that bare \(N\) already supplies generators of the complete unit
group with constant probability, or directly finds a factor.

Together, these facts change the feedback question. On the P99 source event,
feedback cannot enlarge the abstract unit subgroup. It can still refine the
integer block presentation and append known relations. The present result
tracks those two changes separately. A general refinement can create a root
dependency through exponent multiplicities. After that update, a new
relation creates a root dependency exactly when its column closes. A
relation containing one private fresh block to exponent one cannot close for
any prime on that step.

Thus there are two exact saturation gates: multiplicity refinement and
column closure. Accumulating many canonical-inverse relations is useful only
when one of these gates opens. Relation count and abstract subgroup size are
not valid progress measures.

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
exponent factorization

\[
q_j=\prod_{r=1}^t b_r^{\alpha_{rj}},
\qquad
\alpha_{rj}\in\mathbb Z_{\ge0}.
\tag{1}
\]

Because the old \(q_j\) are pairwise coprime, the nonempty supports

\[
D_j=\{r:\alpha_{rj}>0\}
\]

are pairwise disjoint. Let \(F\) be the set of indices of blocks that divide
no old \(q_j\). These are the fresh rows.

Define

\[
\Delta_\alpha:\mathbb Z^s\longrightarrow\mathbb Z^t
\]

by

\[
(\Delta_\alpha x)_r
=\sum_{j=1}^s\alpha_{rj}x_j.
\tag{2}
\]

The old relation matrix in the refined coordinates is

\[
E'=\Delta_\alpha E.
\tag{3}
\]

## 3. Exact multiplicity-refinement gate

### Theorem 1

Fix a prime \(\ell\) and reduce all matrices modulo \(\ell\). Then

\[
\boxed{
\ker E'
=\{c\in\mathbb F_\ell^m:Ec\in\ker\Delta_\alpha\}.
}
\tag{4}

Moreover,

\[
\boxed{
\dim\ker E'-\dim\ker E
=\dim(\operatorname{im}E\cap\ker\Delta_\alpha).
}
\tag{5}

Thus refinement creates a new \(\ell\)-saturation dependency exactly when

\[
\operatorname{im}E\cap\ker\Delta_\alpha\ne\{0\}.
\tag{6}

Because the supports \(D_j\) are disjoint,

\[
\ker\Delta_\alpha
=\operatorname{span}\{e_j:\ell\mid\alpha_{rj}
\text{ for every }r\in D_j\}.
\tag{7}

In particular, refinement preserves the old kernel whenever every old block
has at least one descendant exponent not divisible by \(\ell\). A
multiplicity-free refinement has this property for every prime.

### Proof

For \(c\in\mathbb F_\ell^m\),

\[
E'c=0
\iff
\Delta_\alpha(Ec)=0
\iff
Ec\in\ker\Delta_\alpha,
\]

which proves (4). The linear map \(E\) sends \(\ker E'\) onto
\(\operatorname{im}E\cap\ker\Delta_\alpha\), and its kernel on this domain
is \(\ker E\). Rank-nullity gives (5) and (6).

For each \(j\), the vector \(\Delta_\alpha e_j\) is supported on \(D_j\).
The supports are nonempty and disjoint. Hence the nonzero vectors among
these columns are linearly independent modulo \(\ell\). The \(j\)-th column
vanishes exactly when all \(\alpha_{rj}\) are divisible by \(\ell\), which
proves (7). \(\square\)

The multiplicity branch is executable. The algorithm knows every
\(\alpha_{rj}\), so it can recompute the exact kernel after refinement and
run the relevant prime-root decoder on every new direction. For example,

\[
N=3,
\qquad
q_1=4\equiv1\pmod3,
\qquad
E=[1]
\]

can refine through the endpoint \(2\) to \(4=2^2\). The refined matrix is
\([2]\), whose kernel modulo two has grown from zero to dimension one. This
is a real refinement-root event, not column closure.

Even when the kernel does not change, the refined blocks can be valuable.
They add named integer factors that can be powered, mixed with old blocks,
or reused in later feedback.

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
\tag{8}
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
   \tag{9}
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
   \tag{10}
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

Under P91's distinct-odd-semiprime hypotheses, and after its complete old
decoder has failed on the root image generated by the explicit known
kernel, P91 supplies the matching decoder consequence. In the closing case,
the new kernel direction creates one canonical \(\ell\)-th-root coset. At
most \(\ell\) public gcd tests are complete for this coset when \(\ell\) is
numerically polynomial in \(\log N\).

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
\tag{11}
\]

the appended relation is nonclosing and adds no new \(\ell\)-saturation
dependency.

In particular, if one fresh block occurs in the relation to exponent one,
then the relation adds no new saturation dependency for **any** prime
\(\ell\).

### Proof

By (2), every fresh row of \(E'=\Delta_\alpha E\) is zero. Its entire column
span is therefore zero on that row. Condition (11) excludes \(u\) from the span,
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

Fix one final refined coordinate system and one prime \(\ell\). Let
\(M_0\) be the lifted old relation matrix, and let
\(u_1,\ldots,u_M\) be appended relation columns in these coordinates.
Suppose that for each \(i\) there is a distinct row \(r_i\) such that

\[
(M_0)_{r_i,*}=0,
\qquad
(u_i)_{r_i}\not\equiv0\pmod\ell,
\qquad
(u_j)_{r_i}\equiv0\pmod\ell\quad(j<i).
\tag{12}
\]

Then the appended columns are independent modulo
\(\operatorname{colspan}(M_0)\), and

\[
\boxed{
\ker[M_0\mid u_1\mid\cdots\mid u_M]
=\ker(M_0)\times\{0\}^M.
}
\tag{13}

If every feedback relation has its own private fresh block to exponent one
in the final refined presentation, (12) holds simultaneously for every
prime \(\ell\). No number of these columns adds a new prime-saturation
kernel direction.

### Proof

Suppose

\[
M_0x+\sum_{i=1}^M a_i u_i=0.
\]

If some \(a_i\) is nonzero, choose the largest such index. On row \(r_i\),
the old matrix and all earlier appended columns vanish, while all later
coefficients are zero. The remaining term
\(a_i(u_i)_{r_i}\) is nonzero, a contradiction. Hence every \(a_i=0\), and
then \(x\in\ker M_0\). \(\square\)

The corollary gives an exact answer to “amortize many lucky relations.” Many
columns help only after their block incidences overlap enough to create a
modular column dependency, or later refinement opens the multiplicity gate
of Theorem 1. Stable private cofactors form a triangular matrix, not a
saturation source.

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
\tag{14}

Every later no-factor gcd-free refinement still represents all retained
\(a_i\), so (14) remains true. Abstract subgroup expansion is impossible on
this source event. Feedback changes the public presentation instead:

- it exposes new atomic integer blocks;
- it can change old saturation kernels through exponent multiplicities;
- it adds known relation columns;
- it can create a closing saturation dependency; or
- it can make a short direct or mixed word available.

The true relation of a new block to the original full-group generators
exists, but it is not supplied by abstract generation. The public matrix
\(E\) contains only relations that the algorithm actually knows.

## 8. Algorithmic consequence and exact gap

For feedback saturation, the exact polynomial-time bookkeeping is clear.
After each gcd-free refinement, apply the full exponent map
\(E'=\Delta_\alpha E\) and recompute the kernel modulo every scanned small
prime. Process every direction created by the multiplicity gate. Then append
the new relation column and test its old-span closure. Under P91's
distinct-odd-semiprime hypotheses and after its complete old decoder fails,
P91 gives the short complete root-coset scan for a closing column.

This invalidates two proposed progress measures:

1. On a retained P99 source event, abstract subgroup growth is already
   saturated at \(G_N\).
2. A large count of feedback relations gives no saturation gain when each
   relation retains a private fresh row in the final presentation and no
   multiplicity gate opens.

It also limits an ephemeral-probe rule. If a split is retained but its
relation column and fresh cofactors are discarded, the state can lose the
first half of a future closing dependency. Such deletion can still be a
chosen bounded-memory heuristic, but subgroup growth does not prove it
lossless.

The loss is literal even in one row over \(\mathbb F_2\). The first column
\([1]\) is nonclosing against an empty matrix. A later reused column
\([1]\) closes and gives kernel vector \((1,1)\). If the first column is
discarded, the later column is again nonclosing.

The remaining positive target is precise. One needs an inverse-polynomial
all-input law that does at least one of the following:

- exposes a named block with a successful direct, power, or mixed-word
  decoder;
- opens the multiplicity-refinement gate and produces a non-global root;
- reuses earlier blocks so that a new relation closes modulo a public small
  prime and its root coset leaves the old synchronized image; or
- supplies a different non-power factor localizer on the full-group
  presentation.

The theorem proves no such law. It gives no factoring algorithm and no
computational lower bound.
