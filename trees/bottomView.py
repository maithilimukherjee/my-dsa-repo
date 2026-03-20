from collections import deque

class Solution:
    def bottomView(self, root):
        if not root:
            return []
        
        mp = {}   # hd -> node.data
        q = deque()
        
        q.append((root, 0))
        
        while q:
            node, hd = q.popleft()
            
            # overwrite every time
            mp[hd] = node.data
            
            if node.left:
                q.append((node.left, hd - 1))
            
            if node.right:
                q.append((node.right, hd + 1))
        
        return [mp[key] for key in sorted(mp)]
