# Array Problem #4 — Move Zeroes

# (LeetCode 283)

# 🧩 Problem

# Given an integer array nums, move all zeroes to the end, while keeping the order of non-zero elements the same.

# Do it in-place (no extra array).

# Two Pointer Method (O(n))

class Solution:
    def moveZeros(self, nums):
        insert_pos = 0
        
        # Move all non-zero values forward
        for num in nums:
            if num != 0:
                nums[insert_pos] = num
                insert_pos += 1
        
        # Fill remaining positions with zero        
        while insert_pos < len(nums):
            nums[insert_pos] = 0
            insert_pos += 1