# F289: support descent over a modular union

**Family:** route:F31

Status: exact finite pilot. This packet is not a proof of a general descent
law or a factoring complexity bound.

## Question and implementation

For \(M\) a power of two, the experiment uses

\[
S_{N,M}=\{(x,y)\in\mathbb Z_{>0}^2:xy\geq N,\ xy\equiv N\pmod M\}.
\]

For each public pair \((N,M)\), the source constructs the prescribed feasible
point \(P_0=(x_0,y_0)\) near \(\sqrt N\), sets
\(K=\max(x_0,y_0)\), enumerates the minimal feasible \(y\) for every eligible
\(x\leq K\), and adds every reflected coordinate pair \((y,x)\). It then:

- removes dominated points and collinear hull interiors with exact integer
  cross products;
- queries each vertex \(P=(x,y)\) for the minimum of \(yX+xY\) by binary
  search on monotone adjacent-edge signs;
- retains both endpoints of an optimal edge and selects the endpoint with the
  smaller product;
- asserts \(X_QY_Q\leq xy\), with equality exactly when \(Q=P\);
- precomputes successors, sinks, and step counts; and
- sums exact rational normal-cone lengths after intersection with
  \(1\leq a/b\leq2\).

The labelled cases use \(B=2^e\) for
\(e=8,10,12,14,16\). Their distinct prime labels are the first primes at or
above \(9B/8+2e+1\) and \(7B/4+3e+1\). This gives separated factors rather
than deliberately small gaps. The factors construct \(N\) and audit the four
factor points after each run. The hull, normals, support choices, successors,
and basins receive only \(N\) and \(M\).

## Aggregate exact results

Each row aggregates five semiprimes. Every modulus has 10 proper-factor sinks
and 10 trivial-factor sinks. The trivial-factor basin has zero length in the
chosen slope interval.

| \(M\) | Hull vertices | Moves | Moves with self-normal in \([1,2]\) | False sinks | Max steps | Mean direct proper-factor length | Mean proper-factor basin length | Mean gain |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 23,958 | 0 | 0 | 23,938 | 0 | 42389119/1163962800 | 42389119/1163962800 | 0 |
| 2 | 14,564 | 0 | 0 | 14,544 | 0 | 3173641/56456400 | 3173641/56456400 | 0 |
| 4 | 12,014 | 0 | 0 | 11,994 | 0 | 2136779/37348080 | 2136779/37348080 | 0 |
| 8 | 10,028 | 0 | 0 | 10,008 | 0 | 222011/2714250 | 222011/2714250 | 0 |
| 16 | 9,346 | 784 | 25 | 8,542 | 2 | 5272889/51570750 | 97890433/876702750 | 4/425 |
| 64 | 6,992 | 1,086 | 31 | 5,886 | 2 | 3989266/22952475 | 52200742/237175575 | 452/9765 |
| 256 | 4,982 | 852 | 32 | 4,110 | 3 | 82611330647/324897704781 | 3736159915949/10989187073475 | 642652/7497425 |

The source asserts that every vertex is self-fixed for
\(M=1,2,4,8\). All four controls passed. Every one of the 15 cases with
\(M=16,64,256\) contained an actual move, so the union can escape the fixed
affine-lattice behavior in this finite range. Seven of those 15 cases had a
strictly larger proper-factor basin; movement alone did not guarantee basin
gain.

## Compact move certificates

All three certificates use

\[
N=147053=307\cdot479,
\]

where the factorization is an offline label. Each displayed normal is the
source point's public self-normal and has slope in \([1,2]\). The support
minimum was unique in all three cases.

| \(M\) | Source \(P\), \(xy\) | Target \(Q\), \(uv\) | \(y u+x v\) versus \(2xy\) | Reflected \(2P-Q\), product | Reflected residue versus \(N\bmod M\) |
|---:|---|---|---:|---|---:|
| 16 | (317,465), 147405 | (307,479), 147053 | 294598 < 294810 | (327,451), 147477 | 5 != 13 |
| 64 | (325,457), 148525 | (307,479), 147053 | 295974 < 297050 | (343,435), 149205 | 21 != 45 |
| 256 | (279,539), 150381 | (307,479), 147053 | 299114 < 300762 | (251,599), 150349 | 77 != 109 |

In each row, the reflected point remains positive and its product remains at
least \(N\), but its product has the wrong residue. This is the exact finite
failure of the reflection-closure step used by the affine-lattice control.

## Reproducibility and scope

The retained artifacts are:

- support_union.py: exact source with a 60-second alarm;
- output.json: all 35 compact case summaries, exact aggregate fractions,
  and the three move certificates;
- run.log: phase timings and resource measurements; and
- RESOURCE_ESTIMATE.md: the pre-run resource check and scaling rule.

The run used one process, completed all extensions in 0.774 seconds, and
reported peak RSS 74,858,496 bytes. Enumeration is linear in the numerical
cutoff \(K\); this pilot makes no polynomial-in-\(\log N\) runtime claim.
