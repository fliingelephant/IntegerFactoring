# Proof of F159 one-layer saturation

## 1. Local root layers have quotient size at most two

For \(r\in\{p,q\}\), write \(H_r\) for the image of \(H\) in
\(\mathbf F_r^\times\). This ambient group is cyclic.

If \(x_r^2\in H_r\), then the coset \(x_rH_r\) has order at most two in the
quotient. If \(x_r\notin H_r\), the subgroup
\(\langle H_r,x_r\rangle\) has order \(2|H_r|\). A cyclic group has at most
one subgroup of each order. Hence every element \(y_r\notin H_r\) with
\(y_r^2\in H_r\) belongs to the same index-two extension:

\[
\langle H_r,y_r\rangle=\langle H_r,x_r\rangle.
\tag{14}
\]

This uniqueness is the fixed-layer saturation law.

## 2. The explicit scan

If \(x_r\in H_r\), some \(h\in H\) has \(x=h\pmod r\). Therefore one gcd
in (2) is divisible by \(r\). Unless the same \(h\) matches modulo both
hidden primes, that gcd is proper. Thus, on a no-factor branch, the first
scan classifies \(x\) exactly as globally internal or external in both
hidden components.

Let \(x_0\) be the first external element. F158 gives

\[
K=H\sqcup x_0H,
\qquad
|K|=2|H|,
\qquad
|K_r|=2|H_r|.
\]

For any remaining \(y\in X\), either \(y_r\in H_r\) or (14) puts
\(y_r\in K_r\). Thus \(y_r\in K_r\) for both hidden primes. Because \(K_r\)
is the image of the public list \(K\), some comparison with \(K\) is
divisible by \(p\), and some comparison is divisible by \(q\). If no proper
gcd occurs, one comparison must equal \(N\), so \(y\in K\) globally.

Therefore no second extension survives. This proves (4) and (5). The list
\(K=H\sqcup x_0H\) has size \(2|H|\), which gives the stated cost.

## 3. Compact cyclic alignment

For each \(x_i\), F158 proves that the internal solutions are exactly the
solutions of (8). A comparison that matches in one hidden field only gives
a proper gcd. On the no-factor branch, each \(x_i\) is therefore globally
internal or external in both fields.

Fix the first external \(x_0\). Locally, (14) shows that every other
external \(x_i\) has the form

\[
x_i=x_0g^{k_r}\pmod r
\]

for some exponent \(k_r\pmod M\). Squaring and using (7) gives

\[
2k_r=a_i-a_0\pmod M.
\]

There are at most two public solutions. Testing both in (10) finds a proper
gcd if the two hidden fields choose incompatible solutions. Otherwise one
candidate matches modulo \(N\), so \(x_i\in x_0\langle g\rangle\).

Because \(x_0^2=g^{a_0}\) and \(a_0\) is invertible modulo \(M\), choose
\(b\) with \(a_0b=1\pmod M\). Then

\[
g=(x_0^2)^b\in\langle x_0\rangle.
\]

F158 gives exact local order \(2M\) for \(x_0\). Hence
\(\langle g,x_0\rangle=\langle x_0\rangle\) and (11) follows.

## 4. Source boundary

Equation (12) puts all representatives from one frozen section into the
same quadratic root layer. Sections 1--3 show that this entire layer has
rank at most one beyond \(H\) on a no-factor branch. More candidates can
test more possible alignment disagreements, but they cannot cause repeated
doubling without first changing the base subgroup. This proves (13) and the
stated remaining-source boundary.
