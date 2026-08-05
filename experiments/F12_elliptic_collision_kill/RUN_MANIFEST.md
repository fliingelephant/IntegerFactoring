# F12 elliptic collision kill manifest

**Approach-family ID:** `F12_elliptic_collision_kill`.

Every computation used a named source file, an explicit hard timeout, and a
retained log.  Successful JSON certificates and partial outputs from failed
serialization runs were retained.  No inline interpreter computation was
used.

## Run summary

| Run | Status | Result | Log | Output |
| --- | --- | --- | --- | --- |
| R01 | exit 0 | Found the good curve/CRT point at search length 102; 0.15786575 s internal | `logs/R01_clean_synchronized.log` | `output/R01_clean_synchronized.json` |
| R02 | exit 1 | Exhaustive torus run reached probability construction, then failed because `Fraction` received Sage integers | `logs/R02_torus_reduction.log` | none |
| R03 | exit 1 | Mathematical assertions completed, then JSON serialization failed on a Sage integer | `logs/R03_torus_reduction.log` | `output/R03_torus_reduction.json` (partial, invalid JSON) |
| R04 | exit 0 | Torus identity and exhaustive probability certificate; 1.012120125 s internal | `logs/R04_torus_reduction.log` | `output/R04_torus_reduction.json` |
| R05 | exit 1 | Division check exposed that the support assertion incorrectly counted the constant \(\psi_1=1\) as a nontrivial index | `logs/R05_division_identity.log` | none |
| R06 | exit 0 | 45 division-identity checks and both local collected products; 0.021390458 s internal | `logs/R06_division_identity.log` | `output/R06_division_identity.json` |
| R07 | exit 0 | Repeated-prime, exponent-scan, and perfect-power checks; 0.077078208 s internal | `logs/R07_torus_prime_powers.log` | `output/R07_torus_prime_powers.json` |
| R08 | exit 1 | All floor-witness assertions completed, then JSON serialization failed on a Sage integer | `logs/R08_floor_clean_witness.log` | `output/R08_floor_clean_witness.json` (partial, invalid JSON) |
| R09 | exit 0 | Rechecked the clean witness at \(m=\lfloor\sqrt N\rfloor=101\); 0.020160708 s internal | `logs/R09_floor_clean_witness.log` | `output/R09_floor_clean_witness.json` |
| R10 | exit 0 | Cross-certificate audit passed | `logs/R10_audit.log` | `output/R10_audit.json` |

The failed runs are evidence-bearing and were not deleted or overwritten.
R03 and R08 opened their destination files before serialization failed, so
their partial JSON is intentionally retained and is not used by the audit.

## Exact timeout commands

R01:

```sh
DOT_SAGE=/tmp/f12_elliptic_collision_sage timeout 120 sage experiments/F12_elliptic_collision_kill/search_clean_synchronized.sage --coefficient-limit 40 --output experiments/F12_elliptic_collision_kill/output/R01_clean_synchronized.json > experiments/F12_elliptic_collision_kill/logs/R01_clean_synchronized.log 2>&1
```

R02:

```sh
DOT_SAGE=/tmp/f12_elliptic_collision_sage timeout 120 sage experiments/F12_elliptic_collision_kill/verify_torus_reduction.sage --output experiments/F12_elliptic_collision_kill/output/R02_torus_reduction.json > experiments/F12_elliptic_collision_kill/logs/R02_torus_reduction.log 2>&1
```

R03:

```sh
DOT_SAGE=/tmp/f12_elliptic_collision_sage timeout 120 sage experiments/F12_elliptic_collision_kill/verify_torus_reduction.sage --output experiments/F12_elliptic_collision_kill/output/R03_torus_reduction.json > experiments/F12_elliptic_collision_kill/logs/R03_torus_reduction.log 2>&1
```

R04:

```sh
DOT_SAGE=/tmp/f12_elliptic_collision_sage timeout 120 sage experiments/F12_elliptic_collision_kill/verify_torus_reduction.sage --output experiments/F12_elliptic_collision_kill/output/R04_torus_reduction.json > experiments/F12_elliptic_collision_kill/logs/R04_torus_reduction.log 2>&1
```

