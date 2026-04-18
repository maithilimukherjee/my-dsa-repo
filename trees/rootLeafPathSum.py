'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''


class Solution:

    def hasPathSum(self, root, target):
        '''
        :param root: root of given tree.
        :param sm: root to leaf sum
        :return: true or false
        '''
        # use recursive DFS
        
        if root is None:
            
            return False
            
        if not root.left and not root.right:
            
            if root.data==target:
                return True
                
            else:
                return False
                
        remaining = target-root.data
        
        return (self.hasPathSum(root.left,remaining) or self.hasPathSum(root.right,remaining))
        
    
        
        
