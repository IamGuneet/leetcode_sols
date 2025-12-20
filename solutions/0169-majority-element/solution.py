class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ht = {}
        for i in nums:
            ht[i] = ht.get(i,0)+1
            if ht[i] > len(nums)//2:
                return i
        
        
