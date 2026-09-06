# Proof of F177 V2

## 1. Ordinary square-modulus congruence

An exact common ordinary order \(M\) divides both local group orders. Write

\[
p=1+aM,
\qquad
q=1+bM.
\]

Then

\[
N+1-(p+q)=(p-1)(q-1)=abM^2.
\]

This proves

\[
p+q\equiv N+1\pmod{M^2}.
\tag{1}
\]

Put \(x=q/p\). The balance promise gives \(1<x<2\), and

\[
\frac{p+q}{\sqrt N}=\frac{1+x}{\sqrt x}.
\]

This function is strictly increasing for \(x>1\). Its endpoint values are
\(2\) and \(3/\sqrt2\). This proves the strict interval (4) in the
statement.

One residue class modulo \(M^2\) has at most one more element than interval
length divided by \(M^2\). This gives (8). For the true sum,

\[
S^2-4N=(q-p)^2,
\]

so the square and parity test recovers the two primes. Condition (9) bounds
the list by \(Q(n)+1\), which is QP.

## 2. Orientation-free torus square-modulus congruence

For the hidden orientation \(\epsilon\), the common torus order \(B\)
divides both stated local group orders. Therefore

\[
B^2\mid(p-\epsilon)(q+\epsilon).
\]

For \(D=q-p\) and \(\epsilon^2=1\), expansion gives

\[
(p-\epsilon)(q+\epsilon)
=pq+\epsilon p-\epsilon q-1
=N-1-\epsilon D.
\]

Thus \(\epsilon D\equiv N-1\pmod{B^2}\), which is equivalent to (12).
The algorithm scans both possible values of \(\epsilon\), so it does not
need an orientation oracle.

Again write \(x=q/p\). Then

\[
\frac{q-p}{\sqrt N}=\frac{x-1}{\sqrt x}.
\]

This is strictly increasing for \(x>1\), and its upper endpoint at \(x=2\)
is \(1/\sqrt2\). This proves (13). Each sign class contributes at most

\[
1+\frac{\sqrt N}{\sqrt2 B^2}
\]

candidates, so the two classes together contribute at most

\[
2+\frac{\sqrt{2N}}{B^2}.
\]

The identity

\[
(p+q)^2=(q-p)^2+4pq
\]

proves the recovery test (15). Under condition (17), the combined list has
at most \(2Q(n)+2\) entries.

## 3. Bit cost and scope

All moduli and candidates have \(O(n)\) bits. Modular reduction, interval
enumeration, exact integer square root, parity checks, multiplication, and
division are polynomial-time operations per candidate. A QP number of
candidates therefore gives QP bit cost.

The proof uses only the two balanced prime factors and the divisibility of
their local group orders. It supplies no source for \(M\) or \(B\), and it
does not extend to a different factor pattern.
