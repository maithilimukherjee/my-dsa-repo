class Solution:
    def countLeaves(self, root):
        if root is None:
            return 0
        
        # if leaf node
        if root.left is None and root.right is None:
            return 1
        
        return self.countLeaves(root.left) + self.countLeaves(root.right)
