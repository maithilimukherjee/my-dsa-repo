class Solution:
    def maxLen(self, arr):
        mp = {}
        prefix = 0
        maxi = 0
        
        for i in range(len(arr)):
            
            if arr[i] == 0:
                prefix += -1
            else:
                prefix += 1
            
            if prefix == 0:
                maxi = i + 1
            
            if prefix in mp:
                maxi = max(maxi, i - mp[prefix])
            else:
                mp[prefix] = i
        
        return maxi
