class Solution {
    static int evenlyDivides(int n) {
        int copy = n;
        int countDig = 0;
        
        while (copy > 0) {
            int digit = copy % 10; // take last digit
            
            // avoid dividing by zero
            if (digit != 0 && n % digit == 0) {
                countDig++;
            }
            
            copy = copy / 10;
        }
        
        return countDig;
    }
}
