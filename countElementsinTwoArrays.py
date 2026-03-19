#rule: if you see count number of elements<=x : sort + binary search

class Solution:
    def countLessEq(self, a, b):
        b.sort()
        res = []
        
        def binSearch(num):
            low = 0
            high = len(b) - 1
            ans = -1
            
            while low <= high:
                mid = (low + high) // 2
                
                if b[mid] <= num:
                    ans = mid
                    low = mid + 1
                else:
                    high = mid - 1
                    
            return ans + 1
        
        for num in a:
            res.append(binSearch(num))
            
        return res
