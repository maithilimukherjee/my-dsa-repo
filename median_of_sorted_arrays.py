class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        Finds the median of two sorted arrays in O(log(min(m,n))) time.
        
        Uses a binary search on the smaller array to partition both arrays such that:
            maxLeftX <= minRightY and maxLeftY <= minRightX
        When this condition is met, we've found the correct partition for median.
        
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        # Step 1: Handle edge case where one array is larger
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1  # Ensure nums1 is the smaller array

        a, b = nums1, nums2
        m, n = len(a), len(b)

        inf = float('inf')  # To handle edge cases at partition edges
        low = 0
        high = m

        # Step 2: Binary search loop on smaller array
        while low <= high:
            partitionX = (low + high) // 2
            partitionY = (m + n + 1) // 2 - partitionX

            # Step 3: Find maxLeft and minRight for both arrays
            maxLeftX = -inf if partitionX == 0 else a[partitionX - 1]
            minRightX = inf if partitionX == m else a[partitionX]

            maxLeftY = -inf if partitionY == 0 else b[partitionY - 1]
            minRightY = inf if partitionY == n else b[partitionY]

            # Step 4: Check if correct partition
            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                # Step 5: Median calculation
                if (m + n) % 2 == 0:
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2.0
                else:
                    return max(maxLeftX, maxLeftY)
            elif maxLeftX > minRightY:
                # Move left in a
                high = partitionX - 1
            else:
                # Move right in a
                low = partitionX + 1
