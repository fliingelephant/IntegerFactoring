# F145 manifest — quasipolynomial finite-algebra source boundary

## Promoted V2 proof-only result

F145 studies finite-algebra separator sources after the runtime target was
relaxed to quasipolynomial time. Its exact conclusions are:

- a uniform element of any \(d\)-dimensional commutative algebra over
  \(\mathbb F_r\) is a nonunit with probability at most \(d/r\);
- if a \(d\)-dimensional finite etale algebra has \(d<r\), it is monogenic,
  and a uniform element fails full Krylov rank with probability at most
  \(d(d-1)/r\);
- for \(M\) fresh Krylov probes, the total local-rank mismatch probability
  is at most
  \[
  M d(d-1)(1/p+1/q),
  \]
  which is \(2^{-\Omega(n)}\) when \(Md^2=2^{o(n)}\) and
  \(\min(p,q)=2^{\Omega(n)}\), including the intended case in which both
  \(M\) and the explicit algebra rank \(d\) are quasipolynomial in \(n\);
- a genuine CRT-glued absolute Frobenius map exposes a factor on an explicit
  local factor-degree mismatch, while known factors construct that map;
- monomial fixed-point density and additivity have exact hidden group-order
  congruence conditions; and
- for \(N=pq\), \(p<q\), every binomial jet below \(p\) vanishes modulo
  \(N\), while the coefficient at index \(p\) has gcd \(q\) with \(N\).

The first two claims are finite-algebra specializations of P40. The
Frobenius claim extends the structural interpretation of P06--P09 and P17.
F145 does not retry the standard F04 AKS source.

## Artifact history

The V1 source files and both audits are preserved unchanged.

| Artifact | SHA-256 | State |
|---|---|---|
| STATEMENT.md | c00dfc7f43a2ec5fc5b39841a140f744a046f2e31f580d7c430e23963eb8e6bd | V1 frozen statement |
| PROOF.md | 3837fa6cbd0b5b93700c26b0834998133e3ff181fa61afafb5b70254f2d49b40 | V1 frozen proof |
| HOSTILE_AUDIT.md | 7cb06cd97979dbf85f3919b7e2c2903d549b24572a74f481d04c1da815cfd058 | V1 hostile audit: pass |
| BLIND_RECONSTRUCTION_FAILED.md | bd09ef20e1492d49a35a3528e435d4e68c469c299ff3e5e875210463e2246933 | V1 blind reconstruction: fail |
| V2_STATEMENT.md | 9b7b5b21b65222be8a522163e4686dca7a232c94b87645d062dc017088eee18e | V2 frozen statement |
| V2_PROOF.md | 435877c8bb5fbf6791f280bd7e9e4bd8d5764e66e16971138cda4491287effc8 | V2 frozen proof |
| V2_HOSTILE_AUDIT.md | 1e46a571056199825151534ae9fc358f10e4d592473c4a0a5e6d4c17df726c22 | V2 hostile audit: pass |
| V2_BLIND_RECONSTRUCTION.md | 2fc4b10040a351b371164d4db90d201dd27e8c7d92f821579cd7e9dd593b3ac0 | V2 statement-only reconstruction: pass |

## Exact V2 repair

The V1 blind reconstruction found one scope defect, not a failed displayed
theorem. V1 concluded after (8) that quasipolynomially many probes have
exponentially small total mismatch probability without also bounding the
algebra rank. Large ranks can make one-probe mismatch probability constant.

V2 adds the exact sufficient condition

\[
Md^2=2^{o(n)}
\]

and states the intended specialization explicitly: both the probe count and
the represented algebra rank are quasipolynomial. It makes no conclusion for
larger ranks. No other theorem was broadened. In particular, the stronger
all-composite binomial lemma found during the hostile audit was not added;
the candidate keeps the original semiprime scope.

## Evidence and scope

No research computation was used. No empirical claim is made.

The probability bounds apply to fresh uniform algebra elements. They do not
cover biased or factor-correlated sources. The Krylov theorem assumes finite
etale local algebras with rank smaller than the local characteristic. Its
negligible-mismatch specialization also assumes \(Md^2=2^{o(n)}\). The
Frobenius extraction assumes a genuine local Frobenius map, a factor-degree
mismatch, polylogarithmic rank, and local primes larger than the stated
coefficient bound. The monomial theorem is an exact reduction to hidden
congruences, not an impossibility theorem for adaptive exponent menus. The
jet theorem covers a truncation by numerical order, not sparse large indices
or a compressed interval evaluator. The Krylov theorem controls the final
rank, not arbitrary intermediate elimination entries or other matrix
invariants.

F145 is not an all-input factoring algorithm and is not a lower bound for
general finite-algebra algorithms, arithmetic circuits, or joint decoders of
typical nonzero values.

## Verification state

V1 passed its hostile audit and failed its proof-blind reconstruction on the
missing rank scope. V2 passed a fresh hostile audit and an independent
statement-only blind reconstruction. It is promoted as P132. No cross-family
audit, human audit, or publication-level literature review has run.
