class Solution:
    def inOrder(self, root):
        res = []
        self.helper(root, res)
        return res
        
    def helper(self, root, res):
        if root is None:
            return
        
        self.helper(root.left, res)
        res.append(root.data)
        self.helper(root.right, res)
