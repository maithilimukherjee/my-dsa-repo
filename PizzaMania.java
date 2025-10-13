/*
Small Pizza has an area of 'S' units. Medium Pizza has an area of 'M' units. Large Pizza has an area of 'L' units. Cost of Small, medium and Large Pizza is 'CS' , 'CM', and 'CL' respectively. 
What is the minimum amount of money needed so that one can buy atleast X units square of Pizza?
Example 1: Input: X = 16, S = 3, M = 6, L = 9, CS = 50, CM = 150, CL = 300 Output: 300 
Explanation: We want atleast 16 sq. units of Pizza.
1S 1M 1L area= 3+6+9 = 18 sq units, Cost=500 6S area=18 sq units, Cost=300 2L area=18 sq units, Cost=600 etc. 
Of all the Arrangements, Minimum Cost is Rs. 300.
*/

class Solution {
    static int getPizza(int X, int S, int M, int L, int CS, int CM, int CL) {
        int maxArea = X + Math.max(S, Math.max(M, L));  // buffer
        int[] dp = new int[maxArea + 1];
        
        // large number init
        java.util.Arrays.fill(dp, Integer.MAX_VALUE / 2);
        dp[0] = 0;

        for (int i = 1; i <= maxArea; i++) {
            if (i >= S) dp[i] = Math.min(dp[i], dp[i - S] + CS);
            if (i >= M) dp[i] = Math.min(dp[i], dp[i - M] + CM);
            if (i >= L) dp[i] = Math.min(dp[i], dp[i - L] + CL);
        }

        int ans = Integer.MAX_VALUE;
        for (int i = X; i <= maxArea; i++) {
            ans = Math.min(ans, dp[i]);
        }

        return ans;
    }
}
