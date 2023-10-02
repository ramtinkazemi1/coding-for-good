class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

      ht = {}

      for i in range(len(nums)):

        if target-nums[i] not in ht:
          ht[nums[i]] = i

        else:
          return [ht[target-nums[i]],i]
      
      return []