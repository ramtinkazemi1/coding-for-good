class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        
        prefix_sum = [0]
        
        for i in range(len(gain)):
            prefix_sum.append(prefix_sum[i]+gain[i])

        return max(prefix_sum)