"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # in other words, what is the maximum number of overlapping rooms at any given time? 
        # maintain a number called count, which tells you, at any given time, what is the number of concurrent meetings? 
        # put all start times in a separate array
        # also put all end times in a separate, sorted array
        # use two pointers, start and end, one that goes through start array and one that goes through end array
        # take mins to determine when a meeting is starting or ending

        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        res, count = 0, 0
        s, e = 0, 0

        while s < len(intervals):
            if start[s] < end[e]:
                s+=1
                count +=1 # additional meeting going on
            else: # start and end times are the same or less
                e +=1
                count -=1
            res = max(res, count)
        
        return res
