import operator
from typing import *


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
        stack = []

        for cur in tokens:
            if cur in ops:
                first, second = int(stack.pop()), int(stack.pop())
                result = int(ops[cur](second, first))
                stack.append(result)

            else:
                stack.append(cur)

        return int(stack[0])

# Time Complexity: O(n)
# Space Complexity: O(n)
