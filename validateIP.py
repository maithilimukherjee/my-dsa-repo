class Solution:
    def isValid(self, s):
        
        parts = s.split(".")
        
        if len(parts) != 4:
            return False
        
        for part in parts:
            
            # empty check
            if part == "":
                return False
            
            # only digits
            if not part.isdigit():
                return False
            
            # leading zero check
            if len(part) > 1 and part[0] == '0':
                return False
            
            num = int(part)
            
            # range check
            if num < 0 or num > 255:
                return False
        
        return True
