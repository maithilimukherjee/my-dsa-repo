class Solution:
    def isSubTree(self, T, S):
        if not S:
            return True
        if not T:
            return False
        
        if self.isIdentical(T, S):
            return True
        
        return self.isSubTree(T.left, S) or self.isSubTree(T.right, S)
    
    
    def isIdentical(self, T, S):
        if not T and not S:
            return True
        if not T or not S:
            return False
        
        return (
            T.data == S.data and
            self.isIdentical(T.left, S.left) and
            self.isIdentical(T.right, S.right)
        )
