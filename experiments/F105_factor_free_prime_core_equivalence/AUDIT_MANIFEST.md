# F105 audit manifest

## First-audit candidate inputs

```text
b9b5da6a2c3d564b1df4470af7da31bfe5e9b86366a675104f70cb574f25a28e  DESIGN.md
441e01613248906462f223bfe7e2f2bd62ce7e96edc6e25cdc99192e6b2eafa2  RESULT.md
```

## Corrected candidate inputs

```text
b9b5da6a2c3d564b1df4470af7da31bfe5e9b86366a675104f70cb574f25a28e  DESIGN.md
ffcc2334acb34619ea2308ec9c544fbb1d0ecce4c696f9ce01c3caf9bbb53f45  RESULT.md
```

The corrected result was read in full for the final narrow re-audit. It was
not edited by the auditor.

## Authoritative audit artifacts

```text
ea2c6e7e81f7088abea2a4e9e7e1fc118fb164c1b88dd4b8e0b79ba1bb694ce3  AUDIT.md
0d2026cb2dfa763720599830ba11285d108c43e54e477a1616d6a350c90ba9e8  AUDIT_VERIFY.py
49a8165a3d74944c788b2c5d10cabeecbc589353858f077c30fa82ed83501976  AUDIT_RUNNER.py
6d0b128946f9ffd0bf253e5c03555b6ee4415d95f6739fbfd114ee428caa5b4a  AUDIT_OUTPUT.json
f85e88578324bd6197ca3214fd09dc658e4bfd394f91cd1d2e4d19958f9dde8d  AUDIT_RUN.log
```

## Final narrow re-audit

```text
69868b43e9e10bf1fad7f981ad06406db0a635b6d919c986ffd44032a2193430  FINAL_REAUDIT.md
```

The unchanged verifier was run again only after confirming that the
correction narrows the move rule and clarifies zero-row representation without
expanding the theorem. The fresh direct run exited zero and reported `PASS`.
The authoritative named timeout output and log above remain the pinned
exhaustive evidence.

The authoritative command was:

```text
python3 experiments/F105_factor_free_prime_core_equivalence/AUDIT_RUNNER.py
```

The runner used Python 3.14.5, a 120-second hard timeout, and exited zero. The
logged verifier runtime was 1.6735332079988439 seconds.

## Preserved failed attempt

```text
6de874c8ac8e7ada34d4ace13d9dcf9007c96ada010a40f069057739a4ba8f83  AUDIT_FAILED_20260808T014949Z.log
```

This first attempt failed in the audit verifier. Its gcd-one branch copied
both unchanged entries twice. The failure does not support or refute the
candidate. The corrected verifier source predates the authoritative output
and log.
