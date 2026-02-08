class Solution:
    def getPairs(self, arr):
        
        seen = set()
        pairs = set()
        
        for num in arr:
            
            if -num in seen:
                pairs.add((min(num, -num), max(num, -num)))
            
            seen.add(num)
        
        return sorted(list(pairs))
