class Solution:
    def myAtoi(self, s: str) -> int:
        i, res, neg, over = 0, 0, False, (1 << 31) - 1
        while i < len(s) and s[i] == ' ': # ignore space first
            i += 1
        if i < len(s) and (s[i] == '-' or s[i] == '+'): # save '-'
            neg = s[i] == '-'
            i += 1
        while i < len(s) and '0' <= s[i] <= '9': # generate number
            res = res * 10 + int(s[i])
            i += 1
        if res > over: # handle the overflow
            res = over + 1 if neg else over
        return -res if neg else res


s = Solution()
print(s.myAtoi(" -3123123"))