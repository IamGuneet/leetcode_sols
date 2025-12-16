class Solution:
    def isPalindrome(self, x: int) -> bool:
        op = False
        x = str((x))
        if x == x[::-1]:
            op = True
        return op
        
