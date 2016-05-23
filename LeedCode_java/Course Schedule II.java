/*
There are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

For example:

2, [[1,0]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1]

4, [[1,0],[2,0],[3,1],[3,2]]
There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0. So one correct course order is [0,1,2,3]. Another correct ordering is[0,2,1,3].
*/

public class Solution {
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        if(numCourses==0||prerequisites==null){//非法输入
            return new int[0];
        }
         int len=prerequisites.length;
         int[] result=new int[numCourses];
         if(len==0){
              for(int i=0;i<numCourses;i++){
                 result[i]=i; 
              }
         }
        LinkedList <Integer>list=new <Integer>LinkedList();  
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
        result[j++]=c;
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
        return result;
    }
    return new int[0];
        
    }
}