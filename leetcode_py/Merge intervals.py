# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param {Interval[]} intervals
    # @return {Interval[]}
    def merge(self, intervals):
        if not intervals:
            return intervals
        intervals.sort(key=lambda x: x.start)
        res = [intervals[0]]
        for i in intervals[1:]:
            if i.start <= res[-1].end:
                res[-1].end = max(res[-1].end, i.end)
            else:
                res.append(i)
        return res


class Solution:
    # @param intervals, a list of Interval
    # @return a list of Interval
    def merge(self, intervals):
        intervals = sorted(intervals, key=lambda s: s.start)
        idx = 0
        res = []
        while idx < len(intervals):
            cur = intervals[idx]
            while idx+1 < len(intervals):
                if intervals[idx+1].start <= cur.end:
                    if intervals[idx+1].end > cur.end:
                        cur.end = intervals[idx+1].end
                    idx += 1
                else:
                    break
            res.append(cur)
            idx += 1
        return res