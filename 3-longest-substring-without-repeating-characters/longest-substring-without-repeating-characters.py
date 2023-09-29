class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
            
        pocket= set()

        left = 0
        length = 0

        for right in range(len(s)):
            while s[right] in pocket:
                pocket.remove(s[left])
                left += 1
 
            pocket.add(s[right])
            length = max(length, right-left+1)

        return length
