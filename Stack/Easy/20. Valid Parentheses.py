from typing import *


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets_dict = {')': '(', ']': '[', '}': '{'}

        for char in s:
            if char in brackets_dict:
                if stack and brackets_dict[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return not stack

# Time Complexity: O(n)
# Space Complexity: O(n)
