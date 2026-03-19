"""
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
"""

class Solution:
    def minValue(self, root):
        # code here
        
        if root is None:
            return None
            
        if root.left is None:
            return root.data
            
        return self.minValue(root.left)
