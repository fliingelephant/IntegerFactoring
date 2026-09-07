# Exact bulk spectrum of the unshifted transport modulo 16

**Family:** route:F31

**Status:** exact enumerative discovery for six finite moduli, with complete
small controls and bounded direct checks. No polynomial-bit evaluator,
degree theorem, lower bound, or factoring claim is made.

## Exact convolution construction

Let \(M=2^k\), \(R=M/4\), and write every odd residue uniquely as
\(w=(-1)^\epsilon5^j\), with \(0\leq j<R\). For canonical
\(u=w^{-1}\bmod M\), put
\[
 q(w)=\frac{uw-1}{M},\qquad \mu(w)=u q(w).
\]
The program constructs
\[
 b(w)=w,\qquad a(w)=\mu(w^{-1})\bmod16=wq(w)\bmod16
\]
on the two sign components. Four exact integer-polynomial products, folded
modulo \(X^R-1\), give
\[
\begin{aligned}
 C_+&=a_+*b_+ + a_-*b_-,\\
 C_-&=a_+*b_- + a_-*b_+.
\end{aligned}
\]
Thus \(C_r=\sum_w(\mu(w)\bmod16)(rw\bmod M)\) for every odd \(r\).
With the exact integer
\[
 A_\mu=\sum_w(\mu(w)\bmod16)w,
\]
the numerator
\[
 (8M+r)A_\mu-C_r
\]
is divisible by \(M\), and its quotient modulo 16 is
\(T(8M+r)\bmod16\). The full input \(N=8M+r\) keeps \(M\) as the public
largest power of two at most \(N/8\). The program separately constructs
the canonical quotient for \(r\) and checks the exact correction
\[
 T(8M+r)-T(r)=8A_\mu\pmod {16}.
\]
All polynomial coefficients and folds are exact integers. No floating-point
transform or rounding is used.

## Validation

Every odd residue was checked by direct summation for \(M\leq128\). At each
larger modulus, direct \(O(M)\) summation checked residues 1, 3, 5, 7 and
four seeded residues. Both canonical \(r\) and full \(8M+r\) arguments were
evaluated directly. The bulk table also checked exact divisibility and the
raw/canonical relation for every odd residue.

| k | Directly checked residues beyond 1,3,5,7 | Division failures | Raw/canonical failures | First-bit sign failures |
|---:|---|---:|---:|---:|
| 8 | 17, 225, 211, 55 | 0 | 0 | 0 |
| 10 | 465, 761, 411, 643 | 0 | 0 | 0 |
| 12 | 2509, 2931, 2027, 2957 | 0 | 0 | 0 |
| 14 | 14491, 12317, 13947, 9425 | 0 | 0 | 0 |
| 16 | 3635, 64023, 32165, 32175 | 0 | 0 | 0 |
| 18 | 158641, 211435, 114617, 150833 | 0 | 0 | 0 |

The sign control
\[
 t_0(-r)=t_0(-1)+t_0(r)\quad\text{in }\mathbb F_2
\]
held for every odd residue at all six reported moduli. Here \(t_0\) is bit
zero of \(T(8M+r)/2\bmod8\). No validation anomaly occurred.

## Algebraic normal forms

For every modulus the three bit tables of \(T(8M+r)/2\bmod8\) were put in
two orders:

* ordinary order \(x=(r-1)/2\), using the \(k-1\) bits of \(x\);
* sign/log order \(\epsilon+2j\), so variable zero is \(\epsilon\).

In the tables below, a cell records the ANF degree, total monomial count,
and the exact nonzero counts `degree:count`.

