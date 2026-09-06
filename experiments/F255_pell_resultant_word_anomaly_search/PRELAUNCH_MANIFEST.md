# F255-D01 prelaunch manifest

Frozen before compilation or mathematical execution on the remote host.

| Artifact | SHA-256 |
|---|---|
| `PREREGISTRATION.md` | `6f5c61b09d01b5a17b3a2d54558ac828732d660f4024e826fee70177c14bc67c` |
| `search.cpp` | `b207e826311792aff8e1a74c87e23011a9bbde4e011a0eda43be94ef10548cd2` |
| `remote_run.sh` | `6477c8899881629955d781de39b94ec9780314eb5c0ee3931f1ca81aa0e3cd70` |

The remote image initially lacked Boost headers.  The user explicitly
authorized installing needed dependencies.  `libboost-dev` 1.74 was
installed before compilation.  The run uses eight workers under
`nice -n 15`; this is below the preregistered maximum of 16 workers.

