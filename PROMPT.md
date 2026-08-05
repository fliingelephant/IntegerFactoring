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

> There is a classical Las Vegas algorithm that, for every integer \(N\ge 2\), outputs the complete prime factorization of \(N\) in expected time \(\mathrm{poly}(\log N)\).

Equivalently, it is enough to give a classical Las Vegas algorithm that, for every composite \(N\), outputs a nontrivial divisor \(d\) with \(1<d<N\) in expected time \(\mathrm{poly}(\log N)\), provided the solution explicitly proves the reduction from this task to complete factorization and accounts for the total expected bit complexity. Prime inputs, prime powers, repeated factors, even integers, and arbitrary composites are all permitted.

Assume for purposes of this task that a complete affirmative solution exists. A complete solution must give an explicit algorithm and prove exactly the following:

> Every integer \(N\ge 2\) can be factored completely by a classical Las Vegas algorithm in expected time \(\mathrm{poly}(\log N)\), without promises such as semiprimality, balanced factors, squarefreeness, special factor congruences, or smoothness conditions.

## Success criteria

Partial progress does not count unless it implies exactly the resolution above. In particular, algorithms only for special integer classes, heuristic or average-case analyses, runtime polynomial in \(N\) rather than \(\log N\), quasipolynomial or subexponential algorithms, improvements only to constants or exponents in QS/GNFS-style methods, reductions to another unproved conjecture, reliance on an unproved theorem-strength lemma, quantum algorithms, computational verification through any fixed input size, and candidate algorithms without complete correctness and expected-runtime proofs are insufficient. If the statement above is ambiguous about what counts as an answer, ask before starting; never resolve ambiguity silently.

Polynomial running time must be proved symbolically in the uniform bit-complexity model; it cannot be inferred from benchmarks, fitted curves, successful factorizations, or any finite range of inputs. With \(n\) the input bit length, exhibit a fixed polynomial \(P\), independent of \(N\) and its unknown factors, such that

\[
\mathbb E[T(N)]\le P(n)
\]

for every \(N\). Count intermediate bit lengths, random-bit generation, all arithmetic and invoked subroutines, data-structure sizes, recursion, repetitions, and verification. For every randomized or restart step, prove correctness of every returned answer, almost-sure termination, and a success-probability or expected-trial bound sufficient for the claimed total expectation. Constants may affect practicality, but they do not establish or refute polynomiality and must be fixed independently of \(N\).

## Required sources — read in full before starting

Before proposing, delegating, evaluating, or selecting any research approach, the root agent must personally open and read `notes/Zhihu.md` and `notes/Inspirations.md` in full. Do not skim them, substitute a remembered or delegated summary, or begin the first research wave before reaching the end of both files.

Use `notes/Zhihu.md` as background and motivation. Use `notes/Inspirations.md` as the main but non-exclusive source of starting ideas. Treat every idea in either file as a suggestion to investigate, not as an assumption, requirement, or restriction. Most initial approach families should be inspired directly by materially different entries in `notes/Inspirations.md`; do not replace those concrete entries with a generic list of fields. Also actively generate and explore promising directions that do not appear in either file.

After any context compaction or session restart, re-read both source files together with the durable state below before continuing.

## Durable state — create these files before searching

- `STATEMENT.md` — the exact statement, conventions, and success criteria. Fixed for the whole run; never edit it to fit a result.
- `REGISTRY.md` — one row per approach family: family name, exact claim attempted, exact remaining gap, smallest known obstruction, next decisive test, status.
- `FAILED.md` — every closed route: what was tried, the exact obstruction, the evidence for it, and what would make a retry materially new.
- `PROVED.md` — promoted results only, each with its status label and proof or certificate.
- `notes/Progress.md` — nontrivial intermediate statements and the current research synthesis. Record each statement's precise assumptions, proof or certificate, actual status label, and exact remaining gap. This is working state, not a substitute for promotion to `PROVED.md`.

Create any missing durable-state files before the first search. All mathematical work products land in these files, not only in conversation. After any context compaction, re-read these files before continuing; they are the memory, the conversation is not.

## Status vocabulary — literal, never inflated

Every claim carries exactly one label, with these exact meanings:

- candidate — produced by an agent; no checks yet.
- self-audited — re-checked only by its own author or context. For building on, this counts the same as candidate.
- verifier-backed — survived both steps of the verification cadence below: a hostile audit by a fresh agent that tried to refute it, and an independent end-to-end reconstruction by an agent that never saw the proof.
- promoted — verifier-backed and recorded in `PROVED.md`; later work may cite it, and anything built on it carries at most this label.
- independently audited — additionally checked from outside the producing model family: a different-family model or a human. Present final answers at this label when possible.

If no different-family model is available in this environment, do not simulate independence with another instance of the same family — that is label inflation. Instead deliver the final answer at promoted status, state prominently that the cross-family audit has not run, and list the specific claims an outside model or human referee should check first, in order of risk.

A claim's label only advances through the verification steps below. A later argument never inherits more certainty than its weakest premise's label. Never call a mismatched case, a global compatibility assertion, or a polynomial recurrence “routine” — those are where proofs hide their hard step.

## Orchestration

Use subagents aggressively and dynamically, at most 6 concurrent. Work in waves: agents push the frontier, then fresh agents verify what came back. Do not use a fixed assignment such as “N agents for strategy X.”

- Begin with a genuinely diverse portfolio. Most starting families must come directly from materially different mechanisms in `notes/Inspirations.md`, while some agents independently invent and explore possible directions absent from both source files.

