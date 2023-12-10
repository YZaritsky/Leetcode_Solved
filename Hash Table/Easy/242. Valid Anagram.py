from typing import *


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Edge-Case
        if len(s) != len(t):
            return False

        t_dic = {}

        for i in t:
            t_dic[i] = t_dic.get(i, 0) + 1

        for i in s:
            if t_dic.get(i, 0) > 0:
                t_dic[i] -= 1

            else:
                return False

        return True

# Time Complexity: O(n)
# Space Complexity: O(n)