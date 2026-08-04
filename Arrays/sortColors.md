---

title: Sort Colors
topic: Arrays
pattern: Dutch National Flag
difficulty: Medium
status: Solved
date: 2026-08-04
----------------

# 075. Sort Colors

## 📅 Date

4 August 2026

---

# Problem

Given an array containing only `0`, `1`, and `2`, sort it in-place:

```text
0s → 1s → 2s
```

Without using `.sort()`.

Example:

```python
[2,0,2,1,1,0]

→ [0,0,1,1,2,2]
```

---

# My Initial Thought

I first thought about:

> Traverse the array, remember the positions of similar elements, then place them together.

Then I realized we only have **three possible values**, so we can organize the array using three pointers.

---

# Key Observation 💡

Maintain four regions:

```text
[ 0s | 1s | unknown | 2s ]
       ↑      ↑       ↑
      low    mid     high
```

* `low` → position where the next `0` belongs
* `mid` → scans the unknown region
* `high` → position where the next `2` belongs

---

# Pointer Rules 🧠

### If `nums[mid] == 0`

Swap `low` and `mid`.

```python
nums[low], nums[mid] = nums[mid], nums[low]
```

Then:

```python
low += 1
mid += 1
```

Because the `0` is now correctly placed.

---

### If `nums[mid] == 1`

It's already in the correct region.

```python
mid += 1
```

---

### If `nums[mid] == 2`

Swap `mid` and `high`.

```python
nums[mid], nums[high] = nums[high], nums[mid]
```

Then:

```python
high -= 1
```

**Do NOT increment `mid`.**

Why?

The element coming from `high` hasn't been examined yet.

---

# Python Solution

```python
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        low = 0
        mid = 0
        high = len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1

            elif nums[mid] == 1:
                mid += 1

            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
```

---

# Complexity

```text
Time:  O(n)
Space: O(1)
```

One pass through the array and only three pointers.

---

# Mistakes I Made 🚫

* Initially confused **pointer/index** with the **value**.
* Used conditions like:

```python
while mid == 0
```

instead of checking:

```python
nums[mid]
```

* Initially wanted separate loops for `0` and `2`.
* Initially incremented `mid` after swapping a `2`.
* Learned that the new element coming from `high` is **unprocessed**, so `mid` must stay.

---

# Pattern Recognition 🧠

## Pattern: Dutch National Flag

Think of this pattern when:

* There are only a few categories/values.
* Elements need to be grouped into regions.
* You need in-place rearrangement.
* The problem asks for **O(1) space**.
* A one-pass solution is possible.

Mental model:

```text
0 → left
1 → middle
2 → right
```

The most important rule:

> **When moving a `2` to the right, don't move `mid` because the swapped-in element is still unknown.**

---

# Revision Notes

Remember:

```text
0 → low + mid
1 → mid
2 → high
```

And:

```text
while mid <= high
```

Visual:

```text
[ 0s | 1s | UNKNOWN | 2s ]
       ↑      ↑       ↑
      low    mid     high
```

---

## ⭐ Confidence Level

Before solving: ⭐⭐☆☆☆

After solving: ⭐⭐⭐⭐☆

### 🎯 Homework

Tomorrow, code **Sort Colors from memory** without looking at the solution.

Don't memorize the code.

Remember only:

> **0 → left, 1 → middle, 2 → right.**
