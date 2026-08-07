# F64 hostile audit — fixed-orientation uniformity

**Candidate audited:**
`experiments/F64_fixed_orientation_uniformity/RESULT.md`

**Verified candidate SHA-256:**
`47839484d1548a0660450073a6d055f958c9de27b5d7db980ea143c43c3a01ae`

**Verdict: FAIL as written.**

The two numbered theorems are correct. The fixed-menu union bound is also
correct. The fresh-pivot extension is correct under the original independent
sampling model. Conditioning on earlier failures does not break that result.

The failure is in the stated scope and conclusion. Independence from the
**integer presentation** is not enough to preserve uniformity. A choice can
ignore that presentation, depend on an already observed group element, and
make the output nonuniform. Also, fixed menus may reuse the same input units;
such reuse does not by itself escape the theorem. The candidate's final
paragraph states both boundaries too broadly.

There is one further precision issue. The menu arguments prove upper bounds.
They do not prove that the success probability is of order `T/N`. Repeated or
equivalent menu entries can make the probability independent of `T`.

No research computation was run. The audit below is symbolic. Hashing was
used only to identify the candidate.

## 1. The fixed signed-product theorem — PASS

Let

\[
G=(\mathbb Z/N\mathbb Z)^\times
\]

and let `epsilon_j` be a nonzero coordinate. After conditioning on every
other input, the product has the form

\[
Z=CX_j^{\epsilon_j}.
\]

Both maps `x -> Cx` and `x -> Cx^{-1}` are bijections of `G`. Therefore

\[
\Pr(Z=z\mid (X_i)_{i\ne j})=\frac1{|G|}
\]

for every `z` in `G`. Averaging over the conditioned variables proves exact
uniformity. The proof needs no independence among different menu outputs.

The nonzero-pattern condition is needed for the equality claim. An all-zero
pattern gives `Z=1`. It causes no problem for the later upper bound because
its direct screen never gives a proper factor of an odd semiprime.

## 2. The two direct-screen counts — PASS

Write the CRT image of `Z` as `(a,b)` in

\[
\mathbb F_p^\times\times\mathbb F_q^\times.
\]

The `Z-1` screen is proper in exactly

\[
(q-2)+(p-2)=p+q-4
\]

pairs: exactly one of `a,b` equals `1`. The `Z+1` screen has the same count.
Their intersection consists of the two opposite-sign pairs

\[
(1,-1),\qquad(-1,1).
\]

Hence their union has size

\[
2(p+q-4)-2=2p+2q-10.
\]

Division by `(p-1)(q-1)` proves the first displayed probability.

There are four square roots of one. The two global roots fail to factor, and
the two opposite-sign roots are useful. Thus the useful involution
probability is exactly

\[
\frac{2}{(p-1)(q-1)}.
\]

The candidate correctly distinguishes a direct separator from a non-global
involution. For example, modulo `15`, the unit `7` satisfies

\[
\gcd(7-1,15)=3,
\qquad
7^2\equiv4\not\equiv1\pmod {15}.
\]

Thus the direct-screen event is strictly broader than the non-global-root
event.

## 3. Fixed menus, including reused units — PASS as an upper bound

Let `Z_t` be the output of the `t`-th fixed nonzero signed pattern. Each
`Z_t` is uniform by Theorem 1, even when patterns share inputs, are equal, or
are inverses of one another. No joint independence is required. Therefore

\[
\Pr(\text{some direct screen succeeds})
\le
\min\!\left\{1,
T\frac{2p+2q-10}{(p-1)(q-1)}\right\}.
\]

An all-zero entry has success probability zero, so allowing it does not
invalidate this inequality.

For useful non-global involutions, the corresponding statement is

\[
\Pr(\text{some candidate is a useful involution})
\le
\min\!\left\{1,\frac{2T}{(p-1)(q-1)}\right\}.
\]

This is an upper bound, not a `Theta(T/N)` law. A menu containing `T` copies
of one pattern has probability exactly `2/((p-1)(q-1))`, independent of `T`.
The exact repair is to replace “of order `T/N`” by “at most `O(T/N)` on a
balanced family.”

This also fixes the reuse boundary. Reusing a base unit across different
fixed menu entries is covered. Reuse escapes this argument when it removes
the assumed independent-uniform coordinate inside a candidate—for example,
when two nominal inputs are the same random state and combine to a net
exponent `2`—or when the reuse rule is chosen after observations.

