import java.util.*;

public class Solution {
    public int[] plusOne(int[] digits) {
        if(digits == null || digits.length == 0){
            return new int[0];
        }

        for(int i = digits.length - 1; i >= 0; i--){
            if(digits[i] < 9){
                digits[i]++;
                return digits;
            }else{
                digits[i] = 0;
            }
        }

        int[] result = new int[digits.length + 1];
        result[0] = 1;

        return result;
    }
//    public int[] plusOne(int[] digits) {
//        List<Integer> res = new ArrayList<Integer>();
//        for(int i = 0; i < digits.length; i++) res.add(digits[i]);
//        Collections.reverse(res);
//        int carry = 1;
//        for(int i = 0; i < res.size(); i++){
//            if(carry == 1){
//                int tmp = res.get(i) + 1;
//                carry = tmp / 10;
//                res.set(i, tmp % 10);
//            }else break;
//        }
//        if(carry == 1) res.add(carry);
//        Collections.reverse(res);
//        int[] tmp = new int[res.size()];
//        for(int i = 0; i < res.size(); i++) tmp[i] = res.get(i);
//        return tmp;
//    }
}

public class Solution {
    public int[] plusOne(int[] digits) {
        // IMPORTANT: Please reset any member data you declared, as
        // the same Solution instance will be reused for each test case.
        int[] result = new int[digits.length + 1];
        digits[digits.length - 1] += 1;
        for(int i = digits.length - 1; i >=0 ; i--){
            result[ i + 1 ] += digits[i];
            result[ i ] += result[ i + 1 ] / 10;
            result[ i + 1 ] %= 10;
        }
        
        if(result[0] == 0) return Arrays.copyOfRange(result, 1 , result.length);
        else
        return result; 
    }
}