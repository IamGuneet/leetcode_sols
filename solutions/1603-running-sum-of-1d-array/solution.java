class Solution {
    public int[] runningSum(int[] nums) {
        int[] ans = new int[nums.length];
        for(int i=0;i<nums.length;i++){
            int x=0;
            for(int y=0;y<=i;y++){
                x+=nums[y];
            }
            ans[i]=x;
        }   
        return ans;      
}
}
