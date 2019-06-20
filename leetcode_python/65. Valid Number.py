import re


class Solution:
    def isNumber(self, s: str) -> bool:
        states = [
            { 'b': 0, 's': 1, 'd': 2, '.': 4 }, # 0. start
            { 'd': 2, '.': 4 } ,                # 1. 'sign' before 'e'
            { 'd': 2, '.': 3, 'e': 5, 'b': 8 }, # 2. 'digit' before 'dot'
            { 'd': 3, 'e': 5, 'b': 8 },         # 3. 'dot' with 'digit'
            { 'd': 3 },                         # 4. no 'digit' before 'dot'
            { 's': 6, 'd': 7 },                 # 5. 'e'
            { 'd': 7 },                         # 6. 'sign' after 'e'
            { 'd': 7, 'b': 8 },                 # 7. 'digit' after 'e'
            { 'b': 8 }                          # 8. end with
        ]
        p = 0
        for c in s:
            if '0' <= c <= '9': typ = 'd'
            elif c == ' ': typ = 'b'
            elif c == '.': typ = '.'
            elif c == 'e': typ = 'e'
            elif c in "+-": typ = 's'
            else: typ = '?'
            if typ not in states[p]: return False
            p = states[p][typ]
        return p in [2, 3, 7, 8]

    def isNumber1(self, s: str) -> bool:
        return not not re.findall(re.compile(r'^[\+\-]?(\d+\.\d+|\.\d+|\d+\.|\d+)(e[\+\-]?\d+)?$'), s.strip())


s = Solution()
print(s.isNumber("2e0"))
print(s.isNumber("1 5"))
print(s.isNumber("2e0"))
print(s.isNumber("+3e-2"))
print(s.isNumber("+3.2e-2"))
print(s.isNumber("+3.2e-2.2"))
print(s.isNumber("."))
print(s.isNumber("e"))
