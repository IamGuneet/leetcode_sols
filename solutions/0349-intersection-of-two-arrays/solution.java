import java.util.Arrays;

public class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        // Sort both arrays
        Arrays.sort(nums1);
        Arrays.sort(nums2);

        // Temporary array to store results
        int[] temp = new int[Math.min(nums1.length, nums2.length)];
        int index = 0;

        // Two pointers
        int i = 0, j = 0;

        // Traverse both arrays
        while (i < nums1.length && j < nums2.length) {
            if (nums1[i] == nums2[j]) {
                // Only add if it's the first occurrence or not a duplicate
                if (index == 0 || temp[index - 1] != nums1[i]) {
                    temp[index++] = nums1[i];
                }
                i++;
                j++;
            } else if (nums1[i] < nums2[j]) {
                i++; // Move pointer for nums1
            } else {
                j++; // Move pointer for nums2
            }
        }

        // Return the result array with the exact size
        return Arrays.copyOfRange(temp, 0, index);
    }
}

