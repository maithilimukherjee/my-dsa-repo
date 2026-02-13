class Solution:
    def nextPermutation(self, arr):
        n = len(arr)
        
        # step 1: find pivot
        i = n - 2
        while i >= 0 and arr[i] >= arr[i + 1]:
            i -= 1
        
        # step 2: if no pivot, reverse entire array
        if i < 0:
            arr.reverse()
            return arr
        
        # step 3: find next greater element
        j = n - 1
        while arr[j] <= arr[i]:
            j -= 1
        
        # swap
        arr[i], arr[j] = arr[j], arr[i]
        
        # step 4: reverse suffix
        left = i + 1
        right = n - 1
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        
        return arr
 