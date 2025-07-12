# LC 38 - Count and Say
# https://leetcode.com/problems/count-and-say/
# Generates the nth term in the "Count and Say" sequence.
# Time: O(n * m), where m is avg length of sequence at each step

class Solution(object):
    def countAndSay(self, n):
        if n == 1:
            return "1"
        
        sequence = "1"  # Start with "1"
        
        for _ in range(n - 1):
            new_seq = ""
            count = 1

            for j in range(1, len(sequence)):
                if sequence[j] == sequence[j - 1]:
                    count += 1
                else:
                    new_seq += str(count) + sequence[j - 1]
                    count = 1
            
            # Add last group
            new_seq += str(count) + sequence[-1]
            sequence = new_seq

        return sequence

# 🧪 Example usage
if __name__ == "__main__":
    s = Solution()
    print(s.countAndSay(5))  # Output: "111221"
