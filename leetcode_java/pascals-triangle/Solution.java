import java.util.*;

public class Solution {
    public List<List<Integer>> generate(int numRows) {
        if(numRows == 0) return new ArrayList<>();
        List<List<Integer>> res = new ArrayList<>();
        List<Integer> tmp = new ArrayList<>();
        tmp.add(1);
        res.add(tmp);
        for(int i = 1; i < numRows; i++){
            List<Integer> newtmp = new ArrayList<>();
            newtmp.add(1);
            for(int j = 0; j < tmp.size()-1; j++){
                newtmp.add(tmp.get(j)+tmp.get(j+1));
            }
            newtmp.add(1);
            res.add(newtmp);
            tmp = new ArrayList<>(newtmp);
        }
        return res;
    }
}
public class Solution {
    public List<List<Integer>> generate(int numRows) {
        
        ArrayList<List<Integer>> rt = new ArrayList<List<Integer>>();
        
        Integer[] prev = null;
        
        for(int i = 1 ; i <= numRows; i++){
            
            Integer[] row = new Integer[i];
            
            row[0] = 1;
            row[i - 1] = 1;
            
            for(int j = 1; j < i - 1 ; j++){
                //row.add(j, prev.get(j) + prev.get(j -1));
                row[j] = prev[j] + prev[j - 1];
            }
            
            rt.add(new ArrayList<Integer>(Arrays.asList(row)));
            prev = row;
        }
        
        
        return rt;
        
    }
}
