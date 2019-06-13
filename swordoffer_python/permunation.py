# -*- coding:utf-8 -*-
class Solution:
    def Permutation(self, ss):
        # write code here
        self.res, self.sort = [], list(ss)
        self.sort_dic(0, len(ss))
        self.res.sort()
        return self.res
    def sort_dic(self, s, e):
        if e - s == 1:
            self.res.append(''.join(self.sort))
        same = []
        for i in range(s, e):
            if self.sort[i] not in same:
                same.append(self.sort[i])
                self.sort[s], self.sort[i] = self.sort[i], self.sort[s]
                self.sort_dic(s+1, e)
                self.sort[s], self.sort[i] = self.sort[i], self.sort[s]


s = Solution()
print(s.Permutation("abc"))
