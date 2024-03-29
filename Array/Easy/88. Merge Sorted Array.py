from typing import *


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = m - 1
        j = n - 1
        write_idx = m + n - 1

        while j >= 0:
            if nums1[i] > nums2[j] and i >= 0:
                nums1[write_idx] = nums1[i]
                i -= 1
            else:
                nums1[write_idx] = nums2[j]
                j -= 1

            write_idx -= 1