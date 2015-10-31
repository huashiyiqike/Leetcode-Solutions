public class Solution {
    public void helper(List<String> res, String path, int left, int right, int n){
        if(right > left || right > n || left > n) return;
        if(left == right && left == n){
            res.add(path);
            return;
        }
       // String newpathleft = path+"(", newpathright = path + ")";
        helper(res, path + ")", left, right+1, n);
        helper(res, path+"(", left+1, right, n);
    }
    public List<String> generateParenthesis(int n) {
        int left = 0, right = 0;
        List<String> res = new ArrayList<>();
        helper(res,"",0,0,n);
        return res;
    }
}
public class Solution {
    public List<String> generateParenthesis(int n) {
        
        if (n == 0) return new ArrayList<String>();
        if (n == 1) return Arrays.asList(new String[]{"()"});
        
        HashSet<String> temp = new HashSet<String>();
        
        for(String s : generateParenthesis(n - 1)){
            temp.add("(" + s + ")");
            temp.add("()" + s);
            temp.add(s + "()");
        }
        
        for(int i = 2; i < n - 1 ; i++){
            for(String s : generateParenthesis(n - i)){
                for(String ss : generateParenthesis(i)){

                    temp.add(ss + s);
                    temp.add(s + ss);
                }

            }
        }
        
        return new ArrayList<String>(temp);
    }
}
