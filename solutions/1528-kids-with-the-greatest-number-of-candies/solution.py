class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        larges = max(candies)
        for x in range(len(candies)):
            if candies[x] + extraCandies >= larges:
                candies[x] = True
            else:
                candies[x] = False
        return candies

