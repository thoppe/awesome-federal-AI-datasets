"""Regression checks for the documented catalog harness."""

import subprocess
import sys
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class CatalogHarnessTests(unittest.TestCase):
    def test_catalog_validates(self):
        result = subprocess.run(
            [sys.executable, "src/validate_catalog.py"],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("20 manifests", result.stdout)

    def test_readme_is_current(self):
        result = subprocess.run(
            [sys.executable, "src/build_README.py", "--check"],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)


if __name__ == "__main__":
    unittest.main()
