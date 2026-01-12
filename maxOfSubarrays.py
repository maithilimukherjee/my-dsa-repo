class Solution:
    def maxOfSubarrays(self, arr, k):
        res = []
        
        for i in range(len(arr) - k + 1):
            maxNo = arr[i]
            for j in range(1, k):
                if arr[i + j] > maxNo:
                    maxNo = arr[i + j]
            res.append(maxNo)
        
        return res
