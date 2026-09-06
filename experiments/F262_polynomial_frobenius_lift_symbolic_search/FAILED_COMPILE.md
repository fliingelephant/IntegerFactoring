# Preserved failed target compile

The first authoritative target-host compile used:

```text
nice -n 15 /usr/bin/g++ -std=c++17 -O2 -pthread symbolic_search.cpp -o symbolic_search
```

It failed before execution. `eval_candidate` used an `auto` lambda whose two
conditional branches produced different Boost expression-template types for
`cpp_int`. The diagnostic ended at source line 575 with:

```text
error: operands to ?: have different types ... subtract_immediates ... and ... modulus ...
```

The repair gives the three modular lambdas explicit return type `T` and
materializes each result. No mathematical input or cohort was opened. The
failed source was not frozen. The corrected source compiled successfully in
the same target toolchain.
