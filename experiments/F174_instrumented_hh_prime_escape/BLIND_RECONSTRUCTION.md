# Blind reconstruction of F174

## Scope and verdict

The SHA-256 of the statement read for this reconstruction is

```text
6f5ff26ad6e5735d60e85bb394b992b44e05698bee7c9d51d902a240205d5908
```

I used the Harvey--Hittmeir transcript facts in Section 2 as premises. I did
not independently inspect that external algorithm. I also treat the stated
F172 bound on ordinary common orders as an external family premise.

**Verdict: the displayed operational trichotomy and its quantitative bounds
are valid from those premises, but F174 is not literally correct in all of
its prose.** Section 5's heading says that the raw escaped prime is outside
every old local subgroup. At that point it is known to be outside at least
one such subgroup, not necessarily all of them. A concrete compatible HH
state below refutes the stronger wording. The all-components statement does
become true after the absolute screen reaches its `A_beta = 1` branch.

There is a second necessary scope qualification. For a general input, the
hard branch does not imply that the hidden local orders, or the hidden
quotient orders, are unequal. It only fails to return an exact common order.
Inequality follows after specialization to the F172 family. Thus the opening
phrase "no exact common quotient order" is correct only if it means "no exact
common quotient order is returned or certified."

With these two wording repairs, I find no mathematical obstruction to
(1), (14)--(15), (19)--(20), (23)--(27), (29)--(32), or the claimed QP bit
cost.

## 1. Exhausting the HH exits

The early test cannot fire under the stated parameters. Indeed,

\[
D\ge n=\lceil\log_2(N+1)\rceil
\quad\Longrightarrow\quad
2^D\ge 2^n\ge N+1>N.
\]

The remaining exits are therefore as follows.

1. A gcd screen returns a nontrivial proper divisor.
2. A successful order search is merged into the state. If the new state has
   order greater than \(D\), it is Outcome B.
3. An unsuccessful order search is the line-13 escape and is sent through
   the absolute and relative screens.
4. If the loop ends, the stated arithmetic-progression premise returns a
   prime divisor of composite \(N\).

This list is exhaustive under the Section 2 premise.

## 2. Exact common-order invariant

The invariant has a direct prime-primary induction. Suppose the current
element \(g\) has exact order \(M\) in every \(R_j\), and a scanned integer
\(a\) has exact global order \(t\le D\). Write \(t_j\) for its order in
\(R_j\). For each prime \(\ell\) for which

\[
v_\ell(t)>v_\ell(M),
\]

exactness of the global order says that at least one \(t_j\) has the full
\(\ell\)-adic exponent \(v_\ell(t)\). The corresponding prime-divisor gcd
screen cannot return \(N\). If it does not return a proper factor, it must
return \(1\), which forces every local \(t_j\) to have that full exponent.
Consequently

\[
\operatorname{lcm}(M,t_j)=\operatorname{lcm}(M,t)
\quad\text{for every }j.
\]

The unit group modulo an odd prime power is cyclic. Prime-primary parts of
\(g\) can therefore be retained where \(M\) supplies the largest exponent,
and prime-primary parts of \(a\) can be used where \(t\) supplies it. Their
product has exact order \(\operatorname{lcm}(M,t)\) in every component. This
is the required lcm merge and preserves a completely factored order.

A common exact order \(M\) cannot satisfy \(\gcd(M,N)=N\). If \(N\) has at
least two distinct prime divisors, its largest prime divisor cannot divide
the group order of a component belonging to a smaller prime. If
\(N=p^a\), then \(v_p(M)\le a-1\). Hence a nontrivial \(\gcd(M,N)\) is always
a proper factor. On a no-factor branch, (7) follows.

Before the scan reaches \(\beta\), every earlier integer was either already
killed by the old \(M\), or had its order incorporated into a later multiple
of \(M\). Thus

\[
a^M=1\pmod N\qquad(1\le a<\beta).
\]

This also proves that all such \(a\) are units. The HH return condition gives
\(M\le D\) before line 13 and before the loop-end scan. This reconstructs
(6), (7), and (11), including repeated odd prime powers.

## 3. The exact smooth-prefix cutoff

Put \(L=L_D\), \(J=J_D\), and \(H=H_D\). For all sufficiently large \(L\),
the standard elementary upper bound for the \(L\)-th prime gives \(L\)
distinct primes

\[
q_1,\ldots,q_L\le 2L\log_2(L+1)\le 2LJ\le H.
\]

The finite set below this absolute range is covered by the statement's
finite-table convention. Also,

\[
\log_2 H=3+\log_2L+\log_2J\le 8J,
\]

so every square-free subset product of these primes is at most

\[
H^L\le 2^{8LJ}=X_D.
\]

There are \(2^L\ge 2D>M\) distinct such products.

