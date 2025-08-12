class Solution(object):
    """
    Problem:
    Given n non-negative integers representing an elevation map where the width of each bar is 1,
    compute how much water it can trap after raining.

    Example:
    Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
    Output: 6

    Input: height = [4,2,0,3,2,5]
    Output: 9
    """

    def trap(self, height):
        """
        Algorithm (Two-Pointer O(1) Space):
        1. Initialize two pointers: left at start, right at end.
        2. Track two variables: left_max and right_max to store the highest walls so far from each side.
        3. While left < right:
           - If left_max < right_max:
                • Water at left = left_max - height[left] (if positive).
                • Move left pointer rightward.
                • Update left_max if height[left] is greater.
           - Else:
                • Water at right = right_max - height[right] (if positive).
                • Move right pointer leftward.
                • Update right_max if height[right] is greater.
        4. Return total water collected.
        """

        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0
        water = 0

        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    water += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    water += right_max - height[right]
                right -= 1

        return water


if __name__ == "__main__":
    # Sample test cases
    sol = Solution()
    print(sol.trap([0,1,0,2,1,0,1,3,2,1,2,1]))  # 6
    print(sol.trap([4,2,0,3,2,5]))              # 9
