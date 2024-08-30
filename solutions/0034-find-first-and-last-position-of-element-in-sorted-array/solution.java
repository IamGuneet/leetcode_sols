class Solution {
    public int[] searchRange(int[] nums, int target) {
        int len = nums.length;
        int[] result = {-1,-1};
        for(int i =0;i<len;i++){
            if(nums[i] == target){
                if(result[0] == -1){
                    result[0] = i;
                }
            result[1] = i;
            }

        }     

        return result;
    }
}
