from typing import *

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cur = nums[0]
        k = 0

        for i, n in enumerate(nums):
            if n > cur:
                cur = n
                k += 1
                nums[k] = cur


        return k + 1

#Time complexity: O(n)
#Space Complexity: O(1)