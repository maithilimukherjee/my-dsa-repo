# LC 9 - Palindrome Number
# https://leetcode.com/problems/palindrome-number/
# Time: O(n), Space: O(n) - where n is the number of digits

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x_str = str(x)
        return x_str == x_str[::-1]
