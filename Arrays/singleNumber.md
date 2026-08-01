---
title: Single Number
topic: Bit Manipulation
pattern: Running XOR
difficulty: Easy
status: Solved
date: 2026-08-01
---

# 005. Single Number

## 📅 Date

1 August 2026

---

# Problem

Given a non-empty array `nums`, every element appears **exactly twice** except for one element, which appears only once.

Return that single element.

The solution must run in:

- **O(n)** time
- **O(1)** extra space

Example:

```python
nums = [4,1,2,1,2]

Output:
4
```

---

# My Initial Thought (Frequency Counting)

My first instinct was to somehow count how many times each number appeared.

However, I quickly realized that a single variable cannot remember the frequency of multiple distinct numbers.

The natural solution would be to use a **hash map (dictionary)** to store frequencies.

Example:

```text
4 → 1
1 → 2
2 → 2
```

Then return the number whose frequency is `1`.

Although this works, it requires extra space.

---

# Why Isn't This Optimal?

Using a dictionary gives:

- Time: **O(n)**
- Space: **O(n)**

But the problem specifically asks for:

- Linear time
- **Constant extra space**

This means the interviewer expects another approach.

---

# Key Observation 💡

Every number appears exactly twice except one.

Bitwise XOR has four important properties:

```text
x ^ x = 0
x ^ 0 = x
0 ^ x = x
XOR is commutative and associative
```

Because of these properties:

```text
4 ^ 1 ^ 2 ^ 1 ^ 2
```

can be rearranged as:

```text
4 ^ (1 ^ 1) ^ (2 ^ 2)
```

which becomes:

```text
4 ^ 0 ^ 0
```

which simplifies to:

```text
4
```

Every duplicate number cancels itself.

Only the unique number remains.

---

# Python Solution

```python
class Solution:
    def singleNumber(self, nums):
        ans = 0

        for num in nums:
            ans ^= num

        return ans
```

---

# Complexity

| Approach | Time | Space |
|---|---|---|
| Hash Map | O(n) | O(n) |
| XOR | O(n) | O(1) |

---

# Mistakes I Made 🚫

- Initially tried to solve it using a running count, similar to the previous problem.
- Didn't realize that one variable cannot track frequencies of multiple distinct numbers.
- Forgot that the problem requires **constant extra space**, making a frequency map non-optimal.
- Initially confused XOR with comparison rather than accumulation.
- Mixed up iterating over values and indices by writing:

```python
ans = ans ^ nums[i]
```

inside:

```python
for i in nums:
```

where `i` was already the current value.

---

# Pattern Recognition 🧠

Whenever I see:

- Every element appears exactly twice except one
- Need **O(n)** time
- Need **O(1)** extra space

Think:

> **Can duplicate values cancel each other using XOR?**

This is a classic **Running XOR** pattern.

---

# Similar Problems

- Single Number II
- Single Number III
- Missing Number (XOR Approach)
- Find the Duplicate Number (different pattern)
- Bitwise XOR Basics

---

# Revision Notes (30-Second Recall)

### XOR Properties

```text
x ^ x = 0
x ^ 0 = x
0 ^ x = x
```

XOR is:

- Commutative
- Associative

Algorithm:

```python
ans = 0

for num in nums:
    ans ^= num

return ans
```

Remember:

- Every duplicate cancels itself.
- The unique element remains.

---

## ⭐ Confidence Level

Before solving: ⭐⭐☆☆☆

After solving: ⭐⭐⭐⭐⭐

Need one more revision?

**Yes — revise once after learning Bit Manipulation basics so the XOR intuition becomes second nature.**