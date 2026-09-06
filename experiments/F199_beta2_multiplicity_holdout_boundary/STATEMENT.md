# F199: direct multiplicity holdout does not select the beta-two reciprocal

Status: frozen proof-only candidate.

## Scope and imported beta-two interface

Let

\[
N=pq,
\qquad p<q<2p,
\tag{1}
\]

where \(p,q\) are distinct odd primes. Define

\[
n=\left\lceil\log_2(N+1)\right\rceil,
\qquad B=\lfloor\sqrt N\rfloor,
\qquad A=(-1)^B\binom{N-1}{B}.
\tag{2}
\]

P171--P175 give the following imported facts. The integer

\[
h=\frac{A-(1-q)}N
\tag{3}
\]

is well-defined. For every \(t\le n\), the public residue

\[
z=N^{-1}(A-1)\pmod {2^t}
\tag{4}
\]

is deterministic polynomial-time computable, and

\[
h-z\equiv p^{-1}\pmod {2^t}.
\tag{5}
\]

For the terminal claims below, set

\[
k=\left\lfloor\frac{\log_2N}{4}\right\rfloor,
\qquad t=k-L(n)\ge2,
\qquad L(n)=(\log n)^{O(1)},
\tag{6}
\]

where \(L\) is one fixed public integer-valued function. P175 proves that
either \(p\bmod2^t\) or \(p^{-1}\bmod2^t\) is a deterministic numerical-QP
factoring statistic on this promise.

F199 concerns only direct multiplicity and feature-space encodings of this
statistic. It is not a factoring algorithm and not a lower bound against
nonlocal integer features or adaptive prefix-cell syndromes.

## Theorem 1: the public low-precision equations form a smooth torsor

Put

\[
R=\mathbb Z/2^t\mathbb Z.
\tag{7}
\]

For every unit \(u\in R^\times\), define

\[
P_u=u^{-1},
\qquad Q_u=Nu,
\qquad H_u=z+u
\quad\text{in }R.
\tag{8}
\]

Then

\[
P_uu=1,
\qquad Q_u=Nu,
\qquad P_uQ_u=N,
\qquad NH_u=A-1+Q_u.
\tag{9}
\]

Conversely, every solution of

\[
PU=1,
\qquad Q=NU,
\qquad H=z+U
\tag{10}
\]

has \(U\in R^\times\) and is uniquely of the form (8). Algebraically,

\[
R[U,P,Q,H]/(PU-1,Q-NU,H-z-U)
\cong R[U,U^{-1}].
\tag{11}
\]

The Jacobian minor in the variables \((P,Q,H)\) has determinant \(U\), a
unit at every point. Thus all \(2^{t-1}\) candidate reciprocal residues are
simple points of one smooth relative one-dimensional scheme. The target

\[
u_*=p^{-1}\pmod {2^t}
\tag{12}
\]

is one of these points, but it is not a singular or higher-multiplicity
point of the public congruence system.

This theorem covers the direct ring-equation and local-jet encoding only.
It does not say that an arbitrary polynomial with coefficients computed
from \(N\) cannot orient the torsor. Constructing such a target-correlated
orientation remains the problem.

## Theorem 2: the public coefficient transcript has no transition jet

For \(0\le i\le B\), put

\[
A_i=(-1)^i\binom{N-1}{i},
\qquad
z_i=N^{-1}(A_i-1)\pmod {2^t}.
\tag{13}
\]

Every \(z_i\) is computable in polynomial time when its public index \(i\)
is supplied. For every \(0\le i<B\), the exact recurrence for \(A_i\)
gives

\[
(i+1)(z_{i+1}-z_i)+1+Nz_i=0
\quad\text{in }R.
\tag{14}
\]

Define

\[
\mathcal R_N(K,X,Y)
=(K+1)(Y-X)+1+NX.
\tag{15}
\]

At every transcript point \((i,z_i,z_{i+1})\), its first Hasse derivatives
in \(X,Y\) are

\[
\mathcal R_N^{(0,1,0)}=N-(K+1),
\qquad
\mathcal R_N^{(0,0,1)}=K+1.
\tag{16}
\]

Their sum is the odd unit \(N\). Hence the recurrence hypersurface is
smooth modulo \(2\) at every transcript edge. In particular, the hidden
edge \(i=p-1\) is not a multiplicity outlier of the public \(z_i\) word.

