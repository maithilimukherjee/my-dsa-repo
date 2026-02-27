class Solution:
  def maxLength(self,arr):

    prefix=0
    mp={}
    maxi=0
    
    for i in range(len(arr)):
      prefix+=arr[i]
      
      if prefix==0:
        maxi=i+1

      if prefix in mp:
        maxi = max(maxi,i-mp[prefix])

      else:
        mp[prefix]=i

    return maxi
