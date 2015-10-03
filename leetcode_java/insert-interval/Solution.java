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
public class Solution {
    public List<Interval> insert(List<Interval> intervals, Interval newInterval) {
        int index = 0;
        if(intervals.size() == 0){
            intervals.add(newInterval);
            return  intervals;
        }

        while(index < intervals.size()){
            Interval tmp = intervals.get(index);
            if(tmp.start >= newInterval.start){
                intervals.add(index, newInterval);
                break;
            }
            index++;
        }
        if(newInterval.start > intervals.get(intervals.size()-1).start){
            intervals.add(newInterval);
        }
        Interval pre = intervals.get(0);
        index = 1;
        while(index < intervals.size()){
            Interval tmp = intervals.get(index);
            if(pre.end >= tmp.start){
                if(pre.end < tmp.end){
                    pre.end = tmp.end;
                }
                intervals.remove(index);
            }
            else{
                pre = tmp;
                index++;
            }
        }
        return intervals;
    }
}

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
    public List<Interval> insert(List<Interval> intervals, Interval newInterval) {

        int pos = intervals.size();

        for(int i = 0; i < intervals.size(); i++){
            if(newInterval.start <= intervals.get(i).start){
                pos = i;
                break;
            }
        }
        
        intervals.add(pos, newInterval);

        
        ArrayList<Interval> rt = new  ArrayList<Interval>();

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
