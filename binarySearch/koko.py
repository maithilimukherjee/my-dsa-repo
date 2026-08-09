import math

class Solution:
    def kokoEat(self, arr: list[int], k: int) -> int:
        low, high = 1, max(arr)
        ans = high
        
        while low <= high:
            mid = (low + high) // 2
            
            # Calculate total hours needed at speed 'mid'
            total_hours = sum(math.ceil(pile / mid) for pile in arr)
            
            if total_hours <= k:
                ans = mid       # Valid speed, try to find a smaller one
                high = mid - 1
            else:
                low = mid + 1   # Too slow, increase speed
                
        return ans
