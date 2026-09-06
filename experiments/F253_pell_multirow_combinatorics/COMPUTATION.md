# F253 finite computation record

## Resource check

Before the local search, the observed load averages were 2.47, 2.41, and
2.44. The virtual-memory report showed no throttled pages. Process listing
was denied by the local sandbox. The frozen job was a small, deterministic,
single-process search with an internal 60-second timeout, estimated below
50 MiB and ten seconds. Both runs finished in less than 0.03 seconds. Peak
RSS was not measured.

## V1

The V1 preregistration was frozen with SHA-256

d30118370efb835b4585743499c72629641e74cba5205d8da6d002b9eb7a3f65.

The source was then frozen with SHA-256

8c037e858a85366932d187bb303d1de204c41da6619621586494ceb73d450d2a.

V1 returned the \(N=143\) relation stored in V1_STDOUT.txt. Its normalized
root was mixed, but the same complete window had many earlier cleanup
factors. It was therefore not a screen-free P66 event.

## V2

After viewing V1, a separate V2 preregistration froze the sole change:
discard every modulus with any cleanup factor in its complete window. Its
SHA-256 was

a94f5ab913fbc8899d977b65b62c5fa58014121de84588bac2f2afe078bff617.

The exact V2 wrapper had SHA-256

3dfa9fa6d4d753f76618fb51e219c5aa681f7ae07a24a2518511b04be66d4f89.

V2 returned the \(N=4331\) relation stored in V2_STDOUT.txt. It had no
cleanup factor in the full frozen window. Its normalized root was global.

The V2 wrapper was intentionally minimal and used the absolute frozen path
/private/tmp/pell_orbit_circuit_search.py. The durable packet preserves the
exact bytes and hash, but the source was later moved into this directory.
For an exact replay, first copy search.py back to that temporary path, then
run search_v2.py. This path dependency is a reproducibility defect, not a
mathematical qualification.

The two stdout files were transcribed from the tool output after execution;
the run did not write frozen log files. Therefore their hashes attest only
to the durable transcription. The displayed \(N=4331\) arithmetic is
independently checked in PROOF.md.

## Finite scope

The computation used only \(D=2\), primes \(p\le500\), balanced pairs
\(p<q<2p\), and Pell indices through \(4\,\operatorname{bitlength}(N)\).
It supplies a counterexample to structural full rank in that finite source.
It gives no asymptotic frequency or success bound.

