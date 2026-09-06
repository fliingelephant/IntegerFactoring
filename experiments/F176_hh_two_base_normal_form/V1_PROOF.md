# Proof of F176

## 1. Imported F174 invariant

Run F174 at \(D=n\). All its exits other than the hard line-13 branch are
unchanged. Hence they already give a proper factor or a factored exact
common-order state above \(n\).

On a line-13 branch, let \((g,M)\) be the current Harvey--Hittmeir state and
let \(\beta\) be the escaped integer. F174 proves all of the following.

1. \(\beta\) is prime.
2. \(M\le n\).
3. Every positive integer \(a<\beta\) is a unit and satisfies
   \(a^M=1\pmod N\).
4. In every hidden prime-power component, \(g\) has exact order \(M\).
5. The F174 absolute and relative screens either factor, produce an exact
   common state above \(n\), or produce the stated hard certificate.

Only the possible value of \(\beta\) needs a new argument.

## 2. An explicit polynomial collision bank

Inputs with \(n<64\) are in one fixed finite range and are handled by direct
trial division. Assume \(n\ge64\) and put

\[
t=\lceil\sqrt n\rceil.
\]

Then \(t\le n/4\), so

\[
6^t\le6^{n/4}=2^{(\log_2 6)n/4}<2^{n-1}<N.
\tag{1}
\]

The final inequality uses that \(N\) is odd and
\(n=\lceil\log_2(N+1)\rceil\), which gives
\(N\ge2^{n-1}+1\). Unique factorization gives

\[
|\mathcal S|=
|\{2^u3^v:0\le u,v\le t\}|=(t+1)^2>n.
\tag{2}
\]

Thus \(\mathcal S\) contains more than \(M\) distinct positive integers,
all below \(N\).

Suppose \(\beta\ge5\). Since \(2,3<\beta\), the imported prefix invariant
gives

\[
2^M=3^M=1\pmod N.
\]

It follows that \(x^M=1\pmod N\) for every \(x\in\mathcal S\).

Choose any rational prime \(p\mid N\). Reduction modulo \(p\) maps
\(\mathcal S\) into the roots of \(X^M-1\in\mathbf F_p[X]\). A nonzero
polynomial of degree \(M\) has at most \(M\) roots, so (2) gives distinct
\(x,y\in\mathcal S\) with

\[
p\mid x-y.
\]

But \(0<|x-y|<N\) by (1). Therefore

\[
1<\gcd(|x-y|,N)<N.
\]

The exhaustive pair screen finds such a pair. This proof uses only a
rational prime divisor of \(N\). It is therefore unchanged when \(N\) has
repeated prime factors or is a prime power.

Consequently every surviving escape has \(\beta<5\). Since F174 proves
that \(\beta\) is prime,

\[
\beta\in\{2,3\}.
\tag{3}
\]

## 3. The base-two branch

The Harvey--Hittmeir loop starts from \((g,M)=(1,1)\), and \(2\) is its
first loop integer. Hence (3) with \(\beta=2\) has the trivial current
state \((1,1)\).

The unchanged F174 absolute screen either factors, produces a common exact
order above \(n\), or proves

\[
\sigma(\operatorname{ord}_{R_j}(2))>n
\]

in every hidden component. In the last case, the unchanged relative scan
against the trivial subgroup either factors, produces a common state, or
proves

\[
\operatorname{ord}_{R_j}(2)>C
\]

for every component. This is exactly the hard base-two output.

## 4. The base-three branch is Mersenne

Suppose \(\beta=3\). The loop processed only the nontrivial integer \(2\)
before this escape. It did not return at line 13 for \(2\), so it computed
the exact global order \(m\le n\). Its prime-divisor gcd screens either
factored \(N\), or certified

\[
\operatorname{ord}_{R_j}(2)=m
\]

in every hidden prime-power component. The lcm update from the initial
state gives \(M=m\). Thus

\[
N\mid2^M-1.
\tag{4}
\]

If \(M<n\), then

\[
0<2^M-1\le2^{n-1}-1<N,
\]

contradicting (4). Therefore \(M=n\). Now (4) and
\(2^n-1<2N\) show that the positive integer \((2^n-1)/N\) is less than
two. It is therefore one, and

\[
N=2^n-1.
\tag{5}
\]

Suppose \(n\) is composite. Trial division of the \(O(\log n)\)-bit integer
\(n\) finds a prime \(\ell\mid n\). The standard identity

\[
2^{n/\ell}-1\mid2^n-1
\]

and (5) give the proper factor

\[
1<2^{n/\ell}-1<N.
\]

Thus a no-factor base-three branch has prime \(n\). The input promise says
that \(N\) itself is composite, so it is a composite Mersenne number with
prime exponent.

The current state is \((2,n)\). Applying the unchanged F174 screens to
\(3\) gives either a prior factor, an exact common-order state above \(n\),
or the two hard assertions in (20) of the statement. This proves the full
normal form.

## 5. Cost and recursion

For \(D=n\), every F174 step is QP. The new bank contains \(O(n)\) integers
and \(O(n^2)\) differences. Its integers have at most
\(t\log_2 6=O(\sqrt n)\) bits. Its construction and all gcds are therefore
polynomial time and space.

Trial division of \(n\) costs \(O(\sqrt n)\) arithmetic steps. The power
\(2^{n/\ell}-1\) has at most \(n\) bits. Hence the Mersenne composite-
exponent screen is polynomial too.

For complete factorization, every proper divisor splits the current input
into strictly smaller positive factors. A recursion path has length at most
the original bit length. Multiplying a QP bound by this polynomial depth
does not leave QP. No claim is made that either surviving hard branch
necessarily supplies such a divisor.
