import java.util.*;

class Solution {
    // Question:
    // Given an infinite supply of Indian currency denominations {1, 2, 5, 10, 20, 50, 100, 200, 500, 2000}
    // and a target value N, find the minimum number of coins/notes to make N. Return a list of coins used.
    
    // Approach:
    // Use a greedy strategy: pick the largest coin possible repeatedly until N becomes 0.

    public ArrayList<Integer> minPartition(int N) {
        int[] money = {2000, 500, 200, 100, 50, 20, 10, 5, 2, 1};
        ArrayList<Integer> sol = new ArrayList<>();

        for (int coin : money) {
            int count = N / coin;  // how many times this coin fits
            for (int i = 0; i < count; i++) {
                sol.add(coin);  // add each coin individually
            }
            N %= coin;  // remaining amount
        }

        return sol;
    }

    // Example usage
    public static void main(String[] args) {
        Solution solution = new Solution();
        int N = 2753;
        ArrayList<Integer> result = solution.minPartition(N);
        System.out.println(result);  // Output: [2000, 500, 200, 50, 1, 1, 1]
    }
}
