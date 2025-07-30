"""
QuickSort-based solution for sorting an array of integers in O(n log n) time.
Avoids built-in sort functions. Uses 3-way partitioning and randomized pivots.
Author: tina (aka the one who slays bugs and data)
"""

from random import randint
from typing import List

class QuickSortSolution:
    def sort_array(self, nums: List[int]) -> List[int]:
        """
        Sorts the input list of integers using randomized 3-way QuickSort.
        :param nums: List[int] - the input array
        :return: List[int] - the sorted array
        """

        def quick_sort(left: int, right: int):
            if left >= right:
                return

            pivot = nums[randint(left, right)]
            lt, gt, i = left - 1, right + 1, left

            while i < gt:
                if nums[i] < pivot:
                    lt += 1
                    nums[lt], nums[i] = nums[i], nums[lt]
                    i += 1
                elif nums[i] > pivot:
                    gt -= 1
                    nums[gt], nums[i] = nums[i], nums[gt]
                else:
                    i += 1

            quick_sort(left, lt)
            quick_sort(gt, right)

        quick_sort(0, len(nums) - 1)
        return nums


# ---- test block ---- #
if __name__ == "__main__":
    sorter = QuickSortSolution()
    test_array = [5, 2, 3, 1]
    print("Original:", test_array)
    sorted_array = sorter.sort_array(test_array.copy())
    print("Sorted:  ", sorted_array)
