# F100 final text-only re-audit

## Verdict: **PASS**

Both defects from `REAUDIT.md` are fixed. No arithmetic artifact changed, so
no arithmetic rerun was required.

## 1. Matrix label: PASS

The main theorem paragraph in `RESULT.md` now says:

> Their prime-valuation parity matrix has rank 165 and nullity one.

This matches the computed 230-row matrix, which explicitly includes the row
for prime 2. The old phrase "odd-prime valuation matrix" is absent.

The corrected result hash is:

```text
b22c749489acb53338b6feed4cbec333b4cfdc92fba01e0a2544006526e768f5  RESULT.md
```

## 2. Manifest runtime and result pin: PASS

`RUN_MANIFEST.md` now reports:

```text
elapsed_seconds=1.998962
```

This exactly matches `RUN.log`. The manifest also pins the corrected result
hash shown above.

The final manifest hash is:

```text
130b1ea7b6bf2616cadb35121969c03bd6a562245b7348f055c86ab9747d02e6  RUN_MANIFEST.md
```

## 3. Frozen evidence chain: PASS

All prior corrected arithmetic artifacts retain their audited hashes:

```text
3cca68e44691bd7e16488ba1073de471bf7dc8bae6ee1d62f87cb41a75b41c48  DESIGN.md
d997608bca403b9ce9a8a1e10298317fd483fb5d63cf7b546195d8117871ed2f  analyze_dependency.sage
88c429719d757cf812719b43630ab7924f333bf1c1c8824a427de3832a9ff817  run_with_timeout.py
9bcf6217f412f837fab8e3d0b832e01c80fbd5afa1d173156ec93df95bd94076  OUTPUT.json
753dfeaa57cd985a047f7d8a6d5dbccc9da3e838132b9251202f70deada10200  RUN.log
6eba6f30220e6a56ff1bd7f4129092c828303bf257259d239159d61ed7720b4a  FAILED_RUNS.md
```

The prior failed audits also remain unchanged:

```text
50bd1b5ac7bce7fbcd153bf6cef80bdcd783d0e65b4341eef48f92e112524ee8  AUDIT.md
8a4ad4d0e31a5697b830289e99128947031fecbbe4c9941bb949dcfdfbab792b  REAUDIT.md
```

The successful corrected-output verifier artifacts remain unchanged:

```text
522e14ee992d76b20298407edc876df353d00384817a2f37850c04f22c408e3c  reaudit_dependency_verifier.sage
a72eb92e65d0a55eb7be58866c42256e958ee6b09076163c860f6d90004c0555  REAUDIT_VERIFY_OUTPUT.json
0ba288f481c98d2c45e5ec2f7fabb9ea6bd4f39491f824591e7a674e3cb695d0  REAUDIT_VERIFY_RUN.log
```

## Final decision

**PASS.** The final F100 candidate is coherent and frozen. Its exact scope
remains one factor-assisted finite diagnosis of the selected 166-value F98
certificate. It does not establish an all-input law or a polynomial-time
factoring algorithm.
