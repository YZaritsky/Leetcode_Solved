from typing import *


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        size = len(s)
        if size == 0:
            return 0

        l, r = 0, 1
        best = 1

        while r < size:
            if s[r] in s[l:r]:
                best = max(best, r - l)
                l += 1
            else:
                r += 1

        return max(best, r - l)

# Time Complexity: O(n)
# Space Complexity: O(n)
