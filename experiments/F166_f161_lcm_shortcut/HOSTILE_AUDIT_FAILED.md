# F166 hostile-audit workflow failure

The first hostile audit is preserved in `HOSTILE_AUDIT.md` with SHA-256

`95fa74a0cee818b28fd333f273d2cc4befc7f3e6c9d47c9afab23841ea91bc83`.

Its mathematical verdict was `PASS`, but Section 7 reports an exhaustive
finite check that was not preregistered in `REGISTRY.md`. This violates the
repository computation protocol. The finite check is not needed by the
proof and must not be used as evidence.

The frozen candidate statement and proof are unchanged. A fresh independent
proof-only hostile audit must pass before blind reconstruction or promotion.
