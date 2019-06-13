class Solution:
    # two pointers
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        l, r = 0, len(s)-1
        while l < r:
            if s[l] != s[r]: return False
            l += 1
            r -= 1
        return True

    # half-reverse
    def isPalindrome1(self, x: int) -> bool:
        r = 0
        if 0 <= x < 10: return True
        if x < 0 or x % 10 == 0: return False
        while x > r:
            x, rem = x // 10, x % 10
            r = r * 10 + rem
        return x == r or x == r // 10

s = Solution()
print(s.isPalindrome1(3001))
