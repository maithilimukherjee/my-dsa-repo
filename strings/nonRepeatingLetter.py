class Solution:
    def nonRepeatingChar(self,s):
        #code here
        
        freq={}
        
        for letter in s:
            
            freq[letter]=freq.get(letter,0)+1
            
        for letter in s:
            
            if freq[letter]==1:
                return letter
                
        return '$'
