# Leetcode 74: Search a 2D Matrix
# Time Complexity: O(log(m * n))
# Space Complexity: O(1)

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        # rows and cols
        m = len(matrix)
        n = len(matrix[0]) if matrix else 0

        # treat 2D matrix as 1D sorted array for binary search
        low = 0
        high = m * n - 1

        while low <= high:
            mid = (low + high) // 2

            # convert mid index into 2D coordinates
            row = mid // n
            col = mid % n

            # binary search comparisons
            if target < matrix[row][col]:
                high = mid - 1  # move left
            elif target > matrix[row][col]:
                low = mid + 1   # move right
            else:
                return True     # target found

        return False  # target not in matrix
