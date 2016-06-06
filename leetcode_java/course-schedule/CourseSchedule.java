public class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        LinkedList <Integer>list = new <Integer>LinkedList();  
        if(prerequisites == null){
            return false;
        }
        if(numCourses == 0||prerequisites.length == 0){
            return true;
        }
    int len = prerequisites.length;
    int[] count = new int[numCourses];
     for(int i = 0;i <numCourses; i++){
        count[i] = 0;
    }
    for(int i = 0;i < len; i++){
        count[prerequisites[i][0]]++;
    }
      for(int i = 0;i < numCourses; i++){
        if(count[i] == 0){
            list.add(i);
        }
    }
    int numNoPre = list.size();
    int j = 0;
    while(list.size()>0){
        int c = list.remove();
     //   result[j++]=c;
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
        return true;
    }
    return false;
    }
}