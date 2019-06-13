# -*- coding:utf-8 -*-
class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here
        ls, i, dot = len(s), 1, 0
        # 首位必须为“+/-/number”
        if s[0] != '+' and s[0] != '-' and (s[0] < '0' or s[0] > '9'): return False
        # 遍历1~(len-1)位，如果发现E or e就跳到下一个while
        while i < ls - 1:
            if s[i] == 'E' or s[i] == 'e':
                i += 1
                break
            elif s[i] == '.':
                if dot: return False
                dot += 1
            elif s[i] < '0' or s[i] > '9': return False
            i += 1
        # e后面首位必须为“+/-/number”
        if s[i] != '+' and s[i] != '-' and (s[i] < '0' or s[i] > '9'): return False
        i += 1
        # e不能出现两次，并且e后面的数字组合不能有小数点，其余和前面一样
        while i < ls:
            if s[i] < '0' or s[i] > '9': return False
            i += 1
        return True


s = Solution()
print(s.isNumeric("+500"))
