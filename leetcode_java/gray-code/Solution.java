public class Solution {
    public List<Integer> grayCode(int n) {
        List<Integer> res = new ArrayList<>();
        res.add(0);
        if (n == 0) return res;

        for (int i = 0; i < n; i++) {
            List<Integer> tmp = new ArrayList<>(res);
            Collections.reverse(tmp);
            for (int ii : tmp) {
                res.add(ii + (1 << i));
            }
        }
        return res;
    }
}

public class Solution {
    public List<Integer> grayCode(int n) {

        return IntStream.range(0, (int) Math.pow(2, n))
                .map(i -> (i >> 1) ^ i)
                .boxed()
                .collect(Collectors.toList());

    }
}
