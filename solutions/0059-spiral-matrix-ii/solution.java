class Solution {
    public int[][] generateMatrix(int n) {
        int[][] arr = new int[n][n];
        int top =0;
        int bottom=n-1;
        int left = 0;
        int right = n-1;
        int pointer =0;
        int[] input = new int[(n*n)];
        for(int i=0;i<(n*n);i++){
            input[i] = i+1;
        }
        while(top<=bottom && left<= right){
            for(int i=left;i<=right;i++){
                arr[top][i] = input[pointer];
                pointer++;
            }
            top++;

            for(int i=top;i<=bottom;i++){
                arr[i][right] = input[pointer];
                pointer++;
            }
            right--;
            
            if(top<=bottom){
                for(int i=right;i>=left;i--){
                arr[bottom][i] = input[pointer];
                pointer++;
            }
            bottom--;
            }

               if(left<=right){
                for(int i=bottom;i>=top;i--){
                arr[i][left] = input[pointer];
                pointer++;
            }
            left++;
            }

        }

        return arr;
        
    }
}
