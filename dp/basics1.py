dp = {}

def solve(i):
    if i in dp:
        return dp[i]

    if base_case:
        return value

    dp[i] = recurrence
    return dp[i]
