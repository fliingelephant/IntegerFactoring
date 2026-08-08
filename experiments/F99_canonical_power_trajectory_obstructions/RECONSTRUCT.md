# Proof-blind reconstruction

## Strict verdict

**OVERALL: PASS.**

The orbit-collapse claim, the fixed witness, and the private-row family all
hold. The proof below uses only `RECONSTRUCTION_STATEMENT.md` as mathematical
input. The exact verifier also reports `VERDICT PASS`.

## A. Orbit collapse

Write

\[
N=\frac{a^m-1}{k}.
\]

For every allowed \(r\),

\[
c_rw_r=a^r a^{m-r}=a^m=1+kN. \tag{1}
\]

Thus \(c_rw_r\equiv1\pmod N\). In particular, \(c_r\) is a unit modulo
\(N\), and \(w_r\) is one of its inverses. The assumptions give
\(1\leq w_r<N\). There is exactly one inverse in that interval. Hence
\(w_r\) is the least positive inverse of \(c_r\). Equation (1) also shows
that every exact relation value on this trajectory is the same integer.

Now suppose that \(m\) is odd and that \(a\) is one square-normalized basis
block. The exponent parity of \(a^m\) is \(m\bmod2=1\). Hence every
nonzero binary column is the same one-bit column for \(a\).

Consider a dependency that uses only exact copies of this column. If it
uses \(t\) copies, then \(t\) is even because the common column is nonzero.
The positive square root of the relation product is

\[
Y=\sqrt{(a^m)^t}=(a^m)^{t/2}=(1+kN)^{t/2}\equiv1\pmod N.
\]

Thus its normalized root is \(+1\). This argument depends only on the total
number of copies. It is unchanged if one copy was retained before the
trajectory. With \(s\) exact columns, their restricted matrix has rank one
and kernel dimension \(s-1\), but this whole duplicate subkernel maps to
the single normalized root \(+1\). Raw nullity can therefore grow while
the normalized-root image does not grow.

Finally, (1) gives \(\gcd(a,N)=1\). Every endpoint is a power of \(a\). If
\(a\) is already a prime basis block, its powers contain no smaller
nonunit basis block. Endpoint gcd refinement therefore creates no new
block.

## B. Fixed stable witness

Direct integer arithmetic gives

\[
3^{17}=129{,}140{,}163=1+2(64{,}570{,}081)
\]

and

\[
1871\cdot34511=64{,}570{,}081.
\]

### Primality certificates

I used the following form of Lucas's primality criterion. Suppose the full
prime factorization of \(s-1\) is known. If one integer \(b\) satisfies

\[
b^{s-1}\equiv1\pmod s
\]

and, for every prime \(u\mid s-1\),

\[
\gcd\!\left(b^{(s-1)/u}-1,s\right)=1,
\]

then \(s\) is prime. The table is a recursive certificate. In the last
column, `u:r/g` means that
\(r=b^{(s-1)/u}\bmod s\) and \(g=\gcd(r-1,s)\). Every full-power residue is
one.

| \(s\) | complete factorization of \(s-1\) | \(b\) | checks `u:r/g` |
|---:|:---|---:|:---|
| 2 | base prime | — | — |
| 3 | \(2\) | 2 | `2:2/1` |
| 5 | \(2^2\) | 2 | `2:4/1` |
| 7 | \(2\cdot3\) | 3 | `2:6/1, 3:2/1` |
| 11 | \(2\cdot5\) | 2 | `2:10/1, 5:4/1` |
| 17 | \(2^4\) | 3 | `2:16/1` |
| 29 | \(2^2\cdot7\) | 2 | `2:28/1, 7:16/1` |
| 1871 | \(2\cdot5\cdot11\cdot17\) | 14 | `2:1870/1, 5:932/1, 11:1838/1, 17:81/1` |
| 34511 | \(2\cdot5\cdot7\cdot17\cdot29\) | 7 | `2:34510/1, 5:30233/1, 7:8712/1, 17:26842/1, 29:16242/1` |

The dependency graph in this table ends at \(2\). Lucas's criterion proves
each row in increasing dependency order. In particular, it proves that
both displayed factors of \(N\) are prime.

### Size and order data

The inequalities

\[
2^{25}=33{,}554{,}432<N<67{,}108{,}864=2^{26}
\]

give bitlength \(n=26\). Thus \(n^2=676\), and
\(1871>676\) and \(34511>676\). Both factors exceed the stated trial
bound.

Also,

\[
\begin{aligned}
1870&=2\cdot5\cdot11\cdot17=170\cdot11,\\
34510&=2\cdot5\cdot7\cdot17\cdot29=170\cdot203.
\end{aligned}
\]

Therefore

\[
g=\gcd(1870,34510)=170,
\qquad (A,B)=(11,203).
\]

For the remaining gcd,

\[
AB=2233=7\cdot11\cdot29
\]

and

\[
N-1=64{,}570{,}080=2^5\cdot3\cdot5\cdot17\cdot7913.
\]

