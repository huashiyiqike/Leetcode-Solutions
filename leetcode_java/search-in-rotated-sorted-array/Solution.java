public class Solution {
    public int search(int[] nums, int target) {
        int l = 0, r = nums.length - 1;
        while(l <= r) {
            int mid = l + (r - l) / 2;
            if (nums[mid] == target) return mid;

            if (nums[mid] > nums[r]) {
                if(target >= nums[l] && target < nums[mid]) r = mid - 1;
                else l = mid + 1;
//                if (target > nums[mid]) l = mid + 1;
//                else {
//                    if (target > nums[r]) r = mid - 1;
//                    else l = mid + 1;
//                }
            } else if (nums[mid] <= nums[r]) {
                if(target <= nums[r] && target > nums[mid]) l = mid + 1;
                else r = mid - 1;
//                if (target > nums[mid]) {
//                    if (target > nums[r]) r = mid - 1;
//                    else l = mid + 1;
//                } else r = mid - 1;
            }
        }
        if(nums[l] == target) return l;
        return -1;
    }
}


public class Solution {
    public int search(int[] nums, int target) {
        int l = 0, r = nums.length-1;
        while(l <= r){
            int mid = r+(l-r)/2;
            if(nums[mid] < nums[r]){
                if(target > nums[mid]) {
                    if (target < nums[r]) l = mid + 1;
                    else if(target > nums[r]) r = mid;
                }

                else if(target < nums[mid]) r = mid - 1;
                else return mid;
            }
            else if(nums[mid] > nums[r]){
                if(target > nums[mid]) l = mid + 1;
                else if(target < nums[mid])
            }
        }
    }
}

public class Solution {
    public int search(int[] A, int target) {
        // Note: The Solution object is instantiated only once and is reused by each test case.
        int s = 0;
        int e = A.length;
        
        while(s < e){
            int mid = (s + e) /2;
            
            if(A[mid] == target){
                return mid;
            }
            
            if(target < A[mid]){
                // normal in first half
                
                if(A[s] <= A[mid] && A[s] <= target){
                    e = mid;
                // abnormal    
                }else if(A[mid] <= A[e - 1]){
                    e = mid;
                }else {
                    s = mid + 1;
                }
                
            } else {
   
                // normal in last half
                
                if(A[mid] <= A[e - 1] && target <= A[e - 1]){
                    s = mid + 1;
                } else if(A[s] <= A[mid]) {
                    s = mid + 1;
                } else {
                    e = mid;
                }
   
            }
        }
        
        return -1;
    }
}