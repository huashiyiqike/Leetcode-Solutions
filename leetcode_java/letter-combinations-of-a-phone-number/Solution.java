public class Solution {
     HashMap<Integer , String> map = new HashMap<Integer , String>();
    public List<String> letterCombinations(String digits) {
        List<String> result = new ArrayList<String>();
        if(digits == null || digits.length() == 0){
            return result ;
        }
        map.put(2 ,"abc");
        map.put(3 ,"def");
        map.put(4 ,"ghi");
        map.put(5 ,"jkl");
        map.put(6 ,"mno");
        map.put(7 ,"pqrs");
        map.put(8 ,"tuv");
        map.put(9 ,"wxyz");
        combin( result ,digits ,0, "");
         return result;
    }
     public void combin(List<String> result , String digits , int position ,String temp){
         if(position == digits.length()){
             result.add(temp);
             return ;
         }
         String str = map.get(digits.charAt(position) - '0');
         int len = str.length();
         for(int i = 0 ;i < len ; i++){
             combin(result , digits , position + 1 , temp+str.charAt(i));
         }
     }
}

public class Solution {
    static final char[][] CHAR_MAP = {
            {}, // 0
            {}, // 1
            { 'a', 'b', 'c'}, //2
            { 'd', 'e', 'f'}, //3
            { 'g', 'h', 'i'}, //4
            { 'j', 'k', 'l'}, //5
            { 'm', 'n', 'o'}, //6
            { 'p', 'q', 'r', 's'}, //7
            { 't', 'u', 'v'}, //8
            { 'w', 'x', 'y', 'z'}, //9
    };
    public void helper(char[] num, int start, List<String> res, String path){
        if(start == num.length){
            res.add(path);
            return;
        }
        char[] tmp = CHAR_MAP[(int)num[start]-(int)'0'];
        for(int i = 0; i < tmp.length; i++){
            String newpath = path + tmp[i];
            helper(num, start+1, res, newpath);
        }
    }
    public List<String> letterCombinations(String digits) {
        if(digits.equals("")) return new ArrayList<>();
        char[]  num = digits.toCharArray();
        List<String> res = new ArrayList<>();
        helper(num, 0, res, "");
        return res;
    }
}
public class Solution {
    
    static final char[][] CHAR_MAP = {
        {}, // 0
        {}, // 1
        { 'a', 'b', 'c'}, //2
        { 'd', 'e', 'f'}, //3
        { 'g', 'h', 'i'}, //4
        { 'j', 'k', 'l'}, //5
        { 'm', 'n', 'o'}, //6
        { 'p', 'q', 'r', 's'}, //7
        { 't', 'u', 'v'}, //8
        { 'w', 'x', 'y', 'z'}, //9
    };    

    ArrayList<String> rt;
    char[] stack;

    void find(char[] digits, int p){
        
        if(p == digits.length){
            rt.add(new String(stack));
        }else{
            
            int num = (int) (digits[p] - '0');
            
            for(char pc : CHAR_MAP[num]){
                stack[p] = pc;
                find(digits, p + 1);
            }
        }
    }    
    
    public List<String> letterCombinations(String digits) {
        
        rt = new ArrayList<>();
        stack = new char[digits.length()];
        
        find(digits.toCharArray(), 0);
        return rt;
    }
}
