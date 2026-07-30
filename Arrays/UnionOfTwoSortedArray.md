---
title: Union of Two Sorted Arrays
topic: Arrays
pattern: Two Pointers
difficulty: Medium
status: Solved
date: 2026-07-30
---

# 002. Union of Two Sorted Arrays

## 📅 Date

30 July 2026

---

# Problem

Given two sorted arrays `a[]` and `b[]`, which may contain duplicate elements, return the union of both arrays in sorted order.

The union should contain **only distinct elements**.

Example:

```python
a = [2, 2, 3, 4, 5]
b = [1, 1, 2, 3, 4]

Output:
[1, 2, 3, 4, 5]
```

---

# My Initial Thought (Brute Force)

My first thought was:

- Traverse both arrays.
- Remove duplicates from each array.
- Store all distinct elements in a new array.

Then I realized this doesn't efficiently merge the two arrays, and I was not making use of the fact that **both arrays are already sorted**.

---

# Why Isn't This Optimal?

A naive solution could insert all elements into a set and then sort the result.

Although it works, it ignores the important property that the arrays are already sorted.

Since both arrays are sorted, we can process them in a single traversal using **two pointers**, avoiding unnecessary work.

---

# Key Observation 💡

The important insight is:

> At every step, the smaller of the two current elements is guaranteed to be the next smallest element in the union.

If:

- `a[i] < b[j]` → add `a[i]` and move `i`
- `a[i] > b[j]` → add `b[j]` and move `j`
- `a[i] == b[j]` → add the element once and move both pointers

Since duplicates are adjacent in sorted arrays, before adding an element we only need to check whether it is already the last element in the answer.

---

# Python Solution

```python
class Solution:
    def findUnion(self, a, b):
        ans = []
        i = 0
        j = 0

        while i < len(a) and j < len(b):

            if a[i] < b[j]:
                if not ans or ans[-1] != a[i]:
                    ans.append(a[i])
                i += 1

            elif a[i] > b[j]:
                if not ans or ans[-1] != b[j]:
                    ans.append(b[j])
                j += 1

            else:
                if not ans or ans[-1] != a[i]:
                    ans.append(a[i])
                i += 1
                j += 1

        while i < len(a):
            if not ans or ans[-1] != a[i]:
                ans.append(a[i])
            i += 1

        while j < len(b):
            if not ans or ans[-1] != b[j]:
                ans.append(b[j])
            j += 1

        return ans
```

---

# Complexity

| Approach | Time | Space |
|---|---|---|
| Using Set | O((n+m) log(n+m)) | O(n+m) |
| Two Pointers | O(n+m) | O(1) auxiliary (excluding output) |

---

# Mistakes I Made 🚫

- Initially focused only on removing duplicates instead of merging the arrays.
- Thought I could solve it using `for` loops, but pointer movement is dynamic.
- Forgot that when `a[i] == b[j]`, **both pointers** must move.
- Forgot to process the remaining elements after one array finishes.
- Didn't initially realize that duplicates can occur within the same array as well.
- Mixed up Python syntax while focusing on the algorithm (`append`, `null`, `empty`, etc.).

---

# Pattern Recognition 🧠

Whenever I see:

- Two **sorted arrays**
- Need to merge, union, or intersect them
- Want a linear-time solution

Think:

> **Can I solve this using Two Pointers by traversing both arrays together?**

The same idea is used in the **Merge step of Merge Sort**.

---

# Similar Problems

- Intersection of Two Sorted Arrays
- Merge Two Sorted Arrays
- Remove Duplicates from Sorted Array
- Merge Sorted Array (LeetCode 88)
- Find Common Elements in Three Sorted Arrays

---

# Revision Notes (30-Second Recall)

- Create two pointers: `i` and `j`.
- Compare `a[i]` and `b[j]`.
- Move the pointer pointing to the smaller element.
- If both are equal, add once and move both pointers.
- Before every append, check:
  ```python
  if not ans or ans[-1] != current:
  ```
- Don't forget to process the remaining elements after the main loop.

---

## ⭐ Confidence Level

Before solving: ⭐☆☆☆☆
After solving: ⭐⭐⭐⭐☆

Need one more revision? **Yes**