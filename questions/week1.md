# Week 1: arrays, hashing, two pointers, sliding window

Questions written in my own words for the problems in [PLAN.md](../PLAN.md). Every example output was checked against a reference solution, but the original problem pages may differ in small details (limits, return format). When in doubt, follow the original page.

Rules: think for 20 minutes first, open one hint at a time, and mark `Hints used` honestly in the file header.

## Day 1

### 1. Two Sum
`easy` · `arrays-hashing`

**Task.** Given a list of integers `nums` and an integer `target`, return the indices of the two elements that add up to `target`. Exactly one valid pair exists, and an element cannot be used twice.

**Examples.**
```text
nums = [2, 7, 11, 15], target = 9
-> [0, 1]

nums = [3, 2, 4], target = 6
-> [1, 2]
```

**Assume.** up to 10^4 numbers, values may be negative.

**Aim for.** O(n) time.

**Edge cases to test.** two equal numbers ([3, 3], target 6); negative numbers; the pair is at the very end.

<details><summary>Hint 1 (open only after your 20 minutes)</summary>

What do you need to have seen already to complete a pair at the current element?

</details>

<details><summary>Hint 2 (open only after your 20 minutes)</summary>

Store each value and its index in a dictionary while you scan once.

</details>

Create the file:
```bash
python tools/new_problem.py "Two Sum" --topic arrays-hashing --difficulty easy
```

### 2. Contains Duplicate
`easy` · `arrays-hashing`

**Task.** Return `True` if any value appears at least twice in `nums`, otherwise `False`.

**Examples.**
```text
nums = [1, 2, 3, 1]
-> True

nums = [1, 2, 3, 4]
-> False
```

**Assume.** up to 10^5 numbers.

**Aim for.** O(n) time.

**Edge cases to test.** one element; all elements equal.

<details><summary>Hint 1 (open only after your 20 minutes)</summary>

A set remembers what you have already seen.

</details>

<details><summary>Hint 2 (open only after your 20 minutes)</summary>

You can stop the moment you see a repeat. Compare that with building the whole set first.

</details>

Create the file:
```bash
python tools/new_problem.py "Contains Duplicate" --topic arrays-hashing --difficulty easy
```

### 3. Valid Anagram
`easy` · `arrays-hashing`

**Task.** Given two strings `s` and `t`, return `True` if `t` uses exactly the same letters as `s` with the same counts (the order may differ).

**Examples.**
```text
s = 'listen', t = 'silent'
-> True

s = 'rat', t = 'car'
-> False
```

**Assume.** lowercase letters, up to 5 * 10^4 characters.

**Aim for.** O(n) time.

**Edge cases to test.** different lengths; empty strings; same letters, different counts ('aab' vs 'abb').

<details><summary>Hint 1 (open only after your 20 minutes)</summary>

Two words are anagrams exactly when their letter counts match.

</details>

<details><summary>Hint 2 (open only after your 20 minutes)</summary>

Count with a dictionary or `collections.Counter`. Check the lengths first.

</details>

Create the file:
```bash
python tools/new_problem.py "Valid Anagram" --topic arrays-hashing --difficulty easy
```

## Day 2

### 4. Group Anagrams
`medium` · `arrays-hashing`

**Task.** Given a list of strings, group the words that are anagrams of each other. Return the groups in any order.

**Examples.**
```text
words = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
-> [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
```

**Assume.** up to 10^4 words of up to 100 lowercase letters.

**Aim for.** O(n * k log k), or O(n * k) with letter counts.

**Edge cases to test.** an empty string; a single word; no anagrams at all.

<details><summary>Hint 1 (open only after your 20 minutes)</summary>

What do all anagrams of one word have in common?

</details>

<details><summary>Hint 2 (open only after your 20 minutes)</summary>

Use that shared property as a dictionary key: the sorted letters, or a tuple of 26 counts.

</details>

Create the file:
```bash
python tools/new_problem.py "Group Anagrams" --topic arrays-hashing --difficulty medium
```

### 5. Top K Frequent Elements
`medium` · `arrays-hashing`

**Task.** Given `nums` and an integer `k`, return the `k` values that occur most often. The answer is unique and may be in any order.

**Examples.**
```text
nums = [1, 1, 1, 2, 2, 3], k = 2
-> [1, 2]
```

**Assume.** 1 <= k <= number of distinct values.

