from typing import List
from math import ceil


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        best = high

        while low <= high:
            k = low + ((high - low) // 2)

            hours = 0
            for i in piles:
                hours += ceil(i / k)

            if hours > h:
                low = k + 1

            elif hours <= h:
                high = k - 1
                best = min(best, k)

        return best