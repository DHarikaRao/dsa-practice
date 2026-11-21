# Week 3: trees and graphs

Questions written in my own words for the problems in [PLAN.md](../PLAN.md). Every example output was checked against a reference solution, but the original problem pages may differ in small details (limits, return format). When in doubt, follow the original page.

Rules: think for 20 minutes first, open one hint at a time, and mark `Hints used` honestly in the file header.

## Day 15

### 28. Invert Binary Tree
`easy` · `trees`

**Task.** Mirror a binary tree: swap the left and right child of every node. Return the root. In examples, a tree is written as a level-order list with `None` for missing children; write small helpers to build and read trees in your tests.

**Examples.**
```text
root = [4, 2, 7, 1, 3, 6, 9]
-> [4, 7, 2, 9, 6, 3, 1]
```

**Assume.** 0 to 100 nodes.

**Aim for.** O(n) time.

**Edge cases to test.** empty tree; a single node; a tree that is only a left chain.

<details><summary>Hint 1 (open only after your 20 minutes)</summary>

What does the mirror of a tree consist of?

</details>

<details><summary>Hint 2 (open only after your 20 minutes)</summary>

Swap the two children, then invert each child (recursively, or with a queue).

</details>

Create the file:
```bash
python tools/new_problem.py "Invert Binary Tree" --topic trees --difficulty easy
```

### 29. Maximum Depth of Binary Tree
`easy` · `trees`

**Task.** Return the number of nodes on the longest path from the root down to a leaf.

**Examples.**
```text
root = [3, 9, 20, None, None, 15, 7]
-> 3

root = [1, None, 2]
-> 2
```

**Assume.** up to 10^4 nodes.

**Aim for.** O(n) time.

**Edge cases to test.** empty tree (0); a single node; a long chain (watch recursion depth).

<details><summary>Hint 1 (open only after your 20 minutes)</summary>

depth(node) = 1 + max(depth(left), depth(right)).

</details>

<details><summary>Hint 2 (open only after your 20 minutes)</summary>

Also solve it with BFS, counting levels.

</details>

Create the file:
```bash
python tools/new_problem.py "Maximum Depth of Binary Tree" --topic trees --difficulty easy
```

### 30. Same Tree
`easy` · `trees`

**Task.** Return `True` if two binary trees have the same shape and the same value at every position.

**Examples.**
```text
p = [1, 2, 3], q = [1, 2, 3]
-> True

p = [1, 2], q = [1, None, 2]
-> False
```

**Assume.** up to 100 nodes.

**Aim for.** O(n) time.

**Edge cases to test.** both empty; same values but different shape; same shape but one different value.

<details><summary>Hint 1 (open only after your 20 minutes)</summary>

Compare the two roots, then the two left subtrees, then the two right subtrees.

</details>

<details><summary>Hint 2 (open only after your 20 minutes)</summary>

Handle the cases 'both empty' and 'only one empty' before comparing values.

</details>

Create the file:
```bash
python tools/new_problem.py "Same Tree" --topic trees --difficulty easy
```

## Day 16

### 31. Binary Tree Level Order Traversal
`medium` · `trees`

**Task.** Return the values of a binary tree level by level, left to right, as a list of lists.

**Examples.**
```text
root = [3, 9, 20, None, None, 15, 7]
-> [[3], [9, 20], [15, 7]]
```

**Assume.** up to 2000 nodes.

**Aim for.** O(n) time.

**Edge cases to test.** empty tree (returns []); a single node; a skewed tree.

<details><summary>Hint 1 (open only after your 20 minutes)</summary>

Use a queue (BFS).

</details>

<details><summary>Hint 2 (open only after your 20 minutes)</summary>

At the start of each level, remember how many nodes are in the queue; process exactly that many.

</details>

Create the file:
```bash
python tools/new_problem.py "Binary Tree Level Order Traversal" --topic trees --difficulty medium
```

### 32. Validate Binary Search Tree
`medium` · `trees`

**Task.** Return `True` if the tree is a valid binary search tree: for every node, all values in its left subtree are strictly smaller and all values in its right subtree are strictly greater.

**Examples.**
```text
root = [2, 1, 3]
-> True

root = [5, 1, 4, None, None, 3, 6]
-> False
```

**Assume.** up to 10^4 nodes, values may be very large or small.

**Aim for.** O(n) time.

**Edge cases to test.** duplicate values; a single node; values equal to the bounds of the integer range.

<details><summary>Hint 1 (open only after your 20 minutes)</summary>

