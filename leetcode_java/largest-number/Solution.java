
import java.util.*;

public class Solution {
    public String largestNumber(int[] nums) {
        List<String> lists = new LinkedList<>();
        for(int i:nums) lists.add(String.valueOf(i));
        Collections.sort(lists, new Comparator<String>() {
            @Override
            public int compare(String o1, String o2) {
                return -(o1 + o2).compareTo(o2 + o1); // from large to small
            }
        });
        String res = "";
        for(String s: lists) res += s;
        return res.charAt(0) == '0' ? "0":res;
    }
}

public class Solution {
    public String largestNumber(int[] num) {
        String[] ns = Arrays.stream(num)
                .mapToObj(Integer::toString)
                .sorted((x, y) -> (y + x).compareTo(x + y))
                .toArray(String[]::new);

        if ("0".equals(ns[0])) return "0";

        return String.join("", ns);
    }
}
