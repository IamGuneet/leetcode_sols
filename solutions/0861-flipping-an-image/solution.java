import java.util.*;
class Solution {
    public int[][] flipAndInvertImage(int[][] image) {
        int arrays = image.length;
        int arraylength = image[0].length;
        int[][] output = new int[image.length][arraylength];

        for(int i=0;i<arrays;i++){
            for(int j=0;j<arraylength;j++){
                output[i][arraylength -1-j] = Math.abs(image[i][j] - 1);
            }
        }
        return output;
    }
}
