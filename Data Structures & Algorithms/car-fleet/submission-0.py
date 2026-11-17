class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # go from right to left, because we need to be sure the first one doesn't collide with any in front of it. 

        pair = [[p,s] for p,s in zip(position, speed)]
        pair.sort(key=lambda x: x[0], reverse=True)

        stack = []
        for p, s in pair: # reverse sorted order
            stack.append((target - p)/ s) # append time to stack
            if len(stack) >= 2 and stack[-1] <= stack[-2]: # does it overlap? 
                stack.pop() 
        
        return len(stack)