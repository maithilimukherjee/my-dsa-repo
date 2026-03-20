class Solution:
    def minJumps(self, arr):
        n = len(arr)
        
        # base cases
        if n <= 1:
            return 0
        if arr[0] == 0:
            return -1
        
        jumps = 1
        maxReach = arr[0]
        steps = arr[0]
        
        for i in range(1, n):
            # if we’ve reached the end
            if i == n - 1:
                return jumps
            
            # update the farthest index we can currently reach
            maxReach = max(maxReach, i + arr[i])
            
            # use one step
            steps -= 1
            
            # when no steps left → take a new jump
            if steps == 0:
                jumps += 1
                
                # if we are at or beyond maxReach → stuck
                if i >= maxReach:
                    return -1
                
                # reinitialize steps for the new jump range
                steps = maxReach - i
        
        return -1
