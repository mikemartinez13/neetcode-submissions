import operator
import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        operators = {'*':operator.mul,
                    '-': operator.sub,'/': operator.truediv,'+': operator.add}

        for t in tokens: 
            # print(stack)
            if t not in operators: 
                stack.append(t)
            else:
                r = int(stack.pop())
                l = int(stack.pop())
                res = int(operators[t](l,r))
                
                stack.append(res)

        return int(stack.pop())
