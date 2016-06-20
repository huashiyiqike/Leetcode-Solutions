public class Solution {
    public String reverseVowels(String s) {
        if(s==null||s.length()==0||s.length()==1){
                 return s;
             }
             int strLen=s.length();
             StringBuffer str=new StringBuffer(s);
             int i=0;
             int j=strLen-1;
             char temp;
             while(i<j){
            	 //System.out.println(i);
               while(i<j){
                    char c=Character.toLowerCase(str.charAt(i));
                   if(c=='a'||c=='e'||c=='i'||c=='o'||c=='u'){
                     break;
                 }
                 i++;
               }
               while(i<j){
                   char c=Character.toLowerCase(str.charAt(j));
                   if(c=='a'||c=='e'||c=='i'||c=='o'||c=='u'){
                     break;
                 }
                 j--;
               } 
               if(i!=j){
                   temp=str.charAt(i);
                   str.setCharAt(i,str.charAt(j));
                   str.setCharAt(j,temp);
                   i++;
                   j--;
               }
             } 
             //System.out.println(str.toString());
             return str.toString();
    }
}