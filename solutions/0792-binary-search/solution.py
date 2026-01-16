class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left =0
        right = len(nums)-1
        while(left<=right):
            idx = right - (right-left)//2
            e = nums[idx]

            if(e == target):
                return idx
            elif e>target:
                right = idx-1
            else:
                left = idx+1
        return -1
            
