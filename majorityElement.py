"""
Problem:
Given an array 'arr' of size N, find the majority element.
The majority element is the element that appears more than floor(N/2) times.
If no majority element exists, return -1.

Examples:
Input:  [3, 3, 4, 2, 3, 3, 5]
Output: 3

Input:  [1, 2, 3]
Output: -1
"""

class Solution:

    def majorityElement_sorting(self, arr):
        """
        Approach 1: Sorting
        ---------------------------------
        Algorithm:
        1. Calculate the limit = floor(N/2) + 1 (minimum occurrences for majority).
        2. Sort the array.
        3. Traverse the sorted array and count consecutive occurrences of each number.
        4. If any count >= limit, return that number.
        5. If loop finishes, return -1 (no majority element).
        Time Complexity: O(n log n)
        Space Complexity: O(1)
        """
        limit = (len(arr) // 2) + 1
        count = 1
        arr.sort()

        for i in range(1, len(arr)):
            if arr[i] == arr[i - 1]:
                count += 1
                if count >= limit:
                    return arr[i]
            else:
                count = 1  # reset for new number

        return -1

    def majorityElement_boyer_moore(self, arr):
        """
        Approach 2: Boyer–Moore Voting Algorithm
        ---------------------------------
        Algorithm:
        Phase 1 - Find a candidate:
            - Keep a 'candidate' variable and 'count' counter.
            - Iterate through array:
                - If count == 0, set current number as candidate.
                - If number == candidate, increment count.
                - Else decrement count.
        Phase 2 - Verify:
            - Check if candidate actually appears more than n//2 times.
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # Phase 1: Find a candidate
        candidate = None
        count = 0
        for num in arr:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        # Phase 2: Verify
        if arr.count(candidate) > len(arr) // 2:
            return candidate
        return -1


if __name__ == "__main__":
    sol = Solution()

    # Test cases for Sorting method
    print("Sorting Method:")
    print(sol.majorityElement_sorting([3, 3, 4, 2, 3, 3, 5]))  # 3
    print(sol.majorityElement_sorting([1, 2, 3]))              # -1

    # Test cases for Boyer-Moore method
    print("\nBoyer–Moore Voting Algorithm:")
    print(sol.majorityElement_boyer_moore([3, 3, 4, 2, 3, 3, 5]))  # 3
    print(sol.majorityElement_boyer_moore([1, 2, 3]))              # -1
