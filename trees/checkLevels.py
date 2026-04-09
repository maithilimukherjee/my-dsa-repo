class Solution:
    def check(self, root):
        
        def helper(node, level, leaf_level):
            
            if node is None:
                return True
            
            # if leaf node
            if node.left is None and node.right is None:
                
                # first leaf encountered
                if leaf_level[0] == -1:
                    leaf_level[0] = level
                    return True
                
                # compare with previous leaf level
                return level == leaf_level[0]
            
            # check both sides
            return (helper(node.left, level+1, leaf_level) and 
                    helper(node.right, level+1, leaf_level))
        
        leaf_level = [-1]   # using list to make it mutable
        
        return helper(root, 0, leaf_level)
