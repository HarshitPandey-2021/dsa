---

title: Missing Elements
topic: Arrays / Hash Set
pattern: Range Traversal + Membership Lookup
difficulty: Easy
status: Solved
date: 2026-08-04
----------------

# Missing Elements

## Problem

Given unique integers where the smallest and largest values are present, return all integers missing between them.

Example:

```python
nums = [1, 4, 2, 5]

Output:
[3]
```

---

# My Approach

My initial thought was:

> Find the smallest and largest elements, then check which numbers are missing from that range.

I first thought about sorting the array, but realized **sorting isn't necessary**.

Then I considered:

```python
number not in nums
```

but list lookup is `O(n)`.

So I used a **set** for faster lookup.

---

# Key Idea 💡

1. Find `smallest` and `largest`.
2. Put all numbers into a set.
3. Traverse from `smallest` to `largest`.
4. If a number isn't in the set, add it to the result.

```text
nums = [1, 4, 2, 5]

range:
1 2 3 4 5
    ↑
  missing
```

---

# Python Solution

```python
class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        smallest = min(nums)
        largest = max(nums)

        seen = set(nums)
        result = []

        for i in range(smallest, largest + 1):
            if i not in seen:
                result.append(i)

        return result
```

---

# Important Python Concepts

### `set(nums)`

```python
seen = set(nums)
```

Creates:

```text
[1, 4, 2, 5]
      ↓
{1, 2, 4, 5}
```

Useful because membership lookup is approximately:

```text
O(1)
```

### `.append()`

To add an element to the end of a list:

```python
result.append(i)
```

---

# Complexity

Let `n` be the number of elements and `k` be the size of the value range.

```text
Time:  O(n + k)
Space: O(n + k)
```

The set requires `O(n)` space, and the output itself can contain up to `O(k)` missing values.

---

# Mistakes I Made 🚫

* Initially thought sorting was necessary.
* Initially used:

```python
nums.min()
nums.max()
```

but Python lists use:

```python
min(nums)
max(nums)
```

* Confused `len(nums)` with the largest **value**.
* Initially considered:

```python
for i in nums:
```

but that only visits existing elements. We need to generate the **complete range**.

* Forgot that `range()` excludes its ending value:

```python
range(smallest, largest + 1)
```

* Didn't remember `.append()` for adding an element to a list.

---

# Pattern Recognition 🧠

## Pattern: Range Traversal + Membership Lookup

When a problem says:

> "Some values are missing from a known range."

Think:

```text
Find boundaries
      ↓
Create/know the expected range
      ↓
Check whether each value exists
      ↓
Collect missing values
```

If membership checks are repeated, consider a:

```text
Set → O(1) average lookup
```

---

# Revision Notes

Remember:

```python
smallest = min(nums)
largest = max(nums)
seen = set(nums)
```

Then:

```python
for i in range(smallest, largest + 1):
    if i not in seen:
        result.append(i)
```

### Mental model

> **"What numbers should exist between min and max, and which of them don't exist?"**

---

## ⭐ Confidence Level

Before solving: ⭐⭐☆☆☆

After solving: ⭐⭐⭐⭐☆

### 🎯 Homework

Re-code this once from memory.

The important things to remember are:

```text
min/max → boundaries
set → fast lookup
range(min, max + 1) → complete range
append → collect missing values
```

---
