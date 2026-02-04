class Solution:
    def getLastMoment(self, n, left, right):
        # variable to store maximum fall time
        fall = 0
        
        # for ants moving left
        # time to fall = position
        for x in left:
            fall = max(fall, x)
        
        # for ants moving right
        # time to fall = n - position
        for x in right:
            fall = max(fall, n - x)
        
        # return the last moment
        return fall
