---
title: Missing Number
topic: Arrays
pattern: Mathematical Formula
difficulty: Easy
status: Solved
date: 2026-07-31
---

# 003. Missing Number

## 📅 Date

31 July 2026

---

# Problem

Given an array `nums` containing `n` distinct numbers in the range `[0, n]`, return the only number that is missing from the array.

Example:

```python
nums = [3, 0, 1]

Output:
2
```

---

# My Initial Thought (Brute Force)

My first instinct was to sort the array.

- Sort the array.
- Traverse it from left to right.
- Compare each element with its expected value.
- The first mismatch would be the missing number.

Although this approach works, sorting takes extra time.

---

# Why Isn't This Optimal?

Sorting the array requires **O(n log n)** time.

The problem already tells us that:

- The numbers are in the range **0 to n**.
- Exactly **one number is missing**.
- Every other number appears exactly once.

This means we can use mathematics instead of sorting.

---

# Key Observation 💡

The numbers should form the sequence:

```text
0, 1, 2, 3, ..., n
```

The sum of this sequence is:

```python
n * (n + 1) // 2
```

If we calculate:

- Expected Sum = Sum of numbers from `0` to `n`
- Actual Sum = Sum of all elements in the array

Then:

```text
Missing Number = Expected Sum - Actual Sum
```

Example:

```python
nums = [3, 0, 1]

Expected Sum = 0 + 1 + 2 + 3 = 6
Actual Sum = 3 + 0 + 1 = 4

Missing Number = 6 - 4 = 2
```

---

# Python Solution

```python
class Solution:
    def missingNumber(self, nums):
        n = len(nums)

        expected = n * (n + 1) // 2
        actual = sum(nums)

        return expected - actual
```

---

# Complexity

| Approach | Time | Space |
|---|---|---|
| Sorting | O(n log n) | O(1) |
| Sum Formula | O(n) | O(1) |

---

# Mistakes I Made 🚫

- My first instinct was to sort the array instead of using the given range information.
- Initially overlooked that the numbers are guaranteed to be from **0 to n**.
- Confused whether the formula should use `len(nums)` or `len(nums) - 1`.
- Didn't realize that the array has **n elements**, but the expected numbers are from **0 to n** (a total of `n + 1` numbers).

---

# Pattern Recognition 🧠

Whenever I see:

- Numbers forming a complete consecutive range
- Exactly one number missing
- Need an **O(n)** solution with **O(1)** space

Think:

> **Can I calculate the expected value mathematically and compare it with the actual value?**

---

# Similar Problems

- Missing Number (XOR Approach)
- Find the Duplicate Number
- Set Mismatch
- Find All Numbers Disappeared in an Array
- First Missing Positive

---

# Revision Notes (30-Second Recall)

- The array length is `n`.
- Expected numbers are from `0` to `n`.
- Expected Sum:
  ```python
  n * (n + 1) // 2
  ```
- Actual Sum:
  ```python
  sum(nums)
  ```
- Missing Number:
  ```python
  expected - actual
  ```
- Remember: use `n = len(nums)`, **not** `len(nums) - 1`.

---

## ⭐ Confidence Level

Before solving: ⭐⭐☆☆☆
After solving: ⭐⭐⭐⭐⭐

Need one more revision? **No (Revise once after learning the XOR approach)**