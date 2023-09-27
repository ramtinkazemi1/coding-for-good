class Solution:
    def romanToInt(self, s: str) -> int:
        ht = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        
        result = 0
        left = 0
        while left<len(s)-1:
            if ht[s[left]] < ht[s[left+1]]:
                result += ht[s[left+1]] - ht[s[left]] 
                left+=2
                
            else:
                result += ht[s[left]] 
                
                left+=1
                
        # If there's one character left to process (odd length), add its value
        if left == len(s) - 1:
            result += ht[s[left]]

        return result