# Array Problem #9 — Product of Array Except Self

# (LeetCode 238)

# 🧩 Problem

# Given an array nums,
# return an array output such that
# output[i] = product of all nums except nums[i].

# ⚠️ No division allowed
# ⚡ Must run in O(n)
# 💾 Only constant extra space (ignore result array)

class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        result = [1] * n
        
        # Step 1: Prefix products
        prefix = 1
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]
        
        # Step 2: Suffix products
        suffix = 1
        for i in range(n-1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]
        
        return result
