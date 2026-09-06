import fractions
import json
import pathlib
import time


root = pathlib.Path(__file__).resolve().parent
started = time.monotonic()
with (root / "D07_OUTPUT.json").open() as source:
    d07 = json.load(source)

rows = []
for row in d07["rows"]:
    row = dict(row)
    row["success_rate"] = row["successes"] / row["denominator"]
    rows.append(row)
rows.sort(key=lambda row: fractions.Fraction(row["successes"], row["denominator"]))

minimum = rows[0]
result = {
    "summary": {
        "row_count": len(rows),
        "minimum_success_fraction": [minimum["successes"], minimum["denominator"]],
        "minimum_success_rate": minimum["success_rate"],
        "maximum_success_rate": max(row["success_rate"] for row in rows),
        "mean_success_rate": sum(row["success_rate"] for row in rows) / len(rows),
    },
    "rows": rows,
}
(root / "D08_OUTPUT.json").write_text(json.dumps(result, indent=2, sort_keys=True))
log = {
    "elapsed_seconds": time.monotonic() - started,
    "exit_code": 0,
    "source": "D07_OUTPUT.json",
    "stdout": json.dumps(result["summary"], indent=2, sort_keys=True),
}
(root / "logs" / "F226-D08.log").write_text(json.dumps(log, indent=2, sort_keys=True))
print(log["stdout"])
