from typing import *


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dic = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in nums_dic:
                return [nums_dic[diff], i]
            nums_dic[n] = i

# Time Complexity: O(n)
# Space Complexity: O(n)