# F120 fresh hostile-audit manifest

## Verdict and boundary

The fresh hostile audit verdict is `PASS`.

The audit accepts the degree theorem and the finite exact-value `REUSE`
falsifier. It does not accept an infinite trial-hard semiprime family, a
`CLOSE` theorem, a `ROOT` theorem, a complete-source failure, or a barrier to
representation-level feedback.

No new search, source enumeration, primality run, or external lookup was
performed. The registered candidate computation and the existing independent
verifier were read and checked as preserved evidence.

## Exact-product collision result

Different inverse orbits can share one exact product. This does not break the
degree theorem after exact-value deduplication. Choose one orbit for each
distinct product. Orbits chosen for different products cannot share an
endpoint because the inverse of an endpoint modulo `N` is unique.

The theorem must not be transferred to a raw residue matrix or to named
integer representations. Those are outside the accepted scope.

## SHA-256 pins

Each hash is over the exact file bytes. This manifest has no self-hash.

| Role | File | SHA-256 |
|:---|:---|:---|
| Preregistered question | `QUESTION.md` | `d11a55ce9dc747af2c43935fd352f083d483fd478400512bf7e9c01328064ad6` |
| Candidate result | `RESULT.md` | `a8a63cc9a2bfab6acea2ded42e851fe3d6a185e15f9962bbe802a0ecb1866445` |
| Candidate failed routes | `FAILED_ROUTES.md` | `a87f6076ff69a9bc1c95976cc95849cd9971d5334a00830adaba3b4ccba20c47` |
| Candidate manifest | `MANIFEST.md` | `de8107968f6edfa30bd07d7909c0bbe4b7840199bc669113e993d4f6b1ac1f78` |
| Run registration | `REGISTRATION.json` | `4a014f6d0704d1ba083e53c2e44858838b10938cad0a9d90869cc16e629f09d1` |
| Search source | `find_semiprime_private_row.py` | `04f5abd4140a885f2d3e22f38a597e88e95063aee1479a40d01e9d0c0c178e94` |
| Approved retry runner | `run_with_timeout.py` | `fe383ace9cfbdb39a3398bf69375947219b8902454ccfacde229e1819dcb1be2` |
| Authoritative finite output | `OUTPUT.json` | `bc84fec9d4b8ab17d4a84c5b9a64b753c0625023f7b963e805f4828ee4d361f9` |
| Authoritative finite log | `RUN.log` | `52170ca6a746993fab8a0e03d7c6529d76e8e1527c96948d32f036c992413c5f` |
| Failed-run record | `FAILED_RUNS.md` | `11aae8f244c3ca7256a6b3b73f914ac4b442e5ddafd6523d7c3857a8c66399c4` |
| Failed output | `OUTPUT_FAILED_20260808T054832Z_EXIT_1.json` | `278b311e583cf2e96331aa53dc9037db7f6bcaebb19b41116393caca2275bd48` |
| Failed log | `RUN_FAILED_20260808T054832Z_EXIT_1.log` | `0a6aeb91b2adc447c20743029a62dcb2b85bc1efd3227f28be533853334c61a7` |
| Existing audit registration | `HOSTILE_AUDIT_REGISTRATION.json` | `5ba0d81cb4db4058652f866a91883ea0db6dd5d904911bf31ca5fa7dd19e9bea` |
| Existing independent verifier | `hostile_audit_verify.py` | `00bb4ec2fa001525bbdbf1fdaf5f26279b132c9095190cf224454b432a3402a5` |
| Existing audit runner | `hostile_audit_run_with_timeout.py` | `827378403d472f1e05cbc031dafdba29bffa44c83e691239815f09f30c499eeb` |
| Existing audit output | `HOSTILE_AUDIT_OUTPUT.json` | `af31b41e1a1a525f4308533b61ff6e2aac8a18e4bf97c19730c2e98689ce2e35` |
| Existing audit log | `HOSTILE_AUDIT_RUN.log` | `6714533ffaff5012b42c813a6f993b2c29f58a24c6808d508f464d100fddfb05` |
| Reconstruction statement | `RECONSTRUCT_STATEMENT.md` | `e5607787405ff4c8f70df4d6f2ce835180278f0bde47df815875eff85207174a` |
| Fresh hostile report | `HOSTILE_AUDIT_REPORT.md` | `862f30200ccef7491e16bd366b69dea67f1e438caeb5b7b8698edd47d91f338a` |
| Fresh rejected routes | `HOSTILE_AUDIT_FAILED_ROUTES.md` | `523db2a04c1754bd5d73d9fec879f89fe47f624f25d56e10387763810bce9505` |
