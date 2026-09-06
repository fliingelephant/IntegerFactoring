# F289 affine-node branch pilot resource estimate

This continuation uses one Python process and a 30-second source alarm.

Before implementation, the 16 GB host reported load averages 2.35, 2.22, and
2.14, 72% free memory, no swap activity, and no active numerical job.

The full-union baseline streams candidate points and retains only one optimum
per fixed normal. It does not materialize the hull. The deepest planned tree
has approximately \(2^{10}\) leaves, and the heap stores only live node
bounds. Estimated peak memory is below 128 MB.

The \(B=2^8\) scale runs first. The \(B=2^{10}\) and \(B=2^{12}\) scales run
only if that pilot finishes within 5 seconds. Extension to \(B=2^{14}\) and
\(B=2^{16}\) has additional elapsed-time and measured-RSS gates. At each
scale, the largest tested modulus is the largest power of two not exceeding
\(16\lfloor\sqrt N\rfloor\).
