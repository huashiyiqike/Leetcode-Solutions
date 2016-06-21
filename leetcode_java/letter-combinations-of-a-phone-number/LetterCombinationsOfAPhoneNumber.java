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