## 4. Balanced-family asymptotics — PASS after preserving the inequality

For `p,q=Theta(sqrt(N))`,

\[
(p-1)(q-1)=\Theta(N),
\qquad
2p+2q-10=\Theta(\sqrt N).
\]

Thus one direct-screen probability is `Theta(N^{-1/2})`, and the menu
success probability is

\[
O\!\left(\min\{1,TN^{-1/2}\}\right).
\]

If the input length is `n=ceil(log_2 N)` and `T=poly(n)`, this is

\[
2^{-n/2+O(\log n)},
\]

so the claim of exponential smallness is correct. The candidate's
`T N^{-1/2+o(1)}` notation is acceptable only as the scale of the union-bound
right-hand side, not as an equality for the actual success probability.

## 5. Adaptive fresh-pivot trials — PASS with the exact filtration condition

Let `H_{t-1}` be the full history before trial `t`. This includes all earlier
observations, choices, and failures. Suppose

- `C_t` and `s_t in {+1,-1}` are determined by `H_{t-1}`; and
- the selected pivot `U_t` is uniform and independent of `H_{t-1}`.

Then

\[
Z_t=C_tU_t^{s_t}
\]

is uniform conditional on every realized history. In particular,

\[
\Pr(Z_t=z\mid H_{t-1})=\frac1{|G|}.
\]

Earlier failures can heavily bias the reused variables and hence `C_t`.
They still cannot bias `Z_t`, because the independent unseen pivot masks
that multiplier. Conditioning only on the event that all earlier trials
failed gives a mixture of identical uniform laws, which is again uniform.
The same per-trial bound and union bound therefore apply.

“Fresh uniform” must mean conditionally uniform given the full past, not
merely marginally uniform and not merely unobserved. For example, if `U_2`
is an unseen copy of `U_1`, then it is marginally uniform but is determined
after `U_1` is observed. The adaptive conclusion does not apply. The
candidate's original independent `X_i` model supplies the required
condition, so this is a scope clarification rather than a counterexample to
Theorem 1.

## 6. The final scope claim — FAIL

The candidate concludes:

> Multiplication inside the unit group, with choices independent of that
> presentation, preserves uniformity exactly.

This is false if “that presentation” means the integer endpoint, gcd-free
block, multiplicity, and magnitude data named in the preceding text.
Presentation independence does not imply that a choice is made before the
group element is observed.

A minimal group-only counterexample uses `N=15`. Let `X` be uniform in

\[
G=\{1,2,4,7,8,11,13,14\}.
\]

After observing only the residue `X`, choose exponent `+1` except choose
`-1` for `X=8` and `X=13`. Then

\[
8^{-1}\equiv2\pmod {15},
\qquad
13^{-1}\equiv7\pmod {15}.
\]

The output puts probability `1/4` on each of `2` and `7`, probability `1/8`
on each of `1,4,11,14`, and probability zero on `8,13`. It is not uniform.
The rule uses only the observed group residue. It uses none of the relation
presentation data listed by the candidate.

The example also shows why the theorem cannot establish the asserted
necessity that every successful selector must manufacture correlation *from
the integer presentation*. The theorems only exclude fixed choices and
predictable choices masked by an independent unseen pivot. They do not
exclude choices based on an observed residue, nonuniform inputs, or
correlated inputs. Whether one of those other escape routes gives a useful
uniform factoring algorithm is a separate question.

## 7. Exact repair

The numbered theorems need no change. Replace the final scope conclusion by:

> Under the independent-uniform input model, fixed signed orientations and
> adaptive products with a conditionally uniform unseen pivot cannot improve
> the one-candidate direct-screen probability. F62's named selector lies
> outside this theorem because it chooses from integer presentation data.
> The theorem does not show that presentation dependence is the only escape;
> observed-residue dependence and correlated or nonuniform base states are
> also outside its scope. Reuse across fixed menu entries remains covered.

Also replace the self-inverse menu phrase by the exact inequality

\[
\Pr(\text{some useful involution})
\le \frac{2T}{(p-1)(q-1)}=O(T/N)
\]

on balanced families. With these changes, the result passes.
