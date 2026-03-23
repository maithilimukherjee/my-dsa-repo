class Solution:
    def kthLargest(self, root, k):
        self.count = 0
        self.ans = None
        
        def reverse_inorder(node):
            if not node or self.ans is not None:
                return
            
            # go right first (largest)
            reverse_inorder(node.right)
            
            self.count += 1
            if self.count == k:
                self.ans = node.data
                return
            
            reverse_inorder(node.left)
        
        reverse_inorder(root)
        return self.ans
