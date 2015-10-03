public class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        while(m > 0 && n > 0){
            if(nums1[m-1] > nums2[n-1]){
                nums1[m+n-1] = nums1[m-1];
                m--;
            }else{
                nums1[m+n-1] = nums2[n-1];
                n--;
            }
        }
        while(n > 0){
            nums1[n-1] = nums2[n-1];
            n--;
        }
    }
}

public class Solution {
    
    int safe(int X[], int i){
        if(i < 0) return Integer.MIN_VALUE;
        
        return X[i]; 
    }
    
    public void merge(int A[], int m, int B[], int n) {
        
        int t = A.length - 1;
        
        int pa = m - 1;
        int pb = n - 1;
        
        while(t >= 0){
            
            int a = safe(A, pa);
            int b = safe(B, pb);
            
            if(a > b){
                A[t] = a;
                pa--;
            }else{
                A[t] = b;
                pb--;
            }
            
            t--;
        }
        
    }
}
