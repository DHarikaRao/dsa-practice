# Week 2: stack, binary search, linked lists

Questions written in my own words for the problems in [PLAN.md](../PLAN.md). Every example output was checked against a reference solution, but the original problem pages may differ in small details (limits, return format). When in doubt, follow the original page.

Rules: think for 20 minutes first, open one hint at a time, and mark `Hints used` honestly in the file header.

## Day 8

### 14. Valid Parentheses
`easy` · `stack`

**Task.** `s` contains only the characters `()[]{}`. Return `True` if every bracket is closed by the same type of bracket and in the correct order.

**Examples.**
```text
s = '()[]{}'
-> True

s = '(]'
-> False

s = '([)]'
-> False

s = '{[]}'
-> True
```

**Assume.** up to 10^4 characters.

**Aim for.** O(n) time.

**Edge cases to test.** empty string (True); a lone closing bracket; a lone opening bracket.

<details><summary>Hint 1 (open only after your 20 minutes)</summary>

The most recent unclosed opening bracket must be closed first.

</details>

<details><summary>Hint 2 (open only after your 20 minutes)</summary>

Push opening brackets on a stack; on a closing bracket, check the top of the stack.

</details>

Create the file:
```bash
python tools/new_problem.py "Valid Parentheses" --topic stack --difficulty easy
```

### 15. Min Stack
`medium` · `stack`

**Task.** Design a stack that supports `push(x)`, `pop()`, `top()` and `get_min()`, all in O(1) time.

**Examples.**
```text
operations = ['push(-2)', 'push(0)', 'push(-3)', 'get_min()', 'pop()', 'top()', 'get_min()']
-> [None, None, None, -3, None, 0, -2]
```

**Assume.** pop and top are never called on an empty stack.

**Aim for.** O(1) per operation.

**Edge cases to test.** popping back to one element; duplicate minimum values; pushing a new minimum, then popping it.

<details><summary>Hint 1 (open only after your 20 minutes)</summary>

When you push, what is the minimum of the stack at that moment?

</details>

<details><summary>Hint 2 (open only after your 20 minutes)</summary>

Store the running minimum together with each element.

</details>

Create the file:
```bash
python tools/new_problem.py "Min Stack" --topic stack --difficulty medium
```

### 16. Daily Temperatures
`medium` · `stack`

**Task.** `temperatures[i]` is the temperature on day `i`. For each day, return how many days you must wait for a warmer temperature, or 0 if there is none.

**Examples.**
```text
temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
-> [1, 1, 4, 2, 1, 1, 0, 0]
```

**Assume.** up to 10^5 days.

**Aim for.** O(n) time.

**Edge cases to test.** strictly decreasing temperatures; all equal; a single day.

<details><summary>Hint 1 (open only after your 20 minutes)</summary>

Brute force checks every later day. What information from earlier days lets you avoid that?

</details>

<details><summary>Hint 2 (open only after your 20 minutes)</summary>

Keep a stack of indices of days still waiting for a warmer day; a warmer day resolves several of them at once.

</details>

Create the file:
```bash
python tools/new_problem.py "Daily Temperatures" --topic stack --difficulty medium
```

## Day 9

### 17. Binary Search
`easy` · `binary-search`

**Task.** `nums` is sorted in ascending order with distinct values. Return the index of `target`, or -1 if it is absent.

**Examples.**
```text
nums = [-1, 0, 3, 5, 9, 12], target = 9
-> 4

nums = [-1, 0, 3, 5, 9, 12], target = 2
-> -1
```

**Assume.** up to 10^4 numbers.

**Aim for.** O(log n) time.

**Edge cases to test.** one element; target smaller than everything; target larger than everything.

<details><summary>Hint 1 (open only after your 20 minutes)</summary>

State what must be true about `lo` and `hi` at every step (the invariant).

</details>

<details><summary>Hint 2 (open only after your 20 minutes)</summary>

Decide how `mid` changes `lo` or `hi` so the loop always shrinks the range.

</details>

Create the file:
```bash
python tools/new_problem.py "Binary Search" --topic binary-search --difficulty easy
```

### 18. Search a 2D Matrix
`medium` · `binary-search`

**Task.** A matrix has rows sorted ascending, and the first number of each row is greater than the last number of the previous row. Return `True` if `target` is in the matrix.

**Examples.**
```text
matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target = 3
-> True

matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target = 13
-> False
```

**Assume.** up to 100 x 100.

**Aim for.** O(log(rows * cols)) time.

**Edge cases to test.** single row; single column; a 1 x 1 matrix.

<details><summary>Hint 1 (open only after your 20 minutes)</summary>

Read the matrix, row after row, as one long sorted list.

</details>

<details><summary>Hint 2 (open only after your 20 minutes)</summary>

Search indices 0 .. rows*cols-1 and convert a middle index back with `divmod(mid, cols)`.

</details>

Create the file:
```bash
python tools/new_problem.py "Search a 2D Matrix" --topic binary-search --difficulty medium
```

