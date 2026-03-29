'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    def rightView(self, root):
        # code here
        res=[]
        
        def dfs(root,level):
            
            if root is None:
                return
            
            if level==len(res):
                res.append(root.data)
                
            dfs(root.right,level+1)
            dfs(root.left,level+1)
            
        
        dfs(root,0)
        return res