**Aim for.** better than O(n log n): O(n) with buckets, or O(n log k) with a heap.

**Edge cases to test.** k equals the number of distinct values; negative numbers; a single distinct value.

<details><summary>Hint 1 (open only after your 20 minutes)</summary>

Count the occurrences first.

</details>

<details><summary>Hint 2 (open only after your 20 minutes)</summary>

A value can occur at most n times, so you can bucket values by their count and read the buckets from the top.

</details>

Create the file:
```bash
python tools/new_problem.py "Top K Frequent Elements" --topic arrays-hashing --difficulty medium
```

### 6. Product of Array Except Self
`medium` · `arrays-hashing`

**Task.** Return a list `answer` where `answer[i]` is the product of every element of `nums` except `nums[i]`. Do not use division.

**Examples.**
```text
nums = [1, 2, 3, 4]
-> [24, 12, 8, 6]

nums = [1, 0, 3]
-> [0, 3, 0]
```

**Assume.** at least 2 numbers; every prefix and suffix product fits in a normal integer.

**Aim for.** O(n) time, O(1) extra space besides the output.

**Edge cases to test.** one zero; two zeros; negative numbers.

<details><summary>Hint 1 (open only after your 20 minutes)</summary>

answer[i] = (product of everything to the left) * (product of everything to the right).

</details>

<details><summary>Hint 2 (open only after your 20 minutes)</summary>

Fill `answer` with the left products in one pass, then multiply in the right products on a backward pass.

</details>

Create the file:
```bash
python tools/new_problem.py "Product of Array Except Self" --topic arrays-hashing --difficulty medium
```

## Day 3

### 7. Valid Palindrome
`easy` · `two-pointers`

**Task.** A phrase is a palindrome if, after lowercasing it and removing everything that is not a letter or digit, it reads the same forwards and backwards. Return `True` or `False`.

**Examples.**
```text
s = 'A man, a plan, a canal: Panama'
-> True

s = 'race a car'
-> False
```

**Assume.** up to 2 * 10^5 characters.

**Aim for.** O(n) time, O(1) space.

**Edge cases to test.** empty string; only punctuation (' ,.') counts as a palindrome; digits mixed with letters.

<details><summary>Hint 1 (open only after your 20 minutes)</summary>

Put one pointer at each end.

</details>

<details><summary>Hint 2 (open only after your 20 minutes)</summary>

Move each pointer inward, skipping characters that do not count, and compare lowercase versions.

</details>

Create the file:
```bash
python tools/new_problem.py "Valid Palindrome" --topic two-pointers --difficulty easy
```

### 8. Two Sum II (sorted input)
`medium` · `two-pointers`

**Task.** `numbers` is sorted in ascending order. Return the 1-based indices of two different elements that add up to `target`. Exactly one solution exists. Use only O(1) extra space.

**Examples.**
```text
numbers = [2, 7, 11, 15], target = 9
-> [1, 2]
```

**Assume.** up to 3 * 10^4 numbers.

**Aim for.** O(n) time, O(1) space.

**Edge cases to test.** negative numbers; duplicates; the pair is the first and last element.

<details><summary>Hint 1 (open only after your 20 minutes)</summary>

Because the list is sorted, you know what happens to the sum when you move the left pointer right, or the right pointer left.

</details>

<details><summary>Hint 2 (open only after your 20 minutes)</summary>

Start with pointers at both ends; move whichever one fixes the sum being too small or too large.

</details>

Create the file:
```bash
python tools/new_problem.py "Two Sum II (sorted input)" --topic two-pointers --difficulty medium
```

### 9. 3Sum
`medium` · `two-pointers`

**Task.** Return all unique triplets `[a, b, c]` from `nums` with `a + b + c == 0`. The same triplet must not appear twice in the result. The order of triplets, and of numbers inside a triplet, does not matter.

**Examples.**
```text
nums = [-1, 0, 1, 2, -1, -4]
-> [[-1, -1, 2], [-1, 0, 1]]

nums = [0, 0, 0, 0]
-> [[0, 0, 0]]
```

**Assume.** 3 to 3000 numbers.

**Aim for.** O(n^2) time.

**Edge cases to test.** no valid triplet; all zeros; many repeated values.

<details><summary>Hint 1 (open only after your 20 minutes)</summary>

Sort first. Fix one number, then you need two others that sum to its negative: that is Two Sum II.

</details>

