# F154 candidate — section completion is decoder-inert but can change feedback grammar

## Status and scope

This is a proof-only candidate. It assumes the no-factor branch of the F152
V2 decorated-squareclass theorem. It gives a public quasipolynomial closure
when the observed parity dimension is polylogarithmic. It does not prove that
the closure refines a block, forces a later section disagreement, or factors
an input.

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
   and can therefore change a later feedback grammar.

Thus feedback can create new integer state without creating new modular
information. Any success must occur after refinement or a later source step,
not inside the completion itself.

## 1. Setup

Let \(N\ge3\) be odd. Let \(q_1,\ldots,q_m\) be pairwise-coprime nonsquare
positive units modulo \(N\). For \(v\in\mathbf F_2^m\), put

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
remains safe after the supplied roots are compared.

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

Hence the complete construction and the full factor-free decode remain
quasipolynomial whenever \(d=(\log n)^{O(1)}\) and the explicit block
transcript has quasipolynomial total bit length.

## 5. The feedback-only gain

Equation (11) proves that section completion cannot factor \(N\) through the
current squareclass decoder. Nevertheless, the integers \(s_v\) are new
least-positive canonical inverse representatives. Joint gcd-free refinement
of the old endpoints with all \(s_v\) can expose proper integer blocks that
were not named before completion.

If a later source grammar is allowed to use such newly named blocks, the
available integer generators can change even though every new modular lift
lies on the old section. This is the exact sense in which feedback can add
algorithmic state without adding modular information.

This observation is conditional on a refinement-aware future grammar. If
the new inverse representatives do not refine the named state, or if the
grammar never admits decoder blocks as generators, the completion is fully
inert.

## 6. Precise remaining theorem

The next positive statement must control the second stage:

> For every terminal quasipolynomial section completion, either joint
> integer refinement releases a usable new generator whose later canonical
> lift disagrees with the old section, or persistent agreement forces a
> separate public restriction that cannot hold for all composite inputs.

F154 proves neither alternative. It gives a bounded one-round construction,
not an iteration bound. It does not show that a new block appears, that a
later relation closes, or that a resulting root is non-global.
