class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        _min = nums[0]
        while(left<=right):
            mid = (left+right)//2
            e = nums[mid]
            _min = min(e,_min)
            if (e>nums[right]):
                left = mid+1
            else:
                right = mid-1
        return _min

