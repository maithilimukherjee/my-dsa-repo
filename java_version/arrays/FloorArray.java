class Solution {
    public int findFloor(int[] arr, int x) {
        /*
         * Linear scan O(n):
         * Iterate through the sorted array and keep updating the index of
         * the greatest element seen so far which is <= x.
         */

        int floorIndex = -1;

        for (int i = 0; i < arr.length; i++) {
            if (arr[i] <= x) {
                floorIndex = i;
            } else {
                // since array is sorted, anything further will be > x
                break;
            }
        }

        return floorIndex;
    }
}
