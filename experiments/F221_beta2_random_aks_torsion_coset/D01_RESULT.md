# F221-D01 result

## Status

Completed preregistered discovery run.  This is finite guidance only and is
not evidence for any asymptotic theorem.

The run enumerated 1,300 frozen balanced prime pairs and all local residues
for the fixed-shift scalar

\[
H_1(x)=(x+1)^N-x^N-1.
\]

Observed ranges were:

- maximum local root ratio modulo `p`: `0.1553398058252427`;
- maximum local root ratio modulo `q`: `0.10218978102189781`;
- maximum exact CRT XOR probability: `0.22578130536460916`;
- minimum exact CRT XOR probability: `0.0010075846403807584`.

The largest XOR instance was `p=103, q=137`, with 16 and 14 local roots.
The variation is enough to reject treating F221's random-scale coset bound
as if it automatically covered fixed `a=1`.  No unbounded claim follows.

## Artifacts

- preregistration SHA-256:
  `4f1e5b72d2db256d820cb2859fb47cec60621600ce02eaf65350824af84ad315`;
- source SHA-256:
  `acd30bd29121536fbaf0e9f0837c3c36349a495f11d8faab3c617ec04e6c5f72`;
- run-log SHA-256:
  `239e063ac41cd3544969d0e96cdaffc7a0a093c8665189457055ed4486409e07`;
- output SHA-256:
  `239e063ac41cd3544969d0e96cdaffc7a0a093c8665189457055ed4486409e07`.

The log and JSON hashes agree because the program prints the same canonical
JSON that it writes to the output file.
