# F263 final self-test

The authoritative target source compiled with the frozen runner flags.  Its
exact algebra-only self-test passed and printed

```text
SELF_TEST_PASS controls=12 columns=70 ranks=58,58 nullities=12,12 identities=14 shortcuts=0 adjacent=4 dyadic=0 candidates=148
```

The checks include:

- the even and odd `B` central-binomial parity formulas;
- the public `B=p` cleanup case;
- the unique central numerator and shifted denominator locations;
- unit central denominators and odd-parity multiplier screens;
- exact quadratic-jet composition;
- all 12 mandatory transfer and jet identities;
- both public-prime ranks and nullities;
- the four exact adjacent-start recurrences;
- zero accepted dyadic recurrence in the frozen search box;
- zero operational shortcut among authenticated identities;
- the 148 distinct candidate syntaxes;
- saturated-before-proper gcd ordering;
- literal deterministic cohort hashing;
- bounded-capacity predicate and generator behavior; and
- retention of exact accepted identities and recurrence coefficients.

The self-test does not generate or inspect a frozen discovery or held-out
cohort.  Its stdout and empty stderr are retained under `TARGET_CHECKS/`.
