---
title: Linear Search & Binary Search
topic: Arrays
pattern: Binary Search
difficulty: Easy
status: Solved
date: 2026-07-29
---

# 001. Linear Search & Binary Search

## 📅 Date

29 July 2026

---

# Problem

Given a sorted array `arr[]` and an integer `k`, return `True` if `k` exists in the array; otherwise return `False`.

Example:

```python
arr = [1, 2, 3, 4, 6]
k = 6

Output: True
```

---

# My Initial Thought (Brute Force)

My first instinct was to use **Linear Search**.

- Traverse the array from left to right.
- Compare every element with `k`.
- Return `True` if found.
- Otherwise return `False`.

### Code

```python
class Solution:
    def binarySearch(self, arr, k):
        for i in range(len(arr)):
            if arr[i] == k:
                return True
        return False
```

### Complexity

- Time: **O(n)**
- Space: **O(1)**

---

# Why Isn't This Optimal?

The array is already **sorted**. With Linear Search, I may still check every element, which is slow at scale. A sorted array gives extra information I should use.

---

# Key Observation 💡

Since the array is sorted:

- If the middle element is **smaller** than `k`, the answer **cannot** be in the left half.
- If the middle element is **greater** than `k`, the answer **cannot** be in the right half.

Every comparison removes **half of the remaining search space**. This is the intuition behind **Binary Search**.

---

# Python Solution

```python
class Solution:
    def binarySearch(self, arr, k):
        low = 0
        high = len(arr) - 1

        while low <= high:
            mid = (low + high) // 2

            if arr[mid] == k:
                return True
            elif arr[mid] < k:
                low = mid + 1
            else:
                high = mid - 1

        return False
```

---

# Complexity

| Approach | Time | Space |
|---|---|---|
| Linear Search | O(n) | O(1) |
| Binary Search | O(log n) | O(1) |

---

# Mistakes I Made 🚫

- Used Linear Search first without noticing the sorted property.
- Confused **indices** with **values**.
- Wrote `high = arr[-1]` instead of `len(arr) - 1`.
- Compared `k` with `mid` instead of `arr[mid]`.
- Forgot to recalculate `mid` after updating `low`/`high`.
- Thought the loop should stop at `low == high` — the last element still needs checking.

---

# Pattern Recognition 🧠

Whenever I see a **sorted array** + search for an element + "faster than O(n)", think:
> **Can Binary Search be applied here?**

---

# Similar Problems

- First Occurrence
- Last Occurrence
- Count Occurrences
- Search Insert Position
- Floor and Ceil
- Search in Rotated Sorted Array

---

# Revision Notes (30-Second Recall)

- `low`/`high` always store **indices**, never values.
- Compare `arr[mid]` with `k`.
- Continue while `low <= high`.
- Return `False` if the search space becomes empty.

---

## ⭐ Confidence Level

Before solving: ⭐☆☆☆☆
After solving: ⭐⭐⭐⭐☆

Need one more revision? **Yes**