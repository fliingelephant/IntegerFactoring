# F226-D02 preregistration — infrastructure-only retry

F226-D01 stopped during Sage import.  Sage tried to write its lazy-import
cache under `/Users/zhou/.sage`, which is outside the workspace sandbox.  No
cohort row or mathematical output was produced.

D02 keeps the D01 cohort and calculations unchanged.  The runner now gives
Sage a fresh cache directory under `/private/tmp`.  The source takes the
output filename from the fixed environment value `D02_OUTPUT.json`.  This is
the only source-level change.  D02 keeps the same 300-second time cap and the
same resource limits stated in D01.

