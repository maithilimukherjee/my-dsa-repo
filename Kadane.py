#python ver
class Solution:
    def maxSubarraySum(self, arr):
        currentSum = 0
        maxSum = arr[0]
        
        for num in arr:
            
            currentSum = currentSum + num
            
            if currentSum>maxSum:
                maxSum = currentSum
                
            if currentSum<0:
                currentSum = 0
                
        return maxSum
