class Solution:
    def intersectPoint(self, head1, head2):
        
        def get_length(head):
            length = 0
            while head:
                length += 1
                head = head.next
            return length
        
        len1 = get_length(head1)
        len2 = get_length(head2)
        
        ptr1 = head1
        ptr2 = head2
        
        if len1 > len2:
            diff = len1 - len2
            for _ in range(diff):
                ptr1 = ptr1.next
        else:
            diff = len2 - len1
            for _ in range(diff):
                ptr2 = ptr2.next
        
        while ptr1 and ptr2:
            if ptr1 == ptr2:
                return ptr1   # return node, not data
            ptr1 = ptr1.next
            ptr2 = ptr2.next
