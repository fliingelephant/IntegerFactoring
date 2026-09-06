# F283 provenance

## Origin

F283 is a proof-only boundary packet for the sole evaluator left open by
P230/F282:

\[
 F_B(a)=\frac{\Delta^BX^{2B}|_{X=a}}{B!}
       =h_B(a,a+1,\ldots,a+B)\pmod N.
\]

P230 proves that a uniform public shift makes this scalar a constant-success
splitter on the balanced distinct-odd-semiprime promise. It also proves that
the unnormalized difference is zero modulo \(N\). F283 does not alter that
theorem.

The parent analysis supplied the coefficient identity

\[
 [a^k]F_B(a)=\binom{2B}{k}
 \left\{\begin{matrix}2B-k\\B\end{matrix}\right\}
\]

and the observation that every prime \(B+1<r<2B\) divides every coefficient
of \(F_B\). F283 reconstructs both facts from first principles and connects
them to the central-binomial and interval-product boundaries already
recorded by P227, P230, F197, and F249.

## New boundary

The packet organizes seven exact facts around the evaluator:

1. it is a generalized/r-Stirling diagonal endpoint;
2. its canonical coefficient recurrence and constant-matrix realization
   have minimal dimension \(B+1\) over \(\mathbb Q(a)\);
3. translation and direct block composition use the full coefficient range;
4. monotone divided-power composition crosses a structure constant whose
   gcd with \(N\) is \(p\);
5. the unnormalized endpoint is the known zero modulo \(N\);
6. the guaranteed \(q\)-zero is universal interval content whose explicit
   extraction already factors; and
7. the immediate quotient obtained from a raw lift modulo \(N^2\) can be a
   unit and has no promised factor.

These facts reject a search in the named representations. They do not reject
an outside-scope nonlinear, adaptive, or isolated-endpoint fast-forward.

## Execution provenance

F283 used no source code, SageMath, numerical calculation, finite pattern
search, local or remote cohort, external dataset, or literature search. It
did not modify F282, a proof ledger, a failure ledger, a progress note, or a
registry. It was authored only after the theory-only alignment gate approved
a scoped no-search boundary. No staging or commit belongs to this packet.
