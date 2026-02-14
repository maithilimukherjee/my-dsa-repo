class Solution:
    def unionSets(self, a, b):
        
        return list(set(a) | set(b))
    
# Example usage:
sol = Solution()
a = [1, 2, 3, 6]
b = [3, 4, 5]
print(sol.unionSets(a, b))  
