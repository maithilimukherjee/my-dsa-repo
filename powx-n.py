# LC 50 - Pow(x, n)
# https://leetcode.com/problems/powx-n/
# Time: O(log n), Space: O(log n) for recursion stack

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1.0  # x^0 = 1
        
        if n < 0:
            return 1 / self.myPow(x, -n)  # Handle negative powers
        
        half = self.myPow(x, n // 2)

        if n % 2 == 0:
            return half * half
        else:
            return x * half * half

# 🧪 Example usage
if __name__ == "__main__":
    s = Solution()
    print(s.myPow(2.00000, 10))     # Output: 1024.0
    print(s.myPow(2.00000, -2))     # Output: 0.25
