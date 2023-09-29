class Solution:
    def isPalindrome(self, s: str) -> bool:

        #remember this one line of code!!!
        s_new = re.sub("[^a-z0-9]", "", s.lower())
        left = 0
        right = len(s_new)-1

        while left<=right:
            if s_new[left] != s_new[right]:
                return False
            left+=1
            right-=1
        
        return True
