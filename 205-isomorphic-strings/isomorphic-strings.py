class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        ss = {}
        tt = {}
            
        for char_s, char_t in zip(s, t): #compare characters from s and t one by one to check if they form an isomorphic relationship
            if char_s not in ss and char_t not in tt:
                ss[char_s] = char_t
                tt[char_t] = char_s
            elif ss.get(char_s) != char_t or tt.get(char_t) != char_s:
                return False

        return True