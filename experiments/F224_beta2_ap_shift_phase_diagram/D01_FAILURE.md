# F224-D01 infrastructure failure

The frozen command exited with status 127 before the mathematical binary
ran.  The remote image does not contain `/usr/bin/time`:

```text
remote_run.sh: line 11: /usr/bin/time: No such file or directory
```

- failed log SHA-256:
  `68426631c913c2661499e6d67cdc8fbea908179f089d17855ad1c0340bbb72c6`
- zero-byte output SHA-256:
  `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`

No mathematical row was computed.  No alternate runner was substituted.
