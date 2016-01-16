/**
 * @param {number} n
 * @return {number}
 */
var nthUglyNumber = function(n) {
    var res = [1], cur = idx2 = idx3 = idx5 = 0;
    while(cur < n-1){
        res[++cur] = Math.min(res[idx2]*2, res[idx3]*3, res[idx5]*5);
        if(res[idx2]*2 === res[cur]) idx2++;
        if(res[idx3]*3 === res[cur]) idx3++;
        if(res[idx5]*5 === res[cur]) idx5++;
    }
    return res[n-1];
};
document.writeln(nthUglyNumber(7));