# User function Template for python3
class Solution:

    def winner(self, arr):
        
        freq = {}
        
        # count votes
        for name in arr:
            freq[name] = freq.get(name, 0) + 1
        
        winner_name = ""
        max_votes = 0
        
        # find winner
        for name, votes in freq.items():
            
            if votes > max_votes:
                max_votes = votes
                winner_name = name
            
            elif votes == max_votes:
                if name < winner_name:
                    winner_name = name
        
        return [winner_name, str(max_votes)]
