from typing import *


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()

        counter = 0
        size = len(s)
        if size != 1:
            i = size - 1
        else:
            return 1

        while s[i] != " ":
            counter += 1
            i -= 1

            if s[i] == " " or i == -1:
                break

        return counter
