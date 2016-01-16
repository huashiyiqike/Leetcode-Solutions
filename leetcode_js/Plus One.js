/**
 * @param {number[]} digits
 * @return {number[]}
 */
var plusOne = function(digits) {
    digits = digits.reverse();
    var inc = 1;
    for(var i = 0; i < digits.length; i++){
        digits[i] += inc;
        inc = Math.floor(digits[i] / 10);
        digits[i] %= 10;
    }
    if(inc > 0) digits = digits.concat(1);
    return digits.reverse();
};