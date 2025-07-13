# LC 1672 - Richest Customer Wealth
# https://leetcode.com/problems/richest-customer-wealth/
# Time: O(m * n), Space: O(1)

class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        max = 0
        for customer in accounts:
            total = sum(customer)
            if total > max:
                max = total
        return max
