# Practice questions

Fifty questions for the 4-week [plan](../PLAN.md), written in my own words, with examples, edge cases to test and hints that stay hidden until you open them.

| Week | File |
|---|---|
| 1 | [Week 1: arrays, hashing, two pointers, sliding window](week1.md) |
| 2 | [Week 2: stack, binary search, linked lists](week2.md) |
| 3 | [Week 3: trees and graphs](week3.md) |
| 4 | [Week 4: dynamic programming, greedy, heaps, intervals, mocks](week4.md) |

## How to use a question

1. Copy the `python tools/new_problem.py ...` command under the question. It creates `problems/<topic>/<name>.py` with the header and a test stub.
2. Write your own tests first: the examples from the question, then the edge cases listed under it.
3. Solve it. Think for 20 minutes before opening a hint.
4. Fill in the complexity and notes, run `python -m pytest -q`, then `python tools/update_progress.py` and commit.

For tree and linked-list questions, define a small `TreeNode` or `ListNode` class in your file and helpers that convert to and from Python lists, so your tests stay readable.
