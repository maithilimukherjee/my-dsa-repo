import java.util.HashMap;

class Solution {
    public boolean isSubset(int a[], int b[]) {
        HashMap<Integer, Integer> countA = new HashMap<>();
        
        // count frequency of elements in a
        for (int num : a) {
            countA.put(num, countA.getOrDefault(num, 0) + 1);
        }
        
        // check each element in b
        for (int num : b) {
            if (!countA.containsKey(num) || countA.get(num) == 0) {
                return false; // b has more of this element than a
            }
            countA.put(num, countA.get(num) - 1); // consume one occurrence
        }
        
        return true; // all elements of b found in a
    }
}
