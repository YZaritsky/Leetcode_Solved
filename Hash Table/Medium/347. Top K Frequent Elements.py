from typing import *
from collections import *
from heapq import *


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        results = []
        count_dict, reverse_dict = defaultdict(), defaultdict()

        for n in nums:  # O(n)
            count_dict[n] = count_dict.get(n, 0) + 1

        for n, c in count_dict.items():  # O(n)
            reverse_dict[n] = reverse_dict.get(n, []) + [c]

        max_heap_largest = nlargest(k, list(reverse_dict.keys()))  # O(klogn)

        while k > 0:
            for val in max_heap_largest:
                for item in reverse_dict[val]:
                    results += [item]
                    k -= 1
                    if k == 0:
                        return results

        return results

    # Time Complexity: O(klogk)
    # Memory Complexity: O(n)

    ##### Another Solution O(n) using Count Sort / Bucket Sort Variation.
    def topKFrequent_2(self, nums: List[int], k: int) -> List[int]:
        results = []
        size = len(nums)

        count_dict = defaultdict()
        freq = [[] for i in range(size + 1)]

        for n in nums:  # O(n)
            count_dict[n] = count_dict.get(n, 0) + 1

        for n, c in count_dict.items():  # O(n)
            freq[c].append(n)

        for i in range(size, 0, -1):
            for val in freq[i]:
                results.append(val)
                if len(results) == k:
                    return results

# Time Complexity: O(n)
# Memory Complexity: O(n)
