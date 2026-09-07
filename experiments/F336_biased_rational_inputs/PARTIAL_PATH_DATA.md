# Existing data for cap-specific partial-path efficiency

**Family:** route:F31

This note maps retained F329, F331, and F332 fields. It does not change a
protocol, add a trial, pool inputs into an asymptotic estimate, or infer
anything from a finite zero.

## Exact data map

| Packet | Input and independence law | Original caps | First verified factor information | Cumulative charged cost and failures | Sufficiency |
|---|---|---|---|---|---|
| F329 | Each N has 16 independently generated conditional unit-square inputs. Rank-L has one path per square. Uniform-center and lazy matching have four independently seeded inner replicates per square. Baseline and static-screen views are paired views of the same path. | Pilot: 4, 16, 64, 256 F calls. Scale: 16, 64, 256, 1024 F calls. | Every cap view has status, endpoint.step, endpoint.first_hit_type, endpoint_type, exact decoder output, and direct_factor, screen_factor, root_factor, root_decoding_failure, and factor_success flags. | Every cap view has a frozen state and a complete costs vector. It includes F calls, floor-sum calls and Euclid iterations, all gcd classes, inversions, matching draws/rejections/fair bits, accepted-input generation cost, and charged wall time. Failed and censored attempts stay in every numerator. | Yes, for every recorded cap. |
| F331 | Eight fixed F328 moduli have 32 independently sampled hidden residues each. The three policies share each initial residue for a paired comparison and have separate policy seeds. | One controller cap: 16 rounds, each with one 8-F-call probe. | Each attempt stops at its first controller factor/root, outer root-decoding result, empty-pool failure, or round censor. The aggregate retains status, output_type, accepted_factor, factor_success, rounds, F calls, and the final history outcome. | total_costs is cumulative through first termination or all 16 rounds. It includes every failed attempt and every unselected proposal. | Yes at the sole recorded 16-round cap. It is not sufficient for new earlier round caps because histories do not retain all cumulative randomness and cost counters at each round boundary. |
| F332 | For each selected N there is one deterministic public input a=-1 and one path per method. There are no sampled parameters or inner coins. | Initial cap 8,192; selected fresh reruns at 262,144. Reflection caps fine F calls; adjacent caps blocks, so equal numbers cover different path lengths. | Each method result has completed/censored status, terminal output and branch when present, fine-call or block count, and operation counts. | Final or censored gcd and inversion counts are retained. | No empirical cost-per-success denominator exists for a fixed N. Repeated independently sampled attempts are the missing field. The two cap files are reruns of the same deterministic path, not replicates. |

### Generation and path factors

F329 keeps nonunit outer-generation draws in a separate generation_factors
array. They are not included in the conditional trajectory tables below.
There were two such pilot events and one scale event. Each accepted trajectory
still charges its own generation gcd and fair bits. Within a path, the retained
flags distinguish a direct fixed-point factor, a static edge-screen factor,
and a factor obtained by the outer hidden-root gcd. Thus a
generation-inclusive view can be formed by adding the separate terminal
generation events without assigning later path cost to them.

F331 distinguishes initial_generation_factor, direct_path_factor,
multiplier_generation_factor, proposal_screen_factor,
proposal_ordinary_square_root_outer_factor, outer root-decoding failure, and
round_cap_censor. The retained scale sample had no initial-generation factor.
Uniform policy's 23 factors comprise 6 direct path factors, 7 multiplier
generation factors, 1 proposal-screen factor, and 9 outer root factors.

F332 has no parameter generation. Its only possible factors are public path
outputs or the separately charged gcd between two returned roots. No retained
public run returned a root pair.

## F329 cap table

Each cell below is:

    factor successes / attempts / censors ; F calls per factor / total gcds per factor

The cost ratio divides the cumulative cost of all attempts, including failed
and censored attempts, by verified factor successes. A dash means that the
finite cell had no factor. These are descriptive pooled views of the named
finite datasets; the source JSON also retains every per-N row.

Pilot inputs are N=209, 1333, and 10807:

| method/view | cap 4 | cap 16 | cap 64 | cap 256 |
|---|---|---|---|---|
| rank-L / baseline | 5/48/42; 37.6/38.8 | 30/48/16; 16.2/17.3 | 42/48/4; 23.0/24.0 | 46/48/0; 24.0/25.0 |
| rank-L / static | 18/48/29; 9.9/69.4 | 43/48/3; 7.7/54.3 | 46/48/0; 8.3/58.8 | 46/48/0; 8.3/58.8 |
| uniform-center / baseline | 46/192/146; 15.2/20.3 | 114/192/78; 17.3/19.9 | 174/192/18; 22.5/24.5 | 192/192/0; 24.3/26.2 |
| uniform-center / static | 121/192/71; 4.3/32.2 | 177/192/15; 5.6/40.7 | 192/192/0; 6.1/44.0 | 192/192/0; 6.1/44.0 |
| lazy-uniform / baseline | 47/192/143; 15.0/20.0 | 99/192/90; 20.7/23.6 | 167/192/21; 24.8/27.0 | 187/192/1; 27.9/29.9 |
| lazy-uniform / static | 121/192/70; 4.3/32.2 | 173/192/18; 5.7/41.1 | 191/192/0; 6.2/44.4 | 191/192/0; 6.2/44.4 |

