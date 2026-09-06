# F268-D01 pre-run self-audit

# Verdict: FAIL

frozen_manifest_sha256: b99d47d7ba7a01c456a0b755a5e77f42a237be73ffd6ea422e38d03b076a1cc9

The exact frozen D01 `label_audit.cpp` uses `std::tie` but does not directly
include the standard `<tuple>` header that declares it. A target compiler can
accept this only through a nonportable transitive include. D01 therefore does
not meet its C++17 static contract and is not authorized for compilation or
execution.

This defect was found after D01 was frozen and before any external audit,
compilation, self-test, corpus generation, preflight, local search, or remote
command. The frozen D01 files and `FROZEN.sha256` remain unchanged. The narrow
successor F268-D02 adds the missing include and records this provenance.
