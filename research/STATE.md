# Research State

Updated 2026-09-07 after cycle 15. All jobs are terminal. No expected-quasipolynomial factoring algorithm is established.

## Target and sufficient interface

The target is one classical Las Vegas algorithm that factors every integer in
uniform expected quasipolynomial bit complexity. Failures, restarts, partial
verified outputs, public input shaping, approximate verified subroutines, and
variable attempt durations are allowed.

P249 remains a broad sufficient interface. A public FacRoot procedure on a
uniform Jacobi-positive unit may have arbitrary cost-success correlation. A
uniform quasipolynomial bound on mean verified cost divided by valid-output
probability gives all-input factoring by uncapped dovetailing.

## Promoted cycle result

P251 promotes the selected N-linked jump relative to its declared real-orbit
and three-gap dependencies. For an orbit prefix put
\(m=t+1,L=u+v,d=L-m\) and
\[
 q=(\beta-\alpha)\bmod L=Nu^{-1}\bmod L.
\]
This is generally different from \(N\bmod L\); \(q=0\) is failure. With
\(s=\min(q,L-q)\), every accepted rank difference is covered by
\[
 \{s-h,m-s+h:0\leq h\leq\min(d,\lfloor N/L\rfloor)\}.
\]
The menu dominates each endpoint-valid output. Sampled-endpoint rejections
remain failed attempts.

For \(t=(N-1)/2\), let
\(r=\min(a^{-1}\bmod N,N-a^{-1}\bmod N)\) and
\(s_0=\lfloor t/r\rfloor\). If \(r\geq2\), the actual centered jump is
\(s=s_0\), and one inverse, one quotient, and four gcds on
\(s,s-1,2s-1,2s-3\) dominate it. Equivalently, when \(N=2rs+R\), use
\(R,R+2r,R+r,R+3r\). If \(r=1\), the actual jump is \(s=1\) and has no
proper gcd; the raw value \(s_0=t\) belongs to a different source.

P251 gives an explicit uniform-unit upper bound for this menu on distinct
semiprimes, which is \(O(1/N)\) at fixed factor balance. On every odd
composite, including prime powers, a rational input \(a=xy^{-1}\) with unit
\(1\leq x,y\leq H\) has no selected half-menu factor when \(5H\) is at most
the least prime. Generation factors remain separate valid outputs. No source
lower bound or factoring algorithm follows.

## Fifteenth-cycle evidence

The return-map check passed 4,396 orbit states and 964,448 accepted pairs
through odd \(N\leq31\). The six-rule F339 search retained all 168 F337
source attempts and evaluated 2,754 rule views on 459 cells. Some post hoc
cells had factor probability above 0.4 or 0.6, but every coupled hit lay in
its fully charged fixed-jump menu. The strongest menus used 6, 34, or 104
gcds. No rule was best on all three inputs, and the adjacent rule had no hit.

All three search inputs factor at the first Fermat square test using only
\(N\). They do not establish a performance advantage over that Fermat control
or on broader inputs. General other jumps, larger-height sources, nonlinear
transcript uses, and wider-gap inputs remain open.

Fresh reconstruction matched all four P251 claims. Finite algebra checks
covered 53,186 half-orbit unit parameters through odd \(N\leq511\), all
semiprime source counts, and every guarded rational-height class. The actual
\(r=1\) branch never factors. A separately labeled raw-\(s_0\) diagnostic
factored 168 times and was never credited to the actual source or cost.

An unpromoted conservation law gives
\[
 S(u,L)+S(\alpha,\alpha+\beta)=S(a,N)+2,\qquad S(u,L)\leq S(a,N).
\]
It bounds deleted-interval count discrepancy by \(5S(a,N)\). With P250, a
marginally uniform Jacobi-positive source has polynomial expected direct-menu
cost without rejecting rare large-digit parameters. Useful source success and
one-triple accounting remain assumptions; biased sources need their own mean.

F340 is an unrun route:F29 design. Under its unit and derivative guards, its
degree-four seed uses a critical-value discriminant whose negative Jacobi
character forces local fiber sizes four and two in opposite prime fields. At
higher depth, the public runtime screens \(\Delta_t=H_t(1/2)-H_t(X)\); an
exact divided-difference identity relates it to the proposed character
selector. No higher-depth fiber or growth law is proved. P245 does not
automatically transfer across Jacobi-based rejections.

## Current gap, counts, and restart

No public procedure is proved to meet P249's per-input expected cost/success
contract. P250 and P251 give only their stated source-specific upper bounds
and zero regimes. F339's finite nulls and direct-menu controls do not close
general coupled or randomized procedures.

The catalog has 642 records, 34 routes, 555 experiments, 249 supported assignments, and 306 explicit unknowns.

Next, verify F340's degree-four fiber and divided-difference identities. Then
run its five public policies on F321's wider-gap balanced and unbalanced
inputs, charging every probe, guard, character, update, factor, and failure.
Keep exact root and prime-field source distinctions in offline diagnostics.
Test whether character bias changes higher-depth root growth after all costs;
a fitted finite trend is not a success theorem.
