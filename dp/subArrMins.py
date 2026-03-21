class Solution:
    def sumSubMins(self, arr):
        n = len(arr)
        stack = []
        prev_smaller = [-1] * n
        next_smaller = [n] * n
        
        # previous smaller
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            prev_smaller[i] = stack[-1] if stack else -1
            stack.append(i)
        
        stack.clear()
        
        # next smaller
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            next_smaller[i] = stack[-1] if stack else n
            stack.append(i)
        
        # calculate result
        res = 0
        mod = 10**9 + 7
        
        for i in range(n):
            left = i - prev_smaller[i]
            right = next_smaller[i] - i
            res += arr[i] * left * right
        
        return res % mod
