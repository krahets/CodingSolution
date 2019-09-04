class Solution:
    def letterCombinations(self, digits: str) -> [str]:
        res = []
        dic = {
            '1': '', '2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']
        }
        def dfs(digits, tmp):
            if not digits:
                if tmp: res.append(tmp[:])
                return
            for let in dic[digits[0]]:
                tmp += let
                dfs(digits[1:], tmp)
                tmp = tmp[:-1]
        dfs(digits, "")
        return res


# no leetcode solution