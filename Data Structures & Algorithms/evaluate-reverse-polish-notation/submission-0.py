import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        ops = {
            '+' : operator.add,
            '-' : operator.sub,
            '*' : operator.mul,
            '/' : operator.truediv,
        }

        stack = []
        left, right = 0, 0

        for token in tokens:
            if token in ops:
                right = stack.pop()
                left = stack.pop()
                result = ops[token](left, right)

                if token == '/':
                    result = int(result)
                    
                stack.append(result)
            else:
                i = int(token)
                stack.append(i)
        
        return stack.pop()

