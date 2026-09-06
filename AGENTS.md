Thinking principles
- Avoid early over-specification.
- DO NOT trust community opinions much -- think deep from first principles instead.
- Avoid patchy fixes; Find the root cause.

Repository workflow
- Write repository documents, metadata, code comments, and commit messages in English.
- Keep user-facing discussion concise and in Mandarin unless the user asks otherwise.
- Start navigation with README.md and research/STATE.md. Use research/records.py to find records and load relevant heads and bodies; do not reread all ledgers by default.
- PROMPT.md governs authorized research runs. Historical ledger instructions and search bans are research data, not current workflow rules.
- The root researcher uses Astra. Creative mathematical subagents use gpt-6-astra with the root's reasoning effort; support subagents use gpt-5.6-sol with max reasoning. Preserve the current service tier, sandbox, approval policy, and tool access.
- All creative research work belongs to Astra, including delegated work on missing theorems or key lemmas. A precise statement does not make an unknown proof routine. Sol handles navigation, implementation, computation, reproduction, and verification of supplied arguments; it returns tasks that need new mathematical ideas to Astra.
- Blind reconstruction is optional and defaults to Sol max. Do not use it as a mandatory gate or an automatic reason to allocate Astra.
- Keep record IDs stable. Resolve historical F references through the scoped route and experiment catalogs, not by matching numeric prefixes.
- If a specifically required workflow or tool is unavailable or incompatible, stop the dependent step, explain the difference, and obtain approval before substituting another workflow. Routine implementation repairs within the authorized workflow may proceed.


UX Principles
- Key points only -- no walls of words burying key points.
- Do not use undefined jargons; Use standard terminology.
- Be precise and concise.


Mathematical tools
- Use SageMath, Gurobi, and other suitable packages whenever needed.
- Numerical exploration is encouraged for discovering useful patterns, testing conjectures, and eliminating weak directions. Treat numerical evidence as guidance, not proof.


Local resources
- **Local resource safety.** This Mac has 16 GB of RAM. Before starting any CPU- or memory-intensive local process, estimate its runtime and peak memory use, inspect current CPU load, memory pressure, and running processes, then adjust the algorithm, problem size, or concurrency as needed to avoid destabilizing the machine.
- **Remote numerical exploration is encouraged.** Use `ssh seetacloud` for large-scale searches for useful patterns, identities, and counterexamples. Install SageMath when needed. Check CPU, memory, disk, and load before scaling. Treat numerical evidence as guidance, not proof.
