class Solution:
    def maxProduct(self, arr):

        maxProd = arr[0]
        minProd = arr[0]
        ans = arr[0]

        for i in range(1, len(arr)):

            num = arr[i]

            tempMax = max(num, num * maxProd, num * minProd)
            tempMin = min(num, num * maxProd, num * minProd)

            maxProd = tempMax
            minProd = tempMin

            ans = max(ans, maxProd)

        return ans
