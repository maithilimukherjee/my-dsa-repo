class Solution:
    
    def longestSubarray(self, arr, k):
        
        prefix = 0
        occurrence = {}   # stores prefix sum -> first index
        maxi = 0
        n = len(arr)

        for i in range(n):
            prefix += arr[i]

            # Case 1: subarray from start to i has sum = k
            if prefix == k:
                maxi = max(maxi, i + 1)

            # Case 2: subarray from some j+1 to i has sum = k
            if (prefix - k) in occurrence:
                maxi = max(maxi, i - occurrence[prefix - k])

            # Store first occurrence of prefix sum
            if prefix not in occurrence:
                occurrence[prefix] = i

        return maxi
