# F140-D01 second authoritative-run failure

The unrestricted run completed the finite search but stopped while encoding
`OUTPUT.json`.  Sage had converted the fixed constants in the `.sage` source
to Sage integers, which Python's standard JSON encoder does not accept.  The
mathematical search criteria ran unchanged, but no result file survived.

```text
TypeError: Object of type Integer is not JSON serializable
when serializing list item 0
when serializing dict item 'C_values'
when serializing dict item 'parameters'
```

The corrected source converts all configuration constants and recorded
scores to Python integers before JSON serialization.  This correction does
not change the corpus, graph, path predicate, score, or search cap.
