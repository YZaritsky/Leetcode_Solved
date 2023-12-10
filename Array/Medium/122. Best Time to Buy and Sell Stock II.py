from typing import *


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        size = len(prices)
        cur_price = prices[0]

        # Edge Case 1:
        if size == 1:
            return 0

        for price in prices[1:]:
            if cur_price < price:
                profit += (price - cur_price)

            cur_price = price

        return profit  # Output == int

# Time Complexity: O(n)
# Space Complexity: O(1)

# Edge Cases:
# 1 - List contains only 1 element.