class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = [0]
        for i in range(n):
            head = 1 << i
            for j in range(len(res) - 1, -1, -1):
                res.append(head + res[j])
        return res