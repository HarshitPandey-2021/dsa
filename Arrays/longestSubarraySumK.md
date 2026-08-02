---

title: Longest Subarray with Sum K
topic: Prefix Sum + Hash Map
pattern: Prefix Sum with Earliest Index
difficulty: Medium
status: Solved
date: 2026-08-02
----------------

# 006. Longest Subarray with Sum K

## 📅 Date

2 August 2026

---

# Problem

Given an array `arr` and an integer `k`, find the length of the **longest subarray** whose sum is exactly `k`.

If no such subarray exists, return `0`.

Example:

```python
arr = [10, 5, 2, 7, 1, -10]
k = 15

Output:
6
```

The entire array has sum `15`, so the longest subarray has length `6`.

---

# My Initial Thought

My first thought was to traverse the array and maintain a running sum.

For example:

```text
10
10 + 5 = 15
10 + 5 + 2 = 17
...
```

If the running sum equals `k`, then we found a subarray.

However, this isn't enough because the array can contain **negative numbers**.

For example, the current running sum could be `20`, but an earlier part of the array might have contributed `5`.

Then:

```text
20 - 5 = 15
```

So we need to remember previous prefix sums.

---

# Key Observation 💡

Suppose:

```text
current prefix sum = 20
k = 15
```

We want a subarray whose sum is `15`.

If an earlier prefix sum was `5`:

```text
20 - 5 = 15
```

Therefore, for every current prefix sum, we need to check:

```python
p_sum - k
```

If that prefix sum existed earlier, we found a subarray with sum `k`.

---

# Hash Map Idea

Use a dictionary to store:

```text
prefix_sum → earliest index
```

For example:

```text
10 → 0
15 → 1
17 → 2
```

The key is the prefix sum because that's what we need to search for.

The value is the index because we need it to calculate the subarray length.

---

# Why Store the Earliest Index?

Suppose the same prefix sum appears multiple times:

```text
5 → index 2
5 → index 7
```

We keep:

```text
5 → 2
```

because:

```text
subarray length = current_index - previous_index
```

Using the earliest index gives us the **longest possible subarray**.

Therefore, we should only store a prefix sum the first time we see it.

---

# Algorithm

1. Initialize `p_sum = 0`.
2. Create an empty dictionary.
3. Create `max_len = 0`.
4. Traverse the array.
5. Add the current element to `p_sum`.
6. If `p_sum == k`, the subarray from index `0` has sum `k`.
7. Check whether `p_sum - k` exists in the dictionary.
8. If it exists, calculate the subarray length.
9. Update `max_len`.
10. Store the current prefix sum only if it hasn't appeared before.
11. Return `max_len`.

---

# Python Solution

```python
class Solution:
    def longestSubarray(self, arr, k):
        p_sum = 0
        d = {}
        max_len = 0

        for i in range(len(arr)):
            p_sum += arr[i]

            if p_sum == k:
                max_len = i + 1

            if p_sum - k in d:
                length = i - d[p_sum - k]
                max_len = max(max_len, length)

            if p_sum not in d:
                d[p_sum] = i

        return max_len
```

---

# Dry Run

For:

```python
arr = [10, 5, 2, 7, 1, -10]
k = 15
```

We maintain:

```text
prefix_sum → earliest index
```

| Index | Value | Prefix Sum | Needed Sum | Found?             | Max Length |
| ----: | ----: | ---------: | ---------: | ------------------ | ---------: |
|     0 |    10 |         10 |         -5 | No                 |          0 |
|     1 |     5 |         15 |          0 | Yes, entire prefix |          2 |
|     2 |     2 |         17 |          2 | No                 |          2 |
|     3 |     7 |         24 |          9 | No                 |          2 |
|     4 |     1 |         25 |         10 | Yes                |          4 |
|     5 |   -10 |         15 |          0 | Yes, entire prefix |          6 |

The final answer is:

```text
6
```

---

# Complexity

| Approach              | Time     | Space    |
| --------------------- | -------- | -------- |
| Brute Force           | O(n²)    | O(1)     |
| Prefix Sum + Hash Map | **O(n)** | **O(n)** |

The optimized approach traverses the array once.

---

# Mistakes I Made 🚫

* Initially thought that simply checking whether the running sum equals `k` would be enough.
* Didn't initially recognize that negative numbers mean a subarray can have sum `k` even when the current prefix sum is larger than `k`.
* Initially confused the key and value in the hashmap.
* Learned that for this problem:

  ```text
  prefix_sum → index
  ```

  not:

  ```text
  index → prefix_sum
  ```
* Initially didn't know how to use `enumerate()`.
* Learned that `range(len(arr))` can be used when I need the index.
* Learned that a dictionary uses:

  ```python
  d[key] = value
  ```
* Learned that we should keep the **earliest index** for each prefix sum.

---

# Pattern Recognition 🧠

Whenever I see:

* Find a subarray with a specific sum
* Array may contain **negative numbers**
* Need an efficient solution
* Need the **longest** subarray

Think:

> **Prefix Sum + Hash Map**

The key observation is:

```text
current_prefix - previous_prefix = subarray_sum
```

So if:

```text
current_prefix - previous_prefix = k
```

then:

```text
previous_prefix = current_prefix - k
```

Therefore, search for:

```python
p_sum - k
```

in the hashmap.

---

# Why Interviewers Ask This

This problem tests whether you can move beyond:

> "I'll try every subarray."

and recognize that previous computations can be **remembered and reused**.

It also tests:

* Prefix sums
* Hash maps
* One-pass thinking
* Handling negative numbers
* Choosing what information to store
* Understanding why earliest occurrence matters

---

# Similar Problems

* Subarray Sum Equals K
* Longest Subarray with Sum 0
* Count Subarrays with Sum K
* Longest Subarray with Equal 0s and 1s
* Binary Subarray with Sum
* Two Sum — related hashmap lookup idea

---

# Revision Notes (30-Second Recall)

### Core Idea

Maintain:

```python
p_sum
```

and store:

```text
prefix_sum → earliest index
```

At every index:

```python
p_sum += arr[i]
```

Then check:

```python
p_sum - k
```

If it exists:

```python
length = i - d[p_sum - k]
```

Keep the maximum length.

Remember:

> **Current prefix − previous prefix = subarray sum**

And:

> **Keep the earliest prefix index to get the longest subarray.**

---

## ⭐ Confidence Level

Before solving: ⭐⭐☆☆☆

After solving: ⭐⭐⭐⭐☆

Need one more revision?

**Yes — revise the prefix-sum equation and hashmap logic once before solving another medium prefix-sum problem.**
