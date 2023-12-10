from typing import *


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        counter = 0

        for i in nums:
            if i == 0:
                return 0
            else:
                if i < 0:
                    counter += 1

        if counter % 2 == 1:
            return -1
        else:
            return 1