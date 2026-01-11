# Array Problem #3 — Maximum Subarray (Kadane’s Algorithm)

# (LeetCode 53)

# 🧩 Problem

# Given an integer array nums, find the contiguous subarray (at least one number) which has the largest sum, and return that sum.

# ❌ Brute Force (O(n²)) — Try all subarrays

# But inefficient, so straight to the best approach.

# 🚀 Optimal — Kadane’s Algorithm (O(n))

# Idea:

# Keep running sum

# If running sum drops below 0, reset

# Track the maximum

# 🧠 Complexity
# Time	Space
# O(n)	O(1)

class Solution:
    def maxSubArray(self, nums):
        max_sum = nums[0]
        current_sum = 0
        
        for num in nums:
            current_sum += num
            
            if current_sum > max_sum:
                max_sum = current_sum
            if current_sum < 0:
                current_sum = 0                  #reset to 0
        
        return max_sum
    
