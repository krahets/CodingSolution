class Solution:
    def intToRoman(self, num: int) -> str:
        res = ""
        values = [1000, 900, 500, 400,
                  100, 90, 50, 40,
                  10, 9, 5, 4,
                  1]
        symbols = ['M', 'CM', 'D', 'CD',
                   'C', 'XC', 'L', 'XL',
                   'X', 'IX', 'V', 'IV',
                   'I']
        i = 0
        while num > 0:
            count = num // values[i]
            res += "".join([symbols[i] for _ in range(count)])
            num -= count * values[i]
            i += 1
        return res
            
            


s = Solution()
print(s.intToRoman(1994))
