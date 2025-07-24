# Problem: Find the missing number in an array containing a permutation of numbers from 1 to n
# ------------------------------------------------------------------------------------------------
# You are given an array of size (n - 1), with all distinct integers from 1 to n except one missing.
# Your task is to find and return the missing number.

# Example:
# Input: [1, 2, 3, 5] → Output: 4
# Input: [2, 3]       → Output: 1
# Input: [1]          → Output: 2


class Solution:
    # 🔹 Approach 1: Sorting-based Gap Detection
    # ------------------------------------------------
    # 1. Sort the array.
    # 2. If the first element is not 1 → return 1.
    # 3. Loop through the sorted array:
    #    If there's a gap between arr[i] and arr[i+1] (i.e., arr[i+1] != arr[i] + 1), return arr[i] + 1.
    # 4. If no gap is found, the missing number is the next one after the last element.

    def missingNum(self, arr):
        arr = sorted(arr)
        
        if arr[0] != 1:
            return 1

        for i in range(len(arr) - 1):
            if arr[i + 1] != arr[i] + 1:
                return arr[i] + 1

        return arr[-1] + 1


    # 🔹 Approach 2: Sum of Natural Numbers Formula (Optimal)
    # ----------------------------------------------------------
    # 1. Let n = len(arr) + 1
    # 2. Calculate expected sum of numbers from 1 to n: n * (n + 1) // 2
    # 3. Calculate the actual sum of elements in the array
    # 4. The missing number is the difference between expected and actual sum

    def missingNumMath(self, arr):
        n = len(arr) + 1
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(arr)
        return expected_sum - actual_sum
