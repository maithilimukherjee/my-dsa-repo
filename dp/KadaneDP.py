class Solution:
    def maxSubarraySum(self, arr):
        # Code here
        
        currentSum = arr[0]
        maxSum = arr[0]

        for i in range(1, len(arr)):
            currentSum = max(arr[i], arr[i] + currentSum)
            maxSum = max(maxSum, currentSum)

        return maxSum
