class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        dic = {}
        i, dist, res = 0, 0, 0
        for j in range(len(s)):
            if s[j] in dic and dic[s[j]]:
                dic[s[j]] += 1
            else:
                dic[s[j]] = 1
                dist += 1
            while dist > 2:
                dic[s[i]] -= 1
                if not dic[s[i]]: dist -= 1
                i += 1
            res = max(res, j - i + 1)
        return res

s = Solution()
print(s.lengthOfLongestSubstringTwoDistinct("eceeba"))
            