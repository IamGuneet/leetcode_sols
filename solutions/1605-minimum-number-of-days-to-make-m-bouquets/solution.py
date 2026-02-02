class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m*k > len(bloomDay):
            return -1

        def isPossible(x):
            tot = 0
            count = 0
            for i in bloomDay:
                if i <= x:
                    count+=1
                    if count == k:
                        tot+=1
                        count = 0
                else:
                    count = 0
            return tot>=m


        low = min(bloomDay)
        high = max(bloomDay)
        
        while low<high:
            mid = (low+high)//2
            if isPossible(mid):
                high = mid
            else:
                low = mid+1

        return low

        
            
                


        
