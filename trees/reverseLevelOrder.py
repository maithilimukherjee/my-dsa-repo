from collections import deque

class Solution:
    def reverseLevelOrder(self, root):
        if root is None:
            return []
        
        q = deque()
        q.append(root)
        res = []
        
        while q:
            node = q.popleft()
            res.append(node.data)
            
            # IMPORTANT: push right first, then left
            if node.right:
                q.append(node.right)
            if node.left:
                q.append(node.left)
        
        return res[::-1]
