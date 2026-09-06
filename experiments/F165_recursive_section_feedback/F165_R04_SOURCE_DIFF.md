# F165-R04 source repair provenance

R04 starts from the byte-identical mathematical source used by R03:

- R03 source path:
  `f165_r02_v2_blind_reconstruct.py`
- R03 source SHA-256:
  `d6b0dc314c3ab4108218acc709b7a04a0b1e040a6213497a41b6356c9a09d6c1`
- R04 source path:
  `f165_r04_v2_blind_reconstruct.py`
- R04 source SHA-256:
  `a3b1a94440d3e6e580bccc6efe189a73a86adc366c4e617acc06a5a56377b42f`

The sole semantic repair is to execute both frozen feedback levels for every
corpus input, even after a certificate is known. The related accounting now
includes every executed input. Repeated rediscovery of an existing certificate
is canonicalized, and the earliest success stage is preserved. The remaining
two changes are run identifiers in the docstring and output schema.

The complete source diff is:

```diff
--- f165_r02_v2_blind_reconstruct.py
+++ f165_r04_v2_blind_reconstruct.py
@@ -1,5 +1,5 @@
 #!/usr/bin/env python3
-"""Statement-only reconstruction of the F165-R02 V2 finite replay.
+"""Statement-only reconstruction of the F165-R04 V2 finite replay.
 
 This program deliberately uses only Python's standard library.  It constructs
 the public corpus, analyzes each N without receiving its factors, and emits a
@@ -637,9 +637,6 @@
         "certificates": list(certificates),
         "success_stage": "base" if certificates else None,
     }
-    if certificates:
-        return result
-
     for level in (1, 2):
         old_decode = decoded
         scan = feedback_scan(
@@ -670,10 +667,11 @@
             "certificates": level_certificates,
         }
         result["levels"].append(level_result)
-        result["certificates"].extend(level_certificates)
-        if level_certificates:
+        for certificate in level_certificates:
+            if certificate not in result["certificates"]:
+                result["certificates"].append(certificate)
+        if level_certificates and result["success_stage"] is None:
             result["success_stage"] = f"level_{level}"
-            return result
     return result
 
 
@@ -851,9 +849,9 @@
         },
     }
     aggregates: dict[int, dict[str, int]] = {}
-    if all(len(result["levels"]) == 2 for result in base_null):
+    if all(len(result["levels"]) == 2 for result in public_results):
         for level in (1, 2):
-            aggregates[level] = aggregate_level(base_null, level)
+            aggregates[level] = aggregate_level(public_results, level)
             for key, expected in expected_aggregates[level].items():
                 add_mismatch(
                     mismatches,
@@ -864,16 +862,16 @@
     else:
         add_mismatch(
             mismatches,
-            "two_feedback_levels_for_each_base_null_input",
-            63,
-            sum(len(result["levels"]) == 2 for result in base_null),
+            "two_feedback_levels_for_each_input",
+            64,
+            sum(len(result["levels"]) == 2 for result in public_results),
         )
 
     refinements: dict[int, dict[str, Any] | None] = {}
-    if all(len(result["levels"]) == 2 for result in base_null):
+    if all(len(result["levels"]) == 2 for result in public_results):
         refinements = {
-            1: first_refinement(base_null, 1),
-            2: first_refinement(base_null, 2),
+            1: first_refinement(public_results, 1),
+            2: first_refinement(public_results, 2),
         }
         add_mismatch(
             mismatches,
@@ -945,7 +943,7 @@
         )
 
     payload = {
-        "schema": "F165-R02-V2-blind-reconstruction-1",
+        "schema": "F165-R04-V2-blind-reconstruction-1",
         "replay_status": "FAIL" if mismatches else "STATED_FINITE_CLAIMS_MATCH",
         "final_verdict": (
             "FAIL"
```

No corpus construction, relation generation, ledger rule, decoder arithmetic,
Gaussian elimination, subset order, hash encoding, claimed expectation, or
fixed-depth proof changed. R03 source, runner, log, output, and
`BLIND_RECONSTRUCTION_FAILED.md` remain untouched.