### 19. Koko Eating Bananas
`medium` · `binary-search`

**Task.** `piles[i]` is the number of bananas in pile `i`. A guard returns in `h` hours. Koko chooses a speed of `k` bananas per hour; each hour she picks one pile and eats up to `k` bananas from it (if the pile has fewer, she finishes it and does nothing else that hour). Return the smallest integer `k` that lets her finish all piles within `h` hours.

**Examples.**
```text
piles = [3, 6, 7, 11], h = 8
-> 4

piles = [30, 11, 23, 4, 20], h = 5
-> 30

piles = [30, 11, 23, 4, 20], h = 6
-> 23
```

**Assume.** len(piles) <= h.

**Aim for.** O(n log max(piles)) time.

**Edge cases to test.** h equals the number of piles (answer is the largest pile); a single pile; very large piles.

<details><summary>Hint 1 (open only after your 20 minutes)</summary>

If a speed works, does every faster speed work too?

</details>

<details><summary>Hint 2 (open only after your 20 minutes)</summary>

Binary search the speed. For a given speed, count the hours with a ceiling division per pile.

</details>

Create the file:
```bash
python tools/new_problem.py "Koko Eating Bananas" --topic binary-search --difficulty medium
```

## Day 10

### 20. Search in Rotated Sorted Array
`medium` · `binary-search`

**Task.** A sorted list of distinct integers was rotated at an unknown pivot (for example `[0, 1, 2, 4, 5, 6, 7]` became `[4, 5, 6, 7, 0, 1, 2]`). Return the index of `target` in the rotated list, or -1, in O(log n).

**Examples.**
```text
nums = [4, 5, 6, 7, 0, 1, 2], target = 0
-> 4

nums = [4, 5, 6, 7, 0, 1, 2], target = 3
-> -1
```

**Assume.** up to 5000 numbers, all distinct.

**Aim for.** O(log n) time.

**Edge cases to test.** not rotated at all; one element; two elements.

<details><summary>Hint 1 (open only after your 20 minutes)</summary>

Whichever way you split the range, at least one half is still sorted. How can you tell which?

</details>

<details><summary>Hint 2 (open only after your 20 minutes)</summary>

Check whether the target lies inside the sorted half; if not, search the other half.

</details>

Create the file:
```bash
python tools/new_problem.py "Search in Rotated Sorted Array" --topic binary-search --difficulty medium
```

### 21. Find Minimum in Rotated Sorted Array
`medium` · `binary-search`

**Task.** A sorted list of distinct integers was rotated (possibly zero times). Return its minimum in O(log n).

**Examples.**
```text
nums = [3, 4, 5, 1, 2]
-> 1

nums = [4, 5, 6, 7, 0, 1, 2]
-> 0

nums = [11, 13, 15, 17]
-> 11
```

**Assume.** up to 5000 numbers, all distinct.

**Aim for.** O(log n) time.

**Edge cases to test.** not rotated; one element; rotated by one position.

<details><summary>Hint 1 (open only after your 20 minutes)</summary>

Compare the middle element with the rightmost element.

</details>

<details><summary>Hint 2 (open only after your 20 minutes)</summary>

If mid is greater than the right end, the minimum is to the right of mid; otherwise it is at mid or to its left.

</details>

Create the file:
```bash
python tools/new_problem.py "Find Minimum in Rotated Sorted Array" --topic binary-search --difficulty medium
```

## Day 11

### 22. Reverse Linked List
`easy` · `linked-list`

**Task.** Given the head of a singly linked list, reverse the list and return the new head. In your tests, build the list from a Python list with a small helper, and convert the result back to a list to compare.

**Examples.**
```text
head = [1, 2, 3, 4, 5]
-> [5, 4, 3, 2, 1]

head = [1, 2]
-> [2, 1]
```

**Assume.** 0 to 5000 nodes.

**Aim for.** O(n) time, O(1) extra space (do it iteratively first, then recursively).

**Edge cases to test.** empty list; one node; two nodes.

<details><summary>Hint 1 (open only after your 20 minutes)</summary>

Keep two pointers: the reversed part so far (`prev`) and the current node.

</details>

<details><summary>Hint 2 (open only after your 20 minutes)</summary>

Save `current.next` before you overwrite it.

</details>

Create the file:
```bash
python tools/new_problem.py "Reverse Linked List" --topic linked-list --difficulty easy
```

### 23. Merge Two Sorted Lists
`easy` · `linked-list`

**Task.** Merge two sorted linked lists into one sorted list by reusing the existing nodes. Return the head of the merged list.

**Examples.**
```text
list1 = [1, 2, 4], list2 = [1, 3, 4]
-> [1, 1, 2, 3, 4, 4]

list1 = [], list2 = [0]
-> [0]
```

**Assume.** 0 to 50 nodes each.

**Aim for.** O(n + m) time, O(1) extra space.

**Edge cases to test.** both lists empty; one list empty; all values of one list smaller than the other.

<details><summary>Hint 1 (open only after your 20 minutes)</summary>

