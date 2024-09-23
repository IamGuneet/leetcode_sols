class Solution {
    public boolean isPerfectSquare(int num) {
        int left = 1;
        int right = num;
        if(num == 1) return true;
        while(left<=right){
            int mid = left + (right-left)/2 ;
            long result = (long) mid*mid;
            if(result == num) return true;
            else if (result > num) {
                right = mid-1;
            }else{
                left = mid+1;
            }
        }

    return false;
    }
}
