class Solution {
    public int[] buildArray(int[] nums) {
        int length = nums.length;
        int[] newArr = new int[length];
        int[] temp = nums;
        
        for(int i=0;i<length;i++){
            newArr[i] = temp[temp[i]];
        }

        return newArr;
    }
}