A dummy head node avoids special cases for the first node.

</details>

<details><summary>Hint 2 (open only after your 20 minutes)</summary>

Keep a tail pointer; attach the smaller head each time, and attach whatever remains at the end.

</details>

Create the file:
```bash
python tools/new_problem.py "Merge Two Sorted Lists" --topic linked-list --difficulty easy
```

### 24. Linked List Cycle
`easy` · `linked-list`

**Task.** Return `True` if following `next` pointers from the head ever returns to a node you have already visited. In the examples, `cycle_to` is the index of the node that the last node points back to, or `None`.

**Examples.**
```text
values = [3, 2, 0, -4], cycle_to = 1
-> True

values = [1, 2], cycle_to = None
-> False
```

**Assume.** 0 to 10^4 nodes.

**Aim for.** O(n) time, O(1) space.

**Edge cases to test.** empty list; one node pointing to itself; cycle back to the head.

<details><summary>Hint 1 (open only after your 20 minutes)</summary>

A set of visited nodes works but uses O(n) space.

</details>

<details><summary>Hint 2 (open only after your 20 minutes)</summary>

Use two pointers moving at different speeds: if there is a cycle, the fast one eventually catches the slow one.

</details>

Create the file:
```bash
python tools/new_problem.py "Linked List Cycle" --topic linked-list --difficulty easy
```

## Day 12

### 25. Remove Nth Node From End of List
`medium` · `linked-list`

**Task.** Remove the `n`-th node from the end of a linked list and return the head.

**Examples.**
```text
head = [1, 2, 3, 4, 5], n = 2
-> [1, 2, 3, 5]

head = [1], n = 1
-> []

head = [1, 2], n = 1
-> [1]
```

**Assume.** 1 <= n <= length of the list.

**Aim for.** one pass, O(1) space.

**Edge cases to test.** removing the head; a single node; removing the last node.

<details><summary>Hint 1 (open only after your 20 minutes)</summary>

If two pointers are n nodes apart, what is the second pointer's position when the first one reaches the end?

</details>

<details><summary>Hint 2 (open only after your 20 minutes)</summary>

A dummy node before the head makes removing the first node a normal case.

</details>

Create the file:
```bash
python tools/new_problem.py "Remove Nth Node From End of List" --topic linked-list --difficulty medium
```

### 26. Reorder List
`medium` · `linked-list`

**Task.** Reorder `L0 -> L1 -> ... -> Ln` into `L0 -> Ln -> L1 -> Ln-1 -> L2 -> Ln-2 -> ...`, in place, by changing links only.

**Examples.**
```text
head = [1, 2, 3, 4]
-> [1, 4, 2, 3]

head = [1, 2, 3, 4, 5]
-> [1, 5, 2, 4, 3]
```

**Assume.** 1 to 5 * 10^4 nodes.

**Aim for.** O(n) time, O(1) space.

**Edge cases to test.** one node; two nodes; odd and even lengths.

<details><summary>Hint 1 (open only after your 20 minutes)</summary>

Find the middle with a slow and a fast pointer.

</details>

<details><summary>Hint 2 (open only after your 20 minutes)</summary>

Reverse the second half, then weave the two halves together one node at a time.

</details>

Create the file:
```bash
python tools/new_problem.py "Reorder List" --topic linked-list --difficulty medium
```

## Day 13

### 27. LRU Cache
`medium` · `linked-list`

**Task.** Design a cache with a fixed capacity supporting `get(key)` (returns the value or -1) and `put(key, value)`. When a `put` leaves the cache over capacity, evict the least recently used key. Both a `get` and a `put` count as a use. Both operations must be O(1) on average.

**Examples.**
```text
capacity = 2
operations = ['put(1, 1)', 'put(2, 2)', 'get(1)', 'put(3, 3)', 'get(2)', 'put(4, 4)', 'get(1)', 'get(3)', 'get(4)']
-> [None, None, 1, None, -1, None, -1, 3, 4]
```

**Assume.** capacity of at least 1.

**Aim for.** O(1) per operation.

**Edge cases to test.** updating an existing key counts as a use and must not evict; capacity 1; get on a missing key.

<details><summary>Hint 1 (open only after your 20 minutes)</summary>

You need fast lookup by key, and a way to move an entry to the 'most recent' end in O(1).

</details>

<details><summary>Hint 2 (open only after your 20 minutes)</summary>

A hash map from key to node, plus a doubly linked list ordered by recency. Build the list yourself once, then try `collections.OrderedDict`.

</details>

Create the file:
```bash
python tools/new_problem.py "LRU Cache" --topic linked-list --difficulty medium
```

After LRU Cache, revise the problems you marked with hints.

## Day 14

**Week 2 timed session.** Pick three you have not solved, set a 90-minute timer, and use no hints. Search the names below on LeetCode (statements are not reproduced here):

- Evaluate Reverse Polish Notation
- Generate Parentheses
- Time Based Key-Value Store
- Add Two Numbers
- Find the Duplicate Number
