class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)

        def isFeasible(x):
            day = 1
            total = 0
            for weight in weights:
                total+=weight
                if total>x:
                    total = weight
                    day+=1
                    if day>days:
                        return False
            return True
        
        while low <= high:
            mid = (low+high)//2
            if isFeasible(mid):
                high = mid-1
            else:
                low = mid+1
        return low
