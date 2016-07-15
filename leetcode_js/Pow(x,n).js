/**
 * @param {number} x
 * @param {number} n
 * @return {number}
 */
function myPow(x, n) {
    var res = 1, m = Math.abs(n);
    while (m > 0) {
        if ((m & 1) != 0) {
            res *= x;
        }
        m >>>= 1; // unsigned shift
        x *= x;
    }
    if (n < 0) {
        res = 1 / res;
    }
    return res;
}
