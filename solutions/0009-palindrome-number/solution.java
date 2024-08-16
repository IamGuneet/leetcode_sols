class Solution {
    public boolean isPalindrome(int x) {
          if (x < 0) {
            return false;
        }

        int l =x;
        int y=0;
    while(x!=0){
            y = y*10 + x%10;
            x = x/10;
        }
        if(y == l){
            return true;
        }
       return false;
    }
}
