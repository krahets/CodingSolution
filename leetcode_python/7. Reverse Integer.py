class Solution:
    def reverse(self, x: int) -> int:
        y, res = abs(x), 0
        of = 1 << 31 if x > 0 else (1 << 31) - 1
        while y != 0:
            res = res * 10 + y % 10
            if res > of: return 0
            y //= 10
        return res if x > 0 else -res


s = Solution()
print(s.reverse(-12321321312313))

print(1 << 31)