# Array Problem 1 — Two Sum
# 🧩 Problem Statement

# Given an array nums and a target target, return indices of the two numbers such that they add up to target.
# You may assume exactly one solution, and you cannot use the same element twice.

# Approach — Brute Force Time-(O(n²)), Space-(O(1))

class Solution:
    def twoSum(self, nums, target):
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
