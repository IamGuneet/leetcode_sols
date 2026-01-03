class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen = {0:1}
        cur_sum = 0
        answer = 0

        for num in nums:
            cur_sum+=num

            if cur_sum-k in seen:
                answer+=seen[cur_sum-k]
            seen[cur_sum] = seen.get(cur_sum,0)+1
        return answer
