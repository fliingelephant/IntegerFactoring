# F219 V1 scope correction

V1 had the following authoritative hashes:

- `STATEMENT.md`: `429883addb3c2bef03c0870777d03d8b2981341bc780dada61298bb4aa5f7855`
- `PROOF.md`: `87d2940d9f2fc0522308b812063b3ead9f3cf9db75adc3629e1195da8af9bb3e`
- `SELF_AUDIT.md`: `03263e5fec468dc44beb870787a12f81be305e9c2db44c7ebc246c7df7139e30`
- `RESULT.md`: `ae97e00d9e6d01fe31eb049d181393a0eda0ee5942297ad4d39a060b030eb3d8`

V1 correctly computed the exact probability `L_s/L_t` of sampling the true
refinement. It then described `L_t/L_s` as the expected trial count of the
whole accepted-factor algorithm. That scope was too strong. A wrong
refinement can fortuitously return a verified factor, so the actual stopping
time can be smaller.

V2 makes the exact statement:

- the waiting time to the true refinement is geometric with mean
  `L_t/L_s`;
- the waiting time to any verified factor is at most that true-hit waiting
  time;
- the cost cancellation is exact for the certified true-hit route and is
  not a lower bound against off-class factor events.
