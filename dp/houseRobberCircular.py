class Solution:
    def maxValue(self, arr):
        n = len(arr)
        
        # edge case
        if n == 1:
            return arr[0]
        
        # helper for normal linear house robber
        def rob_linear(nums):
            m = len(nums)
            
            if m == 1:
                return nums[0]
            
            prev2 = nums[0]
            prev1 = max(nums[0], nums[1])
            
            for i in range(2, m):
                current = max(prev1, nums[i] + prev2)
                prev2 = prev1
                prev1 = current
            
            return prev1
        
        # case 1: exclude last house
        case1 = rob_linear(arr[:-1])
        
        # case 2: exclude first house
        case2 = rob_linear(arr[1:])
        
        return max(case1, case2)
