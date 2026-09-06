# Preserved pre-freeze self-test failure

The first authoritative target-host compile succeeded.  Its algebra-only
self-test then exited with

```text
F263_ERROR candidate count drift: 148
```

The source expected 146 candidate syntaxes, but the frozen catalog contains
148.  Inspection showed no duplicate syntax and no missing algebra check; the
manual assertion was wrong.  The assertion was corrected to 148.  No cohort
was generated or opened.  This failed source revision is not authoritative
and is excluded from every mathematical result.

The next pre-freeze source added an exact saturated-before-proper ordering
test.  Its target-host self-test failed with

```text
F263_ERROR saturated-before-proper ordering
```

The test constructed `Eval` from a temporary `uint128_t(15)`, while `Eval`
retains a constant reference to its modulus.  The reference therefore
dangled inside the test.  Production always passes the persistent row field
`in.n`; no production arithmetic or grammar was implicated.  The failed
source and stderr hashes were

```text
source: 720c7d603307de526b62851e1d30388d99fa47bf549b3f913d47eba2b71dbe27
stderr: c5238018ffabf27aac5e2dcc2b95ee91acf74da4567114197db960299155a59c
```

After explicit approval, the test alone was repaired by binding
`const uint128_t test_n=15` before constructing `Eval`.  No cohort was
generated or opened.
