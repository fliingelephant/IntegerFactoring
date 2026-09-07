# F325 exact contraction statement for independent reconstruction

Let N>1 be odd, h=(N-1)/2, and a,b units modulo N. Let rep choose residues in [-h,h], and t=b^-1 modulo N. Let r be exactly the involution of Jeřábek, arXiv:1207.5220, Lemma 4.7, on V={0,1,2} times [-h,h], including its rule that every nonzero nonunit coordinate is fixed. Its fixed vertices have the divisor-or-root decoder of that lemma.

Define

```
D* = {(1,x): x != 0 and the signs of x,rep(a*x),rep(t*x)
                   are not all equal}.
r*(1,x) = (1,-x) for (1,x) in D*;
r*(v) = r(v) otherwise.
```

Let s reflect each layer by x->rep(1-x), except that (0,-h) and (1,-h) are paired together and (2,-h) is its sole fixed vertex. The path protocol starts at (2,-h), applies r*, stops at an r*-fixed vertex, and otherwise applies s and repeats.

Claims to reconstruct:

1. r* is an involution and every fixed vertex has the original valid decoder. The protocol terminates in at most 3N r* calls.
2. For a current (1,x) in D*, x!=h, define z as follows. If x>0, z is the least integer in [x+1,h] for which az mod N and tz mod N both lie in [1,h], with fallback h. If x<0, z is the least integer in [x+1,-1] for which both residues lie in [h+1,N-1], with fallback 0. Applying z-x complete r*-then-s steps produces (1,z), with no r*-fixed source in the skipped interior. At x=h the next complete step goes to (0,-h).
3. This z is computable by a deterministic algorithm polynomial in log N, using the fixed-variable integer-feasibility theorem of Lenstra (1983) as a declared dependency. No factorization, integer counting, or floating optimization is assumed.
4. For a=-1 modulo N, all nonzero layer-1 vertices belong to D*. The entire layer-1 subgraph of the two-matchings graph is one alternating path whose external attachments are the s-edge to (0,-h) and the r*-edge to (0,1). In particular, the oriented r*-then-s protocol from (0,1) reaches (0,-h) after h+1 ordinary calls and can replace that segment by an explicit polynomial-bit connector.
5. If the complete modified path consists of U noncontracted r* calls and J contracted segments of respective positive lengths ell_i, then its expanded length is U+sum ell_i and the exact accelerated algorithm has cost at most (U+J)poly(log N). No quasipolynomial bound on U+J is claimed. No endpoint agreement with the original unmodified r path is claimed. No extra gcd stops are included in these equalities.
6. Let E={0} union {nonzero x: the centered signs of x,ax,tx are all equal}, and write its positive members as e_1<...<e_m. Removing D* from V and contracting the alternating r*-and-s chains gives a parity graph on W=({0,2} times [-h,h]) union ({1} times E). Its first matching is r restricted to W. Its second matching leaves all layer-0/layer-2 s edges unchanged except the cross-layer port and replaces layer 1 by the pairs (1,0)<->(1,e_1), (1,-e_i)<->(1,e_(i+1)) for i<m, and (0,-h)<->(1,-e_m). When m=0, use only (0,-h)<->(1,0). It has exactly one fixed vertex (2,-h). All neighbor queries on this graph are polynomial-bit using the same fixed-dimensional feasibility dependency, without enumerating E or computing m.
