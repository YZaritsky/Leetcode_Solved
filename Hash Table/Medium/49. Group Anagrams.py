from collections import *
from typing import *


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_dic = defaultdict(list)

        for word in strs:
            l_map = [0] * 26
            for l in word:
                l_map[ord(l) - ord("a")] += 1

            l_map = tuple(l_map)
            strs_dic[l_map] = strs_dic.get(l_map, []) + [word]

        return strs_dic.values()

# Let 'm' be the size of the biggest word.
# Let 'n' be the size of "strs".

# Time Complexity: O(m * n)
# Space Complexity: O(m * n)
