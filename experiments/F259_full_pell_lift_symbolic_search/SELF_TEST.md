# Pre-freeze self-test

The authoritative target-host compile and algebra-only self-test used

```text
/usr/bin/g++ -std=c++17 -O2 -pthread symbolic_search.cpp -o symbolic_search
timeout 120s nice -n 15 ./symbolic_search --self-test
```

The corrected source printed

```text
SELF_TEST_PASS N=4331 families=22 words=255 atoms=41078 identity_mining={prime=1000000007,samples=96,holdout=64,columns=16,rank=14,nullity=2,cocycle_real=1,cocycle_imag=1}
```

This self-test materializes one small public semiprime only to check exact
algebra, grammar dimensions, and score ranges. It does not generate or inspect
the frozen discovery or held-out cohorts. The mathematical run has not started.

The local Mac compiler could not find Boost Multiprecision. The requested
remote host has `/usr/include/boost/multiprecision/cpp_int.hpp`, and the
authoritative runner also uses `/usr/bin/g++` there. No alternate arithmetic
library or implementation was substituted.