For comparison, define the unavailable integral quotients

\[
H_i=
\begin{cases}
(A_i-1)/N,&0\le i<p,\\[1mm]
(A_i-1+q)/N,&p\le i\le B.
\end{cases}
\tag{17}
\]

Then

\[
H_i-z_i\equiv p^{-1}\mathbf 1_{i\ge p}\pmod {2^t},
\tag{18}
\]

and therefore

\[
(H_{i+1}-H_i)-(z_{i+1}-z_i)
\equiv p^{-1}\mathbf 1_{i=p-1}pmod {2^t}.
\tag{19}
\]

Thus the desired one-error word exists only after inserting the missing
quotient transcript \(H_i\). Equation (14) shows that it is absent from the
public \(z_i\) transcript.

## Theorem 3: direct Boolean holdout has an exact degree boundary

Identify the odd residues modulo \(2^t\) with the Boolean cube

\[
\Omega=\mathbb F_2^m,
\qquad m=t-1,
\tag{20}
\]

using the free bits above the fixed low bit one. Let \(F\) be a nonzero
multilinear polynomial on \(\Omega\) of total degree at most \(d\). Then

\[
\boxed{\left|\operatorname{supp}F\right|\ge2^{m-d}.}
\tag{21}
\]

Consequently, if \(S\subseteq\Omega\) and \(F\) vanishes on
\(\Omega\setminus S\), then

\[
|S|\ge2^{m-d}.
\tag{22}
\]

In particular:

1. a polynomial supported at one candidate has degree exactly \(m\);
2. if \(|S|<2^{m-d}\), restricting evaluation from \(\Omega\) to
   \(\Omega\setminus S\) remains injective on the degree-at-most-\(d\)
   polynomial space;
3. equivalently, deleting fewer than \(2^{m-d}\) columns from the standard
   degree-at-most-\(d\) Reed--Muller feature matrix does not reduce its
   column span.

When \(d=(\log n)^{O(1)}\) and \(|S|=2^{(\log n)^{O(1)}}\), one has
\(|S|<2^{m-d}\) for all sufficiently large inputs because \(m=\Theta(n)\).
Thus the direct low-degree singleton or QP-holdout decoder has zero
vanishing space on the complement.

This theorem applies to the candidate bits themselves and to affine changes
of those bits. It does not cover an arbitrary nonlinear feature embedding
whose coordinates already contain target-correlated integer information.

## Theorem 4: higher-order holdout is incompatible with a missing neighbor

For a multilinear polynomial \(F\) and \(x\in\mathbb F_2^m\), write
\(D_SF(x)\) for the Hasse derivative indexed by \(S\subseteq[m]\). For
every \(T\subseteq[m]\),

\[
F(x+\mathbf 1_T)=\sum_{S\subseteq T}D_SF(x).
\tag{23}
\]

Therefore

\[
D_SF(x)=0\quad(|S|<s)
\tag{24}
\]

is equivalent to the vanishing of \(F\) throughout the Hamming ball of
radius \(s-1\) about \(x\).

Let \(u\in\Omega\). If (24) holds at every point of
\(\Omega\setminus\{u\}\) for some \(s\ge2\), then

\[
F(u)=0.
\tag{25}
\]

Indeed, a Hamming neighbor of \(u\) belongs to the constrained set, and its
radius-one Taylor identity includes \(u\). Thus no multilinear polynomial,
of any degree, can have nonzero value at one held-out candidate while
vanishing to order at least two at every other candidate.

More generally, \(C\) centers with order-\(s\) conditions directly cover at
most

\[
C\sum_{j=0}^{s-1}\binom mj
\tag{26}
\]

cube points. For numerical-QP \(C\) and
\(s=(\log n)^{O(1)}\), this quantity is numerical QP and cannot leave a
unique uncovered point in \(|\Omega|=2^{\Theta(n)}\).

For the direct univariate scalar encoding there is an analogous boundary.
If \(x_1,\ldots,x_M\) are distinct field points and a polynomial \(f\) has
Hasse multiplicity at least \(s\) at every point except \(x_j\), while
\(f(x_j)\ne0\), then

\[
\deg f\ge s(M-1).
\tag{27}
\]

