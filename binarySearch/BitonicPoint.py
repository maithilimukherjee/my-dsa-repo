"""
🧠 PROBLEM:
Given an array arr[] that is first strictly increasing and then maybe strictly decreasing, 
find the *bitonic point*, i.e., the maximum element in the array.

It is guaranteed that there is exactly ONE bitonic point.

✅ OUTPUT: return the maximum value (not its index)

----------------------------------------------------

🔥 TRICK TO REMEMBER:
- It's like climbing a mountain ⛰️
- First part: strictly increasing
- Then comes the peak (bitonic point)
- Then strictly decreasing
- Binary search works here because both sides are "sorted" in opposite ways.
"""

# 🔁 Linear Search Approach (O(n))
class SolutionLinear:
    def findMaximum(self, arr):
        for i in range(1, len(arr)):
            if arr[i] < arr[i - 1]:
                return arr[i - 1]
        return arr[-1]  # array is fully increasing


# ⚡ Binary Search Approach (O(log n))
class SolutionBinary:
    def findMaximum(self, arr):
        low = 0
        high = len(arr) - 1

        while low <= high:
            mid = (low + high) // 2

            # Edge case: only two elements left
            if mid == 0:
                return max(arr[0], arr[1])
            if mid == len(arr) - 1:
                return max(arr[-1], arr[-2])

            # If mid is the bitonic point
            if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
                return arr[mid]
            
            # If in increasing part
            elif arr[mid] > arr[mid - 1]:
                low = mid + 1

            # If in decreasing part
            else:
                high = mid - 1
