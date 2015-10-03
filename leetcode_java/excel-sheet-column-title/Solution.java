
public class Solution {
  public String convertToTitle(int n) {
    String res = "";
    char tmp;
    while(n > 0){
      n -= 1;
      tmp = (char)('A' + n % 26);
      res = tmp + res;
      n /= 26;
    }
    return res;
  }
};
public class Solution {
  public String convertToTitle(int n) {
    if(n < 27){
      return (char)('A' + (n - 1)) + "";
    }

    if( n % 26 == 0) {
      return convertToTitle(n / 26 - 1) + 'Z';
    }

    return convertToTitle(n / 26) + convertToTitle(n % 26);
  }
}
