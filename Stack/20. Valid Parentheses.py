class Solution:
    def isValid(self, s):
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in mapping:
                if not stack:
                    return False
                top = stack.pop()
                if mapping[char] != top:
                    return False
            else:
                stack.append(char)

        return len(stack) == 0


s = Solution()
print(s.isValid("()"))      
print(s.isValid("()[]{}"))  
print(s.isValid("(]"))      
print(s.isValid("([])"))    
print(s.isValid("([)]"))    
