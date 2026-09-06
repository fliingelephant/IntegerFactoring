# Pre-freeze public synthetic throughput benchmark

The authoritative target binary was compiled with the runner flags:

```text
/usr/bin/g++ -std=c++17 -O3 -DNDEBUG -pthread symbolic_search.cpp -o symbolic_search
```

`--benchmark` uses one fixed public synthetic pair

```text
p=2^60-93, q=2^60-33.
```

It does not generate, write, or summarize a discovery or held-out cohort. It
runs the maximum 120-bit source window only to count grammar throughput.

Three valid runs reported:

```text
atoms=123481 seconds=4.936830 atoms_per_second=25012.203210
atoms=123481 seconds=4.267517 atoms_per_second=28935.092159
atoms=123481 seconds=4.953039 atoms_per_second=24930.349709
```

The last run polled the target process with `ps` and measured peak RSS
`16136 KiB`. An earlier attempt to use `/usr/bin/time -v` failed with status
127 because that executable is absent. A first `/proc` poll had a quoting
defect and reported zero RSS. Neither failed monitor changed the source or
produced mathematical cohort output.

Using the slowest valid time, `7040*4.953039/8 = 4358.7` seconds, or 72.6
minutes, under ideal eight-thread scaling. The frozen 1.2–3 hour forecast
allows for shared-host load and imperfect scaling. Eight measured worker
footprints plus the approximately 40 MiB result array are below 200 MiB;
the declared peak envelope is 512 MiB.
