class Solution:
    # Question:
    # Given an infinite supply of Indian currency denominations {1, 2, 5, 10, 20, 50, 100, 200, 500, 2000}
    # and a target value N, find the minimum number of coins and/or notes needed to make the change for N.
    # Return a list containing the values of coins used.
    
    # Approach:
    # 1. Start with the largest denomination and check if it can be used for the remaining amount N.
    # 2. If it can, add it to the solution list and subtract it from N.
    # 3. Repeat the process until N becomes 0.
    # 4. This greedy approach works because using the largest coin available at each step ensures
    #    the minimum number of coins/notes.

    def minPartition(self, N):
        money = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
        sol = []

        while N > 0:
            for coin in money:
                if N >= coin:  # pick coin if it fits
                    sol.append(coin)
                    N -= coin
                    break  # restart from the largest coin
        return sol
