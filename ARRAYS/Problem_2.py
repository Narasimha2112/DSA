# Array Problem #2 — Best Time to Buy and Sell Stock

# (LeetCode 121)

# 🧩 Problem

# You are given an array prices where prices[i] is the price of a stock on day i.
# You want to buy once and sell once, and make maximum profit.

# Return the max profit.
# If you cannot make profit, return 0.

# 🧠 Complexity
# Time	Space
# O(n)	O(1)

class Solution:
    def maxProfit(self, prices):
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            if price < min_price:
                min_price = price
            else:
                max_profit = max(max_profit, price - min_price)
        
        return max_profit