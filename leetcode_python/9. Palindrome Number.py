class Solution:
    # half-reverse
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        ori, rev = x, 0
        while ori:
            rev = rev * 10 + ori % 10
            ori //= 10
        return ori == rev


s = Solution()
print(s.isPalindrome(3001))
