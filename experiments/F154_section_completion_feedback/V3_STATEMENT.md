# F154 V3 candidate — section completion is decoder-inert but can change a refinement-mediated feedback grammar

## Status and scope

This is a proof-only candidate. It assumes the no-factor branch of the F152
V2 decorated-squareclass theorem. It gives a public quasipolynomial closure
when the observed parity dimension is polylogarithmic. It does not prove that
the closure must refine a block, force a later section disagreement, or give
an all-input factoring law.

The feedback statement uses one explicit interface restriction. A later
grammar can observe completion data only through blocks newly named by joint
gcd-free refinement. The theorem makes no inertness claim for an arbitrary
future grammar that can inspect the raw completion values, their count, or
their provenance.

## Closest prior results and the material difference

P66 gives the complete squareclass decoder. P128 retains unreduced word
presentations. P129 identifies the bridge-cycle rank and root gate. F152 V2
proves that a failed decoder is exactly a homomorphic decorated section over
the observed parity span.

F154 asks what happens if the algorithm explicitly completes that section.
It manufactures one exact integer relation for every parity vector in the
span and proves two opposing facts:

1. the completed family is algebraically harmless to the current decoder;
2. its new canonical inverse representatives can expose new integer blocks
   and can therefore change a refinement-mediated feedback grammar.

Thus feedback can create new named integer state without creating new
modular information. Any success must occur after refinement or a later
source step, not inside the completion itself.

## 1. Setup

Let \(N\ge3\) be odd. Let \(q_1,\ldots,q_m\) be pairwise-coprime nonsquare
positive units modulo \(N\), where nonsquare means not an integer square.
For \(v\in\mathbf F_2^m\), put

\[
Q(v)=\prod_{j=1}^m q_j^{v_j},
\qquad
C(v,w)=\prod_{j=1}^m q_j^{v_jw_j}.
\tag{1}
\]

Use the decorated group

\[
E_Q(N)=
\{(v,z):z^2\equiv Q(v)\pmod N\},
\tag{2}
\]

with

\[
(v,z)\star(w,t)
=
(v+w,ztC(v,w)^{-1}).
\tag{3}
\]

Assume an explicit retained relation transcript has no useful normalized
root. By F152 V2, its decorated lifts define a quotient section

\[
h:W\longrightarrow E_Q(N)/\{(0,1),(0,-1)\}
\tag{4}
\]

on the observed parity span \(W\).

Choose an explicit parity basis of \(W\) from the retained transcript and
keep the actual decorated lift of each basis vector. Their star-products
give a public homomorphic lift

\[
\widetilde h:W\longrightarrow E_Q(N),
\qquad
\widetilde h(v)=(v,z_v),
\tag{5}
\]

whose quotient is \(h\). Take each \(z_v\) in \(\{1,\ldots,N-1\}\).

## 2. Public section completion

Let

\[
s_v=\iota_N(z_v)
\tag{6}
\]

be the least positive inverse of \(z_v\) modulo \(N\), and define the exact
positive integer

\[
\boxed{
P_v=s_v^2Q(v).
}
\tag{7}
\]

Then

\[
P_v\equiv1\pmod N.
\tag{8}
\]

Give \(P_v\) the supplied modular root \(1\) and the explicit factor
presentation \(s_v^2Q(v)\). Its decorated lift is exactly

\[
(v,s_v^{-1})=(v,z_v)=\widetilde h(v).
\tag{9}
\]

The values \(P_v\) are pairwise distinct. Also \(P_0=1\), and every
\(v\ne0\) gives \(P_v>1\).

## 3. Exact inertness theorem

For every subset \(S\subseteq W\),

\[
\prod_{v\in S}P_v
\quad\hbox{is an integer square}
\quad\Longleftrightarrow\quad
\sum_{v\in S}v=0.
\tag{10}
\]

For every such dependency, the normalized modular root supplied by the
positive integer square is exactly

\[
\boxed{+1\pmod N.}
\tag{11}
\]

Therefore adding all section-completion records to the old transcript
cannot enlarge its useful normalized-root image. Mixed old/completion
dependencies also have only global roots. Root-aware exact-value deletion
preserves the current normalized-root image after the supplied roots are
compared. Occurrence, presentation, and provenance metadata must be retained
if a later grammar is allowed to observe them.

Every pair \(v,w\in W\) gives the explicit triple square

\[
P_vP_wP_{v+w}
=
\left(
s_vs_ws_{v+w}Q(v+w)C(v,w)
\right)^2,
\tag{12}
\]