Scale inputs are the two retained F328 moduli at 20, 28, and 36 bits:

| method/view | cap 16 | cap 64 | cap 256 | cap 1024 |
|---|---|---|---|---|
| rank-L / baseline | 0/96/96; — | 3/96/93; 2013.0/2014.0 | 14/96/82; 1631.4/1632.4 | 36/96/60; 2057.4/2058.4 |
| rank-L / static | 6/96/90; 248.8/1741.8 | 18/96/78; 300.9/2106.4 | 37/96/59; 489.5/3426.8 | 57/96/39; 932.2/6525.7 |
| uniform-center / baseline | 5/384/379; 1219.2/1297.0 | 17/384/367; 1412.5/1436.1 | 59/384/325; 1530.4/1537.9 | 135/384/249; 2241.4/2245.2 |
| uniform-center / static | 14/384/370; 431.3/3046.8 | 64/384/320; 352.6/2474.6 | 143/384/241; 519.0/3636.2 | 200/384/184; 1164.5/8153.6 |
| lazy-uniform / baseline | 9/384/375; 675.9/719.6 | 28/384/356; 840.0/854.7 | 59/384/325; 1503.6/1511.1 | 131/384/253; 2333.5/2337.4 |
| lazy-uniform / static | 28/384/356; 212.9/1504.0 | 79/384/305; 273.7/1921.2 | 146/384/238; 491.6/3444.4 | 212/384/172; 1077.0/7541.0 |

The same retained summaries include floor-sum Euclid iterations, inversions,
random bits, sparse-pool size, and charged time per factor. No new cap can be
inserted without a new run because only the four named prefix snapshots were
serialized.

## F331 sole-cap table

The 256 attempts per policy span two moduli at each of 20, 28, 36, and 44
bits. All costs include failures, root-decoding failures, unselected
proposals, and round censors.

| policy | factors/attempts | round censors | F calls/factor | gcds/factor | floor Euclid iterations/factor | fair bits/factor |
|---|---:|---:|---:|---:|---:|---:|
| path | 16/256 | 233 | 1959.00 | 2708.00 | 840918.75 | 6007.69 |
| uniform | 23/256 | 228 | 1344.74 | 2529.65 | 592058.30 | 31927.83 |
| last | 15/256 | 241 | 2113.53 | 2130.93 | 936131.13 | 747.20 |

## Exact retained sources

| Packet | File | SHA256 |
|---|---|---|
| F329 | experiments/F329_random_center_paths/random_center_paths.py | 01b1ff6a1a02f0d36aff8cde7408866069f09c8554f280e8951564704459a325 |
| F329 | experiments/F329_random_center_paths/pilot_aggregate_output.json | 50eee8575d33951295a112abaabe9aaf2208ea52820c4e91b7f72b188b9d873d |
| F329 | experiments/F329_random_center_paths/scale_aggregate_output.json | 7de2d57a6264c931f3f0a3a06cfa8e0e281fd1d02a40116ac0e974b13b5912c2 |
| F331 | experiments/F331_square_input_feedback/square_input_feedback.py | 4c74e3070fed9d27d03a3fa9dd5de75e0b95997e51317733cc6b658901bda4ab |
| F331 | experiments/F331_square_input_feedback/aggregate_feedback.py | 70814b930ae9947a98ebe4b9c423a64b502e6610b82894210097915715d8ef49 |
| F331 | experiments/F331_square_input_feedback/aggregate_output.json | e6ba10d64e88e7031864904250e6284642f762cf062cd5d762fe4e4b32b2f8ac |
| F332 | experiments/F332_minus_one_paths/minus_one_paths.py | f77289e01e29a3a8df3e88a1c60230e10ef75d2b89c41874ae3821cc48e5f6ae |
| F332 | experiments/F332_minus_one_paths/aggregate_output.json | 4760eb4b4d46154297ddd1a0cb539df1dc3695d5aab88957f0d521e54eeb3396 |

F329 and F331 therefore suffice for exact finite cost-per-success
reconstruction at their original caps. F332 does not, because it has one
deterministic path per fixed input rather than repeated attempts from a stated
input or coin law.
