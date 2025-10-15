class Solution {
    int maxSubarraySum(int[] arr) {
        int maxEndingHere = arr[0];
        int maxSoFar = arr[0];
        
        for(int i = 1; i < arr.length; i++) {
            // either extend the previous subarray or start fresh from current element
            maxEndingHere = Math.max(arr[i], maxEndingHere + arr[i]);
            // track the best we've seen so far
            maxSoFar = Math.max(maxSoFar, maxEndingHere);
        }
        
        return maxSoFar;
    }
}
