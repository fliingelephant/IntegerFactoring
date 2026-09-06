# F151 manifest — QP large-order and Jacobi-torus boundary

## Candidate status

V1 failed its hostile audit because it made the unrestricted claim that
integer carry effects were the only remaining progress source. The four
displayed mathematical theorems survived. V1 and its failed audit remain
preserved.

V2 is the frozen proof-only scope repair. It limits the result to the
explicitly listed short-window exponent, collision, and sign screens. It
leaves larger exponents, component-order finding beyond the cutoff, and all
other decoders open. Its fresh hostile re-audit passed. Its independent
statement-only reconstruction verified the mathematical core but returned a
conditional verdict because `iota_N`, the exact-value decoder, factor-free
refinement, and the external-premise interfaces were not fully stated.

V3 is the narrow self-containment repair. It defines the missing notation,
states the first-occurrence factor-free square decoder exactly, and records
the Harvey--Hittmeir and Pilatte results as explicit cited premises. It adds
no all-input progress claim and does not strengthen V2. V3 passed a fresh
hostile audit and a fresh independent statement-only reconstruction. It is
the promoted version.

## Frozen history and hashes

- V1 `STATEMENT.md`:
  `eaa960c2e3e9ee594ec714d58d2a69af0ea2e1c818c89524cbd154aef2935acb`;
- V1 `PROOF.md`:
  `0cc9660bc00f668c5f14f34ac684fa916e0acd4e05c59108b8a9864c761dcefd`;
- V1 `HOSTILE_AUDIT_FAILED.md`:
  `249eda66360cf80f16257821c58cb1dcffe1495fb028ae9b1a70be29af8448c7`;
- V2 `V2_STATEMENT.md`:
  `325c1f8facf40e114586a5e7c1759129d7a422479102f9798da6a5fa42f7dec6`;
- V2 `V2_PROOF.md`:
  `79f6ba29e886e61c98e913ade8933e5c4157822047bfae6332e6bc017c2855be`;
- V2 independent reconstruction `V2_BLIND_RECONSTRUCTION.md`:
  `3158e2011a416827b7be07b4e6105fda61a6a351ea7c31d29118f0e403a0a989`;
- V2 hostile re-audit `V2_HOSTILE_REAUDIT.md`:
  `64a74cd43084ad3578db218fd1ed8a43e836b33cf6131ba152fe3097fa185fe2`;
- V2 hostile checker `V2_HOSTILE_REAUDIT_CHECK.py`:
  `109dcac3a3785f59cfd9e866fb471009a69e679078281221945a1b1c279365c8`;
- V3 `V3_STATEMENT.md`:
  `73c8e7a8c58fd3fd40f56f3128ded748313a98cd9b76ec663bee9ec55ba50b98`;
- V3 `V3_PROOF.md`:
  `a4ffebd5cd981ea949850bc2cb71ff34a07ec41969904cf7c46cd05941ca3f57`;
- V3 hostile audit `V3_HOSTILE_AUDIT.md`:
  `c56708f30685bad8e9623e3184824e917ebf1709ba0c2c6236f3859de43b2f02`;
- V3 independent reconstruction `V3_BLIND_RECONSTRUCTION.md`:
  `d2723413004c14e035526e5b176d7228d86a596431aa605ea23836d32b8e0698`.

## Closest prior results

- P55 already gives the exact Jacobi-torus signed-gap relation.
- P85 blocks generic fixed quasipolynomial modular-word menus.
- P132 gives the quasipolynomial finite-algebra sampling boundary.
- P133 gives the quasipolynomial local-matroid exchange boundary.

F151 is materially different because it imports a deterministic certified
large-order element, upgrades it to a large-order-in-every-prime-component
source, and tests the direct splice into the existing P55 torus. V3 does not
change this comparison.

## External primary sources

- Harvey and Hittmeir, arXiv:2601.11131v2, Theorem 1.1.
- Pilatte, arXiv:2404.16450v2, Corollaries 1.4--1.5 and Theorem 3.18.

## Scope

The candidate proves local collision freedom only for its displayed
short-window screens, and it proves one fixed-Kummer-coordinate splice
obstruction. The now-explicit exact-value decoder has finite capability
witnesses, but no all-input success law. The candidate does not prove that
the large-order source has no factor signal. In particular, it does not
exclude larger exponents, component-order mismatches, other value-dependent
decoders, canonical integer carry effects, a structured classical sampler
for Pilatte's basis, or other Jacobi-torus/high-order combinations. It is not
a factoring algorithm.
