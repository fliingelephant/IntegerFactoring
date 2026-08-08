# F107 — origin of the F98 cross-trajectory rows

## Question

Are the cross-trajectory prime rows in the 166-column F98 circuit inherited
from a public integer base shared by the trajectories, or do they arise from
new gcd coincidences between canonical integer representatives?

## Classification

Each selected feedback record has an oriented trajectory key and the exact
public base integers `u,v`. A prime-row occurrence is base-inherited across
two trajectory keys only if the two keys share an exact base integer that is
divisible by that prime. Otherwise their shared prime is a metric
cross-trajectory overlap. This definition is deliberately strict. Merely
sharing a modular subgroup or sharing a base not divisible by the prime does
not explain the integer gcd.

Classify every cross-trajectory row by all unordered pairs of trajectory keys
in its support. Measure binary rank and column connectivity for rows with at
least one metric cross pair and for rows whose every cross pair is explained
by a shared divisible base.

Also reconstruct exact zero-carry chains inside one oriented trajectory. Keep
these separate from cross-trajectory base inheritance.

## Falsifiers

The scalable structural explanation is strong only if base-inherited and
carry-chain rows supply nearly all rank. It is weak if metric cross rows alone
carry most rank or global connectivity.

## Scope

This is a factor-assisted diagnosis of one fixed circuit. A metric label does
not prove randomness, rarity, or an asymptotic birthday law.
