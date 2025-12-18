class Solution:
    def isPalindrome(self, s: str) -> bool:
        def check(s,i=0):
            if(i >= len(s)//2):
                return True
            
            if (s[i] != s[len(s)-i-1]):
                return False
            
            return check(s,i+1)
        s = s.lower()
        s = "".join(ch for ch in s if ch.isalnum())
        return check(s)
        
