# F284 failed and superseded runs

All runs used the same supplied mathematics and the same test domain. The first
three failures were routine Sage/Python integration errors. Their logs and
status files are retained. The source was repaired in place, so the historical
source bytes are identified by hashes but are not separately snapshotted.

| Run | Duration | Disposition |
| --- | ---: | --- |
| D01 | 4.915608000 s | Failed before the jet tests: Sage rejected the two-argument `QQ(n,d)` coercion. Source SHA-256 before repair: `5e0957bc14ef25b7a033533e6950fcc13cde527a7444b1edf543bf8eeb65d3d8`. |
| D02 | 2.279764041 s | All mathematical assertions completed, then JSON serialization rejected a Sage `Integer` in the literal-case counter. Source SHA-256 before repair: `514790c37213cc752f454de8dfbb0ed27e80f7588a385aabfdc3c27e2d6308f0`. |
| D03 | 2.280032833 s | All mathematical assertions completed, then JSON serialization rejected the Sage zero returned for an odd log coefficient's numerator bit length. Source SHA-256 before repair: `1ea461f54e0cc90e786d81135832efc171a7c23230db4385738bc3cf3924045e`. |
| D04 | 2.744000541 s | Passed all mathematical checks. Superseded because the environment field rendered the Sage version function instead of calling it. The mathematical payload matches D05 exactly after deleting environment and timing metadata. |

No run timed out. D05 is the authoritative run.
