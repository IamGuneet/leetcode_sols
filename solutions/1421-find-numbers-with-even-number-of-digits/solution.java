class Solution {
    public int findNumbers(int[] nums) {
        int even=0;
        for(int i:nums){
            String s = Integer.toString(i);
            int len = s.length();
            if(len%2 == 0){
                even++;
            }
        }
        return even;
    }
}
