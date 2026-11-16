import math

class MinStack:

    def __init__(self):
        self.__stack = []
        self.__stack_min_dp = [math.inf]
        # print(self.__stack)
        # print(self.__stack_min_dp,'\n')

    def push(self, val: int) -> None:
        self.__stack_min_dp.append(min(self.__stack_min_dp[-1], val))
        self.__stack.append(val)
        # print(self.__stack)
        # print(self.__stack_min_dp,'\n')

    def pop(self) -> None:
        self.__stack.pop()
        self.__stack_min_dp.pop()
        # print(self.__stack)
        # print(self.__stack_min_dp,'\n')

    def top(self) -> int:
        # print(self.__stack)
        # print(self.__stack_min_dp,'\n')
        return self.__stack[-1]

    def getMin(self) -> int:
        # print(self.__stack)
        # print(self.__stack_min_dp,'\n')
        return self.__stack_min_dp[-1]
        
