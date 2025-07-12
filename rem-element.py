# LC 27 - Remove Element
# https://leetcode.com/problems/remove-element/
# Time: O(n), Space: O(1)
# Uses two pointers to remove all instances of `val` in-place.

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            if nums[left] == val:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
            else:
                left += 1
        return left  # new length of array without `val`

# 🧪 Example usage
if __name__ == "__main__":
    s = Solution()
    arr = [3, 2, 2, 3]
    new_len = s.removeElement(arr, 3)
    print("New length:", new_len)
    print("Updated array:", arr[:new_len])  # Output: [2, 2]
