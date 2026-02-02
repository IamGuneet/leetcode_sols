class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low = 1
        high = max(nums)

        def calcDivisior(x):
            cur_sum = 0
            for num in nums:
                cur_sum+= math.ceil(num/x)
            return cur_sum <= threshold

        while low <= high:
            mid = (high+low)//2
            if calcDivisior(mid):
                high = mid-1
            else:
                low = mid+1
        return low

        
        
