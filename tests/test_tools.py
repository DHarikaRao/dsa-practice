"""Tests for the helper tools. Run with: python -m pytest -q"""
import ast
import datetime
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))

import new_problem  # noqa: E402
import update_progress  # noqa: E402

README = f"# Test\n\n{update_progress.START}\nold\n{update_progress.END}\n\nfooter\n"


class ToolsCase(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        (self.root / "templates").mkdir()
        shutil.copy(ROOT / "templates" / "solution_template.py", self.root / "templates")
        (self.root / "problems").mkdir()
        (self.root / "README.md").write_text(README, encoding="utf-8")

    def tearDown(self):
        self.tmp.cleanup()

    def make(self, title="Two Sum", topic="arrays-hashing", difficulty="easy", today=None):
        return new_problem.create_problem(
            title, topic, difficulty, "https://example.com/p", root=self.root,
            today=today or datetime.date(2026, 11, 19),
        )


class TestNewProblem(ToolsCase):
    def test_slugify(self):
        self.assertEqual(new_problem.slugify("Two Sum"), "two_sum")
        self.assertEqual(new_problem.slugify("  3Sum (Closest)! "), "p_3sum_closest")
        with self.assertRaises(ValueError):
            new_problem.slugify("???")

    def test_creates_a_valid_python_file_with_a_parsable_header(self):
        path = self.make()
        self.assertEqual(path, self.root / "problems" / "arrays-hashing" / "two_sum.py")
        ast.parse(path.read_text(encoding="utf-8"))  # must be valid Python
        header = update_progress.parse_header(path)
        self.assertEqual(header["problem"], "Two Sum")
        self.assertEqual(header["difficulty"], "easy")
        self.assertEqual(header["date"], "2026-11-19")
        self.assertEqual(header["hints used"], "no")
        self.assertIn("def two_sum()", path.read_text(encoding="utf-8"))

    def test_refuses_to_overwrite_and_rejects_bad_input(self):
        self.make()
        with self.assertRaises(FileExistsError):
            self.make()
        with self.assertRaises(ValueError):
            self.make(topic="cooking")
        with self.assertRaises(ValueError):
            self.make(difficulty="impossible")
        with self.assertRaises(ValueError):
            self.make(title='bad """ title')

    def test_the_real_template_is_valid_python_with_every_placeholder(self):
        text = (ROOT / "templates" / "solution_template.py").read_text(encoding="utf-8")
        for placeholder in ("{{TITLE}}", "{{TOPIC}}", "{{DIFFICULTY}}", "{{URL}}", "{{DATE}}", "{{FUNC}}"):
            self.assertIn(placeholder, text)


class TestProgress(ToolsCase):
    def test_empty_repo_shows_a_getting_started_message(self):
        _, new = update_progress.update_readme(self.root)
        self.assertIn("No solutions yet", new)
        self.assertIn("footer", new)

    def test_table_counts_and_orders_solutions(self):
        self.make("Two Sum", "arrays-hashing", "easy", datetime.date(2026, 11, 19))
        self.make("Valid Parentheses", "stack", "easy", datetime.date(2026, 11, 20))
        self.make("Coin Change", "dp", "medium", datetime.date(2026, 11, 21))
        text = update_progress.render(update_progress.collect(self.root))
        self.assertIn("**Solved: 3** (easy 2, medium 1, hard 0)", text)
        self.assertIn("Solved without hints: 3 of 3", text)
        self.assertLess(text.index("Coin Change"), text.index("Two Sum"))  # newest first
        self.assertIn("(problems/dp/coin_change.py)", text)

    def test_hints_are_counted_honestly(self):
        path = self.make()
        path.write_text(path.read_text(encoding="utf-8").replace("Hints used: no", "Hints used: yes, looked at the editorial"), encoding="utf-8")
        text = update_progress.render(update_progress.collect(self.root))
        self.assertIn("Solved without hints: 0 of 1", text)

    def test_update_is_idempotent_and_keeps_the_rest_of_the_readme(self):
        self.make()
        _, first = update_progress.update_readme(self.root)
        (self.root / "README.md").write_text(first, encoding="utf-8")
        _, second = update_progress.update_readme(self.root)
        self.assertEqual(first, second)
        self.assertTrue(first.startswith("# Test"))
        self.assertTrue(first.rstrip().endswith("footer"))

    def test_missing_markers_are_reported(self):
        (self.root / "README.md").write_text("no markers here", encoding="utf-8")
        with self.assertRaises(ValueError):
            update_progress.update_readme(self.root)

    def test_files_without_a_header_are_ignored(self):
        stray = self.root / "problems" / "other"
        stray.mkdir(parents=True)
        (stray / "scratch.py").write_text("print('hello')\n", encoding="utf-8")
        self.assertEqual(update_progress.collect(self.root), [])


if __name__ == "__main__":
    unittest.main()
