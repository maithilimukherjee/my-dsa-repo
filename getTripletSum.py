
class Solution:
    def findTriplets(self, arr):
        
        n = len(arr)
        
        for i in range(n):
            
            seen = set()
            
            for j in range(i+1, n):
            
                need = -(arr[i] + arr[j])
                
                if need in seen:
                    return True
                
                seen.add(arr[j])
        
        return False
