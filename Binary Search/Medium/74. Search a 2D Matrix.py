from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        size, row_size = len(matrix), len(matrix[0])

        low, high = 0, (size * row_size) - 1

        while low <= high:
            m = (low + high) // 2
            m_row = (m // row_size)
            m_idx = m % row_size

            if matrix[m_row][m_idx] == target:
                return True

            elif matrix[m_row][m_idx] < target:
                low = m + 1

            elif matrix[m_row][m_idx] > target:
                high = m - 1

        return False

# Time Complexity: O(log(mn))
# Space Complexity: O(1)
