'''
# node class:

class Node:
    def __init__(self,val):
        self.next=None
        self.data=val

'''

class Solution:
    def removeLoop(self, head):
        
        slow = head
        fast = head
        
        # phase 1: detect loop
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                break
        else:
            return  # no loop
        
        # phase 2: remove loop
        slow = head
        
        # special case: loop starts at head
        if slow == fast:
            while fast.next != slow:
                fast = fast.next
            fast.next = None
            return
        
        # normal case
        prev = None
        while slow != fast:
            prev = fast
            slow = slow.next
            fast = fast.next
        
        prev.next = None
