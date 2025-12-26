class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l = len(nums)
        sum_ = (l*(l+1))//2
        tmp = 0
        for i in nums:
            tmp+=i
        return sum_-tmp

        
