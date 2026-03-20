class Solution(object):
    """
    Problem:
    Given two strings s and t, return True if t is an anagram of s, and False otherwise.
    An Anagram is a word or phrase formed by rearranging the letters of another.

    Example:
    Input: s = "anagram", t = "nagaram"
    Output: True

    Input: s = "rat", t = "car"
    Output: False
    """

    def isAnagram(self, s, t):
        """
        Algorithm:
        1. If the lengths of s and t are different, they cannot be anagrams → return False.
        2. Create two integer arrays (size 26) to store letter frequencies for s and t.
        3. Iterate through both strings:
           - Convert each character to its alphabetical index using ord(char) - ord('a').
           - Increment the frequency count for that character in the respective array.
        4. Compare the two frequency arrays:
           - If they are identical, return True (same letters in same amounts).
           - Otherwise, return False.
        """

        # Step 1: Length check
        if len(s) != len(t):
            return False

        # Step 2: Frequency arrays
        count_s = [0] * 26
        count_t = [0] * 26

        # Step 3: Count letters
        for i in range(len(s)):
            count_s[ord(s[i]) - ord('a')] += 1
            count_t[ord(t[i]) - ord('a')] += 1

        # Step 4: Compare frequency arrays
        return count_s == count_t


if __name__ == "__main__":
    # Sample test cases
    sol = Solution()
    print(sol.isAnagram("anagram", "nagaram"))  # True
    print(sol.isAnagram("rat", "car"))          # False
