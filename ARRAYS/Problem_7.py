# Array Problem #7 — Missing Number

# (LeetCode 268)

# 🧩 Problem

# Given an array nums containing n distinct numbers in the range [0, n],
# return the one number missing from the array.

class Solution:
    def missingNumber(self, nums):
        n = len(nums)
        expected = n * (n + 1) // 2
        return expected - sum(nums)
