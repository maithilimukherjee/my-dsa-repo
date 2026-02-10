class Solution:
    
    # Function to find the maximum number of meetings
    # that can be performed in a meeting room.
    #follow Activity Selection Concept
    
    def maximumMeetings(self, start, end):
        
        n = len(start)
        meetings = []
        
        # make (end, start) pairs
        for i in range(n):
            meetings.append((end[i], start[i]))
        
        # sort by end time
        meetings.sort()
        
        count = 1
        last_end = meetings[0][0]
        
        # select meetings greedily
        for i in range(1, n):
            
            curr_start = meetings[i][1]
            
            if curr_start > last_end:
                count += 1
                last_end = meetings[i][0]
        
        return count
