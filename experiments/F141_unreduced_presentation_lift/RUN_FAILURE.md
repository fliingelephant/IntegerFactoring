# Preserved first-run failure

The first registered command failed during `import sage.all`.  Sage tried to
write its lazy-import cache below `/Users/zhou/.sage`, and the workspace
sandbox denied the write.  No certificate or corpus position ran.

The exact stderr/stdout is preserved in `RUN_FAILED_SANDBOX.log`.  The retry
sets `DOT_SAGE=/private/tmp/f141_sage_state`.  The source, corpus, timeout,
and success criteria are unchanged.
