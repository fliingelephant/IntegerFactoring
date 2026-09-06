# F226-D06 preregistration — Sage-integer serialization repair

F226-D05 completed every cohort calculation in 6.2 seconds, then failed
while serializing Sage integer counters in the final summary.  Its partial
JSON contains the already serialized failure rows but is not a valid
artifact.  D06 adds `default=int` to the two JSON encoders.  No cohort,
mathematical calculation, or resource limit changes.  Output is
`D06_OUTPUT.json`; log is `logs/F226-D06.log`.

