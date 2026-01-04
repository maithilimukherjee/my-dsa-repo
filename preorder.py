class Solution:
    def preOrder(self, root):
        res = []
        self.helper(root, res)
        return res

    def helper(self, root, res):
        if root is None:
            return
        
        res.append(root.data)
        self.helper(root.left, res)
        self.helper(root.right, res)
