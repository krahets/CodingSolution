class Solution:
    def generateParenthesis(self, n: int) -> [str]:
        res = []
        def dfs(i, j, tmp):
            if not (i or j):
                res.append(tmp)
                return
            if i:
                dfs(i - 1, j, tmp + '(')
            if j > i:
                dfs(i, j - 1, tmp + ')')
        dfs(n, n, "")
        return res




   
