"""Create a new solution file from the template.

Usage:
    python tools/new_problem.py "Two Sum" --topic arrays-hashing --difficulty easy \
        --url https://leetcode.com/problems/two-sum/
"""
import argparse
import datetime
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOPICS = [
    "arrays-hashing", "two-pointers", "sliding-window", "stack", "binary-search", "linked-list",
    "trees", "heap", "graphs", "backtracking", "dp", "greedy", "intervals", "strings", "math", "other",
]
DIFFICULTIES = ["easy", "medium", "hard"]


def slugify(title: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "_", title.lower()).strip("_")
    if not slug:
        raise ValueError("The title must contain letters or digits.")
    if slug[0].isdigit():
        slug = "p_" + slug  # a Python function name cannot start with a digit
    return slug


def create_problem(title, topic, difficulty, url="", root=ROOT, today=None) -> Path:
    if topic not in TOPICS:
        raise ValueError(f"Unknown topic '{topic}'. Choose one of: {', '.join(TOPICS)}")
    if difficulty not in DIFFICULTIES:
        raise ValueError(f"Difficulty must be one of: {', '.join(DIFFICULTIES)}")
    if '"""' in title or "\n" in title:
        raise ValueError("The title cannot contain triple quotes or line breaks.")

    slug = slugify(title)
    path = Path(root) / "problems" / topic / f"{slug}.py"
    if path.exists():
        raise FileExistsError(f"{path} already exists. Open it and keep working there.")

    text = (Path(root) / "templates" / "solution_template.py").read_text(encoding="utf-8")
    values = {
        "{{TITLE}}": title.strip(),
        "{{TOPIC}}": topic,
        "{{DIFFICULTY}}": difficulty,
        "{{URL}}": url or "-",
        "{{DATE}}": (today or datetime.date.today()).isoformat(),
        "{{FUNC}}": slug,
    }
    for placeholder, value in values.items():
        text = text.replace(placeholder, value)

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return path


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("title")
    parser.add_argument("--topic", required=True, choices=TOPICS)
    parser.add_argument("--difficulty", required=True, choices=DIFFICULTIES)
    parser.add_argument("--url", default="")
    args = parser.parse_args()
    try:
        path = create_problem(args.title, args.topic, args.difficulty, args.url)
    except (ValueError, FileExistsError) as error:
        print(f"Error: {error}")
        sys.exit(1)
    print(f"Created {path.relative_to(ROOT)}")
    print("Next: solve it, run `python -m pytest -q`, then `python tools/update_progress.py`.")


if __name__ == "__main__":
    main()
