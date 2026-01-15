# Array Problem #8 — Find All Duplicates in an Array

# (LeetCode 442)

# 🧩 Problem

# Given an array nums of length n
# where each number is in the range [1, n],
# some numbers appear twice, others once.

# Return all numbers that appear twice.

class Solution:
    def duplicates(self, nums):
        seen = set()
        duplicates = []
        
        for num in nums:
            if num in seen:
                duplicates.append(num)
            else:
                seen.add(num)
        return duplicates