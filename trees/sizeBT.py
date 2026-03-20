from typing import Optional
from collections import deque
"""

definition of binary tree node.
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
"""

class Solution:
    def getSize(self, node : Optional['Node']) -> int:
        # code here
        
        if node is None:
            
            return 0
            
        return 1+self.getSize(node.left)+self.getSize(node.right)
        
        
        
