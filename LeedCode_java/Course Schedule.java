/*
There are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

For example:

2, [[1,0]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0. So it is possible.

2, [[1,0],[0,1]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
*/

public class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        LinkedList <Integer>list=new <Integer>LinkedList();  
        if(prerequisites==null){
            return false;
        }
        if(numCourses==0||prerequisites.length==0){
            return true;
        }
    int len=prerequisites.length;
    int[] count=new int[numCourses];
     for(int i=0;i<numCourses;i++){
        count[i]=0;
    }
    for(int i=0;i<len;i++){
        count[prerequisites[i][0]]++;
    }
      for(int i=0;i<numCourses;i++){
        if(count[i]==0){
            list.add(i);
        }
    }
    int numNoPre=list.size();
    int j=0;
    while(list.size()>0){
        int c=list.remove();
     //   result[j++]=c;
         for(int i=0;i<len;i++){
             if(prerequisites[i][1]==c){
                count[prerequisites[i][0]]--;
                if(count[prerequisites[i][0]]==0){
                     list.add(prerequisites[i][0]);
                     numNoPre++;
                }
             }
         }
    }
    if(numNoPre==numCourses){
        return true;
    }
    return false;
    }
}