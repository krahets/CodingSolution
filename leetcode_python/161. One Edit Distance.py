class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        i, dif = 0, len(t) - len(s)
        if dif < 0: s, t, dif = t, s, -dif
        if dif > 1: return False
        while i < len(s) and s[i] == t[i]: i += 1
        if i == len(s): return bool(dif)
        if not dif: i += 1
        while i < len(s) and s[i] == t[i + dif]: i += 1
        return i == len(s)

s = Solution()
print(s.isOneEditDistance("acb","abc"))
