class Solution:
	def pythagoreanTriplet(self, arr):
    	# code here
    	
    	seen=set()
    	
    	for num in arr:
    	    
    	    seen.add(num*num)
    	    
    	for i in range(0,len(arr)):
    	    
    	    for j in range(i+1,len(arr)):
    	        
    	        s = arr[i]**2 + arr[j]**2
    	        
    	        if s in seen:
    	            
    	            return True
    	            
        return False
    	 
