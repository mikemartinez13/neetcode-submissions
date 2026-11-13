class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1

        #given heights[l], heights[r]
        # formula is area = min(heights[l], heights[r]) * (r - l)

        # for i in range(len(heights)):
        #     for j in range(len(heights)):
        #         print(min(heights[i], heights[j]) * abs(i-j))

        maxwater = 0
        while l < r:
            curwater = min(heights[l], heights[r]) * (r-l)
            maxwater = max(curwater, maxwater)
            # print("max:",maxwater, "left height:",heights[l], "right height:", heights[r], "width:", (r-l))
            if heights[l] <= heights[r]:
                l+=1
            else:
                r-=1


        return maxwater

