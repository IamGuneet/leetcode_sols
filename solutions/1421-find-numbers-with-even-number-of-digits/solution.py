class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        total = 0
        for i in nums:
            if i ==0:
                total+=1
            else:
                count = 0
                temp = i
                while temp>0:
                    count +=1
                    temp = temp//10
            if count%2 == 0:
                total+=1
        return total
        
