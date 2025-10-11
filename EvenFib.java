/*
================================================================================
Sum of Even Fibonacci Numbers ≤ N
================================================================================

Problem Statement:
------------------
Given a number N, find the sum of all the even-valued terms in the Fibonacci
sequence that are less than or equal to N.

Fibonacci sequence: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...

Example:

Input: N = 8
Output: 10
Explanation: Even Fibonacci numbers ≤ 8 are 2 and 8. Sum = 2 + 8 = 10.

--------------------------------------------------------------------------------
Trick / Insight:
----------------
Notice the pattern of even Fibonacci numbers in the sequence:

Fibonacci sequence: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...
Even numbers:      2,    8,       34,         144, ...

Observation:
- Every 3rd Fibonacci number is even. 
- So instead of checking every number, we can directly generate even Fibonacci numbers
  using the recurrence relation for even Fibonacci numbers:

Let E_k = k-th even Fibonacci number
E_1 = 2, E_2 = 8, E_3 = 34, ...
Recurrence: E_k = 4 * E_(k-1) + E_(k-2)

--------------------------------------------------------------------------------
Algorithm:
1. Initialize sum = 0
2. Set first two even Fibonacci numbers: a = 2, b = 8
3. While a ≤ N:
   - Add a to sum
   - Update a, b using a, b = b, 4*b + a
4. Return sum

--------------------------------------------------------------------------------
Java Implementation:
-------------------
*/
class Solution {
    public long sumEvenFibonacci(int N) {
        long sum = 0;
        long a = 2, b = 8; // first two even Fibonacci numbers
        
        while (a <= N) {
            sum += a;
            long next = 4 * b + a; // next even Fibonacci
            a = b;
            b = next;
        }
        
        return sum;
    }
}

/*
--------------------------------------------------------------------------------
Time & Space Complexity:
-----------------------
Time Complexity: O(log N)  // because even Fibonacci numbers grow exponentially
Space Complexity: O(1)

================================================================================
*/
