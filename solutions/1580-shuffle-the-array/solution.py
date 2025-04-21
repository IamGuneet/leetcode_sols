class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        temp = []
        for x in range(n):
            temp.append(nums[x])
            temp.append(nums[x+n])
        return temp

        
