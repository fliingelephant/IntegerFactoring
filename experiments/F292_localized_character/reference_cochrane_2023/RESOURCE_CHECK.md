# Resource check before PDF rendering

The official PDF is a born-digital, unencrypted 12-page file of 242,664
bytes. The configured renderer is pymupdf4llm 1.27.2.3.

At 2026-09-07 03:39 local time, the 16 GB host reported load averages 2.04,
2.15, and 2.08, 72% free memory, no swap activity, and no numerical job.
One macOS suggestion service occupied approximately one CPU core.

The render uses one Python process. For this PDF, estimated runtime is below
30 seconds and estimated peak memory is below 256 MB.
