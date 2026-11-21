# Week 4: dynamic programming, greedy, heaps, intervals, mocks

Questions written in my own words for the problems in [PLAN.md](../PLAN.md). Every example output was checked against a reference solution, but the original problem pages may differ in small details (limits, return format). When in doubt, follow the original page.

Rules: think for 20 minutes first, open one hint at a time, and mark `Hints used` honestly in the file header.

## Day 22

### 41. Climbing Stairs
`easy` · `dp`

**Task.** You climb a staircase of `n` steps, taking 1 or 2 steps at a time. In how many distinct ways can you reach the top?

**Examples.**
```text
n = 2
-> 2

n = 3
-> 3

n = 5
-> 8
```

**Assume.** 1 <= n <= 45.

**Aim for.** O(n) time, O(1) space.

**Edge cases to test.** n = 1; n = 2; the largest n (no recursion without memoisation!).

<details><summary>Hint 1 (open only after your 20 minutes)</summary>

To stand on step n, which two steps could you have come from?

</details>

<details><summary>Hint 2 (open only after your 20 minutes)</summary>

ways(n) = ways(n - 1) + ways(n - 2). You only need the last two values.

</details>

Create the file:
```bash
python tools/new_problem.py "Climbing Stairs" --topic dp --difficulty easy
```

### 42. House Robber
`medium` · `dp`

**Task.** `nums[i]` is the money in house `i`. You cannot rob two adjacent houses. Return the most money you can rob.

**Examples.**
```text
nums = [1, 2, 3, 1]
-> 4

nums = [2, 7, 9, 3, 1]
-> 12
```

**Assume.** 1 to 100 houses.

**Aim for.** O(n) time, O(1) space.

**Edge cases to test.** one house; two houses; all houses worth 0.

<details><summary>Hint 1 (open only after your 20 minutes)</summary>

At each house you choose: skip it, or rob it and add the best total from two houses back.

</details>

<details><summary>Hint 2 (open only after your 20 minutes)</summary>

Keep only the best totals for the previous two houses.

</details>

Create the file:
```bash
python tools/new_problem.py "House Robber" --topic dp --difficulty medium
```

### 43. Coin Change
`medium` · `dp`

**Task.** `coins` lists coin values, and you have an unlimited supply of each. Return the fewest coins that sum to `amount`, or -1 if it cannot be made.

**Examples.**
```text
coins = [1, 2, 5], amount = 11
-> 3

coins = [2], amount = 3
-> -1

coins = [1], amount = 0
-> 0

coins = [1, 3, 4], amount = 6
-> 2
```

**Assume.** amount up to 10^4.

**Aim for.** O(amount * number of coins) time.

**Edge cases to test.** amount 0; a coin larger than the amount; an amount that cannot be made.

<details><summary>Hint 1 (open only after your 20 minutes)</summary>

Define best[a] as the fewest coins for amount a. How does best[a] relate to best[a - coin]?

</details>

<details><summary>Hint 2 (open only after your 20 minutes)</summary>

Start with best[0] = 0 and everything else as infinity. Note that greedily taking the largest coin fails on the last example.

</details>

Create the file:
```bash
python tools/new_problem.py "Coin Change" --topic dp --difficulty medium
```

## Day 23

### 44. Longest Increasing Subsequence
`medium` · `dp`

**Task.** Return the length of the longest strictly increasing subsequence of `nums` (the elements need not be next to each other).

**Examples.**
```text
nums = [10, 9, 2, 5, 3, 7, 101, 18]
-> 4

nums = [0, 1, 0, 3, 2, 3]
-> 4

nums = [7, 7, 7, 7]
-> 1
```

**Assume.** up to 2500 numbers.

**Aim for.** O(n^2) first, then O(n log n) using `bisect`.

**Edge cases to test.** all equal values; strictly decreasing; a single element.

<details><summary>Hint 1 (open only after your 20 minutes)</summary>

For each index, what is the longest increasing subsequence that ends there?

</details>

<details><summary>Hint 2 (open only after your 20 minutes)</summary>

For the O(n log n) version, keep the smallest possible tail value for each subsequence length and use binary search.

</details>

Create the file:
```bash
python tools/new_problem.py "Longest Increasing Subsequence" --topic dp --difficulty medium
```

### 45. Word Break
`medium` · `dp`

**Task.** Given a string `s` and a list of words `word_dict`, return `True` if `s` can be split into a sequence of dictionary words. Words may be reused.

**Examples.**
```text
s = 'leetcode', word_dict = ['leet', 'code']
-> True

s = 'applepenapple', word_dict = ['apple', 'pen']
-> True

s = 'catsandog', word_dict = ['cats', 'dog', 'sand', 'and', 'cat']
-> False
```

**Assume.** s up to 300 characters.

**Aim for.** O(len(s)^2) time.

**Edge cases to test.** a word longer than s; reusing the same word; a string that can only be split in one specific way.

<details><summary>Hint 1 (open only after your 20 minutes)</summary>

Let can[i] mean 'the first i characters can be split into words'.

</details>

<details><summary>Hint 2 (open only after your 20 minutes)</summary>

can[i] is true if some j < i has can[j] true and s[j:i] is a word. Put the words in a set.

</details>

Create the file:
```bash
python tools/new_problem.py "Word Break" --topic dp --difficulty medium
```

## Day 24

### 46. Jump Game
`medium` · `greedy`

**Task.** `nums[i]` is the maximum jump length from index `i`. Starting at index 0, return `True` if you can reach the last index.

