# F224-D02 result

## Execution

The approved D02 wrapper completed successfully.

- output rows: 480 data rows plus one header;
- real time: 3.69 seconds;
- user time: 3.69 seconds;
- system time: 0.00 seconds;
- output SHA-256:
  `453ba8bbac8e92f38b78651e06c7f22d07f68356e4b3625f473730e01cd15d42`;
- log SHA-256:
  `de3ac3dc27d167caf790fef37b109c3af0d3e83d840e1fb2efdbb1fc7c686218`.

As preregistered, shell `time -p` gives no peak-RSS field.  The 2-GiB
virtual-memory limit was enforced.

## Frozen statistic

Across all rows, the AP cells contained 11,767,411 off-target integers.
Only 197 were exclusive local roots.  They occurred in 115 of 480 rows.
No row had more than five exclusive roots.  The largest row fraction was
`1/77`, at the smallest tested scale.

Every row contained the exact candidate exactly once.  Every row's five
outcome counts summed to its AP population.  No row had a shift which was
a scalar root in both hidden fields.

Near the preregistered capacity scale `L*d/p in [1/2,2]`, there were 104
rows.  Thirteen had a positive off-target count.  The aggregate was 15
exclusive roots among 933,751 off-target integers, a fraction
`1.60642398e-5`.

Grouped by factor bit scale, the aggregate off-target fractions were:

```text
b=12: 9.9320969e-4
b=14: 2.4397914e-4
b=16: 5.6534747e-5
b=18: 1.2306490e-5
b=20: 3.9945640e-6
```

The finite trend supports obstruction guidance, not a positive density
conjecture: the number of off-target roots stayed bounded while the AP
population grew.  The symbolic F224 bound, not this run, supplies the
unbounded theorem.
