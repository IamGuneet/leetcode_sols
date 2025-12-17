class Solution:
    def findGCD(self, nums: List[int]) -> int:
        s = nums[0]
        l = nums[0]
        for i in nums:
            if i>l:
                l=i
            if i<s:
                s=i
        def gdc(a,b) -> int:
            if b ==0:
                return a
            else :
                return gdc(b,a%b)
        op = gdc(l,s)
        return op
