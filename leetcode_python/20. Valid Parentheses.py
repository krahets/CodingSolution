class Solution:
    def isValid(self, s: str) -> bool:
        dic = {'{': '}',  '[': ']', '(': ')'}
        stack = []
        for i in range(len(s)):
            if stack and stack[-1] in dic.keys() and s[i] == dic[stack[-1]]:
                stack.pop()
            else:
                stack.append(s[i])
        return not stack

s = Solution()
print(s.isValid("[(])"))
