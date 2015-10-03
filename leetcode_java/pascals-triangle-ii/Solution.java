import java.util.*;

public class Solution {
    public List<Integer> getRow(int rowIndex) {
        Integer[] res = new Integer[rowIndex+1];
        Arrays.fill(res, 0);
        res[0] = 1;
        for(int i = 1; i <= rowIndex; i++){
            for(int j = i; j > 0 ; j--){
                res[j] = res[j-1] + res[j];
            }
        }
        return Arrays.asList(res);
    }
}
public class Solution {
    public List<Integer> getRow(int rowIndex) {
        Integer[] row = new Integer[rowIndex + 1];
        
        Arrays.fill(row, 1);
        
        for(int i = 0 ; i < rowIndex - 1; i++){
            for(int j = i + 1; j >= 1; j--){
                row[j] = row[j] + row[j - 1];
            }
        }
        
        return Arrays.asList(row);
    }
}
