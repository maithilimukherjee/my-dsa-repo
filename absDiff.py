from typing import List

class Solution:
    def findPair(self, arr: List[int], x: int) -> int:
        
        seen = set(arr)
        
        for num in seen:
            
            if (num + x) in seen or (num - x) in seen:
                if x != 0 or arr.count(num) > 1:
                    return True
        
        return False
