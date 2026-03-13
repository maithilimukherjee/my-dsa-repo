class Solution:
    def findLargest(self, n, sod):

        if sod == 0:
            if n == 1:
                return "0"
            return "-1"

        if sod > 9 * n:
            return "-1"

        result = ""

        for i in range(n):

            if sod >= 9:
                result += "9"
                sod -= 9
            else:
                result += str(sod)
                sod = 0

        return result
