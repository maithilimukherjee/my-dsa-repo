# LC 35 - Search Insert Position
# https://leetcode.com/problems/search-insert-position/
# Binary Search solution (O(log n))

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1

        return low  # this is the correct insert position

# 🧪 Example usage
if __name__ == "__main__":
    s = Solution()
    print(s.searchInsert([1, 3, 5, 6], 5))  # Output: 2
    print(s.searchInsert([1, 3, 5, 6], 2))  # Output: 1
    print(s.searchInsert([1, 3, 5, 6], 7))  # Output: 4