Assume \(\beta-1\ge Y_D=H^2\). Then every \(q_i<\beta\), and (11) makes every
subset product an \(M\)-th root of unity modulo each prime divisor \(p\) of
\(N\). If \(p>X_D\), those subset products remain distinct modulo \(p\).
This gives more than \(M\) roots of the degree-\(M\) polynomial
\(x^M-1\) over \(\mathbb F_p\), a contradiction. Therefore every prime
divisor \(p\) of \(N\) satisfies

\[
p\le X_D.
\]

Reduction from \((\mathbb Z/p^a\mathbb Z)^\times\) to
\(\mathbb F_p^\times\) has a \(p\)-group kernel. Since
\(\operatorname{ord}_{p^a}(g)=M\) and \(p\nmid M\), the reduction of \(g\)
still has order \(M\). Hence \(M\mid p-1\), so \(p=kM+1\) occurs in the
scan (13). The gcd with \(N\) is a proper divisor, including when
\(N=p^a\).

Thus a no-factor escape has \(\beta-1<Y_D\), which proves the exact
\(\beta\le Y_D\) bound in (14). Equations (10) and (15) follow directly
from

\[
H_D=O(\log D\log\log D),
\qquad
\log D=(\log n)^{O(1)}.
\]

The constants \(8\), the square in \(Y_D\), and the definition of \(L_D\)
all have sufficient slack for this counting argument.

## 4. What the raw escape does and does not prove

Because every proper factor of a composite \(\beta\) is smaller than
\(\beta\), (11) and the cyclic local groups would put every prime factor of
\(\beta\), and hence \(\beta\) itself, in every \(H_j\). That would imply
\(\beta^M=1\pmod N\), contrary to (17). Therefore the escaped integer is
prime.

However, (17) says only that \(\beta\notin H_j\) for at least one \(j\).
It does not say this for every \(j\). The distinction is real. Consider

\[
N=2047=23\cdot89,
\qquad n=D=11,
\qquad g=2,
\qquad M=11.
\]

Since \(2^{11}=2048\), the element \(2\) has exact order \(11\) modulo both
\(23\) and \(89\). At the next source integer \(\beta=3\), one has

\[
3=2^8\pmod {23},
\]

so \(3\in H_{23}\). In contrast,

\[
\langle2\rangle\pmod {89}
=\{1,2,4,8,16,32,64,39,78,67,45\},
\]

so \(3\notin H_{89}\). Its order modulo \(23\) is \(11\), while
\(3^{11}\ne1\pmod {89}\); hence its global order is greater than \(D=11\),
exactly as required for a line-13 escape. This refutes the Section 5 heading
if "outside every" is read literally.

The valid raw statement is:

\[
a\in H_j\text{ for all }a<\beta\text{ and all }j,
\qquad
\beta\notin H_j\text{ for at least one }j.
\]

Equivalently, \(\beta\) is outside the product condition
\(\prod_j H_j\), not necessarily outside each factor. On Outcome C, (20)
repairs the stronger claim: membership in any \(H_j\) would make the local
order divide \(M\le D\), contradicting (20).

## 5. Absolute factor-first classification

Let \(t_j=\operatorname{ord}_{R_j}(\beta)\).

If \(1<A_\beta<N\), the gcd itself is a proper factor.

If \(A_\beta=N\), every \(t_j\) divides \(\Lambda_D\). Start with the
factored exponent \(E=\Lambda_D\). For each prime \(\ell\mid E\), test
\(\gcd(\beta^{E/\ell}-1,N)\), repeatedly as applicable.

- A result \(N\) permits replacing \(E\) by \(E/\ell\).
- A proper result factors \(N\).
- A result \(1\) means that every local order retains the current full
  \(\ell\)-primary exponent.

If no factor occurs, the final \(E=m\) is therefore the exact order of
\(\beta\) in every component. The line-13 premise says that the global
order exceeds \(D\), so \(m>D\). As in Section 2 above,
\(\gcd(m,N)>1\) would be a proper factor; otherwise this is an Outcome B
state with \(\gcd(m,N)=1\).

If \(A_\beta=1\), then \(\beta^{\Lambda_D}\ne1\pmod {p_j}\) for every
prime divisor \(p_j\) of \(N\). Thus \(t_j\nmid\Lambda_D\). Some exact
primary divisor \(\ell^a\parallel t_j\) has

\[
a>\lfloor\log_\ell D\rfloor,
\]

and consequently \(\ell^a>D\). This is exactly (20).

These three gcd outcomes are exhaustive and disjoint.

## 6. Relative factor-first classification

The cyclicity of \((\mathbb Z/R_j\mathbb Z)^\times\) and
\(|H_j|=M\) imply that \(H_j\) is precisely its subgroup of solutions to
\(x^M=1\). Therefore

\[
\beta^{eM}=1\pmod {R_j}
\quad\Longleftrightarrow\quad
\beta^e\in H_j
\quad\Longleftrightarrow\quad
e_j\mid e.
\]

