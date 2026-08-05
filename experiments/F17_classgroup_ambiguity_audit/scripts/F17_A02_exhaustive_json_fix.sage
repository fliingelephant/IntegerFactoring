"""Rerun F17_A01 with a JSON encoder that accepts Sage Integer objects.

F17_A01 is retained byte-for-byte as the exact failed source.  This wrapper
loads all of its definitions without executing its final call, changes only
the JSON serializer, assigns the new run ID, and executes the same checks.
"""

from json import dump as standard_dump
from pathlib import Path
from sys import argv


source_path = Path(__file__).with_name("F17_A01_exhaustive.sage")
source = source_path.read_text()
trailer = "\nrun()\n"
assert source.endswith(trailer)

namespace = {"__file__": str(source_path), "__name__": "F17_A01_definitions"}
exec(compile(source[: -len(trailer)], str(source_path), "exec"), namespace)


def sage_integer_dump(value, handle, **kwargs):
    return standard_dump(value, handle, default=int, **kwargs)


namespace["dump"] = sage_integer_dump
namespace["RUN"] = "F17_A02"
namespace["argv"] = [argv[0], argv[1]]
namespace["run"]()
