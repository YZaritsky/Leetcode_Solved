from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        window = [prices[0]]

        for price in prices[1:]:
            window.append(price)

            if window[0] < window[1]:
                best = max(best, window[1] - window[0])
                window.pop()

            elif window[0] >= window[1]:
                window.pop(0)

        return best

# Time Complexity: O(n)
# Space Complexity: O(1)