This equivalence is the essential justification for (21)--(26). A proper
\(G_e\) factors \(N\). On a no-factor scan, all earlier values are \(1\).
If the first global value \(N\) occurs at \(e\), then every \(e_j\mid e\).
If some \(e_j<e\), the earlier test at that integer would already have had
a nontrivial gcd. Hence every \(e_j=e\), proving (23). Also \(e\ne1\),
because (17) excludes \(\beta^M=1\pmod N\).

For each component, the cyclic subgroup

\[
K_j=\langle g,\beta\rangle
\]

has order \(M e\). If \(\ell\mid e\), the \(\ell\)-primary part of
\(\beta\) has the full \(\ell\)-exponent of \(Me\); if \(\ell\nmid e\),
the corresponding primary part of \(g\) does. Multiplying these selected
primary parts constructs one public element \(h\) of exact order
\(L=Me\) in every component. It also proves

\[
L=Me=\operatorname{lcm}(M,\operatorname{ord}_N(\beta)).
\]

The integer \(e\le C\) can be factored within the stated QP budget, so the
factorization of \(L\) is known. A nontrivial \(\gcd(L,N)\) is again a
proper factor; otherwise (27) holds. Finally, the line-13 global order gives
\(L>D\), and \(e\ge2\) gives strict growth.

If every \(G_e=1\) through \(C\), then an \(e_j\le C\) would make the test
at \(e=e_j\) nontrivial. Thus every \(e_j>C\). The same cyclic-subgroup
equivalence shows that \(e_j\) is the exact order of \(\beta^M\) modulo
\(R_j\). Hence the \(C+1\) fingerprints in (30) are distinct, and in fact

\[
|\langle g,\beta\rangle_{R_j}|=M e_j\ge M(C+1),
\]

which proves (31).

## 7. Final trichotomy and QP cost

The HH exits in Section 1, followed by the disjoint gcd classifications in
Sections 5 and 6, give the operational Outcomes A, B, and C. On C, the
absolute branch gives (20), the relative branch gives (26), and the prefix
argument gives a prime \(\beta\le Y_D\). Thus (28)--(31) all hold. Notice
that the outcomes are exclusive as return branches; their mathematical
witness properties need not be exclusive. A hard-block tuple can coexist
with an as-yet-unknown exact common order.

All costs are QP in \(n\):

- the stated HH bound is QP for QP \(D\);
- \(\Lambda_D\) has QP bit length, and its sieve, modular exponentiation,
  and stripping take QP bit operations;
- the relative scan performs \(C\) modular exponentiations and gcds;
- the prefix scan has at most \(X_D\) candidates, where
  \(\log_2X_D=O(\log D\log\log D)=(\log n)^{O(1)}\);
- the constructed orders, their factorizations, the selected primary
  exponents, and all residues have QP encoding length.

This establishes the uniform deterministic QP cost. It does not establish a
factoring algorithm because Outcome C remains possible.

## 8. F172 corollary and the hidden-order scope

Assume the F172 premise means that every residue whose exact orders are
equal across all hidden prime-power components has that common order at most
six. Choose an admissible QP \(D>6\) (with the finite small inputs handled as
stated). Outcome B would provide a residue \(h\) with common exact order
\(L>D>6\), a contradiction. Therefore only A or C can be returned, proving
(32) conditionally on that family premise.

There is an additional family-only consequence. On C, each local order
\(t_j\) of \(\beta\) has \(\sigma(t_j)>D\), so \(t_j>D>6\). If all the
\(t_j\) were equal, \(\beta\) itself would violate the F172 common-order
bound. Thus at least two hidden local orders differ on the F172 family.

No such inequality follows for arbitrary odd composite \(N\). Conditions
(29) are compatible with all \(t_j\) being the same, and they are also
compatible with all quotient orders being one common value \(e_j=E>C\).
The general hard branch means that the bounded scans did not *return* an
exact common order. It does not prove that no exact common order exists.
Accordingly, the final question about localizing "the unequal hidden
orders" is valid only in the F172 specialization.

## Claim-by-claim disposition

- **HH exits and (5):** exhaustive after observing that the early exit is
  impossible under \(D\ge n\); otherwise dependent on the quoted HH premise.
- **Common state (6)--(7) and prefix (11):** reconstructed by the
  prime-divisor screens and cyclic prime-power unit groups.
- **Cutoff (8)--(15):** reconstructed with the exact constants.
- **Raw subgroup wording (16)--(17):** equations valid; "outside every old
  local subgroup" is false before the absolute screen.
- **Absolute cases (18)--(20):** reconstructed.
- **Relative cases (21)--(26):** reconstructed.
- **Outcomes (27)--(31):** reconstructed as operational return branches.
- **QP cost:** reconstructed.
- **F172 consequence (32):** valid conditional on the stated family premise;
  hidden-order inequality is family-specific.
