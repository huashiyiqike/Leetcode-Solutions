import java.util.*;
/**
 * Definition for an interval.
 * public class Interval {
 *     int start;
 *     int end;
 *     Interval() { start = 0; end = 0; }
 *     Interval(int s, int e) { start = s; end = e; }
 * }
 */
/**
 * Definition for an interval.
 * public class Interval {
 *     int start;
 *     int end;
 *     Interval() { start = 0; end = 0; }
 *     Interval(int s, int e) { start = s; end = e; }
 * }
 */
public class Solution {
    public List<Interval> merge(List<Interval> intervals) {
        if(intervals.size() <= 1) return intervals;
        Comparator<Interval> comparator = new Comparator<Interval>() {
            @Override
            public int compare(Interval o1, Interval o2) {
                if(o1.start < o2.start) return -1;
                else if (o1.start > o2.start) return 1;
                else{
                    if(o1.end < o2.end) return -1;
                    else if(o1.end > o2.end) return 1;
                }
                return 0;
            }
        };
        Collections.sort(intervals, comparator);
        List<Interval> res = new ArrayList<>();// intervals.get(0);
        res.add(intervals.get(0));
        Collections.sort(intervals, comparator);
        for(int i = 1; i < intervals.size();i++){
            if(intervals.get(i).start > res.get(res.size()-1).end) res.add(intervals.get(i));
            else res.get(res.size()-1).end = Math.max(intervals.get(i).end, res.get(res.size()-1).end);
        }
        return res;
    }
}
public class Solution {
    public List<Interval> merge(List<Interval> intervals) {
        
        ArrayList<Interval> rt = new  ArrayList<Interval>();
        
        Collections.sort(intervals, new Comparator<Interval>() {
            public int compare(Interval o1, Interval o2) {
                return o1.start - o2.start;
            }
        });

        LinkedList<Interval> s = new LinkedList<Interval>(intervals);

        while (s.size() > 1) {
            Interval i1 = s.pop();
            Interval i2 = s.pop();

            if (i1.end >= i2.start) {
                s.push(new Interval(i1.start, Math.max(i1.end, i2.end)));
            } else {
                s.push(i2);
                rt.add(i1);
            }
        }
        
        rt.addAll(s);
        
        return rt;
    }
}
