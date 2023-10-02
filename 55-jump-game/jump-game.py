class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        farthest = 0 

        for i in range(len(nums)):
            if i > farthest:
                return False  # If the current position is unreachable, return False
            farthest = max(farthest, i + nums[i])  # Update the farthest reachable position

        return farthest >= len(nums) - 1
