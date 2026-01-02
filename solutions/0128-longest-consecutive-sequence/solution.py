class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        nums.sort()
        cur = nums[0]
        count = 1
        max_count = 1

        for i in range(1,len(nums)):
            if nums[i]-1 == cur:
                count+=1
            elif nums[i] == cur:
                continue
            else:
                count=1
            cur = nums[i]
            max_count = max(count,max_count)
        return max_count

        
