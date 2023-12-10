from typing import *


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        best = 0

        for price in prices[1:]:
            best = max(best, price - min_price)
            min_price = min(min_price, price)

        return best
