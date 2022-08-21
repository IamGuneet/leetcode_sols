class Solution {
    public int[] buildArray(int[] nums) {
                    int[] ans = new int[nums.length] ;

        for(int element: nums){

            ans[element] = nums[nums[element]]; 

        }
       
                    return ans;

    }
}
