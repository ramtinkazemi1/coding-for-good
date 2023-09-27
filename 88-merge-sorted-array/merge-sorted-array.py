class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #must use [:] to do it IN PLACE""
        nums1[:] = sorted(nums1[:m] + nums2)
