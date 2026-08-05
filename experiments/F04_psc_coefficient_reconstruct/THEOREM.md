# Determinant criterion, reconstructed from first principles

## Statement and conventions

Let `K` be a field.  Let nonzero `F,G in K[X]` have degrees `m>n`.  Put
`R_0=F`, `R_1=G`, and run ordinary Euclidean division

`R_(i-1) = Q_i R_i + R_(i+1)`

until the last nonzero remainder `R_s`; write `d_i=deg R_i`, so

`m=d_0>d_1=n>...>d_s=g`.

For `0<=j<=n`, let `Phi_j` send `(U,V)`, with

`deg U<n-j` and `deg V<m-j`,

to the coefficient vector in degrees `j,...,m+n-j-1` of `UF+VG`.  The source
and target both have dimension `m+n-2j`.  Let `D_j` be the determinant in the
ordering in the question (increasing shifts of `F`, then increasing shifts of
`G`, and increasing coefficient degrees).  Transposing the displayed matrix
or changing those orderings can only change its determinant by sign, so it
cannot affect the criterion below.

**Theorem.** `D_j != 0` exactly when `j` is one of
`d_1,...,d_s`.

## Extended-remainder facts

Write

`R_i=S_i F+T_i G`,

starting with `(S_0,T_0)=(1,0)` and `(S_1,T_1)=(0,1)`, and applying the same
Euclidean recurrence.  Direct induction gives, for `i>=2`,

`deg S_i=n-d_(i-1)` and `deg T_i=m-d_(i-1)`.

Indeed this is true for `i=2`, where `S_2=1` and `T_2=-Q_1`.  At every later
step the newest quotient term has degree strictly larger than the older term,
so no leading cancellation is possible.  The same recurrence also gives

`S_i T_(i-1)-S_(i-1) T_i` equal to `+1` or `-1`.

Thus `S_i` and `T_i` are coprime.

## The minimal-approximation lemma

Fix `i>=2`.  There are no `U,V`, not both zero, satisfying

`deg U<n-d_i`, `deg V<m-d_i`, and `deg(UF+VG)<d_i`.

To prove this, put `H=UF+VG`.  If `U=0`, then a nonzero `VG` has degree at
least `n>d_i`, so suppose `U!=0`.  Set `A=-V`, so `H=UF-AG`, and compare
`A/U` with the Euclidean approximant `-T_i/S_i`.  The identity

`S_i H-U R_i=-(A S_i+T_i U)G`

has left-hand side of degree less than `n`: the two summands have degrees at
most

`(n-d_(i-1))+(d_i-1)<n` and `(n-d_i-1)+d_i<n`.

If `A S_i+T_i U` were nonzero, the right-hand side would have degree at least
`n`, a contradiction.  Hence it vanishes.  Coprimality of `S_i,T_i` implies
`(U,A)=L(S_i,-T_i)` for some polynomial `L`.  Consequently `H=L R_i`, which
is either zero with `L=0` or has degree at least `d_i`.  Both alternatives
contradict the assumptions.  This proves the lemma.  The case `i=1` is even
simpler: at `j=n` the bound `deg U<0` forces `U=0`, and then no nonzero `VG`
has degree below `n`.

## Kernel characterization and all cases

Every `UF+VG` in the source of `Phi_j` has degree at most
`m+n-j-1`.  Therefore `(U,V)` is in its kernel exactly when
`deg(UF+VG)<j` (with the zero polynomial allowed).

* If `j=d_i`, the minimal-approximation lemma (or the direct `i=1` argument)
  says the kernel is zero.  Since `Phi_j` is square, `D_j!=0`.
* If `d_(i+1)<j<d_i`, use
  `R_(i+1)=S_(i+1)F+T_(i+1)G`.  Its coefficient degrees are
  `n-d_i<n-j` and `m-d_i<m-j`, while `deg R_(i+1)=d_(i+1)<j`.
  It is a nonzero kernel witness, so `D_j=0`.  This includes every abnormal
  gap, including the gap immediately below the top index `n=d_1`.
* If `j<g`, the exact syzygy `(U,V)=(G/R_s,-F/R_s)` obeys both strict degree
  bounds and maps to zero.  Thus `D_j=0` below a positive-degree gcd.

These cases exhaust `0<=j<=n`.  In particular, the top index `n`, a positive
gcd, and arbitrary degree gaps require no genericity or characteristic
assumption beyond `K` being a field.

## Application to the fixed certificate

For `F=P=X^2953-1` and any field reduction `G=H_a`, a verified chain

`2953,2952,...,0`

has `d_1,...,d_s=2952,...,0`.  The theorem therefore certifies all 2,953
determinants for that field and shift without constructing their exponentially
redundant dense matrices.

