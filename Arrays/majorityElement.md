# Majority Element

---

**title:** Majority Element
**topic:** Arrays / Hash Map / Boyer-Moore Voting
**pattern:** Frequency Counting (Hash Map)
**difficulty:** Easy
**status:** Solved
**date:** 2026-08-05

---

# Problem

Given an integer array `nums`, return the **majority element**.

A majority element is the element that appears **more than ⌊n / 2⌋ times**.

It is guaranteed that a majority element always exists.

Example:

```python
nums = [2, 2, 1, 1, 1, 2, 2]

Output:
2
```

---

# My Approach

My first thought was:

> Count how many times each element appears, then return the one with the highest frequency.

I decided to use a **dictionary (hash map)** because it allows storing the frequency of every number efficiently.

---

# Key Idea 💡

1. Create an empty dictionary.
2. Traverse the array.
3. Count the frequency of each element.
4. Traverse the dictionary.
5. Return the element with the highest frequency.

```text
nums = [2,2,1,1,1,2,2]

          ↓

{
    2 : 4,
    1 : 3
}

Highest frequency → 2
```

---

# Python Solution

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}

        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        max_count = 0
        majority = None

        for num in count:
            if count[num] > max_count:
                max_count = count[num]
                majority = num

        return majority
```

---

# Important Python Concepts

### Dictionary

```python
count = {}
```

Stores:

```text
element → frequency
```

Example:

```python
count = {
    2: 4,
    1: 3
}
```

---

### Membership Check

```python
if num in count:
```

Checks whether the key already exists in the dictionary.

---

### Updating Frequency

```python
count[num] += 1
```

Increases the count of an existing element.

---

### Adding a New Key

```python
count[num] = 1
```

Used when the element appears for the first time.

---

# Complexity

Let `n` be the number of elements.

```text
Time:  O(n)
Space: O(n)
```

* One pass to count frequencies.
* One pass through the dictionary.
* Dictionary stores at most `n` unique elements.

---

# Mistakes I Made 🚫

* Initially used a list instead of a dictionary.
* Confused **indices** with **elements**.
* Tried to modify the input array:

```python
nums[i] = count[i]
```

which isn't needed.

* Forgot that we should update the dictionary instead of the array.
* Used incorrect syntax:

```python
if num is in count
```

Correct syntax:

```python
if num in count
```

* Tried:

```python
count += 1
```

instead of updating the frequency of a specific key:

```python
count[num] += 1
```

* Tried:

```python
return max(count)
```

which returns the largest **key**, not the key with the highest frequency.

---

# Pattern Recognition 🧠

## Pattern: Frequency Counting (Hash Map)

Whenever a problem asks:

> "How many times does each element occur?"

Think:

```text
Traverse array
      ↓
Store frequency in a dictionary
      ↓
Use frequencies to answer the question
```

Hash maps are commonly used for:

```text
Frequency counting
Grouping
Duplicate detection
Fast lookup
```

---

# Similar Problems

* Two Sum
* Contains Duplicate
* Valid Anagram
* Top K Frequent Elements
* First Unique Character in a String

---

# Revision Notes

Remember:

```python
count = {}
```

Count frequencies:

```python
for num in nums:
    if num in count:
        count[num] += 1
    else:
        count[num] = 1
```

Find the maximum frequency:

```python
max_count = 0
majority = None

for num in count:
    if count[num] > max_count:
        max_count = count[num]
        majority = num
```

Return:

```python
return majority
```

### Mental Model

> **"Count every element first, then choose the one that appears the most."**

---

## ⭐ Confidence Level

Before solving: ⭐⭐☆☆☆

After solving: ⭐⭐⭐⭐☆

### 🎯 Homework

1. Re-code the hash map solution from memory.
2. Learn the **Boyer-Moore Voting Algorithm** (O(n) time, O(1) space), which is the optimal interview solution for this problem.

The important things to remember are:

```text
Dictionary → frequency counting
num in dictionary → key exists
count[num] += 1 → update frequency
Highest frequency → majority element
```
