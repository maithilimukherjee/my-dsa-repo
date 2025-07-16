# LC 141 - Linked List Cycle
# https://leetcode.com/problems/linked-list-cycle/
# Time: O(n), Space: O(1)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        Detects if a linked list has a cycle using Floyd’s Tortoise and Hare algorithm.

        Step-by-step:
        1. Initialize two pointers, slow and fast, both starting at the head.
        2. Move slow by 1 step and fast by 2 steps in each iteration.
        3. If there is a cycle, fast will eventually meet slow inside the cycle.
        4. If fast reaches the end (i.e., None), there’s no cycle.

        :type head: ListNode
        :rtype: bool
        """
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next          # move one step
            fast = fast.next.next     # move two steps
            if slow == fast:
                return True           # cycle detected

        return False                  # reached end, no cycle
