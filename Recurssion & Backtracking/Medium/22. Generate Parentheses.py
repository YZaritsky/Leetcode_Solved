from typing import *


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        results = []

        def parenthesis_helper(open, closed, current):
            if open == closed == n:
                results.append(current)
                return

            if open < n:
                parenthesis_helper(open + 1, closed, current + "(")

            if closed < open:
                parenthesis_helper(open, closed + 1, current + ")")

        parenthesis_helper(open=0, closed=0, current="")
        return results
