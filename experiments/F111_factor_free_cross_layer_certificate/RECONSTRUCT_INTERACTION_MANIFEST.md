# Complete interaction reconstruction manifest

## Isolation

The only supplied inputs read before reconstruction were:

1. `RECONSTRUCT_INTERACTION_STATEMENT.md`
2. `RECONSTRUCT_INTERACTION_INPUT.json`
3. `RECONSTRUCT_STATEMENT.md`

No other pre-existing F111 file was read. No F98, F109, F110, F115, F116,
or `LAYER_INTERACTION_*` artifact was read. Later verification inspected
only newly written `RECONSTRUCT_INTERACTION_*` artifacts.

## Primary execution

Launcher command:

```text
python3 experiments/F111_factor_free_cross_layer_certificate/RECONSTRUCT_INTERACTION_run_with_timeout_v1.py
```

Recorded child command:

```text
/opt/homebrew/opt/python@3.14/bin/python3.14 -B /Users/zhou/autoresearch/IntegerFactoring/experiments/F111_factor_free_cross_layer_certificate/RECONSTRUCT_INTERACTION_decoder_v1.py --input /Users/zhou/autoresearch/IntegerFactoring/experiments/F111_factor_free_cross_layer_certificate/RECONSTRUCT_INTERACTION_INPUT.json --output /Users/zhou/autoresearch/IntegerFactoring/experiments/F111_factor_free_cross_layer_certificate/RECONSTRUCT_INTERACTION_OUTPUT.json
```

Working directory:

```text
/Users/zhou/autoresearch/IntegerFactoring/experiments/F111_factor_free_cross_layer_certificate
```

Named timeout: `F111_COMPLETE_INTERACTION_HARD_TIMEOUT_V1`.
Hard timeout: 7,200 seconds.
Runner elapsed time: 53.322489 seconds.
Decoder elapsed time: 53.252812209000695 seconds.
Exit code: 0.
Status: PASS.

The decoder ran internal perfect-power, ordered-overlap, and binary-kernel
checks. A separate three-chunk test compared every batched first-overlap
answer with a literal ordered scan for probes 2 through 4,999. It passed.
A separate read-only output check verified every source and normalization
count identity, every matrix nullity, every root-map image size, the quotient
dimension identity, the non-global root congruence and terminal gcds, and
`79043 * 41011 = N`. It passed.

Three non-computational command-formatting errors and their successful
replacements are preserved in `RECONSTRUCT_INTERACTION_FAILED_COMMANDS.md`.
No reconstruction attempt failed.

## File pins

| File | Bytes | SHA-256 | Role |
|---|---:|---|---|
| `RECONSTRUCT_INTERACTION_STATEMENT.md` | 3,860 | `a4c50da4ba3d76d2137115bdd423b5738b35f14d13dc6b1fed1d76c9f54627e6` | permitted interaction specification |
| `RECONSTRUCT_INTERACTION_INPUT.json` | 89 | `5aaf110ebf1cf1530a194463366ca9bdcd7db67dd213a4a49f4186e3f13e49f3` | permitted public input |
| `RECONSTRUCT_STATEMENT.md` | 4,869 | `e1a573feaceb2465d599df21a41b46372c25c6c30cb15ad7d1b6c56230fe0dae` | permitted source specification |
| `RECONSTRUCT_INTERACTION_decoder_v1.py` | 43,109 | `de0997c55ee97348de53dd41e0c999636bec6f61b2e5b49de9cb4193972d1365` | independent factor-free decoder |
| `RECONSTRUCT_INTERACTION_run_with_timeout_v1.py` | 2,656 | `fa700aac90a1dbdc747c34aecd555b3f034f31eff2d23448f43c21068bc47599` | named hard-timeout runner |
| `RECONSTRUCT_INTERACTION_RUN_V1.log` | 7,000 | `de12e4847090017f96b20b2f481e013f4a665532f8e6e0e314b96a8c81e047a0` | complete successful log |
| `RECONSTRUCT_INTERACTION_OUTPUT.json` | 54,627 | `e010c1598d712da38e6b1a5fb0f79646d78f90f1218bc6ed3e833dd9a6fdcd48` | machine-readable exact result |
| `RECONSTRUCT_INTERACTION_FAILED_COMMANDS.md` | 1,029 | `7cb382004342d5ba6ff63d5043962032778ecc1bfcb140ac36c4317d4e1c2584` | preserved read-only command errors |
| `RECONSTRUCT_INTERACTION_REPORT.md` | 8,019 | `820ef26300e9de99fdce93dd551665621f460d81b79e49f17b6b39a482ce7f35` | human-readable result |

This manifest is not self-hashed. Every supplied input, computation source,
log, output, error record, and report that it indexes is pinned above.

## Internal bounded-encoding pins

Large integers use an 8-byte length followed by the minimal unsigned
big-endian payload. Sequences end with an 8-byte count. Matrix rows and
vectors use fixed-width little-endian bitsets followed by width and count.
No pin depends on unbounded decimal conversion.

| Object | SHA-256 |
|---|---|
| full retained-record sequence | `482ad162109e6dc4bde270cfd6cff49bb646372ef2aab285d62055e81a59976b` |
| union distinct exact values | `1ad4fca9e74943bacedd5462b7417dca60845df6427d92f708c567632317c471` |
| union gcd-basis blocks | `3b30326818a526001c8929ffd0893fd77026b6c2e90f878896d64d9a977a2b11` |
| frozen rows | `24b4427792077dfca80fd373d44a654a452c4c37761b66d28060f0bf19b9df36` |
| frozen kernel | `e04409f930dcb920d6844bce221ae6da4365d7ad0f658700985ad8bd5dd0e04b` |
| appended standalone rows | `0565196228b637cdc6fc14fdb900ff27cc5cc838f8de2fb10800f8b3b8bff808` |
| newly appended union rows | `4139c7f26537abd4e8fb225331af5f728c602f73f3a2f43737ac75af4ffccd76` |
| union rows | `8cf552b8b7cee891270b668d8ab6cf3228d978cbf05eadc80deedc5d248be8ad` |
| union kernel | `2c5bb13b2269957a6a6f4ea83f8afd795b6cda588c269515bf7d07c535fd28fa` |
| quotient basis | `51437e9cbf955dfaa3c3baf45dc6867bd2608186c113a5eed551f678fb2ca068` |
| non-global product | `6f7784a31401b7a43c03188668fd0c3bd4dedb201351e6e867595dfd51d68c07` |
| non-global positive root | `a6acf32e3d6eb81f39592a76a7387b902695263764780f14f244acad34c8d490` |
