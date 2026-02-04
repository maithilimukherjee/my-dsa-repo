class Solution:
    def countRevPairs(self, arr):
        
        def mergeSort(arr):
            
            if len(arr) <= 1:
                return arr, 0
                
            mid = len(arr)//2
            
            left, inv_left = mergeSort(arr[:mid])
            right, inv_right = mergeSort(arr[mid:])
            
            inv_count = inv_left + inv_right

            # --------- ADD THIS PART (count pairs) ----------
            j = 0
            for i in range(len(left)):
                while j < len(right) and left[i] > 2*right[j]:
                    j += 1
                inv_count += j
            # -----------------------------------------------

            # --------- normal merge (small fix) -------------
            merged = []
            i = j = 0
            
            while i < len(left) and j < len(right):
                
                if left[i] <= right[j]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1
            # -----------------------------------------------

            merged += left[i:]
            merged += right[j:]
            
            return merged, inv_count
            
        _, count = mergeSort(arr)
        return count
