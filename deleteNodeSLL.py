class node:
    def __init__(self):
        self.data = None
        self.next = None

class Solution:
    # Question:
    # Given the head of a singly linked list and an integer k (1-based indexing),
    # delete the k-th node from the list and return the updated head.

    # Approach:
    # 1. If k == 1, delete the head by returning head.next.
    # 2. For k > 1, traverse the list while keeping track of the previous node.
    # 3. Once the k-th node is reached, set prev.next = curr.next to skip it.
    # 4. Return the head of the updated list.
    
    def deleteNode(self, head, k):
        # If we need to delete the first node
        if k == 1:
            return head.next  # new head

        curr = head
        prev = None
        count = 1  # 1-based indexing

        # Traverse to the k-th node
        while curr is not None and count < k:
            prev = curr
            curr = curr.next
            count += 1

        # Delete the k-th node by skipping it
        if curr is not None:
            prev.next = curr.next

        return head
