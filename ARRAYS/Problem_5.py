# Array Problem #5 — Rotate Array

# (LeetCode 189)

# 🧩 Problem

# Given an array nums and an integer k, rotate the array to the right by k steps.

class Solution:
    def rotate(self, nums, k):
        n = len(nums)
        k %= n
        
        #helper to reverse in place
        def reverse(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        
        reverse(0, n-1)
        reverse(0, k-1)
        reverse(k, n-1)