# F214 provenance

## Research question

F214 freezes the exact named-model boundary for the C192/F209 remaining
primitive:

> Given the complete factorization of
> \(m\mid\operatorname{lcm}((N-1)/2,
> N-\lfloor\sqrt N\rfloor^2)\), locate a balanced modular-inverse point
> with the endpoint product constraint without scanning the balanced
> interval, the unit group, or an equally large explicit representation.

The packet specializes first to the permitted full modulus
\(m=K=(N-1)/2\), where an exact integer collapse is available. It then
audits the direct scan, explicit paired CRT, explicit local-sum MCSS,
continued-fraction completion, direct bivariate Coppersmith, and termwise
Fourier formulations.

## Local promoted and progress sources

1. `PROMPT.md` supplies the bit-length and numerical-QP conventions and the
   requirement not to infer asymptotic runtime from finite evidence.
2. P175 in `PROVED.md` supplies the audited use of
   Gao--Feng--Hu--Pan Theorem 3.1 as a terminal after a true factor residue
   modulo a sufficiently large unit modulus is known.
3. P183 in `PROVED.md` supplies the one-near-size-spine recurrence theorem
   and the exact definitions of \(K,E,M\).
4. C192 in `notes/Progress.md` states the remaining inverse-box primitive
   and records that F209's observed pruning still required a
   \(\Theta(\sqrt N)\) same-node scan.
5. `experiments/F209_D01_inverse_torsor_interval_frontier/RESULT.md`
   supplies the finite experiment's exact scope. No F209 row is used as
   proof evidence in F214.

The F212 and F213 manifests were consulted only as packet-format precedents.
No mathematical claim from either candidate is imported.

## Primary source for the arithmetic-progression terminal

