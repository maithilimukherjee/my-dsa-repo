class Solution:
    def mirror(self, root):
        
        if root is None:
            return None
        
        # swap
        root.left, root.right = root.right, root.left
        
        # recurse on children
        self.mirror(root.left)
        self.mirror(root.right)
        
        return root
