public class Solution {
    public int[] searchRange(int[] nums, int target) {
        int l = 0, r = nums.length - 1;
        int[] res = {-1, -1};
        while(l <= r){
            int mid = l + (r - l)/2;
            if(nums[mid] >= target) r = mid - 1;
            else l = mid + 1;
        }
        res[0] = r+1;

        l = r+1;
        r = nums.length - 1;
        while(l <= r){
            int mid = l + (r - l)/2;
            if(nums[mid] <= target) l = mid + 1;
            else r = mid - 1;
        }
        res[1] = l - 1;
        if(res[0] > res[1]){
            res[0] = -1;
            res[1] = -1;
            return res;
        }
        return res;
    }
}

public class Solution {
    public int[] searchRange(int[] A, int target) {
        
        int s = 0, e = A.length;
        
        while( s < e ){
            int mid = (s + e) / 2;
            
            if(A[mid] == target){
                
                int _s = mid, _e = mid;
                
                while(_s - 1 >= 0       && A[_s - 1] == target) _s--;
                while(_e + 1 < A.length && A[_e + 1] == target) _e++;
                
                return new int[]{_s, _e};
                
            }else if(A[mid] < target){
                s = mid + 1;
            }else if(A[mid] > target){
                e = mid;
            }
            
        }
        
        return new int[]{-1, -1};
        
    }
}