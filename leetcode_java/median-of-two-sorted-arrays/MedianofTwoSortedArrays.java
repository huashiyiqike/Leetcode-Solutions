public class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int len1 = nums1.length;
        int len2 = nums2.length;
        if((len1 + len2 ) % 2 == 1){
            return findMid(nums1 , nums2 , 0 , len1 - 1 , 0 ,len2 - 1 , (len1 + len2)/2);
        }else{
            return (findMid(nums1 , nums2 , 0 , len1 - 1, 0 ,len2 - 1 , (len1 + len2)/2) + findMid(nums1 , nums2 , 0 , len1 - 1, 0 ,len2 - 1 , (len1 + len2)/2-1))*0.5;
        }
    }
    public double findMid(int[] nums1, int[] nums2 , int start1 ,int end1 ,int start2 ,int end2 ,int k) {
        int len1 = end1 - start1 + 1;
        int len2 = end2 - start2 + 1;
        if(len1 == 0){
            return nums2[k + start2];
        }
        if(len2 == 0){
            return nums1[k + start1];
        }
        if( k == 0){
            return nums1[start1] < nums2[start2] ? nums1[start1] : nums2[start2];
        }
        int mid1 = len1*k/(len1 + len2);
        int mid2 = k - mid1 -1;
        mid1 = mid1 + start1;
        mid2 = mid2 + start2;
        if(nums1[mid1] > nums2[ mid2]){
           k = k - (mid2 - start2 + 1);
           start2 = mid2 + 1;
           end1 = mid1 ;
           
        }else {
            k = k - (mid1 - start1 + 1);
           start1 = mid1 + 1;
           end2 = mid2 ;
        }
        return findMid(nums1 , nums2 , start1 , end1 , start2 , end2 , k);
    }
}