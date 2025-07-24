#sort 0s,1s,2s
#similar to sort colors problem
#use dutch national flag algo

class Solution:
    # Function to sort an array of 0s, 1s, and 2s
    def sort012(self, arr):
        # code here
        low = 0
        mid = 0
        high = len(arr)-1
        
        while mid<=high:
            if arr[mid] == 0:
                arr[low], arr[mid] = arr[mid], arr[low]
                low = low+1
                mid = mid+1
                
            elif arr[mid]==1:
                mid = mid+1
                
            else:
                arr[high], arr[mid] = arr[mid], arr[high]
                high = high-1
            
        return arr
        
