# Resource check before PDF rendering

The two born-digital, unencrypted PDFs contain 29 and 16 pages and total
738,549 bytes. The configured renderer is pymupdf4llm 1.27.2.3.

At 2026-09-07 04:06 local time, the 16 GB host reported load averages 2.88,
2.49, and 2.19, 73% free memory, no swap activity, and no numerical job.
One macOS suggestion service occupied approximately one CPU core.

Rendering uses one Python process. Estimated total runtime is below 30
seconds and estimated peak memory is below 300 MB.
