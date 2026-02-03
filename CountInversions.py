#Given an array of integers arr[]. You have to find the Inversion Count of the array. 
#Inversion count is the number of pairs of elements (i, j) such that i < j and arr[i] > arr[j]
#Use Merged Sort Algorithm to solve this problem optimally.
class Solution:
    def inversionCount(self, arr):
        def merge_sort(arr):
            if len(arr) <= 1:
                return arr, 0
            mid = len(arr) // 2
            left, inv_left = merge_sort(arr[:mid])
            right, inv_right = merge_sort(arr[mid:])
            
            merged = []
            i = j = 0
            inv_count = inv_left + inv_right
            
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    inv_count += len(left) - i
                    j += 1
            
            merged += left[i:]
            merged += right[j:]
            return merged, inv_count
        
        _, count = merge_sort(arr)
        return count
