# LC 67 - Add Binary
# https://leetcode.com/problems/add-binary/
# Time: O(max(len(a), len(b))), Space: O(1) (excluding output string)

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        total = int(a, 2) + int(b, 2)
        binary = bin(total)
        return binary[2:]
