class Solution {
    public boolean checkIfPangram(String sentence) {
        boolean[] check = new boolean[26];
        for(char i: sentence.toCharArray()){
            if(i >= 'a' && i <= 'z'){
                check[i-'a'] = true;
            }
        }

        for(boolean i: check){
            if(i!= true){
                return false;
            }
        }
        return true;
        
        
    }
}
