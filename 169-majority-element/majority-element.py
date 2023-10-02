class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        x = len(nums)/2

        dic = {}

        for num in nums:
            if num not in dic:
                dic[num]=1
            else:
                dic[num]+=1
        
        
        for key,val in dic.items():
            if (val > x):
                return key
        
