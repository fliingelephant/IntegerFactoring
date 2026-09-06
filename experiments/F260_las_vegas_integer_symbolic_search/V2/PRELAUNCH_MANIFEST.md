# F260-D02 V2 prelaunch manifest

Status: **FROZEN STATIC REPAIR — VALIDATION AND HOSTILE AUDIT PENDING**

F260-D02 is a new sibling packet. F260-D01 remains immutable and failed. Its
hostile audit SHA-256 is
`9e49fb75f86b5ccdd7b3290053099cd822ab547a06495dbee82f64ff7a5e636d`.

## D02 packet bytes

```text
d0ceeddbab866cc9d35f85565ffc0f3282a955fd22603d666e9d00790dd00229  ALGEBRA.md
2ebd75dea01d34fe72682d45524abc2e6072618866393d963ba6dccd221059d7  PREREGISTRATION.md
c6d0f016e471911c115a497311ef05e5682c796df6c3887626ac5cb25bcb3911  search.cpp
6812855a4ef7b87c351cfe1c29d098dae0470788139d9ca27b7c8d94f5de43be  remote_run.sh
b8f019b4e9b78cec7fcd772fb75ca7395c881ae6793db711bc78fe14991d9c59  PROVENANCE.md
34baff67c8af30225206e32d8009c3be1dee06d405532bd6857baf82e14a4c6f  VALIDATION_PENDING.md
297f87601eaab098cb18cc6244543bbd7c80c390b2ba575879f80e41f3ec04a3  STATIC_REVIEW.md
63ce96dcaa52114b7d18a1e4e516bc63db76cd533089abbbf7389c4fa8f48a54  AUDIT_REQUEST.md
```

`FROZEN.sha256` is the machine-readable authentication boundary. It also
authenticates this manifest. A later hostile audit is not part of the frozen
repair bytes. The runner authenticates the audit through a one-record
sidecar, exact PASS text, and the SHA-256 of the exact `FROZEN.sha256` bytes.

## Qualification state

The packet received a static source/document review only. It was not compiled,
executed, self-tested, benchmarked, or transferred. No corpus or cohort was
generated or inspected. No durable ledger changed. F258-D01 was active, so
the registered firewall withheld target validation.

Do not start discovery or held-out directly. After F258-D01 stops, the only
registered path is:

1. obtain the independent hostile audit requested in `AUDIT_REQUEST.md`;
2. transfer the exact frozen packet and the authenticated audit artifacts;
3. invoke `remote_run.sh` in its registered target directory; and
4. let the runner authenticate, compile, self-test, benchmark, and enforce all
   resource and production gates.

Any change to a listed byte invalidates the audit request and requires a new
experiment freeze.
