# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    # @param {Interval[]} intervals
    # @param {Interval} newInterval
    # @return {Interval[]}
    def insert(self, intervals, newInterval):
        if not intervals:
            return [newInterval]
        # intervals.append(newInterval)
        # intervals.sort(key=lambda x:x.start)
        for idx, item in enumerate(intervals):
            if item.start >= newInterval.start:
                intervals.insert(idx, newInterval)
                break
        if newInterval.start > intervals[-1].start:
            intervals.append(newInterval)

        res = [intervals[0]]
        for i in intervals:
            if i.start <= res[-1].end:
                res[-1].end = max(res[-1].end, i.end)
            else:
                res.append(i)
        return res


class Solution:
    # @param {Interval[]} intervals
    # @param {Interval} newInterval
    # @return {Interval[]}
    def insert(self, intervals, newInterval):
        if not intervals:
            return [newInterval]
        for idx, item in enumerate(intervals):
            if newInterval.start <= intervals[idx].start:
                intervals.insert(idx, newInterval)
                break
        if newInterval.start > intervals[-1].start:
            intervals.append(newInterval)
        res = []
        cur = intervals[0]
        for i in intervals[1:]:
            if i.start <= cur.end:
                if i.end > cur.end:
                    cur.end = i.end
            else:
                res.append(cur)
                cur = i
        res.append(cur)
        return res
