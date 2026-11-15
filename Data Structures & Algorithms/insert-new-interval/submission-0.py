class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval) # then, the other intervals will be nonoverlapping
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i]) 
            # if new interval was not overlapping, then it must be overlapping. So we must merge. 
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])] 
                # the "newInterval" is set to this now merged new interval, and then it goes back as a check 
                # to make sure that it is not overlapping with additional intervals coming up. 

        res.append(newInterval)
        return res
