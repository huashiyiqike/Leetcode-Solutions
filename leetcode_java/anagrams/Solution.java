import java.util.*;

public class Solution {
    public List<String> anagrams(String[] strs) {
        Map<String, List<String>> map = new HashMap<>();
        for (String i : strs) {
            String keys;
            char[] tmp = i.toCharArray();
            Arrays.sort(tmp);
            keys = new String(tmp);

            List<String> tmplist;
            if (map.containsKey(keys)) {
                tmplist = map.get(keys);
            } else {
                tmplist = new ArrayList<>();
            }
            tmplist.add(i);
            map.put(keys, tmplist);
        }

        List<String> res = new ArrayList<>();
        for (String i : map.keySet()) {
            List<String> tmplist2 = map.get(i);
            if (tmplist2.size() > 1)
                res.addAll(tmplist2);
        }

        return res;
    }
}

public class Solution {
    public List<String> anagrams(String[] strs) {
        return Arrays.stream(strs)
                .collect(Collectors.groupingBy(
                        k -> {
                            char[] w = k.toCharArray();
                            Arrays.sort(w);
                            return new String(w);
                        }
                ))
                .values()
                .stream()
                .filter(v -> v.size() > 1)
                .flatMap(v -> v.stream())
                .collect(Collectors.toList());
    }
}
