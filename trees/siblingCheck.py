'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
def noSibling(root):
    # code here
    
    res=[]
    
    def dfs(node):
        
        if not node:
            return 
        
        if node.left and not node.right:
            res.append(node.left.data)
            
        if node.right and not node.left:
            res.append(node.right.data)
            
        
        dfs(node.left)
        dfs(node.right)
            
        
    dfs(root)
    
    if not res:
        return [-1]
        
    else:
        return sorted(res)
    
    
    
      
