class Solution {
    static int lis(int arr[]) {
        // code here
        
        int low, high = 0;
        int n = arr.length;
        int tails[] = new int[n];
        int k=1;
        int mid = 0;
        
        tails[0]=arr[0];
        
        for(int i=1; i<arr.length; i++)
        {
            if (tails[k-1]<arr[i])
            {
                tails[k++]=arr[i];
            }
            
            else
            {
                low=0;
                high=k-1;
                
                while(low<=high)
                {
                    mid=(low+high)/2;
                    
                    if (tails[mid]>=arr[i])
                    high=mid-1;
                    
                    else
                    low=mid+1;
                }
                
                tails[low]=arr[i];
            }
        }
        
        return k;
        
    }
}