The last factor has residues \(3,4,25\) modulo \(7,11,29\), respectively.
Hence \(\gcd(AB,N-1)=1\).

The equality \(3^{17}=1+2N\) gives \(3^{17}\equiv1\) modulo each prime
factor and modulo \(N\). The order in each case divides the prime number
17. It is not one because \(3\not\equiv1\) modulo any of these moduli.
Thus

\[
\operatorname{ord}_{1871}(3)=
\operatorname{ord}_{34511}(3)=
\operatorname{ord}_{N}(3)=17.
\]

It follows that the powers with \(0\leq e\leq676\) visit exactly 17
residues. Their first occurrences are \(3^r\), for \(0\leq r\leq16\),
because

\[
3^{16}=43{,}046{,}721<N.
\]

For \(1\leq r\leq16\), both \(3^r\) and \(3^{17-r}\) are less than
\(N\). Part A applies with \((a,m,k)=(3,17,2)\). The canonical inverse of
\(c=3^r\) is \(w=3^{17-r}\), and every such first presentation has exact
value

\[
cw=3^{17}=1+2N.
\]

The remaining first presentation is the residue one, with value one.

### Endpoint gcds

Fix \(1\leq r\leq16\), and let \(\ell\) be either prime factor of \(N\).
If \(\ell\mid3^r-3^{17-r}\), then the order 17 of 3 modulo \(\ell\)
would divide \(2r-17\). This implies \(17\mid r\), which is impossible.

If \(\ell\mid3^r+3^{17-r}\), then

\[
3^{2r-17}\equiv-1\pmod\ell.
\]

After squaring, 17 would divide \(2(2r-17)\). Since 17 is odd, this again
implies \(17\mid r\), which is impossible. Neither prime factor of \(N\)
divides either endpoint sum or difference. Therefore

\[
\gcd(c-w,N)=\gcd(c+w,N)=1
\]

for every nontrivial residue.

All endpoints are powers of the already prime block 3. Thus this complete
one-seed trajectory supplies duplicate kernel directions whose global root
is \(+1\), but it supplies neither a direct factor nor a block split.

## C. Private-row family

Fix \(T\geq1\). The construction below works for all such \(T\), and hence
for every sufficiently large \(T\). Put

\[
d_e=2^e-1 \qquad (1\leq e\leq T).
\]

### Private primes and the CRT class

For each \(e\), Bertrand's postulate supplies a prime \(q_e\) in the
interval

\[
2^{4T+2e}<q_e<2^{4T+2e+1}. \tag{2}
\]

These intervals are disjoint. Thus the \(q_e\) are distinct. Also,
\(q_e>2^T>d_e\). Let \(x_e\) be the inverse of \(d_e\) modulo \(q_e^2\),
and prescribe

\[
R_T\equiv -x_e+q_e\pmod{q_e^2} \tag{3}
\]

for every \(e\). Also prescribe

\[
R_T\equiv1\pmod{2^T}. \tag{4}
\]

Set

\[
M_T=\prod_{e=1}^T q_e^2,
\qquad
Q_T=2^T M_T.
\]

The moduli in (3) and (4) are pairwise coprime. The Chinese remainder
theorem gives a unique class \(R_T\pmod{Q_T}\). This class is reduced:
it is odd, and (3) is nonzero modulo every \(q_e\). Choose
\(1\leq R_T<Q_T\).

### A distinct odd semiprime in the class

Use Bertrand's postulate once more to choose a prime

\[
2^{2T}<p_T<2^{2T+1}. \tag{5}
\]

It is coprime to \(Q_T\). Let \(a_T\) be the least positive residue of
\(R_Tp_T^{-1}\pmod{Q_T}\). No \(q_e\) is 3, so \(3\nmid Q_T\). At least
one \(k_T\in\{1,2\}\) makes

\[
b_T=a_T+k_TQ_T
\]

not divisible by 3. Then \(Q_T<b_T<3Q_T\) and
\(\gcd(b_T,3Q_T)=1\).

Dirichlet's theorem gives primes in the class
\(b_T\pmod{3Q_T}\). Choose the least one and call it \(\ell_T\). Linnik's
theorem supplies absolute constants \(C,L>0\) such that

\[
Q_T<b_T\leq\ell_T\leq C(3Q_T)^L. \tag{6}
\]

Define

\[
N_T=p_T\ell_T.
\]

Both factors are odd. Equation (6) and the size of \(Q_T\) show that they
are distinct. Hence \(N_T\) is an odd semiprime. Moreover,

\[
N_T\equiv p_Ta_T\equiv R_T\pmod{Q_T}. \tag{7}
\]

The semiprimes are distinct as \(T\) varies. Indeed, the intervals in (5)
are pairwise disjoint. Also \(Q_T>p_T\), so (6) makes \(p_T\) the smaller
prime factor of \(N_T\). Different values of \(T\) give different smaller
prime factors. Explicitly,

