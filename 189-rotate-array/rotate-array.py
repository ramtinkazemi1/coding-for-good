class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        this rotates the array to the LEFT! not right.
        nums[:] = nums[k+1:] + nums[:k+1]
        """
        k = k % len(nums)  # Calculate the rotation steps
        nums[:] = nums[-k:] + nums[:-k]