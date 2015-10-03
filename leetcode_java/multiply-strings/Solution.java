import java.util.*;

public class Solution {
    int convert(char a){
        return (int)a - (int)'0';
    }
    public String multiply(String num1, String num2) {
        int[] res = new int[num1.length() + num2.length()];
        for(int i = num1.length()-1; i > 0; i--){
            for(int j = num2.length()-1; j > 0; j--){
                res[i+j+1] += convert(num1.charAt(i))
                        * convert(num2.charAt(j));
            }
        }
        int carry = 0;
        char[] reschar = new char[res.length];
        for(int i = res.length-1; i > 0; i--){
            res[i] += carry;
            carry = res[i] / 10;
            res[i] %= 10;
            reschar[i] = (char)(res[i]+(int)'0');
        }
        int start = 0;
        while(start+1 < res.length && res[start] == 0){start++;}
        return new String(Arrays.copyOfRange(reschar, start, reschar.length);
//        StringBuilder sb = new StringBuilder();
//        for (int num : products) sb.append(num);
//        while (sb.length() != 0 && sb.charAt(0) == '0') sb.deleteCharAt(0);
//        return sb.length() == 0 ? "0" : sb.toString();
    }
}

public class Solution {
    public String multiply(String num1, String num2) {
        
        int[] paper = new int[num1.length() + num2.length()];
        
        Arrays.fill(paper, 0);
        
        char[] _num1 = num1.toCharArray(); 
        char[] _num2 = num2.toCharArray();
        
        for (int i = 0; i < _num2.length; i++) {
            for (int j = 0; j < _num1.length; j++) {
                paper[paper.length - (i + j + 2)] += (_num1[j] - '0') * (_num2[i] - '0');
            }
        }


        // add

        for (int i = 0; i < paper.length - 1; i++) {
            paper[i + 1] += paper[i] / 10;
            paper[i] %= 10;

        }

        String s = "";
        for(int i = paper.length - 1; i > 0 ; i--){

            if(paper[i] == 0 && "".equals(s))
                continue;

            s += paper[i];
        }

        s += paper[0];
        

        return s;
        
    }
}