class Solution {
    public int diagonalSum(int[][] mat) {
        int sum =0;
            int len = mat.length;
        // primary
        for(int i=0;i<mat.length;i++){
            for(int j=0;j<mat[i].length;j++){
                if(i==j){
                    sum = sum + mat[i][j];
                }
                if(j == len -1-i ){
                    sum = sum + mat[i][j];
                }
            }
        }
        if(len%2 !=0 ){
            sum = sum - mat[len/2][len/2];
        }

return sum;
    }
}
