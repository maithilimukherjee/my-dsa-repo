class Solution(object):
    def xorOperation(self, n, start):
        """
        Given two integers n and start, return the result of the following operation:
        XOR all elements in the array where nums[i] = start + 2*i for i in range(n).

        Example:
        n = 5, start = 0
        nums = [0, 2, 4, 6, 8]
        return 0 ^ 2 ^ 4 ^ 6 ^ 8 = 8

        :type n: int
        :type start: int
        :rtype: int
        """
        xorVal = start
        for i in range(1,n):
            val = start+2*i
            xorVal = xorVal^val
        return xorVal

