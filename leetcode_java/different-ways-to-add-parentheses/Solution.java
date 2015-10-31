import java.lang.String;
import java.util.HashMap;
import java.util.List;

public class Solution {
    Map<String, List<Integer>> map = new HashMap<>();
    public List<Integer> diffWaysToCompute(String input) {
        List<Integer> res = new ArrayList<Integer>();
        for (int i = 0; i < input.length(); i++) {
            char c = input.charAt(i);
            if (c == '-' || c == '+' || c == '*') {
                List<Integer> al, bl;
                String a = input.substring(0, i);
                String b = input.substring(i + 1);
                if(map.containsKey(a)) al = map.get(a);
                else {
                    al = diffWaysToCompute(a);
                    map.put(a, al);
                }
                if(map.containsKey(b)) bl = map.get(b);
                else {
                    bl = diffWaysToCompute(b);
                    map.put(b, bl);
                }
                for (int x : al) {
                    for (int y : bl) {
                        if (c == '-') {
                            res.add(x - y);
                        } else if (c == '+') {
                            res.add(x + y);
                        } else if (c == '*') {
                            res.add(x * y);
                        }
                    }
                }
            }
        }
        if (res.size() == 0) res.add(Integer.valueOf(input));
        return res;
    }
}