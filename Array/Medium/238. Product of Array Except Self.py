from typing import *
from collections import *
from heapq import *


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [[] for i in range(len(nums))]
        size = len(nums)
        postfix, prefix = 1, 1

        for i in range(size - 1, -1, -1):
            answer[i] = postfix
            postfix *= nums[i]

        for i in range(size):
            answer[i] *= prefix
            prefix *= nums[i]

        return answer

# Details:
# 32-bit, O(n), no Division, atleast 2 items in nums, Each items is in range (-30...30)


# Naive Solution:
# 1. iterate through every item
# 2. iterate through all other items to calculate sum

# Time Complexity: O(n^2)
# Space Complexity: O(1)

################


# Better Solution:
# 1. Itereate through items from left to right to calculate prefix and add it to answer[i].
# 2. Iterate in reverse to calculate suffix and multiply it in answer[i].
# 3. answer[i] now contains the requested task.

# Time Complexity: O(n)
# Space Complexity: O(1)