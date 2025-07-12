# LC 41 - First Missing Positive
# https://leetcode.com/problems/first-missing-positive/
# Time: O(n), Space: O(1)
# Places each number at its correct index to find the missing positive

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        # Place each number at the correct index if possible
        for i in range(n):
            while 1 <= nums[i] <= n and nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]  # Swap

        # Find the first missing positive
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1  # If all positions are filled correctly

# 🧪 Example usage
if __name__ == "__main__":
    s = Solution()
    print(s.firstMissingPositive([3, 4, -1, 1]))  # Output: 2
