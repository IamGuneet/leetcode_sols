class Solution:
    def reverseWords(self, s: str) -> str:
        i = len(s) -1
        result = ""

        while i>=0:
            while i>=0 and s[i]==" ":
                i-=1
            
            if i<0 :
                break
            end = i
            while i>=0 and s[i]!=" ":
                i-=1
            word = s[i+1:end+1]
            
            if result !="":
                result+=" "

            result +=word
        return result
        
