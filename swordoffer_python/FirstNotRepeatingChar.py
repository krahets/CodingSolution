# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s): 
        # write code here 65 - 122
        counts = [0 for _ in range(ord('z') - ord('A') + 1)]
        for i in range(len(s)):
            counts[self.H(ord(s[i]))] += 1
        for i in range(len(s)):
            if counts[self.H(ord(s[i]))] == 1:
                return i
        return -1
    def H(self, val):
        return val - 65

s = Solution()
print(s.FirstNotRepeatingChar("NXWtnzyoHoBhUJaPauJaAitLWNMlkKwDYbbigdMMaYfkVPhGZcrEwp"))
