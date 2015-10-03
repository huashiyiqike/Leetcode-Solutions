import java.util.*;
public class Solution {
    public int hIndex(int[] citations) {
        Arrays.sort(citations);
        for(int i = 0 ; i < citations.length/2; i++){
            int tmp = citations[i];
            citations[i] = citations[citations.length-i-1];
            citations[citations.length-i-1] = tmp;
        }
        for(int i = 1; i <= citations.length; i++){
            if(citations[i-1] < i) return i - 1;
        }
        return citations.length;
    }
}
