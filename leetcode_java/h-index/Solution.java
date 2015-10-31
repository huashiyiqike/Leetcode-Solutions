import java.util.*;
import java.util.Arrays;
import java.util.Collections;

public class Solution {
    public int hIndex(int[] citations) {
        Arrays.sort(citations);
        int i;
        for (i = 0; i < citations.length; i++)
            if (citations[i] >= citations.length - i)
                break;
        return citations.length - i;

        // reverse
//        for(int i = 0 ; i < citations.length/2; i++){
//            int tmp = citations[i];
//            citations[i] = citations[citations.length-i-1];
//            citations[citations.length-i-1] = tmp;
//        }
//        for(int i = 1; i <= citations.length; i++){
//            if(citations[i-1] < i) return i - 1;
//        }
//        return citations.length;
    }
}


//The idea is to see that the result can only range from 0 to the length
// of the array (because we can't have h-index greater than the total papers
// published). So we create an array "arr" which acts like a HashMap (using
// pigeon hole principle) and loop backwards from the highest element, then we
// find "tot" which is the total number of papers that has more than i citations,
// and we stop when tot>=i (total number of papers with more than i citations >= i).
// We don't need to keep going because we are trying the biggest i possible,
// we stop and return the result.

public class Solution {
    public int hIndex(int[] citations) {
        int n = citations.length, tot = 0;
        int[] arr = new int[n + 1]; // n+1
        for (int i = 0; i < n; i++) {
            if (citations[i] >= n) arr[n]++;
            else arr[citations[i]]++;
        }
        for (int i = n; i >= 0; i--) {
            tot += arr[i];
            if (tot >= i) return i;
        }
        return 0;
    }
}