Comparing a node only with its parent is not enough. In the second example, 3 is smaller than its parent 4, but it sits in the right subtree of 5.

</details>

<details><summary>Hint 2 (open only after your 20 minutes)</summary>

Carry an allowed range (low, high) down the recursion. Or check that an in-order traversal is strictly increasing.

</details>

Create the file:
```bash
python tools/new_problem.py "Validate Binary Search Tree" --topic trees --difficulty medium
```

## Day 17

### 33. Lowest Common Ancestor of a BST
`medium` · `trees`

**Task.** Given a binary search tree and two values `p` and `q` that are in it, return the value of their lowest common ancestor: the deepest node that has both as descendants (a node counts as its own descendant).

**Examples.**
```text
root = [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], p = 2, q = 8
-> 6

root = [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], p = 2, q = 4
-> 2
```

**Assume.** all values are distinct.

**Aim for.** O(height) time.

**Edge cases to test.** one of the two values is the ancestor of the other; p equals q; the root is the answer.

<details><summary>Hint 1 (open only after your 20 minutes)</summary>

Use the BST property instead of searching the whole tree.

</details>

<details><summary>Hint 2 (open only after your 20 minutes)</summary>

If both values are smaller than the current node, go left; if both are larger, go right; otherwise the current node is the answer.

</details>

Create the file:
```bash
python tools/new_problem.py "Lowest Common Ancestor of a BST" --topic trees --difficulty medium
```

### 34. Kth Smallest Element in a BST
`medium` · `trees`

**Task.** Return the `k`-th smallest value (counting from 1) in a binary search tree.

**Examples.**
```text
root = [3, 1, 4, None, 2], k = 1
-> 1

root = [5, 3, 6, 2, 4, None, None, 1], k = 3
-> 3
```

**Assume.** 1 <= k <= number of nodes.

**Aim for.** O(h + k) time.

**Edge cases to test.** k = 1; k = number of nodes; a tree that is only a right chain.

<details><summary>Hint 1 (open only after your 20 minutes)</summary>

What order does an in-order traversal visit the values of a BST?

</details>

<details><summary>Hint 2 (open only after your 20 minutes)</summary>

Traverse in order and stop as soon as you have visited k nodes. An iterative version with an explicit stack stops early cleanly.

</details>

Create the file:
```bash
python tools/new_problem.py "Kth Smallest Element in a BST" --topic trees --difficulty medium
```

## Day 18

### 35. Number of Islands
`medium` · `graphs`

**Task.** A grid contains `'1'` (land) and `'0'` (water). An island is a group of land cells connected up, down, left or right. Return the number of islands.

**Examples.**
```text
grid = ['11110', '11010', '11000', '00000']
-> 1

grid = ['11000', '11000', '00100', '00011']
-> 3
```

**Assume.** up to 300 x 300.

**Aim for.** O(rows * cols) time.

**Edge cases to test.** all water; all land; a 1 x 1 grid; a large grid (recursion depth for DFS).

<details><summary>Hint 1 (open only after your 20 minutes)</summary>

Scan every cell. When you find land you have not visited, you have found a new island.

</details>

<details><summary>Hint 2 (open only after your 20 minutes)</summary>

Flood-fill that whole island (DFS or BFS) so you never count it again. Decide how to mark cells visited, and what that costs.

</details>

Create the file:
```bash
python tools/new_problem.py "Number of Islands" --topic graphs --difficulty medium
```

### 36. Max Area of Island
`medium` · `graphs`

**Task.** A grid contains `1` (land) and `0` (water). Return the area (number of cells) of the largest island, or 0 if there is none. Cells connect up, down, left and right.

**Examples.**
```text
grid = [[0, 1, 0], [1, 1, 0], [0, 0, 1]]
-> 3

grid = [[0, 0, 0]]
-> 0
```

**Assume.** up to 50 x 50.

**Aim for.** O(rows * cols) time.

**Edge cases to test.** no land; the whole grid is one island; diagonal cells do not connect.

<details><summary>Hint 1 (open only after your 20 minutes)</summary>

Same flood fill as Number of Islands.

</details>

<details><summary>Hint 2 (open only after your 20 minutes)</summary>

Let the fill return the number of cells it visited.

</details>

Create the file:
```bash
python tools/new_problem.py "Max Area of Island" --topic graphs --difficulty medium
```

### 37. Rotting Oranges
`medium` · `graphs`

**Task.** A grid contains `0` (empty), `1` (fresh orange) and `2` (rotten orange). Every minute, each fresh orange next to a rotten one (up, down, left, right) becomes rotten. Return the minimum number of minutes until no fresh orange remains, or -1 if that is impossible.

