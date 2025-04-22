class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        op =[]
        for x in nums:
            count =0
            for y in nums:
                if x > y:
                    count+=1
            op.append(count)
        return op
        
