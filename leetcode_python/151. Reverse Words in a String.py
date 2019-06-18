class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        res = ""
        i, j = len(s) - 1, len(s)
        while i > 0:
            if s[i] == ' ':
                res += s[i + 1: j] + ' '
                while s[i] == ' ': i -= 1
                j = i + 1
            i -= 1
        return res + s[:j]

    def reverseWords1(self, s: str) -> str:
        return " ".join(s.split()[::-1])
            


s = Solution()
print(s.reverseWords("I am a    boy"))
