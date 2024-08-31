class Solution {
    public void rotate(int[] nums, int k) {
        int n = nums.length;
        k = k % n;  
        
        // Create a new array to store the result
        int[] arr = new int[n];
        
        // Place elements in the correct positions
        for (int i = 0; i < n; i++) {
            arr[(i + k) % n] = nums[i];
        }
        
        // Copy the result back to the original array
        for (int i = 0; i < n; i++) {
            nums[i] = arr[i];
        }
    }
}

