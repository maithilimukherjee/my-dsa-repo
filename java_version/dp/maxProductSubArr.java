class Solution {
    int maxProduct(int[] arr) {
        // code here
        int maxProduct=arr[0];
        int minProduct=arr[0];
        int ans=arr[0];
        
        int tempMax=0;
        int tempMin=0;
        
        for(int i=1; i<arr.length; i++)
        {
            int num = arr[i];
            
            tempMax = Math.max(num, Math.max(num*maxProduct, num*minProduct));
            tempMin = Math.min(num, Math.min(num*maxProduct, num*minProduct));
            
            maxProduct=tempMax;
            minProduct=tempMin;
        
        ans=Math.max(ans,maxProduct);
        
        }
        return ans;
    }
}
