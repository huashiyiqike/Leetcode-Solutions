/**
 * @param {number} x
 * @return {number}
 */
var reverse = function(x) {
    var sign = 1;
    if(x < 0){
        sign = -1;
        x = -x;
    }
    var res = 0;
    while(x > 0){
        res *= 10;
        res += x % 10;
        x = Math.floor(x / 10);
        if(res > Math.pow(2, 31) - 1) return 0;
    }
    return res*sign;
};