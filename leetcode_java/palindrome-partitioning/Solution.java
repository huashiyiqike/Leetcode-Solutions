import java.util.*;

public class Solution{
    public boolean ispal(String a){
        for(int i = 0; i < a.length()/2;i++){
            if(a.charAt(i) != a.charAt(a.length() -1 - i)) return false;
        }
        return true;
    }
    public void helper(List<List<String>> res, List<String> path, String s, int idx) {
        for(int i = idx+1; i < s.length()+1; i++){
            String tmp = s.substring(idx, i);
            if(ispal(tmp)){
                List<String> newpath = new LinkedList<>(path);
                newpath.add(tmp);
                if(i != s.length())
                    helper(res, newpath, s, i);
                else res.add(newpath);
            }
        }
    }
    public List<List<String>> partition(String s) {
        List<String> path= new LinkedList<>();
        List<List<String>> res = new LinkedList<>();
        helper(res, path, s, 0);
        return res;
    }
}

public class Solution {
    
    boolean isPal(String s){

        char[] S = s.toCharArray();

        for(int i = 0; i < S.length / 2; i++){
            if(S[i] != S[S.length - i - 1])
                return false;
        }

        return true;
    }
    

    
    public List<List<String>> partition(String s) {

        List<List<String>> rt = new ArrayList<List<String>>();

        if("".equals(s)) return rt;
        if(s.length() == 1) return Arrays.asList(Arrays.asList(s));
        
        for(int i = 0; i < s.length(); i++){
            String x = s.substring(0, i + 1);
            if(isPal(x)){
                List<List<String>> sub = partition(s.substring(i + 1));

                if(sub.isEmpty()){
                    rt.add(Arrays.asList(x));
                } else {
                    for(List<String> l : sub){
                        ArrayList<String> _l = new ArrayList<String>();
                        _l.add(x);
                        _l.addAll(l);
                        rt.add(_l);
                    }
                }
            }
        }
        
        return rt;
        
    }
}