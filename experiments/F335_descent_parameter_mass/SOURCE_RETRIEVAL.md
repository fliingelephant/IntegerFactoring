# F335 source retrieval

**Family:** route:F31

The unchanged `how-to-download-ref` workflow was run from its resolved local
path at `.agents/skills/how-to-download-ref`. The requested manifest contained
only arXiv `2210.14095` and DOI `10.1215/ijm/1255631807`. Both identities were
absent before retrieval. The renderer used the same `python3` interpreter as
the other helpers and `pymupdf4llm 1.27.2.3`.

The first sandboxed fetch attempt failed at DNS resolution. The authorized
retry through the same helper retrieved metadata and the PDF for arXiv
`2210.14095`. It produced
`.knowledge/2210.14095_on-the-distribution-of-partial-quotients-of-reduced-fraction.md`
with `full_text: yes` and cite key `aistleitner_2022_distribution`.

The same helper retrieved metadata for DOI
`10.1215/ijm/1255631807`, but every documented PDF tier returned `miss`.
The KB therefore contains `.knowledge/10-1215-ijm-1255631807.md` with
`full_text: no` and cite key `rosser_1962_approximate`. No Playwright install,
Sci-Hub call, or alternate download workflow was used. The route owner and
root consulted the public Rosser--Schoenfeld scan separately for Corollary 3,
formula (3.8); this packet does not claim that scan as locally cached full
text.

The helper regenerated `INDEX.md` with the unchanged title `Integer Factoring
references` and source note `Research literature and full text.` Explicit
arXiv and DOI identity checks then found the expected Markdown entries, and
the final `kb_doctor` result was `0 FAIL, 0 WARN`. The complete helper output,
including the initial network failure and the DOI PDF miss, is retained in
`reference_skill_run.log`.

`REFERENCE_SHA256SUMS.txt` records SHA-256 for both metadata files, the arXiv
PDF, both rendered Markdown entries, and all 211 extracted arXiv figure assets.
The principal asset hashes are:

- arXiv metadata: `4bdd3e1b7f827a523281fccd14b0fb1f3c792165eecdb95471a4c30360afc69e`;
- arXiv PDF: `470aadbd16b496789f6b3269ec0fa90db4955a4d5507207675ff15124a0841f8`;
- arXiv Markdown: `8781799bcee14aadd67e5384df687781f50dd0d7679f94dfce7b57fbea00fe13`;
- DOI metadata: `1113b5278d4d2a9ab7127c8cef53d3c50727735dd9b2237de7063474f804e4e9`;
- DOI metadata-only Markdown: `da531e08a13225dbea5570920e13371924568ddc0b3ebe301844d052377ec575`.

The Aistleitner--Borda--Hauke paper is related background for fixed-denominator
continued-fraction statistics. The frozen F335 proof is elementary and does
not depend on it. The Rosser--Schoenfeld prime-interval estimate is the declared
external dependency used only for the infinite balanced-input family.