\[
Q_T>2^Tq_1^2>2^{9T+4}>2^{2T+1}>p_T.
\]

### Consecutive states and exact canonical inverses

Equations (4) and (7) give \(N_T\equiv1\pmod{2^T}\). For \(1\leq e\leq T\),
define

\[
w_e=N_T-\frac{N_T-1}{2^e}.
\]

This is an integer in \([1,N_T-1]\). Also \(2^e<N_T\), and

\[
2^ew_e
=2^eN_T-(N_T-1)
=1+(2^e-1)N_T
=P_e. \tag{8}
\]

Thus \(w_e\) is the canonical inverse of \(c_e=2^e\). The states are
consecutive powers of two, with no wrap before \(e=T\).

### Private rows and square-class independence

Fix \(e\). Equations (3) and (7) give

\[
P_e=1+d_eN_T\equiv d_eq_e\pmod{q_e^2}.
\]

Since \(q_e\nmid d_e\),

\[
v_{q_e}(P_e)=1. \tag{9}
\]

For \(j\ne e\), reduction modulo \(q_e\) gives

\[
P_j\equiv1-d_jd_e^{-1}
\equiv(d_e-d_j)d_e^{-1}\pmod{q_e}. \tag{10}
\]

The nonzero integer \(d_e-d_j=2^e-2^j\) has absolute value less than
\(2^T<q_e\). Therefore (10) is nonzero, and

\[
q_e\nmid P_j \qquad(j\ne e). \tag{11}
\]

Suppose a product \(\prod_eP_e^{\epsilon_e}\), with
\(\epsilon_e\in\{0,1\}\), is a positive rational square. If some
\(\epsilon_e=1\), then (9) and (11) make its \(q_e\)-valuation odd. This is
impossible for a rational square. Hence every \(\epsilon_e=0\). The
classes of \(P_1,\ldots,P_T\) are linearly independent in
\(\mathbb Q_{>0}^{\times}/(\mathbb Q_{>0}^{\times})^2\).

### Size

From (2),

\[
(10T^2+3T)\log2
<\log Q_T
<(10T^2+5T)\log2. \tag{12}
\]

Indeed, this follows by summing \(4T+2e\) and
\(4T+2e+1\) for \(1\leq e\leq T\), doubling for \(q_e^2\), and adding
the \(T\log2\) term.

Equations (5), (6), and (12) give

\[
\log Q_T<\log N_T
\leq (2T+1)\log2+\log C+L\log(3Q_T).
\]

Therefore

\[
\log N_T=\Theta(T^2).
\]

If \(B_T=\lfloor\log_2N_T\rfloor+1\) is the bitlength, then
\(B_T=\Theta(T^2)\), so

\[
T=\Theta(\sqrt{B_T}).
\]

## Exact scope

The proved obstruction has only these conclusions:

- Exact duplicate relation count is not a progress measure.
- Raw binary nullity is not a progress measure.
- Consecutiveness alone does not force a binary closure.

It is not a failure claim for the full multi-seed rule. It does not prove
an \(n^2\)-long private-row family. It does not imply a factoring lower
bound.

The obstruction also does not apply to the current F98 certificate as
described in the supplied statement. That certificate removes repeated
exact values, uses 166 distinct selected values, and produces a non-global
root that factors its modulus. These F98 facts are scope conditions from
the supplied statement. I did not inspect or audit any F98 artifact.

## Independent computation record

The named verifier is `RECONSTRUCT_verify.py`. It uses Python exact integer
arithmetic and a recursive Lucas test. It does not use a primality library.
The command ran under a hard 20-second timeout and exited with status zero:

```text
/opt/homebrew/bin/timeout --verbose 20s /opt/homebrew/bin/python3 RECONSTRUCT_verify.py > RECONSTRUCT_OUTPUT.txt 2> RECONSTRUCT_LOG.txt
```

SHA-256 hashes:

| File | SHA-256 |
|:---|:---|
| `RECONSTRUCTION_STATEMENT.md` | `53feb27185d06de2c0e8565bb1c324b02c13f64d1dfbab641ca9efa0923b1058` |
| `RECONSTRUCT_verify.py` | `0046473dfc53c254e0d33e427bdbae67b968a97be5f5382c6192788bef4a691a` |
| `RECONSTRUCT_OUTPUT.txt` | `f1259dff00ce140b5840ced62b6d1d1d94fbef1f5127780a53b6792fa23dbf91` |
| `RECONSTRUCT_LOG.txt` | `567850ea8b79558614c16f351f3d6b057ddbd1f46b7ac50de46fe1a75bd39ba0` |

Input scope: I read only `RECONSTRUCTION_STATEMENT.md` in this experiment
directory. I did not read any candidate, theorem, ledger, or other durable
project proof file. Files created by this reconstruction are
`RECONSTRUCT.md`, `RECONSTRUCT_verify.py`, `RECONSTRUCT_OUTPUT.txt`, and
`RECONSTRUCT_LOG.txt`.
