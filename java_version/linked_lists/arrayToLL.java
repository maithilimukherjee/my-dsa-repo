/*
// Representation of a node
class Node {
    int data;
    Node next;
    Node (int d) {
       data = d;
       next = null;
    }
};
*/
class Solution {
    public Node arrayToList(int arr[]) {
        // code here
        
        int i = 1;
        
        if (arr.length==0)
        return null;
        
        Node head = new Node(arr[0]);
        Node curr = head;
        
        while(i<arr.length)
        {
            curr.next=new Node(arr[i++]);
            curr=curr.next;
        }
        
        return head;
    }
}
