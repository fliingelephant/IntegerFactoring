import json
import pathlib
import resource
import subprocess
import time


root = pathlib.Path(__file__).resolve().parent
log_dir = root / "logs"
log_dir.mkdir(exist_ok=True)

started = time.monotonic()
result = subprocess.run(
    ["/usr/local/bin/sage", "scan_binary_child_orbits.sage"],
    cwd=root,
    capture_output=True,
    text=True,
    timeout=300,
)
elapsed = time.monotonic() - started
usage = resource.getrusage(resource.RUSAGE_CHILDREN)

record = {
    "argv": ["/usr/local/bin/sage", "scan_binary_child_orbits.sage"],
    "elapsed_seconds": elapsed,
    "exit_code": result.returncode,
    "max_rss_platform_units": usage.ru_maxrss,
    "stderr": result.stderr,
    "stdout": result.stdout,
}
(log_dir / "F226-D01.log").write_text(json.dumps(record, indent=2, sort_keys=True))
print(json.dumps(record, indent=2, sort_keys=True))
raise SystemExit(result.returncode)
