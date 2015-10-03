public class Solution {
  public int majorityElement(int[] nums) {
    int count = 1, cur = nums[0];
    for(int i = 1; i < nums.length; i++){
      if(nums[i] == cur) count++;
      else{ count--;
        if(count < 0){
          count = 0;
          cur = nums[i];
        }
      }
    }
    return cur;
  }
}

public class Solution {
  public int majorityElement(int[] num) {
    int m = num[0];
    int c = 1;

    for(int i = 1; i < num.length; i++){
      if(num[i] == m){
        c++;
      }else if (c > 1){
        c--;
      }else{ // c == 1 && num[i] != m
        m = num[i];
      }
    }

    return m;
  }
}
