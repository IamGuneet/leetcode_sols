class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        gp = 0
        for x in range(len(nums)):
            for y in range(x+1,len(nums)):
                if nums[x] == nums[y]:
                    gp+=1
        return gp
        
