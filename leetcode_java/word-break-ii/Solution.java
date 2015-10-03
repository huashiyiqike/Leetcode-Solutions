public class Solution {
    public void back(List<String> res, String path, int start,
                     Map<Integer, List<Integer>> backtrackmap, String s){
        if(start == 0){
            res.add(path);
            return;
        }
        List<Integer> l = backtrackmap.get(start);
        if(l == null) return;
        for(int i = 0; i < l.size(); i++){
            String newpath;
            if(start == s.length())
                newpath = s.substring(l.get(i), start);
            else
                newpath = s.substring(l.get(i), start) + " " + path;
            back(res, newpath, l.get(i), backtrackmap, s);
        }
    }
    public List<String> wordBreak(String s, Set<String> wordDict) {
        boolean[] dp = new boolean[s.length()+1];
        dp[0] = true;
        Map<Integer, List<Integer>> backtrackmap = new HashMap<>();
        for(int i = 0; i < s.length(); i++){
            for(int j = i+1; j <= s.length(); j++){
                String tmp = s.substring(i,j);
                if(dp[i] && wordDict.contains(tmp)) {
                    dp[j] = true;
                    List<Integer> l;
                    if(backtrackmap.containsKey(j))
                        l = backtrackmap.get(j);
                    else
                        l = new ArrayList<>();
                    l.add(i);
                    backtrackmap.put(j, l);
                }
            }
        }
        List<String> res = new ArrayList<>();
        back(res, "", s.length(), backtrackmap, s);
        return res;
    }
}

public class Solution {
    
    ArrayList<Integer>[] P;
    char[] S;
    ArrayList<String> rt;
    
    void joinAll(int offset, LinkedList<String> parents){
        
        if(P[offset].isEmpty()){
            
            rt.add(String.join(" ", parents));
            return;
        }
        
        for(Integer p : P[offset]){
            
            parents.push(new String(S, p, offset - p));
            
            joinAll(p, parents);
            
            parents.pop();
        }
        
    }

    public List<String> wordBreak(String s, Set<String> dict) {
        S = s.toCharArray();

        P = new ArrayList[S.length + 1];
        P[0] = new ArrayList<Integer>();

        for(int i = 0; i < S.length; i++){
            for(int j = 0; j <= i; j++){
                String w = new String(S, j, i - j + 1);
                if(P[j] != null && dict.contains(w)){

                    if(P[i + 1] == null){
                        P[i + 1] = new ArrayList<Integer>();
                    }
                    
                    P[i + 1].add(j);
                }
            }
        }

        rt = new ArrayList<String>();
        
        if(P[S.length] != null){
            joinAll(S.length, new LinkedList<String>());
        }
        
        return rt;
    }
}
