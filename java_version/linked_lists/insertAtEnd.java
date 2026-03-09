/*
class Node{
    int data;
    Node next;

    Node(int x){
        data = x;
        next = null;
    }
}
*/
class Solution {
    public Node insertAtEnd(Node head, int x) {
        // code here
        
        if (head==null)
        {
            return new Node(x);
        }
        
        Node curr = head;
        
        while(curr.next!=null)
        {
            curr=curr.next;
        }
        
        Node newNode = new Node(x);
        curr.next=newNode;
        
        return head;
    }
}
