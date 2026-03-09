class Solution {
    public Node insertInMiddle(Node head, int x) {
        if (head == null) {
            return new Node(x);
        }

        Node newNode = new Node(x);
        Node slow = head;
        Node fast = head;

        // Move fast twice as fast as slow. 
        // When fast reaches the end (or second to last), 
        // slow will be at the insertion point.
        while (fast.next != null && fast.next.next != null) {
            fast = fast.next.next;
            slow = slow.next;
        }

        // Insert newNode after the slow pointer
        newNode.next = slow.next;
        slow.next = newNode;

        return head;
    }
}
