class Solution:
    def firstRepeated(self, arr):
        freq = {}
        
        # count frequency
        for num in arr:
            freq[num] = freq.get(num, 0) + 1
        
        # find first repeating element
        for i in range(len(arr)):
            if freq[arr[i]] > 1:
                return i + 1
        
        return -1
