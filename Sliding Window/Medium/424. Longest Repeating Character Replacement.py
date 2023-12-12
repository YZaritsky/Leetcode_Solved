from collections import defaultdict
from typing import *


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict()
        best = 0
        window = []

        for i in s:
            window.append(i)
            count[i] = count.get(i, 0) + 1

            if len(window) - max(count.values()) <= k:
                best = max(best, len(window))
            else:
                count[window.pop(0)] -= 1

        return best


#Time Complexity: O(n)
#Space Complexity: O(n)