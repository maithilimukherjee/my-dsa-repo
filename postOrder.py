class Solution:
    def postOrder(self, root):
        res = []
        self.helper(root, res)
        return res

    def helper(self, root, res):
        if root is None:
            return
        
        self.helper(root.left, res)
        self.helper(root.right, res)
        res.append(root.data)
