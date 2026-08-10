class Solution(object):
    def maxSizeSlices(self, slices):
        k = len(slices) // 3
        
        def linear_robber(arr, k):
            prev2 = [0] * (k + 1)  # dp[i-2]
            prev1 = [0] * (k + 1)  # dp[i-1]
            
            for slice_val in arr:
                curr = [0] * (k + 1)
                for j in range(1, k + 1):
                    skip = prev1[j]
                    take = prev2[j - 1] + slice_val
                    curr[j] = max(skip, take)
                prev2, prev1 = prev1, curr
                
            return prev1[k]
        
        return max(linear_robber(slices[:-1], k), linear_robber(slices[1:], k))
