from typing import *

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sol, cur_sum = [], 0

        for i in nums:
            cur_sum += i
            sol.append(cur_sum)

        return sol