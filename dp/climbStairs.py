class Solution:
  def climbStairs(self,n):
    
    if n==0:
      return 1
    if n==1 or n==2:
      return n

    prev1=1
    prev2=3

    for i in range(3,n+1):
      curr = prev1+prev2
      prev1=prev2
      prev2=curr

    return prev2
