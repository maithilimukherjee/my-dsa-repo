/*
PROBLEM:
Given a square matrix M of size n x n, where M(i,j) = i + j (1-based indexing),
and a number q, count how many times the number q appears in the matrix.

TRICK:
We want number of pairs (i, j) such that:
  1 <= i <= n, 1 <= j <= n, and i + j == q

This becomes:
  j = q - i
So j is valid only when:
  1 <= q - i <= n
Solve for i:
  q - n <= i <= q - 1
And i also must be in [1, n]

So valid i range is:
  low = max(1, q - n)
  high = min(n, q - 1)

Final count = high - low + 1
*/

class Solution {
    static long sumMatrix(long n, long q) {
        long low = Math.max(1, q - n);
        long high = Math.min(n, q - 1);
        
        if (low > high) return 0;  // no valid (i, j) pairs
        
        return high - low + 1;
    }
}
