class Solution {
    public int oddCells(int m, int n, int[][] indices) {
        int[][] matrix = new int[m][n];
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[i].length; j++) {
        matrix[i][j] = 0;
    }
    }

        for(int i=0;i<indices.length;i++){
            for(int j=0;j<1;j++){
                int row = indices[i][j]; 
                int col = indices[i][j+1]; 

                for(int r=0;r<n;r++){
                    matrix[row][r]++;
                }

                 for(int c=0;c<m;c++){
                    matrix[c][col]++;
                }

            }
        }
        int odd=0;
             for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[i].length; j++) {
                if( matrix[i][j] % 2 != 0 ){
                    odd++;
                }
    }
    }

        return odd;
}
}
