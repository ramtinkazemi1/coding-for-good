class Solution:
    def isValid(self, s: str) -> bool:
        matching_bracket = {')': '(', '}': '{', ']': '['}
        stack = []
        
        for char in s:
            if char in matching_bracket:  
                if stack and stack[-1] == matching_bracket[char]:
                    stack.pop()  
                else:
                    return False 
            else:
                stack.append(char) 
                
        return len(stack) == 0