This scalar statement does not rule out a sparse high-degree circuit whose
parameters already encode \(x_j\).

## Theorem 5: a QP explicit target cloud is already terminal

Assume the precision (6). Suppose a deterministic or Las Vegas numerical-QP
algorithm outputs an explicit list

\[
\mathcal U_N\subseteq(\mathbb Z/2^t\mathbb Z)^\times
\tag{28}
\]

of numerical-QP cardinality and guarantees

\[
p^{-1}\bmod2^t\in\mathcal U_N.
\tag{29}
\]

Then \(N\) factors in numerical-QP time. For each \(u\in\mathcal U_N\),
compute

\[
s=u^{-1}\pmod {2^t}
\tag{30}
\]

and invoke the P175 known-residue-class terminal with
\(p\equiv s\pmod {2^t}\). Verify every returned candidate by exact
division. The iteration containing the true reciprocal succeeds, and a QP
number of QP calls remains QP.

The same conclusion holds if each explicit cloud column has a publicly
enumerable numerical-QP-size preimage list of reciprocal candidates. A
public index cloud guaranteed to contain the exact index \(p\) is even more
direct: \(\gcd(i,N)\) factors when \(i=p\).

This theorem does not apply to an aggregate column representing an
exponentially large prefix cell. Selecting such a cell without listing its
members remains open.

## Theorem 6: every one-bit reciprocal lift remains paired

Let \(1\le j<t\), let \(\bar u\) be an odd residue modulo \(2^j\), and put

\[
u_b=\bar u+b2^j\pmod {2^{j+1}},
\qquad b\in\{0,1\}.
\tag{31}
\]

Define

\[
P_b=u_b^{-1},
\qquad Q_b=Nu_b
\pmod {2^{j+1}}.
\tag{32}
\]

Then

\[
P_1\equiv P_0+2^j,
\qquad
Q_1\equiv Q_0+2^j
\pmod {2^{j+1}}.
\tag{33}
\]

Both triples satisfy

\[
P_bu_b=1,
\qquad Q_b=Nu_b,
\qquad P_bQ_b=N
\pmod {2^{j+1}}.
\tag{34}
\]

Thus the public congruence tree has two valid children above every prefix.
The simultaneous top-bit toggle is an involution exchanging them.

There is also no pruning from the balance inequalities alone. Put

\[
M=2^{j+1}.
\tag{35}
\]

If \(3M<\sqrt N\), then for each \(b\) there are odd integers
\(\widetilde P_b,\widetilde Q_b\) in the prescribed residue classes with

\[
\sqrt N-M<\widetilde P_b<\sqrt N
<\widetilde Q_b<\sqrt N+M
<2\widetilde P_b.
\tag{36}
\]

At every precision \(M\le N^{1/4}\), condition \(3M<\sqrt N\) holds for
all sufficiently large \(N\). Equation (36) asserts only plausible balanced
integer representatives. It does not assert that the representatives are
prime or that their product is \(N\). Those exact integer conditions are the
missing selector.

## Exact surviving route: adaptive prefix cells

The preceding results do not obstruct a one-child prefix chain. If
\(a=(a_1,\ldots,a_\ell)\) is one prefix of the \(m\) free reciprocal bits,
then its cell has the exact indicator

\[
\chi_a(x)
=\prod_{r=1}^{\ell}(1+x_r+a_r),
\tag{37}
\]

which has degree \(\ell\) and support \(2^{m-\ell}\). For
\(\ell=(\log n)^{O(1)}\), the full degree-at-most-\(\ell\) feature space has
numerical-QP dimension.

Therefore a numerical-QP syndrome that selected the correct prefix cell at
each stage would give a valid numerical-QP sequential chain. Fixed-ratio
contraction is not required. F199 proves only that the direct public
congruence jets, the public \(z_i\) recurrence, a singleton holdout, and an
explicit QP target list do not supply that syndrome.

F199 proves no lower bound against:

1. a nonlocal integer feature involving canonical representatives or
   Euclidean quotients;
2. an aggregate cell statistic with a QP evaluator;
3. an adaptive prefix-cell or one-bit lift syndrome;
4. a nonlinear target-correlated feature embedding;
5. a sparse high-degree circuit; or
6. a different factoring algorithm.
