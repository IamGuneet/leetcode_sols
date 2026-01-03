class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = {}
        n = len(nums)
        op= []
        for num in nums:
            count[num] = count.get(num,0)+1
            if count[num] > n//3 and num not in op:
                op.append(num)

        return op
            
        
