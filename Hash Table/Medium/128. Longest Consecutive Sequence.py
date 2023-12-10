from typing import *
from collections import *

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_dict = defaultdict()
        best_streak = 0

        for i in nums:
            nums_dict[i] = nums_dict.get(i, 0) + 1

        for i in nums:
            cur_streak = 1
            j = i
            if nums_dict.get(j - 1, 0):
                continue
            else:
                while nums_dict.get(j + 1, 0):
                    nums_dict[j + 1] -= 1
                    cur_streak += 1
                    j += 1

            best_streak = max(best_streak, cur_streak)

        return best_streak

# Time Complexity: O(n)
# Space Complexity: O(n)