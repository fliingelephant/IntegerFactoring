# F226-D03 preregistration — integer bit-length repair

F226-D02 passed Sage initialization but stopped before the first cohort row.
The source converted `N` to a Python integer and then called Sage's `nbits`
method on it.  D03 changes that expression to Python's exact
`N.bit_length()`.  The cohort, mathematical calculations, resource limits,
and all other source lines remain unchanged.  Output is `D03_OUTPUT.json`
and the log is `logs/F226-D03.log`.

