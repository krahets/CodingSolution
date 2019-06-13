class Solution:
    def longestPalindrome(self, s: str) -> str:
        left, right = 0, 0
        for i in range(len(s)):
            odd = self.mid_expand(s, i, i)
            even = self.mid_expand(s, i, i+1)
            m = max(odd, even)
            if m > right - left:
                left = i - (m - 1) // 2
                right = i + m // 2
        return s[left:right+1]

    def mid_expand(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1
