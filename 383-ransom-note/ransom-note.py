class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        mg = {}
        rn = {}

        for char in magazine:
            if char not in mg:
                mg[char] = 1
            else:
                mg[char] += 1
        
        for char in ransomNote:
           if char not in rn:
               rn[char] = 1
           else:
               rn[char] += 1

        for char in ransomNote:
            if char in mg:
                mg[char] -= 1
                rn[char] -= 1
                if mg[char] < 1:
                    del mg[char]
            else:
                return False
        return True
