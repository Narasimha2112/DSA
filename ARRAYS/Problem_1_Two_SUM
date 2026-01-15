### **Array Problem #1 — Two Sum**

---

## 🧩 **Problem**

Given an array `nums` and a target `target`, return **indices of the two numbers** such that they add up to target.
You may assume **exactly one solution**, and you **cannot use the same element twice**.

---

## ✅ **Approach 1 — Brute Force (O(n²))**

Check every pair.

```python
class Solution:
    def twoSum(self, nums, target):
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
```

👉 Easy but slow when n is large.

---

## 🚀 **Approach 2 — HashMap (O(n)) — Best**

Store value → index
Check if complement exists.

```python
class Solution:
    def twoSum(self, nums, target):
        seen = {}               # value : index
        
        for i, num in enumerate(nums):
            comp = target - num
            if comp in seen:
                return [seen[comp], i]
            seen[num] = i
```

### 🧪 Example

```
nums   = [2, 7, 11, 15]
target = 9
```

* i=0 → num=2 → comp=7 → store {2:0}
* i=1 → num=7 → comp=2 → found in map 🎉
  Return `[0,1]`.

---

## 🧠 **Complexity**

| Method      | Time  | Space |
| ----------- | ----- | ----- |
| Brute Force | O(n²) | O(1)  |
| HashMap     | O(n)  | O(n)  |

---

