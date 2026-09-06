# F130 hostile audit — PASS AS CLAIMED

The proof-only construction passed a hostile audit. No counterexample was
found to its definition, termination, or
\(2^{O((\log n)^4)}\) bit-complexity bound. It does not prove factoring
success.

The audit checked the following points.

1. Named blocks always remain divisors of the fixed initial endpoint
   product. Novel decoder blocks never enter the word grammar.
2. Full multiplicity-aware refinement handles cases such as \(6\) versus
   \(12\). Perfect-power normalization makes every strict change split an
   old block into at least two descendants, so the named block count grows.
3. The product of the named blocks divides \(A_0\). This bounds the stage
   count by \(2^{O((\log n)^2)}\).
4. Each frozen menu, the full transcript, every refinement, and the final
   decoder have size and cost \(2^{O((\log n)^4)}\).
5. Residue deduplication is safe inside one frozen stage. Endpoint insertion
   correctly precedes exact-value deduplication.
6. Equal exact values add only a global-root duplicate direction. Their
   deletion preserves the normalized-root image.
7. Old dependencies survive every later append. One complete final P66
   decode is therefore sufficient.
8. The preprocessing scope includes odd nonsquarefree inputs. Exact perfect
   powers return a proper divisor before the core construction.

Two clarifications were applied after the audit. The source-inclusion text
now refers only to the actual enriched basis, not a hypothetical smaller
sub-bank basis. The perfect-power sentence now states the returned divisor
and recursion explicitly. These changes narrow or explain the existing
claim; they do not change the mathematics audited above.

Verdict: **PASS AS CLAIMED**. The exact unresolved gate is still an all-input
proof of a direct factor or a non-global final normalized-root image.

