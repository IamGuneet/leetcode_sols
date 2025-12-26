class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        occur = {}
        for num in nums:
            occur[num] = occur.get(num,0 )+1
        for key,val in occur.items():
            if val == 1:
                return key
        
