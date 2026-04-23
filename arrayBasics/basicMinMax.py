class Solution:
    def get_min_max(self, arr):
        if not arr:
            return None, None  # or raise ValueError("Empty array")

        big = smol = arr[0]

        for num in arr[1:]:
            if num > big:
                big = num
            if num < smol:
                smol = num

        return smol, big