**Examples.**
```text
grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
-> 4

grid = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
-> -1

grid = [[0, 2]]
-> 0
```

**Assume.** up to 10 x 10.

**Aim for.** O(rows * cols) time.

**Edge cases to test.** no fresh oranges (answer 0); a fresh orange that can never be reached; no rotten oranges at all.

<details><summary>Hint 1 (open only after your 20 minutes)</summary>

The rot spreads from all rotten oranges at the same time.

</details>

<details><summary>Hint 2 (open only after your 20 minutes)</summary>

Use a multi-source BFS: put every rotten orange in the queue first, then count the BFS levels. Afterwards, check that no fresh orange is left.

</details>

Create the file:
```bash
python tools/new_problem.py "Rotting Oranges" --topic graphs --difficulty medium
```

## Day 19

### 38. Clone Graph
`medium` · `graphs`

**Task.** Given one node of a connected, undirected graph (each node has a value and a list of neighbours), return a deep copy of the whole graph. In examples, the graph is written as an adjacency list: entry `i` lists the neighbours of the node with value `i + 1`. Your tests should check the structure matches and that no node object is shared with the original.

**Examples.**
```text
adjacency = [[2, 4], [1, 3], [2, 4], [1, 3]]
-> [[2, 4], [1, 3], [2, 4], [1, 3]]
```

**Assume.** up to 100 nodes.

**Aim for.** O(nodes + edges) time.

**Edge cases to test.** a single node with no neighbours; an empty graph (None); a graph with a cycle.

<details><summary>Hint 1 (open only after your 20 minutes)</summary>

You need a way to avoid copying the same node twice, and to find the copy of a node you have already made.

</details>

<details><summary>Hint 2 (open only after your 20 minutes)</summary>

A dictionary from original node to its copy does both jobs: create the copy the first time you see a node, then link neighbours.

</details>

Create the file:
```bash
python tools/new_problem.py "Clone Graph" --topic graphs --difficulty medium
```

### 39. Course Schedule
`medium` · `graphs`

**Task.** There are `num_courses` courses, numbered `0` to `num_courses - 1`. A pair `[a, b]` in `prerequisites` means you must take course `b` before course `a`. Return `True` if you can finish all courses.

**Examples.**
```text
num_courses = 2, prerequisites = [[1, 0]]
-> True

num_courses = 2, prerequisites = [[1, 0], [0, 1]]
-> False
```

**Assume.** up to 2000 courses.

**Aim for.** O(courses + prerequisites) time.

**Edge cases to test.** no prerequisites; a course that requires itself ([[0, 0]]); several disconnected groups of courses.

<details><summary>Hint 1 (open only after your 20 minutes)</summary>

You can finish exactly when the prerequisite graph has no cycle.

</details>

<details><summary>Hint 2 (open only after your 20 minutes)</summary>

Detect it with a DFS that tracks three states (unvisited, in progress, done), or with Kahn's algorithm using in-degrees.

</details>

Create the file:
```bash
python tools/new_problem.py "Course Schedule" --topic graphs --difficulty medium
```

## Day 20

### 40. Pacific Atlantic Water Flow
`medium` · `graphs`

**Task.** `heights` is a grid of heights. Water flows from a cell to a neighbour (up, down, left, right) whose height is less than or equal to the current cell. The Pacific Ocean touches the top and left edges; the Atlantic touches the bottom and right edges. Return every cell `[row, col]` from which water can reach both oceans.

**Examples.**
```text
heights = [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]
-> [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]
```

**Assume.** up to 200 x 200.

**Aim for.** O(rows * cols) time.

**Edge cases to test.** a single cell; a completely flat grid; a single row.

<details><summary>Hint 1 (open only after your 20 minutes)</summary>

Simulating water from every cell is too slow. Think backwards.

</details>

<details><summary>Hint 2 (open only after your 20 minutes)</summary>

Start from each ocean's border and move to neighbours that are at least as high; the answer is the cells reached from both oceans.

</details>

Create the file:
```bash
python tools/new_problem.py "Pacific Atlantic Water Flow" --topic graphs --difficulty medium
```

After this one, revise the problems you marked with hints.

## Day 21

**Week 3 timed session.** Pick three you have not solved, set a 90-minute timer, and use no hints. Search the names below on LeetCode (statements are not reproduced here):

- Binary Tree Right Side View
- Count Good Nodes in Binary Tree
- Construct Binary Tree from Preorder and Inorder Traversal
- Surrounded Regions
