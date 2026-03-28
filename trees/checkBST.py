class Solution:
    def isBST(self, root):
        self.prev = float('-inf')
        
        def inorder(node):
            if not node:
                return True
                
            if not inorder(node.left):
                return False
                
            if node.data <= self.prev:
                return False
                
            self.prev = node.data
            
            return inorder(node.right)
        
        return inorder(root)
