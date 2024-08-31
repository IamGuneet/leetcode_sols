class Solution {
    public void setZeroes(int[][] matrix) {
        int rlen= matrix.length;
        int rcol = matrix[0].length;

        boolean[] row = new boolean[rlen];    
        boolean[] col = new boolean[rcol];    

        for(int i=0;i< rlen ; i++){

            for(int j=0;j<rcol;j++){
                if(matrix[i][j] == 0){
                    row[i] = true;
                    col[j] = true;
                }
            }
        }

         for(int i=0;i< rlen ; i++){
            for(int j=0;j<rcol;j++){
                if(row[i] || col[j]){
                    matrix[i][j] =0;
                }
            }
        }
    }
}
