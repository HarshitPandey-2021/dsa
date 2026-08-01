---
title: Max Consecutive Ones
topic: Arrays
pattern: Running Count (Streak Counting)
difficulty: Easy
status: Solved
date: 2026-08-01
---

# 004. Max Consecutive Ones

## 📅 Date

1 August 2026

---

# Problem

Given a binary array `nums`, return the maximum number of consecutive `1`s in the array.

Example:

```python
nums = [1,1,0,1,1,1]

Output:
3
```

---

# My Initial Thought

My first idea was to traverse the array once while maintaining two variables:

- `count` → stores the current streak of consecutive `1`s.
- `max_count` → stores the longest streak seen so far.

Whenever I encounter:

- `1` → increment `count`.
- `0` → reset `count` to `0`.

While traversing, continuously update `max_count` whenever the current streak becomes larger.

---

# Why Is This Optimal?

We only need to know:

- the current consecutive streak
- the maximum streak seen so far

There is no need to store previous elements or use any extra data structure.

A single traversal is enough.

---

# Key Observation 💡

At any point in the traversal, the only information that matters is:

- Current streak of consecutive `1`s
- Best streak found so far

Whenever we see:

```python
1
```

the streak grows.

Whenever we see:

```python
0
```

the streak breaks, so we reset it.

Example:

```python
nums = [1,1,0,1,1,1]

count = 1, max = 1
count = 2, max = 2
0 -> count = 0
count = 1, max = 2
count = 2, max = 2
count = 3, max = 3
```

Answer:

```text
3
```

---

# Python Solution

```python
class Solution:
    def findMaxConsecutiveOnes(self, nums):
        count = 0
        max_count = 0

        for num in nums:
            if num == 1:
                count += 1
                max_count = max(max_count, count)
            else:
                count = 0

        return max_count
```

---

# Complexity

| Approach | Time | Space |
|---|---|---|
| Single Traversal | O(n) | O(1) |

---

# Mistakes I Made 🚫

- Initially updated `max_count` by assigning `count` directly instead of keeping the maximum.
- Wrote the reset condition (`if nums[i] != 1`) inside the `if nums[i] == 1` block, making it unreachable.
- Used index-based iteration (`nums[i]`) even though iterating directly over the values is cleaner in Python.

---

# Pattern Recognition 🧠

Whenever I see:

- Longest consecutive sequence
- Current streak
- Continuous occurrences
- Need only one traversal

Think:

> **Can I maintain a running count and reset it whenever the streak breaks?**

This is a classic **Running Count / Streak Counting** pattern.

---

# Similar Problems

- Max Consecutive Ones II
- Max Consecutive Ones III
- Longest Continuous Increasing Subsequence
- Longest Substring Without Repeating Characters (extends to Sliding Window)
- Longest Repeating Character Replacement

---

# Revision Notes (30-Second Recall)

- Maintain two variables:
  ```python
  count
  max_count
  ```
- If current element is `1`:
  ```python
  count += 1
  max_count = max(max_count, count)
  ```
- If current element is `0`:
  ```python
  count = 0
  ```
- One traversal is sufficient.
- No extra space required.

---

## ⭐ Confidence Level

Before solving: ⭐⭐☆☆☆
After solving: ⭐⭐⭐⭐⭐

Need one more revision? **No (Revisit when learning Sliding Window with Max Consecutive Ones II & III.)**