<details><summary>Hint 2 (open only after your 20 minutes)</summary>

Skip repeated values at every level so you never produce a duplicate triplet.

</details>

Create the file:
```bash
python tools/new_problem.py "3Sum" --topic two-pointers --difficulty medium
```

## Day 4

### 10. Container With Most Water
`medium` · `two-pointers`

**Task.** `heights[i]` is the height of a vertical line at position `i`. Pick two lines that, with the x-axis, hold the most water. Return that maximum area (distance between the lines times the shorter height).

**Examples.**
```text
heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
-> 49
```

**Assume.** 2 to 10^5 lines.

**Aim for.** O(n) time.

**Edge cases to test.** exactly two lines; all lines the same height; heights in descending order.

<details><summary>Hint 1 (open only after your 20 minutes)</summary>

Start with the widest container, using both ends.

</details>

<details><summary>Hint 2 (open only after your 20 minutes)</summary>

Moving the taller line inward can never help. Which pointer should you move, and why?

</details>

Create the file:
```bash
python tools/new_problem.py "Container With Most Water" --topic two-pointers --difficulty medium
```

### 11. Best Time to Buy and Sell Stock
`easy` · `arrays-hashing`

**Task.** `prices[i]` is a stock's price on day `i`. Choose one day to buy and a later day to sell to maximise profit. Return the best profit, or 0 if no profit is possible.

**Examples.**
```text
prices = [7, 1, 5, 3, 6, 4]
-> 5

prices = [7, 6, 4, 3, 1]
-> 0
```

**Assume.** up to 10^5 days.

**Aim for.** O(n) time, O(1) space.

**Edge cases to test.** a single day; strictly increasing prices; all prices equal.

<details><summary>Hint 1 (open only after your 20 minutes)</summary>

At each day, what is the best day you could have bought on?

</details>

<details><summary>Hint 2 (open only after your 20 minutes)</summary>

Track the lowest price seen so far and the best profit so far in one pass.

</details>

Create the file:
```bash
python tools/new_problem.py "Best Time to Buy and Sell Stock" --topic arrays-hashing --difficulty easy
```

## Day 5

### 12. Longest Substring Without Repeating Characters
`medium` · `sliding-window`

**Task.** Return the length of the longest substring of `s` that contains no repeated character.

**Examples.**
```text
s = 'abcabcbb'
-> 3

s = 'bbbbb'
-> 1

s = 'pwwkew'
-> 3
```

**Assume.** up to 5 * 10^4 characters, any characters.

**Aim for.** O(n) time.

**Edge cases to test.** empty string (answer 0); all characters unique; spaces and symbols.

<details><summary>Hint 1 (open only after your 20 minutes)</summary>

Keep a window [left, right] that has no repeats.

</details>

<details><summary>Hint 2 (open only after your 20 minutes)</summary>

When the new character is already in the window, how far must `left` move? Store each character's last index.

</details>

Create the file:
```bash
python tools/new_problem.py "Longest Substring Without Repeating Characters" --topic sliding-window --difficulty medium
```

### 13. Longest Repeating Character Replacement
`medium` · `sliding-window`

**Task.** Given an uppercase string `s` and an integer `k`, you may change at most `k` characters to any other uppercase letter. Return the length of the longest substring that can be turned into one repeated letter.

**Examples.**
```text
s = 'AABABBA', k = 1
-> 4

s = 'ABAB', k = 2
-> 4
```

**Assume.** up to 10^5 characters.

**Aim for.** O(n) time.

**Edge cases to test.** k = 0; k >= length of s; a single character.

<details><summary>Hint 1 (open only after your 20 minutes)</summary>

A window is acceptable when (window length - count of its most frequent letter) <= k.

</details>

<details><summary>Hint 2 (open only after your 20 minutes)</summary>

Grow the window to the right; when it is not acceptable, slide the left edge by one.

</details>

Create the file:
```bash
python tools/new_problem.py "Longest Repeating Character Replacement" --topic sliding-window --difficulty medium
```

## Day 6

Revise every problem where you needed hints. Re-implement each one from scratch without looking at your old file.

## Day 7

**Week 1 timed session.** Pick three you have not solved, set a 90-minute timer, and use no hints. Search the names below on LeetCode (statements are not reproduced here):

- Longest Consecutive Sequence
- Subarray Sum Equals K
- Permutation in String
- Minimum Window Substring (harder)
