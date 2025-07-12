# LC 1 - Two Sum
# https://leetcode.com/problems/two-sum/

# ----------------------------------------
# 🐌 Brute-force solution (O(n^2))
# ----------------------------------------

class SolutionBrute(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return i, j

# ----------------------------------------
# ⚡ Optimized solution (O(n)) using hashmap
# ----------------------------------------

def twoSum(nums, target):
    hashmap = {}  # value -> index
    for i, num in enumerate(nums):
        diff = target - num
        if diff in hashmap:
            return [hashmap[diff], i]
        hashmap[num] = i