R05:

```sh
DOT_SAGE=/tmp/f12_elliptic_collision_sage timeout 120 sage experiments/F12_elliptic_collision_kill/verify_division_identity.sage --witness experiments/F12_elliptic_collision_kill/output/R01_clean_synchronized.json --output experiments/F12_elliptic_collision_kill/output/R05_division_identity.json > experiments/F12_elliptic_collision_kill/logs/R05_division_identity.log 2>&1
```

R06:

```sh
DOT_SAGE=/tmp/f12_elliptic_collision_sage timeout 120 sage experiments/F12_elliptic_collision_kill/verify_division_identity.sage --witness experiments/F12_elliptic_collision_kill/output/R01_clean_synchronized.json --output experiments/F12_elliptic_collision_kill/output/R06_division_identity.json > experiments/F12_elliptic_collision_kill/logs/R06_division_identity.log 2>&1
```

R07:

```sh
DOT_SAGE=/tmp/f12_elliptic_collision_sage timeout 120 sage experiments/F12_elliptic_collision_kill/verify_torus_prime_powers.sage --output experiments/F12_elliptic_collision_kill/output/R07_torus_prime_powers.json > experiments/F12_elliptic_collision_kill/logs/R07_torus_prime_powers.log 2>&1
```

R08:

```sh
DOT_SAGE=/tmp/f12_elliptic_collision_sage timeout 120 sage experiments/F12_elliptic_collision_kill/verify_floor_clean_witness.sage --witness experiments/F12_elliptic_collision_kill/output/R01_clean_synchronized.json --output experiments/F12_elliptic_collision_kill/output/R08_floor_clean_witness.json > experiments/F12_elliptic_collision_kill/logs/R08_floor_clean_witness.log 2>&1
```

R09:

```sh
DOT_SAGE=/tmp/f12_elliptic_collision_sage timeout 120 sage experiments/F12_elliptic_collision_kill/verify_floor_clean_witness.sage --witness experiments/F12_elliptic_collision_kill/output/R01_clean_synchronized.json --output experiments/F12_elliptic_collision_kill/output/R09_floor_clean_witness.json > experiments/F12_elliptic_collision_kill/logs/R09_floor_clean_witness.log 2>&1
```

R10:

```sh
timeout 60 python3 experiments/F12_elliptic_collision_kill/audit_certificates.py --elliptic experiments/F12_elliptic_collision_kill/output/R01_clean_synchronized.json --torus experiments/F12_elliptic_collision_kill/output/R04_torus_reduction.json --division experiments/F12_elliptic_collision_kill/output/R06_division_identity.json --prime-powers experiments/F12_elliptic_collision_kill/output/R07_torus_prime_powers.json --floor-witness experiments/F12_elliptic_collision_kill/output/R09_floor_clean_witness.json --output experiments/F12_elliptic_collision_kill/output/R10_audit.json > experiments/F12_elliptic_collision_kill/logs/R10_audit.log 2>&1
```

## Successful source hashes

| Source | SHA-256 |
| --- | --- |
| `search_clean_synchronized.sage` | `4b98339369bdb79e33d545a3e1fce54c8e19f252ecf136269722b24864a0d92e` |
| `verify_torus_reduction.sage` | `cb6b20adc412ed97f4c70f8c7942f6ad6e3ed552968959fca093d2f8c3f7a511` |
| `verify_division_identity.sage` | `cdd4196510c10936248a96223321be35a94ea25c2235dbb83815522ac54dd8a0` |
| `verify_torus_prime_powers.sage` | `6f4022faebe13be37ea67212dfecf18fbb0bc452ed9a60865ae79547f7c0bae4` |
| `verify_floor_clean_witness.sage` | `a933956d18248c6ffe5d0f49c0a765eb4495a5b7b2476639bba56b6b2b074334` |
| `audit_certificates.py` | `5c75400520647f7d9f92d1d6b5745c0560006743c98d97353973a5ca38f292c6` |

R10 rechecked these embedded source hashes and records SHA-256 values for all
five successful mathematical certificates in `output/R10_audit.json`.

