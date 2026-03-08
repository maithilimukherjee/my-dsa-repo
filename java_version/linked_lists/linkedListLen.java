/*
class Node{
    int data;
    Node next;
    Node(int a){  data = a; next = null; }
}*/

class Solution {
    public int getCount(Node head) {
        // code here
        Node curr = head;
        int length=0;
        
        while(curr!=null)
        {
            length++;
            curr=curr.next;
        }
        
        return length;
    }
}
