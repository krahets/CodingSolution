# -*- coding:utf-8 -*-
class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        # write code here
        return self.match_str(s, pattern, 0, 0)

    def match_str(self, s, p, i, j):
        ls, lp = len(s), len(p)
        if not j < lp:
            if not i < ls: return True
            return False
        if j+1 < lp and p[j+1] == '*':
            if i < ls and (s[i] == p[j] or p[j] == '.'):
                return self.match_str(s, p, i+1, j) or self.match_str(s, p, i, j+2)
            return self.match_str(s, p, i, j+2)
        if i < ls and (s[i] == p[j] or p[j] == '.'):
            return self.match_str(s, p, i+1, j+1)


s = Solution()
print(s.match("bcbbabab",".*a*a"))
