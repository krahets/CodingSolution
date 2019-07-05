class Solution:
    def isValid(self, s: str) -> bool:
        dic = {'{': '}',  '[': ']', '(': ')'}
        if s and s[0] not in dic: return False
        stack = []
        for c in s:
            if not stack or c in dic: stack.append(c)
            elif stack[-1] in dic and dic[stack[-1]] == c: stack.pop()
            else: return False  
        return not stack