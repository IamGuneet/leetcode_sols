class Solution:
    def romanToInt(self, s: str) -> int:
        rti = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        val = 0
        prev = 0
        for ch in reversed(s):
            curr = rti[ch]

            if curr < prev:
                val-=curr
            else:
                val+=curr
                
            prev = curr

        return val

    
        
