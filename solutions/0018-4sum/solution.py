class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        op = set()

        for i in range(n):
            for j in range(i+1,n):
                seen = set()
                for k in range(j+1,n):
                    req = target - (nums[i]+nums[j]+nums[k])
                    if req in seen:
                        tup = tuple(sorted([nums[i],nums[j],nums[k],req]))
                        op.add(tup)
                    seen.add(nums[k])
        return [list(quad) for quad in op]
        
