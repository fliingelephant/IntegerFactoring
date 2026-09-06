# F138 nonzero-arm registered revision 1

## Trigger

Registered run 1 finished all arithmetic but failed while serializing the
report. Sage changed the literal `5` in the `carry` field into a Sage
`Integer`, which is not accepted by Python's default JSON encoder.

## Pinned correction

Change only

```text
"carry": 5
```

to

```text
"carry": int(5)
```

The fixed integers, primality checks, source parameters, anchored relation,
privacy checks, and all Boolean falsifiers remain unchanged.

Failed verifier SHA-256:
`b945dce61bda8434afd87b8b9c3e283de469c1cd127a9f75886ef21f4621fdfc`.

