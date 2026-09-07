# F326 source cache

## Lenstra fixed-dimensional integer programming

- H. W. Lenstra Jr., *Integer Programming with a Fixed Number of
  Variables*, Mathematics of Operations Research 8 (1983), 538-548.
- DOI: 10.1287/moor.8.4.538
- Cite key: lenstra_1983_integer
- Rendered full text:
  .knowledge/10-1287-moor-8-4-538.md
- Full-text status: yes (PDF render)
- Raw metadata:
  .knowledge/.raw/doi/10.1287-moor.8.4.538.json
- Raw PDF:
  .knowledge/.raw/doi/10.1287-moor.8.4.538.pdf

The unchanged how-to-download-ref skill was resolved to
/Users/zhou/autoresearch/IntegerFactoring/skills/how-to-download-ref.
Plain python3 used pymupdf4llm 1.27.2.3. The first sandboxed metadata
request recorded a DNS miss. The same documented fetch helper then succeeded
with authorized network access and obtained metadata and an open PDF through
Semantic Scholar. Rendering used --only-missing.

The generated Semantic Scholar BibTeX lacked a DOI field, so the first
read-only KB doctor correctly reported that the bibliography entry and
rendered DOI entry could not be matched. The DOI field
10.1287/moor.8.4.538 was added explicitly to this new bibliography entry;
the final doctor result is 0 FAIL, 0 WARN. No helper, generated paper body,
or existing citation was edited. INDEX.md retained the exact canonical
title “Integer Factoring references” and source note
“Research literature and full text.”

## Asset hashes

- metadata JSON:
  2ab395d8b2a14a6b8955eca3950b7b9e9e7c94cdf970629f9b081184231c3eee
- PDF:
  65a9ff4a23c3747cab12b6b277a64988aad95d83169c5babb9359917c1676569
- rendered Markdown:
  8a8c714d39881d383d217dae2b13ef405bc35f126053fd3d46b878fc5c641e8d
- bibliography after insertion:
  cc458d393de2046c7db358c23cefde2a696bed8362830f5580ae40fb8df1fa56
- regenerated index:
  e4ea011aa7398fad8289f43af3e403e3df509eb9e84dceca64736c32e76f4c37
- retained skill log:
  1d8309279edc70aaef05779dd0f51f6dbdba09a2c78ae9ccfec1d232dd441f64

This source supports the fixed-dimensional integer-programming dependency in
F325. The F326 implementation uses a reconstructed Euclidean floor-sum
algorithm and does not depend on the Lenstra cache.
