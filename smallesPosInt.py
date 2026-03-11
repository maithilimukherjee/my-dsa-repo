from typing import List

class Solution:
    def smallestpositive(self, arr: List[int], n: int) -> int:
        
        arr.sort()
        
        res = 1
        
        for num in arr:
            
            if num > res:
                return res
            
            res += num
        
        return res
