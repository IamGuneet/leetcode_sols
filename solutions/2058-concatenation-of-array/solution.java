class Solution {
    public int[] getConcatenation(int[] nums) {
        int[] ans = new int[2*nums.length];
        // ans[0]=nums[0];
        // ans[nums.length]=nums[0];
        int x = nums.length;
        for(int i=0;i<nums.length;i++){
            ans[i] = nums[i];
                ans[i+x] = nums[i];
        }
        return ans;
    }
}