| k | bit | ordinary coordinate | sign/log coordinate |
|---:|---:|---|---|
| 8 | 0 | deg 5; total 51; [1:4,2:11,3:16,4:14,5:6] | deg 5; total 29; [1:3,2:3,3:10,4:9,5:4] |
| 8 | 1 | deg 6; total 68; [1:3,2:14,3:15,4:18,5:11,6:7] | deg 6; total 35; [1:4,2:7,3:10,4:11,5:2,6:1] |
| 8 | 2 | deg 7; total 56; [1:2,2:9,3:17,4:18,5:7,6:2,7:1] | deg 7; total 69; [1:4,2:10,3:18,4:20,5:13,6:3,7:1] |
| 10 | 0 | deg 7; total 233; [1:5,2:21,3:39,4:66,5:51,6:43,7:8] | deg 7; total 117; [1:2,2:13,3:23,4:30,5:26,6:17,7:6] |
| 10 | 1 | deg 8; total 260; [1:3,2:19,3:53,4:64,5:59,6:37,7:16,8:9] | deg 8; total 133; [1:6,2:18,3:25,4:37,5:27,6:15,7:4,8:1] |
| 10 | 2 | deg 9; total 262; [1:6,2:18,3:44,4:63,5:63,6:40,7:23,8:4,9:1] | deg 9; total 262; [1:4,2:22,3:39,4:64,5:62,6:45,7:20,8:5,9:1] |
| 12 | 0 | deg 9; total 951; [1:5,2:22,3:85,4:155,5:225,6:233,7:140,8:76,9:10] | deg 9; total 469; [1:6,2:14,3:51,4:103,5:112,6:96,7:54,8:27,9:6] |
| 12 | 1 | deg 9; total 1030; [1:7,2:25,3:91,4:163,5:233,6:231,7:164,8:88,9:28] | deg 9; total 517; [1:4,2:23,3:64,4:105,5:127,6:112,7:57,8:21,9:4] |
| 12 | 2 | deg 10; total 984; [1:7,2:28,3:64,4:161,5:233,6:215,7:163,8:81,9:25,10:7] | deg 10; total 1006; [1:4,2:19,3:78,4:172,5:218,6:230,7:180,8:74,9:26,10:5] |
| 14 | 0 | deg 11; total 4037; [1:6,2:31,3:121,4:339,5:676,6:854,7:848,8:684,9:335,10:131,11:12] | deg 11; total 1947; [1:4,2:32,3:91,4:235,5:382,6:449,7:376,8:234,9:102,10:35,11:7] |
| 14 | 1 | deg 12; total 4132; [1:6,2:41,3:153,4:342,5:665,6:848,7:856,8:665,9:366,10:141,11:36,12:13] | deg 12; total 2010; [1:4,2:32,3:112,4:234,5:393,6:455,7:393,8:247,9:106,10:25,11:8,12:1] |
| 14 | 2 | deg 13; total 4076; [1:7,2:39,3:139,4:352,5:633,6:875,7:850,8:616,9:364,10:148,11:45,12:7,13:1] | deg 13; total 4033; [1:8,2:39,3:136,4:351,5:640,6:830,7:867,8:639,9:349,10:136,11:29,12:8,13:1] |
| 16 | 0 | deg 13; total 16225; [1:6,2:46,3:183,4:666,5:1473,6:2415,7:3250,8:3192,9:2548,10:1564,11:646,12:222,13:14] | deg 13; total 8009; [1:6,2:38,3:160,4:482,5:964,6:1476,7:1665,8:1515,9:970,10:503,11:171,12:50,13:9] |
| 16 | 1 | deg 14; total 16472; [1:5,2:47,3:234,4:669,5:1522,6:2567,7:3219,8:3209,9:2549,10:1486,11:675,12:224,13:51,14:15] | deg 14; total 8134; [1:1,2:45,3:176,4:506,5:999,6:1495,7:1673,8:1533,9:971,10:497,11:187,12:46,13:4,14:1] |
| 16 | 2 | deg 15; total 16314; [1:11,2:50,3:228,4:702,5:1518,6:2513,7:3175,8:3202,9:2461,10:1501,11:662,12:227,13:54,14:9,15:1] | deg 15; total 16322; [1:8,2:49,3:232,4:665,5:1522,6:2518,7:3210,8:3142,9:2533,10:1468,11:681,12:236,13:53,14:4,15:1] |
| 18 | 0 | deg 15; total 65081; [1:7,2:62,3:295,4:1135,5:2942,6:6141,7:9733,8:12038,9:12192,10:9629,11:6289,12:3134,13:1131,14:337,15:16] | deg 15; total 32685; [1:5,2:43,3:261,4:863,5:2040,6:4047,7:5791,8:6430,9:5780,10:3970,11:2170,12:942,13:266,14:68,15:9] |
| 18 | 1 | deg 15; total 65838; [1:5,2:70,3:337,4:1218,5:3027,6:6269,7:9807,8:12205,9:12201,10:9753,11:6251,12:3111,13:1171,14:343,15:70] | deg 15; total 32696; [1:7,2:55,3:273,4:914,5:2127,6:4021,7:5732,8:6403,9:5785,10:3977,11:2186,12:874,13:273,14:58,15:11] |
| 18 | 2 | deg 16; total 65462; [1:11,2:57,3:327,4:1190,5:3122,6:6192,7:9697,8:12189,9:12304,10:9599,11:6051,12:3124,13:1177,14:353,15:59,16:10] | deg 16; total 65620; [1:9,2:58,3:330,4:1181,5:3131,6:6151,7:9735,8:12114,9:12266,10:9823,11:6164,12:3084,13:1161,14:336,15:66,16:11] |

