class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum_arr = []
        for i in range(len(nums)):
            if i!=0:
                sum_arr.append(nums[i]+sum_arr[i-1])
            else:
                sum_arr.append(nums[i])
        return sum_arr
