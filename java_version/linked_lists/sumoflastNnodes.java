/*
Node class is as follows:

class Node {
    int data;
    Node next;

    public Node (int data){
        this.data = data;
        this.next = null;
    }
}
*/

class Solution {

    // Return the sum of last k nodes
    public int sumOfLastN_Nodes(Node head, int n) {
        // write code here
        int sum=0;
        Node current=head;
        
        int c=0;
        int length=0;
        
        while(current!=null)
        {
            length++;
            current=current.next;
        }
        
        
        current=head;
        
        int pos = length-n+1;
        
        while(current!=null)
        {
            c++;
            
            if(c>=pos)
            sum=sum+current.data;
            
            current=current.next;
        }
        
        return sum;
    }
}
