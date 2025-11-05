#dfs each node
#take max among each of the paths that hit NULL

'''
# Node Class:
class Node:
    def _init_(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def height(self, root):
        # code here
        
        if not root:
            return 0
        
        else:
            left = self.maxDepth(root.left)
            right = self.maxDepth(root.right)
            
        return max(left,right) + 1
