public class Solution {
    public int hIndex(int[] citations) {
        int left = 0, right = citations.length - 1;
        while(left <= right){
            int mid = (left + right) / 2;
            if(citations[mid] < citations.length - mid) left = mid + 1;
            else if(citations[mid] > citations.length - mid) right = mid - 1;
            else return citations.length - mid;
        }
        return citations.length - (right + 1);
    }
}