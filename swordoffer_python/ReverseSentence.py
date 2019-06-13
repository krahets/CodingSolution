# -*- coding:utf-8 -*-
class Solution:
    def ReverseSentence(self, s):
        # write code here
        res, length, last = list(s), len(s), -1
        for i in range(len(res)):
            if res[i] == ' ': 
                self.reverse(res, last + 1, i)
                last = i
        self.reverse(res, 0, length)
        return "".join(res)

    def reverse(self, res, l, r):
        while l < r:
            res[l], res[r-1] = res[r-1], res[l]
            l += 1
            r -= 1

    def ReverseSentence1(self, s):
        return " ".join(s.split(" ")[::-1])
s = Solution()
print(s.ReverseSentence("student. a am I"))
print(s.ReverseSentence1("student. a am I"))
