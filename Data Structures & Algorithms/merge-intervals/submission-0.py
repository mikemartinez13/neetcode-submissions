class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[1])
        #print(intervals)
        intervals.sort(key=lambda x: x[0])
        #print(intervals)

        last_merged = intervals[0]
        res = [last_merged]

        for i in range(1,len(intervals)):
            # they DO NOT overlap if: 
            #print("last merged: ", last_merged)
            if last_merged[1] < intervals[i][0]:
                res.append(intervals[i])
                last_merged = intervals[i]
            else:
                new = [min(last_merged[0], intervals[i][0]), max(last_merged[1], intervals[i][1])]
                res[-1] = new
                last_merged = new
            #print(res)


        return res