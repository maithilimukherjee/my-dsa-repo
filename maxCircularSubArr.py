class Solution:
    def maxCircularSum(self, arr):
        # code here
        
        total = sum(arr)
        
        max_sum = cur_max = arr[0]
        min_sum = cur_min = arr[0]
        
        for num in arr[1:]:
            
            cur_max = max(num, cur_max + num)
            max_sum = max(max_sum, cur_max)
            
            cur_min = min(num, cur_min + num)
            min_sum = min(min_sum, cur_min)
        
        if max_sum < 0:
            return max_sum
        
        return max(max_sum, total - min_sum)
        
