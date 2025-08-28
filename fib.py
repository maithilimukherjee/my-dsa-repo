#fibonnaci in python

#User function Template for python3

class Solution:
    #Function to return list containing first n fibonacci numbers.
    def fibonacciNumbers(self,n):
        # your code here
        if n==1:
            return [0]
            
        elif n==2:
            return [0,1]
        
        else:
            a = 0
            b = 1
            t = a+b
            fib = [0,1]
            
            for i in range(2,n):
                fib.append(t)
                a = b
                b = t
                t = a+b
            
            return fib
            
