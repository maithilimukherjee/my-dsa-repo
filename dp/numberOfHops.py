#User function Template for python3

class Solution:
    #Function to count the number of ways in which frog can reach the top.
    def countWays(self,n):
        
        # code here
        
        if n==0:
            return 1
            
        elif n==1:
            return 1
        
        elif n==2:
            return 2
            
        else:
            
            a=1
            b=1
            c=2
            
            for step in range(3,n+1):
                
                d=a+b+c
                a=b
                b=c
                c=d
                
            return c 
