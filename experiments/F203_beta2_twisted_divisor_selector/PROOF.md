# Proof of F203

## 1. Location of the hidden divisor

Since \(p<q\), one has \(p<\sqrt N<q\), so \(p\leq B<q\). The balance
condition \(q<2p\) gives

\[
 \sqrt N<\sqrt2\,p<2p,
\]

hence \(B/2<p\). Therefore \(p\) lies in
\((\lceil B/2\rceil,B]\), while \(q\) does not.

More explicitly, the odd prime \(p\geq3\) also gives
\(B+1\leq\sqrt N+1<\sqrt2p+1<2p\), so
\(\lceil B/2\rceil<p\). This removes the possible endpoint ambiguity from
the ceiling.

The granted congruence \(u\equiv p^{-1}\pmod m\) gives

\[
 r\equiv p\pmod m.
\]

Since \(N=pq\), it also gives

\[
 c\equiv Nu\equiv q\pmod m.
\]

The two odd lifts of \(r\pmod m\) are \(r\) and \(r+m\pmod{2m}\).
Thus \(w_{m,r}(p)=\epsilon\in\{+1,-1\}\), and its sign identifies the
unique child progression containing \(p\).

## 2. The public sibling relation

Write

\[
 p\equiv r+am\pmod{2m},\qquad a\in\{0,1\}.
\]

Let \(v\equiv r^{-1}\pmod{2m}\). Because \(r,v\) are odd and \(m\) is
even,

\[
 (r+am)(v+am)
 =rv+am(r+v)+a^2m^2
 \equiv1\pmod{2m}.
\]

Therefore

\[
 p^{-1}\equiv v+am\pmod{2m}.
\]

Multiplication by the odd integer \(N\) preserves the lift bit:

\[
 q\equiv Np^{-1}
 \equiv Nv+aNm
 \equiv c_0+am\pmod{2m},
\]

where \(c_0\equiv Nv\pmod{2m}\).

If \(c\ne r\), then \(q\not\equiv r\pmod m\), so its weight is zero.
If \(c=r\), then \(c_0\) is one of \(r,r+m\). Shifting \(c_0\) by
\(am\) flips its \(w_{m,r}\)-sign exactly when \(a=1\). Since

\[
 \epsilon=w_{m,r}(r+am)=(-1)^a,
\]

one obtains

\[
 w_{m,r}(q)=w_{m,r}(c_0)(-1)^a
 =\lambda\epsilon.
\]

This proves the public sibling relation.

## 3. Twisted divisor coefficient

The positive divisors of \(N=pq\) are exactly

\[
 1,p,q,N.
\]

Hence, after subtracting the public endpoint terms,

\[
 T=pw_{m,r}(p)+qw_{m,r}(q).
\]

If \(c\ne r\), the second weight is zero, and \(T=\epsilon p\). If
\(c=r\), Section 2 gives

\[
 T=\epsilon p+\lambda\epsilon q
 =\epsilon(p+\lambda q).
\]

This is the displayed three-case formula. Since \(p,q\) are distinct,
none of its values is zero. In the first two cases its sign is \(\epsilon\).
In the last case \(p-q<0\), so its sign is \(-\epsilon\). This proves the
selector formula.

The factor extraction is exact. In the first case, \(|T|=p\). In the second,
\(s=|T|=p+q\), and \(p,q\) are the integer roots of

\[
 X^2-sX+N.
\]

In the third, \(d=|T|=q-p\). Then

\[
 d^2+4N=(q-p)^2+4pq=(p+q)^2.
\]

Thus an exact integer square root gives \(s=p+q\), followed by

\[
 p=\frac{s-d}{2},\qquad q=\frac{s+d}{2}.
\]

All inputs and outputs have \(O(\log N)\) bits. Conversely, given the
factorization, list the four divisors and evaluate their public weights.
This proves polynomial-time equivalence on the promise.

For the Lambert series, expand formally:

\[
 \sum_{a\geq1}\frac{a w_{m,r}(a)X^a}{1-X^a}
 =\sum_{a\geq1}\sum_{k\geq1}a w_{m,r}(a)X^{ak}.
\]

The coefficient of \(X^N\) is obtained exactly when \(a\mid N\), and is
therefore \(S_{m,r}(N)\).

