class Solution:
    def leftView(self, root):
        res = []
        
        def dfs(node, level):
            if not node:
                return
            
            # first node of this level
            if level == len(res):
                res.append(node.data)
            
            # go left first, then right
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
        
        dfs(root, 0)
        return res
