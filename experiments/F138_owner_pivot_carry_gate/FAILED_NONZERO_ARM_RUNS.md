# F138 nonzero-arm failed runs

## Registered run 1

The proof checks completed, but JSON serialization failed before an output
file was written. Sage's preparser converted the literal `5` in the reported
`carry` field to a Sage `Integer`. Python's JSON encoder rejected that type.

```text
TypeError: Object of type Integer is not JSON serializable
when serializing dict item 'carry'
when serializing dict item 'certificate'
```

The failure occurred only in output formatting. No check result was emitted,
so this run is not evidence. The frozen failed verifier hash is

```text
b945dce61bda8434afd87b8b9c3e283de469c1cd127a9f75886ef21f4621fdfc
```

