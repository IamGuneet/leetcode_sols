class Solution {
    public int singleNonDuplicate(int[] nums) {
        int len = nums.length;
        int left = 0;
        int right = len - 1;

        while (left < right) {
            int mid = left + (right - left) / 2;
            int e = nums[mid];
            
            // Check if mid is even or odd
            if (mid % 2 == 0) {
                if (e == nums[mid + 1]) {
                    left = mid + 2;  // Move left to mid + 2 to exclude the pair
                } else {
                    right = mid;     // Narrow down the search to the left side
                }
            } else {
                if (e == nums[mid - 1]) {
                    left = mid + 1;  // Move left to exclude the correct pair
                } else {
                    right = mid;     // Narrow down the search to the left side
                }
            }
        }
        return nums[left];
    }
}

