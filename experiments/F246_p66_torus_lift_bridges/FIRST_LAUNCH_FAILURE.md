# F246 first launch failure

The first remote launch stopped before `scan.py` started.

- frozen preregistration SHA-256:
  `e044a235bd6d4dfa1a1b0117a175a5220b8800fff371bdde98d270e7a72d0c19`;
- frozen scan SHA-256:
  `5cfedf8a7314068d19f8adaa92b11fc0e6b351f0e9302daef886ede177041efd`;
- frozen runner SHA-256:
  `cd628724d80099f06380751e78a7349251985efeab13cd8c9c3474df783b0892`;
- attempted command:
  `bash /root/F246_p66_torus_lift_bridges/remote_run.sh <preregistration hash>`;
- exact failure:
  `/root/F246_p66_torus_lift_bridges/remote_run.sh: line 8: python3: command not found`.

No training row, held-out row, or summary file was produced.  A later
read-only check confirmed that `python3` and `python` are absent from `PATH`.
The host has `/root/miniconda3/bin/python`, version 3.12.3, with SHA-256

`0c05a22b0b180580a76437114a95cf138f67c8f46245acad26017c803b42b8c1`.

That interpreter was inspected only with `--version` and `sha256sum`.  It was
not used to execute the scan.  Using it requires an explicit workflow change;
no silent substitution was made.