Yiming Gao, Yansong Feng, Honggang Hu, and Yanbin Pan, “On Factoring and
Power Divisor Problems via Rank-3 Lattices and the Second Vector,”
Cryptology ePrint Archive, Report 2025/1004, current revision cited by P175,
[`eprint.iacr.org/2025/1004`](https://eprint.iacr.org/2025/1004), primary
PDF
[`eprint.iacr.org/2025/1004.pdf`](https://eprint.iacr.org/2025/1004.pdf).

Exact use: Theorem 3.1 with \(r=1\) locates a selected prime divisor
\(p\equiv s\pmod m\) in

\[
O\!\left(
\left\lceil\frac{N^{1/4}}m\right\rceil
\log^{7+3\epsilon}N
\right)
\]

deterministic Turing-machine bit operations, under the source's unit and
range premises. F214 invokes it only for a numerical-QP-size list that is
guaranteed to contain the true residue.

## Primary source for CRT sum choices and MCSS

Markus Hittmeir, “Integer Factorization as Subset-Sum Problem,” *Journal of
Number Theory* **249** (2023), 93--118, DOI
[`10.1016/j.jnt.2023.02.010`](https://doi.org/10.1016/j.jnt.2023.02.010),
author preprint
[`arXiv:2205.10074`](https://arxiv.org/abs/2205.10074).

Exact scope used:

1. local modular-hyperbola sum choices combine under optimal CRT;
2. the factorization search can be formulated as a multiple-choice
   subset-sum instance;
3. the paper's first relevant procedure is deterministic and rigorous but
   gives a power-scale special-purpose improvement, not numerical QP at the
   F214 scale; and
4. the faster two-list time-space procedure is explicitly presented without
   a rigorous asymptotic runtime analysis and with non-negligible space.

F214 proves its own fiber and explicit half-list cardinality bounds. It does
not attribute those bounds to Hittmeir and does not infer hardness of MCSS.

## Primary sources for the bivariate small-root range

Don Coppersmith, “Small Solutions to Polynomial Equations, and Low Exponent
RSA Vulnerabilities,” *Journal of Cryptology* **10** (1997), 233--260, DOI
[`10.1007/s001459900030`](https://doi.org/10.1007/s001459900030), publisher
record at
[`research.ibm.com`](https://research.ibm.com/publications/small-solutions-to-polynomial-equations-and-low-exponent-rsa-vulnerabilities).

Jean-Sébastien Coron, Alexey Kirichenko, and Mehdi Tibouchi, “A Note on the
Bivariate Coppersmith Theorem,” *Journal of Cryptology* **26** (2013),
246--250, DOI
[`10.1007/s00145-012-9121-x`](https://doi.org/10.1007/s00145-012-9121-x),
primary manuscript
[`orbilu.uni.lu`](https://orbilu.uni.lu/bitstream/10993/12392/1/copnote.pdf).

Exact use: for an irreducible bivariate integer polynomial of maximum degree
\(\delta\) in each variable and scaled height \(W\), the proved direct
small-root guarantee has product threshold \(XY<W^{2/(3\delta)}\), with
the source's explicit constant or epsilon slack. F214 has \(\delta=1\) and
shows that its full-box product bound is \(\Theta(W)\), outside the
sufficient range. No converse is claimed.

## Primary source delimiting “lattice optimality” language

Yoshinori Aono, Manindra Agrawal, Takakazu Satoh, and Osamu Watanabe, “On
the Optimality of Lattices for the Coppersmith Technique,” *Applicable
Algebra in Engineering, Communication and Computing* **28** (2017), DOI
[`10.1007/s00200-017-0336-9`](https://doi.org/10.1007/s00200-017-0336-9),
earlier ACISP 2012 version DOI
[`10.1007/978-3-642-31448-3_28`](https://doi.org/10.1007/978-3-642-31448-3_28),
author manuscript
[`ePrint 2012/108`](https://eprint.iacr.org/2012/108.pdf).

Exact scope used: the paper analyzes optimality within specified standard
Coppersmith lattice constructions and selected equations. F214 cites it to
prevent an inflated universal lattice-lower-bound reading. F214 does not
apply an optimality theorem from that paper to polynomial (18).

## Primary source for the totient estimate

J. Barkley Rosser and Lowell Schoenfeld, “Approximate Formulas for Some
Functions of Prime Numbers,” *Illinois Journal of Mathematics* **6**
(1962), 64--94, DOI
[`10.1215/ijm/1255631807`](https://doi.org/10.1215/ijm/1255631807),
primary journal page
[`Project Euclid`](https://projecteuclid.org/journals/illinois-journal-of-mathematics/volume-6/issue-1/Approximate-formulas-for-some-functions-of-prime-numbers/10.1215/ijm/1255631807.full).

Exact use: their explicit lower estimates for Euler's totient imply the
uniform asymptotic consequence

\[
\varphi(r)\gg r/\log\log r,
\]

and hence \(\varphi(r)=r^{1-o(1)}\). The separate estimate
\(2^{\omega(r)}=r^{o(1)}\) is proved elementarily in F214 from a factorial
lower bound. The finite packet claim is the explicit inequality (12), not
the asymptotic shorthand alone.

## Primary modular-hyperbola comparison

Javier Cilleruelo and Moubariz Z. Garaev, “Concentration Points on Two and
Three Dimensional Modular Hyperbolas and Applications,” *Geometric and
Functional Analysis* **21** (2011), 892--904, DOI
[`10.1007/s00039-011-0127-6`](https://doi.org/10.1007/s00039-011-0127-6),
author preprint
[`arXiv:1007.1526`](https://arxiv.org/abs/1007.1526).

Exact scope used: the paper gives upper bounds for the number of modular
hyperbola points in short boxes over prime moduli. F214 uses it only as a
representative primary concentration result. Such a count bound is not an
exact algorithm for locating the promised point modulo the composite
\(K\).

## Search and evidence policy

The public-source search was limited to ordinary mathematical background
and the named primary papers above. It did not search for a solution to the
top-level factoring problem.

No mathematical computation, finite search, random sampling, benchmark,
local experiment, or remote SSH experiment was run. The full-\(K\) collapse,
prime-power fiber bound, scan counts, CRT list counts, and Fourier-support
formula are symbolic proofs. SHA-256 is used only after drafting to freeze
the text.

No durable registry, proved ledger, failed ledger, progress ledger,
statement ledger, process ledger, or inspiration file was changed.
