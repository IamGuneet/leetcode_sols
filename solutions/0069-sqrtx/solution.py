class Solution:
    def mySqrt(self, x: int) -> int:
        low =1
        high =x
        result =0
        if x == 0:
            return x
        while high>=low:
            mid = (low +(high-low)//2)
            if (x/mid >= mid and mid*mid <= x  ):
                result = mid
                low = mid+1
            else:
                high = mid-1
        return result    
