class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def hourCheck(k):
            cur_sum = 0
            for pile in piles:
                cur_sum += math.ceil(pile/k)
                if cur_sum > h:
                    return False
            return True
        
        low,high = 1, max(piles)
        ans = max(piles)
        while(low<=high):
            mid = (low+high)//2
            if hourCheck(mid) :
                ans = mid
                high = mid-1
            else:
                low = mid+1
        return ans

        
