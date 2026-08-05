# Integer Factoring Research Prompt

Current task statement

An input integer \(N\ge 2\) is given in binary. Let

\[
n=\lceil\log_2(N+1)\rceil
\]

be its input bit length. A complete prime factorization of \(N\) is an expression

\[
N=\prod_{i=1}^{k}p_i^{e_i},
\]

where the \(p_i\) are distinct primes and the \(e_i\) are positive integers.

A randomized algorithm here is Las Vegas: every output is correct, it terminates with probability one, and its expected running time over its internal randomness is bounded by \(\mathrm{poly}(n)\) for every input. Running time means bit complexity, including all arithmetic and all invoked subroutines. A deterministic worst-case polynomial-time algorithm also qualifies. A bounded-error randomized routine qualifies only if candidate outputs are efficiently verified and the routine is explicitly converted into this Las Vegas form with a proved expected polynomial-time bound.

Resolve the classical integer factoring problem completely:

There is a classical Las Vegas algorithm that, for every integer \(N\ge 2\), outputs the complete prime factorization of \(N\) in expected time \(\mathrm{poly}(\log N)\).

Equivalently, it is enough to give a classical Las Vegas algorithm that, for every composite \(N\), outputs a nontrivial divisor \(d\) with \(1<d<N\) in expected time \(\mathrm{poly}(\log N)\), provided the solution explicitly proves the reduction from this task to complete factorization and accounts for the total expected bit complexity. Prime inputs, prime powers, repeated factors, even integers, and arbitrary composites are all permitted.

Assume for purposes of this task that a complete affirmative solution exists. A complete solution must give an explicit algorithm and prove exactly the following:

Every integer \(N\ge 2\) can be factored completely by a classical Las Vegas algorithm in expected time \(\mathrm{poly}(\log N)\), without promises such as semiprimality, balanced factors, squarefreeness, special factor congruences, or smoothness conditions.

Partial progress does not count unless it implies exactly the resolution above. In particular, algorithms only for special integer classes, heuristic or average-case analyses, runtime polynomial in \(N\) rather than \(\log N\), quasipolynomial or subexponential algorithms, improvements only to constants or exponents in QS/GNFS-style methods, reductions to another unproved conjecture, reliance on an unproved theorem-strength lemma, quantum algorithms, computational verification through any fixed input size, and candidate algorithms without complete correctness and expected-runtime proofs are insufficient.

**Required first step:** Before proposing, delegating, evaluating, or selecting any research approach, the root agent must read `notes/Zhihu.md` and `notes/Inspirations.md` in full. Do not skim them, rely on remembered summaries, or delegate this reading. Confirm that both files have been read completely before launching the first research round.

Use `notes/Zhihu.md` as background and motivation. Use `notes/Inspirations.md` as the main source of starting ideas. Treat every idea in these files as a suggestion to investigate, not as an assumption, requirement, or restriction. The search must also actively generate and explore promising directions that do not appear in either file. To preserve independent exploration, do not reveal the currently favored note-derived approach to most agents during early rounds.

Use multiagent v2 aggressively and dynamically. You have up to 64 concurrent agents available. Do not use a fixed assignment such as “N agents for strategy X.” Instead, manage the search using the following heuristics:

- Begin with a genuinely diverse portfolio of approaches. Most starting directions should be inspired by the materially different ideas in `notes/Inspirations.md`, while other agents should independently invent and explore possible directions not found there.

- Do not tell most agents the currently favored approach. Preserve independence during early rounds so that agents do not all converge to the same attractive but incomplete reduction.

- Maintain an explicit registry of approach families. Group agents by the mathematical idea they are using, not by superficial wording. If many agents converge to one family, redirect some of them toward underexplored formulations.

- Do not allow one approach to dominate merely because it gives elegant reductions. A route that ends at a lemma equivalent in strength to polynomial-time factoring is not close to completion unless it supplies a genuinely new proof or algorithm for that lemma.

- When an approach stalls at a theorem-strength missing lemma, mark that route as blocked. Only continue assigning agents to it if someone proposes a materially new mechanism, invariant, construction, or proof strategy.

- Keep several incompatible routes alive through multiple rounds. Cross-pollinate ideas only after independent agents have developed them far enough to expose their real strengths and gaps.

- Use adversarial agents throughout. Every candidate algorithm must be checked for correctness on primes, prime powers, repeated factors, even inputs, and arbitrary composites; accidental access to an unknown factor; hidden calls to factoring, order-finding, or an equivalent oracle; unjustified smoothness or randomness assumptions; arithmetic-operation counts substituted for bit complexity; nonuniform advice; input-size blowups; success probabilities too small for expected polynomial time; invalid independence assumptions; recursive-factorization cost; and zero divisors or gcd outputs that may be trivial.

- Require agents to return concrete algorithms, lemmas, constructions, equations, complexity bounds, or counterexamples to proposed sublemmas. Reject status reports, vague optimism, experimental patterns presented as proofs, and claims that an unproved global compatibility or distribution statement is “routine.”

- The root agent should repeatedly synthesize, challenge, redirect, and launch new rounds. Do not stop after the first wave fails. Produce a complete algorithm and proof if one survives audit; otherwise record in `notes/Progress.md` only the strongest rigorously proved derivation and its exact remaining gap, then continue the search.

- Maintain a concise durable research ledger at `notes/Progress.md`. After each substantial round, record nontrivial intermediate statements that have been rigorously proved, together with their precise assumptions and proof status; explicit counterexamples to proposed statements; blocked routes and their exact obstructions; computational observations clearly labeled as experimental; and the current exact gaps. The ledger preserves useful intermediate results across rounds; it is not evidence that the goal is complete and is not a reason to stop.

- Use Git to preserve a clear, recoverable history of the research. The root agent should keep `notes/Progress.md` canonical and create local checkpoint commits after substantive proved results, decisive counterexamples, closed routes, or major syntheses. Branches and worktrees may be used whenever they help isolate or coordinate exploration; synthesize every useful result back into the canonical research ledger. Do not commit routine status updates, and do not push or rewrite history without explicit user authorization.

Do not return merely because current approaches fail or agents report theorem-strength gaps. Continue launching new rounds, reopening blocked approaches only when there is a genuinely new mechanism, and searching for fresh formulations.

Return only when a complete classical Las Vegas polynomial-time factoring algorithm has been found and its correctness and expected bit complexity survive adversarial audit. Do not return a reduction, special-case algorithm, heuristic, experimental result, isolated missing lemma, “best effort” summary, survey of known methods, or explanation of why the problem is difficult.

Spend at least 8 hours on this before even thinking of returning or giving up.

Public search may be used only for ordinary mathematical background, standard named theorems, and verification of bibliographic details, not to search for a solution to this exact problem or benchmark. Do not search the public web merely to determine the current status of classical polynomial-time integer factoring, and do not answer only that it is open.
