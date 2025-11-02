
class Solution:
    def isPanagram(self, S):
        # convert string to lowercase
        S = S.lower()
        
        # create a dictionary for all alphabets with initial value 0
        alpha_dict = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}
        
        # mark letters that appear in the string
        for ch in S:
            if 'a' <= ch <= 'z':
                alpha_dict[ch] = 1
        
        # check if all values are 1 (means all letters are present)
        for val in alpha_dict.values():
            if val == 0:
                return 0  # not a pangram
                
        return 1  # pangram
