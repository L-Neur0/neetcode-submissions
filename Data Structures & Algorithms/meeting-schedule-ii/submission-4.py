"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # we need 2 arrays to differntiate
        starts = []
        ends = [] 
        res = count = 0 

        for i in range(len(intervals)):
            starts.append(intervals[i].start)
            ends.append(intervals[i].end)
        starts.sort()
        ends.sort()
        start, end = 0, 0 

        while start < len(intervals):
            if starts[start] < ends[end]: 
                count += 1 
                start += 1
            else: 
                count -= 1 
                end += 1 
            res = max(res, count)
        return res 



        
        