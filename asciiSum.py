"""
Given a string s consisting of lowercase English letters, for every character whose first and last occurrences are at different positions, calculate the sum of ASCII values of characters strictly between its first and last occurrence.
Return all such non-zero sums (order does not matter).

"""

class Solution:
    def asciirange(self, s):
        from collections import defaultdict
        
        # store all indices where each character appears
        char_indices = defaultdict(list)
        for i, ch in enumerate(s):
            char_indices[ch].append(i)
        
        res = []
        
        for ch in char_indices:
            positions = char_indices[ch]
            if len(positions) >= 2:
                first = positions[0]
                last = positions[-1]
                # sum ASCII values of characters strictly between
                total = sum(ord(s[i]) for i in range(first + 1, last))
                if total > 0:
                    res.append(total)
        
        return res
