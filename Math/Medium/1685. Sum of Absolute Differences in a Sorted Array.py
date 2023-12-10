from typing import *


class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        results = []
        total_sum, num_count = sum(nums), len(nums)
        left_sum, right_sum = 0, total_sum

        for i, n in enumerate(nums):
            results.append(
                n * i - left_sum +
                right_sum - n * (num_count - i)
            )

            right_sum -= n
            left_sum += n

        return results

# Time Complexity O(n)
# Space Complexity O(n)