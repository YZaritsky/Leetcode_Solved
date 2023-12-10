from typing import *


class Solution:
    def romanToInt(self, s: str) -> int:
        con_dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        size = len(s)

        for i, n in enumerate(s):
            concat = True
            if n in "IXC":
                if i + 1 <= size - 1:
                    if (n == "I" and s[i + 1] in "VX") or (n == "X" and s[i + 1] in "LC") or (
                            n == "C" and s[i + 1] in "DM"):
                        concat = False

            if concat:
                result += con_dic[n]
            if not concat:
                result -= con_dic[n]

        return result