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

The array is already **sorted**.

With Linear Search, I may still check every element.

If there are **1,000,000** elements, this can be slow.

A sorted array gives extra information that I should use.

---

# Key Observation 💡

Since the array is sorted:

- If the middle element is **smaller** than `k`,
  then the answer **cannot** be in the left half.

- If the middle element is **greater** than `k`,
  then the answer **cannot** be in the right half.

Every comparison removes **half of the remaining search space**.

This is the intuition behind **Binary Search**.

---

# Binary Search Algorithm

1. Initialize `low = 0` and `high = len(arr) - 1`.
2. While `low <= high`
3. Find the middle index.
4. Compare `arr[mid]` with `k`.
5. If equal → return `True`.
6. If `k > arr[mid]` → search the right half.
7. Otherwise → search the left half.
8. If the loop finishes → return `False`.

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

### Linear Search

Time: **O(n)**

Space: **O(1)**

---

### Binary Search

Time: **O(log n)**

Space: **O(1)**

---

# Mistakes I Made 🚫

These are my personal mistakes while learning this problem.

- I used Linear Search first without thinking about the sorted property.
- I confused **indices** with **values**.
- I wrote `high = arr[-1]` instead of `len(arr) - 1`.
- I compared `k` with `mid` instead of `arr[mid]`.
- I forgot to recalculate `mid` after updating `low` or `high`.
- I returned `True` too early inside the loop.
- I initially thought the loop should stop when `low == high`, but I learned that the last remaining element still needs to be checked.

---

# Pattern Recognition 🧠

Whenever I see:

- A **sorted array**
- Search for an element
- The interviewer asks for something faster than **O(n)**

I should immediately think:

> **Can Binary Search be applied here?**

---

# Interview Takeaways

The power of Binary Search is **not finding the middle**.

The power is that **every comparison eliminates half of the remaining search space**.

---

# Similar Problems

- First Occurrence
- Last Occurrence
- Count Occurrences
- Search Insert Position
- Floor and Ceil
- Lower Bound / Upper Bound
- Search in Rotated Sorted Array

---

# Revision Notes (30-Second Recall)

- `low` and `high` always store **indices**, never values.
- Compare **`arr[mid]`** with `k`.
- If `arr[mid] < k`, move `low = mid + 1`.
- Else move `high = mid - 1`.
- Continue while `low <= high`.
- Return `False` if the search space becomes empty.

---

# What I Learned Today

Today wasn't just about Binary Search.

I learned to:

- Look for hidden clues in the problem statement (like a sorted array).
- Separate **indices** from **values**.
- Dry-run my code before assuming it's correct.
- Debug my own logic instead of immediately looking for the solution.

This is the first Binary Search I've written from scratch, so it's an important milestone in my DSA journey.