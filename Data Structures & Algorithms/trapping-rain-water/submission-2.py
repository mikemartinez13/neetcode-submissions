class Solution:
    def trap(self, height: List[int]) -> int:
        maxL = [0] * len(height)
        maxR = [0] * len(height)

        # build maxleft and maxright arrays
        
        for i in range(1,len(height)):
            maxL[i] = max(maxL[i-1], height[i-1])

        for j in range(len(height)-2, -1, -1):
            maxR[j] = max(maxR[j+1], height[j+1])

        # print(maxL)
        # print(maxR)

        rainwater = [0] * len(height)
        for k in range(len(height)):
            water = min(maxL[k], maxR[k]) - height[k]
            rainwater[k] = water if water > 0 else 0

        return sum(rainwater)
