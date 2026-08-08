# F122 — the stable private row does not block the fixed source

## Verdict

**Prefix certificate. The registered no-stop run did not finish.**

The fixed source factors

```text
N = 2,000,887,089,301
  = 1,000,289 * 2,000,309
```

before feedback. The universe-private seed-2 row remains absent from every
dependency. Other columns supply both direct extraction and a non-global
root.

The feedback gate is closed on this input.

## Public direct certificate

The fixed all-pairs menu contains pair `(2,12)`, orientation
`[2*12^e]_N`, and exponent `e=1012 <= 41^2`. It gives

```text
c = [2*12^1012]_N = 1,407,720,713,745,
w = c^(-1) mod N  = 1,483,206,522,841,
gcd(c-w,N)        = 1,000,289,
N / gcd(c-w,N)    = 2,000,309.
```

This word and screen are fixed from `N` alone. Endpoint factorization did not
select them. The registered source reached this event at attempt 166,901,
inside all-pairs menu index 9. If the residue had occurred earlier, the same
screen would already have run. Thus first-occurrence deduplication cannot
remove the factor certificate.

This direct event is sufficient to certify success of the complete source.
Every later source position is irrelevant to that conclusion.

## Exact-root prefix evidence

The stopped retry reached 1,278,360 of 2,758,520 attempt positions and 340 of
780 all-pairs menus. Its globally exact-value-deduplicated prefix had

```text
columns                         704,274
rank                            617,511
kernel nullity                   86,763
non-global fundamental roots     42,071
proper direct screens                  3
```

The first non-global fundamental root appeared at column 72,648:

```text
x = 721,509,455,990,
x^2 = 1 mod N,
gcd(x-1,N) = 1,000,289,
gcd(x+1,N) = 2,000,309.
```

The hidden-prime rows used for this diagnostic were factor-assisted. This
root record is therefore finite discovery evidence, not a recovered public
support. The public direct certificate above does not have that limitation.

An old dependency extends by zero coefficients when new exact columns are
appended. Its exact root does not change. Therefore the prefix proves that
the complete exact matrix has `CLOSE` and a nonzero `ROOT` image, even though
the no-stop terminal matrix was not materialized.

## Private-column separation

The seed-2 exact value is

```text
N+1 = 2 * 1,000,443,544,651.
```

F120 proves that its large prime row is private against the complete
canonical exact-value universe. Its column coefficient is zero in every
dependency, not only in the computed prefix. Both stopped checkpoints also
observed row degree one and zero fundamental dependencies containing the
private column.

Thus this input separates the three proposed gates:

- `REUSE` fails for the protected row;
- `CLOSE` holds among other columns;
- `ROOT` holds among other columns.

Universal row reuse is not necessary for this source to factor.

## Resource outcome

The first run was interrupted by a parent-task continuation. Its exact
checkpoint is preserved.

The unchanged retry reached 992,903,168 bytes of resident memory. The user
reported a computer memory problem. The parent stopped the run to avoid more
pressure. Its exact checkpoint and interrupt log are preserved.

The no-stop design stored a growing exact-value set and a large elimination
state after success was already known. A further retry would add resource
cost but no evidence needed for the feedback decision. Future null searches
must stop on the first direct factor or non-global root. Only a case with no
success must complete the full source.

## Scope

F122 is one finite input. It proves no all-input source law and no feedback
progress law. It shows only that the F120 stable-private witness is not a
valid feedback test: the fixed pre-feedback source already factors it.
