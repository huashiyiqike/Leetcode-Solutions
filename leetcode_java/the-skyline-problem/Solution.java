

import java.lang.Integer;
import java.lang.Override;
import java.util.*; 

public class Solution {
    public List<int[]> getSkyline(int[][] buildings) {
        List<int[]> list = new ArrayList<int[]>();
        if(buildings == null || buildings.length == 0){
            return list;
        }
        List<int[]> height = new ArrayList<int[]>();
        int len = buildings.length;
        
        for(int i = 0;i < len ; i++){
            height.add(new int[]{buildings[i][0],-buildings[i][2]});
            height.add(new int[]{buildings[i][1],buildings[i][2]});
        }
        
        Collections.sort(height,new Comparator<int[]>(){  
            @Override  
            public int compare(int[] a, int[] b) {  
                if(a[0] == b[0]){
                    return a[1] - b[1];
                }
                return a[0] - b[0];
            }  
       });
       Queue<Integer> queue = new PriorityQueue<>((a, b) -> (b - a));
       queue.offer(0);
       int pre = 0;
       int heightSize = height.size();
       for(int hei[] : height ){
           if(hei[1] < 0){
               queue.offer(-hei[1]);
           }else{
               queue.remove(hei[1]);
           }
           int cur = queue.peek();
           if(pre != cur){
               list.add(new int[]{hei[0],cur});
               pre = cur;
           }
       }
       return list;
    }
}

public class Solution {
    public List<int[]> getSkyline(int[][] buildings) {
        PriorityQueue<int[]> queue = new PriorityQueue<int[]>(new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                return o2[0] - o1[0];
            }
        });
        List<int[]> res = new LinkedList<>();
        int i = 0;
        int furthest;
        Arrays.sort(buildings, new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                return o1[0] - o2[0];
            }
        });
        while (!queue.isEmpty() || i < buildings.length) {
            if (queue.isEmpty() || (i < buildings.length
                    && buildings[i][0] <= queue.peek()[1])) {
                furthest = buildings[i][0];
                while (i < buildings.length && buildings[i][0] <= furthest) {
                    queue.offer(new int[]{buildings[i][2], buildings[i][1]});
                    i++;
                }
            } else {
                furthest = queue.peek()[1];
                while (!queue.isEmpty() && queue.peek()[1] <= furthest) {
                    queue.poll();
                }
            }
            int height = queue.isEmpty() ? 0 : queue.peek()[0];
            if (res.isEmpty() || height != res.get(res.size() - 1)[1]) {
                res.add(new int[]{furthest, height});
            }
        }
        return res;
    }
}

public class Solution {
    public List<int[]> merge(List<int[]> left, List<int[]> right) {
        int i = 0, j = 0;
        int h1 = -1, h2 = -1;
        ArrayList<int[]> res = new ArrayList<>();
        while (i < left.size() && j < right.size()) {
            if (left.get(i)[0] < right.get(i)[0]) {
                h1 = left.get(i)[0];
                int[] newpoint = {left.get(i)[1], Math.max(h1, h2)};
                if (res.isEmpty() || res.get(res.size() - 1)[1] != newpoint[1])
                    res.add(newpoint);
                i++;
            } else if (right.get(i)[0] < left.get(i)[0]) {
                h2 = right.get(i)[0];
                int[] newpoint = {right.get(j)[1], Math.max(h1, h2)};
                if (res.isEmpty() || res.get(res.size() - 1)[1] != newpoint[1])
                    res.add(newpoint);
                j++;
            } else {
                h1 = left.get(i)[0];
                h2 = right.get(i)[0];
                int[] newpoint = {left.get(i)[1], Math.max(h1, h2)};
                if (res.isEmpty() || res.get(res.size() - 1)[1] != newpoint[1])
                    res.add(newpoint);
                j++;
                i++;
            }
        }
        while (i < left.size()) {
            if (res.isEmpty() || res.get(res.size() - 1)[1] != left.get(i)[1])
                res.add(left.get(i));
            i++;
        }
        while (j < right.size()) {
            if (res.isEmpty() || res.get(res.size() - 1)[1] != right.get(j)[1])
                res.add(right.get(j));
            j++;
        }
        return res;
    }

    public List<int[]> getSkyline(int[][] buildings) {
        List<int[]> res = new ArrayList<>();
        if (buildings.length == 0) return null;
        else if (buildings.length == 1) {
            int[] tmp = {buildings[0][0], buildings[0][2]};
            int[] tmp2 = {buildings[0][1], 0};
            res.add(tmp);
            res.add(tmp2);
            return res;
        } else {
            List<int[]> left = new ArrayList<>(), right = new ArrayList<>();
            for (int i = 0; i < buildings.length; i++) {
                if (i < buildings.length / 2) left.add(buildings[i]);
                else right.add(buildings[i]);
            }
            return merge(left, right);
        }
    }
}


public class Solution {
    static int li(int[] building) {
        return building[0];
    }

    static int ri(int[] building) {
        return building[1];
    }

    static int hi(int[] building) {
        return building[2];
    }

    static class SortedBuilds {
        int[][] buildings;
        int p = 0;

        PriorityQueue<int[]> inserted = new PriorityQueue<>((a, b) -> li(a) - li(b));

        SortedBuilds(int[][] buildings) {
            this.buildings = buildings;
        }

        boolean hasNext() {
            return p < buildings.length || !inserted.isEmpty();
        }


        int[] next() {

            if (p < buildings.length && !inserted.isEmpty()) {

                if (li(buildings[p]) < li(inserted.peek())) {
                    return buildings[p++];
                } else {
                    return inserted.poll();
                }

            } else if (p < buildings.length) {
                return buildings[p++];
            } else { // !inserted.isEmpty())
                return inserted.poll();
            }

        }

        void insert(int[] building) {
            inserted.add(building);
        }
    }

    public List<int[]> getSkyline(int[][] buildings) {

        List<int[]> all = new ArrayList<>();
        if (buildings.length == 0) return all;

        SortedBuilds sortedBuilds = new SortedBuilds(buildings);

        int[] a = sortedBuilds.next();

        while (sortedBuilds.hasNext()) {
            int[] b = sortedBuilds.next();

            if (ri(a) == li(b) && hi(a) == hi(b)) {
                a = new int[]{li(a), ri(b), hi(a)};
                continue;
            }

            // a.r b.l
            if (ri(a) <= li(b)) {
                all.add(new int[]{li(a), hi(a)});

                if (ri(a) < li(b)) {
                    all.add(new int[]{ri(a), 0});
                }

                a = b;
                continue;
            }

            // a.l b.l
            if (li(a) == li(b)) {

                // make a higher than b
                if (hi(a) < hi(b)) {
                    sortedBuilds.insert(a);
                    a = b;
                    continue;
                }

                if (ri(a) < ri(b)) {
                    sortedBuilds.insert(new int[]{ri(a), ri(b), hi(b)});
                }
                // else drop b (b inside a)
                continue;
            }

            //
            if (hi(a) < hi(b)) {

                all.add(new int[]{li(a), hi(a)});

                if (ri(a) > ri(b)) {
                    sortedBuilds.insert(new int[]{ri(b), ri(a), hi(a)});
                }

                a = b;
                continue;
            }

            // a.h >= b.h

            if (ri(a) < ri(b)) {
                sortedBuilds.insert(new int[]{ri(a), ri(b), hi(b)});
            }
            // else drop b (b inside a)
        }

        all.add(new int[]{li(a), hi(a)});
        all.add(new int[]{ri(a), 0});

        return all;
    }
}
