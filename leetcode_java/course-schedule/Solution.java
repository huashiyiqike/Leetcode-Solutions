import java.io.*;
import java.util.*;
public class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        int[] pre = new int[numCourses];
        List<List<Integer>> next = new ArrayList<>();
        for(int i = 0; i < numCourses; i++) next.add(new ArrayList<Integer>());
        Arrays.fill(pre, 0);
        for(int i = 0; i < prerequisites.length; i++){
            int from = prerequisites[i][1], to = prerequisites[i][0];
            pre[to]++;
            next.get(from).add(to);
        }
        int count = 0;
        Queue<Integer> queue = new LinkedList<>();
        for(int i = 0 ;i < numCourses ; i++) {
            if (pre[i] == 0) {
                queue.offer(i);
                count++;
            }
        }
        while(!queue.isEmpty()){
            int node = queue.poll();
            for(int i:next.get(node)){
                pre[i]--;
                if(pre[i] == 0){
                    queue.offer(i);
                    count++;
                }
            }
        }
        return count == numCourses;
    }
}

//http://blog.csdn.net/ljiabin/article/details/45846837
public class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        List<List<Integer>> posts = new ArrayList<List<Integer>>();
        for (int i = 0; i < numCourses; i++) {
            posts.add(new ArrayList<Integer>());
        }

        int[] preNums = new int[numCourses];
        for (int i = 0; i < prerequisites.length; i++) {
            posts.get(prerequisites[i][1]).add(prerequisites[i][0]);
            preNums[prerequisites[i][0]]++;
        }

        Queue<Integer> queue = new LinkedList<Integer>();
        for (int i = 0; i < numCourses; i++) {
            if (preNums[i] == 0){
                queue.offer(i);
            }
        }

        int count = numCourses;
        while (!queue.isEmpty()) {
            int cur = queue.poll();
            for (int i : posts.get(cur)) {
                if (--preNums[i] == 0) {
                    queue.offer(i);
                }
            }
            count--;
        }

        return count == 0;
    }
}

public class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        // init the adjacency list
        List<Set> posts = new ArrayList<Set>();
        for (int i = 0; i < numCourses; i++) {
            posts.add(new HashSet<Integer>());
        }

        // fill the adjacency list
        for (int i = 0; i < prerequisites.length; i++) {
            posts.get(prerequisites[i][1]).add(prerequisites[i][0]);
        }

        // count the pre-courses
        int[] preNums = new int[numCourses];
        for (int i = 0; i < numCourses; i++) {
            Set set = posts.get(i);
            Iterator<Integer> it = set.iterator();
            while (it.hasNext()) {
                preNums[it.next()]++;
            }
        }

        // remove a non-pre course each time
        for (int i = 0; i < numCourses; i++) {
            // find a non-pre course
            int j = 0;
            for ( ; j < numCourses; j++) {
                if (preNums[j] == 0) break;
            }

            // if not find a non-pre course
            if (j == numCourses) return false;

            preNums[j] = -1;

            // decrease courses that post the course
            Set set = posts.get(j);
            Iterator<Integer> it = set.iterator();
            while (it.hasNext()) {
                preNums[it.next()]--;
            }
        }

        return true;
    }
}


public class Solution {
    
    static class Vertex {
        
        int id;
        
        Vertex(int id){
            this.id = id;
        }
        
        Set<Integer> in  = new HashSet<>();
        Set<Integer> out = new HashSet<>();
        
        boolean isSink(){
            return out.isEmpty();
        }
    }
    
    Vertex safe(Vertex[] G, int id){
        if(G[id] == null){
            G[id] = new Vertex(id);
        }
        
        return G[id];
    }
    
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        
        Vertex[] G = new Vertex[numCourses];
        
        for(int[] p : prerequisites){
            safe(G, p[0]).out.add(p[1]);
            safe(G, p[1]).in.add(p[0]);
        }
        
        Set<Vertex> S = Arrays.stream(G)
                            .filter(v -> v != null)
                            .collect(Collectors.toSet());
        

        loop:
        while(!S.isEmpty()){
            
            for(Vertex v : S){
                if(v.isSink()){
                    S.remove(v);
                    
                    for(int i : v.in){
                        G[i].out.remove(v.id);
                    }
                    
                    continue loop;
                }
            }
            
            return false;
        }
        
        return true;
    }
}
