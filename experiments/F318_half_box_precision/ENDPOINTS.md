# From one diagonal interval to arbitrary rectangles

The original inverse graph is symmetric: the matrix
U[u,v]=1_(uv=N modulo M) on the canonical odd residues satisfies U=U^t.
For endpoints x,y in [0,M], define

    D(x,y)=count(min(x,y)<=u,v<max(x,y)).

For arbitrary half-open intervals I=[a,b), J=[c,d), polarization gives
the exact integer identity

    2*count(I,J)=D(a,d)+D(b,c)-D(a,c)-D(b,d).              (1)

To verify it, let p_x be the indicator of odd residues below x.
D(x,y)=(p_y-p_x)^t U(p_y-p_x); expand the four terms and use symmetry.
The formula handles overlapping intervals and coincident endpoints.

At partial precision, recovering the count modulo 2^p from (1) requires
the four diagonal-interval values modulo 2^(p+1), followed by division of
the even residue. Alternatively, values modulo M already determine each
D exactly because 0<=D<=M/2<M. Taking those exact representatives and
dividing their integer contrast gives the exact rectangle count.

This is an algebraic reduction, not a constructor for D. F318 computes
only D(0,M/2) modulo eight. In particular, its fixed half-box cannot be
substituted for the four variable intervals in (1).

The next targeted question can therefore use a single interval on both
coordinates, retaining the additional precision bit. On such an interval,
count parity is just the number of fixed roots u^2=N modulo M in the
interval; all nonfixed inverse pairs contribute twice. The first new bit
counts those internal pairs modulo two. A fast construction for this
variable-endpoint pair count would address a cut operation directly.

No assertion is made that a Pfaffian, a Cauchy determinant, or a character
formula evaluates that pair count. These may be investigated as actual
aggregation mechanisms, with their interval and precision scopes retained.
