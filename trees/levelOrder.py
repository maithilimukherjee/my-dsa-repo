class Solution:
    def levelOrder(self, root):
        if not root:
            return []
            
        res = []
        
        def bfs(nodes):
            if not nodes:
                return
            
            next_level = []
            level_vals = []
            
            for node in nodes:
                level_vals.append(node.data)
                
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            
            res.append(level_vals)
            bfs(next_level)
        
        bfs([root])
        return res
