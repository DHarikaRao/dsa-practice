"""Rebuild the progress table in README.md from the header of every solution file.

Usage:
    python tools/update_progress.py          # rewrite the table
    python tools/update_progress.py --check  # exit 1 if README.md is out of date
"""
import argparse
import ast
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
START, END = "<!-- PROGRESS:START -->", "<!-- PROGRESS:END -->"


def parse_header(path: Path) -> dict:
    """Read the 'Key: value' lines at the top of a solution's docstring."""
    try:
        doc = ast.get_docstring(ast.parse(Path(path).read_text(encoding="utf-8"))) or ""
    except SyntaxError:
        return {}
    fields = {}
    for line in doc.splitlines():
        if not line.strip():
            break
        key, separator, value = line.partition(":")
        if separator:
            fields[key.strip().lower()] = value.strip()
    return fields


def collect(root=ROOT) -> list[dict]:
    entries = []
    problems = Path(root) / "problems"
    for path in sorted(problems.rglob("*.py")):
        fields = parse_header(path)
        if "problem" not in fields:
            continue
        entries.append({
            "title": fields["problem"],
            "topic": fields.get("topic", "other"),
            "difficulty": fields.get("difficulty", "?"),
            "date": fields.get("date", ""),
            "time": fields.get("time", "?"),
            "space": fields.get("space", "?"),
            "hints": fields.get("hints used", "?"),
            "path": path.relative_to(root).as_posix(),
        })
    return entries


def render(entries: list[dict]) -> str:
    if not entries:
        return ("No solutions yet. Create the first one with:\n\n"
                "```bash\npython tools/new_problem.py \"Two Sum\" --topic arrays-hashing --difficulty easy "
                "--url https://leetcode.com/problems/two-sum/\n```")

    levels = Counter(e["difficulty"] for e in entries)
    topics = Counter(e["topic"] for e in entries)
    no_hints = sum(1 for e in entries if e["hints"].lower().startswith("no"))
    lines = [
        f"**Solved: {len(entries)}** (easy {levels['easy']}, medium {levels['medium']}, hard {levels['hard']}). "
        f"Solved without hints: {no_hints} of {len(entries)}.",
        "",
        "| Topic | Solved |",
        "|---|---|",
    ]
    lines += [f"| {topic} | {count} |" for topic, count in sorted(topics.items())]
    lines += ["", "| Date | Problem | Topic | Difficulty | Time | Space | Hints used |", "|---|---|---|---|---|---|---|"]
    for e in sorted(entries, key=lambda e: (e["date"], e["title"]), reverse=True):
        lines.append(
            f"| {e['date']} | [{e['title']}]({e['path']}) | {e['topic']} | {e['difficulty']} "
            f"| {e['time']} | {e['space']} | {e['hints']} |"
        )
    return "\n".join(lines)


def update_readme(root=ROOT) -> tuple[str, str]:
    """Return (old README text, new README text) with the progress block regenerated."""
    readme_path = Path(root) / "README.md"
    text = readme_path.read_text(encoding="utf-8")
    if START not in text or END not in text:
        raise ValueError(f"README.md must contain the markers {START} and {END}")
    head, rest = text.split(START, 1)
    _, tail = rest.split(END, 1)
    return text, f"{head}{START}\n{render(collect(root))}\n{END}{tail}"


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("--check", action="store_true", help="fail if the README table is out of date")
    args = parser.parse_args()
    try:
        old, new = update_readme()
    except ValueError as error:
        print(f"Error: {error}")
        sys.exit(1)
    if args.check:
        if old != new:
            print("README.md is out of date. Run: python tools/update_progress.py")
            sys.exit(1)
        print("README.md is up to date.")
        return
    (ROOT / "README.md").write_text(new, encoding="utf-8")
    print(f"README.md updated ({len(collect())} solutions).")


if __name__ == "__main__":
    main()