**Examples.**
```text
nums = [2, 3, 1, 1, 4]
-> True

nums = [3, 2, 1, 0, 4]
-> False
```

**Assume.** up to 10^4 numbers.

**Aim for.** O(n) time, O(1) space.

**Edge cases to test.** one element (True); a leading zero ([0, 1] is False); zeros in the middle that can be jumped over.

<details><summary>Hint 1 (open only after your 20 minutes)</summary>

You do not need to know the exact path, only how far you can possibly get.

</details>

<details><summary>Hint 2 (open only after your 20 minutes)</summary>

Track the farthest index reachable so far; if you ever stand on an index beyond it, the answer is False.

</details>

Create the file:
```bash
python tools/new_problem.py "Jump Game" --topic greedy --difficulty medium
```

### 47. Merge Intervals
`medium` · `intervals`

**Task.** Given a list of intervals `[start, end]`, merge all overlapping intervals and return the non-overlapping result. Intervals that only touch (`[1, 4]` and `[4, 5]`) count as overlapping.

**Examples.**
```text
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
-> [[1, 6], [8, 10], [15, 18]]

intervals = [[1, 4], [4, 5]]
-> [[1, 5]]
```

**Assume.** up to 10^4 intervals; the input may be unsorted.

**Aim for.** O(n log n) time.

**Edge cases to test.** one interval; an interval completely inside another ([1, 10] and [2, 3]); unsorted input.

<details><summary>Hint 1 (open only after your 20 minutes)</summary>

Sort by start. Then overlaps can only happen between neighbours.

</details>

<details><summary>Hint 2 (open only after your 20 minutes)</summary>

Compare each interval with the last merged one: extend its end, or append a new interval.

</details>

Create the file:
```bash
python tools/new_problem.py "Merge Intervals" --topic intervals --difficulty medium
```

### 48. Insert Interval
`medium` · `intervals`

**Task.** `intervals` is a list of non-overlapping intervals sorted by start. Insert `new_interval`, merging overlaps, and return a sorted, non-overlapping list.

**Examples.**
```text
intervals = [[1, 3], [6, 9]], new_interval = [2, 5]
-> [[1, 5], [6, 9]]

intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], new_interval = [4, 8]
-> [[1, 2], [3, 10], [12, 16]]
```

**Assume.** up to 10^4 intervals.

**Aim for.** O(n) time.

**Edge cases to test.** empty list; new interval before everything; new interval after everything; new interval that swallows everything.

<details><summary>Hint 1 (open only after your 20 minutes)</summary>

Split the work into three phases by position.

</details>

<details><summary>Hint 2 (open only after your 20 minutes)</summary>

Copy the intervals that end before the new one starts; merge those that overlap it; copy the rest.

</details>

Create the file:
```bash
python tools/new_problem.py "Insert Interval" --topic intervals --difficulty medium
```

## Day 25

### 49. Kth Largest Element in an Array
`medium` · `heap`

**Task.** Return the `k`-th largest element of `nums` in sorted order (duplicates count separately), not the k-th distinct value.

**Examples.**
```text
nums = [3, 2, 1, 5, 6, 4], k = 2
-> 5

nums = [3, 2, 3, 1, 2, 4, 5, 5, 6], k = 4
-> 4
```

**Assume.** 1 <= k <= len(nums).

**Aim for.** O(n log k) with a heap; quickselect averages O(n).

**Edge cases to test.** k = 1; k = len(nums); many duplicates.

<details><summary>Hint 1 (open only after your 20 minutes)</summary>

Sorting works in O(n log n). Can you do better when k is small?

</details>

<details><summary>Hint 2 (open only after your 20 minutes)</summary>

Keep a min-heap of the k largest values seen so far; the root is your answer.

</details>

Create the file:
```bash
python tools/new_problem.py "Kth Largest Element in an Array" --topic heap --difficulty medium
```

### 50. Task Scheduler
`medium` · `heap`

**Task.** `tasks` is a list of letters; each task takes one time unit. Two runs of the same letter must be separated by at least `n` time units (other tasks or idle time). Return the least total time needed to finish all tasks.

**Examples.**
```text
tasks = ['A', 'A', 'A', 'B', 'B', 'B'], n = 2
-> 8

tasks = ['A', 'A', 'A', 'B', 'B', 'B'], n = 0
-> 6

tasks = ['A', 'A', 'A', 'A', 'A', 'A', 'B', 'C', 'D', 'E', 'F', 'G'], n = 2
-> 16
```

**Assume.** up to 10^4 tasks, uppercase letters.

**Aim for.** O(n) time with a formula, or O(n log 26) with a heap simulation.

**Edge cases to test.** n = 0; all tasks different; one task much more frequent than the rest.

<details><summary>Hint 1 (open only after your 20 minutes)</summary>

The most frequent task forces a layout. How many 'frames' of length n + 1 does it need?

</details>

<details><summary>Hint 2 (open only after your 20 minutes)</summary>

Fill the gaps with other tasks. The answer is at least the number of tasks, and at least the length of the frame layout.

</details>

Create the file:
```bash
python tools/new_problem.py "Task Scheduler" --topic heap --difficulty medium
```

## Day 26

Full revision of every problem marked `Hints used: yes`. Re-implement from scratch.

## Day 27

**Mock assessment (no hints, online editor).** Pick three you have not solved, set a 90-minute timer, and use no hints. Search the names below on LeetCode (statements are not reproduced here):

- Subsets
- Combination Sum
- Decode Ways
- Maximum Subarray
- Unique Paths

## Day 28

Review the mock. List your two weakest topics and plan the next two weeks around them.
