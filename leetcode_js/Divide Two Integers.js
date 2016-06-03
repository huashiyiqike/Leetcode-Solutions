/**
 * @param {number} dividend
 * @param {number} divisor
 * @return {number}
 */
var divide = function(dividend, divisor) {
    if(divisor == 0) return Infinity;
    var res = 0, add = 1, 
    neg = dividend * divisor < 0?-1:1;
    dividend = Math.abs(dividend);
    divisor = Math.abs(divisor);
    var div = divisor; 
    while(dividend >= divisor){
        while(dividend >= (div + div)){
            div += div; // << 31bit shift cause overflow
            add += add;
        } 
        dividend -= div;
        res += add;
        while(dividend < div){
            div >>= 1;
            add >>= 1;
        } 
    }
    res *= neg;
    res = Math.min(res , Math.pow(2 , 31) - 1);
    res = Math.max(res , - Math.pow(2 , 31)) 
    return res;
};