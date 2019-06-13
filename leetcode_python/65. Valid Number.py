import re

class Solution:
    def isNumber(self, s: str) -> bool:
        # 前后空格
        # 以e为分界线，前面可以有小数点，后面不可以有，前后两部分都可以有正负号
        s = s.strip(' ')
        if not s: return False
        i = 0
        length = len(s)
        while i < length and s[i] != 'e': i += 1
        if i in [0, length - 1]: return False
        i, end = 0, i
        if i < end and s[i] in ['+', '-']: i += 1
        while i < end:
            if s[i] == '.':
                i += 1
                break
            if not '0' <= s[i] <= '9': break
            i += 1
        if (i >= end or not '0' <= s[i] <= '9') and (i < 2 or not '0' <= s[i-2] <= '9') and s[i-1] == '.':
            return False
        while i < end and '0' <= s[i] <= '9': i += 1
        if i != end: return False
        if i == length: return True
        i += 1
        if i < length and s[i] in ['+', '-']: i += 1
        while i < length and '0' <= s[i] <= '9': i += 1
        if i != length: return False
        return True

    def isNumber1(self, s: str) -> bool:
        return not not re.findall(re.compile(r'^[\+\-]?(\d+\.\d+|\.\d+|\d+\.|\d+)(e[\+\-]?\d+)?$'), s.strip())


s = Solution()
print(s.isNumber1("4.ee2"))
