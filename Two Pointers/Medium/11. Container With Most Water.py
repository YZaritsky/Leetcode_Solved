from typing import *


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        best = 0

        while l < r:
            cur = min(height[l], height[r]) * (r - l)
            best = max(best, cur)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return best

# Time Complexity: O(n)
# Space Complexity: O(1)
