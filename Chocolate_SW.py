"""
Problem:
Given an array arr[] of positive integers, where each value represents the number of chocolates in a packet.
There are M students, and the task is to distribute chocolate packets such that:
    1. Each student gets exactly one packet.
    2. The difference between the maximum and minimum number of chocolates in the chosen packets is minimized.

Return this minimum possible difference.
"""

class Solution:
    def findMinDiff(self, arr, M):
        # Sort the packets
        arr.sort()
        
        # Initialize minimum difference
        diff = float('inf')
        
        # Slide a window of size M
        for i in range(len(arr) - M + 1):
            current_diff = arr[i + M - 1] - arr[i]
            diff = min(diff, current_diff)
        
        return diff

class Solution:
    def findMinDiff(self, arr, M):
        arr.sort()
        diff = float('inf')  
        
        for i in range(len(arr) - M + 1):
            d = arr[i + M - 1] - arr[i]
            if d < diff:
                diff = d
        
        return diff
