# F140-D01 third authoritative-run failure

The corrected JSON run returned no paths.  Inspection of Sage's generated
Python source found that the `.sage` preparser had changed each Python
bitwise-XOR operator `^` to exponentiation `**`.  Consequently every parity
vector stayed zero and every starting column was rejected as dependent.

The output hash
`dce82241c0acf634ace5bf3f0b1c3e78c778af11db45bb6e1914c23bb4cb78e4`
is preserved as a failed logical run.  It is not evidence that paths are
absent.

The next source uses `operator.xor`, which the Sage preparser does not alter.
It also hashes the registered `.sage` source instead of Sage's generated
`.sage.py` file.  No corpus or path criterion changes.
