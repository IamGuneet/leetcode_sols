class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # sign_change = 0
        pos = []
        neg = []
        op = []
        for num in nums:
            if num<0:
                neg.append(num)
            else: 
                pos.append(num)
        p = n = 0
        for i in range(len(nums)):
            if i%2 == 0:
                op.append(pos[p])
                p+=1
            else:
                op.append(neg[n])
                n+=1
        return op


                
        
