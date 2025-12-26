class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        max_ = 0
        for i in nums:
            if i == 0:
                if count>= max_:
                    max_ = count
                count = 0
            else:
                count+=1
        return max(count,max_)
        
