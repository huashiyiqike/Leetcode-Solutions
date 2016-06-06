
import java.lang.reflect.Array;
import java.util.*;

public class Solution {
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        if(numCourses == 0 || prerequisites == null){//非法输入
            return new int[0];
        }
         int len = prerequisites.length;
         int[] result = new int[numCourses];
         if(len == 0){
              for(int i = 0;i < numCourses; i++){
                 result[i] = i; 
              }
         }
        LinkedList <Integer> list = new <Integer>LinkedList();  
    int[] count = new int[numCourses];
     for(int i = 0;i < numCourses; i++){
        count[i] = 0;
    }
    for(int i = 0;i < len; i++){
        count[prerequisites[i][0]]++;
    }
      for(int i = 0;i <numCourses ; i++){
        if(count[i] == 0){
            list.add(i);
        }
    }
    int numNoPre = list.size();
    int j = 0;
    while(list.size() > 0){
        int c = list.remove();
        result[j++] = c;
         for(int i = 0;i < len; i++){
             if(prerequisites[i][1] == c){
                count[prerequisites[i][0]]--;
                if(count[prerequisites[i][0]] == 0){
                     list.add(prerequisites[i][0]);
                     numNoPre++;
                }
             }
         }
    }
    if(numNoPre == numCourses){
        return result;
    }
    return new int[0];
        
    }
}