class Solution:
    def is_sum_tree(self, node):
        
        def helper(node):
            if node is None:
                return (True, 0)
            
            if node.left is None and node.right is None:
                return (True, node.data)
            
            left_ok, left_sum = helper(node.left)
            right_ok, right_sum = helper(node.right)
            
            if node.data == left_sum + right_sum:
                return (left_ok and right_ok, node.data + left_sum + right_sum)
            else:
                return (False, 0)
        
        return helper(node)[0]
