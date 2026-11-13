class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # just expand the new interval when you have to merge and instead insert the new when to insert
        inserted = False
        res = []

        for i in range(len(intervals)):
            if intervals[i][1] < newInterval[0]: 
                res.append(intervals[i])
            elif intervals[i][0] > newInterval[1]:
                if not inserted: 
                    res.append(newInterval)
                    inserted = True 
                res.append(intervals[i])
            else: 
                # increase interval
                newInterval[0] = min(intervals[i][0], newInterval[0])
                newInterval[1] = max(intervals[i][1], newInterval[1])

        if not inserted:
            res.append(newInterval)

        return res

        