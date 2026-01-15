# Array Problem #10 — Remove Duplicates from Sorted Array

# (LeetCode 26)

# 🧩 Problem

# Given a sorted array nums,
# remove duplicates in-place so that each element appears only once,
# and return the new length.

# Modify array such that first k elements are unique.

class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        
        slow = 0
        
        for fast in range(1, len(nums)):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
        
        return slow + 1