# -*- coding:utf-8 -*-
class Solution:
    def LeftRotateString(self, s, n):
        # write code here
        res, length = list(s), len(s)
        for i in range(int(n/2)):
            res[i], res[n-1-i] = res[n-1-i], res[i]
        for i in range(n, int((n+length)/2)):
            res[i], res[length-1-i+n] = res[length-1-i+n], res[i]
        for i in range(int(length/2)):
            res[i], res[length-1-i] = res[length-1-i], res[i]
        return "".join(res)


s = Solution()
print(s.LeftRotateString("abcXYZdef", 3))
