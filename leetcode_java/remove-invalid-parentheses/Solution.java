public class Solution {
    public List<String> removeInvalidParentheses(String s) {
        List<String> result = new ArrayList<String>();
        dfs(result,0,0,s,new char[]{'(',')'});
        return result;
    }
    public void dfs(List<String> result,int flag_i,int flag_j,String s,char[] word){
        int len = s.length();
        for(int stack = 0,i = flag_i;i < len;++i){
            if(s.charAt(i) == word[0]) stack++;
            if(s.charAt(i) == word[1]) stack--;
            if(stack >= 0) continue;
            for(int j = flag_j;j <= i;++j){
                if((s.charAt(j) == word[1]) && (j == flag_j || s.charAt(j-1)!=word[1])){
                    dfs(result,i,j,s.substring(0,j)+s.substring(j+1,len),word);
                }
            }
             return ;
        }
            String reverse = new StringBuilder(s).reverse().toString();
            if(word[0] == '('){
                dfs(result,0,0,reverse,new char[]{')','('});
            }else{
                result.add(reverse);
            }
        }
}