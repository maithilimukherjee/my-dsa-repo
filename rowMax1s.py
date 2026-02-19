class Solution:
    def rowWithMax1s(self, arr):
        
        if not arr:
            return -1
        
        n = len(arr)
        m = len(arr[0])
        
        j = m - 1
        ans = -1
        
        for i in range(n):
            while j >= 0 and arr[i][j] == 1:
                j -= 1
                ans = i
        
        return ans
