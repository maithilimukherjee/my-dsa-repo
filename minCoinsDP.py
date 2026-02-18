class Solution:
    def minCoins(self, coins, S):
        dp = [float('inf')] * (S + 1)
        dp[0] = 0
        
        for i in range(1, S + 1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], 1 + dp[i - coin])
        
        return dp[S] if dp[S] != float('inf') else -1
