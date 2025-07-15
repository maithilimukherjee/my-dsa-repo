// LC 3136 - Check if a string is a valid word
// https://leetcode.com/problems/check-if-a-string-is-a-valid-word
// Time: O(n), Space: O(1)

class Solution {
    public boolean isValid(String word) {
        if (word.length() < 3) return false;

        int vowelCount = 0;
        int consonantCount = 0;

        for (int i = 0; i < word.length(); i++) {
            char temp = word.charAt(i);

            // Return false if not a letter or digit
            if (!Character.isLetterOrDigit(temp)) {
                return false;
            }

            // Check for vowels
            if (temp == 'a' || temp == 'e' || temp == 'i' || temp == 'o' || temp == 'u' ||
                temp == 'A' || temp == 'E' || temp == 'I' || temp == 'O' || temp == 'U') {
                vowelCount++;
            } 
            // Count consonants (ignore digits)
            else if (Character.isLetter(temp)) {
                consonantCount++;
            }
        }

        return vowelCount > 0 && consonantCount > 0;
    }
}
