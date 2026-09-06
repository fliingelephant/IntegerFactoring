# F242 V2 provenance

The closest positive result is F238/P205.  It uses the ordinary local unit
orders `p-1,q-1`, the public factor `N-1`, an arbitrary unfactored word,
and Miller amplification after a global return.  F242 transfers that exact
mechanism to every quadratic norm-one torus orientation.  The new common
part is supplied by `N-J`, where `J` is the public Jacobi sign.

The closest torus interface is F170/P156, which requires one certified exact
common torus order.  F242 does not certify or factor a common order.  It uses
a raw public word and the full hidden common shifted divisor already present
in `N-J`.

The exact full-torus sampler differs from the Cayley sampler used in P55.  It
maps a uniform algebra unit by `z/bar(z)`.  Constant local fibre size gives
the full uniform torus, including the Cayley point at infinity.  A
choose-discriminant-first rejection order preserves the hidden orientation
law.

## V1 record and V2 repair

The frozen V1 hashes are:

```text
e3364b88dbf11b4a1b53daeeaa629e6c22d97de58615a146a671c616ac2c7123  STATEMENT.md
8b6217f246b4f7462a619322256c4e474e90ad6a1204dceccbe831dc0dd21719  PROOF.md
a4a0d42552c75143ed86b53d94130e163d005c1f9c18fabbc49147074566eb36  SELF_AUDIT.md
4de0646c0e0ccf0f364ca7ce22416a44af4496f57f74aed1fd533e7dbefd47b6  PROVENANCE.md
8954d70255041168f931e40b5f824d8f67c23b1ec2af72b2cb16d5ab74114b55  MANIFEST.md
```

The V1 hostile audit returned **PASS** and has SHA-256

```text
9863d61a199dd0a4b162a9c43e9934dd7e32a5ee46221b5738e9e5e8dc2c6c76  HOSTILE_AUDIT.md
```

The V1 strict statement-only reconstruction returned **FAIL** and has
SHA-256

```text
dc4d5ae3f0f276796b3e4e087ab1f8da597f737b9af6509527054549bcb3a282  BLIND_RECONSTRUCTION.md
```

The blind reconstruction independently recovered the exact torus sampler,
shifted-gcd identity, Miller law, four-orientation average, and conditional
complexity bound.  Its sole failure was self-containment: V1's final warning
named the P158/F172 family but did not define that family or prove the size
relation needed for the warning.

V2 removes that named-family paragraph and the corresponding proof section.
It replaces them with the direct, self-contained boundary that a fixed word
gives only four residual laws and that the theorem proves none of them small.
The core theorem is unchanged.

No mathematical computation was used.  Both versions are proof-only.
