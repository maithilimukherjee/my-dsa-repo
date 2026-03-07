import java.util.HashSet;

public class Solution
{
  public boolean hasTripletSum(int[] arr, int target)
  {
      int n = arr.length;

      for(int i=0; i<n; i++)
        {
          HashSet<Integer> seen = new HashSer<>();
          int currTarget = target - arr[i];

          for(int j=i+1; j<n;j++)
            {
              if(seen.contains(currTarget-arr[j]))
              {
                return true;
              }

              seen.add(arr[j]);
            }
        }

       return false;
  }

