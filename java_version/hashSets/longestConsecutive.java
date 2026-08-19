class Solution {
    public int longestConsecutive(int[] arr) {
        // code here
        HashSet<Integer> set = new HashSet<>();
        
        for(int x: arr)
        set.add(x);
        
        int longest = 0;
        
        for(int element:set)
        {
            if(!set.contains(element-1))
            {
                int current = element;
                int count = 1;
                
                while(set.contains(current+1))
                {
                    current++;
                    count++;
                }
                
                if (count>longest)
                longest=count;
            }
        }
        
        return longest;
    }
}
