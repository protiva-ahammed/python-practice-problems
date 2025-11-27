from typing import List


class Solution13:
    def evalRPN(self, tokens: List[str])->int:
        stack=[]
        for i in tokens:
             stack=[]
        for i in tokens:
            if i not in '+-/*':
                stack.append(int(i))
            else:
                t1,t2 = stack.pop(),stack.pop()
                if i == '+':
                    stack.append(t1+t2)
                elif i == '-':
                    stack.append(t2-t1)
                elif i =='/':
                    stack.append(int(t2/t1))
                elif i == '*':
                    stack.append(t1*t2)
        return stack[0]
    