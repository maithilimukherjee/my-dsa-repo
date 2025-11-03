## Subset Sum Problem

### Question
Given an array of positive integers `arr[]` and a value `sum`, determine if there exists a subset of `arr[]` whose sum equals `sum`.


### ⚡ Trick
Use the **Include–Exclude** principle.  
For every element, you have **two choices**:  
1. Include it in the subset → decrease `sum` by that element.  
2. Exclude it → move to the next element.  

Base conditions:  
- `sum == 0` → subset found ✅  
- `arr.length == 0` → no subset left ❌  

### 💻 Code
```java
class Solution {
    static boolean isSubsetSum(int arr[], int sum) {
        // base cases
        if (sum == 0)
            return true; // subset found
        if (arr.length == 0)
            return false; // no elements left

        // pick the last element
        int last = arr[arr.length - 1];

        // if last element > sum → can't include it
        if (last > sum) {
            int newArr[] = new int[arr.length - 1];
            for (int i = 0; i < arr.length - 1; i++)
                newArr[i] = arr[i];
            return isSubsetSum(newArr, sum);
        } else {
            // either include or exclude the last element
            int newArr[] = new int[arr.length - 1];
            for (int i = 0; i < arr.length - 1; i++)
                newArr[i] = arr[i];

            // check both possibilities
            return isSubsetSum(newArr, sum - last) || isSubsetSum(newArr, sum);
        }
    }
}
