class Solution:
    def binarysearch(self, arr, k):
        """
        Perform binary search to find the first occurrence of k in a sorted array.

        Args:
            arr (List[int]): Sorted list of integers (may contain duplicates).
            k (int): Element to search for.

        Returns:
            int: Index of first occurrence of k, or -1 if not found.
        """
        ll = 0
        ul = len(arr) - 1
        result = -1

        while ll <= ul:
            mid = (ll + ul) // 2

            if arr[mid] == k:
                result = mid
                ul = mid - 1  # Keep looking on the left side
            elif arr[mid] < k:
                ll = mid + 1
            else:
                ul = mid - 1

        return result
