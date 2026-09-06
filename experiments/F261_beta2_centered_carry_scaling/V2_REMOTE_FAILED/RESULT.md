# F261-D02 V2 result

Status: **COHORT-GENERATOR CAP FAILURE; NO MATHEMATICAL ROW**.

The exact frozen V2 source compiled.  The exact self-test and complete
preflight passed.  Because the live load exceeded 64, the runner reduced the
worker count from four to two as registered.

```text
F261_V2_SELF_TEST_PASS
20,000,000 carry iterations: 4.11119 seconds
conservative production projection: 594.76 seconds
registered limit: 14,400 seconds
```

All four separately tagged generator benchmarks had positive hits, including
three safe-safe hits in 20,000,000 attempts.  Production then stopped before
the first row file because the exact 16-bit `close` cohort exhausted its
frozen 64-attempt row cap:

```text
F261_D02_FAIL cohort attempt cap exhausted: close f=16
```

No summary, row, inverse-map, or consecutive-prime output exists.  This is a
generator/protocol failure, not mathematical evidence about centered carries.
Changing the generator, attempt cap, or cohort requires a new preregistration
and explicit user approval; V2 must not be rerun unchanged.

Retrieved hashes:

```text
F261-D02.launch.log       d13bfb42404f63abc44d1984444be641ba5ce5c2fda56f7120c36b5df035b0d7
F261-D02.stdout           9ae3c9f3ce4e9b8b10b2790aacdc3b896a048f00c87f3727e41a7eaef3cb259e
F261-D02.stderr           76dfa3136bec1770b6a2651b0a42be3bedbb5799f82b93367559462e416dcd08
F261-D02.preflight.txt    550b498265358dac837d4c4fb8a2d43036aa02a5e408eca2f233613317c7629a
incompatible process log e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
```
