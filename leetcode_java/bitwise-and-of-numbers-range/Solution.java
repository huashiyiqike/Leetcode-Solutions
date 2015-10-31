public class Solution {
    public int maxbit(int n) {
        int tmp = n, count = 0;
        while (tmp > 0) {
            tmp >>= 1;
            count++;
        }
        return count;
    }

    public int rangeBitwiseAnd(int m, int n) {
        if (maxbit(m) != maxbit(n)) return 0;
        int res = 0, count = maxbit(m) - 1;
        while (count >= 0 && (m & (1 << count)) == (n & (1 << count))) {
            res |= (m & (1 << count));
            count--;
        }
        return res;
    }
}

public class Solution {
    public int rangeBitwiseAnd(int m, int n) {
        int c = 0;
        while (m != n) {
            m >>= 1;
            n >>= 1;
            ++c;
        }
        return n << c;
    }
}

public class Solution {

    static final int SIZE = Integer.SIZE;

    static final long[] POW = new long[SIZE + 1];

    static {
        for (int i = 0; i < SIZE; i++) {
            POW[i] = (long) Math.pow(2, i);
        }
    }

    public int rangeBitwiseAnd(int m, int n) {

        for (int i = SIZE; i > 0; i--) {
            if (POW[i - 1] <= m && m < POW[i]) {
                if (POW[i - 1] <= n && n < POW[i]) {
                    long p = POW[i - 1];
                    return (int) p | rangeBitwiseAnd((int) (m & (p - 1)), (int) (n & (p - 1)));
                }
            }
        }

        return 0;
    }
}
