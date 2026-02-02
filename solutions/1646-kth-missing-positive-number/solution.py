class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        low = 0
        high = len(arr)
        while low < high:
            mid = (low+high)//2

            if arr[mid] - (mid+1) >=k:
                high = mid
            else:
                low = mid+1
        return low+k
        
