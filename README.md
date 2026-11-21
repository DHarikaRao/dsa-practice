# DSA Practice

![tests](https://github.com/DHarikaRao/dsa-practice/actions/workflows/ci.yml/badge.svg)

Daily data structures and algorithms practice in Python. Every solution is a small file with its own tests, a note on the approach, its time and space complexity, and an honest record of whether I needed hints.

## How I practice

1. **Think for 20 minutes before looking at anything.** Write the brute force first, then improve it.
2. **If I am stuck, read one hint, not the solution.** If I read the solution, I mark `Hints used: yes` and re-implement it from scratch the next day without looking.
3. **Write tests before declaring it solved:** the examples from the problem plus at least two edge cases I thought of.
4. **State the time and space complexity** and the pattern (two pointers, sliding window, BFS, ...) in the file header.
5. **Revisit** every problem marked with hints after three days.

The progress table below is generated from the file headers, so it cannot drift from the code.

## Progress

<!-- PROGRESS:START -->
No solutions yet. Create the first one with:

```bash
python tools/new_problem.py "Two Sum" --topic arrays-hashing --difficulty easy --url https://leetcode.com/problems/two-sum/
```
<!-- PROGRESS:END -->

## Quickstart

```bash
git clone https://github.com/DHarikaRao/dsa-practice.git
cd dsa-practice
pip install pytest

# start a problem (creates problems/<topic>/<name>.py from the template)
python tools/new_problem.py "Two Sum" --topic arrays-hashing --difficulty easy \
    --url https://leetcode.com/problems/two-sum/

# solve it, then check it
python -m pytest -q

# refresh the progress table in this README
python tools/update_progress.py
```

Topics: `arrays-hashing`, `two-pointers`, `sliding-window`, `stack`, `binary-search`, `linked-list`, `trees`, `heap`, `graphs`, `backtracking`, `dp`, `greedy`, `intervals`, `strings`, `math`, `other`.

## Structure

```text
├── problems/<topic>/<name>.py   # one solution per file: header, function, tests
├── questions/week1-4.md         # 50 written questions with examples, edge cases and hints
├── templates/solution_template.py
├── tools/new_problem.py         # create a solution file from the template
├── tools/update_progress.py     # rebuild the progress table in this README
├── tests/test_tools.py          # tests for the tools
└── PLAN.md                      # the 4-week study plan
```

## Plan

See [PLAN.md](PLAN.md) for the 4-week schedule: topics by week, suggested problems, a daily routine, and weekly timed sessions.

The questions for each problem are in [questions/](questions/README.md).

## License

MIT. See [LICENSE](LICENSE).
