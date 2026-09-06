# F240 V2 provenance

F240 V1 was frozen as a proof-only packet.  Its fresh hostile audit returned
**FAIL** at one exact decoder endpoint.  For every allowed semiprime,

\[
B=N-1,\qquad u=1
\]

gives

\[
a=b=0,\qquad c=1,\qquad T=0,
\]

so the recovery polynomial is identically zero.  V1 had an unqualified
direct-factor-bank sentence even though its proof noticed possible
degeneracy.

V2 makes only the mathematical repair requested by that audit.  It requires
`a,b>=0` and `(a,b)!=(0,0)` before invoking candidate recovery, and it adds
an exhaustive symbolic check of true center-index cases, zero centered
residues, round-half-up endpoints, and repeated-root cases.  It does not
broaden the theorem's scope.  The carry identities, `d=2` offset,
divisor-only grammar, P205 support optimum, divisor-window direction, and
additive-selector boundary are unchanged.

No numerical computation, search, script, web source, or remote process was
used.  V1 and `HOSTILE_AUDIT.md` remain unchanged.  No durable ledger,
registry, progress, or promoted-proof file was edited.

## Frozen predecessor hashes

| V1 artifact | SHA-256 |
|---|---|
| `STATEMENT.md` | `a9e57ccf65bcc793bccf844fb74216742acaecabe77d4e34ec9946ffb98015b9` |
| `PROOF.md` | `d8a1df081ee5c8c52a4515c1f0370486a8546a3a4589dce3bd76732fa0a76015` |
| `SELF_AUDIT.md` | `a7ac335219c52fb61f881eddfbc26fde16f2f7bff32fa5cd2a968b46fa8e24c2` |
| `PROVENANCE.md` | `521b31b7e210516311427ada75b6a719997ca76df9c71d9f35a8d990bc097361` |
| `MANIFEST.md` | `99affe0665add866d18b15bf2583cca8cba2a45327645849cce06c96be446caa` |
| `HOSTILE_AUDIT.md` | `4cd1acc3f3fdfe387a9c016c64602baebe81156463bf01ae40726df6f1c9e7be` |

V2 is frozen at self-audited status.  Fresh hostile re-audit and a later
statement-only reconstruction are pending.
