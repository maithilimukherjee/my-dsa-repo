class Solution:
    def lis(self, arr):
        # code here
        
        tails=[]
        pos=0
        low=0
        high=0
        
        tails.append(arr[0])
        
        for i in range(1,len(arr)):
            
            if arr[i]>tails[-1]:
                tails.append(arr[i])
                
            else:
                
                low=0
                high=len(tails)-1
                
                while low<=high:
                    
                    mid=(low+high)//2
                    
                    if tails[mid]>=arr[i]:
                        high=mid-1
                    
                    else:
                        low=mid+1
            
                tails[low]=arr[i]
            
        return len(tails)
