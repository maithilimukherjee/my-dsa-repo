/*
================================================================================
Number of Digits in Nth Fibonacci Number
================================================================================

Problem Statement:
------------------
Given a number N, find the number of digits in the Nth Fibonacci Number.

Examples:

Input: N = 5
Output: 1
Explanation: 5th Fibonacci number is 5 which contains only one digit

Input: N = 12
Output: 3
Explanation: 12th Fibonacci number is 144 which contains three digits

Your Task:
----------
Complete the function noOfDigits(int N) which returns the number of digits in
the Nth Fibonacci number.

Expected Time Complexity: O(1)
Expected Space Complexity: O(1)

--------------------------------------------------------------------------------
Trick / Insight:
----------------
Directly calculating the Nth Fibonacci number for large N is impractical because
the number grows exponentially. Instead, we can use Binet's formula along with 
logarithms to calculate the number of digits without generating the number itself.

--------------------------------------------------------------------------------
Step 1: Binet’s Formula
----------------------
F(n) = (phi^n - psi^n) / sqrt(5)
where
    phi = (1 + sqrt(5)) / 2  // golden ratio
    psi = (1 - sqrt(5)) / 2

For large n, |psi^n| is negligible, so we can approximate:
F(n) ≈ phi^n / sqrt(5)

--------------------------------------------------------------------------------
Step 2: Number of Digits
------------------------
Number of digits in a number X:
digits = floor(log10(X)) + 1

Substitute F(n):
digits ≈ floor(log10(phi^n / sqrt(5))) + 1
        = floor(n * log10(phi) - 0.5 * log10(5)) + 1

This gives a constant-time solution without calculating the Fibonacci number.

--------------------------------------------------------------------------------
Java Implementation:
-------------------
*/
class Solution {
    public int noOfDigits(int n) {
        // Base case: 1st Fibonacci number is 1, which has 1 digit
        if (n == 1) return 1;

        // Golden ratio
        double phi = (1 + Math.sqrt(5)) / 2;

        // Apply formula: digits = floor(n*log10(phi) - log10(sqrt(5))) + 1
        double digits = n * Math.log10(phi) - 0.5 * Math.log10(5);

        return (int) Math.floor(digits) + 1;
    }
}

/*
--------------------------------------------------------------------------------
Time & Space Complexity:
-----------------------
Time Complexity: O(1)
Space Complexity: O(1)

================================================================================
*/
