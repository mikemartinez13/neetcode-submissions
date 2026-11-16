class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])

        #print(intervals)
        # sort the intervals, JIC

        # greedy approach - iterate through the intervals in sorted roder, and always remove the one with the largest spread of the interval
        last_checked = intervals[0]
        count = 0

        for i in range(1,len(intervals)):
            #print("last:", last_checked, "interval:", intervals[i])
            if intervals[i][0] >= last_checked[1]:
                last_checked = intervals[i]
            else:
                count +=1 
                last_checked = min(intervals[i], last_checked, key=lambda x: x[1])
        
        return count

