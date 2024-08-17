class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        int len = candies.length;
        List<Boolean> result = new ArrayList<>();

        for(int i=0;i<len;i++){
            int sum = candies[i] + extraCandies;
            boolean great = true;
            for(int j=0;j<len;j++){
                if(sum < candies[j]){
                    great = false;
                }
            }
            result.add(great);
        }

        return result;
    }
}
