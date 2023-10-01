class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        
        if (len(nums) < 2*k+1):
            return [-1]*len(nums)
        
        
        prefix = [nums[0]]
        
        for i in range(1,len(nums)):
            prefix.append(prefix[i-1]+nums[i])
            
        print(prefix)
            
        ans = []
        
        
        for i in range(len(nums)):
            ans.append(-1)
            
        for i in range(k,len(nums)-k):
            if i == k:
                ans[i] = (prefix[k*2]//(2*k+1))
            else:
                ans[i] = ( (prefix[k*2+i-k] - prefix[i-k-1]) //(2*k+1) )
        
        return ans