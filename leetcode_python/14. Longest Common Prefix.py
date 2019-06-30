class Solution:
    def longestCommonPrefix(self, strs: [str]) -> str:
        if not strs: return ""
        mi = len(strs[0])
        for s in strs[1:]: mi = min(mi, len(s))
        for i in range(mi):
            for j in range(len(strs) - 1):
                if strs[j][i] != strs[j + 1][i]:
                    return strs[j][:i]
        return strs[0][:i+1] if mi else ""


s = Solution()
print(s.longestCommonPrefix(["aaa", "aaa"]))
