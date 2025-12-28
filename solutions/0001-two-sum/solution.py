class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}

        for index,val in enumerate(nums):
            if target-val in seen:
                return [seen[target-val],index]
            else:
                seen[val] = index

        
