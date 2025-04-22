class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        net_gain = [0]
        for x in range(len(gain)):
            net_gain.append(net_gain[x]+gain[x])
        return max(net_gain)