and the displayed positive root is \(1\) modulo \(N\). Thus the completion
can contain many exact square relations while every one remains a global
decoy.

## 4. Quasipolynomial cost

Let \(d=\dim W\), and let

\[
\Lambda_Q=\sum_{j=1}^m\lceil\log_2(q_j+1)\rceil.
\tag{13}
\]

The completion has exactly \(2^d\) indexed records. Every \(P_v\) has at most
\(2n+\Lambda_Q+O(1)\) bits, where
\(n=\lceil\log_2(N+1)\rceil\). It can be generated with

\[
\operatorname{poly}(2^d,n+\Lambda_Q)
\tag{14}
\]

bit operations.

Hence the complete construction and a compact full factor-free decode remain
quasipolynomial whenever \(d=(\log n)^{O(1)}\) and the explicit block
transcript, including the \(q_j\) list, has quasipolynomial total bit length.
Here a compact decode computes a kernel basis and its root image. It does not
enumerate every dependency.

## 5. The refinement-mediated feedback channel

Equation (11) proves that section completion cannot factor \(N\) through the
current squareclass decoder. Nevertheless, the integers \(s_v\) are newly
computed least-positive canonical inverse representatives. They need not be
distinct or absent from the old state. Joint gcd-free refinement of the old
endpoints with all \(s_v\) can expose proper integer blocks that were not
named before completion.

Use the following interface restriction for the feedback statement:

> After completion, the later source grammar can observe the completion only
> through blocks newly named by that joint gcd-free refinement.

Under this restriction, newly named blocks can change the available integer
generators even though every completion lift lies on the old section. This is
the exact sense in which feedback can add algorithmic state without adding
modular information.

If refinement names no new block, or if the grammar excludes all such blocks
as generators, this refinement-mediated feedback channel is inert. This does
not imply that completion is inert for an arbitrary grammar that can inspect
the raw \(s_v\), the \(P_v\), their count, or their provenance.

## 6. Exact finite witness for named-state expansion and later capability

Take

\[
N=77,
\qquad
q_1=4706,
\qquad
T_1=q_1,
\qquad
\alpha_1=3.
\tag{15}
\]

Here \(q_1=61\cdot77+9\), so \(\alpha_1^2\equiv q_1\pmod{77}\).
The positive integer \(q_1\) is not an integer square and is a unit modulo
\(77\). The one-record transcript has no parity dependency. Its section lift
is \(z_{(1)}=3\), and

\[
s_{(1)}=26,
\qquad
3\cdot26=1+77.
\tag{16}
\]

The completion record is

\[
P_{(1)}=26^2\cdot4706\equiv1\pmod{77}.
\tag{17}
\]

Joint refinement is nontrivial:

\[
4706=26\cdot181,
\qquad
\gcd(26,4706)=26.
\tag{18}
\]

Thus the old named block \(4706\) splits into the coprime named blocks
\(26\) and \(181\). The residue \(4706\equiv9\pmod{77}\) has order \(15\),
whereas \(26\) has order \(30\). A named-block grammar that accepts the new
blocks therefore has a strictly larger generated modular subgroup.

The current completion decoder and the displayed endpoint gcd screens do
not factor \(77\): completion dependencies have normalized root \(+1\), and

\[
\gcd(26,77)=\gcd(181,77)=1.
\tag{19}
\]

After refinement admits \(26\) through the restricted named-block
interface, however, a later grammar can perform the finite power test

\[
26^{15}\equiv34\pmod{77},
\qquad
\gcd(34-1,77)=11,
\qquad
\gcd(34+1,77)=7.
\tag{20}
\]

Thus this is a finite refinement-mediated witness that a later grammar can
factor the displayed input. It is not new modular information:
\(26=\iota_{77}(3)\) was already publicly computable from the supplied root
\(3\). The witness gives no all-input law that selects a useful exponent,
computes a suitable order, forces refinement, or guarantees a factor.

## 7. Precise remaining theorem

The next positive statement must control the second stage:

> For every terminal quasipolynomial section completion, either joint
> integer refinement releases a usable new generator whose later canonical
> lift disagrees with the old section, or persistent agreement forces a
> separate public restriction that cannot hold for all composite inputs.

F154 proves neither alternative. It gives a bounded one-round construction,
not an iteration bound. It does not show that a new block must appear, that a
later relation must close, or that a resulting root must be non-global on
general inputs.
