class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0": return "0"
        res = []
        for loc in range(len(num2)): # multiply
            x2 = ord(num2[len(num2) - 1 - loc]) - ord('0')
            ans, tmp, car = [], 0, 0
            for n1 in num1[::-1]:
                x1 = ord(n1) - ord('0')
                tmp = x1 * x2 + car
                car = tmp // 10
                ans.append(str(tmp % 10))
            if car: ans.append(str(car))
            ans.reverse()
            ans.extend(['0' for _ in range(loc)])
            i, j, car = len(res) - 1, len(ans) - 1, 0
            res_tmp = []
            while i >= 0 or j >= 0: # add
                a1 = ord(res[i]) - ord('0') if i >= 0 else 0
                a2 = ord(ans[j]) - ord('0') if j >= 0 else 0
                tmp = a1 + a2 + car
                car = tmp // 10
                res_tmp.append(str(tmp % 10))
                i, j = i - 1, j - 1
            if car: res_tmp.append("1")
            res_tmp.reverse()
            res = res_tmp
        return "".join(res)