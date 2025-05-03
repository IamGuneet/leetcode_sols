# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        low = 0
        high = n
        result =0

        while high>=low:
            mid = low+(high-low)//2
            op = guess(mid)
            if(op == 0):
                result = mid
                return result
            elif op == -1:
                high = mid-1
            else:
                low = mid+1

        # return result