When \(m=2,r=1\), the two supported classes modulo four are one and three,
with signs \(+1\) and \(-1\), while the even classes have weight zero.
This is exactly \(\chi_4\).

## 4. The first contracted quotient

Because \(p\equiv r\pmod m\) and \(q\equiv c\pmod m\), one has
\(N\equiv rc\pmod m\), so \(K\) is integral. Also

\[
 0<rc<m^2<p^2<N,
\]

which proves \(K>0\). Since \(m\geq2\),

\[
 K=\frac{N-rc}{m}<\frac N2.
\]

As \(m\) is coprime to the odd number \(N\),

\[
 \gcd(K,N)
 =\gcd(mK,N)
 =\gcd(N-rc,N)
 =\gcd(rc,N).
\]

The inequalities \(0<r,c<m<p<q\) show that both \(r\) and \(c\) are
coprime to \(N\). Hence \(\gcd(K,N)=1\).

Write

\[
 p=r+mP,\qquad q=c+mQ
\]

for integers \(P,Q\), and put \(a=P\bmod2\), \(b=Q\bmod2\). Expansion
gives

\[
 N=rc+m(rQ+cP)+m^2PQ
\]

and therefore

\[
 K=rQ+cP+mPQ.
\]

Modulo two, \(r,c\) are odd and \(m\) is even, so

\[
 \delta\equiv K\equiv P+Q\equiv a+b\pmod2.
\]

For bits this is exactly \(b=a\mathbin{\mathsf{xor}}\delta\).

For either candidate pair \((a,b)\), expand

\[
 (r+am)(c+bm)=rc+m(ac+br)+abm^2.
\]

Using \(N-rc=mK\) gives

\[
 \frac{N-(r+am)(c+bm)}{2m}
 =\frac{K-ac-br-abm}{2}.
\]

The numerator on the right is even because

\[
 K-ac-br-abm\equiv\delta-a-b\equiv0\pmod2.
\]

Also \(0<r+am,c+bm<2m<p\), so their product is below \(p^2<N\).
Thus both \(K'_a\) are positive and below \(N/(2m)\).

Finally, \(2m\) is coprime to \(N\), and both lifted residues are positive
and below \(p\). Therefore

\[
 \gcd(K'_a,N)
 =\gcd(2mK'_a,N)
 =\gcd((r+am)(c+bm),N)
 =1.
\]

For the true bit pair, the lifted residues are precisely those of \(p,q\),
so \(K'_a\) is the next quotient state by definition.

## 5. Exact coalescence

If \(\delta=0\), then \(b=a\), and substitution gives

\[
 K'_0=K/2,
 \qquad
 K'_1=(K-r-c-m)/2.
\]

Their difference is \((r+c+m)/2>0\), so they cannot agree.

If \(\delta=1\), then \(b=1-a\), and

\[
 K'_0=(K-r)/2,
 \qquad
 K'_1=(K-c)/2.
\]

They agree exactly when \(r=c\). In this case \(a+b=1\), so the two factors
occupy opposite \(2m\)-children of their common class modulo \(m\). Swapping
the orientation between the smaller and larger factor does not change the
candidate quotient.

At \(m=2\), every odd integer is one modulo two, so \(r=c=1\). Moreover,

\[
 \delta\equiv\frac{N-1}{2}\pmod2
\]

is one exactly when \(N\equiv3\pmod4\). The common value is

\[
 \frac{K-r}{2}
 =\frac{(N-1)/2-1}{2}
 =\frac{N-3}{4}.
\]

This proves the coalescence theorem.

## 6. Complexity statement and non-implications

Since \(0<K<N/2\), its binary length is at most the binary length of
\(N\) minus one. A construction making only one recursive call on such an
integer obeys

\[
 \mathcal T(n)\leq\mathcal T(n-1)+Q(n).
\]

For nondecreasing numerical-QP \(Q\), iteration gives

\[
 \mathcal T(n)\leq nQ(n),
\]

which is still numerical QP. This proves only the recursion accounting.

Nothing above shows how the factorization of \(K\) chooses \(a\). In the
coalescing case, even replacing \(K\) by the candidate next quotient does
not help, because both candidates are the same integer. This is an exact
information identity, not a hardness claim. It leaves all adaptive
deterministic decoders outside its scope.
