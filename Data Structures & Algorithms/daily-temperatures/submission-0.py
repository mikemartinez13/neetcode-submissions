class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # The stack will be on monotonic nonincreasing order. 

        res = [0] * len(temperatures) # already initiliazed to be zeros
        stack = [] # pair of values, we'll also have the index [temp, index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = (i-stackInd)
            stack.append([t,i])
        return res