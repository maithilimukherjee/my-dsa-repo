class Solution:    
    def minPlatform(self, arr, dep):
        n = len(arr)
        if n == 0:
            return 0
         
        platforms = 0
        maxPlt = 0
         
        arr.sort()
        dep.sort()
         
        i = 0
        j = 0
         
        while i < n and j < n:
            if arr[i] <= dep[j]:
                platforms += 1
                i += 1   
            else:
                platforms -= 1
                j += 1

            maxPlt = max(maxPlt, platforms)
        
        return maxPlt
