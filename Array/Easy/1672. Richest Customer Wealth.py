from typing import *


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        best = 1
        for i in range(len(accounts)):
            cur_sum = sum(accounts[i])
            if best <= cur_sum:
                best = cur_sum

        return best