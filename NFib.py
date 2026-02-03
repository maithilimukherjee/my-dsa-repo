#we only care about last digit so we can use mod 10 to keep our numbers small
class Solution:
    def fib (self,N):
        #code here
        
        if N==0:
            return 0
        
        if N==1:
            return 1
        
        a=0    
        b=1
        
        for _ in range(2,N+1):
            
            c=(a+b)%10
            a=b
            b=c
        
        return b