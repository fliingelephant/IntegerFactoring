# F165-R02 proof-hash provenance

This record explains the proof digest discrepancy discovered before R03 ran.

1. The proof was first created at the R01 path with first line
   `# F165-R01 V2 fixed-depth cost theorem: independent proof draft`.
   Its observed SHA-256 was
   `6684527b567bec8c2505dc4eb98aec6c2c6ee2c65ab021fe499e071b513f1a9d`.
2. Before R02 registration, `apply_patch` moved that proof to
   `F165_R02_V2_FIXED_DEPTH_PROOF_DRAFT.md` and changed only `R01` to `R02`
   in the first line. Its immediate and current observed SHA-256 is
   `ceb6e30d5759f21ad51dc4b97f41370b6fb7234546adeb1c9264653b34aa03aa`.
3. The current R02 file modification time is 2026-08-12 02:07:06 +0800. This
   predates the failed R02 launch. No proof edit occurred after the R02 freeze.
4. The digest preserved in the R02 registry row is
   `ceb6e30d5759f21ad51dc4eb98aec6c2c6ee2c65ab021fe499e071b513f1a9d`.
   It equals the first 24 hexadecimal digits of the observed R02 digest
   concatenated with the last 40 hexadecimal digits of the observed R01
   digest. It does not match any file digest observed during reconstruction.

The actual R02 proof file remains untouched. The original R01 text is exactly
reconstructible from it by changing only the first-line identifier from R02
back to R01; the known R01 digest above checks that reconstruction. No claimed
file preimage exists for the spliced registry digest. R03 therefore uses the
fresh path `F165_R03_V2_FIXED_DEPTH_PROOF_DRAFT.md` and a newly measured hash.
