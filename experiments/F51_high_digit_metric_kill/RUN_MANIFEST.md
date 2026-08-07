# F51 canonical high-digit metric kill manifest

**Approach-family:** F12 exponent-N Teichmüller and principal-digit carriers.

This artifact studies a materially new source-side channel: the statistical
law of nonzero canonical high digits from random public units. It does not use
one scalar equality followed by one gcd.

## Runs

| Run | Source | Timeout | Log | Output | Purpose |
| --- | --- | --- | --- | --- | --- |
| F51-D01 | `scripts/F51_D01_enumerate.py` | 180 s | `logs/F51-D01.log` | `output/F51-D01.json` | Exact finite fibre, collision, gcd-event, and interval-discrepancy scan for h and lambda. |
| F51-D02 | `scripts/F51_D02_local_laws.py` | 180 s | `logs/F51-D02.log` | `output/F51-D02.json` | Verify the exact carry/Fermat-digit formulas and inspect hidden-factor marginal Fourier energy. |
| F51-D03 | `scripts/F51_D03_real_statistics.py` | 180 s | `logs/F51-D03.log` | `output/F51-D03.json` | Check the exact reflection law, normalized moments, and fixed real interval masses. |
| F51-D04 | `scripts/F51_D04_balanced_scan.py` | 180 s | `logs/F51-D04.log` | `output/F51-D04.json` | Adversarial scan of every balanced odd-prime pair with smaller prime at most 101. |
| F51-D05 | `scripts/F51_D05_fourier_scan.py` | 180 s | `logs/F51-D05.log` | `output/F51-D05.json` | Full finite DFT split into gcd-free and hidden-factor frequency classes. |

## Invocation

From the repository root:

```sh
./experiments/F51_high_digit_metric_kill/run_F51_D01.sh
./experiments/F51_high_digit_metric_kill/run_F51_D02.sh
./experiments/F51_high_digit_metric_kill/run_F51_D03.sh
./experiments/F51_high_digit_metric_kill/run_F51_D04.sh
./experiments/F51_high_digit_metric_kill/run_F51_D05.sh
```

Finite output is discovery or certificate evidence only. It proves no
unbounded distribution theorem.

F51-D01 through F51-D04 use only Python's standard library. F51-D05 records
and uses NumPy 2.4.6 for the finite DFT.

## SHA-256

| Run | Source | Wrapper | Output | Log |
| --- | --- | --- | --- | --- |
| F51-D01 | 0251538673176a946e707d9c324b560a9b8414a0a515577e7d59ba6d950e2cdc | 29b6c5f6ef8fd22e359049d06c632c0342048dc01ef890ac074e7ad876e94e50 | 6609560ccc9f5e63314f03a4f39eae63d499bbdc1d94803851b27f6a9e91648c | 396142a1d278cd4f9fd4a4372415aeddee660ee040ec8c2ebef71f2407c2d605 |
| F51-D02 | fd923f8c40dea8fddcde7c304231c8e5635d3ccfb782bbe1559f460f09e9bc32 | 784fbf3de90067fbae76954b2e644537bcb7b335d339f4853e19a95bb8eb5408 | 6cec6da477328b3f70530e394f8dbe3f67607a003e808a85354aeb19caea7a47 | eeb57c7fd578fdd7a490a85a1a5d3e99d3aa055d5b060652b3f2657670c469b7 |
| F51-D03 | 211e0c155eae77fd5befba89d69644db22bd2f07ecd73bb42d16bb42aacb22d0 | 06fd58926a61f9e9234fd7eea6e58b8f32af8dbbdfb15075189d38a333b5a674 | 96a69a52659c247f9c35f5ad908e4ff92a080fb9aa58d2e5808b4b75427cbfc8 | 5322af88174fed8f0f381f02e99f21878cbf54af7d3644afc0060f0c9d08c5af |
| F51-D04 | 4b1fe71c6af85a26a88028bc55a6f1f75931479e710e1a91133045657d8bd5e4 | 3be7f298bc1a7b5481ef0ce029f251395c4b929ef619a6bc1dc27f16a47c2046 | afc427706f51bf6a6b750c70553f4747c4091d83f7c1a8fc2ca466a06d3a01b5 | e66aedcd0a92ef882a4f2fd0b0870af863aad0d06b8d22517e200cbeffe845d9 |
| F51-D05 | 31c7bd02cbfb10f808916ead868bd63ed40eb8fa5167349e0fa0ba901a3148a1 | b52f80ba0879dc9b1794cbddcc183ff9b045fc0618738c483d3b5b467e8da71f | 48c961afbb11c646e052fc15ac7157a1780c86f0ae0f2342e1f67e2d182892bd | df4c2f37a2958b4a067eb43889839aad92f60af96166ca37c96b5801c99a3e34 |
