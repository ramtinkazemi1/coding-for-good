class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        if sum(nums)<target: return 0
        
        left = curr = 0

        #important
        ans = len(nums)
        
        for right in range(len(nums)):

            curr += nums[right]
            while curr >= target:    #pay attn to the condition
                curr -= nums[left]
                ans = min(ans, right - left + 1)
                left += 1
        
        return ans