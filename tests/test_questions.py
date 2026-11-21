"""Keep the written questions consistent with the tools. Run with: python -m pytest -q"""
import re
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))

import new_problem  # noqa: E402

COMMAND = re.compile(r'python tools/new_problem\.py "([^"]+)" --topic (\S+) --difficulty (\S+)')


def commands():
    found = []
    for path in sorted((ROOT / "questions").glob("week*.md")):
        found += COMMAND.findall(path.read_text(encoding="utf-8"))
    return found


class TestQuestions(unittest.TestCase):
    def test_there_are_fifty_questions_with_unique_titles(self):
        titles = [title for title, _, _ in commands()]
        self.assertEqual(len(titles), 50)
        self.assertEqual(len(set(titles)), 50)

    def test_every_command_uses_a_valid_topic_and_difficulty(self):
        for title, topic, difficulty in commands():
            self.assertIn(topic, new_problem.TOPICS, title)
            self.assertIn(difficulty, new_problem.DIFFICULTIES, title)

    def test_every_title_makes_a_unique_valid_file_name(self):
        slugs = [new_problem.slugify(title) for title, _, _ in commands()]
        self.assertEqual(len(slugs), len(set(slugs)))
        for slug in slugs:
            self.assertTrue(slug.isidentifier(), slug)

    def test_every_command_actually_creates_a_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "templates").mkdir()
            shutil.copy(ROOT / "templates" / "solution_template.py", root / "templates")
            for title, topic, difficulty in commands():
                self.assertTrue(new_problem.create_problem(title, topic, difficulty, root=root).exists(), title)

    def test_every_question_has_two_hidden_hints(self):
        for path in sorted((ROOT / "questions").glob("week*.md")):
            text = path.read_text(encoding="utf-8")
            questions = len(COMMAND.findall(text))
            self.assertEqual(text.count("<details>"), 2 * questions, path.name)
            self.assertEqual(text.count("<details>"), text.count("</details>"), path.name)

    def test_every_question_title_appears_in_the_plan(self):
        plan = (ROOT / "PLAN.md").read_text(encoding="utf-8")
        missing = [title for title, _, _ in commands() if title not in plan]
        self.assertEqual(missing, [])


if __name__ == "__main__":
    unittest.main()
