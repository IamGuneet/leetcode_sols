class Solution {
    public int[] smallerNumbersThanCurrent(int[] nums) {
        int len = nums.length;
        int[] output = new int[len];

        for(int i=0;i<len;i++){
            int small = 0;
            for(int j=0;j<len;j++){
                if(nums[i] > nums[j]){
                    small++;
                }
            }
            output[i] = small;
        }
        return output;
    }
}
