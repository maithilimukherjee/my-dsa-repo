class Solution:
    
    def hasTripletSum(self, arr, target):
        n = len(arr)
        
        # Iterate over all pairs
        for i in range(n):
            seen = set()
            curr_target = target - arr[i]
            
            # Check if there exists a pair (arr[j], arr[k]) such that arr[j] + arr[k] = curr_target
            for j in range(i+1, n):
                if (curr_target - arr[j]) in seen:
                    return True
                seen.add(arr[j])
        
        return False
