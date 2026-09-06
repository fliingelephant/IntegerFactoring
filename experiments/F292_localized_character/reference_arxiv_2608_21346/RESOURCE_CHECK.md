# Resource check before PDF rendering

The source PDF is a born-digital, unencrypted 32-page file of 480,852 bytes.
The configured renderer is pymupdf4llm 1.27.2.3.

At 2026-09-07 02:42 local time, the 16 GB host reported load averages 2.05,
2.08, and 2.07, 74% free memory, no swap activity, and no numerical job.
One macOS suggestion service occupied approximately one CPU core.

The render uses one Python process. For this PDF, estimated runtime is below
30 seconds and estimated peak memory is below 256 MB.
