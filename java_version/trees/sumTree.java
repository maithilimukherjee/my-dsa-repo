class Solution {
    
    boolean isSumTree(Node root) {
        return helper(root) != -1;
    }
    
    int helper(Node node) {
        
        if (node == null) return 0;
        
        // leaf node
        if (node.left == null && node.right == null) {
            return node.data;
        }
        
        int left = helper(node.left);
        int right = helper(node.right);
        
        // if any subtree is invalid
        if (left == -1 || right == -1) return -1;
        
        // check sum tree condition
        if (node.data == left + right) {
            return node.data + left + right;
        } else {
            return -1;
        }
    }
}
