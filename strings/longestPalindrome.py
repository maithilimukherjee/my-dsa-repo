class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]

        longest = ""
        for i in range(len(s)):
            # odd length palindrome
            temp = expand(i, i)
            if len(temp) > len(longest):
                longest = temp
            # even length palindrome
            temp = expand(i, i+1)
            if len(temp) > len(longest):
                longest = temp

        return longest
