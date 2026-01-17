class Solution:
    def missingNumber(self, arr):
        s = set(arr)

        i = 1
        while True:
            if i not in s:
                return i
            i += 1
