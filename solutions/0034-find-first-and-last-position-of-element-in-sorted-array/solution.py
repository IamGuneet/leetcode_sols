class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def first():
            left = 0
            right = len(nums)-1
            ans = -1
            while(left<=right):
                idx = right - (right-left)//2
                mid = nums[idx]
                if (mid == target):
                    ans = idx
                    right = idx-1
                elif target>mid:
                    left = idx+1
                else:
                    right= idx-1
            return ans
        
        def last():
            left = 0
            right = len(nums)-1
            ans = -1
            while(left<=right):
                idx = right - (right-left)//2
                mid = nums[idx]
                if (mid == target):
                    ans = idx
                    left = idx+1
                elif target>mid:
                    left = idx+1
                else:
                    right= idx-1
            return ans

        return [first(),last()]

                
        
