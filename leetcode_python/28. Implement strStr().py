class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle: return 0
        l_h, l_n = len(haystack), len(needle)
        for i in range(l_h + 1):
            for j in range(l_n + 1):
                if j == l_n: return i
                if i + j == l_h: return -1
                if haystack[i+j] != needle[j]: break

    def strStr1(self, haystack, needle):
        return haystack.find(needle)

s = Solution()
print(s.strStr1("aaaaa", ""))



# brute force O(MN)