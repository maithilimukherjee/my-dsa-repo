# user function template for python3
class Solution:
    def subarraySum(self, arr, target):
        
        currentSum = 0
        start = 0
        
        for i in range(len(arr)):
            
            currentSum += arr[i]
            
            # shrink window if sum exceeds target
            while currentSum > target and start <= i:
                currentSum -= arr[start]
                start += 1
            
            # check if target found
            if currentSum == target:
                return [start + 1, i + 1]  # 1-based indexing
        
        return [-1]
