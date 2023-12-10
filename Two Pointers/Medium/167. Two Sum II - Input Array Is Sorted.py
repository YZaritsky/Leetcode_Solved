from typing import *


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        cur = numbers[l] + numbers[r]

        while cur != target:
            if cur > target:
                r -= 1
            if cur < target:
                l += 1

            cur = numbers[l] + numbers[r]

        return [l + 1, r + 1]



#Time Complexity: O(n)
#Space Complexity: O(1)