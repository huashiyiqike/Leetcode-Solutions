import java.util.*;
public class Solution {
    public void sortColors(int[] nums) {
        int zero = -1, two = nums.length, cur = 0;
        while(cur < two){
            if(nums[cur] == 0){
                zero++;
                nums[cur] = nums[zero];
                nums[zero] = 0;
                if(zero >= cur) cur = zero+1;
            }
            else if (nums[cur] == 2){
                two--;
                nums[cur] = nums[two];
                nums[two] = 2;
            }
            else cur++;
        }
    }
}

public class Solution {
    
    void swap(int[] A, int i, int j){
        int t = A[i];
        A[i] = A[j];
        A[j] = t;
    }
     
    public void sortColors(int[] A) {
        
        int red = 0;
        int blue = A.length - 1;
        
        int white = 0;
        
        while( white <= blue ){
            
            if(A[white] == 0){ // red 
                swap(A, white, red);
            
                red++;
                white++;
            }else if(A[white] == 1){ // white
                
                white++;
                
            }else if (A[white] == 2) { //blue
                
                swap(A, white, blue);
                
                blue--;
            }
        }
        
    }
}
