class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        l, res = 0, 0
        for r in range(len(s)):
            if s[r] in dic:
                l = max(dic[s[r]], l)
            dic[s[r]] = r + 1
            res = max(res, r - l + 1)
        return res


s = Solution()
print(s.lengthOfLongestSubstring("tmmzuxt"))
