# Arithmetic short paths and a rational block kernel

**Family:** route:F31

Status: author proofs with an exact finite pilot. The statement-only input is
frozen for fresh reconstruction. No result is promoted here. No expected QP
cost/success bound or external novelty is claimed.

## Mathematical advance

PROOF.md extends F328's endpoint count identity to every signed remainder
r=rep(a*t). It expresses 2Q(t)-t through at most 2|r|-1 public inverse-image
tests and proves |2Q(t)-t|<=|r|. This is useful symbolic structure near
small remainders; the existing floor-sum evaluator is already polynomial
in the input bit length. The argument includes repeated factors and does
not require a Jacobi promise for the identity itself.

For a=-1 and N=1 mod 4, the established Jeřábek / Buresh-Oppenheim interval
involution has a constant-matrix traversal. RATIONAL_PATHS.md goes further
for adjacent matching: even representatives turn the four signed branches
into blocks P and Q with positive primitive lifts

    P:(U,V)->(U+V,U),  Q:(U,V)->(V,U+V).

The reached path has a public kernel requiring one modular inverse per
moving block. This is an exact rational-tree correspondence, not only a
generic matrix observation. Its Q-then-P runs translate u to u+2. Finding
the first failed run condition is an explicit modular-inverse parity query
on consecutive integers. An efficient first-exit evaluator, or a separate
randomized proposal with a proved charged hitting probability, is still
missing. A known real continued-fraction target has not been identified.

The fixed a=-1 family has no hidden random root. A valid square root of -1
is kept separate from a verified factor. If N has a prime divisor 3 mod 4,
the root outcome is impossible, but no path-length bound follows.

## Exact initial pilot

The named source short_path_conditions.py independently compared direct
counts over every odd N<=101, every unit a, and every 1<=t<=(N-1)/2.
All 70,620 identities and discrepancy bounds passed across 2,106 parameter
pairs. Each of r=1 and r=-1 had 1,053 checked instances. These are exact
finite checks of the stated identity, not its unbounded proof.

All three retained F328 short paths were reproduced at their original
7,31,25 terminal F calls. Their nonunit factors were 13553,13553,12373.
The seven-call coordinates are

    0 -> -1 -> 3062970 -> 1531486 -> 765744
      -> 24720663 -> 12360336.

Three stages use F-negation followed by reflection, hence the monotone
map x->Q(x). Their defects are 2,2,9. The intervening scaled-inverse reset
has defect 16. Thus this short sample contains rank-compression descents
between inverse resets. Its occurrence probability is still unproved;
the sample does not justify selecting inputs using offline factors.

The pilot used 0.060839 seconds and 28,065,792 bytes peak RSS under the
documented 30-second / 256 MB boundary. Source, output, resource check, log,
and wrapper status are retained. The source SHA256 is
79a69f1a2c0b91092968a6312756be2eadd145d3ef812ae67f9756190a6d7f0f.

## Verification handoff

STATEMENT_ONLY.md is proof-free and self-contained with declared P246
dependency. Its frozen SHA256 is
a1b1b87a5b3d4ea524a24ec6bcfb3c24b666fdaace6ab115830d912a1ebd67bc.
It includes the exact count/affine/matrix identities, positive-block kernel,
guards, and inverse-parity translation condition. It excludes every
small-lift-size, hitting, novelty, or QP claim.

The proposed a=-1 numerical follow-on is being implemented separately as
F332. RATIONAL_PATHS.md preserves the root's N=61 candidate against a
2N lift-norm bound as pending that check. It is not a dependency of the
frozen statement. The author has not changed shared ledgers or Git state.
