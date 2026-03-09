class Solution:
    def areIsomorphic(self, s1, s2):
        if len(s1) != len(s2):
            return False
            
        # mp1 tracks s1 -> s2, mp2 tracks s2 -> s1
        mp1 = {}
        mp2 = {}
        
        for char1, char2 in zip(s1, s2):
            # Check s1 -> s2 mapping
            if char1 in mp1:
                if mp1[char1] != char2:
                    return False
            else:
                mp1[char1] = char2
                
            # Check s2 -> s1 mapping to ensure uniqueness
            if char2 in mp2:
                if mp2[char2] != char1:
                    return False
            else:
                mp2[char2] = char1
                    
        return True
