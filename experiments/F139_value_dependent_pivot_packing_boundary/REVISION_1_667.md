# F139 verifier revision 1

The first replay failed only at JSON serialization. The verifier now converts
the fixed `packed_carry` report field from a Sage `Integer` to a Python
`int`. No input, arithmetic check, expected value, or pass condition changed.
