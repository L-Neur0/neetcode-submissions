class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])

        cur = intervals[0]
        res = []

        for i in range(len(intervals)):
            if intervals[i][0] <= cur[1] and intervals[i][1] >= cur[0]:
                # they overlap
                cur[0] = min(cur[0], intervals[i][0])
                cur[1] = max(cur[1], intervals[i][1])
            else:
                res.append(cur)
                cur = intervals[i]

        res.append(cur)

        return res 