The same ANF computation was restricted to \(\epsilon=0\), first at even
exponents \(j=2t\), which are squares, and then at odd exponents
\(j=2t+1\).

| k | bit | even j, square exponents | odd j, nonsquare exponents |
|---:|---:|---|---|
| 8 | 0 | deg 5; total 9; [1:1,3:5,4:2,5:1] | deg 5; total 16; [0:1,1:2,2:5,3:2,4:5,5:1] |
| 8 | 1 | deg 4; total 17; [1:4,2:3,3:7,4:3] | deg 5; total 11; [1:2,2:2,3:3,4:3,5:1] |
| 8 | 2 | deg 4; total 16; [1:3,2:3,3:5,4:5] | deg 5; total 20; [0:1,1:2,2:5,3:8,4:3,5:1] |
| 10 | 0 | deg 7; total 53; [1:1,2:10,3:17,4:9,5:12,6:3,7:1] | deg 7; total 62; [1:4,2:10,3:18,4:15,5:8,6:6,7:1] |
| 10 | 1 | deg 6; total 68; [1:6,2:13,3:14,4:20,5:10,6:5] | deg 7; total 59; [1:3,2:12,3:17,4:15,5:8,6:3,7:1] |
| 10 | 2 | deg 6; total 71; [1:4,2:13,3:17,4:22,5:10,6:5] | deg 7; total 71; [1:3,2:17,3:20,4:17,5:11,6:2,7:1] |
| 12 | 0 | deg 9; total 219; [1:4,2:10,3:32,4:58,5:59,6:34,7:17,8:4,9:1] | deg 9; total 250; [0:1,1:6,2:17,3:43,4:65,5:61,6:33,7:16,8:7,9:1] |
| 12 | 1 | deg 8; total 259; [1:4,2:18,3:46,4:62,5:66,6:45,7:17,8:1] | deg 8; total 265; [1:3,2:22,3:41,4:67,5:61,6:49,7:17,8:5] |
| 12 | 2 | deg 8; total 240; [1:3,2:12,3:41,4:54,5:60,6:47,7:20,8:3] | deg 9; total 261; [0:1,1:6,2:20,3:43,4:63,5:70,6:35,7:16,8:6,9:1] |
| 14 | 0 | deg 11; total 955; [1:3,2:25,3:61,4:157,5:226,6:218,7:159,8:76,9:25,10:4,11:1] | deg 11; total 1030; [1:4,2:23,3:93,4:157,5:245,6:239,7:167,8:69,9:24,10:8,11:1] |
| 14 | 1 | deg 10; total 1008; [1:3,2:25,3:82,4:162,5:211,6:233,7:162,8:91,9:34,10:5] | deg 11; total 1076; [0:1,1:8,2:29,3:78,4:186,5:233,6:234,7:190,8:83,9:26,10:7,11:1] |
| 14 | 2 | deg 10; total 1028; [1:7,2:26,3:72,4:165,5:228,6:235,7:176,8:93,9:21,10:5] | deg 10; total 993; [0:1,1:4,2:24,3:80,4:161,5:228,6:221,7:167,8:76,9:26,10:5] |
| 16 | 0 | deg 13; total 3963; [1:4,2:31,3:121,4:333,5:613,6:846,7:841,8:623,9:362,10:145,11:37,12:6,13:1] | deg 13; total 4156; [0:1,1:7,2:36,3:128,4:342,5:673,6:886,7:883,8:685,9:354,10:119,11:33,12:8,13:1] |
| 16 | 1 | deg 12; total 4076; [1:1,2:41,3:135,4:352,5:639,6:837,7:863,8:669,9:332,10:155,11:43,12:9] | deg 13; total 4118; [1:5,2:36,3:129,4:334,5:655,6:849,7:895,8:654,9:362,10:151,11:38,12:9,13:1] |
| 16 | 2 | deg 12; total 4141; [1:7,2:40,3:149,4:358,5:663,6:879,7:869,8:626,9:351,10:154,11:37,12:8] | deg 12; total 4080; [0:1,1:5,2:38,3:142,4:361,5:625,6:867,7:840,8:661,9:364,10:131,11:42,12:3] |
| 18 | 0 | deg 15; total 16235; [1:4,2:38,3:209,4:631,5:1390,6:2518,7:3247,8:3179,9:2544,10:1470,11:697,12:249,13:50,14:8,15:1] | deg 15; total 16372; [1:9,2:36,3:223,4:673,5:1477,6:2508,7:3214,8:3195,9:2556,10:1527,11:694,12:199,13:50,14:10,15:1] |
| 18 | 1 | deg 15; total 16266; [1:6,2:50,3:221,4:685,5:1471,6:2518,7:3184,8:3192,9:2534,10:1464,11:672,12:215,13:49,14:4,15:1] | deg 15; total 16242; [0:1,1:5,2:58,3:202,4:691,5:1506,6:2502,7:3167,8:3253,9:2461,10:1436,11:681,12:219,13:47,14:12,15:1] |
| 18 | 2 | deg 14; total 16430; [1:8,2:47,3:225,4:679,5:1513,6:2500,7:3203,8:3217,9:2579,10:1504,11:673,12:232,13:42,14:8] | deg 14; total 16328; [0:1,1:6,2:51,3:214,4:685,5:1485,6:2495,7:3168,8:3245,9:2515,10:1506,11:675,12:223,13:51,14:8] |

These are finite exact ranks of ANF support, not degree lower bounds or
asymptotic formulas. The degree of bit one drops from \(k-2\) to \(k-3\)
at the tested \(k=12,18\), in both complete coordinates. This is recorded
as a finite data variation only.

## Packed evidence and resources

Every truth table is stored as a least-significant-bit-first packed bitset
with a SHA-256 hash. ANFs with at most 256 terms store every exact monomial
mask. Denser ANFs store a packed coefficient bitset and hash. No expanded
dense truth-table or monomial list is written.

The pilot \(k=8,10,12\) run took 0.618024 seconds and 257,392,640 bytes peak
RSS. The scale \(k=14,16,18\) run took 1.636694 seconds and 309,329,920
bytes peak RSS. The \(k=18\) modulus itself took 0.340628 seconds. Both runs
used one Sage process, an internal 28-second alarm, an external 30-second
timeout, and a one-GiB RSS watchdog.

Evidence:
`bulk_carry_spectrum.py`, `pilot_output.json`, `pilot_run.log`,
`pilot_status.json`, `scale_output.json`, `scale_run.log`,
`scale_status.json`, `RESOURCE.md`, and `SHA256SUMS.txt`.
