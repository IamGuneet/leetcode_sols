class Solution {
    public int[] searchRange(int[] nums, int target) {
        int[] result = new int[2];
        int len = nums.length;
        result[0] = -1;
        result[1] = -1;
        int left = 0;
        int right = len -1;
        while(left <= right){
            int mid = left + (right-left)/2;
            int val = nums[mid];

            if(val == target){
                result[0] = mid;
                right = mid -1;
            }else if( val < target){
                left = mid +1;
            }else{
                right = mid-1;
            }

        }
        
        left = 0;
        right = len -1;
           while(left <= right){
            int mid = left + (right-left)/2;
            int val = nums[mid];

            if(val == target){
                result[1] = mid;
                left = mid +1;
            }else if( val < target){
                left = mid +1;
            }else{
                right = mid-1;
            }

        }

        return result;
    }
}
