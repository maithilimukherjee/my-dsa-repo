class Solution {
    public double fractionalKnapsack(int[] val, int[] wt, int capacity) {
        int n = val.length;
        
        // each item: {ratio, value, weight}
        double[][] items = new double[n][3];
        for (int i = 0; i < n; i++) {
            items[i][0] = (double) val[i] / wt[i]; // ratio
            items[i][1] = val[i];
            items[i][2] = wt[i];
        }

        // sort by ratio descending
        java.util.Arrays.sort(items, (a, b) -> Double.compare(b[0], a[0]));

        double totalValue = 0.0;
        int currentWeight = 0;

        for (int i = 0; i < n; i++) {
            if (currentWeight == capacity) break;

            double value = items[i][1];
            double weight = items[i][2];

            if (currentWeight + weight <= capacity) {
                // take whole item
                currentWeight += weight;
                totalValue += value;
            } else {
                // take fraction
                int remaining = capacity - currentWeight;
                totalValue += items[i][0] * remaining;
                currentWeight = capacity; // knapsack full
            }
        }

        return Math.round(totalValue * 1e6) / 1e6;
    }
}
