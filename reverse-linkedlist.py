# LC 206 - Reverse Linked List
# https://leetcode.com/problems/reverse-linked-list/
# Time: O(n), Space: O(1)

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        prev = None
        curr = head

        while curr:
            next_node = curr.next   # store next node
            curr.next = prev        # reverse the link
            prev = curr             # move prev forward
            curr = next_node        # move curr forward

        return prev  # new head of the reversed list
