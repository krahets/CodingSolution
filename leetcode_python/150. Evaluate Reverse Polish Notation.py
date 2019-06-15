class Solution:
    def evalRPN(self, tokens: [str]) -> int:
        symbol = ['+', '-', '*', '/']
        stack = []
        for t in tokens:
            if t in symbol:
                stack.append(self.eval(stack.pop(-2), stack.pop(), t))
            else:
                stack.append(int(t))
        return stack[-1]


    def eval(self, x, y, symbol):
        if symbol == '+': return x + y
        if symbol == '-': return x - y
        if symbol == '*': return x * y
        if symbol == '/': return int(x / y)


s = Solution()
s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])