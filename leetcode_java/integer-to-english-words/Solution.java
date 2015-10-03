public class Solution {
    public String numberToWords(int num) {
        String[] to19 = ("One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve" +
                "Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen").split(" ");
        String[] tens = "Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety".split(" ");
        String[] div = "Thousand Million Billion".split(" ");

        if(num < 20)
            return to19[num-1];
        else if(num < 100)
            return tens[num/10 - 2] + (num % 10 == 0?"":to19[num%10 - 1]);
        else if(num < 1000)
            return to19[num/100 - 1] + " Hundred" + (num % 100 == 0? "":numberToWords(num%100));
        else{
            String res = " ";
            for(int i = 0; i < 3 && num > 0; i++){
                res = " " + numberToWords(num%1000) + div[i] + res;
                num /= 1000;
            }
            return res;
        }
    }
}