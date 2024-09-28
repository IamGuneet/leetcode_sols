class Solution {
    public int search(int[] nums, int target) {
        int left = 0;
        int right = nums.length -1 ;
        if(right == 0 && nums[0] == target){
            return 0;
        }else if (right == 0){
            return -1;
        }
        while(left<=right){
            int mid = left + (right-left)/2;
            int e = nums[mid];

            if(e == target){
                return mid;
            }else if(e > target){
                right = mid-1;
            }else{
                left = mid+1;
            }
        }
        return -1;


        
    }
}
