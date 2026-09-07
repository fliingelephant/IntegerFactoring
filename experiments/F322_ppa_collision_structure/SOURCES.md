# F322 source preparation

**Status:** primary full text ready. This file records retrieval and
navigation only. It makes no mathematical claim for F322.

## Primary paper

- Emil Jeřábek, *Integer factoring and modular square roots*.
- arXiv:1207.5220.
- DOI: 10.1016/j.jcss.2015.08.001.
- Generated citation key: jebek_2012_integer.
- Rendered full text:
  .knowledge/1207.5220_integer-factoring-and-modular-square-roots.md.
- Frontmatter status: full_text is yes.

Useful navigation anchors in the rendered paper are:

- Section 3, “Search complexity of factoring”;
- Theorem 3.4, FacRoot in PPA;
- Theorem 3.16, Root in FP[FacRoot] and hence PPA;
- Section 4.2, “Explicit algorithm”;
- Lemma 4.8, related PPA problems; and
- Lemma 4.10, QuadRec in PPA.

These anchors are for later first-principles reading. No theorem is imported
or interpreted here.

## Exact skill workflow

The vendored how-to-download-ref skill resolved to
/Users/zhou/autoresearch/IntegerFactoring/skills/how-to-download-ref.
The same python3 provided pymupdf4llm 1.27.2.3. The preflight found a
16 GiB host, 67 percent free memory, zero swap, and load averages
1.97, 1.97, 1.92.

The pre-fetch identity check returned missing. The first sandboxed helper
call reported DNS failure. The same documented helper was rerun with approved
network access; it handled one HTTP 429 retry and fetched both metadata and
the PDF. Rendering used --only-missing, so existing papers were skipped.

The generated Semantic Scholar BibTeX lacked an arXiv or DOI identity field.
The new bibliography entry was explicitly repaired with the already-fetched
eprint, archivePrefix, and DOI values. No helper or generated paper body was
edited. INDEX was regenerated with its canonical title
“Integer Factoring references” and source note
“Research literature and full text.” The final checker reports:

    0 FAIL, 0 WARN

The complete command and repair log is skill_run.log.

## Asset hashes

| SHA-256 | Asset |
| --- | --- |
| b3eeef4785013552aa222ff40cfc69cc656dde48fe431c2b493fac25ed9cb7ac | .knowledge/.raw/arxiv/1207.5220.json |
| 83df89e189a4a2956221eae66647638cc105f39171cf667cf3924c74e4f3d01b | .knowledge/.raw/arxiv/1207.5220.pdf |
| be175015a8654e439c54b9d2015473eecf44e22880ba2ec63c57f508772e5790 | .knowledge/1207.5220_integer-factoring-and-modular-square-roots.md |
| 11995b1eaf75a30a003a1f1f54f9c60a3092a4a52d039a60ac1edfb906002138 | .knowledge/references.bib after append and identity repair |
| 2169d6c426ac556daf18d4622e47a4ebf57d82bb965e3d1e31368051f824683d | .knowledge/INDEX.md after canonical regeneration |
| a8c1eba9fc217fb0f80ebf82d572ea05b1c51cfcb7e01b2842aa0cb0ff30f011 | experiments/F322_ppa_collision_structure/skill_run.log |

## Existing repository navigation

Rust-reader searches for the exact names Papadimitriou,
Buresh-Oppenheim, WEAKPIGEON, Jeřábek, and “parity principle” found
no existing dedicated record. A broad PPA substring search is not useful
because it also matches words such as kappa.

The closest scoped heads are:

- P206, “modular collision energy is the exact difference-word source,”
  in PROVED.md; it is a conditional Las Vegas source theorem, not an
  all-input algorithm.
- P210, “the square baseline strips all cross-sign support, but the natural
  collision sources stay generic,” in PROVED.md; it is a conditional
  bridge for distinct odd semiprimes.
- P216, “the complete tailored negative-Pell component bank need not contain
  a square dependency,” in PROVED.md; it is one exact Pell-source
  counterexample, not a probability or factoring obstruction.
- X01, “generic exact linear compression of arbitrary square classes,” in
  FAILED.md; its promoted part is a narrow linear-rank obstruction.

No relation from these records to the paper’s PPA or WeakPigeon reductions
is asserted. They are only local navigation points for later comparison.
