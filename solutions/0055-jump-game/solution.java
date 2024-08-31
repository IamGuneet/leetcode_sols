class Solution {
    public boolean canJump(int[] nums) {
        int maxR =0;
        int len = nums.length;

        if(len == 1){
            return true;
        }
        for(int i=0;i<len;i++){
           
            if(i >maxR){
                return false;
            }
            maxR = Math.max(maxR,i+nums[i]);
            if(maxR >= len-1){
                return true;
            }

        }
        return false;
    }
}
