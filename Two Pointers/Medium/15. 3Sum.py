from typing import *


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        size = len(nums)
        nums.sort()

        for i, n in enumerate(nums):
            if i > 0 and nums[i - 1] == n:
                continue

            target = -n
            l, r = i + 1, size - 1

            while l < r:
                cur_res = nums[l] + nums[r]

                if cur_res > target:
                    r -= 1
                elif cur_res < target:
                    l += 1

                elif cur_res == target:
                    results.append([(-target), nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return results

# Time Complexity: O(n^2)
# Space Complexity: O(n)
