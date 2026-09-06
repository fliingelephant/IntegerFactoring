# F139 preserved failed runs

## Run 1 — JSON serialization failure

The first preregistered replay completed all arithmetic and then failed while
serializing the report. Sage's preparser converted the literal value of the
`packed_carry` output field to a Sage `Integer`, which Python's JSON encoder
does not serialize by default.

The mathematical checks were not changed. Revision 1 wraps that output-only
field in `int(...)`.

The failed standard-output file is empty because the exception occurred
before `print`:

```text
OUTPUT_FAILED_1.json
SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
```

The terminal error was:

```text
TypeError: Object of type Integer is not JSON serializable
when serializing dict item 'packed_carry'
```

This run is not evidence for the certificate.

## Run 2 — second JSON serialization failure

After revision 1, the replay again completed its arithmetic and failed while
serializing the report. The fixed row labels in `peeling_witness` were also
Sage `Integer` objects. Revision 2 converts each reported row label with
`int(...)`. No mathematical check changed.

The failed standard-output file is again empty:

```text
OUTPUT_FAILED_2.json
SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
```

The terminal error was:

```text
TypeError: Object of type Integer is not JSON serializable
when serializing dict item 'row'
when serializing dict item 'peeling_witness'
```

This run is not evidence for the certificate.
