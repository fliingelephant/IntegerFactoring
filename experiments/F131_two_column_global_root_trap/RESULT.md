# F131 result

## Verdict

The proposed auxiliary statement is false. Two distinct nonsquare canonical
exact values can form a square while every endpoint screen has gcd one and
the joint root is the global root (-1\bmod N).

The exact finite counterexample is

\[
N=9407=23\cdot409,
\]

with endpoint pairs ((9025,4802)) and ((6534,6912)). Their exact values
are (2\cdot4655^2) and (2\cdot4752^2), and their joint root is
(4703N-1).

## Corrected law

If distinct exact values have common squarefree kernel (s), write them as
(sa^2,sb^2). Their joint root is global exactly when (a+b=N). This can
happen only for (s\in\{1,2,3\}). Thus every two-column dependency with
(s\ge5) gives a non-global root and a factor.

An unconditional infinite nonsquarefree family shows that the endpoint
screens do not remove the small-kernel trap.

## Evidence status

The theorem passed a corrected hostile re-audit and an independent
proof-blind reconstruction. F131-D01 also checked the two displayed
certificates and eight arithmetic-progression members. The finite run is not
used to prove the infinite statement.

