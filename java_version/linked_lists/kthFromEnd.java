class Solution {

    int getKthFromLast(Node head, int k) {
        
        Node slow = head;
        Node fast = head;
        
        // move fast k steps ahead
        for(int i = 0; i < k; i++)
        {
            if(fast == null)
                return -1;   // k > length
            
            fast = fast.next;
        }
        
        // move both until fast reaches end
        while(fast != null)
        {
            slow = slow.next;
            fast = fast.next;
        }
        
        return slow.data;
    }
}
