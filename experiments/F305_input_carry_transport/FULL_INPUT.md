# Restoring the full input after the canonical transport

F305's floor transport is stated for the canonical odd input nu in [1,M).
It applies to the full-input B oracle in P239 with a computable correction;
the carry definition must not be silently changed.

Write N=nu+tM, with t>=0. The canonical inverse graph is unchanged, and
for every shifted domain (c,d),

    q_cd(N)=q_cd(nu)-t.

The exact polynomial identity

    binom(q-t,2)=binom(q,2)-t*q+binom(t+1,2)

therefore gives, with phi=M/2,

    B_cd(N)=B_cd(nu)-t*H_cd(nu)+phi*binom(t+1,2) mod M.  (1)

Here the first-carry sum H_cd is computable without a rectangle oracle.
For H_00=sum(uv-nu)/M and

    h(c)=sum_(u odd<c)u^(-1) mod M,

the shifted product expands to

    H_cd(nu)=H_00(nu)+nu*h(c)+nu*h(d) mod M.            (2)

Its additional term M*C(c,d) vanishes at this precision. P238 computes
H_00. The reciprocal prefixes use the finite progression expansion in
FLOOR_MARGINALS.md. Hence all corrections in (1) have polynomial bit cost
in the full input length and k.

The correction is a sum of c-only, d-only and constant terms. It cancels
from the four-corner difference used by P239. Thus that count identity
can also use B_cd(nu) directly, with its multiplier N-M/2 reduced modulo M.
This does not compute B_cd(nu): the fixed carry-measure transform from
REPORT.md is still missing.

This integration observation follows from exact integer identities; it is
not a claim that merely replacing N by nu preserves an individual carry
sum. The graph and rectangle counts are invariant, but the individual B
values require (1).
