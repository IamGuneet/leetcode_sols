class Solution {
    public int peakIndexInMountainArray(int[] arr) {
        int left = 0;
        int right = arr.length -1;
        while(left<right){
            int mid = left + (right-left)/2 ;
            int ele = arr[mid];

            if(ele> arr[mid+1]){
                right = mid;
            }else{
                left = mid+1;
            }
        }
        return left;
    }
}