- Do not tell most agents the currently favored approach; preserve independence during early rounds so they do not converge on the same attractive but incomplete reduction. Agents may be assigned a direction, but never shown another agent's partial proof of it.

- Group approaches in `REGISTRY.md` by the mathematical mechanism and by their terminal missing lemma, not by terminology. If several agents converge to one family, redirect the surplus toward underexplored formulations.

- A route that ends at a missing lemma as strong as the original problem is blocked, not “one lemma away.” Record it in `FAILED.md`. Reopen a blocked route only for a materially new mechanism, invariant, or construction, and say in `REGISTRY.md` what is new.

- Before starting any route, check `FAILED.md` and state either: “no close prior route” or “closest prior route is X; this differs materially because of <new lemma / source / witness / certificate / scope>.”

- Before assigning agents to a new approach family, spend one fresh agent trying to kill it first: check the smallest instance, and adversarially test any claimed source the approach builds on. Most families die at this step for the price of one agent.

- Require every agent to return a proved lemma, an explicit construction, or a counterexample. Reject status reports, vague optimism, and claims that an unproved global compatibility statement is routine.

Every candidate factoring algorithm must also be checked for correctness on primes, prime powers, repeated factors, even inputs, and arbitrary composites; accidental access to an unknown factor; hidden calls to factoring, order-finding, or an equivalent oracle; unjustified smoothness, distribution, randomness, or independence assumptions; arithmetic-operation counts substituted for bit complexity; uncontrolled intermediate bit lengths; nonuniform advice; input-size blowups; success probabilities too small for expected polynomial time; recursive-factorization cost; and zero divisors or gcd outputs that may be trivial.

## Stalled routes

When a route stalls, classify it explicitly in `REGISTRY.md` as either (a) method failure or (b) evidence against the exact auxiliary claim or mechanism on which the route depends. If (b), redirect part of the effort of that family to counterexample search for that auxiliary claim. Every stalled route must carry one of these two classifications; “still working” is not a classification. This classification must not replace the affirmative task with a general hardness or nonexistence project.

## Verification cadence

Every candidate proof or refutation of a mathematical claim gets, in order: one focused hostile audit round (a subagent instructed to refute it: find any gap, unsupported claim, quantifier slip, or misapplied citation, and be skeptical), then one independent end-to-end reconstruction by a fresh agent that has not seen the proof, working only from the statement and the claimed key ideas. Only after both does the label advance to verifier-backed. A failed audit sticks to that exact version: address the specific objection or retract the claim — never resubmit an unchanged or cosmetically edited proof to a fresh auditor. Audit claimed counterexamples and impossibility conclusions about auxiliary claims with the same hostility as proofs; a wrong refutation closes a route that was alive. Do not re-audit after prose-only edits; re-audit only when the mathematical content changes. Final candidate results should additionally be checked by a model from a different family before being presented as the answer.

## Reporting gate

Report a result to me only on a significant update: a complete proof of the top-level statement; a certified counterexample to a proposed auxiliary claim; a proved lemma that removes a named dependency; a minimal obstruction that closes a route; or a strictly stronger or simpler theorem with proof. A counterexample to an auxiliary claim is an intermediate result, not completion of this affirmative task. New notation, restructuring, another finite computation, or a reduction to a theorem-strength lemma is not significant and goes in the files, not in a report.

## Computation rules

Only write programs when essential; most work here should be proofs. When a computation is justified, it is a named finite question whose output is a small witness, certificate, or table. Never run computation through inline stdin. Every run gets a named source file, the approach-family ID it serves, a timeout, a log, and an output location, recorded in `REGISTRY.md`. A computation can refute a lemma or discover a certificate; it cannot prove an unbounded theorem — preserve the smallest exact certificate and then prove the resulting claim.

Finite experiments, benchmark factorizations, and fitted runtime curves are sanity checks only. They may expose an error or refute a universal claim, but they do not prove polynomial running time.

## Git workflow

Use Git to preserve a clear, recoverable history of the research. The root agent owns the canonical durable-state files and should create local checkpoint commits after substantive proved results, decisive counterexamples, closed routes, or major syntheses. Branches and worktrees may be used whenever they help isolate or coordinate exploration; synthesize every useful result back into the canonical durable state. Do not commit routine status updates, and do not push or rewrite history without explicit user authorization.

## Web policy

Public search may be used only for ordinary mathematical background or standard named theorems, not to search for a solution to this exact problem or benchmark. Do not search the public web merely to determine whether the problem is open, and do not answer that it is open.

## Persistence

Do not return merely because current approaches fail or agents report theorem-strength gaps. Continue launching new rounds, reopening blocked approaches only under the reopen rule above, and searching for fresh formulations. There is no time budget: the completion condition, not the clock, decides when the run ends. Return only when a complete affirmative resolution has survived the full verification cadence; otherwise keep `FAILED.md` and `REGISTRY.md` as the honest record and continue.

This prompt is intended to run as a persistent `/goal`. Treat the active goal as the persistent registration of this task; do not create a duplicate goal, and do not mark it complete until the success criteria above have been met. If persistent goal tooling is unavailable, say so at the start of the run.

## On stop

When I end the run: apply the reporting gate to what you present. Then append to `PROCESS_LESSONS.md`: what you learned this session that would make future runs more efficient — preferring lessons transferable to other mathematical problems, plus any environment issues that wasted time. Process lessons only, never mathematical claims — the name is the rule; math belongs in the other files at its earned label.
