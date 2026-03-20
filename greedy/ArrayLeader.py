/*
Input: arr = [16, 17, 4, 3, 5, 2] 
Output: [17, 5, 2]
Explanation: Note that there is nothing greater on the right side of 17, 5 and, 2.
*/

class Solution:
    def leaders(self, arr):
        n = len(arr)
        leaderArr = []
        
        for i in range(n):
            flag = 0
            for j in range(i+1, n):
                if arr[j] > arr[i]:
                    flag = 1
                    break
            
            if flag == 0:
                leaderArr.append(arr[i])
        
        return leaderArr

// Greedy Approach
//Instead of checking every element to the right, we can simply traverse the array from right to left and keep track of the maximum we’ve seen so far.
//If arr[i] >= max_from_right, then arr[i] is a leader.


  class Solution:
    def leaders(self, arr):
        n = len(arr)
        leaderArr = []
        max_from_right = float('-inf')
        
        for i in range(n-1, -1, -1):
            if arr[i] >= max_from_right:
                leaderArr.append(arr[i])
                max_from_right = arr[i]
        
        # reverse since we traversed from right
        return leaderArr[::-1]

  
