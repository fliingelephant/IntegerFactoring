"""CLI regressions for stable evidence references. Uses isolated text fixtures."""

import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROUTE_ROW = "| F12 | Example route |\n"
RUN_ROW = "| F13-R01 | F12 | Example run |\n"
REGISTRY = (
    "# Registry\n\n| ID | Title |\n| --- | --- |\n"
    + ROUTE_ROW
    + "| F1 | Unrelated route |\n\n## Computation ledger\n\n"
    "| Run | Family | Purpose |\n| --- | --- | --- |\n"
    "| F12 | F1 | Same label in a different table |\n"
    + RUN_ROW
)
ROUTES = '''[[routes]]
id = "route:F12"
title = "Example route"
source = { path = "REGISTRY.md", table = "routes", key = "F12" }
'''
EXPERIMENTS = '''[[experiments]]
id = "experiment:F13_example"
path = "experiments/F13_example"
route_ids = ["route:F12"]
route_evidence = [
  { path = "REGISTRY.md", table = "runs", key = "F13-R01" },
  { path = "experiments/F13_example/RESULT.md", field = "Family" },
]
'''
PACKET = "# Example packet\n\n**Family:** F12.\n\n## Result\nFixture only.\n"


class StableReferenceTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(prefix="factoring-reference-test-")
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        (self.root / "research").mkdir()
        (self.root / "notes").mkdir()
        (self.root / "experiments/F13_example").mkdir(parents=True)
        shutil.copyfile(Path(__file__).with_name("records.py"), self.root / "research/records.py")
        for path, heading in (
            ("PROVED.md", "## P01"),
            ("FAILED.md", "## X01"),
            ("notes/Progress.md", "### C00"),
        ):
            (self.root / path).write_text(f"{heading} — Fixture\n\n**Status:** fixture.\n")
        self.registry = self.root / "REGISTRY.md"
        self.packet = self.root / "experiments/F13_example/RESULT.md"
        self.routes = self.root / "research/routes.toml"
        self.experiments = self.root / "research/experiments.toml"
        self.registry.write_text(REGISTRY)
        self.packet.write_text(PACKET)
        self.routes.write_text(ROUTES)
        self.experiments.write_text(EXPERIMENTS)
        self.cli("build")

    def cli(self, *arguments, succeeds=True):
        result = subprocess.run(
            [sys.executable, str(self.root / "research/records.py"), *arguments],
            capture_output=True,
        )
        if succeeds:
            self.assertEqual(result.returncode, 0, result.stderr.decode())
        else:
            self.assertNotEqual(result.returncode, 0)
        return result

    def test_insertion_reordering_and_field_reflow_preserve_identity(self):
        self.cli("check")
        self.assertEqual(self.cli("show", "route:F12").stdout, ROUTE_ROW.encode())
        reordered = REGISTRY.replace(ROUTE_ROW, "").replace(
            "| F1 | Unrelated route |\n", "| F1 | Unrelated route |\n" + ROUTE_ROW
        )
        reordered = reordered.replace(RUN_ROW, "").replace(
            "| F12 | F1 | Same label in a different table |\n",
            RUN_ROW + "| F12 | F1 | Same label in a different table |\n",
        )
        self.registry.write_text("\nExtra introductory text.\n\n" + reordered)
        self.packet.write_text("\nNew preface.\n\n" + PACKET.replace(
            "**Family:** F12.", "**Family:**\nF12.\nA continuation of the same field."
        ))
        self.cli("check")
        self.assertEqual(self.cli("show", "route:F12").stdout, ROUTE_ROW.encode())
        head = self.cli("head", "route:F12").stdout.decode()
        self.assertIn("routes", head)
        self.assertIn("F12", head)

    def test_missing_or_ambiguous_selectors_fail(self):
        cases = (
            (REGISTRY.replace(ROUTE_ROW, ""), PACKET),
            (REGISTRY.replace(ROUTE_ROW, ROUTE_ROW * 2), PACKET),
            (REGISTRY.replace(RUN_ROW, ""), PACKET),
            (REGISTRY + RUN_ROW, PACKET),
            (REGISTRY, PACKET.replace("**Family:**", "**Other:**")),
            (REGISTRY, PACKET + "\n**Family:** F12.\n"),
            (REGISTRY.replace(ROUTE_ROW, ROUTE_ROW.replace("F12", "F120")), PACKET),
        )
        for index, (registry, packet) in enumerate(cases):
            with self.subTest(case=index):
                self.registry.write_text(registry)
                self.packet.write_text(packet)
                self.cli("check", succeeds=False)

    def test_positional_reference_is_not_accepted(self):
        self.routes.write_text(ROUTES.replace(
            '{ path = "REGISTRY.md", table = "routes", key = "F12" }',
            '"REGISTRY.md:5"',
        ))
        self.cli("check", succeeds=False)

    def test_field_does_not_include_following_metadata(self):
        self.experiments.write_text(EXPERIMENTS.replace(
            '  { path = "REGISTRY.md", table = "runs", key = "F13-R01" },\n', ""
        ))
        self.packet.write_text(PACKET.replace(
            "**Family:** F12.", "**Family:** Unassigned.\n**Status:** Mentions F12."
        ))
        self.cli("check", succeeds=False)

    def test_parent_route_does_not_match_subroute(self):
        self.routes.write_text(ROUTES.replace("F12", "F26"))
        self.experiments.write_text(EXPERIMENTS.replace("route:F12", "route:F26"))
        self.registry.write_text(REGISTRY.replace(ROUTE_ROW, ROUTE_ROW.replace("F12", "F26"))
                                 .replace(RUN_ROW, RUN_ROW.replace("| F12 |", "| F26-Q |")))
        self.packet.write_text(PACKET.replace("F12", "F26-Q"))
        self.cli("check", succeeds=False)


if __name__ == "__main__":
    unittest.main()
