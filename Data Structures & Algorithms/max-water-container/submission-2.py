class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1

        maxwater = 0
        while l < r:
            maxwater = max(min(heights[l], heights[r]) * (r-l), maxwater)
            # print("max:",maxwater, "left height:",heights[l], "right height:", heights[r], "width:", (r-l))
            if heights[l] <= heights[r]:
                l+=1
            else:
                r-=1

        return maxwater

