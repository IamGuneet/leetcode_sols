class Solution {
    public int largestAltitude(int[] gain) {
        int curralt =0;
        int max=0;

        for(int i=0;i<gain.length;i++){
            curralt += gain[i];
            if(curralt > max){
                max = curralt;
            }
        }
        return max;
    }

}
