---

title: Two Sum
topic: Hash Map
pattern: Complement Lookup
difficulty: Easy
status: Solved
date: 2026-08-03
----------------

# 006. Two Sum

## 📅 Date

3 August 2026

---

# Problem

Given an array of integers `nums` and an integer `target`, return the **indices of the two numbers** that add up to the target.

You may not use the same element twice.

Each input is guaranteed to have exactly one solution.

Example:

```python
nums = [2,7,11,15]
target = 9

Output:
[0,1]
```

Because:

```text
nums[0] + nums[1] = 2 + 7 = 9
```

---

# My Initial Thought (Two Loops)

My first thought was to use **two loops** to check different combinations of elements.

For example:

```text
2 + 7
2 + 11
2 + 15
...
```

This would eventually find the pair that adds up to the target.

I correctly identified that this approach would take:

```text
O(n²)
```

because we may need to compare many pairs of elements.

---

# Improving the Approach

Instead of checking every possible combination, I realized that for every number, I can calculate exactly what number I need.

The formula is:

```text
needed = target - current_number
```

For example:

```text
target = 9
current = 2

needed = 9 - 2
needed = 7
```

So instead of searching through all other elements, I can ask:

> "Have I already seen `7`?"

---

# Important Question 🤔

At first, I wondered whether this only worked when the first number was part of the answer.

For example:

```text
nums = [2,7,11,15]
target = 18
```

The answer is:

```text
7 + 11 = 18
```

But the approach still works.

When we reach `7`:

```text
needed = 18 - 7
needed = 11
```

We haven't seen `11` yet, so we store `7`.

When we reach `11`:

```text
needed = 18 - 11
needed = 7
```

We have already seen `7`.

Therefore:

```text
7 + 11 = 18
```

The important idea is that we remember **previously seen numbers**.

---

# Choosing the Data Structure

We need to quickly store and look up:

```text
number → index
```

A Python dictionary is perfect for this.

Example:

```python
d = {
    2: 0,
    7: 1
}
```

This means:

```text
number 2 → index 0
number 7 → index 1
```

Now if we need `7`, we can quickly check:

```python
if needed in d:
```

And get its index using:

```python
d[needed]
```

---

# Key Observation 💡

For every element:

```text
needed = target - current
```

Then:

1. Check whether `needed` already exists in the dictionary.
2. If it does, we found the pair.
3. If it doesn't, store the current number and its index.

The dictionary acts as our memory of previously seen numbers.

---

# Important Detail: Check Before Store

We check for the complement **before** storing the current number.

```python
if needed in d:
    return [d[needed], i]

d[nums[i]] = i
```

This prevents using the **same element twice**.

For example:

```text
nums = [3,3]
target = 6
```

At the first `3`:

```text
needed = 3
```

But the dictionary is empty.

So we store:

```text
3 → 0
```

At the second `3`:

```text
needed = 3
```

Now `3` already exists in the dictionary.

So we return:

```text
[0,1]
```

---

# Python Solution

```python
class Solution:
    def twoSum(self, nums, target):
        d = {}

        for i in range(len(nums)):
            needed = target - nums[i]

            if needed in d:
                return [d[needed], i]

            d[nums[i]] = i
```

---

# Dry Run

Example:

```python
nums = [3,2,4]
target = 6
```

Initial:

```text
d = {}
```

### i = 0

```text
nums[i] = 3
needed = 6 - 3 = 3
```

Is `3` in `d`?

```text
No
```

Store:

```text
d = {3: 0}
```

---

### i = 1

```text
nums[i] = 2
needed = 6 - 2 = 4
```

Is `4` in `d`?

```text
No
```

Store:

```text
d = {3: 0, 2: 1}
```

---

### i = 2

```text
nums[i] = 4
needed = 6 - 4 = 2
```

Is `2` in `d`?

```text
Yes
```

Dictionary tells us:

```text
d[2] = 1
```

Current index:

```text
i = 2
```

Therefore:

```python
return [1, 2]
```

---

# Complexity

| Approach  | Time  | Space |
| --------- | ----- | ----- |
| Two Loops | O(n²) | O(1)  |
| Hash Map  | O(n)  | O(n)  |

The dictionary solution takes **O(n)** time because we process the array once and dictionary lookup is **O(1) on average**.

The trade-off is **O(n) extra space** for storing previously seen numbers.

---

# Mistakes I Made 🚫

* Initially thought I needed two loops to find combinations.
* Correctly identified that the two-loop approach would be **O(n²)**.
* Didn't immediately see that I could calculate the required complement using:

```text
target - current
```

* Initially got confused about whether the approach would work when the answer involved later elements such as `7 + 11`.
* Understood that we need a dictionary to remember previously seen numbers.
* Initially reversed the dictionary mapping by writing:

```python
d[i] = nums[i]
```

which stores:

```text
index → number
```

instead of:

```text
number → index
```

* Corrected it to:

```python
d[nums[i]] = i
```

* Initially struggled with the Python syntax for looping through indices.
* Learned that:

```python
for i in range(len(nums)):
```

gives us the index, while:

```python
nums[i]
```

gives us the current value.

* Initially wasn't sure how to check whether the required number existed in the dictionary.
* Learned:

```python
if needed in d:
```

---

# Pattern Recognition 🧠

## Pattern: Complement Lookup / Hash Map

Whenever I see a problem asking me to:

* Find two numbers that satisfy a condition
* Find a pair with a specific sum
* Check whether a required value has already appeared
* Return indices or positions
* Need fast lookup

Think:

> **"Can I calculate what I need and remember what I've already seen?"**

For Two Sum:

```text
current number
      ↓
target - current
      ↓
   needed
      ↓
Have I seen it?
```

This is the key mental model.

---

# Why Interviewers Ask This

Two Sum looks simple, but it tests an important interview skill:

> Can you improve a brute-force solution by identifying what information needs to be remembered?

A beginner often thinks:

```text
"Try every pair."
```

An interviewer wants you to eventually think:

```text
"I know exactly what partner I need.
Can I remember previous values so I can find that partner quickly?"
```

That's the transition from:

```text
Brute Force → Optimization
```

---

# Similar Problems

* Two Sum II — Input Array Is Sorted
* 3Sum
* 4Sum
* Subarray Sum Equals K
* Count Number of Pairs With Given Sum
* Contains Duplicate
* First Unique Character in a String

---

# Revision Notes (30-Second Recall)

For every number:

```python
needed = target - nums[i]
```

Check:

```python
if needed in d:
```

If found:

```python
return [d[needed], i]
```

Otherwise remember:

```python
d[nums[i]] = i
```

Mental model:

```text
Current number
      ↓
What number do I need?
      ↓
target - current
      ↓
Have I seen it?
      ↓
Yes → return indices
No  → remember current
```

Remember:

> **Don't search for every pair. Calculate the complement and look it up.**

---

## ⭐ Confidence Level

Before solving: ⭐⭐☆☆☆

After solving: ⭐⭐⭐⭐☆

Need one more revision?

**Yes — re-code Two Sum from memory once without looking at the solution.**

The main thing to make automatic is:

```text
number → index
```

and:

```text
needed = target - current
```
