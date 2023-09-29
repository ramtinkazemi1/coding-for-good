class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()   #nums = nums.sort() did not work!
        ans = []

        for i in range(len(nums) - 2):
            
            if nums[i] > 0: #if our first element after sorting is greater than 0!
                break
                
            if i > 0 and nums[i] == nums[i-1]: #to avoid duplicate triplets
                continue

            left = i + 1
            right = len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    triplet = [nums[i], nums[left], nums[right]]
                    ans.append(triplet)
                    while left < right and nums[left] == triplet[1]:
                        left += 1
                    while left < right and nums[right] == triplet[2]:
                        right -= 1
        return ans