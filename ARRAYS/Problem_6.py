# Array Problem #6 — Contains Duplicate

# (LeetCode 217)

# 🧩 Problem

# Given an integer array nums,
# return true if any value appears at least twice,
# otherwise return false.

class Solution:
    def ContainsDuplicate(self, nums):
        seen = set()
        
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False