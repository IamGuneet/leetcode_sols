class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1

        while(left<right):
            mid = (left+right)//2
            e = nums[mid]
            if (mid%2 == 1 and nums[mid-1] == e) or (mid%2==0 and nums[mid+1] == e):
                left = mid+1
            else:
                right = mid
        return nums[left]

        
