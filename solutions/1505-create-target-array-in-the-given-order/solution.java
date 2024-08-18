class Solution {
    public int[] createTargetArray(int[] nums, int[] index) {
        ArrayList<Integer> target = new ArrayList<>();
        for(int i =0;i<nums.length;i++){
            target.add(index[i],nums[i]);
        }
        int[] output = new int[nums.length];

        for(int i=0;i<nums.length;i++){
            output[i] = target.get(i);
        }
        return output;
    }
}
