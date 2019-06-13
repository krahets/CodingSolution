class Solution:
    def reverseWords(self, s: str) -> str:
        l = []
        i, left, right = 0, 0, -2
        while i < len(s) + 1:
            if i == len(s) or s[i] == ' ':
                left, right = right + 1, i - 1
                for j in range(right, left, -1):
                    l.append(s[j])
                l.append(' ')
            i += 1
        return "".join(l[:-1])

    def reverseWords1(self, s: str) -> str:
        return ' '.join(i[::-1] for i in s.split())

s = Solution()
print(s.reverseWords1("I abcm a botmy"))
