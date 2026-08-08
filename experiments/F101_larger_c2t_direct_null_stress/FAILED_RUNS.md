# Preserved failed runs

## F01 — launcher interpreter absent

The attempted command was

```text
/usr/local/bin/python3 run_single_1m_sage_with_timeout.py
```

from `experiments/F98_multiseed_presentation_closure_kill/`. It failed before
the launcher or mathematical source started:

```text
zsh:1: no such file or directory: /usr/local/bin/python3
```

Exit status was 127. No run log or mathematical output was created. This
failure gives no evidence. No alternate interpreter was substituted.
