class Solution:
    # function to find equilibrium point in the array.
    def findEquilibrium(self, arr):
        total_sum = sum(arr)
        left_sum = 0

        for i in range(len(arr)):
            total_sum -= arr[i]  # now this is right_sum

            if left_sum == total_sum:
                return i

            left_sum += arr[i]

        return -1
