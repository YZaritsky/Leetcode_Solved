from typing import *


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        size = len(temperatures)
        results = [0 for i in range(size)]

        stack = []  # Pairs: [temp, index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stack_t, stack_i = stack.pop()
                results[stack_i] = (i - stack_i)

            stack.append([t, i])

        return results

# Time Complexity: O(n)
# Space Complexity: O(n)
