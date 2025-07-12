# LC 1480 - Running Sum of 1d Array
# https://leetcode.com/problems/running-sum-of-1d-array/
# Time: O(n), Space: O(1)

class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            nums[i] = sum
        return nums
