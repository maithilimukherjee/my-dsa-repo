
class Solution:
    def minCostClimbingStairs(self, cost):
        #Write your code here
        
        n=len(cost)
        
        if n==1:
            return cost[0]
        
        prev2 = cost[0]   # dp[0]
        prev1 = cost[1]   # dp[1]
        
        #prev1 represents dp[i-1]
        #prev2 represents dp[i-2]
        
        current=0
        
        for i in range(2,n):
            
            current=cost[i]+min(prev2,prev1)
            prev2=prev1
            prev1=current
            
        
        return min(prev1,prev2)
        
