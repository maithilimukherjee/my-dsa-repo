# LC 7 - Reverse Integer
# https://leetcode.com/problems/reverse-integer/
# Time: O(log n), Space: O(1)

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        # convert integer to string for easy reversal
        s = str(x)

        # handle negative numbers by slicing and manually adding '-'
        if x < 0:
            rev = "-" + s[:0:-1]
        else:
            rev = s[::-1]

        # convert reversed string back to integer
        result = int(rev)

        # check for 32-bit signed integer overflow
        if result < -2**31 or result > 2**31 - 1:
            return 0

        return result
